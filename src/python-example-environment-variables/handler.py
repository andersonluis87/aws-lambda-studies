import os


def hello(event, context):
    return os.environ['ENVIRONMENT_NAME']
