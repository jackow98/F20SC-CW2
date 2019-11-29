def remove_duplicates(list_of_strings: list) -> list:
    """

    :param list_of_strings:
    :return:
    """
    return list(dict.fromkeys(list_of_strings))