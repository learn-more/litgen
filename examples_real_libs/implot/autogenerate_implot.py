import os, sys

THIS_DIR = os.path.dirname(__file__)
sys.path = [THIS_DIR + "/../../pybind_autogenerator"] + sys.path
from code_generator import (
    perform_generation,
    remove_all_generated_code,
    CppCodeType,
    code_style_implot,
)
import os

THIS_DIR = os.path.dirname(__file__)
IMPLOT_DIR = (
    THIS_DIR + "/../../../thirdparty/mahi-gui/3rdparty/implot"
)  # pybind/py-mahi-gui/thirdparty/mahi-gui/3rdparty/implot
IMPLOT_PYBIND_DIR = THIS_DIR + "/../../../src"
assert os.path.isdir(IMPLOT_DIR)
assert os.path.isdir(THIS_DIR)
assert os.path.isdir(IMPLOT_PYBIND_DIR)


def autogenerate_implot():
    input_header_file = IMPLOT_DIR + "/implot.h"
    dst_file = IMPLOT_PYBIND_DIR + "/implot.cpp"

    # remove_all_generated_code(dst_file)
    # return

    # Configure options
    code_style_options = code_style_implot()

    for code_type in CppCodeType:
        print(f"{code_type=}")
        perform_generation(input_header_file, dst_file, code_type, code_style_options)


if __name__ == "__main__":
    autogenerate_implot()
