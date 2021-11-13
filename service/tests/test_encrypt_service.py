import pytest
import base64
from Crypto import Random
from Crypto.Cipher import AES
from ..core.libs.encrypt_lib import encrypt_text, decrypt_text

def iv_key():
    iv = Random.new().read(AES.block_size)
    iv_str = base64.b64encode(iv).decode('ascii')
    return iv_str    

key = "very_secure_key"
values_encrypt = [
    ("hello", "9w30I+uEm1c+onjjyk4N1w==", key, '9w30I+uEm1c+onjjyk4N10a9fLs6O4juxO5mXK4m9aM='),
    ("hello", "9w30I+uEm1c+onjjyk4N1w==", key, '9w30I+uEm1c+onjjyk4N10a9fLs6O4juxO5mXK4m9aM='),
    ("hello", "9w30I+uEm1c+onjjyk4N1w==", key, '9w30I+uEm1c+onjjyk4N10a9fLs6O4juxO5mXK4m9aM=')
]


@pytest.mark.parametrize('text, iv, key, expected_output', values_encrypt)
def test_encrypt_text_must_be_idempotent(text: str, iv: str, key: str, expected_output: str) -> None:
    assert encrypt_text(text, iv, key) == expected_output


values_decrypt = [
    ('9w30I+uEm1c+onjjyk4N10a9fLs6O4juxO5mXK4m9aM=', key, 'hello'),
    ('9w30I+uEm1c+onjjyk4N10a9fLs6O4juxO5mXK4m9aM=', key, 'hello'),
    ('9w30I+uEm1c+onjjyk4N10a9fLs6O4juxO5mXK4m9aM=', key, 'hello')
]

@pytest.mark.parametrize('encrypted_text, key, decrypted_text', values_decrypt)
def test_decrypt_text_must_return_original_value(encrypted_text: str, key:str, decrypted_text:str) -> None:
    assert decrypt_text(encrypted_text, key) == decrypted_text