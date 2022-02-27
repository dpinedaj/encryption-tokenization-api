from fastapi import HTTPException

import logging

class EncryptorException(HTTPException):
    def __init__(self, message):
        logging.error(f"Error: {self.__class__.__name__}, detail: {message}")
        super(EncryptorException, self).__init__(status_code=400, detail= message)