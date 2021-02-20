"""
"""
import mypythonlibrary.helloworld
import mypythonlibrary.clitools


def test_helloworld():
    string = mypythonlibrary.helloworld.helloworlds(1)
    assert string == 'Hello World!'
