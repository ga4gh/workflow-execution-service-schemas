# Simple client usage via bravo


from bravado.client import SwaggerClient
from bravado.swagger_model import Loader
from bravado.requests_client import RequestsClient
from bravado_core.exception import SwaggerValidationError
from bravado_core.formatter import SwaggerFormat

DEFAULT_CONFIG = {
    'validate_requests': True,
    'validate_responses': True
}


def validate_int64(test):
    # TODO improve to check numerality
    if str(test) != test:
        raise SwaggerValidationError('int64 are serialized as strings')


# This is to support serializing int64 as strings on the wire. JavaScript
# only supports up to 2^53.
int64_format = SwaggerFormat(
        format='int64',
        to_wire=lambda i: str(i) if isinstance(int, long) else i,
        to_python=lambda i: i if isinstance(str, long) else long(i),
        validate=validate_int64,  # jsonschema validates integer
        description='Converts [wire]str:int64 <=> python long')


class Client:
    """
    simple wrapper around bravado swagger Client. see
    https://github.com/Yelp/bravado/blob/master/docs/source/configuration.rst#client-configuration
    https://github.com/Yelp/bravado#example-with-basic-authentication
    """
    def __init__(
            self, url, config=DEFAULT_CONFIG,
            http_client=None, request_headers=None):
        swagger_path = '{}/swagger.json'.format(url.rstrip("/"))
        config['formats'] = [int64_format]
        self._config = config
        self.models = SwaggerClient.from_url(swagger_path,
                                             config=config,
                                             http_client=http_client,
                                             request_headers=request_headers)
        self.client = self.models.WorkflowExecutionService

    @classmethod
    def config(cls, url, http_client=None, request_headers=None):
        swagger_path = '{}/swagger.json'.format(url.rstrip("/"))
        http_client = http_client or RequestsClient()
        loader = Loader(http_client, request_headers=request_headers)
        spec_dict = loader.load_spec(swagger_path)
        return spec_dict


def main():
    print('client')


if __name__ == '__main__':
    main()
