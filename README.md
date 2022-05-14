`litgen` is a pybind11 literate automatic generator for humans who like nice code and API.


_Work in progress, and not ready to be used outside its nest yet! Expect bugs and refactorings at a rapid pace!_

## Quick demo:

### Starting point: a documented and consistent C++ API

Below, is a simple API which we would like to publish to Python. 

As you can see:
* It is nicely documented, and we would like this doc to be seen from Python
* It handles arrays via template functions, and we would like to be able to use these functions with python/numpy arrays

```cpp
#pragma once
#ifndef MY_API
#define MY_API
#endif

namespace LiterateGeneratorExample
{
    // Adds two numbers
    MY_API inline int add(int a, int b) { return a + b; }

    // Adds three numbers, with a surprise
    MY_API inline int add(int a, int b, int c) { return a + b + c + 4; }

    // Modify an array by multiplying its elements (template function!)
    MY_API template<typename T> void mul_inside_array(T* array, size_t array_size, double factor)
    {
        for (size_t i  = 0; i < array_size; ++i)
            array[i] *= (T)factor;
    }
    
    // Modify an array by adding a value to its elements (*non* template function)
    MY_API inline void add_inside_array(uint8_t* array, size_t array_size, uint8_t number_to_add)
    {
        for (size_t i  = 0; i < array_size; ++i)
            array[i] += number_to_add;
    }
    
    
    // A superb struct
    struct Foo            // MY_API_STRUCT
    {
        // Multiplication factor
        int factor = 10;

        // addition factor
        int delta = 0;

        // Do some math
        int calc(int x) { return x * factor + delta; }
    };

} // namespace LiterateGeneratorExample


````

### Interactive Python session with this API

Below, is an example interactive session with this class; after it was published to Python 
(using code generated by `litgen`).

As you can see:
* We have access to all the structs, function, and methods
* We have acces to all the doc
* Python/Numpy arrays are transferred transparently
* With arrays, type checkings are made automatically. In case of an error, the user is informed with a nice message


````python
> python

>>> import litgensample

>>> # Read the doc
>>> help(litgensample.add)
"""
Help on built-in function add in module litgensample:

add(...) method of builtins.PyCapsule instance
    add(*args, **kwargs)
    Overloaded function.
    
    1. add(a: int, b: int) -> int
    
    Adds two numbers
    
    2. add(a: int, b: int, c: int) -> int
    
    Adds three numbers, with a surprise
"""
>>> litgensample.add(3,4)
7


>>> help(litgensample.mul_inside_array)
"""
Help on built-in function mul_inside_array in module litgensample:

mul_inside_array(...) method of builtins.PyCapsule instance
    mul_inside_array(array: numpy.ndarray, factor: float) -> None

    Modify an array by adding a value to its elements (template function!)
"""

>>> import numpy as np
>>> a = np.ones((10), np.int32)
>>> a
array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], dtype=int32)

>>> # We can use the templated array function with almost any type
>>> litgensample.mul_inside_array(a, 10)
>>> a
array([10, 10, 10, 10, 10, 10, 10, 10, 10, 10], dtype=int32)

>>> # If we use the non templated array function with bad element types
>>> # we are informed with a nice message
>>> litgensample.add_inside_array(a, 10)
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
RuntimeError:
        Bad type!  Expected a buffer of native type:
            uint8_t*
        Which is equivalent to
            B
        (using py::array::dtype().char_() as an id)


>>> help(litgensample.Foo)
"""
Help on class Foo in module litgensample:

class Foo(pybind11_builtins.pybind11_object)
 |  A superb struct
 |
 |  Method resolution order:
 |      Foo
 |      pybind11_builtins.pybind11_object
 |      builtins.object
 |
 |  Methods defined here:
 |
 |  __init__(...)
 |      __init__(self: litgensample.Foo) -> None
 |
 |  calc(...)
 |      calc(self: litgensample.Foo, x: int) -> int
 |
 |      Do some math
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  delta
 |      addition factor
 |
 |  factor
 |      Multiplication factor
"""

>>> f = litgensample.Foo()
>>> f.calc(3)
30
````


### Python bindings generated by `litgen`

Below is the generated code that made this possible

````cpp
#include "litgensample.h"

#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <stdint.h>

namespace py = pybind11;


void py_init_module_litgensample(py::module& m)
{
    using namespace LiterateGeneratorExample;

// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
// <autogen:pydef_cpp> // Autogenerated code below! Do not edit!

    auto pyClassFoo = py::class_<Foo>
        (m, "Foo", 
        "A superb struct")

        .def(py::init<>()) 
        .def_readwrite("factor", &Foo::factor, "Multiplication factor")
        .def_readwrite("delta", &Foo::delta, "addition factor")

        .def("calc",
            [](Foo& self, int x)
            {
                { return self.calc(x); }
            },
            py::arg("x"),
            "Do some math"
        )

        ; 


    m.def("add",
        [](int a, int b)
        {
            { return add(a, b); }
        },
        py::arg("a"),
        py::arg("b"),
        "Adds two numbers"
    );


    m.def("add",
        [](int a, int b, int c)
        {
            { return add(a, b, c); }
        },
        py::arg("a"),
        py::arg("b"),
        py::arg("c"),
        "Adds three numbers, with a surprise"
    );


    m.def("mul_inside_array",
        [](py::array & array, double factor)
        {
            // convert array (py::array&) to C standard buffer (mutable)
            void* array_buffer = array.mutable_data();
            int array_count = array.shape()[0];
            
            char array_type = array.dtype().char_();
            if (array_type == 'B')
                { mul_inside_array(static_cast<uint8_t*>(array_buffer), array_count, factor); return; }
            if (array_type == 'b')
                { mul_inside_array(static_cast<int8_t*>(array_buffer), array_count, factor); return; }
            if (array_type == 'H')
                { mul_inside_array(static_cast<uint16_t*>(array_buffer), array_count, factor); return; }
            if (array_type == 'h')
                { mul_inside_array(static_cast<int16_t*>(array_buffer), array_count, factor); return; }
            if (array_type == 'I')
                { mul_inside_array(static_cast<uint32_t*>(array_buffer), array_count, factor); return; }
            if (array_type == 'i')
                { mul_inside_array(static_cast<int32_t*>(array_buffer), array_count, factor); return; }
            if (array_type == 'L')
                { mul_inside_array(static_cast<uint64_t*>(array_buffer), array_count, factor); return; }
            if (array_type == 'l')
                { mul_inside_array(static_cast<int64_t*>(array_buffer), array_count, factor); return; }
            if (array_type == 'f')
                { mul_inside_array(static_cast<float*>(array_buffer), array_count, factor); return; }
            if (array_type == 'd')
                { mul_inside_array(static_cast<double*>(array_buffer), array_count, factor); return; }
            if (array_type == 'g')
                { mul_inside_array(static_cast<long double*>(array_buffer), array_count, factor); return; }

            // If we arrive here, the array type is not supported!
            throw std::runtime_error(std::string("Bad array type: ") + array_type );
        },
        py::arg("array"),
        py::arg("factor"),
        "Modify an array by multiplying its elements (template function!)"
    );


    m.def("add_inside_array",
        [](py::array & array, uint8_t number_to_add)
        {
            // convert array (py::array&) to C standard buffer (mutable)
            void* array_buffer = array.mutable_data();
            int array_count = array.shape()[0];
            
            char array_type = array.dtype().char_();
            if (array_type != 'B')
                throw std::runtime_error(std::string(R"msg(
                        Bad type!  Expected a buffer of native type:
                                    uint8_t*
                                Which is equivalent to 
                                    B
                                (using py::array::dtype().char_() as an id)
                    )msg"));
            { add_inside_array(static_cast<uint8_t*>(array_buffer), array_count, number_to_add); return; }
        },
        py::arg("array"),
        py::arg("number_to_add"),
        "Modify an array by adding a value to its elements (non template function)"
    );


// </autogen:pydef_cpp> // Autogenerated code below! Do not edit!
// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE END !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

}````

## Build sample library (litgensample)

````bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt
pip install -v -e .
````

