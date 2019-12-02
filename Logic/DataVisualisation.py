# TODO: Make generic
import matplotlib.pyplot as plt
import pydot
import matplotlib.image as mpimg
from Logic.HelperFunctions import get_last_four_hex_digits


class DataVisualisation:

    # TODO: Clear graphs
    @staticmethod
    def create_histogram(item_to_count_dict: dict, title: str, x_label="", y_label=""):
        """
        Using matplot lib, generate and display a histogram
        :param item_to_count_dict:
        :param title:
        :param x_label:
        :param y_label:
        :return:
        """
        plt.bar(range(len(item_to_count_dict)), list(item_to_count_dict.values()), align='center')
        # TODO: Make display of labels pretty
        plt.xticks(
            range(len(item_to_count_dict)),
            list(item_to_count_dict.keys()),
            horizontalalignment='center',
            verticalalignment='center',
            wrap=True
        )
        plt.xlabel(x_label, fontsize=14)
        plt.ylabel(y_label, fontsize=14)
        plt.title(title)
        plt.show()

    @staticmethod
    def create_graph(docs_read_by_visitors_dicts: dict, doc_uuid, visitor_uuid):
        """

        :param docs_read_by_visitors_dicts:
        :param doc_uuid:
        :param visitor_uuid:
        :return:
        """
        graph = pydot.Dot(graph_type='digraph')

        userNodes = []
        docNodes = []

        for user in docs_read_by_visitors_dicts:
            for key, docs in user.items():
                user_node = pydot.Node(get_last_four_hex_digits(key), shape="rectangle", style="filled")
                if key == visitor_uuid:
                    user_node.set_color("green")

                userNodes.append(user_node)
                graph.add_node(user_node)

                for doc in docs:
                    doc_node = pydot.Node(get_last_four_hex_digits(doc), shape="circle", style="filled")
                    if doc == doc_uuid:
                        doc_node.set_color("green")

                    docNodes.append(doc_node)
                    graph.add_node(doc_node)
                    graph.add_edge(pydot.Edge(user_node, doc_node))

        # TODO: Display nicer
        file_name = "alsoLikes-" + get_last_four_hex_digits(doc_uuid) + "-" + get_last_four_hex_digits(visitor_uuid) + ".png"
        graph.write_png(file_name)
        img = mpimg.imread(file_name)
        plt.imshow(img)
        plt.show()