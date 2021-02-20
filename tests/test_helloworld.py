"""
"""
import pconway.helloworld
import pconway.clitools


def test_helloworld():
    string = pconway.helloworld.helloworlds(1)
    assert string == 'Hello World!'
