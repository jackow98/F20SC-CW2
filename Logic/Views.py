class Views:
    @staticmethod
    def get_visitors_per_browser() -> dict:
        """
        Return a dictionary with number of visitors for each browser
        :return:
        """

    # TODO: review visitor_useragent documentation to understand what regex to use
    # TODO: possibly overload above function?
    @staticmethod
    def get_visitors_per_browser_simple() -> dict:
        """
        Return a dictionary with number of visitors for each browser removing extra information about version etc.
        :return:
        """

    # TODO: use https://pypi.org/project/pycountry/ and https://pypi.org/project/pycountry-convert/
    @staticmethod
    def get_visitors_per_continent(visitors_by_country: dict) -> dict:
        """
        Generate a new dictionary that groups visitors by continent
        :param visitors_by_country:
        :return:
        """

    @staticmethod
    def get_visitors_per_country(list_of_visits: list, doc_uuid: str) -> dict:
        """
        Given a document, return a dictionary with number of visitors for each country
        :param list_of_visits:
        :param doc_uuid:
        :return:
        """