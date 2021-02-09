import json

import pymysql


def lambda_handler(event, context):
    return {
        'status': 200,
        'data': json.dumps({
            'event': event
        })
    }
 