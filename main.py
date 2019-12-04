import click

from ErrorHandling.InputValidation import validate_uuid, validate_task, validate_file
from Logic.Tasks import Tasks


@click.command()
@click.option('-u', default="", help='The UUID of the the user e.g. "745409913574d4c6"', type=str)
@click.option('-d', default="",
              help='The UUID of the the document e.g. "140228202800-6ef39a241f35301a9a42cd0ed21e5fb0"', type=str)
@click.option('-t', default="", required=True, help='The task id e.g. "2a"', type=str)
@click.option('-f', default="", required=True, help='The file name e.g. "issuu_cw2"', type=str)
def get_input(u: str, d: str, t: str, f: str):
    """
    Command line interface for app that calls method associated with given task passing relevant parameters

    :param u: The UUID of the the user e.g. "745409913574d4c6
    :param d: The UUID of the the document e.g. "140228202800-6ef39a241f35301a9a42cd0ed21e5fb0
    :param t: The task id e.g. "2a
    :param f: The file name e.g. "issuu_cw2
    :return:
    """

    validate_uuid(u)
    validate_uuid(d)
    validate_task(t)
    validate_file(f)

    invoke_task(u, d, t, f)


def invoke_task(u: str, d: str, t: str, f: str) -> str:
    """
    Case statement that invokes task functionality matched to task parameter

    :param u: The UUID of the the user e.g. "745409913574d4c6
    :param d: The UUID of the the document e.g. "140228202800-6ef39a241f35301a9a42cd0ed21e5fb0
    :param t: The task id e.g. "2a
    :param f: The file name e.g. "issuu_cw2
    :return:
    """
    tasks = Tasks(u, d, t, f)

    switcher = {
        "2a": tasks.run_task_2a,
        "2b": tasks.run_task_2b,
        "3a": tasks.run_task_3a,
        "3b": tasks.run_task_3b,
        "4d": tasks.run_task_4d,
        "5": tasks.run_task_5,
        "6": tasks.run_task_6,
    }

    task_to_execute = switcher.get(t, lambda: "Invalid Task")
    return task_to_execute()


if __name__ == '__main__':
    get_input()
