import re
import sys
from ErrorHandling import CustomExceptions


# TODO: Group exceptions, make generic
# TODO: Add a safety check for all


# Code from https://stackoverflow.com/questions/11384589/what-is-the-correct-regex-for-matching-values-generated-by-uuid-uuid4-hex
def validate_uuid(visitor_uuid: str):
    """

    :param visitor_uuid:
    :return:
    """
    try:
        if re.match(r'\b(uuid:){0,1}\s*([a-f0-9\\-]*){1}\s*', visitor_uuid) or visitor_uuid == "":
            return True
        else:
            raise CustomExceptions.UUIDError(visitor_uuid)

    except CustomExceptions.UUIDError as err:
        print(err.message)
        sys.exit()


def validate_task(task: str):
    try:
        if task == "":
            raise CustomExceptions.MissingTaskError
        if task in ['2a', '2b', '3a', '3b', '4d', '5', '6']:
            return True
        else:
            raise CustomExceptions.IncorrectTaskError(task)

    except CustomExceptions.IncorrectTaskError as err:
        print(err.message)
        sys.exit()

    except CustomExceptions.MissingTaskError as err:
        print(err.message)
        sys.exit()


def validate_file(file: str):
    try:
        if file == "":
            raise CustomExceptions.MissingFileError

    except CustomExceptions.MissingFileError as err:
        print(err.message)
        sys.exit()
