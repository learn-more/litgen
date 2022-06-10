import srcmlcpp
from srcmlcpp import srcml_main, srcml_types_parse
from srcmlcpp.srcml_types import *
from srcmlcpp import code_utils


def test_c_array_fixed_size_to_std_array():
    options = srcmlcpp.SrcmlOptions()

    def code_to_decl_statement(code):
        element = srcml_main.get_only_child_with_tag(options, code, "decl")
        cpp_decl = srcml_types_parse.parse_decl(options, element, None)
        return cpp_decl

    code = "const int v[3]"
    cpp_decl = code_to_decl_statement(code)
    new_decl = cpp_decl.c_array_fixed_size_to_std_array()
    code_utils.assert_are_codes_equal(new_decl, "const std::array<int, 3>& v")

    code = "const unsigned int v[3]"
    cpp_decl = code_to_decl_statement(code)
    new_decl = cpp_decl.c_array_fixed_size_to_std_array()
    code_utils.assert_are_codes_equal(new_decl, "const std::array<unsigned int, 3>& v")

    code = "int v[2]"
    cpp_decl = code_to_decl_statement(code)
    new_decls = cpp_decl.c_array_fixed_size_to_new_modifiable_decls()
    assert len(new_decls) == 2
    code_utils.assert_are_codes_equal(new_decls[0], "BoxedInt & v_0")
    code_utils.assert_are_codes_equal(new_decls[1], "BoxedInt & v_1")