from Logic.DataVisualisation import DataVisualisation
import pycountry_convert as pc


class Views:
    @staticmethod
    def get_visitors_per_browser(visits: list) -> dict:
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
        # TODO: Make generic
        res = {}
        for key in visitors_by_country.keys():
            country_code = pc.country_name_to_country_alpha2(key, cn_name_format="default")
            continent_code = pc.country_alpha2_to_continent_code(country_code)
            continent_name = pc.convert_continent_code_to_continent_name(continent_code)
            print(continent_name)
            if continent_name in res:
                res[continent_name] = res[continent_name] + 1
            else:
                res[continent_name] = 1

        return res

    @staticmethod
    def get_visitors_per_country(visits: list,  doc_uuid: str) -> dict:
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
