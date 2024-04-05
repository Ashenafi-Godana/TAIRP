import json
import random

def lambda_handler(event, context):
    # Generate a random number
    random_number = random.randint(1, 100)
    
    # Prepare the response
    response = {
        "statusCode": 200,
        "body": json.dumps({
            "random_number": random_number
        })
    }
    
    return response
