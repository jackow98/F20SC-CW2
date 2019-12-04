from FileManagement import FileManagement
from Logic.AlsoLikes import AlsoLikes
from Logic.DataVisualisation import DataVisualisation
from Logic.Views import Views


class Tasks:
    def __init__(self, visitor_uuid="", doc_uuid="", task_id="", file_name=""):
        """
        Constructor that is called when task is run

        :param visitor_uuid: The visitor UUID provided by user
        :param doc_uuid: The document UUID provided by user
        :param task_id: The task ID provided by user
        :param file_name: The file name provided by user
        """
        self.visits = FileManagement(file_name)
        self.visitor_uuid = visitor_uuid
        self.doc_uuid = doc_uuid
        self.task_id = task_id
        self.file_name = file_name

    # TODO: Handle exceptions

    def run_task_2a(self):
        """
        Take a doc_uuid and display a histogram of countries of the viewers
        """
        visitors_by_country = Views.get_visitors_per_country(self.visits, self.doc_uuid)
        DataVisualisation.create_histogram(visitors_by_country, "Visitors per Country", "Countries", "Visitors")

    def run_task_2b(self):
        """
        Take a doc_uuid and display a histogram of the continents of the viewers
        """
        visitors_by_country = Views.get_visitors_per_country(self.visits, self.doc_uuid)
        visitors_by_continent = Views.get_visitors_per_continent(visitors_by_country)
        DataVisualisation.create_histogram(visitors_by_continent, "Visitors per Continent", "Continents", "Visitors")

    def run_task_3a(self):
        """
        Display a histogram of all browser identifiers of the viewers.
        """
        visitors_per_browser = Views.get_visitors_per_browser(self.visits)
        DataVisualisation.create_histogram(visitors_per_browser, "Visitors per Browser", "Browsers", "Visitors")

    def run_task_3b(self):
        """
        Display a histogram of all main browser names of the viewers.
        """
        visitors_per_browser_simple = Views.get_visitors_per_browser_simple(self.visits)
        DataVisualisation.create_histogram(
            visitors_per_browser_simple, "Visitors per Browser Simple", "Browsers", "Visitors"
        )

    def run_task_4d(self) -> str:
        """
        Returns a sorted “also like” list of documents

        :return: A string detailing the top 10 document ID's
        """
        top_documents = AlsoLikes.get_also_likes(self.visits, self.doc_uuid, self.visitor_uuid)

        return_string = f"Top {len(top_documents)} documents are: {top_documents}"
        print(return_string)
        return return_string

    def run_task_5(self):
        """
        Saves an also likes graph between the input document and all documents also read by visitor
        :return:
        """
        docs_read_by_visitors_dicts = AlsoLikes.get_docs_read_by_visitors_dict(self.visits, self.doc_uuid)
        file_name = DataVisualisation.create_also_likes_graph(
            docs_read_by_visitors_dicts, self.doc_uuid, self.visitor_uuid
        )

        return_string = f"Graph created and saved as a PDF and saved at: {file_name}"
        print(return_string)
        return

    def run_task_6(self):
        """
        Saves and displays an also likes graph between the input document and all documents also read by visitor
        :return:
        """
        docs_read_by_visitors_dicts = AlsoLikes.get_docs_read_by_visitors_dict(self.visits, self.doc_uuid)
        file_name = DataVisualisation.create_also_likes_graph(
            docs_read_by_visitors_dicts, self.doc_uuid, self.visitor_uuid
        )
        DataVisualisation.open_file(file_name)
