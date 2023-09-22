import unittest
import sys
import os
from flask import Flask
from flask_testing import TestCase
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

class TestApp(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_index(self):
        response = self.client.get('/')
        self.assert200(response)
        self.assertIn('Calculadora de Suma de Números Pares'.encode('utf-8'), response.data)

    def test_calculate_sum(self):
        response = self.client.post('/', data={'numero_inicio': '1', 'numero_fin': '10'})
        self.assert200(response)
        self.assertIn('La suma de los números pares'.encode('utf-8'), response.data)
        self.assertIn(b'30', response.data)

if __name__ == '__main__':
    unittest.main()
