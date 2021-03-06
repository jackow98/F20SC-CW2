from ErrorHandling import CustomExceptions
from ErrorHandling.InputValidation import validate_input, check_uuid
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
        self.visitors_by_country = {}

    # TODO: Handle exceptions

    def get_visitors_by_country_and_check(self):
        """
        A method to check for a valid user uuid input and non empty visitor dictionary

        :return: String with error message if error or empty string upon success
        """
        if self.doc_uuid == "":
            return "Please enter a valid UUID "

        input_valid = validate_input(self.doc_uuid, lambda d: check_uuid(d), CustomExceptions.UUIDError)

        if input_valid != "":
            return input_valid
        else:
            self.visitors_by_country = Views.get_visitors_per_country(self.visits, self.doc_uuid)

            if self.visitors_by_country == {}:
                return f"No documents with doc uuid of '{self.doc_uuid}' were found"

        return ""

    def run_task_2a(self) -> str:
        """
        Take a doc_uuid and display a histogram of countries of the viewers
        """
        check = self.get_visitors_by_country_and_check()
        if check != "":
            return check

        DataVisualisation.create_histogram(self.visitors_by_country, "Visitors per Country", "Countries", "Visitors")

    def run_task_2b(self):
        """
        Take a doc_uuid and display a histogram of the continents of the viewers
        """
        check = self.get_visitors_by_country_and_check()
        if check != "":
            return check

        visitors_by_continent = Views.get_visitors_per_continent(self.visitors_by_country)

        if visitors_by_continent == {}:
            return f"No documents with doc uuid of '{self.doc_uuid}' were found"

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
        if self.doc_uuid == "":
            return "Please enter a valid UUID "

        doc_uuid_valid = validate_input(self.doc_uuid, lambda d: check_uuid(d), CustomExceptions.UUIDError)

        if doc_uuid_valid != "":
            return doc_uuid_valid

        top_documents = AlsoLikes.get_also_likes(self.visits, self.doc_uuid, self.visitor_uuid)

        if not top_documents:
            return f"There are no also liked documents for the doc UUID '{self.doc_uuid}'"

        return f"Top {len(top_documents)} documents are: {top_documents}"

    def run_task_5(self):
        """
        Saves an also likes graph between the input document and all documents also read by visitor
        :return:
        """
        doc_uuid_valid = validate_input(self.doc_uuid, lambda d: check_uuid(d), CustomExceptions.UUIDError)

        if doc_uuid_valid != "":
            return doc_uuid_valid

        docs_read_by_visitors_dicts = AlsoLikes.get_docs_read_by_visitors_dict(self.visits, self.doc_uuid)

        if not docs_read_by_visitors_dicts:
            return f"There are no also liked documents for the doc UUID '{self.doc_uuid}'"

        file_name = DataVisualisation.create_also_likes_graph(
            docs_read_by_visitors_dicts, self.doc_uuid, self.visitor_uuid
        )

        return f"Graph created and saved as a PDF at: {file_name}"

    def run_task_6(self):
        """
        Saves and displays an also likes graph between the input document and all documents also read by visitor
        :return:
        """
        docs_read_by_visitors_dicts = AlsoLikes.get_docs_read_by_visitors_dict(self.visits, self.doc_uuid)

        if not docs_read_by_visitors_dicts:
            return f"There are no also liked documents for the doc UUID '{self.doc_uuid}'"

        file_name = DataVisualisation.create_also_likes_graph(
            docs_read_by_visitors_dicts, self.doc_uuid, self.visitor_uuid
        )
        DataVisualisation.open_file(file_name)
