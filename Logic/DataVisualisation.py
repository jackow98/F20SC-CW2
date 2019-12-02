# TODO: Make generic
import matplotlib.pyplot as plt
import numpy as np
import pydot


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
        graph = pydot.Dot(graph_type='digraph')

        i = 0
        userNodes = []
        docNodes = []

        for user in docs_read_by_visitors_dicts:
            for key, docs in user.items():
                user_node = pydot.Node(key[-4:], shape="rectangle", style="filled")
                if key == visitor_uuid:
                    user_node.set_color("green")

                userNodes.append(user_node)
                graph.add_node(user_node)

                for doc in docs:
                    doc_node = pydot.Node(doc[-4:], shape="circle", style="filled")
                    if doc == doc_uuid:
                        print("equal")
                        doc_node.set_color("green")

                    docNodes.append(doc_node)
                    graph.add_node(doc_node)
                    graph.add_edge(pydot.Edge(doc_node, user_node))

        graph.write_png("myGraph.png")
