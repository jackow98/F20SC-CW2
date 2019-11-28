class Views:
    def get_visitors_per_browser(self) -> dict:
        """
        Return a dictionary with number of visitors for each browser
        :return:
        """

    # TODO: review visitor_useragent documentation to understand what regex to use
    # TODO: possibly overload above function?
    def get_visitors_per_browser_simple(self) -> dict:
        """
        Return a dictionary with number of visitors for each browser removing extra information about version etc.
        :return:
        """

    # TODO: use https://pypi.org/project/pycountry/ and https://pypi.org/project/pycountry-convert/
    def get_visitors_per_continent(self, visitors_by_country: dict) -> dict:
        """
        Generate a new dictionary that groups visitors by continent
        :param visitors_by_country:
        :return:
        """

    def get_visitors_per_country(self, doc_uuid: str) -> dict:
        """
         Given a document, return a dictionary with number of visitors for each country
        :param doc_uuid:
        :return:
        """