import certifi
import pymongo as pymongo

from core.dotenv_util import DotEnvGetter
from utils.funcs import serialize_dataclass


class DbWrapper:
    """
    A class used to interact with a MongoDB collection.

    ...

    Attributes
    ----------
    __connection_string : str
        The connection string to MongoDB obtained from environment variables.
    __client : pymongo.MongoClient
        The MongoDB client instance.
    __db : pymongo.database.Database
        The MongoDB database instance.
    _collection : pymongo.collection.Collection
        The MongoDB collection instance to be used for the operations.

    Methods
    -------
    insert_one(record):
        Inserts a single record into the collection.
    insert_many(record):
        Inserts multiple records into the collection.
    find(record):
        Finds all records that match the query in the collection.
    find_one(record):
        Finds the first record that matches the query in the collection.
    replace_one(filter_condition, record):
        Replaces the first record that matches the filter condition in the collection.
    update_one(find_query, update_query):
        Updates the first record that matches the find_query in the collection.
    """

    __connection_string = DotEnvGetter().db_uri,
    __client: str = pymongo.MongoClient(
        __connection_string,
        tlsCAFile=certifi.where())
    __db = __client[DotEnvGetter().db_name]

    def __init__(self, collection: str):
        """
        Initializes the DbWrapper with a specific collection.

        Parameters
        ----------
        collection : str
            The name of the collection to be used for the operations.
        """
        self._collection: pymongo.collection.Collection = self.__db[collection]

    def insert_one(self, record):
        """
        Inserts a single record into the collection.

        Parameters
        ----------
        record : Any
            The record to be inserted into the collection.

        Returns
        -------
        pymongo.results.InsertOneResult
            The result of the insert operation.
        """
        record = serialize_dataclass(record)
        result = self._collection.insert_one(record)
        return result

    def insert_many(self, record):
        """
        Inserts multiple records into the collection.

        Parameters
        ----------
        record : list
            The records to be inserted into the collection.

        Returns
        -------
        pymongo.results.InsertManyResult
            The result of the insert operation.
        """
        record = serialize_dataclass(record)
        result = self._collection.insert_many(record)
        return result

    def find(self, record):
        """
        Finds all records that match the query in the collection.

        Parameters
        ----------
        record : dict
            The query to find records in the collection.

        Returns
        -------
        pymongo.cursor.Cursor
            The cursor to the found records.
        """
        result = self._collection.find(record)
        return result

    def find_one(self, record):
        """
        Finds the first record that matches the query in the collection.

        Parameters
        ----------
        record : dict
            The query to find a record in the collection.

        Returns
        -------
        dict or None
            The found record, or None if no record matches the query.
        """
        result = self._collection.find_one(record)
        return result

    def replace_one(self, filter_condition: dict, record):
        """
        Replaces the first record that matches the filter condition in the collection.

        Parameters
        ----------
        filter_condition : dict
            The filter condition to find a record in the collection.
        record : Any
            The record to replace the found record with.

        Returns
        -------
        pymongo.results.UpdateResult
            The result of the replace operation.
        """
        record = serialize_dataclass(record)
        result = self._collection.replace_one(filter_condition, record)
        return result

    def update_one(self, find_query, update_query):
        """
        Updates the first record that matches the find_query in the collection.

        Parameters
        ----------
        find_query : dict
            The query to find a record in the collection.
        update_query : dict
            The modifications to apply.

        Returns
        -------
        pymongo.results.UpdateResult
            The result of the update operation.
        """
        update_query = serialize_dataclass(update_query)
        result = self._collection.update_one(find_query, update_query)
        return result
