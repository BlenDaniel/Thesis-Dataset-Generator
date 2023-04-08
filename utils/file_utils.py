import csv
import json
import os
import tkinter as tk
from tkinter import filedialog

def choose_file():
    """Opens a file dialog and returns the selected file path."""
    root = tk.Tk()
    root.withdraw()
    current_dir = os.getcwd()
    file_path = filedialog.askopenfilename()
    return file_path

def read_csv_file(filename):
    """Reads a CSV file and returns the data as a list of lists."""
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        data = [row for row in csvreader]
    return data


def write_csv_file(data, filename):
    """Writes data to a CSV file."""
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for row in data:
            csvwriter.writerow(row)

def read_json_file(filename):
    """Reads a JSON file and returns the data as a Python object."""
    with open(filename, 'r') as jsonfile:
        data = json.load(jsonfile)
    return data

def write_json_file(data, filename):
    """Writes data to a JSON file."""
    with open(filename, 'w') as jsonfile:
        json.dump(data, jsonfile)

def save_path():
    """returns the appropriate directory"""
    return "data/useable/"

def get_generated(filename):
    """returns the appropriate directory"""
    return "data/useable/"+filename



