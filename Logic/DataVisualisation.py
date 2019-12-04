# TODO: Make generic
import os

import matplotlib.pyplot as plt
import pydot

from Logic.HelperFunctions import get_last_four_hex_digits


class DataVisualisation:

    @staticmethod
    def clear_plot():
        """
        Clears the matplot display
        """
        plt.clf()

    @staticmethod
    def write_graph_to_file(graph, doc_uuid: str, visitor_uuid: str):
        """
        Writes a .dot graph to a PDF file and opens it

        :param graph: The dot graph to be written
        :param doc_uuid: The doc uuid associated with the graph
        :param visitor_uuid: The doc uuid associated with the graph
        """
        file_name = "alsoLikes-" + get_last_four_hex_digits(doc_uuid) + "-" + get_last_four_hex_digits(
            visitor_uuid) + ".pdf"
        directory = "AlsoLikesGraphs"

        if not os.path.exists(directory):
            os.makedirs(directory)

        file_path = os.path.join("AlsoLikesGraphs", file_name)
        graph.write_pdf(file_path)
        os.startfile(file_path)

    @staticmethod
    def create_histogram(item_to_count_dict: dict, title: str, x_label="", y_label=""):
        """
        Using matplotlib, generate and display a histogram

        :param item_to_count_dict: Dictionary of objects with key as x axis value and value as y axis value
        :param title: Title of the histogram
        :param x_label: Label for x-axis
        :param y_label: Label for y-axis
        :return:
        """
        DataVisualisation.clear_plot()
        plt.bar(range(len(item_to_count_dict)), list(item_to_count_dict.values()), align='center')

        plt.xticks(
            range(len(item_to_count_dict)),
            list(item_to_count_dict.keys()),
            rotation=45
        )
        plt.xlabel(x_label, fontsize=11)
        plt.ylabel(y_label, fontsize=11)
        plt.title(title)

        plt.show()

    @staticmethod
    def create_also_likes_graph(docs_read_by_visitors_dicts: dict, doc_uuid, visitor_uuid):
        """
        Using pydot, generate, save and display an also likes graph

        :param docs_read_by_visitors_dicts: A list of objects with user_uuid as key and doc_uuid read as values
        :param doc_uuid: The doc uuid to that the user has viewed
        :param visitor_uuid: The visitor uuid of the user that has initially viewed the document
        :return:
        """
        graph = pydot.Dot(graph_type='digraph')

        user_nodes = []
        doc_nodes = []

        print(docs_read_by_visitors_dicts)
        #  Iterate over all visitors and create a node for each
        for user in docs_read_by_visitors_dicts:
            for key, docs in user.items():
                user_node = pydot.Node(get_last_four_hex_digits(key), shape="rectangle", style="filled")

                # Colour node if visitor id provided by user matches node
                if key == visitor_uuid:
                    user_node.set_color("green")

                user_nodes.append(user_node)
                graph.add_node(user_node)

                #  Iterate over all documents for each visitor and create a node for each
                for doc in docs:
                    doc_node = pydot.Node(get_last_four_hex_digits(doc), shape="circle", style="filled")
                    if doc == doc_uuid:
                        doc_node.set_color("green")

                    doc_nodes.append(doc_node)
                    graph.add_node(doc_node)
                    graph.add_edge(pydot.Edge(user_node, doc_node))

        DataVisualisation.write_graph_to_file(graph, doc_uuid, visitor_uuid)
