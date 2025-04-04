![Pip](https://github.com/pthom/litgen/workflows/pip/badge.svg)


# litgen - Literate Generator

**litgen** is an automatic Python bindings generator designed for developers who appreciate clean, well-documented, and discoverable code and APIs.

It simplifies the process of creating Python bindings for C++ libraries using [pybind11](https://pybind11.readthedocs.io/en/stable/) or [nanobind](https://nanobind.readthedocs.io), and generating bindings that are easy to use, properly documented, and fully integrated into Python IDEs.

For a full guide on how to use litgen, see the [documentation](https://pthom.github.io/litgen/).

## Key Features
- Automatically generates Python bindings for C++ libraries.
- Generates fully documented and discoverable Python code, ensuring smooth interaction for end users.
- Provides IDE-friendly bindings with accurate function signatures and auto-completion.
- Works as a C++ transformation and refactoring tool, useful for various workflows.

## Documentation

To dive deeper into how litgen works, check out the [full documentation](https://pthom.github.io/litgen/).

## Battle-Tested
Though relatively new (released in 2022), litgen has been extensively tested on over 20 different libraries, totaling more than 100,000 lines of code. It is the main engine behind the Python bindings for the popular [Dear ImGui Bundle](https://github.com/pthom/imgui_bundle).

## Keep in Touch

We’d love to hear about how you're using litgen! If you are using it, please consider [sharing your experience and insights](https://github.com/pthom/litgen/discussions).

## Help the Project

If litgen has made a difference for you—especially in a commercial or research setting—please consider [making a donation](https://www.paypal.com/donate/?hosted_button_id=SHJ68RVDKURZA). Your support helps keep the project alive and growing. Every contribution, no matter the size, is greatly appreciated!


## Contributions

Contributions are welcome! If you'd like to report a bug, suggest a feature, or submit a pull request, please visit our [GitHub issues page](https://github.com/pthom/litgen/issues). See the developer documentation inside [Build.md](Build.md)

**Notable contributors:**
* Many thanks to [@davidlatwe](https://github.com/davidlatwe) for his contributions to the nanobind support in litgen!

## License

litgen is published under the [GNU General Public License, version 3](https://raw.githubusercontent.com/pthom/litgen/main/LICENSE.txt). Code generated by litgen is **not** subject to GPL, allowing you to freely use it in your projects.
