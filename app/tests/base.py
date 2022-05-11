import unittest
import json
from fastapi.testclient import TestClient
from mongoengine import connect, disconnect
from main import app

# client = TestClient(app)


class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connect("mongoenginetest", host="mongomock://127.0.0.1:8000")
        cls.client = TestClient(app)

    @classmethod
    def tearDownClass(cls):
        disconnect()

    def setUp(self):
        data = open("app/dummy_data/homework_quiz.json")
        self.quiz_data = json.load(data)
        # We are currently not providing an endpoint for creating questions and the only way to
        # create a question is through the quiz endpoint which is why we are using the quiz endpoint
        # to create questions and a quiz
        response = self.client.post("/quiz/", json=self.quiz_data)
        self.quiz = json.loads(response.content)
