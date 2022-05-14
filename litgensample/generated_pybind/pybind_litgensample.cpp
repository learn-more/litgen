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


        .def("instance",
            [](Foo& self)
            {
                { return self.Instance(); }
            },
            ""
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


    m.def("test_with_one_const_buffer",
        [](const py::array & values)
        {
            // convert values (py::array&) to C standard buffer (const)
            const void* values_buffer = values.data();
            int values_count = values.shape()[0];
            
            char array_type = values.dtype().char_();
            if (array_type != 'b')
                throw std::runtime_error(std::string(R"msg(
                        Bad type!  Expected a buffer of native type:
                                    const int8_t*
                                Which is equivalent to 
                                    b
                                (using py::array::dtype().char_() as an id)
                    )msg"));
            { return test_with_one_const_buffer(static_cast<const int8_t*>(values_buffer), values_count); }
        },
        py::arg("values"),
        ""
    );


    m.def("test_with_one_nonconst_buffer",
        [](py::array & values)
        {
            // convert values (py::array&) to C standard buffer (mutable)
            void* values_buffer = values.mutable_data();
            int values_count = values.shape()[0];
            
            char array_type = values.dtype().char_();
            if (array_type != 'b')
                throw std::runtime_error(std::string(R"msg(
                        Bad type!  Expected a buffer of native type:
                                    int8_t*
                                Which is equivalent to 
                                    b
                                (using py::array::dtype().char_() as an id)
                    )msg"));
            { test_with_one_nonconst_buffer(static_cast<int8_t*>(values_buffer), values_count); return; }
        },
        py::arg("values"),
        ""
    );


    m.def("test_with_one_template_buffer",
        [](const py::array & values)
        {
            // convert values (py::array&) to C standard buffer (const)
            const void* values_buffer = values.data();
            int values_count = values.shape()[0];
            
            char array_type = values.dtype().char_();
            if (array_type == 'B')
                { return test_with_one_template_buffer(static_cast<const uint8_t*>(values_buffer), values_count); }
            if (array_type == 'b')
                { return test_with_one_template_buffer(static_cast<const int8_t*>(values_buffer), values_count); }
            if (array_type == 'H')
                { return test_with_one_template_buffer(static_cast<const uint16_t*>(values_buffer), values_count); }
            if (array_type == 'h')
                { return test_with_one_template_buffer(static_cast<const int16_t*>(values_buffer), values_count); }
            if (array_type == 'I')
                { return test_with_one_template_buffer(static_cast<const uint32_t*>(values_buffer), values_count); }
            if (array_type == 'i')
                { return test_with_one_template_buffer(static_cast<const int32_t*>(values_buffer), values_count); }
            if (array_type == 'L')
                { return test_with_one_template_buffer(static_cast<const uint64_t*>(values_buffer), values_count); }
            if (array_type == 'l')
                { return test_with_one_template_buffer(static_cast<const int64_t*>(values_buffer), values_count); }
            if (array_type == 'f')
                { return test_with_one_template_buffer(static_cast<const float*>(values_buffer), values_count); }
            if (array_type == 'd')
                { return test_with_one_template_buffer(static_cast<const double*>(values_buffer), values_count); }
            if (array_type == 'g')
                { return test_with_one_template_buffer(static_cast<const long double*>(values_buffer), values_count); }

            // If we arrive here, the array type is not supported!
            throw std::runtime_error(std::string("Bad array type: ") + array_type );
        },
        py::arg("values"),
        ""
    );


    m.def("test_with_two_template_buffers",
        [](const py::array & values1, py::array & values2)
        {
            // convert values1 (py::array&) to C standard buffer (const)
            const void* values1_buffer = values1.data();
            int values1_count = values1.shape()[0];
            
            // convert values2 (py::array&) to C standard buffer (mutable)
            void* values2_buffer = values2.mutable_data();
            int values2_count = values2.shape()[0];
            
            char array_type = values1.dtype().char_();
            if (array_type == 'B')
                { return test_with_two_template_buffers(static_cast<const uint8_t*>(values1_buffer), static_cast<uint8_t*>(values2_buffer), values1_count); }
            if (array_type == 'b')
                { return test_with_two_template_buffers(static_cast<const int8_t*>(values1_buffer), static_cast<int8_t*>(values2_buffer), values1_count); }
            if (array_type == 'H')
                { return test_with_two_template_buffers(static_cast<const uint16_t*>(values1_buffer), static_cast<uint16_t*>(values2_buffer), values1_count); }
            if (array_type == 'h')
                { return test_with_two_template_buffers(static_cast<const int16_t*>(values1_buffer), static_cast<int16_t*>(values2_buffer), values1_count); }
            if (array_type == 'I')
                { return test_with_two_template_buffers(static_cast<const uint32_t*>(values1_buffer), static_cast<uint32_t*>(values2_buffer), values1_count); }
            if (array_type == 'i')
                { return test_with_two_template_buffers(static_cast<const int32_t*>(values1_buffer), static_cast<int32_t*>(values2_buffer), values1_count); }
            if (array_type == 'L')
                { return test_with_two_template_buffers(static_cast<const uint64_t*>(values1_buffer), static_cast<uint64_t*>(values2_buffer), values1_count); }
            if (array_type == 'l')
                { return test_with_two_template_buffers(static_cast<const int64_t*>(values1_buffer), static_cast<int64_t*>(values2_buffer), values1_count); }
            if (array_type == 'f')
                { return test_with_two_template_buffers(static_cast<const float*>(values1_buffer), static_cast<float*>(values2_buffer), values1_count); }
            if (array_type == 'd')
                { return test_with_two_template_buffers(static_cast<const double*>(values1_buffer), static_cast<double*>(values2_buffer), values1_count); }
            if (array_type == 'g')
                { return test_with_two_template_buffers(static_cast<const long double*>(values1_buffer), static_cast<long double*>(values2_buffer), values1_count); }

            // If we arrive here, the array type is not supported!
            throw std::runtime_error(std::string("Bad array type: ") + array_type );
        },
        py::arg("values1"),
        py::arg("values2"),
        ""
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


    m.def("sub",
        [](int a, int b)
        {
            { return sub(a, b); }
        },
        py::arg("a"),
        py::arg("b"),
        ""
    );


    m.def("mul",
        [](int a, int b)
        {
            { return mul(a, b); }
        },
        py::arg("a"),
        py::arg("b"),
        ""
    );


    m.def("foo_instance",
        []()
        {
            { return FooInstance(); }
        },
        ""
    );


// </autogen:pydef_cpp> // Autogenerated code below! Do not edit!
// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE END !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

}