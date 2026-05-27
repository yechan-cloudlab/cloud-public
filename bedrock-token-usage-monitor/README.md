# Amazon Bedrock Token Usage Monitor

This repository contains an AWS SAM example that counts and records Amazon Bedrock token usage with AWS Lambda.

The Lambda function does three things:

1. Calls Amazon Bedrock CountTokens before inference to estimate input tokens.
2. Blocks the request when the estimated input token count exceeds MAX_INPUT_TOKENS.
3. Calls Amazon Bedrock Converse, returns the model answer, and records token usage metadata.

The Lambda response includes the model answer and token usage. DynamoDB and CloudWatch Logs store only token usage metadata, not the original prompt or answer text.

## Architecture

~~~text
Client or test event
  -> Lambda
     -> CountTokens
     -> Input token limit check
     -> Bedrock Converse
     -> DynamoDB token usage metadata
     -> CloudWatch Logs token usage summary
~~~

## Project structure

~~~text
bedrock-token-usage-monitor/
+-- README.md
+-- template.yaml
+-- .gitignore
+-- src/
|   +-- app.py
|   +-- requirements.txt
+-- events/
|   +-- sample-request.json
+-- docs/
    +-- architecture.md
~~~

## Prerequisites

- AWS CLI configured with deploy permissions
- AWS SAM CLI installed
- Python 3.12
- Amazon Bedrock model access enabled in the target AWS Region
- boto3 version that supports bedrock-runtime CountTokens. This example pins boto3 in src/requirements.txt for Lambda packaging
- Permission to create Lambda, DynamoDB, IAM, and CloudWatch Logs resources

This example invokes Amazon Bedrock. Bedrock, Lambda, DynamoDB, and CloudWatch Logs usage can incur AWS charges.

## Deploy

From this directory:

~~~bash
sam build
sam deploy --guided
~~~

During deployment, set these parameters as needed:

- TokenUsageTableName: DynamoDB table name for usage metadata
- MaxInputTokens: maximum estimated input tokens allowed before blocking
- DefaultModelId: default Bedrock model ID
- DefaultMaxOutputTokens: default maximum output tokens for the Converse call

CloudWatch Logs are written to the default Lambda log group:

~~~text
/aws/lambda/<function-name>
~~~

## Test with a sample event

After deployment, invoke the Lambda function with the sample event:

~~~bash
sam remote invoke BedrockTokenUsageFunction --event-file events/sample-request.json
~~~

You can also invoke the deployed Lambda from the AWS Console or AWS CLI.

## Request format

~~~json
{
  "user_id": "demo-user",
  "model_id": "anthropic.claude-3-haiku-20240307-v1:0",
  "prompt": "Explain Amazon Bedrock in one sentence.",
  "max_tokens": 256,
  "temperature": 0.2,
  "top_p": 0.9
}
~~~

model_id is optional when DEFAULT_MODEL_ID is configured.

## Lambda response example

~~~json
{
  "request_id": "7e9a3f3a-1f37-4d11-89a5-0f5b4d6e1a9b",
  "user_id": "demo-user",
  "model_id": "anthropic.claude-3-haiku-20240307-v1:0",
  "answer": "Amazon Bedrock is a fully managed AWS service for building generative AI applications.",
  "usage": {
    "estimated_input_tokens": 42,
    "input_tokens": 42,
    "output_tokens": 31,
    "total_tokens": 73
  }
}
~~~

## DynamoDB record

The DynamoDB table stores token usage metadata only:

~~~json
{
  "request_id": "7e9a3f3a-1f37-4d11-89a5-0f5b4d6e1a9b",
  "user_id": "demo-user",
  "model_id": "anthropic.claude-3-haiku-20240307-v1:0",
  "estimated_input_tokens": 42,
  "input_tokens": 42,
  "output_tokens": 31,
  "total_tokens": 73,
  "created_at": "2026-05-27T00:00:00+00:00"
}
~~~

The example does not store:

- prompt text
- model answer text
- AWS credentials
- cost calculation results

## CloudWatch Logs

The Lambda function prints a token usage summary to CloudWatch Logs:

~~~json
{
  "event": "bedrock_token_usage",
  "request_id": "7e9a3f3a-1f37-4d11-89a5-0f5b4d6e1a9b",
  "user_id": "demo-user",
  "model_id": "anthropic.claude-3-haiku-20240307-v1:0",
  "blocked": false,
  "usage": {
    "estimated_input_tokens": 42,
    "input_tokens": 42,
    "output_tokens": 31,
    "total_tokens": 73
  }
}
~~~

Use the Lambda function name from the SAM output to find the log group:

~~~text
/aws/lambda/<function-name>
~~~

## Security notes

- Do not commit AWS credentials.
- Do not log raw prompts or model answers when they may contain sensitive data.
- Review Bedrock model access and IAM permissions before deployment.
- Keep token counting separate from cost calculation because model pricing can vary by model, Region, and date.

## Related article

- [Amazon Bedrock token usage monitoring with Lambda](https://tistory-cloud.tistory.com/entry/Amazon-Bedrock-%ED%86%A0%ED%81%B0-%EC%82%AC%EC%9A%A9%EB%9F%89-%EB%AA%A8%EB%8B%88%ED%84%B0%EB%A7%81-Lambda%EB%A1%9C-%EC%9E%85%EB%A0%A5%C2%B7%EC%B6%9C%EB%A0%A5-%ED%86%A0%ED%81%B0%EC%9D%84-%EA%B3%84%EC%82%B0%ED%95%98%EA%B3%A0-%EA%B8%B0%EB%A1%9D%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95)

