# Add a line for setting the controller "app" which matches the name of the
# module that hosts the controller functions.
sed -i 's/"operation/"x-swagger-router-controller": "ga4gh.wes.server", \n        "operation/g' workflow_execution_service.swagger.json
# Inject a base path
sed -i 's/"swagger"/  "basePath": "\/", "swagger"/g' workflow_execution_service.swagger.json
mv workflow_execution_service.swagger.json swagger/workflow_execution_service.swagger.json
