# IAM Permissions for Lambda fuctions
- Our lambda funcions access other services
    - For example S3 to storage images
    - Or DynamoDB to store and retrieve data
- By Default our Lambda functions are not authorized to do that
- So for this, we provide an IAM policy
- IAM allows you to entirely secure your AWS Setup

You can add policies by editing the `serverless.yml` file: 
```yml
    provider:
    name: aws
    runtime: python3.8
    profile: serverless-admin
    region: sa-east-1
    iamRoleStatements:
        - Effect: "Allow"
        Action:
            - "lambda:*"
        Resource:
            - "*"
```