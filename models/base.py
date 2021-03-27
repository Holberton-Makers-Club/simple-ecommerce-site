"""
Base class handles serialization/deserialization by calling methods of a given database connection
The default connection is FirestoreClient
"""

from models.storage.firestore import FirestoreClient


class Base():
    """ Base Model """
    db_client = FirestoreClient()

    def __init__(self, *args, **kwargs):
        """ init """
        from uuid import uuid4
        for (k, v) in kwargs.items():
            setattr(self, k, v)
        if not kwargs.get('id'):
            self.id = str(uuid4())

    @classmethod
    def connection(cls):
        return Base.db_client.connected()

    @classmethod
    def get_by_class(cls):
        return Base.db_client.get_by_class(cls.__name__)
    
    @classmethod
    def get_by_id(cls, id):
        return Base.db_client.get_by_id(cls.__name__, id)
    
    @classmethod
    def get_by_attr(cls, attr, val):
        return Base.db_client.get_by_attr(cls.__name__, attr, val)
    
    def to_dict(self):
        """ return dictionary representation of object """
        return self.__dict__

    def save(self):
        print('saving')
        Base.db_client.save(self)

    @classmethod
    def update_attr_by_id(cls, id, attr, val):
        return Base.db_client.update_attr_by_id(cls, id, attr, val)

    def delete(self):
        Base.db_client.delete(self)
    
    @classmethod
    def delete_by_id(cls, id):
        Base.db_client.delete_by_id(cls, id)
