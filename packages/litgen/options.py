from typing import List

from codemanip import code_replacements
from codemanip.code_replacements import StringReplacement

from srcmlcpp import SrcmlOptions


class LitgenOptions:
    """Configuration of the code generation (include / excludes, indentation, c++ to python translation settings, etc.)"""

    #
    # There are interesting options to set in SrcmlOptions (see srcmlcpp/srcml_options.py)
    #
    # Notably:
    # * fill srcml_options.functions_api_prefixes
    #   (the prefixes that denotes the functions that shall be published)
    # * Also, fill the excludes if you encounter issues with some functions or declarations you want to ignore
    srcml_options: SrcmlOptions = SrcmlOptions()

    #
    # Shall the binding show the original location and or signature of elements as a comment
    #
    original_location_flag_show = False
    # if showing location, how many parent folders shall be shown
    original_location_nb_parent_folders = 0
    # If True, the complete C++ original signature will be show as a comment in the python stub (pyi)
    original_signature_flag_show = False

    #
    # List of code replacements when going from C++ to Python
    # These replacements are applied to type names (for example double -> float, vector-> List, etc)
    # as well as comment (which may contain type names)
    #
    # Note:
    # - by default, code_replacements is prefilled with standard_code_replacements(),
    # - by default, comments_replacements is prefilled with standard_comments_replacements(),
    #
    code_replacements: List[StringReplacement] = []
    comments_replacements: List[StringReplacement] = []

    #
    # Layout settings for the generated python stub code
    #

    # Size of an indentation in the python stubs
    python_indent_size = 4
    python_ident_with_tabs: bool = False
    # Insert as many empty lines in the python stub as found in the header file, keep comments layout, etc.
    python_reproduce_cpp_layout: bool = True
    # Reformat the generated python to remove long series of empty lines (disabled if < 0)
    python_max_consecutive_empty_lines: int = -1
    # The generated code will try to adhere to this max length
    python_max_line_length = 80
    # Strip (remove) empty comment lines
    python_strip_empty_comment_lines: bool = False
    # Run black formatter
    python_run_black_formatter: bool = False
    python_black_formatter_line_length: int = 88

    #
    # Layout settings for the C++ generated pydef code
    #

    # Spacing option in C++ code
    cpp_indent_size: int = 4
    cpp_indent_with_tabs: bool = False

    #
    # enum options
    #

    # Remove the typical "EnumName_" prefix from enum values.
    # For example, with the C enum:
    #     enum MyEnum { MyEnum_A = 0, MyEnum_B };
    # Values would be named "a" and "b" in python
    #
    enum_flag_remove_values_prefix: bool = True
    # Skip count value from enums, for example like in:
    #    enum MyEnum { MyEnum_A = 1, MyEnum_B = 1, MyEnum_COUNT };
    enum_flag_skip_count: bool = True

    #
    # C Buffers to py::array
    #
    # If active, signatures with a C buffer like this:
    #       MY_API inline void add_inside_array(uint8_t* array, size_t array_size, uint8_t number_to_add)
    # will be transformed to:
    #       void add_inside_array(py::array & array, uint8_t number_to_add)
    #
    # It also works for templated buffers:
    #       MY_API template<typename T> void mul_inside_array(T* array, size_t array_size, double factor)
    # will be transformed to:
    #       void mul_inside_array(py::array & array, double factor)
    # (and factor will be down-casted to the target type)
    #

    buffer_flag_replace_by_array = True
    # buffer_types List[str]. Which means that `uint8_t*` are considered as possible buffers
    buffer_types: List[str] = [
        "uint8_t",
        "int8_t",
        "uint16_t",
        "int16_t",
        "uint32_t",
        "int32_t",
        "uint64_t",
        "int64_t",
        "float",
        "double",
        "long double",
    ]
    buffer_template_types: List[str] = [
        "T"
    ]  # Which means that templated functions using a buffer use T as a templated name
    buffer_size_names: List[str] = ["nb", "size", "count", "total", "n"]

    #
    # C style arrays functions and methods parameters
    #
    # If c_array_const_flag_replace is active, then signatures like
    #       void foo_const(const int input[2])
    # will be transformed to:
    #       void foo_const(const std::array<int, 2>& input)
    #
    # If c_array_modifiable_flag_replace is active, then signatures like
    #       void foo_non_const(int output[2])
    # will be transformed to:
    #       void foo_non_const(BoxedInt & output_0, BoxedInt & output_1)
    # (c_array_modifiable_max_size is the maximum number of params that can be boxed like this)
    #
    c_array_const_flag_replace = True
    c_array_modifiable_flag_replace = True
    c_array_modifiable_max_size = 10

    #
    # C style arrays structs and class members
    #
    # If c_array_numeric_member_flag_replace is active, then members like
    #       struct Foo {  int values[10]; };
    # will be transformed to a property that points to a numpy array
    # which can be read/written from python (this requires numpy)
    c_array_numeric_member_flag_replace = True
    # list of numeric types that can be stored in a numpy array
    c_array_numeric_member_types = [  # don't include char !
        "int",  # See https://numpy.org/doc/stable/reference/generated/numpy.chararray.html
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

    # If c_string_list_flag_replace is active, then C string lists `(const char **, size_t)`
    # will be replaced by `const std::vector<std::string>&`. For example:
    #     void foo(const char * const items[], int items_count)
    # will be transformed to:
    #     void foo(const std::vector<std::string>& const items[])
    c_string_list_flag_replace = True

    #
    # Options that need rework
    #
    # Shall we generate a __str__() method for structs
    generate_to_string: bool = False
    # Function that may generate additional code in the function defined in the  __init__.py file of the package
    # poub_init_function_python_additional_code: Optional[Callable[[FunctionsInfos], str]]

    #
    # Sanity checks and utilities below
    #
    def assert_buffer_types_are_ok(self) -> None:
        # the only authorized type are those for which the size is known with certainty
        # * int and long are not acceptable candidates: use int8_t, uint_8t, int32_t, etc.
        # * concerning float and doubles, there is no standard for fixed size floats, so we have to cope with
        #   float, double and long double and their various platforms implementations...
        authorized_types = [
            "uint8_t",
            "int8_t",
            "uint16_t",
            "int16_t",
            "uint32_t",
            "int32_t",
            "uint64_t",
            "int64_t",
            "float",
            "double",
            "long double",
        ]
        for buffer_type in self.buffer_types:
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

    def __init__(self) -> None:
        from litgen.internal import cpp_to_python

        self.srcml_options = SrcmlOptions()
        self.code_replacements = cpp_to_python.standard_code_replacements()
        self.comments_replacements = cpp_to_python.standard_comment_replacements()


#
# Example of configurations for several libraries (immvision, imgui, implot)
#


def code_style_immvision() -> LitgenOptions:
    from litgen.internal import cpp_to_python

    options = LitgenOptions()
    options.generate_to_string = True
    options.cpp_indent_size = 4
    options.srcml_options.functions_api_prefixes = ["IMMVISION_API"]
    options.code_replacements = cpp_to_python.standard_code_replacements() + cpp_to_python.opencv_replacements()

    options.buffer_flag_replace_by_array = False

    def init_function_python_additional_code_require_opengl_initialized(
        function_infos,
    ) -> str:  # function_infos of type FunctionInfos
        # make sure to transfer the ImGui context before doing anything related to ImGui or OpenGL
        title = function_infos.function_code.docstring_cpp
        if "opengl" in title.lower() and "initialized" in title.lower():
            return "\n    _cpp_immvision.transfer_imgui_context_python_to_cpp()\n\n"
        else:
            return ""

    # options.poub_init_function_python_additional_code = init_function_python_additional_code_require_opengl_initialized

    return options


def _preprocess_imgui_code(code: str) -> str:
    """
    The imgui code uses two macros (IM_FMTARGS and IM_FMTLIST) which help the compiler
        #define IM_FMTARGS(FMT)             __attribute__((format(printf, FMT, FMT+1)))
        #define IM_FMTLIST(FMT)             __attribute__((format(printf, FMT, 0)))

    They are used like this:
        IMGUI_API bool          TreeNode(const char* str_id, const char* fmt, ...) IM_FMTARGS(2);

    They are removed before processing the header, because they would not be correctly interpreted by srcml.
    """
    import re

    new_code = code
    new_code = re.sub(r"IM_FMTARGS\(\d\)", "", new_code)
    new_code = re.sub(r"IM_FMTLIST\(\d\)", "", new_code)
    return new_code


def code_style_imgui() -> LitgenOptions:
    from litgen.internal import cpp_to_python

    options = LitgenOptions()

    options.generate_to_string = False
    options.cpp_indent_size = 4

    options.code_replacements = cpp_to_python.standard_code_replacements()
    options.code_replacements += code_replacements.parse_string_replacements(
        r"""
        \bImVector\s*<\s*([\w:]*)\s*> -> List[\1]
        """
    )

    options.original_location_flag_show = True
    # options.original_signature_flag_show = True

    options.buffer_flag_replace_by_array = True

    options.srcml_options.functions_api_prefixes = ["IMGUI_API"]
    options.srcml_options.header_guard_suffixes.append("IMGUI_DISABLE")

    options.buffer_types += ["float"]
    options.c_array_numeric_member_types += [
        "ImGuiID",
        "ImS8",
        "ImU8",
        "ImS16",
        "ImU16",
        "ImS32",
        "ImU32",
        "ImS64",
        "ImU64",
    ]

    options.srcml_options.code_preprocess_function = _preprocess_imgui_code

    options.srcml_options.function_name_exclude_regexes = [
        # IMGUI_API void          SetAllocatorFunctions(ImGuiMemAllocFunc alloc_func, ImGuiMemFreeFunc free_func, void* user_data = NULL);
        #                                               ^
        # IMGUI_API void          GetAllocatorFunctions(ImGuiMemAllocFunc* p_alloc_func, ImGuiMemFreeFunc* p_free_func, void** p_user_data);
        #                                               ^
        # IMGUI_API void*         MemAlloc(size_t size);
        #           ^
        # IMGUI_API void          MemFree(void* ptr);
        #                                 ^
        r"\bGetAllocatorFunctions\b",
        r"\bSetAllocatorFunctions\b",
        r"\bMemAlloc\b",
        r"\bMemFree\b",
        # IMGUI_API void              GetTexDataAsAlpha8(unsigned char** out_pixels, int* out_width, int* out_height, int* out_bytes_per_pixel = NULL);  // 1 byte per-pixel
        #                                                             ^
        # IMGUI_API void              GetTexDataAsRGBA32(unsigned char** out_pixels, int* out_width, int* out_height, int* out_bytes_per_pixel = NULL);  // 4 bytes-per-pixel
        #                                                             ^
        r"\bGetTexDataAsAlpha8\b",
        r"\bGetTexDataAsRGBA32\b",
        # IMGUI_API ImVec2            CalcTextSizeA(float size, float max_width, float wrap_width, const char* text_begin, const char* text_end = NULL, const char** remaining = NULL) const; // utf8
        #                                                                                                                                                         ^
        r"\bCalcTextSizeA\b",
        "appendfv",
        # Exclude function whose name ends with V, like for example
        #       IMGUI_API void          TextV(const char* fmt, va_list args)                            IM_FMTLIST(1);
        # which are utilities for variadic print format
        r"\w*V\Z",
    ]

    options.srcml_options.decl_name_exclude_regexes = [
        #     typedef void (*ImDrawCallback)(const ImDrawList* parent_list, const ImDrawCmd* cmd);
        #     ImDrawCallback  UserCallback;       // 4-8  // If != NULL, call the function instead of rendering the vertices. clip_rect and texture_id will be set normally.
        #     ^
        r"\bUserCallback\b",
        # struct ImDrawData
        # { ...
        #     ImDrawList**    CmdLists;               // Array of ImDrawList* to render. The ImDrawList are owned by ImGuiContext and only pointed to from here.
        #               ^
        # }
        r"\bCmdLists\b",
    ]

    options.srcml_options.class_name_exclude_regexes = [r"^ImVector\b"]

    return options


def code_style_implot() -> LitgenOptions:
    options = code_style_imgui()
    options.srcml_options.functions_api_prefixes = ["IMPLOT_API", "IMPLOT_TMP"]

    options.srcml_options.function_name_exclude_regexes = [
        #  Legitimate Excludes
        # Exclude functions whose name end with G, like for example
        #       IMPLOT_API void PlotLineG(const char* label_id, ImPlotGetter getter, void* data, int count);
        # which are made for specialized C/C++ getters
        r"\w*G\Z",
        # Exclude function whose name ends with V, like for example
        #       IMPLOT_API void TagXV(double x, const ImVec4& color, const char* fmt, va_list args) IM_FMTLIST(3);
        # which are utilities for variadic print format
        r"\w*V\Z",
        #  Excludes due to two-dimensional buffer
        #  PlotHeatmap(.., const T* values, int rows, int cols, !!!
        #                            ^          ^          ^
        "PlotHeatmap",
        #  Excludes due to antique style string vectors
        #  for which there is no generalizable parse
        # void SetupAxisTicks(ImAxis idx, const double* values, int n_ticks, const char* const labels[], bool show_default)
        #                                                            ^                           ^
        "SetupAxisTicks",
        # void PlotBarGroupsH(const char* const label_ids[], const T* values, int item_count, int group_count, double group_height=0.67, double y0=0, ImPlotBarGroupsFlags flags=ImPlotBarGroupsFlags_None);
        # void PlotBarGroups (const char* const label_ids[], const T* values, int item_count, int group_count, double group_width=0.67, double x0=0, ImPlotBarGroupsFlags flags=ImPlotBarGroupsFlags_None);
        #                                            ^                                ^
        "PlotBarGroups",
        "PlotBarGroupsH",
        # void PlotPieChart(const char* const label_ids[], const T* values, int count, double x, double y, double radius, bool normalize=false, const char* label_fmt="%.1f", double angle0=90);
        #                                         ^                               ^
        "PlotPieChart",
    ]

    return options
