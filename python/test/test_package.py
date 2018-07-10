# -*- coding: utf-8 -*-
import os.path
import unittest

import swagger_spec_validator
import yaml


class TestPackage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cwd = os.path.dirname(os.path.realpath(__file__))
        spec_dir = os.path.join(cwd, '../../openapi')
        cls.swagger_path = os.path.join(spec_dir, 'workflow_execution_service.swagger.yaml')

    def test_version_consensus(self):
        from ga4gh.wes import __version__
        with open(self.swagger_path, 'r') as f:
            spec_version = yaml.safe_load(f)['info']['version']
        assert __version__ == spec_version

    def test_schema_validity(self):
        """Check to make sure that the Swagger schema specification is
        valid by running it through the online validator. If the schema
        is valid, the online validator will return 200 OK and an empty
        JSON response."""
        path = os.path.abspath(self.swagger_path)
        swagger_spec_validator.validate_spec_url('file://' + path)