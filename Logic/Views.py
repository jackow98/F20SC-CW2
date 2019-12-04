import re

from Logic.DataVisualisation import DataVisualisation
import pycountry_convert as pc
from user_agents import parse


class Views:
    @staticmethod
    def get_visitors_per_browser(visits) -> dict:
        """
        Return a dictionary with number of visitors for each browser
        :return:
        """
        return visits.get_matched_parameter_count("visitor_useragent")


    # TODO: review visitor_useragent documentation to understand what regex to use
    # TODO: possibly overload above function?
    @staticmethod
    def get_visitors_per_browser_simple(visits) -> dict:
        """
        Return a dictionary with number of visitors for each browser removing extra information about version etc.
        :return:
        """

        mydic = {'Other': 0}

        for visit in visits.file:
            ua_string = visit.get("visitor_useragent", "")
            user_agent = parse(ua_string)
            if user_agent.browser.family in mydic:
                mydic[user_agent.browser.family] += 1
            else:
                mydic[user_agent.browser.family] = 1

        finaldic = {}
        for browser in mydic:
            if mydic[browser] <= 30:
                mydic['Other'] += mydic[browser]
            else:
                finaldic[browser] = mydic[browser]

        finaldic['Other'] = mydic['Other']

        return finaldic


    # TODO: use https://pypi.org/project/pycountry/ and https://pypi.org/project/pycountry-convert/
    @staticmethod
    def get_visitors_per_continent(visitors_by_country: dict) -> dict:
        """
        Generate a new dictionary that groups visitors by continent
        :param visitors_by_country:
        :return:
        """
        # TODO: Make generic
        res = {}
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
    def get_visitors_per_country(visits,  doc_uuid: str) -> dict:
        """
        Given a document, return a dictionary with number of visitors for each country
        :param list_of_visits:
        :param doc_uuid:
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
