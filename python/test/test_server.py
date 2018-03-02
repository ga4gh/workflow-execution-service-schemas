# With app.py running start this test
import logging
import uuid
import unittest
import subprocess
import time

# setup connection, models and security
from bravado.requests_client import RequestsClient
from bravado.exception import HTTPNotFound

from ga4gh.dos.client import Client

SERVER_URL = 'http://localhost:8080/ga4gh/wes/v1'


class TestServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # start a test server
        print('setting UP!!!!!!!!!!')
        p = subprocess.Popen(
            ['ga4gh_dos_server'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=False)
        time.sleep(2)
        # print(p.poll(), p.pid)
        cls._server_process = p

        http_client = RequestsClient()
        # http_client.set_basic_auth(
        #   'localhost', 'admin', 'secret')
        # http_client.set_api_key(
        #   'localhost', 'XXX-YYY-ZZZ', param_in='header')
        local_client = Client(SERVER_URL, http_client=http_client)
        client = local_client.client
        models = local_client.models

        # setup logging
        root = logging.getLogger()
        root.setLevel(logging.ERROR)
        logging.captureWarnings(True)
        cls._models = models

        cls._client = client
        cls._local_client = local_client

    @classmethod
    def tearDownClass(cls):
        print('tearing down')
        print(cls._server_process.pid)
        cls._server_process.kill()
        cls._server_process.terminate()

    def test_nothing(self):
        """test nothing"""
        assert True
