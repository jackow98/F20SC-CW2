def remove_duplicates(list_of_strings: list) -> list:
    """

    :param list_of_strings:
    :return:
    """
    return list(dict.fromkeys(list_of_strings))

# TODO: Ask Paul what he thinks, what does Hans mean by hex digits
def get_last_four_hex_digits(string):
    return string[-4:]