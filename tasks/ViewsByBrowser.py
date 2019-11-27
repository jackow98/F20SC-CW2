class ViewsByBrowser:

    def get_visitors_per_browser(self) -> dict:
        """
        Return a dictionary with number of visitors for each browser
        :param doc_uuid:
        :return:
        """

    # TODO: review visitor_useragent documentation to understand what regex to use
    # TODO: possibly overload above function?
    def get_visitors_per_browser_simple(self) -> dict:
        """
        Return a dictionary with number of visitors for each browser removing extra information about version etc.
        :param doc_uuid:
        :return:
        """