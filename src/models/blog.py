import uuid
import datetime

from src.common.database import Database
from src.models.post import Post


class Blog(object):
    """

    """
    def __init__(self, author, title, description, author_id, _id=None):
        self.author = author
        self.title = title
        self.description = description
        self.author_id = author_id
        self._id = uuid.uuid4().hex if _id is None else _id

    def new_post(self, title, content, date=datetime.datetime.utcnow()):
        """

        :param title:
        :param content:
        :param date:
        """
        post = Post(blog_id=self._id,
                    title=title,
                    content=content,
                    author=self.author,
                    created_date=date)
        post.save_to_mongo()

    def get_posts(self):
        """

        :return:
        """
        return Post.from_blog(self._id)

    def save_to_mongo(self):
        """

        """
        Database.insert(collection='blogs',
                        data=self.json())

    def json(self):
        """

        :return:
        """
        return {
            'author': self.author,
            'author_id': self.author_id,
            'title': self.title,
            'description': self.description,
            '_id': self._id
        }

    @classmethod
    def from_mongo(cls, id):
        """

        :param id:
        :return:
        """
        blog_data = Database.find_one(collection='blogs',
                                      query={'_id': id})
        return cls(**blog_data)

    @classmethod
    def find_by_author_id(cls, author_id):
        """

        :param author_id:
        :return:
        """
        blogs = Database.find(collection='blogs',
                              query={'author_id': author_id})
        return [cls(**blog) for blog in blogs]
