from typing import List
from typing import (
    Literal,  # for enums annotations, when some enum values depend on other values of the same enum
)
import numpy
from enum import Enum

# Disable black formatter
# fmt: off

# TODO:
#  * Remove these decls, they will be autogenerated later
#  * Reactivate the two overloads of add and see how to deal with them
#         // Adds two numbers
#         MY_API inline int add(int a, int b) { return a + b; }
#         // Adds three numbers, with a surprise
#         // MY_API inline int add(int a, int b, int c) { return a + b + c + 4; }



class BoxedUnsignedLong:
    value: float = 0

    def __init___(self, value = 0.):
        self.value = value
    def __repr__(self):
        return f"BoxedUnsignedLong({self.value})"


class BoxedInt:
    value: int = 0

    def __init___(self, value = 0.):
        self.value = value
    def __repr__(self):
        return f"BoxedInt({self.value})"


class Point2:
    x: int
    y: int


class Foo:
    pass


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# <autogen:pyi> // Autogenerated code below! Do not edit!





# <namespace LiterateGeneratorExample>    # example_library/litgensample.h:35

class MyEnum(Enum):    # example_library/litgensample.h:40
    """ A super nice enum
     for demo purposes ( bool val = False )
    """
    a = 1    # This is value a
    aa = 2   # this is value aa
    aaa = 3  # this is value aaa

    #  Lonely comment

    #  This is value b
    b = 4

    #  This is c
    #  with doc on several lines
    c = Literal[MyEnum.a] | Literal[MyEnum.b]


#
#  C Style array tests
#

#  Tests with Boxed Numbers
def add_c_array2(values: List[int]) -> int:    # example_library/litgensample.h:63
    pass
def log_c_array2(values: List[int]) -> None:    # example_library/litgensample.h:64
    pass
def change_c_array2(    # example_library/litgensample.h:65
    values_0: BoxedUnsignedLong,
    values_1: BoxedUnsignedLong
    ) -> None:
    pass
def get_points(out_0: Point2, out_1: Point2) -> None:    # example_library/litgensample.h:75
    pass

#
#  C Style buffer to numpy.ndarray tests
#

def add_inside_buffer(buffer: numpy.ndarray, number_to_add: int) -> None:    # example_library/litgensample.h:82
    """ Modifies a buffer by adding a value to its elements"""
    pass
def buffer_sum(buffer: numpy.ndarray, stride: int = -1) -> int:    # example_library/litgensample.h:88
    """ Returns the sum of a  buffer"""
    pass
def add_inside_two_buffers(    # example_library/litgensample.h:96
    buffer_1: numpy.ndarray,
    buffer_2: numpy.ndarray,
    number_to_add: int
    ) -> None:
    """ Modifies two buffers"""
    pass


def mul_inside_buffer(buffer: numpy.ndarray, factor: float) -> None:    # example_library/litgensample.h:107
    """ Modify an array by multiplying its elements (template function!)"""
    pass

#
#  C String lists tests
#

def c_string_list_total_size(    # example_library/litgensample.h:117
    items: List[str],
    output_0: BoxedInt,
    output_1: BoxedInt
    ) -> int:
    pass


def add(a: int, b: int) -> int:    # example_library/litgensample.h:129
    """ Adds two numbers"""
    pass

#  Adds three numbers, with a surprise
#  MY_API inline int add(int a, int b, int c) { return a + b + c + 4; }


def sub(a: int, b: int) -> int:    # example_library/litgensample.h:135
    pass

def mul(a: int, b: int) -> int:    # example_library/litgensample.h:137
    pass


def foo_instance() -> Foo:    # example_library/litgensample.h:176
    """ return_value_policy::reference"""
    pass

#     MY_API None ToggleBool(bool v) {
#         printf("ToggleBool ptr=%p value=%s\n", v, (v) ? "True" : "False");
#         v = !(v);
#     }
#
#     MY_API None ToggleBool2(std::shared_ptr<bool> v) {
#         bool b = v.get();
#         printf("ToggleBool2 ptr=%p value=%s\n", b, (b) ? "True" : "False");
#         b = !(b);
#     }
#
# </namespace LiterateGeneratorExample>

# </autogen:pyi>

# fmt: on
