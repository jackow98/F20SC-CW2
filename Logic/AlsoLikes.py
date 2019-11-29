from Logic.ListFunctions import remove_duplicates
from collections import OrderedDict, Counter

# Todo: user overloading or set params to include optional sort_function
# TODO: is it better to return object that includes doc_uuid


class AlsoLikes:

    @staticmethod
    def get_also_likes(visits: list, doc_uuid: str, visitor_uuid="") -> list:
        # TODO: Review application structure, course specification doesn't want list of visits as parameter
        """
        Return list of 10 doc ids that user has also viewed
        :param visits:
        :param doc_uuid:
        :param visitor_uuid:
        :return:
        """
        docs_read_by_visitors_dicts = []

        # Get also likes for provided document ID if no visitor ID is provided
        if visitor_uuid == "":
            visitors_of_doc = visits.get_visitors(doc_uuid)

            for visitor in visitors_of_doc:
                docs_read_by_visitors_dicts.append(visits.get_documents(visitor))

        # Get also likes for provided visitor ID if provided
        else:
            docs_read_by_visitors_dicts.append(visits.get_documents(visitor_uuid))

        # Convert dictionary to list
        # TODO: Consider removing step above if not useful to have a dictionary
        docs_read_by_visitors_list = []
        for doc in docs_read_by_visitors_dicts:
            for visitors in doc.values():
                docs_read_by_visitors_list.extend(visitors)

        # Sort list and return first 10 values
        return AlsoLikes.sort_by_number_of_visitors(docs_read_by_visitors_list)[:10]

    @staticmethod
    def sort_by_number_of_visitors(visitors: list) -> list:
        res = {}
        # Count occurrences of each visitor 
        for visit in visitors:
            try:
                if visit in res:
                    res[visit] = res[visit] + 1
                else:
                    res[visit] = 1
            except KeyError:
                # print("Missing value in doc")
                # TODO: Handle error cases correctly
                pass

        # Sort by number of occurrences
        sorted_list_of_visitors = sorted(res.items(), key=Counter(res.items()).get, reverse=True)
        sorted_list_of_visitors = OrderedDict(sorted_list_of_visitors)

        return list(sorted_list_of_visitors.keys())

    @staticmethod
    def generate_also_likes_graph(doc_uuid: str, also_viewed_docs: list):
        """
        Generate a graph to display relationship between input and also like documents
        
        :param doc_uuid: 
        :param also_viewed_docs: 
        :return: 
        """