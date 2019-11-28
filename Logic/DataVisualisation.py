# TODO: Make generic
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


class DataVisualisation:

    @staticmethod
    def create_histogram(item_to_count_dict: list):
        """
        Using matplot lib, generate and display a histogram
        :param item_to_count_dict:
        :return:
        """
        # objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
        # y_pos = np.arange(len(objects))
        # performance = [10,8,6,4,2,1]
        #
        # plt.barh(y_pos, performance, align='center', alpha=0.5)
        # plt.yticks(y_pos, objects)
        # plt.xlabel('Usage')
        # plt.title('Programming language usage')
        #
        # plt.show()