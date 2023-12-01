from enum import Enum


class ErrorCodes(Enum):
    HEIGHT_GREATER = "the height cannot be greater than permitted"
    HEIGHT_LESS = "the height cannot be less than permitted"
    WIDTH_GREATER = "the width cannot be greater than permitted"
    WIDTH_LESS = "the width cannot be less than permitted"
    WEIGHTLESS = "weight cannot be less than zero"
