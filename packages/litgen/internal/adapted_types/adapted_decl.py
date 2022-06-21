from __future__ import annotations
from dataclasses import dataclass
from typing import cast

from srcmlcpp.srcml_types import *

from litgen.internal import cpp_to_python
from litgen.internal.adapted_types.adapted_element import AdaptedElement
from litgen.options import LitgenOptions


@dataclass
class AdaptedDecl(AdaptedElement):
    def __init__(self, decl: CppDecl, options: LitgenOptions) -> None:
        super().__init__(decl, options)

    # override
    def cpp_element(self) -> CppDecl:
        return cast(CppDecl, self._cpp_element)

    def decl_name_cpp(self) -> str:
        decl_name_cpp = self.cpp_element().decl_name
        return decl_name_cpp

    def decl_value_cpp(self) -> str:
        decl_value_cpp = self.cpp_element().initial_value_code
        return decl_value_cpp

    def decl_name_python(self) -> str:
        decl_name_cpp = self.cpp_element().decl_name
        decl_name_python = cpp_to_python.var_name_to_python(decl_name_cpp, self.options)
        return decl_name_python

    def decl_value_python(self) -> str:
        decl_value_cpp = self.cpp_element().initial_value_code
        decl_value_python = cpp_to_python.var_value_to_python(decl_value_cpp, self.options)
        return decl_value_python

    def decl_type_python(self) -> str:
        decl_type_cpp = self.cpp_element().cpp_type.str_code()
        decl_type_python = cpp_to_python.type_to_python(decl_type_cpp, self.options)
        return decl_type_python

    def is_immutable_for_python(self) -> bool:
        cpp_type_name = self.cpp_element().cpp_type.str_code()
        r = cpp_to_python.is_cpp_type_immutable_for_python(cpp_type_name)
        return r

    def c_array_fixed_size_to_const_std_array(self) -> AdaptedDecl:
        """
        Processes decl that contains a *const* c style array of fixed size, e.g. `const int v[2]`

        We simply wrap it into a std::array, like this:
                `const int v[2]` --> `const std::array<int, 2> v`
        """
        cpp_element = self.cpp_element()
        assert cpp_element.is_c_array_known_fixed_size(self.options.srcml_options)
        assert cpp_element.is_const()
        array_size = cpp_element.c_array_size_as_int(self.options.srcml_options)

        # If the array is `const`, then we simply wrap it into a std::array, like this:
        # `const int v[2]` --> `[ const std::array<int, 2> v ]`
        new_cpp_decl = copy.deepcopy(self.cpp_element())
        new_cpp_decl.c_array_code = ""

        new_cpp_decl.cpp_type.specifiers.remove("const")
        cpp_type_name = new_cpp_decl.cpp_type.str_code()

        std_array_type_name = f"std::array<{cpp_type_name}, {array_size}>&"
        new_cpp_decl.cpp_type.typenames = [std_array_type_name]

        new_cpp_decl.cpp_type.specifiers.append("const")
        new_cpp_decl.decl_name = new_cpp_decl.decl_name

        new_adapted_decl = AdaptedDecl(new_cpp_decl, self.options)
        return new_adapted_decl

    def c_array_fixed_size_to_mutable_new_boxed_decls(self) -> List[AdaptedDecl]:
        """
        Processes decl that contains a *non const* c style array of fixed size, e.g. `int v[2]`
            * we may need to "Box" the values if they are of an immutable type in python,
            * we separate the array into several arguments
            For example:
                `int v[2]`
            Becomes:
                `[ BoxedInt v_0, BoxedInt v_1 ]`

        :return: a list of CppDecls as described before
        """
        cpp_element = self.cpp_element()
        srcml_options = self.options.srcml_options
        array_size = cpp_element.c_array_size_as_int(srcml_options)

        assert array_size is not None
        assert cpp_element.is_c_array_known_fixed_size(srcml_options)
        assert not cpp_element.is_const()

        cpp_type_name = cpp_element.cpp_type.str_code()

        if cpp_to_python.is_cpp_type_immutable_for_python(cpp_type_name):
            boxed_type = cpp_to_python.BoxedImmutablePythonType(cpp_type_name)
            cpp_type_name = boxed_type.boxed_type_name()

        new_decls: List[AdaptedDecl] = []
        for i in range(array_size):
            new_decl = copy.deepcopy(self)
            new_decl.cpp_element().decl_name = new_decl.cpp_element().decl_name + "_" + str(i)
            new_decl.cpp_element().cpp_type.typenames = [cpp_type_name]
            new_decl.cpp_element().cpp_type.modifiers = ["&"]
            new_decl.cpp_element().c_array_code = ""
            new_decls.append(new_decl)

        return new_decls

    def _str_pydef_as_pyarg(self) -> str:
        """pydef code for function parameters"""
        param_template = 'py::arg("{argname_python}"){maybe_equal}{maybe_defaultvalue_cpp}'

        maybe_defaultvalue_cpp = self.cpp_element().initial_value_code
        if len(maybe_defaultvalue_cpp) > 0:
            maybe_equal = " = "
        else:
            maybe_equal = ""

        argname_python = self.decl_name_python()

        param_line = code_utils.replace_in_string(
            param_template,
            {
                "argname_python": argname_python,
                "maybe_equal": maybe_equal,
                "maybe_defaultvalue_cpp": maybe_defaultvalue_cpp,
            },
        )
        return param_line

    def _str_stub_class_member(self) -> List[str]:
        """pydef code for class members"""
        decl_name_python = self.decl_name_python()
        decl_type_python = self.decl_type_python()

        default_value_python = self.decl_value_python()
        if len(default_value_python) > 0:
            maybe_defaultvalue_python = default_value_python
            maybe_equal = " = "
        else:
            maybe_defaultvalue_python = ""
            maybe_equal = ""

        decl_template = f"{decl_name_python}:{decl_type_python}{maybe_equal}{maybe_defaultvalue_python}"

        title_lines = [decl_template]
        body_lines: List[str] = []
        code_lines = self._str_stub_layout_lines(title_lines, body_lines, add_pass_if_empty_body=False)
        return code_lines

    # override
    def _str_pydef_lines(self) -> List[str]:
        """intentionally not implemented, since it depends on the context
        (is this decl a function param, a method member, an enum member, etc.)"""
        raise ValueError("Not implemented")

    # override
    def _str_stub_lines(self) -> List[str]:
        """intentionally not implemented, since it depends on the context
        (is this decl a function param, a method member, an enum member, etc.)"""
        raise ValueError("Not implemented")
