class CustomException(Exception):
    def __init__(self, *args, **kwargs):
        super(CustomException, self).__init__(*args, **kwargs)


class ConnectionError(CustomException):
    pass
