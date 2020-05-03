# Environment Variables
- Enviromnent variables are good because they provide external **configuration** to your functions
- This way, we can change a function's behaviour without even changing the code of the function.

## Usage
1. Define environment variables
    ```yml
    environment:
    ENVIRONMENT_NAME: Production
    ```
2. Use environment variables
    ```yml
    functions:
    hello-env-prod:
        handler: handler.hello
    hello-env-dev:
        handler: handler.hello
        environment:
        ENVIRONMENT_NAME: Development
    ```


