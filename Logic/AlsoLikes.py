# Todo: user overloading or set params to include optional sort_function
# TODO: is it better to return object that includes doc_uuid


class AlsoLikes:

    def get_also_likes(self, doc_uuid: str) -> list:
        """
        Return list of 10 doc ids that user has also viewed
        :param doc_uuid:
        :return:
        """

    def generate_also_likes_graph(self, doc_uuid: str, also_viewed_docs: list):
        """
        Generate a graph to display relationship between input and also like documents
        
        :param doc_uuid: 
        :param also_viewed_docs: 
        :return: 
        """