class InvokeException(Exception):
    error_code = 0
    message = ""

    def __init__(self, error_code=None, message=None):
        if error_code:
            self.error_code = error_code
        if message:
            self.message = message

    def to_dict(self):
        return {
            'error_code': self.error_code,
            'message': self.message
        }


class PrefixError(InvokeException):
    error_code = 1
    message = "prefix error!"


class FormatError(InvokeException):
    error_code = 2
    message = "host or port can not be none!"


class RequestError(InvokeException):
    error_code = 3
    message = "request failure!"




