import lg_mylib


def test_namespace():
    assert "details" not in dir(lg_mylib)

    assert "local_function" not in dir(lg_mylib)

    assert "Inner" in dir(lg_mylib)
    assert lg_mylib.Inner.foo_inner() == 45
    assert lg_mylib.Inner.foo_inner2() == 46