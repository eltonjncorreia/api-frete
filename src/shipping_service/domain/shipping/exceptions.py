class ExceptionBase(Exception):
    def __init__(self, message: str) -> None:
        self.message = message


class HeightCannotBeGreaterThanPermitted(ExceptionBase):
    """ Height cannot be Greater than permitted"""


class HeightCannotBeLessThanPermitted(ExceptionBase):
    """ Height cannot be less than permitted"""


class WidthCannotBeGreaterThanPermitted(ExceptionBase):
    """ Height cannot be greater than permitted"""


class WidthCannotBeLessThanPermitted(ExceptionBase):
    """ Height cannot be less than permitted"""


class WeightCannotLessThanZero(ExceptionBase):
    """ Height cannot be less than permitted"""
