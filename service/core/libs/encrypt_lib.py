import base64
import hashlib
from typing import Union
from Crypto.Cipher import AES
import logging


def encrypt_text(text: str, iv: str, key: str, encoding='utf-8') -> str:
    """Function that encrypt a text having an string type key

    Args:
        text (str): text to encrypt
        key (str): encryption key

    Returns:
        str: encripted text
    """
    def __pack(text_en: str):

        blockSize = AES.block_size
        return text_en + (blockSize
                          - len(text_en) % blockSize)\
            * chr(blockSize - len(text_en) % blockSize)

    _encrypted = ""
    try:
        if text is None:
            return None
        _key = hashlib.sha256(key.encode()).digest()
        _text = __pack(text)
        _vector = base64.b64decode(iv.encode("ascii"))
        _code = AES.new(_key, AES.MODE_CBC, _vector)
        _encrypted = base64.b64encode(_code.encrypt(_text.encode())
                                     ).decode(encoding)
        logging.info("Value _encrypted")
    except Exception as exc:
        logging.error(str(exc))
    return _encrypted


def decrypt_text(text: Union[bytes, str],
                 iv: str,
                 key: str,
                 decode: str = 'utf-8') -> str:
    """Function that decrypt text having an string type key

    Args:
        text (Union[bytes, str]): encrypted text to decrypt
        key (str): string text to decrypt
        decode (str, optional): decode type to return values. Defaults to 'utf-8'.

    Returns:
        str: decrypted text.
    """
    def __unpack(text_des):
        return text_des[:-ord(text_des[len(text_des)-1:])]

    _decrypted = ""
    try:
        if text is None:
            return None
        _text = text if type(text) == bytes else text.encode(decode)
        _key = hashlib.sha256(key.encode()).digest()
        _encrypted = base64.b64decode(_text)
        _vector = base64.b64decode(iv.encode("ascii"))
        _code = AES.new(_key, AES.MODE_CBC, _vector)

        _decrypted = __unpack(_code.decrypt(_encrypted))\
            .decode(decode)
        logging.info("Value decrypted")
    except Exception as exc:
        logging.error(str(exc))

    return _decrypted
