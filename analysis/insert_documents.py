import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Function to open a file dialog and select an Excel file
def select_excel_file():
    Tk().withdraw()  # We don't want a full GUI, so keep the root window from appearing
    file_path = askopenfilename(title="Select the Excel file", filetypes=[("Excel file", "*.xlsx *.xls")])
    return file_path

# Function to create a DataFrame from an Excel file
def create_dataframe_from_excel(file_path):
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"An error occurred: {e}")
        return None