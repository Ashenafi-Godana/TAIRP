import json
import random

def lambda_handler(event, context):
    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)
    
    # Prepare the response
    response = {
        "statusCode": 200,
        "body": json.dumps({
            "random_number": random_number
        })
    }
    
    return response
