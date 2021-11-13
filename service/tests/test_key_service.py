import os
import pytest
from ..core.handlers import KeyHandler
from ..core.exceptions import VariableNotFoundException


def test_key_service_return_encryption_key():
    key = 'very secure key'
    os.environ['encryption_key'] = key
    assert KeyHandler().encryption_key == key

def test_key_service_return_encryption_iv():
    iv = "9w30I+uEm1c+onjjyk4N1w=="
    os.environ['encryption_iv'] = iv
    assert KeyHandler().encryption_iv == iv

def test_key_service_raise_exception_for_encryption_key():
    del os.environ['encryption_key']
    with pytest.raises(VariableNotFoundException) as excinfo:
        KeyHandler().encryption_key
        assert str(excinfo.value) == "The variable encryption_key doesn't exist in the environment."

def test_key_service_raise_exception_for_encryption_iv():
    del os.environ['encryption_iv']
    with pytest.raises(VariableNotFoundException) as excinfo:
        KeyHandler().encryption_iv
        assert str(excinfo.value) == "The variable encryption_iv doesn't exist in the environment."