import pymongo
from src.secrets.secrets import DATABASE_API
class Database(object):

    URI = DATABASE_API
    DATABASE = ""

    @staticmethod
    def initialize():
        """

        """
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']
        print('DataBase initialized')

    @staticmethod
    def insert(collection, data):
        """

        :param collection:
        :param data:
        """
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def update_one(collection,filter,data):
        Database.DATABASE[collection].update_one(filter,data)

    @staticmethod
    def find(collection, query):
        """

        :param collection:
        :param query:
        :return:
        """
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_all(collection):
        """

        :param collection:
        :param query:
        :return:
        """
        return Database.DATABASE[collection].find()

    @staticmethod
    def find_one(collection, query):
        """

        :param collection:
        :param query:
        :return:
        """
        return Database.DATABASE[collection].find_one(query)
