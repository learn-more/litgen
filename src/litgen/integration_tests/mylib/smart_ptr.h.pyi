# ============================================================================
# This file was autogenerated
# It is presented side to side with its source: smart_ptr.h
#    (see integration_tests/bindings/lg_mylib/__init__pyi which contains the full
#     stub code, including this code)
# ============================================================================
from typing import List

# type: ignore

# <litgen_stub> // Autogenerated code below! Do not edit!
####################    <generated_from:smart_ptr.h>    ####################

class SmartElem:
    x: int = 0
    def __init__(self, x: int = 0) -> None:
        """Auto-generated default constructor with named params"""
        pass

def make_shared_elem(x: int) -> SmartElem:
    pass

class ElemContainer:
    def __init__(self) -> None:
        pass
    vec: List[SmartElem]
    shared_ptr: SmartElem
    vec_shared_ptrs: List[SmartElem]

# The signature below is incompatible with pybind11:
#     None change_unique_elem(std::unique_ptr<Elem>& elem, int x) { ... }
# Reason: such a signature might change the pointer value! Example:
#    None reset_unique_elem(std::unique_ptr<Elem>& elem) { elem.reset(new Elem());    }
####################    </generated_from:smart_ptr.h>    ####################

# </litgen_stub> // Autogenerated code end!
