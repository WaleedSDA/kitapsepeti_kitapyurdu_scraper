class DbWrapper:

    __connection_string = f"mongodb+srv://{__user}:<{__password}>@{__host}/?retryWrites=true&w=majority",
    __client: str = pymongo.MongoClient(
        __connection_string,
        tlsCAFile=certifi.where())
    __db = __client[__database]

    def __init__(self, collection: str):
        self._collection: pymongo.collection.Collection = self.__db[collection]

    def insert_one(self, record):
        record = serialize(record)
        result = self._collection.insert_one(record)
        return result

    def insert_many(self, record):
        record = serialize(record)
        result = self._collection.insert_many(record)
        return result

    def find(self, record):
        result = self._collection.find(record)
        return result

    def find_one(self, record):
        result = self._collection.find_one(record)
        return result

    def replace_one(self, filter_condition: dict, record):
        record = serialize(record)
        result = self._collection.replace_one(filter_condition, record)
        return result

    def update_one(self, find_query, update_query):
        update_query = serialize(update_query)
        result = self._collection.update_one(find_query, update_query)
        return result
