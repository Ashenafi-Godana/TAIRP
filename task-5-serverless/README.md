# Random Number Generator Serverless Function

This project demonstrates a simple serverless function deployed on AWS Lambda, which generates random numbers and exposes them through API Gateway.

## Prerequisites

Before you begin, ensure you have the following:

- An AWS account
- AWS CLI installed and configured
- Python (if you want to modify the Lambda function)
- Optionally, a tool like `curl` or Postman for testing the API

## Deployment Steps

1. **Create the Lambda Function**:

   - Log in to the AWS Management Console.
   - Open the Lambda service.
   - Create a new Lambda function.
   - Choose the appropriate runtime (e.g., Python 3.8).
   - Copy and paste the code from `lambda_function.py`.
   - Save and deploy the Lambda function.

2. **Create API Gateway**:

   - Open the API Gateway service.
   - Create a new REST API.
   - Add a new resource and method (e.g., GET).
   - Choose "Integration type" as "Lambda Function" and select the Lambda function you created.
   - Deploy the API.

## Usage

Once the deployment is complete, you can access the API endpoint to generate random numbers. Each request to the endpoint will trigger the Lambda function, which will return a random number between 1 and 100.

## Additional Information

- This is a basic example to introduce you to serverless computing and event-driven architectures using AWS Lambda and API Gateway.
- You can modify the Lambda function to perform more complex tasks or integrate with other AWS services.
- Ensure to manage your AWS resources efficiently to avoid unexpected costs.
