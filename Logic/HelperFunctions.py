def remove_duplicates(list_of_strings: list) -> list:
    """
    Removes any duplicate values from a list

    :param list_of_strings: The list with duplicates
    :return: Amended list with removed duplicates
    """
    return list(dict.fromkeys(list_of_strings))


def get_last_four_hex_digits(string):
    """
    Slices string to get last 4 characters

    :param string: String to slice
    :return: Sliced string
    """
    return string[-4:]
