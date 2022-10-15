from codemanip import code_utils

import srcmlcpp


# There are lots of other tests:
# - inside classes_tests.py (methods related tests)
# - inside template_tests.py (template related tests)
# - inside litgen


def test_functions():
    options = srcmlcpp.SrcmlcppOptions()

    f = srcmlcpp.srcmlcpp_main.code_first_function_decl(options, "Foo f();")
    assert f.return_type.typenames == ["Foo"]
    assert not f.is_static()
    assert not f.is_const()
    assert len(f.specifiers) == 0
    assert not f.is_template()
    assert not f.is_arrow_notation_return_type()

    f = srcmlcpp.srcmlcpp_main.code_first_function_decl(options, "static inline virtual Foo* f();")
    assert f.is_static()
    assert not f.is_operator()
    assert not f.is_template()
    assert not f.is_virtual_method()  # no parent struct here
    assert f.returns_pointer()


def test_arrow_return():
    options = srcmlcpp.SrcmlcppOptions()
    f = srcmlcpp.srcmlcpp_main.code_first_function_decl(options, "auto f() -> Foo;")
    assert f.return_type.typenames == ["auto", "Foo"]
    assert not f.is_static()
    assert not f.is_const()
    assert len(f.specifiers) == 0
    assert not f.is_template()
    assert f.is_arrow_notation_return_type()
    assert f.str_code() == "auto f() -> Foo;"

    f = srcmlcpp.srcmlcpp_main.code_first_function_decl(options, "auto f() {}")
    assert not f.is_arrow_notation_return_type()
    assert f.is_inferred_return_type()
    assert f.str_code() == "auto f()<unprocessed_block/>"


def test_operator():
    options = srcmlcpp.SrcmlcppOptions()
    # Call operator
    f = srcmlcpp.srcmlcpp_main.code_first_function_decl(options, "int operator()(int rhs);")
    assert f.is_operator()
    assert f.operator_name() == "()"
    assert f.return_type.str_code() == "int"
    # + operator
    f = srcmlcpp.srcmlcpp_main.code_first_function_decl(options, "int operator+(int rhs);")
    assert f.is_operator()
    assert f.operator_name() == "+"
    assert f.return_type.str_code() == "int"
    # cast operator
    f = srcmlcpp.srcmlcpp_main.code_first_function_decl(options, "operator ImVec4() const;")
    assert f.is_operator()
    assert f.operator_name() == "ImVec4"
    assert not hasattr(f, "return_type")
    # inline cast operator
    f = srcmlcpp.srcmlcpp_main.code_first_function_decl(options, "inline operator ImVec4() const;")
    assert f.is_operator()
    assert f.operator_name() == "ImVec4"
    assert f.return_type.str_code() == "inline"


def test_with_qualified_types():
    code = """
        namespace Ns {
            struct S {};
            void f1(S s);
            void f2(int);
        }
    """
    options = srcmlcpp.SrcmlcppOptions()
    cpp_unit = srcmlcpp.code_to_cpp_unit(options, code)
    functions = cpp_unit.all_functions_recursive()
    f1 = functions[0]
    f2 = functions[1]

    f1_qualified = f1.with_qualified_types()
    code_utils.assert_are_codes_equal(f1_qualified.str_code(), "void f1(Ns::S s);")
    code_utils.assert_are_codes_equal(f1.str_code(), "void f1(S s);")
    assert f1_qualified is not f1

    f2_qualified = f2.with_qualified_types()
    code_utils.assert_are_codes_equal(f2_qualified.str_code(), "void f2(int );")
    code_utils.assert_are_codes_equal(f2.str_code(), "void f2(int );")
    assert f2_qualified is f2
