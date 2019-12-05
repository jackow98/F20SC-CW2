import pycountry_convert as pc
from user_agents import parse


class Views:
    @staticmethod
    def get_visitors_per_browser(visits) -> dict:
        """
        Return a dictionary with number of visitors for each browser

        :visits: The list of visit objects to iterate over
        :return: Dictionary with number of visitors for each browser
        """
        return visits.get_matched_parameter_count("visitor_useragent")

    @staticmethod
    def get_visitors_per_browser_simple(visits) -> dict:
        """
        Return a dictionary with number of visitors for each browser removing extra information about version etc.

        :visits: The list of visit objects to iterate over
        :return: Dictionary with number of visitors for each browser removing extra information about version etc.
        """

        # create dictionary with all the simple browser names and their occurrences
        visits_by_browser_dictionary = {'Other': 0}
        for visit in visits.file:
            ua_string = visit.get("visitor_useragent", "")
            user_agent = parse(ua_string)
            if user_agent.browser.family in visits_by_browser_dictionary:
                visits_by_browser_dictionary[user_agent.browser.family] += 1
            else:
                visits_by_browser_dictionary[user_agent.browser.family] = 1

        # using the dictionary created above, create and return a new dictionary that combines any browsers with less
        # than 30 occurrences into a single 'Other' item. THis helps the histogram to be more readable
        reduced_visits_by_browser_dictionary = {}
        for browser in visits_by_browser_dictionary:
            if visits_by_browser_dictionary[browser] <= 30:
                visits_by_browser_dictionary['Other'] += visits_by_browser_dictionary[browser]
            else:
                reduced_visits_by_browser_dictionary[browser] = visits_by_browser_dictionary[browser]

        reduced_visits_by_browser_dictionary['Other'] = visits_by_browser_dictionary['Other']

        return reduced_visits_by_browser_dictionary

    @staticmethod
    def get_visitors_per_continent(visitors_by_country: dict) -> dict:
        """
        Generate a new dictionary that groups visitors by continent

        :param visitors_by_country: A dictionary with country as keys and list of count as value
        :return:
        """

        res = {}
        # For each country, get country ID from name then convert to continent ID and find corresponding name
        for key in visitors_by_country.keys():
            country_code = pc.country_name_to_country_alpha2(key, cn_name_format="default")
            continent_code = pc.country_alpha2_to_continent_code(country_code)
            continent_name = pc.convert_continent_code_to_continent_name(continent_code)

            if continent_name in res:
                res[continent_name] = res[continent_name] + 1
            else:
                res[continent_name] = 1

        return res

    @staticmethod
    def get_visitors_per_country(visits, doc_uuid: str) -> dict:
        """
        Given a document, return a dictionary with number of visitors for each country
        :param visits: The list of visit objects to iterate over
        :param doc_uuid: The doc UUID to gather country information about
        :return:
        """
        visits_per_country_codes = visits.get_matched_parameter_count("visitor_country", "subject_doc_id", doc_uuid)
        visits_per_country_names = {}

        # Convert Country codes to country names, if error with code conversion, adds code as key
        for country in visits_per_country_codes.keys():
            try:
                country_name = pc.country_alpha2_to_country_name(country)
                visits_per_country_names[country_name] = visits_per_country_codes[country]
            except NameError:
                visits_per_country_names[country] = visits_per_country_codes[country]

        return visits_per_country_names
