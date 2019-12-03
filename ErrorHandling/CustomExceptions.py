class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class VisualisationError(Error):
    pass


class UUIDError(Error):
    def __init__(self, uuid: str):
        self.message = f"The UUID '{uuid}' is incorrectly formatted"


class MissingTaskError(Error):
    def __init__(self):
        self.message = f"Please include a task ID"


class IncorrectTaskError(Error):
    def __init__(self, uuid: str):
        self.message = f"The task '{uuid}' is not a valid task"


class MissingFileError(Error):
    def __init__(self):
        self.message = f"Please include a file name"
