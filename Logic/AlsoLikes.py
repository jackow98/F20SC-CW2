from collections import OrderedDict, Counter


class AlsoLikes:

    @staticmethod
    def get_docs_read_by_visitors_dict(visits, doc_uuid: str) -> list:
        """
        Returns a list of objects that details documents read by other users who have also read provided document

        :param visits: The list of visit objects to iterate over
        :param doc_uuid: The doc uuid to that the user has viewed
        :return: A list of objects with each visitor uuid as key and a list of documents they have read as the value
        """
        docs_read_by_visitors_dicts = []

        # Get also likes for provided document ID
        visitors_of_doc = visits.get_visitors(doc_uuid)

        for visitor in visitors_of_doc:
            docs_read_by_visitors_dicts.append(visits.get_documents(visitor))

        return docs_read_by_visitors_dicts

    @staticmethod
    def get_also_likes(visits, doc_uuid: str, visitor_uuid="") -> list:
        """
        Return list of 10 doc ids that user has also viewed

         :param visits: The list of visit objects to iterate over
        :param doc_uuid: The doc uuid to that the user has viewed
        :param visitor_uuid: The visitor uuid of the user that has initially viewed the document

        :return: A list of top 10 documents read by similar visitors sorted by number of visitors per doc
        """

        docs_read_by_visitors_dicts = AlsoLikes.get_docs_read_by_visitors_dict(visits, doc_uuid)

        # Convert list of objects to list of doc_uuid
        docs_read_by_visitors_list = []
        for doc in docs_read_by_visitors_dicts:
            for visitors in doc.values():
                docs_read_by_visitors_list.extend(visitors)

        # Sort list and return first 10 values
        return AlsoLikes.sort_by_number_of_visitors(docs_read_by_visitors_list)[:10]

    @staticmethod
    def sort_by_number_of_visitors(docs_read_by_visitors_list: list) -> list:
        """
        Sorts a list of documents by number of visitors

        :param docs_read_by_visitors_list: A list of document uuid
        :return: A sorted list of document uuid
        """
        res = {}
        # Count occurrences of each visitor 
        for visit in docs_read_by_visitors_list:
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
