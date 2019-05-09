# Simple server implementation
import os

import connexion
from flask_cors import CORS

# These are imported by name by connexion so we assert it here.
from controllers import *  # noqa


SWAGGER_FILENAME = 'workflow_execution_service.swagger.yaml'
current_directory = os.path.dirname(os.path.realpath(__file__))
SWAGGER_PATH = os.path.join(current_directory, SWAGGER_FILENAME)


def configure_app():
    # The model name has to match what is in
    # tools/prepare_swagger.sh controller.
    app = connexion.App(
        "ga4gh.wes.server",
        swagger_ui=True,
        swagger_json=True)
    app.add_api(SWAGGER_PATH)

    CORS(app.app)
    return app


def main():
    app = configure_app()
    app.run(port=8080, debug=True)


if __name__ == '__main__':
    main()
