import re

def convertToValidJson(files):
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

def getVisitors(docUUID):


def main():
    # Files to convert
    files = ["issuu_cw2", "issuu_sample"]
    convertToValidJson(files)

