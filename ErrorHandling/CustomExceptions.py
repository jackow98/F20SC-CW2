class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class VisualisationError(Error):
    pass


class UUIDError(Error):
    def __init__(self, uuid: str):
        if uuid == "":
            self.message = f"Please include a UUID"
        else:
            self.message = f"The UUID '{uuid}' is incorrectly formatted"


class IncorrectTaskError(Error):
    def __init__(self, task_id: str):
        if task_id == "":
            self.message = f"Please include a task ID"
        else:
            self.message = f"The task '{task_id}' is not a valid task"


class MissingFileError(Error):
    def __init__(self):
        self.message = f"Please include a file name"


class MissingDocument(Error):
    def __init__(self):
        self.message = f"No record of provided document"
