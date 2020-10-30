from aws_cdk import (
aws_lambda as lb,
aws_apigateway as apigw,
core
)
class RootstreamTwitchStreamlinkStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        lambda_function = lb.Function(self, 'streamlinkerfunction',
           runtime=lb.Runtime.PYTHON_3_8,
           code=lb.Code.asset('lambda'),
           handler='streamlinker.handler'
        )
  
        api_gateway = apigw.LambdaRestApi(self,'streamlinker', handler=lambda_function, rest_api_name='streamlinkerapi')
