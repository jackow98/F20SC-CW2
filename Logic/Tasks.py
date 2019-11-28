from Logic.DataVisualisation import DataVisualisation
from FileManagement import FileManagement
from Logic.Views import Views


class Tasks:
    def __init__(self, user_uuid="", doc_uuid="", task_id="", file_name=""):
        """

        :param user_uuid:
        :param doc_uuid:
        :param task_id:
        :param file_name:
        """
        self.visits = FileManagement(file_name)
        self.user_uuid = user_uuid
        self.doc_uuid = doc_uuid
        self.task_id = task_id
        self.file_name = file_name

    # TODO: Pass correct parameters, implement functionality and handle excpetions
    def run_task_2a(self):
        """

        :return:
        """
        visitors_by_country = Views.get_visitors_per_country(self.visits, self.doc_uuid)
        DataVisualisation.create_histogram(visitors_by_country, "Visitors per Country")

    # TODO: Pass correct parameters, implement functionality and handle excpetions
    def run_task_2b(self):
        """

        :return:
        """
        visitors_by_country = Views.get_visitors_per_country(self.visits, self.doc_uuid)
        visitors_by_continent = Views.get_visitors_per_continent(visitors_by_country)
        DataVisualisation.create_histogram(visitors_by_continent, "Visitors per Continent")

    # TODO: Pass correct parameters, implement functionality and handle excpetions
    def run_task_3a(self):
        """

        :return:
        """
        visitors_per_browser = Views.get_visitors_per_browser(self.visits)
        DataVisualisation.create_histogram(visitors_per_browser, "Visitors per Browser")

    # TODO: Pass correct parameters, implement functionality and handle excpetions
    def run_task_3b(self):
        """

        :return:
        """
        visitors_per_browser_simple = Views.get_visitors_per_browser_simple(self.visits)


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
