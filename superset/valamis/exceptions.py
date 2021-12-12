class ValamisError(Exception):
    """
    Base class for all exceptions
    """
    pass


class UserCreationError(ValamisError):
    pass


class InvalidFilenameError(ValamisError):
    pass


class ValidationError(ValamisError):
    pass


class JWTIsEmpty(ValamisError):
    pass
