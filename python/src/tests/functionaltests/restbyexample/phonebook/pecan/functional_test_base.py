import os
from unittest import TestCase

from pecan import set_config
from pecan.testing import load_test_app

from restbyexample.phonebook import PhonebookDbAdapterImpl
from restbyexample.phonebook.pecan.controllers.root import RootController


class FunctionalTestBase(TestCase):
    def setUp(self):
        self.app = load_test_app(os.path.join(os.path.dirname(__file__), 'config.py'))
        RootController.phonebook._db_adapter = PhonebookDbAdapterImpl()

    def tearDown(self):
        set_config({}, overwrite=True)