import click
from FileManagement import FileManagement
from Logic.Tasks import Tasks


@click.command()
@click.option('-u', default="", help='The UUID of the the user e.g. "745409913574d4c6"')
@click.option('-d', default="",
              help='The UUID of the the document e.g. "140228202800-6ef39a241f35301a9a42cd0ed21e5fb0"')
@click.option('-t', default="", required=True, help='The task id e.g. "2a"')
@click.option('-f', default="", required=True, help='The file name e.g. "issuu_cw2"')
def get_input(u: str, d: str, t: str, f: str):
    """
    Command line interface for application that calls method associated with given task passing relevant parameters

    :param u: The UUID of the the user e.g. "745409913574d4c6
    :param d: The UUID of the the document e.g. "140228202800-6ef39a241f35301a9a42cd0ed21e5fb0
    :param t: The task id e.g. "2a
    :param f: The file name e.g. "issuu_cw2
    :return:
    """
    invoke_task(u, d, t, f)


def invoke_task(u: str, d: str, t: str, f: str):
    """
    Case statement that invokes task functionality matched to task parameter
    :param t:
    :return:
    """
    tasks = Tasks(u, d, t, f)

    # TODO: Invoke tasks
    switcher = {
        "2a": tasks.run_task_2a(),
        "2b": "2b",
        "3a": "3a",
        "3b": "3b",
        "4d": "4d",
        "5": "5",
        "6": "6"
    }

    return switcher.get(t, "Invalid Task")


if __name__ == '__main__':
    get_input()
