import logging
import os, sys;

import pytest

_THIS_DIR = os.path.dirname(__file__); sys.path.append(_THIS_DIR + "/../..")

from litgen.internal import code_utils
from litgen.options import CodeStyleOptions, code_style_implot
import litgen
from litgen.internal.function_params_adapter import make_function_params_adapter
from litgen.internal import function_adapt_c_arrays, cpp_to_python
from litgen.internal import module_pydef_generator
import srcmlcpp
from srcmlcpp.srcml_types import *

OPTIONS = litgen.options.code_style_implot()
OPTIONS.srcml_options.functions_api_prefixes = ["MY_API"]


def get_first_function_decl(code) -> CppFunctionDecl:
    cpp_unit = srcmlcpp.code_to_cpp_unit(OPTIONS.srcml_options, code)
    for child in cpp_unit.block_children:
        if isinstance(child, CppFunctionDecl) or isinstance(child, CppFunction):
            return child
    return None


def test_make_function_params_adapter():

    def make_adapted_function(code):
        function_decl = get_first_function_decl(code)
        struct_name = ""
        function_adapted_params = make_function_params_adapter(function_decl, OPTIONS, struct_name)
        return function_adapted_params

    # Easy test with const
    code = """void foo(const int v[2]);"""
    function_adapted_params = make_adapted_function(code)
    code_utils.assert_are_codes_equal(function_adapted_params.function_infos, "void foo(const std::array<int, 2>& v);")

    # Less easy test with non const
    code = """void foo(unsigned long long v[2]);"""
    function_adapted_params = make_adapted_function(code)
    code_utils.assert_are_codes_equal(
        function_adapted_params.function_infos,
        "void foo(BoxedUnsignedLongLong & v_0, BoxedUnsignedLongLong & v_1);")

    # Full test with a mixture
    code = """void foo(bool flag, const double v[2], double outputs[2]);"""
    function_adapted_params = make_adapted_function(code)
    code_utils.assert_are_codes_equal(
        function_adapted_params.function_infos,
        "void foo(bool flag, const std::array<double, 2>& v, BoxedDouble & outputs_0, BoxedDouble & outputs_1);")


def test_use_function_params_adapter_const():
    code = """void foo_const(const int input[2]);"""
    function_decl = get_first_function_decl(code)
    generated_code = module_pydef_generator._generate_pydef_function(function_decl, OPTIONS)
    # logging. warning("\n" + generated_code)
    code_utils.assert_are_codes_equal(generated_code, """
        m.def("foo_const",
            [](const std::array<int, 2>& input)
            {
                auto foo_const_adapt_fixed_size_c_arrays = [](const std::array<int, 2>& input)
                {
                    foo_const(input.data());
                };
        
                foo_const_adapt_fixed_size_c_arrays(input);
            },
            py::arg("input")
        );    
    """)


def test_use_function_params_adapter_non_const():
    code = """void foo_non_const(int output[2]);"""
    function_decl = get_first_function_decl(code)
    generated_code = module_pydef_generator._generate_pydef_function(function_decl, OPTIONS)
    # logging.warning("\n" + generated_code)
    code_utils.assert_are_codes_equal(generated_code, """
        m.def("foo_non_const",
            [](BoxedInt & output_0, BoxedInt & output_1)
            {
                auto foo_non_const_adapt_fixed_size_c_arrays = [](BoxedInt & output_0, BoxedInt & output_1)
                {
                    int output_raw[2];
                    output_raw[0] = output_0.value;
                    output_raw[1] = output_1.value;
        
                    foo_non_const(output_raw);
        
                    output_0.value = output_raw[0];
                    output_1.value = output_raw[1];
                };
        
                foo_non_const_adapt_fixed_size_c_arrays(output_0, output_1);
            },
            py::arg("output_0"),
            py::arg("output_1")
        );    
    """)


def test_mixture():
    code = """void foo(bool flag, const double v[2], double outputs[2]);"""
    function_decl = get_first_function_decl(code)
    generated_code = module_pydef_generator._generate_pydef_function(function_decl, OPTIONS)
    code_utils.assert_are_codes_equal(
        generated_code, """
            m.def("foo",
                [](bool flag, const std::array<double, 2>& v, BoxedDouble & outputs_0, BoxedDouble & outputs_1)
                {
                    auto foo_adapt_fixed_size_c_arrays = [](bool flag, const std::array<double, 2>& v, BoxedDouble & outputs_0, BoxedDouble & outputs_1)
                    {
                        double outputs_raw[2];
                        outputs_raw[0] = outputs_0.value;
                        outputs_raw[1] = outputs_1.value;
            
                        foo(flag, v.data(), outputs_raw);
            
                        outputs_0.value = outputs_raw[0];
                        outputs_1.value = outputs_raw[1];
                    };
            
                    foo_adapt_fixed_size_c_arrays(flag, v, outputs_0, outputs_1);
                },
                py::arg("flag"),
                py::arg("v"),
                py::arg("outputs_0"),
                py::arg("outputs_1")
            );    
    """)
