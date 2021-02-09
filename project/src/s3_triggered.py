import json

import paramiko
import pymysql

from core import TEST_VALUE


def lambda_handler(event, context):
    return {
        'status': 200,
        'data': json.dumps({
            'event': event,
            'value': TEST_VALUE
        })
    }
