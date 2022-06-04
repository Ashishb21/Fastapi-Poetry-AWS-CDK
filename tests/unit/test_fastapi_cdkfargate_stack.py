import aws_cdk as core
import aws_cdk.assertions as assertions

from fastapi_cdkfargate.fastapi_cdkfargate_stack import FastapiCdkfargateStack

# example tests. To run these tests, uncomment this file along with the example
# resource in fastapi_cdkfargate/fastapi_cdkfargate_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = FastapiCdkfargateStack(app, "fastapi-cdkfargate")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
