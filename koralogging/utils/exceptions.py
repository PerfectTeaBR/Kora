from http import HTTPStatus
import requests


class APIError(Exception):
    
    def __init__(self, message: str, request) -> None:
        super().__init__(message)
        self.message = "Deu um erro aqui viu!"
        self.request = request
