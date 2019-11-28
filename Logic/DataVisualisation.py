# TODO: Make generic
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


class DataVisualisation:

    @staticmethod
    def create_histogram(item_to_count_dict: dict, title: str):
        """
        Using matplot lib, generate and display a histogram
        :param item_to_count_dict:
        :return:
        """
        plt.bar(range(len(item_to_count_dict)), list(item_to_count_dict.values()), align='center')
        plt.xticks(range(len(item_to_count_dict)), list(item_to_count_dict.keys()))
        plt.title(title)
        plt.show()
