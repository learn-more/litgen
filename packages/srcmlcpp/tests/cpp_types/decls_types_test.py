import srcmlcpp.srcmlcpp_main
from codemanip import code_utils

from srcmlcpp import srcmlcpp_main
from srcmlcpp.cpp_types import *
from srcmlcpp.srcmlcpp_options import SrcmlcppOptions


def to_decl(code: str) -> CppDecl:
    options = SrcmlcppOptions()
    cpp_decl = srcmlcpp_main.code_first_decl(options, code)
    return cpp_decl


def to_decl_statement(code: str) -> CppDeclStatement:
    options = SrcmlcppOptions()
    cpp_decl = srcmlcpp_main.code_first_decl_statement(options, code)
    return cpp_decl


def test_is_c_string_list_ptr():
    assert to_decl("const char * const items[]").is_c_string_list_ptr()
    assert to_decl("const char * items[]").is_c_string_list_ptr()
    assert to_decl("const char ** const items").is_c_string_list_ptr()
    assert to_decl("const char ** items").is_c_string_list_ptr()

    assert not to_decl("const char ** const items=some_default_value()").is_c_string_list_ptr()
    assert to_decl("const char ** const items=nullptr").is_c_string_list_ptr()
    assert to_decl("const char ** const items=NULL").is_c_string_list_ptr()

    assert not to_decl("const char ** items[]").is_c_string_list_ptr()
    assert not to_decl("const char items[]").is_c_string_list_ptr()
    assert not to_decl("char **items").is_c_string_list_ptr()
    assert not to_decl("const unsigned char ** items").is_c_string_list_ptr()


def test_cpp_type():
    options = srcmlcpp.SrcmlcppOptions()

    cpp_type = srcmlcpp.srcmlcpp_main.code_to_cpp_type(options, "int")
    assert len(cpp_type.typenames) == 1
    assert not cpp_type.is_inferred_type()
    assert not cpp_type.is_const()

    cpp_type = srcmlcpp.srcmlcpp_main.code_to_cpp_type(options, "extern static const unsigned int**")
    assert cpp_type.is_const()
    assert cpp_type.is_static()
    assert "extern" in cpp_type.specifiers
    assert cpp_type.typenames == ["unsigned", "int"]
    assert cpp_type.modifiers == ["*", "*"]

    options.functions_api_prefixes = "MY_API"
    cpp_type = srcmlcpp.srcmlcpp_main.code_to_cpp_type(options, "MY_API int &&")
    assert "MY_API" in cpp_type.specifiers
    assert cpp_type.modifiers == ["&&"]
    assert cpp_type.typenames == ["int"]


def test_decl():
    options = srcmlcpp.SrcmlcppOptions()

    cpp_decl = srcmlcpp.srcmlcpp_main.code_first_decl(options, "int a")
    assert cpp_decl.initial_value_code == ""
    assert cpp_decl.cpp_type.str_code() == "int"

    cpp_decl = srcmlcpp.srcmlcpp_main.code_first_decl(options, "int a = 5")
    assert cpp_decl.initial_value_code == "5"

    cpp_decl = srcmlcpp.srcmlcpp_main.code_first_decl(options, "int a[5]")
    assert cpp_decl.is_c_array()
    assert cpp_decl.c_array_size_as_int() == 5
    assert cpp_decl.is_c_array()

    cpp_decl = srcmlcpp.srcmlcpp_main.code_first_decl(options, "int a[]")
    assert cpp_decl.is_c_array()
    assert cpp_decl.c_array_size_as_int() is None
    assert not cpp_decl.is_c_array_known_fixed_size()

    options.named_number_macros = {"COUNT": 3}
    cpp_decl = srcmlcpp.srcmlcpp_main.code_first_decl(options, "const int v[COUNT]")
    assert cpp_decl.is_c_array()
    assert cpp_decl.c_array_size_as_int() == 3
    assert cpp_decl.is_c_array_known_fixed_size()

    code = "unsigned int b : 3"
    cpp_decl = srcmlcpp.srcmlcpp_main.code_first_decl(options, code)
    assert cpp_decl.is_bitfield()
    assert cpp_decl.bitfield_range == ": 3"


def test_decl_statement():
    # Basic test
    code = "int a;"
    code_utils.assert_are_equal_ignore_spaces(to_decl_statement(code), "int a;")

    # # Test with *, initial value and east/west const translation
    code = "int const *a=nullptr;"
    code_utils.assert_are_equal_ignore_spaces(to_decl_statement(code), "const int * a = nullptr;")

    # Test with several variables + modifiers
    code = "int a = 3, &b = b0, *c;"
    code_utils.assert_are_codes_equal(
        to_decl_statement(code),
        """
        int a = 3;
        int & b = b0;
        int * c;
    """,
    )

    # Test with double pointer, which creates a double modifier
    code = "uchar **buffer;"
    code_utils.assert_are_codes_equal(to_decl_statement(code), "uchar * * buffer;")

    # Test with a template type
    code = "std::map<int, std::string>x={1, 2, 3};"
    code_utils.assert_are_codes_equal(to_decl_statement(code), "std::map<int, std::string> x = {1, 2, 3};")

    # Test with a top comment for two decls in a decl_stmt
    code = """
    // Comment line 1
    // continued on line 2
    int a = 42, b = 0;
    """
    code_utils.assert_are_codes_equal(
        to_decl_statement(code),
        """
    // Comment line 1
    // continued on line 2
    int a = 42;
    // Comment line 1
    // continued on line 2
    int b = 0;
    """,
    )

    # Test with an EOL comment
    code = """
    int a = 42; // This is an EOL comment
    """
    decl = to_decl_statement(code)
    decl_str = str(decl)
    code_utils.assert_are_codes_equal(
        decl_str,
        """
    int a = 42; // This is an EOL comment
    """,
    )


# def test_decl_with_qualified_types():
#     code = """
#     namespace N1
#     {
#         struct Boo {};
#
#         namespace N2
#         {
#             struct Foo {};
#             namespace N3
#             {
#                 struct Foo3 {
#                     // These should be interpreted as N1::N2::Foo f = N1::N2::Foo();
#                     Foo f = Foo();
#                     N2::Foo f_n2 = N2::Foo();
#                     N1::N2::Foo f_n1_n2 = N1::N2::Foo();
#
#                     // Those should not, and left unmodified
#                     N3::Foo f_n1 = N1::Foo();
#                     N3::Foo f_n3 = N3::Foo();
#                 };
#             }
#         }
#     }
#     """
#     options = srcmlcpp.SrcmlcppOptions()
#     cpp_unit = srcmlcpp.code_to_cpp_unit(options, code)
#     structs = cpp_unit.all_structs_recursive()
#     foo3 = structs[2]
#
# def qualified_decl_initial_value(i: int) -> str:
#     r = foo3.get_members()[i].with_qualified_types().str_code()
#     return r
#
# # assert qualified_decl_initial_value(0) == "N1::N2::Foo f = N1::N2::Foo()"
# assert qualified_decl_initial_value(1) == "N1::N2::Foo f_n2 = N1::N2::Foo()"
# assert qualified_decl_initial_value(2) == "N1::N2::Foo f_n1_n2 = N1::N2::Foo()"

# _access_type, foo3_member = foo3.get_members()[0]
# foo3_member_type = foo3_member.cpp_type
# assert foo3_member_type.str_code() == "Foo2"
#
# foo3_member_type_qualified = foo3_member_type.with_qualified_types(foo3.cpp_scope())
# assert foo3_member_type_qualified.str_code() == "N1::N2::Foo2"
#
# _access_type, foo3_member2 = foo3.get_members()[1]
# assert foo3_member2.cpp_type.with_qualified_types(foo3.cpp_scope()) is foo3_member2.cpp_type


def test_decl_qualified_type_full():

    # Given the current code
    code = """
        int f();
        namespace N1 {
            namespace N2 {
                struct S2 { constexpr static int s2 = 0; };
                enum class E2 { a = 0 };  // enum class!
                int f2();
            }
            namespace N3 {
                enum E3 { a = 0 };        // C enum!
                int f3();

                // We want to qualify the parameters' declarations of this function
                // Note the subtle difference for enum and enum class
                // The comment column gives the expected qualified type and initial values
                void g(
                        int _f = f(),             // => int _f = f()
                        N2::S2 s2 = N2::S2(),     // => N1::N2 s2 = N1::N2::S2()
                        N2::E2 e2 = N2::E2::a,    // => N1::N2::E2 e2 = N1::N2::E2::a
                        E3 e3 = E3::a,            // => N1::N3::E3 a = N1::N3::a
                        int _f3 = N1::N3::f3(),   // => int _f3 = N1::N3::f3()
                        int other = N1::N4::f4(), // => N1::N4::f4()                    (untouched!)
                        int _s2 = N2::S2::s2      // => N1::N2::S2::s2
                    );
            }
        }
    """
    options = srcmlcpp.SrcmlcppOptions()
    cpp_unit = srcmlcpp.code_to_cpp_unit(options, code)

    g = cpp_unit.all_functions_recursive()[3]

    params = g.parameter_list.parameters

    # int _f = f(),            // => int _f = f()
    i0 = params[0].decl.initial_value_code_with_qualified_types()
    assert i0 == "f()"
    # N2::S2 s2 = N2::S2(),    // => N1::N2 s2 = N1::N2::S2()
    i1 = params[1].decl.initial_value_code_with_qualified_types()
    assert i1 == "N1::N2::S2()"
    # N2::E2 e2 = N2::E2::a,    // => N1::N2::E2 e2 = N1::N2::E2::a
    i2 = params[2].decl.initial_value_code_with_qualified_types()
    assert i2 == "N1::N2::E2::a"
    # E3 e3 = E3::a,           // => N1::N3::E3 a = N1::N3::a      (enum non class!)
    i3 = params[3].decl.initial_value_code_with_qualified_types()
    assert i3 == "N1::N3::E3::a"
    # int _f3 = N1::N3::f3(),  // => int _f3 = N1::N3::f3()
    i4 = params[4].decl.initial_value_code_with_qualified_types()
    assert i4 == "N1::N3::f3()"
    # int other = N1::N4::f4() // => N1::N4::f4()                    (untouched!)
    i5 = params[5].decl.initial_value_code_with_qualified_types()
    assert i5 == "N1::N4::f4()"
    # int _s2 = N2::S2::s2      // => N1::N2::S2::s2
    i6 = params[6].decl.initial_value_code_with_qualified_types()
    assert i6 == "N1::N2::S2::s2"
