# TODO: decide where to use classes
import re
import json
import os


class FileManagement:

    # TODO: Make static variable that holds list of visits

    def __init__(self, file_name):
        """
        Constructor stores file name and loads file
        :param file_name:
        """
        self.file_name = file_name
        self.file = self.load_file()

    def load_file(self) -> json:
        """
        Load in list of visits converting to JSON if there is a Json decoder exception
        :return:
        """
        # TODO: Exception handler, checks if valid Json, if not convert then try again else throw exception
        with open(os.path.join("Data", self.file_name + ".json")) as raw_file:
            try:
                return json.load(raw_file)
            # If exception, convert to JSON and load with new file name
            except json.decoder.JSONDecodeError:
                self.convert_to_valid_json()
                return self.load_file()
    # TODO: Handle all exceptions

    def get_visitors(self, doc_uuid: str) -> list:
        """
        Given a document, return a list of all visitor UUID's for said document
        :param doc_uuid:
        :return:
        """
        # TODO: Implement iterator over visits

    def get_documents(self, user_uuid: str) -> list:
        """
        Given a user, return a list of all document UUID's for said user
        :param user_uuid:
        :return:
        """

    # TODO: Explicitly define param and return types
    def convert_to_valid_json(self):
        """
        Converts the .json files provided in coursework doc to correctly formatted JSON and writes to file
        :return:
        """
        with open(os.path.join("Data", self.file_name + ".json")) as raw_file:
            raw_file_contents = raw_file.read()

        # Convert objects to list of objects
        raw_file_contents_new = re.sub('}', '},', raw_file_contents)
        raw_file_contents_new = "[" + raw_file_contents_new[:-2] + "]"

        # Create new file _new appended to file name and updates instances file_name param
        new_file_name = self.file_name + "_new"

        with open(os.path.join("Data", new_file_name + ".json"), "w+") as raw_file_new:
            raw_file_new.write(raw_file_contents_new)
            self.file_name = new_file_name

