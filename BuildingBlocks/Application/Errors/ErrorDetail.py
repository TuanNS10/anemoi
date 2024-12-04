class ErrorDetail(Exception):
    def __init__(self, message, code):
        self.message = message if isinstance(message, list) else [message]
        self.code = code
        