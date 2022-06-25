import inspect
import logging
import sys
import traceback
from dataclasses import dataclass
from typing import List, Optional, Tuple
from xml.etree import ElementTree as ET  # noqa

from codemanip import code_utils
from codemanip.code_position import CodePosition

import srcmlcpp
from srcmlcpp import srcml_types
from srcmlcpp.internal import srcml_utils, srcml_main_deprecated
from srcmlcpp.srcml_exception import SrcMlException
from srcmlcpp.srcml_options import SrcmlOptions


###########################################
#
# Error and warning messages
#
###########################################


@dataclass
class ErrorContext:
    concerned_lines: List[str]
    start: Optional[CodePosition] = None
    end: Optional[CodePosition] = None

    def __str__(self) -> str:
        msg = ""
        for i, line in enumerate(self.concerned_lines):
            msg += line + "\n"
            if self.start is not None:
                if i == self.start.line:
                    nb_spaces = self.start.column - 1
                    if nb_spaces < 0:
                        nb_spaces = 0
                    msg += " " * nb_spaces + "^" + "\n"

        return msg


def _extract_error_context(element: ET.Element) -> ErrorContext:
    cpp_element = srcml_types.CppElement(element)

    full_code = srcml_main_deprecated.srcml_main_context().current_parsed_file_unit_code
    if len(full_code) > 0:
        full_code_lines = [""] + full_code.split("\n")

        start = cpp_element.start()
        end = cpp_element.end()
        if start is not None and end is not None and len(full_code) > 0:
            concerned_lines = full_code_lines[start.line : end.line + 1]
            new_start = CodePosition(0, start.column)
            new_end = CodePosition(
                end.line - start.line,
                end.column,
            )
            return ErrorContext(concerned_lines, new_start, new_end)
        else:
            return ErrorContext([], CodePosition(), CodePosition())
    else:
        original_code = srcmlcpp.srcml_to_code(element)
        return ErrorContext(original_code.split("\n"), cpp_element.start(), cpp_element.end())


def _highlight_responsible_code(element: ET.Element) -> str:
    error_context = _extract_error_context(element)
    return str(error_context)


def _show_element_info(element: ET.Element, encoding: str) -> str:
    def file_location(element: ET.Element):
        header_filename = srcml_main_deprecated.srcml_main_context().current_parsed_file
        if len(header_filename) == 0:
            header_filename = "Position"
        start = srcml_utils.element_start_position(element)
        if start is not None:
            return f"{header_filename}:{start.line}:{start.column}"
        else:
            return f"{header_filename}"

    element_tag = srcml_utils.clean_tag_or_attrib(element.tag)
    concerned_code = _highlight_responsible_code(element)
    message = f"""
    While parsing a "{element_tag}", corresponding to this C++ code:
    {file_location(element)}
{code_utils.indent_code(concerned_code, 12)}
    """
    return message


def _warning_detailed_info(
    options: SrcmlOptions, current_element: Optional[ET.Element], additional_message: str
) -> str:
    def _get_python_call_info() -> Tuple[str, str]:
        stack_lines = traceback.format_stack()
        error_line = stack_lines[-4]
        frame = inspect.currentframe()  # type: ignore
        if frame is not None:
            caller_function_name = inspect.getframeinfo(frame.f_back.f_back.f_back).function  # type: ignore
        else:
            caller_function_name = ""
        return caller_function_name, error_line

    python_caller_function_name, python_error_line = _get_python_call_info()

    def show_python_callstack() -> str:
        return f"""
                Python call stack info:
        {code_utils.indent_code(python_error_line, 4)}
        """

    message = ""

    if current_element is not None:
        message += _show_element_info(current_element, options.encoding)

    if options.flag_show_python_callstack:
        message += show_python_callstack()

    if len(additional_message) > 0:
        message = (
            code_utils.unindent_code(additional_message, flag_strip_empty_lines=True)
            + "\n"
            + code_utils.unindent_code(message, flag_strip_empty_lines=True)
        )

    return message


class SrcMlExceptionDetailed(SrcMlException):
    def __init__(self, options: SrcmlOptions, current_element: Optional[ET.Element], additional_message: str) -> None:
        message = _warning_detailed_info(
            options=options, current_element=current_element, additional_message=additional_message
        )
        super().__init__(message)


def emit_srcml_warning(
    options: SrcmlOptions,
    current_element: Optional[ET.Element],
    additional_message: str,
    message_header: str = "Warning",
) -> None:
    if options.flag_quiet:
        return
    message = _warning_detailed_info(options, current_element, additional_message)

    in_pytest = "pytest" in sys.modules
    if in_pytest:
        logging.warning(message)
    else:
        print(f"{message_header}: " + message, file=sys.stderr)


def emit_warning(options: SrcmlOptions, message: str) -> None:
    if options.flag_quiet:
        return
    in_pytest = "pytest" in sys.modules
    if in_pytest:
        logging.warning(message)
    else:
        print("Warning: " + message, file=sys.stderr)
