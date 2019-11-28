from Logic.DataVisualisation import DataVisualisation
from FileManagement import FileManagement
from Logic.Views import Views


class Tasks:
    def __init__(self, user_uuid="", doc_uuid="", task_id="", file_name=""):
        """
        :param list_of_visits:
        """
        f = FileManagement(file_name)
        self.visits = FileManagement(f.file_name)
        print(str(self.visits.file))
        self.user_uuid = user_uuid
        self.doc_uuid = doc_uuid
        self.task_id = task_id
        self.file_name = file_name

    # TODO: Pass correct parameters, implement functionality and handle excpetions
    def run_task_2a(self):
        """

        :return:
        """

    # TODO: Pass correct parameters, implement functionality and handle excpetions
    def run_task_2b(self):
        """

        :return:
        """

    # TODO: Pass correct parameters, implement functionality and handle excpetions
    def run_task_3a(self):
        """

        :return:
        """
        # print(type(self.visits.file))
        # Views.get_visitors_per_browser(self.visits)


    # TODO: Pass correct parameters, implement functionality and handle excpetions
    def run_task_3b(self):
        """

        :return:
        """

    # TODO: Pass correct parameters, implement functionality and handle excpetions
    def run_task_4d(self):
        """

        :return:
        """

    # TODO: Pass correct parameters, implement functionality and handle excpetions
    def run_task_5(self):
        """

        :return:
        """

    # TODO: Pass correct parameters, implement functionality and handle excpetions
    def run_task_6(self):
        """

        :return:
        """
