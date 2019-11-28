import click


@click.command()
@click.option('-u', default=None, help='The UUID of the the user e.g. "745409913574d4c6"')
@click.option('-d', default=None,
              help='The UUID of the the document e.g. "140228202800-6ef39a241f35301a9a42cd0ed21e5fb0"')
@click.option('-t', default=None, required=True, help='The task id e.g. "2a"')
@click.option('-f', default=None, required=True, help='The file name e.g. "issuu_cw2.json"')
def getInput(u, d, t, f):
    """
    Command line interface for application that calls method associated with given task passing relevant parameters

    :param u:
    :param d:
    :param t:
    :param f:
    :return:
    """
    print(u, d, t, f)


if __name__ == '__main__':
    getInput()
