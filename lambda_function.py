import json

def lambda_handler(event, context):
    f = open('gonda.json',)
    data = json.load(f)
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps(data)
    # }
    return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET',
                "Access-Control-Allow-Credentials": 'true'
            },
            'body': json.dumps(data)
        }
