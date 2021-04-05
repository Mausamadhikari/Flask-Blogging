import uuid

from flask import session
from src.common.database import Database
from src.models.blog import Blog


class User(object):
    """

    """
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    @classmethod
    def get_by_email(cls, email):
        """

        :param email:
        :return:
        """
        data = Database.find_one("users", {"email": email})
        if data is not None:
            return cls(**data)

    @classmethod
    def get_by_id(cls, _id):
        """

        :param _id:
        :return:
        """
        data = Database.find_one("users", {"_id": _id})
        if data is not None:
            return cls(**data)

    @staticmethod
    def login_valid(email, password):
        """

        :param email:
        :param password:
        :return:
        """
        user = User.get_by_email(email)
        if user is not None:
            return user.password == password
        return False

    @classmethod
    def register(cls, email, password):
        """

        :param email:
        :param password:
        :return:
        """
        user = cls.get_by_email(email)
        if user is None:
            new_user = cls(email, password)
            new_user.save_to_mongo()
            session['email'] = email
            return True
        else:
            return False

    @classmethod
    def updateprofile(cls, email, name):
        """
        update profile
        """
        user = User.get_by_email(email)
        filters = {
            "email": session['email']
        }
        data = {
            "$set": {
                "name": name
            }
        }
        user.update_to_mongo(filters, data)

    @staticmethod
    def login(user_email):
        """

        :param user_email:
        """
        session['email'] = user_email

    @staticmethod
    def logout():
        """

        """
        session['email'] = None

    def get_blogs(self):
        """

        :return:
        """
        return Blog.find_by_author_id(self._id)

    def json(self):
        """

        :return:
        """
        return {
            "email": self.email,
            "_id": self._id,
            "password": self.password
        }

    def save_to_mongo(self):
        """

        """
        Database.insert("users", self.json())
