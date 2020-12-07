import pymongo
class Database(object):

    URI = "mongodb+srv://dbadmin:dbadmin@cluster0.x710q.mongodb.net/educationalapp?retryWrites=true&w=majority"
    DATABASE = ""

    @staticmethod
    def initialize():
        """

        """
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(collection, data):
        """

        :param collection:
        :param data:
        """
        Database.DATABASE[collection].insert(data)

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
