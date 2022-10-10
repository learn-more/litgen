import litgen


def test_multiple_options_instances():
    options1 = litgen.options.LitgenOptions()
    options1.python_convert_to_snake_case = False
    options1.srcmlcpp_options.functions_api_prefixes = "SOME_API"
    options2 = litgen.LitgenOptions()
    assert id(options1) != id(options2)
    assert id(options1.srcmlcpp_options) != id(options2.srcmlcpp_options)
    assert len(options2.srcmlcpp_options.functions_api_prefixes) == 0
