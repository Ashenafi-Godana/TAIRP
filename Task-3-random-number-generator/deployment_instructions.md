1. Deployment instruction:
   Deploying the serverless function involves creating the Lambda function and configuring API Gateway. Here are detailed deployment instructions:

1.1. Create Lambda Function:

- Go to the AWS Lambda console.
- Click on "Create function" and select "Author from scratch".
- Provide a name for your function (e.g., RandomNumberGenerator).
- Choose a runtime (e.g., Python 3.8).
- Paste the Lambda function code into the code editor.
- Click on "Create function" to create the Lambda function.

  1.2 Configure API Gateway:

- Go to the AWS API Gateway console.
- Click on "Create API" and choose "HTTP API".
- Name your API (e.g., RandomNumberAPI).
- Click on "Create API".
- Create a new resource by clicking on "Create" under the "Resources" section.
- Name the resource (e.g., random-number).
- Create a new GET method by clicking on the "Actions" dropdown and selecting "Create method".
- Choose "Lambda function" as the integration type.
- Select the appropriate region and choose your Lambda function (e.g., RandomNumberGenerator).
- Click on "Save" to save the configuration.

  1.3 Deploy API:

- Click on "Deploy API" in the top-right corner of the API Gateway console.
- Choose a stage name (e.g., prod) and click on "Deploy".
- Note down the provided Invoke URL, as it will be used to access the API.
