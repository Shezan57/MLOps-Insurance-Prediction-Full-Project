import os
import sys
import certifi
import pymongo
from src.exception import MyException
from src.logger import logging
from src.constants import DATABASE_NAME, COLLECTION_NAME, MONGODB_URL_KEY

# Load the certificate authority file to avoid timeout errors when connention to MongoDB
ca = certifi.where()

class MongoDBClient:
    """MongoDBClient is responsible for establishing a connection to the MongoDB database.
    
    Attributes:
    client: MongoDBClient
        A shared MongoClient instance for the class.
    database: Database
       The specific database instance that MongoDBClient connects to.
    Methods:
    __init__(database_name: str) -> None
        Initializes the MongoDB connection using the given database name.
    
    """
    client = None  # Shared MongoClient instance
    
    def __init__(self, database_name: str = DATABASE_NAME) -> None:
        """
        Initializes a connection to the MongoDB database. If no existing connection is found, it establishes a new one.

        Parameters:
        ----------
        database_name : str, optional
            Name of the MongoDB database to connect to. Default is set by DATABASE_NAME constant.

        Raises:
        ------
        MyException
            If there is an issue connecting to MongoDB or if the environment variable for the MongoDB URL is not set.
        """
        try:
            #Check if a MongoDB has already been established; if not , create a connection
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise MyException(f"{MONGODB_URL_KEY} environment variable not set")
                # Stablish a new MongoDB client connection
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
                
            # Use the MongoClient for this instance 
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info(f"Successfully connected to MongoDB database: {database_name}")
        
        except Exception as e:
            # raise a custom exception with traceback details if connection fails
            raise MyException(e, sys)