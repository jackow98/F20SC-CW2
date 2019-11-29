# TODO: Make generic
import matplotlib.pyplot as plt
import numpy as np


class DataVisualisation:

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