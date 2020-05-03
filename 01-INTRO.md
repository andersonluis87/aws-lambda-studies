# AWS Lambda

- Virtual functions - no servers to manage!
- Limited by time - short executions
- Run on-demand
- Scaling is automated!

- Easy Pricing:
    - Pay per request and compute time
    - Free tier of 1.000.000 AWS Lambda requests and 400.000 GBs of compute time

- Integrated with the whole AWS Stack
- Integrated with many programming languages
- Easy monitoring through AWS CloudWatch
- Easy to get more resources per funcions (up to 1.5GB of RAM!)
- Increasing RAM will also improve CPU and network!

## Languages
- aws-nodejs 
- aws-python
- aws-python3
- aws-groovy-gradle
- aws-java-gradle
- aws-java-maven
- aws-scala-sbt
- aws-csharp

## Integrations
- **API Gateway:** Provides an APi for you yours directly to your Lambda funcions
- **Kinesis:** Real time streaming of data. Your Lambda functions can process data as it arrives in streams in Kinesis.
- **DynamoDB:** NoSQL database. You can store your data using lambda funcions.
- **AWS S3 - Simple Storage Service:** You can access files stored in S3 buckets using lambda functions as well
- **AWS IoT Internet of Things** 
- **CloudWatch Events:** Run your functions in a schecule or cron job
- **CloudWatch Logs:** Streaming logs
- **AWS SNS - Simple Notification Service:** Notify users via e-mail, SMS... 
- **AWS Cognito:** User Integration


# Serverless Framework
- The serverless framework aims to ease the pain of creating, deploying, managing and debugging Lambda functions.
- It integrates well with CI/CD tools
- It has CloudFormation support so your entire stack can be deployed using this Framework

## Installing Serverless
1. Install dependencies (node and AWS CLI)
    - NodeJS: https://nodejs.org/en/download/package-manager/
    - AWS CLI: https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html
2. Install serverless framework:
    ```
    npm install -g serverless
    ```
3. Setting up AWS for the `serverless-admin` user
    - On your AWS Console:
        - Go to IAM > Users 
        - Add a user named `serverles-admin` (recommended)
        - Under Select AWS Access type, tick "Programmatic access".
        - On Permissions, click on "Attach existing policies directly" and tick "AdministratorAccess"
        - Click on "Create User" and download the credentials.
4. Download credentials on you machine
5. Setup Serverless to use these credentials
    ``` 
    serverless config credentials --provider aws --key {USER_KEY} --secret {YOUR_SECRET} --profile serverless-admin
    ```

## Deploying a Hello World Function Using Serverless
1. Creating and Preparing our first hello-world service:
    - You can create a new project by simply typing `serverless` or `sls` on you terminal.
    - After selecting your template, go to the project created and open the `serverless.yml` file.
    - Add the `profile` and `region` in the `provider`:
        ```yml
        provider:
            name: aws
            runtime: python3.8
            profile: serverless-admin
            region: sa-east-1
        ```  
2. Deploying the Service:
    ```
    sls deploy -v
    ```

## Invoking the function
1. Invoking the function on AWS Console
2. Invoking the function from our computer using Serverless:
    ```
    sls invoke -f hello -l
    ```

## Updating the function
1. Change the function content
    - Make any changes to the function
2. Deploy the stack
    - Use the same command we used before:
    ```
    sls deploy -v
    ```
    *Notice this deploy overwrites the whole stack, which takes some time depending on the files size*
3. Change the function
    - Make another change to the function
4. Deploy the function without deploying the entire stack
    ```
    sls deploy function -f hello
    ```
    This updates only the function code.
    *Notice that the second deploy was much faster than the first one*


## Fetching function logs
1. View function logs in AWS CloudWatch Logs
    - Go to Monitoring > View logs in CloudWatch
2. Stream function logs from our computer using Serverless
    ```
    sls logs -f hello -t
    ```

## Destroying the Service
- Problem - we need to clean up:
    - Function
    - Dependencies of the function
    - CloudWatch Log groups
    - IAM Roles
    - Everything else the framework has created
- Serverless solves these problems for us:
    ```
    sls remove
    ```