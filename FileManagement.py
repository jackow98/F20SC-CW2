# TODO: decide where to use classes
import re
import json
import os
from Logic.HelperFunctions import remove_duplicates


class FileManagement:

    # TODO: Remove duplicate code in get_visitors, get_documents and get_matched_parameter_count

    def __init__(self, file_name):
        """
        Constructor stores file name and loads file
        :param file_name:
        """
        self.file_name = file_name
        self.file = self.load_file()

    def load_file(self, file_name="") -> json:
        """
        Load in list of visits converting to JSON if there is a Json decoder exception
        :return:
        """
        # TODO: Exception handler, checks if valid Json, if not convert then try again else throw exception
        if file_name == "":
            file_name = self.file_name

        with open(os.path.join("Data", file_name + ".json")) as raw_file:
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
        # TODO: Use an iterator?
        # TODO: User username as well as user uuid
        # TODO: Consider looking at event_type paramater to decide if page has been read?
        res = []
        for visit in self.file:
            try:
                if doc_uuid == visit["subject_doc_id"]:
                    res.append(visit["visitor_uuid"])
            except KeyError:
                # TODO: Handle error cases correctly
                pass

        # Remove duplicates
        return remove_duplicates(res)

    def get_documents(self, visitor_uuid: str) -> dict:
        """
        Given a user, return a list of all document UUID's for said user
        :param visitor_uuid:
        :return:
        """
        # TODO: Use an iterator?
        res = []
        for visit in self.file:
            try:
                if visitor_uuid == visit["visitor_uuid"]:
                    res.append(visit["subject_doc_id"])
            except KeyError:
                # TODO: Handle error cases correctly
                pass

        return {visitor_uuid: remove_duplicates(res)}

    def get_matched_parameter_count(self, param_to_count, param_to_match=None, param_to_match_val=None):
        """
        Generic method to generate a dictionary that counts number of occurrences of given parameter
        :param param_to_count: The parameter that is being counted in the resulting dictionary
        :param param_to_match: The parameter to filter visit objects, if omitted then matches all
        :param param_to_match_val: The value to match against param_to_match
        :return:
        """
        res = {}
        for visit in self.file:
            try:
                # Match the document to the specified parameter e.g. subject_doc_id
                if param_to_match is None or visit[param_to_match] == param_to_match_val:
                    # TODO: Make a delegate validation function that checks country codes etc.
                    # If the dictionary already has key then increment otherwise insert
                    if visit[param_to_count] in res:
                        res[visit[param_to_count]] = res[visit[param_to_count]] + 1
                    else:
                        res[visit[param_to_count]] = 1
            except KeyError:
                # print("Missing value in doc")
                # TODO: Handle error cases correctly
                pass
        return res

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

