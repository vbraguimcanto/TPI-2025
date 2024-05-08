import json

def lambda_handler(event, context):
    """ Lambda function to send e-mails
    Parameters
    ----------
    event: dict, required - API Gateway Lambda Proxy Input Format
    context: object, required - Lambda Context runtime methods and attributes

    Returns
    ------
        API Gateway Lambda Proxy Output Format: dict
    """
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message':'Hello World'})
    }