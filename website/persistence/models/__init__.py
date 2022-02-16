from website.persistence.db import Document, db


class User(Document):
    collection = db.users

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.email


class Data(Document):
    collection = db.data


class Diary(Document):
    collection = db.dairy


class Training(Document):
    collection = db.training


class Sleep(Document):
    collection = db.sleep
