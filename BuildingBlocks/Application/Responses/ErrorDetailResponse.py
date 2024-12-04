from typing import List

class ErrorDetailResponse:
    def __init__(self, messages: List[str], code: str):
        self.messages = messages
        self.code = code
        