import os
import zipfile


# make folder for test-data
def make_folder(folder_name):
    CMAPSS_path = os.path.join(folder_name)
    CMAPSS = os.makedirs(CMAPSS_path)
    return CMAPSS
make_folder("CMAPSS-Data")


# extract test-data to folder
def extract_data(data_path, extract_to="."):
    with zipfile.ZipFile(data_path, "r") as file:
        file.extractall(path=extract_to)
extract_data("/Users/marcelmann/Downloads/CMAPSSData.zip", "/Users/marcelmann/PycharmProjects/CMAPSS/CMAPSS-Data")




