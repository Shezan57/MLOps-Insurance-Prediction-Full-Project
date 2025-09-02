import os
import sys

import numpy as np
import dill
import yaml
from pandas import DataFrame
from src.exception import MyException
from src.logger import logging

def read_yaml_file(file_path: str) -> dict:
    """
    Reads a YAML file and returns its contents as a dictionary.

    :param file_path: Path to the YAML file.
    :return: Dictionary containing the YAML file contents.
    """
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except Exception as e:
        raise MyException(e, sys) from e

def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    """
    Writes a dictionary to a YAML file.

    :param file_path: Path to the YAML file.
    :param content: Dictionary to write to the YAML file.
    :param replace: If True, replace the file if it exists.
    """
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as file:
            yaml.dump(content, file)
    except Exception as e:
        raise MyException(e, sys) from e 


def load_object(file_path: str) -> object:
    """
    Loads a Python object from a file using dill.

    :param file_path: Path to the file containing the object.
    :return: The loaded Python object.
    """
    try:
        with open(file_path, 'rb') as file:
            return dill.load(file)
    except Exception as e:
        raise MyException(e, sys) from e


def save_numpy_array_data(file_path: str, data: np.ndarray) -> None:
    """
    Saves a NumPy array to a file.

    :param file_path: Path to the file where the array will be saved.
    :param data: NumPy array to save.
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file:
            np.save(file, data)
    except Exception as e:
        raise MyException(e, sys) from e
    

def load_numpy_array_data(file_path: str) -> np.ndarray:
    """
    Loads a NumPy array from a file.

    :param file_path: Path to the file containing the array.
    :return: The loaded NumPy array.
    """
    try:
        with open(file_path, 'rb') as file:
            return np.load(file)
    except Exception as e:
        raise MyException(e, sys) from e
    

def save_object(file_path: str, obj: object) -> None:
    logging.info("Entered the save_object method of Main Utils")
    """
    Saves a Python object to a file using dill.

    :param file_path: Path to the file where the object will be saved.
    :param obj: The Python object to save.
    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as file:
            dill.dump(obj, file)
        logging.info("Successfully saved the object.")
    except Exception as e:
        logging.error(f"Error occurred while saving the object: {e}")
        raise MyException(e, sys) from e
    

# def drop_columns(df: DataFrame, cols: list)-> DataFrame:

#     """
#     drop the columns form a pandas DataFrame
#     df: pandas DataFrame
#     cols: list of columns to be dropped
#     """
#     logging.info("Entered drop_columns methon of utils")

#     try:
#         df = df.drop(columns=cols, axis=1)

#         logging.info("Exited the drop_columns method of utils")
        
#         return df
#     except Exception as e:
#         raise MyException(e, sys) from e