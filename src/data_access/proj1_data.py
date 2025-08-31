import sys
import pandas as pd
import numpy as np
from typing import Optional

from src.configuration.mongo_db_connection import MongoDBClient
from src.constants import DATABASE_NAME
from src.exception import MyException

class Proj1Data:
    """A Class to export MongoDB records as a pandas DataFrame.
    """
    
    def __init__(self) -> None:
        """Initialize the MongoDB client connection
        """
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise MyException(e, sys)
    
    def export_collection_as_dataframe(self, collection_name: str, database_name: Optional[str] = None) -> pd.DataFrame:
        """Export a MongoDB collection as a pandas DataFrame.

        Parameters:
        ----------
        collection_name : str
            The name of the MongoDB collection to export.
        database_name : Optional[str], optional
            The name of the database to use. If None, uses the default database from the MongoDB client.

        Returns:
        -------
        pd.DataFrame
            A pandas DataFrame containing the data from the specified MongoDB collection.

        Raises:
        ------
        MyException
            If there is an issue fetching data from MongoDB or converting it to a DataFrame.
        """
        try:
            # Access specified collection from the default or specified database
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client.client[database_name][collection_name]
            
            # converti collection data to DaraFrame and process 
            print("Fetching data from MongoDB")
            df = pd.DataFrame(list(collection.find()))
            print(f"Rows and columns in df: {df.shape}")
            if "id" in df.columns.to_list():
                df = df.drop(columns=["id"], axis=1)
            df.replace({"na": np.nan}, inplace=True)
            
            return df

        except Exception as e:
            raise MyException(e, sys)