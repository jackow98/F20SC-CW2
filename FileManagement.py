# TODO: decide where to use classes
import re


class FileManagement:

    # TODO: Make static variable that holds list of visits

    def load_file(self, file_name: str) -> list:
        """
        Load in list of visits and store in class
        :param file_name:
        :return:
        """

    # TODO: Implement iterator over visits
    def get_visitors(self, doc_uuid: str) -> list:
        """
        Given a document, return a list of all visitor UUID's for said document
        :param doc_uuid:
        :return:
        """

    def get_documents(self, user_uuid: str) -> list:
        """
        Given a user, return a list of all document UUID's for said user
        :param doc_uuid:
        :return:
        """

    @staticmethod
    def convert_to_valid_json(files: list):
        """
        Converts the .json files provided in coursework doc to correctly formatted JSON

        :return:
        """
        for file in files:
            with open(file + ".json") as raw_file:
                raw_file_contents = raw_file.read()

            # Convert objects to list of objects
            raw_file_contents_new = re.sub('}', '},', raw_file_contents)
            raw_file_contents_new = "[" + raw_file_contents_new[:-2] + "]"

            with open(file + "_new.json", "w+") as raw_file_new:
                raw_file_new.write(raw_file_contents_new)


def main():
    # Files to convert
    files = ["issuu_cw2", "issuu_sample"]
    FileManagement.convert_to_valid_json(files)