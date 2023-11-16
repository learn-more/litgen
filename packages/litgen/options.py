from __future__ import annotations

from typing import Any, Callable

from codemanip import code_utils
from codemanip.code_replacements import RegexReplacementList

from srcmlcpp import SrcmlcppOptions

from litgen.internal.template_options import TemplateFunctionsOptions, TemplateClassOptions
from litgen.internal.class_iterable_info import ClassIterablesInfos


class LitgenOptions:
    """Numerous options to configure litgen code generation.

    (include / excludes, indentation, c++ to python translation settings, function parameters
    adaptations, etc.)"""

    # ------------------------------------------------------------------------------
    # Note about regexes below:
    # =========================
    # - regexes can support several alternatives: separate them by "|"
    # For example, in order to match an exact function name, as well as functions ending with "_private",
    # use a regex like this:
    #         r"^YourFunctionName$|_private$",
    # - If a regex string is empty, it will not match anything
    # - To match everything, use r".*"
    # - It is advised to prefix your regex strings with "r" (in order to use raw strings)
    # ------------------------------------------------------------------------------

    ################################################################################
    #    <srcmlcpp options>
    ################################################################################
    # There are interesting options to set in SrcmlcppOptions (see srcmlcpp/srcmlcpp_options.py)
    #
    # Notably:
    # * fill srcmlcpp_options.functions_api_prefixes: the prefix(es) that denotes exported dll functions
    # * also set LitgenOptions.fn_exclude_non_api=True if you want to exclude non api functions and methods
    srcmlcpp_options: SrcmlcppOptions

    ################################################################################
    #    <Layout settings for the generated python stub code>
    ################################################################################
    #    <show the original location and or signature of elements as a comment>
    original_location_flag_show = False
    # if showing location, how many parent folders shall be shown
    # (if -1, show the full path)
    original_location_nb_parent_folders = 0
    # If True, the complete C++ original signature will be show as a comment in the python stub (pyi)
    original_signature_flag_show = False
    # Size of an indentation in the python stubs
    python_indent_size = 4
    python_ident_with_tabs: bool = False
    # Insert as many empty lines in the python stub as found in the header file, keep comments layout, etc.
    python_reproduce_cpp_layout: bool = True
    # The generated code will try to adhere to this max length (if negative, this is ignored)
    python_max_line_length = 80
    # Strip (remove) empty comment lines
    python_strip_empty_comment_lines: bool = False
    # Run black formatter
    python_run_black_formatter: bool = False
    python_black_formatter_line_length: int = 88

    ################################################################################
    #    <Layout settings for the C++ generated pydef code>
    ################################################################################
    # Spacing option in C++ code
    cpp_indent_size: int = 4
    cpp_indent_with_tabs: bool = False

    ################################################################################
    #    <names translation from C++ to python>
    ################################################################################
    # List of code replacements when going from C++ to Python
    # Notes:
    # - by default, type_replacements is prefilled with standard_type_replacements()
    #   type_replacements will be applied to all types (including class and enum names)
    # - by default, value_replacements is prefilled with standard_value_replacements()
    # - by default, comments_replacements is prefilled with standard_comments_replacements()
    # - by default, the others are empty
    # - type_replacements, var_names_replacements and function_names_replacements enable you
    #   to modify the outputted python code
    type_replacements: RegexReplacementList  # = cpp_to_python.standard_type_replacements() by default
    var_names_replacements: RegexReplacementList  # = RegexReplacementList() by default (i.e. empty)
    namespace_names_replacements: RegexReplacementList  # = RegexReplacementList() by default (i.e. empty)
    function_names_replacements: RegexReplacementList  # = RegexReplacementList() by default (i.e. empty)
    value_replacements: RegexReplacementList  # = cpp_to_python.standard_value_replacements() by default
    comments_replacements: RegexReplacementList  # = cpp_to_python.standard_comment_replacements() by default
    macro_name_replacements: RegexReplacementList  # = RegexReplacementList() by default (i.e. empty)
    # Convert variables, functions and namespaces names to snake_case (class, structs, and enums names are always preserved)
    python_convert_to_snake_case: bool = True

    ################################################################################
    #    <functions and method adaptations>
    ################################################################################

    # fn_exclude_non_api:
    # if srcmlcpp_options.functions_api_prefixes is filled, and fn_exclude_non_api=True,
    # then only functions with an api marker will be exported.
    fn_exclude_non_api: bool = True
    # fn_non_api_comment:
    # if fn_exclude_non_api is False, a comment can be added to non api functions in the stub file
    fn_non_api_comment: str = "(private API)"

    # Exclude certain functions and methods by a regex on their name
    fn_exclude_by_name__regex: str = ""

    # Exclude certain functions and methods by a regex on any of their parameter type and/or return type
    # (those should be decorated type)
    # For example:
    #     options.fn_exclude_by_param_type__regex = "^char\s*$|^unsigned\s+char$|Callback$"
    # would exclude all functions having params of type "char *", "unsigned char", "xxxCallback"
    #
    # Note: this is distinct from `fn_params_exclude_types__regex` which removes params
    # from the function signature, but not the function itself.
    fn_exclude_by_param_type__regex: str = ""

    # ------------------------------------------------------------------------------
    # Templated functions options
    # ------------------------------------------------------------------------------
    # Template function must be instantiated for the desired types.
    # See https://pybind11.readthedocs.io/en/stable/advanced/functions.html#binding-functions-with-template-parameters
    #
    # fn_template_options:
    #    of type Dict[ TemplatedFunctionNameRegexStr (aka str), List[CppTypeName] ]
    #
    # For example,
    # 1. This line:
    #        options.fn_template_options.add_specialization(r"template^", ["int", double"])
    #    would instantiate all template functions whose name end with "template" with "int" and "double"
    # 2. This line:
    #        options.fn_template_options.add_specialization(r".*", ["int", float"])
    #    would instantiate all template functions (whatever their name) with "int" and "float"
    # 3. This line:
    #        options.fn_template_options.add_ignore(r".*")
    #    would ignore all template functions (they will not be exported)
    fn_template_options: TemplateFunctionsOptions
    # if fn_template_decorate_in_stub is True, then there will be some
    # decorative comments in the stub file, in order to visually group
    # the generated functions together
    fn_template_decorate_in_stub: bool = True

    # ------------------------------------------------------------------------------
    # Vectorize functions options
    # ------------------------------------------------------------------------------
    # Numeric functions (i.e. function accepting and returning only numeric params or py::array), can be vectorized
    # i.e. they will accept numpy arrays as an input.
    # See https://pybind11.readthedocs.io/en/stable/advanced/pycpp/numpy.html#vectorizing-functions
    # and https://github.com/pybind/pybind11/blob/master/tests/test_numpy_vectorize.cpp
    #
    # * fn_vectorize__regex and fn_namespace_vectorize__regex contain a regexes
    # on functions names + namespace names for which this transformation will be applied.
    #
    # For example, to vectorize all function of the namespace MathFunctions, apply these options:
    #     options.fn_namespace_vectorize__regex: str = r"MathFunctions^$"
    #     options.fn_vectorize__regex = r".*"
    #
    # * fn_vectorize_prefix and fn_vectorize_suffix will be added to the vectorized functions names
    #   (they can be empty, in which case the vectorized function will be a usable overload with the same name)
    fn_vectorize__regex: str = r""
    fn_namespace_vectorize__regex: str = r""
    fn_vectorize_prefix: str = ""
    fn_vectorize_suffix: str = ""

    # ------------------------------------------------------------------------------
    # Exclude some params by name
    # ------------------------------------------------------------------------------
    #
    # Remove some params from the python published interface. A param can only be removed if it has a default value
    # in the C++ signature
    fn_params_exclude_names__regex: str = ""
    fn_params_exclude_types__regex: str = ""

    # ------------------------------------------------------------------------------
    # Return policy
    # ------------------------------------------------------------------------------
    # Force the function that match those regexes to use `pybind11::return_value_policy::reference`
    #
    # Note:
    #    you can also write "// py::return_value_policy::reference" as an end of line comment after the function.
    #    See packages/litgen/integration_tests/mylib/include/mylib/return_value_policy_test.h as an example
    fn_return_force_policy_reference_for_pointers__regex: str = ""
    fn_return_force_policy_reference_for_references__regex: str = ""

    # ------------------------------------------------------------------------------
    # Force overload
    # ------------------------------------------------------------------------------
    # Force using py::overload for functions that matches these regexes
    fn_force_overload__regex: str = ""
    # Force using a lambda for functions that matches these regexes
    # (useful when pybind11 is confused and gives error like
    #     error: no matching function for call to object of type 'const detail::overload_cast_impl<...>'
    fn_force_lambda__regex: str = ""

    # ------------------------------------------------------------------------------
    # C style buffers to py::array
    # ------------------------------------------------------------------------------
    #
    # Signatures with a C buffer like this:
    #       MY_API inline void add_inside_array(uint8_t* array, size_t array_size, uint8_t number_to_add)
    # may be transformed to:
    #       void add_inside_array(py::array & array, uint8_t number_to_add)              (c++ bound signature)
    #       def add_inside_array(array: numpy.ndarray, number_to_add: int) -> None       (python)
    #
    # It also works for templated buffers:
    #       MY_API template<typename T> void mul_inside_array(T* array, size_t array_size, double factor)
    # will be transformed to:
    #       void mul_inside_array(py::array & array, double factor)                      (c++ bound signature)
    #       def mul_inside_array(array: numpy.ndarray, factor: float) -> None            (python)
    # (and factor will be down-casted to the target type)
    #
    # fn_params_buffer_replace_by_array_regexes contains a regex on functions names
    # for which this transformation will be applied.
    # Set it to r".*" to apply this to all functions, set it to "" to disable it
    #
    fn_params_replace_buffer_by_array__regex: str = r""

    # fn_params_buffer_types: list of numeric types that are considered as possible buffers.
    # You can customize this list in your own options by removing items from it,
    # but you *cannot* add new types or new synonyms (typedef for examples); since the conversion between
    # py::array and native relies on these *exact* names!
    #
    # By default, fn_params_buffer_types will contain those types:
    fn_params_buffer_types: str = code_utils.join_string_by_pipe_char(
        [
            "uint8_t",
            "int8_t",
            "uint16_t",
            "int16_t",
            "uint32_t",
            "int32_t",
            "np_uint_l",  # Platform dependent: "uint64_t" on *nixes, "uint32_t" on windows
            "np_int_l",  # Platform dependent: "int64_t" on *nixes, "int32_t" on windows
            "float",
            "double",
            "long double",
            "long long",
        ]
    )

    # fn_params_buffer_template_types: list of templated names that are considered as possible templated buffers
    # By default, only template<typename T> or template<typename NumericType> are accepted
    fn_params_buffer_template_types: str = code_utils.join_string_by_pipe_char(["T", "NumericType"])

    # fn_params_buffer_size_names__regex: possible names for the size of the buffer
    # = ["nb", "size", "count", "total", "n"] by default
    fn_params_buffer_size_names__regex: str = code_utils.join_string_by_pipe_char(
        [
            code_utils.make_regex_var_name_contains_word("nb"),
            code_utils.make_regex_var_name_contains_word("size"),
            code_utils.make_regex_var_name_contains_word("count"),
            code_utils.make_regex_var_name_contains_word("total"),
            code_utils.make_regex_var_name_contains_word("n"),
        ]
    )

    # ------------------------------------------------------------------------------
    # C style arrays functions and methods parameters
    # ------------------------------------------------------------------------------
    #
    # Signatures like
    #       void foo_const(const int input[2])
    # may be transformed to:
    #       void foo_const(const std::array<int, 2>& input)    (c++ bound signature)
    #       def foo_const(input: List[int]) -> None:           (python)
    # fn_params_replace_c_array_const_by_std_array__regex contains a list of regexes on functions names
    # for which this transformation will be applied.
    # Set it to r".*" to apply this to all functions, set it to "" to disable it
    fn_params_replace_c_array_const_by_std_array__regex: str = r".*"

    # Signatures like
    #       void foo_non_const(int output[2])
    # may be transformed to:
    #       void foo_non_const(BoxedInt & output_0, BoxedInt & output_1)         (c++ bound signature)
    #       def foo_non_const(output_0: BoxedInt, output_0: BoxedInt) -> None    (python)
    # fn_params_replace_c_array_modifiable_by_boxed__regex contains a list of regexes on functions names
    # for which this transformation will be applied.
    # Set it to r".*" to apply this to all functions, set it to "" to disable it
    fn_params_replace_c_array_modifiable_by_boxed__regex: str = r".*"
    # (c_array_modifiable_max_size is the maximum number of params that can be boxed like this)
    fn_params_replace_modifiable_c_array__max_size = 10

    # ------------------------------------------------------------------------------
    # C style string list functions and methods parameters
    # ------------------------------------------------------------------------------
    # Signatures like
    #     void foo(const char * const items[], int items_count)
    # may be transformed to:
    #     void foo(const std::vector<std::string>& const items[])        (c++ bound signature)
    #     def foo(items: List[str]) -> None                              (python)
    # fn_params_replace_c_string_list_regexes contains a list of regexes on functions names
    # for which this transformation will be applied.
    # Set it to [r".*"] to apply this to all functions, set it to [] to disable it
    fn_params_replace_c_string_list__regex: str = r".*"

    # ------------------------------------------------------------------------------
    # Make "immutable python types" modifiable, when passed by pointer or reference
    # ------------------------------------------------------------------------------
    #
    # adapt functions params that use non const pointers or reference to a type that is immutable in python.

    # Signatures like
    #     int foo(int* value)
    # May be transformed to:
    #     def foo(BoxedInt value) -> int                                  (python)
    # So that any modification done on the C++ side can be seen from python.
    #
    # fn_params_adapt_modifiable_immutable_regexes contains a list of regexes on functions names
    # Set it to r".*" to apply this to all functions. Set it to "" to disable it
    fn_params_replace_modifiable_immutable_by_boxed__regex: str = ""

    # As an alternative, we can also add the modified value to the returned type
    # of the function (which will now be a tuple)
    #
    # For example
    #     int foo(int* value)
    # May be transformed to:
    #     def foo(int value) -> Tuple[int, bool]
    # So that any modification done on the C++ side can be seen from python.
    #
    # fn_params_output_modifiable_immutable_to_return__regex contains a list of regexes on functions names
    # Set it to r".*" to apply this to all functions. Set it to "" to disable it
    fn_params_output_modifiable_immutable_to_return__regex: str = ""

    # ------------------------------------------------------------------------------
    # Custom adapters (advanced, very advanced and not documented here)
    # fn_custom_adapters may contain callables of signature
    #   f(adapted_function: AdaptedFunction) -> Optional[LambdaAdapter]
    # ------------------------------------------------------------------------------
    fn_custom_adapters: list[Any]

    ################################################################################
    #    <class, struct, and member adaptations>
    ################################################################################

    # Exclude certain classes and structs by a regex on their name
    class_exclude_by_name__regex: str = ""
    # Exclude certain members by a regex on their name
    member_exclude_by_name__regex: str = ""
    # Exclude members based on their type
    member_exclude_by_type__regex: str = ""

    # class_create_default_named_ctor__regex / struct_create_default_named_ctor__regex:
    # regex giving the list of class & struct names for which we want to generate a named
    # constructor for Python, when no default constructor is provided by C++
    # (by default, this is active for all structs and not for the classes,
    #  in order for it to work, all struct members need to be default constructible if
    #  they are not declared with a default value)
    struct_create_default_named_ctor__regex: str = r".*"
    class_create_default_named_ctor__regex: str = r""

    # class_expose_protected_methods__regex:
    # regex giving the list of class names for which we want to expose protected methods.
    # (by default, only public methods are exposed)
    # If active, this will use the technique described at
    # https://pybind11.readthedocs.io/en/stable/advanced/classes.html#binding-protected-member-functions)
    class_expose_protected_methods__regex: str = ""

    # class_expose_protected_methods__regex:
    # regex giving the list of class names for which we want to be able to override virtual methods
    # from python.
    # (by default, this is not possible)
    # If active, this will use the technique described at
    # https://pybind11.readthedocs.io/en/stable/advanced/classes.html#overriding-virtual-functions-in-python
    #
    # Note: if you want to override protected functions, also fill `class_expose_protected_methods__regex`
    class_override_virtual_methods_in_python__regex: str = ""

    # class_dynamic_attributes__regex
    # By default, classes exported from C++ do not support dynamic attributes and the only writable attributes are
    # the ones explicitly defined using class_::def_readwrite() or class_::def_property().
    # If active, this will use the technique described at
    # https://pybind11.readthedocs.io/en/stable/classes.html#dynamic-attributes
    class_dynamic_attributes__regex: str = ""

    # class_deep_copy__regex & class_copy__regex:
    # By default, structs and classes exported from C++ do not support (deep)copy.
    # However, if they do have a copy constructor (implicit or user defined),
    # (deep)copy can be enabled by invoking this constructor.
    # https://pybind11.readthedocs.io/en/stable/advanced/classes.html#deepcopy-support
    class_deep_copy__regex: str = ""
    class_copy__regex: str = ""
    # If class_copy_add_info_in_stub=True, the existence of __copy__ and __deepcopy__
    # will be mentioned in the stub file.
    class_copy_add_info_in_stub: bool = False

    # iterable classes: if some cpp classes expose begin()/end()/size(), they can be made iterable in python
    # Make classes iterables by setting:
    #     options.class_iterables_infos.add_iterable_class(python_class_name__regex, iterable_python_type_name)
    class_iterables_infos: ClassIterablesInfos

    # ------------------------------------------------------------------------------
    # Templated class options
    # ------------------------------------------------------------------------------
    # Template class must be instantiated for the desired types, and a new name must be given for each instantiation
    # See https://pybind11.readthedocs.io/en/stable/advanced/classes.html#binding-classes-with-template-parameters
    #
    # class_template_options enables to set this
    #
    # For example
    # 1. this call would instantiate some classes for types "int" and "const char *", with a naming scheme:
    #   MyClass<int> (cpp)  -> MyClassInt (python)
    #   ------------------------------------------
    #     options.class_template_options.add_specialization(
    #         class_name_regex=r"^MyPrefix",                 # r"^MyPrefix" => select class names with this prefix
    #         cpp_types_list=["int", "const char *"],        # instantiated types
    #         naming_scheme=TemplateNamingScheme.camel_case_suffix
    #     )
    # 2. this call would ignore all template classes:
    #        options.class_template_options.add_ignore(r".*")
    #    would ignore all template functions (they will not be exported)
    class_template_options: TemplateClassOptions
    # if class_template_decorate_in_stub is True, then there will be some
    # decorative comments in the stub file, in order to visually group
    # the generated classes together
    class_template_decorate_in_stub: bool = True

    # ------------------------------------------------------------------------------
    # Adapt class members
    # ------------------------------------------------------------------------------
    # adapt class members which are a fixed size array of a numeric type:
    #
    # For example
    #       struct Foo {  int values[10]; };
    # May be transformed to:
    #       class Foo:
    #           values: numpy.ndarray
    #
    # i.e. the member will be transformed to a property that points to a numpy array
    # which can be read/written from python (this requires numpy)
    # This is active by default.
    member_numeric_c_array_replace__regex: str = r".*"

    # member_numeric_c_array_types: list of numeric types that can be stored in a numpy array
    # for a class member which is a fixed size array of a numeric type
    # - Synonyms (defined via. `typedef` or `using`) are allowed here
    # - *don't* include char, *don't* include byte, those are not numeric!
    #   See https://numpy.org/doc/stable/reference/generated/numpy.chararray.html
    member_numeric_c_array_types: str = code_utils.join_string_by_pipe_char(
        [
            "int",
            "unsigned int",
            "long",
            "unsigned long",
            "long long",
            "unsigned long long",
            "float",
            "double",
            "long double",
            "uint8_t",
            "int8_t",
            "uint16_t",
            "int16_t",
            "uint32_t",
            "int32_t",
            "uint64_t",
            "int64_t",
            "bool",
        ]
    )

    ################################################################################
    #    <namespace adaptations>
    ################################################################################

    # All C++ namespaces that match this regex will not be emitted as a submodule
    # (i.e. their inner code will be placed in the root python module, or in the parent
    # module)
    namespace_root__regex = r""

    # All C++ namespaces that match this regex will be excluded
    # By default, any namespace whose name contains "internal" or "detail" will be excluded.
    namespace_exclude__regex = r"[Ii]nternal|[Dd]etail"

    ################################################################################
    #    <enum adaptations>
    ################################################################################
    # Exclude certain enums by a regex on their name
    enum_exclude_by_name__regex: str = ""
    # Remove the typical "EnumName_" prefix from "C enum" values.
    # For example, with the C enum:
    #     enum MyEnum { MyEnum_A = 0, MyEnum_B };
    # Values would be named "a" and "b" in python
    enum_flag_remove_values_prefix: bool = True
    # Skip count value from enums, for example like in:
    #    enum MyEnum { MyEnum_A = 1, MyEnum_B = 1, MyEnum_COUNT };
    enum_flag_skip_count: bool = True
    # By default, all enums export rudimentary arithmetic and bit-level operations ( r".*" matches any enum name)
    enum_make_arithmetic__regex = r".*"

    ################################################################################
    #    <define adaptations>
    ################################################################################
    # Simple preprocessor defines can be exported as global variables, e.g.:
    #     #define MY_VALUE 1
    #     #define MY_FLOAT 1.5
    #     #define MY_STRING "abc"
    #     #define MY_HEX_VALUE 0x00010009
    # This is limited to *simple* defines (no param, string, int, float or hex only)
    # By default nothing is exported
    macro_define_include_by_name__regex: str = ""

    ################################################################################
    #    <post processing>
    ################################################################################
    # If you need to process the code after generation, fill these functions
    postprocess_stub_function: Callable[[str], str] | None = None
    postprocess_pydef_function: Callable[[str], str] | None = None

    ################################################################################
    #    <Sanity checks and utilities below>
    ################################################################################
    def check_options_consistency(self) -> None:
        # the only authorized type are those for which the size is known with certainty
        # * int and long are not acceptable candidates: use int8_t, uint_8t, int32_t, etc.
        # * concerning float and doubles, there is no standard for fixed size floats, so we have to cope with
        #   float, double and long double and their various platforms implementations...
        authorized_types = [
            "byte",
            "uint8_t",
            "int8_t",
            "uint16_t",
            "int16_t",
            "uint32_t",
            "int32_t",
            "np_uint_l",  # Platform dependent: "uint64_t" on *nixes, "uint32_t" on windows
            "np_int_l",  # Platform dependent: "int64_t" on *nixes, "int32_t" on windows
            "float",
            "double",
            "long double",
            "long long",
        ]
        for buffer_type in self.fn_params_buffer_types_list():
            if buffer_type not in authorized_types:
                raise ValueError(
                    f"""
                    options.build_types contains an unauthorized type: {buffer_type}
                    Authorized types are: { ", ".join(authorized_types) }
                    """
                )

    def indent_cpp_spaces(self) -> str:
        space = "\t" if self.cpp_indent_with_tabs else " "
        return space * self.cpp_indent_size

    def indent_python_spaces(self) -> str:
        space = "\t" if self.python_ident_with_tabs else " "
        return space * self.python_indent_size

    def fn_params_buffer_types_list(self) -> list[str]:
        return code_utils.split_string_by_pipe_char(self.fn_params_buffer_types)

    def fn_params_buffer_template_types_list(self) -> list[str]:
        return code_utils.split_string_by_pipe_char(self.fn_params_buffer_template_types)

    def member_numeric_c_array_types_list(self) -> list[str]:
        return code_utils.split_string_by_pipe_char(self.member_numeric_c_array_types)

    def __init__(self) -> None:
        # See doc for all the params at their declaration site (scroll up to the top of this file!)
        from litgen.internal import cpp_to_python

        self.srcmlcpp_options = SrcmlcppOptions()
        self.srcmlcpp_options.header_filter_preprocessor_regions = True

        self.type_replacements = cpp_to_python.standard_type_replacements()
        self.value_replacements = cpp_to_python.standard_value_replacements()
        self.comments_replacements = cpp_to_python.standard_comment_replacements()

        self.function_names_replacements = RegexReplacementList()
        self.var_names_replacements = RegexReplacementList()
        self.macro_name_replacements = RegexReplacementList()
        self.namespace_names_replacements = RegexReplacementList()

        self.fn_template_options = TemplateFunctionsOptions()
        self.class_template_options = TemplateClassOptions()

        self.class_iterables_infos = ClassIterablesInfos()

        self.fn_custom_adapters = []
