from Logic.DataVisualisation import DataVisualisation
from FileManagement import FileManagement
from Logic.Views import Views
from Logic.AlsoLikes import AlsoLikes
import pprint

class Tasks:
    def __init__(self, visitor_uuid="", doc_uuid="", task_id="", file_name=""):
        """

        :param visitor_uuid:
        :param doc_uuid:
        :param task_id:
        :param file_name:
        """
        self.visits = FileManagement(file_name)
        self.visitor_uuid = visitor_uuid
        self.doc_uuid = doc_uuid
        self.task_id = task_id
        self.file_name = file_name

    # TODO: Pass correct parameters, implement functionality and handle excpetions
    def run_task_2a(self):
        """

        :return:
        """
        visitors_by_country = Views.get_visitors_per_country(self.visits, self.doc_uuid)
        DataVisualisation.create_histogram(visitors_by_country, "Visitors per Country", "Countries", "Visitors")

    # TODO: Pass correct parameters, implement functionality and handle excpetions
    def run_task_2b(self):
        """

        :return:
        """
        visitors_by_country = Views.get_visitors_per_country(self.visits, self.doc_uuid)
        visitors_by_continent = Views.get_visitors_per_continent(visitors_by_country)
        DataVisualisation.create_histogram(visitors_by_continent, "Visitors per Continent", "Continents", "Visitors")

    # TODO: Pass correct parameters, implement functionality and handle excpetions
    def run_task_3a(self):
        """

        :return:
        """
        visitors_per_browser = Views.get_visitors_per_browser(self.visits)
        DataVisualisation.create_histogram(visitors_per_browser, "Visitors per Browser", "Browsers", "Visitors")

    # TODO: Pass correct parameters, implement functionality and handle excpetions
    def run_task_3b(self):
        """

        :return:
        """
        # TODO: Finish implementing
        visitors_per_browser_simple = Views.get_visitors_per_browser_simple(self.visits)
        DataVisualisation.create_histogram(
            visitors_per_browser_simple, "Visitors per Browser Simple", "Browsers", "Visitors")

    # TODO: Pass correct parameters, implement functionality and handle excpetions
    def run_task_4d(self) -> str:
        """

        :return:
        """
        top_documents = AlsoLikes.get_also_likes(self.visits, self.doc_uuid, self.visitor_uuid)
        print(f"Top {len(top_documents)} documents are: {top_documents}")
        return f"Top {len(top_documents)} documents are: {str(top_documents)}"

    # TODO: Pass correct parameters, implement functionality and handle excpetions
    def run_task_5(self):
        """

        :return:
        """
        docs_read_by_visitors_dicts = AlsoLikes.get_docs_read_by_visitors_dict(self.visits, self.doc_uuid)
        DataVisualisation.create_also_likes_graph(docs_read_by_visitors_dicts, self.doc_uuid, self.visitor_uuid)

    # TODO: Pass correct parameters, implement functionality and handle excpetions
    def run_task_6(self):
        """

        :return:
        """
