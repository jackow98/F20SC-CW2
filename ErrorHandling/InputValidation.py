import re
import sys

from ErrorHandling import CustomExceptions


# TODO: Group exceptions, make generic
# TODO: Add a safety check for all

def check_file(f: str):
    if f == "":
        raise CustomExceptions.MissingFileError
    else:
        return True


def check_uuid(s: str):
    if re.match(r'\b(uuid:){0,1}\s*([a-f0-9\\-]*){1}\s*', s):
        return True
    else:
        raise CustomExceptions.UUIDError(s)


def check_task(t: str):
    if t == "":
        raise CustomExceptions.IncorrectTaskError("")
    if t in ['2a', '2b', '3a', '3b', '4d', '5', '6']:
        return True
    else:
        raise CustomExceptions.IncorrectTaskError(t)


def validate_input(input_string: str, check_func, exception) -> str:
    try:
        check_func(input_string)
        return ""
    except exception as err:
        return err.message


def validate_uuid(visitor_uuid: str) -> str:
    """

    :param visitor_uuid:
    :return:
    """
    return validate_input(visitor_uuid, lambda u: check_uuid(u), CustomExceptions.UUIDError)


def validate_task(task: str) -> str:
    return validate_input(task, lambda t: check_task(t), CustomExceptions.IncorrectTaskError)


def validate_file(file: str) -> str:
    return validate_input(file, lambda f: check_file(f), CustomExceptions.MissingFileError)
