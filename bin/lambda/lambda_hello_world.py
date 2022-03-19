"""
This is a hello world example for a AWS lambda
"""
import json

def lambda_handler(event,context):
    """
    Function called when lambda is executed
    """
    return {
        'statusCode': 200,
        'body': json.dumps('Complete: ' + str(event) + ' ' + str(context) )
    }
