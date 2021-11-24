#!/usr/bin/python3
""" """
from models.base_model import Base
from models import BaseModel, City, Place, State, User
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel
        self.dict = {}
        self.state = State({'name': "test_state"})
        self.city = City({'state_id': self.state.id, 'name': "test_city"})
        self.user = User({'email': "test@test.net",
                          'password': "test_password"})
        self.place = Place({'city_id': self.city.id, 'user_id': self.user.id,
                            'description': "", 'latitude': 0.0,
                            'longitude': 0.0, 'name': 'test_place'})

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        from models import storage
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_default(self):
        """ """
        i = self.value(**self.dict)
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ """
        i = self.value(**self.dict)
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = self.value(**self.dict)
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "test relies on filestorage")
    def test_save(self):
        """ Testing save """
        i = self.value(**self.dict)
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ """
        i = self.value(**self.dict)
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ """
        i = self.value(**self.dict)
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    @unittest.skip("test no longer relevant")
    def test_kwargs_one(self):
        """ """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """ """
        new = self.value(**self.dict)
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        new = self.value(**self.dict)
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ """
        new = self.value(**self.dict)
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
