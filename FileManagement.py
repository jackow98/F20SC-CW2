# TODO: decide where to use classes
import json
import os
import re

from Logic.HelperFunctions import remove_duplicates


class FileManagement:

    def __init__(self, file_name):
        """
        Constructor stores file name and loads file
        :param file_name: The name of the JSON file containing a list of visits e.g. "issuu_cw2"
        """
        self.file_name = file_name
        self.file = self.load_file()

    def load_file(self, file_name="") -> json:
        """
        Load in list of visits converting to JSON if there is a Json decoder exception

        :param file_name: The name of the JSON file e.g. "issuu_cw2"
        :return: The JSON object corresponding to the loaded file
        """
        if file_name == "":
            file_name = self.file_name

        with open(os.path.join("Data", file_name + ".json")) as raw_file:
            try:
                return json.load(raw_file)

            # If exception, convert to JSON and load with new file name
            except json.decoder.JSONDecodeError:
                self.convert_to_valid_json()
                return self.load_file()

    def get_matched_visits_list(self, uuid_to_match: str, field_to_match: str, field_to_return: str) -> list:
        """
        Generic method that given a value and field, returns a list of all matched values corresponding to match

        :param uuid_to_match: A UUID to match against provided field_to_match parameter
        :param field_to_match: The field to match the provided uuid_to_match parameter against
        :param field_to_return:
        :return:
        """
        res = []
        for visit in self.file:
            try:
                if uuid_to_match == visit[field_to_match]:
                    res.append(visit[field_to_return])
            except KeyError:
                # TODO: Handle error cases correctly
                pass

        return res

    def get_visitors(self, doc_uuid: str) -> list:
        """
        Given a document, return a list of all visitor UUID's for provides document

        :param doc_uuid: The UUID of the document to match
        :return: A list of all visitor UUID's for provides document
        """
        res = self.get_matched_visits_list(doc_uuid, "subject_doc_id", "visitor_uuid")
        return remove_duplicates(res)

    def get_documents(self, visitor_uuid: str) -> dict:
        """
        Given a user, return a dictionary of all document UUID's for said user removing duplicates

        :param visitor_uuid: The UUID of the visitor to match
        :return: A dictionary with key visitor_uuid and list of viewed documents as the value
        """
        res = self.get_matched_visits_list(visitor_uuid, "visitor_uuid", "subject_doc_id")
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
