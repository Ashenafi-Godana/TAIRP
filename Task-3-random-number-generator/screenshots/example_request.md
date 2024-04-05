Request:
GET https://your-api-id.execute-api.your-region.amazonaws.com/prod/random-number

Response(200 OK):
{
"random_number": 42
}

You can make requests to the API using tools like cURL or Postman. Each request will trigger the Lambda function to generate a new random number, which will be returned in the response.
