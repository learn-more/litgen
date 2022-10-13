# ============================================================================
# This file was autogenerated
# It is presented side to side with its source: enum_test.h
#    (see integration_tests/bindings/lg_mylib/__init__pyi which contains the full
#     stub code, including this code)
# ============================================================================

# type: ignore
import sys
from typing import Literal, List, Any, Optional, Tuple, Dict
import numpy as np
from enum import Enum, auto
import numpy

# <litgen_stub> // Autogenerated code below! Do not edit!
####################    <generated_from:enum_test.h>    ####################

class BasicEnum(Enum):
    """ BasicEnum: a simple C-style enum"""
    # C-style enums often contain a prefix that is the enum name in itself, in order
    # not to pollute the parent namespace.
    # Since enum members do not leak to the parent namespace in python, litgen will remove the prefix by default.

    a = enum.auto()   # (= 1)  # This will be exported as BasicEnum.a
    aa = enum.auto()  # (= 2)  # This will be exported as BasicEnum.aa
    aaa = enum.auto() # (= 3)  # This will be exported as BasicEnum.aaa

    # Lonely comment

    # This is value b
    b = enum.auto()   # (= 4)



class ClassEnum(Enum):
    """ ClassEnum: a class enum that should be published"""
    on = enum.auto()      # (= 0)
    off = enum.auto()     # (= 1)
    unknown = enum.auto() # (= 2)


####################    </generated_from:enum_test.h>    ####################

# </litgen_stub> // Autogenerated code end!
