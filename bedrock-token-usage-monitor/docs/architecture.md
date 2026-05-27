# Architecture

This example records Amazon Bedrock token usage metadata with a single Lambda function.

~~~text
Client or test event
  -> Lambda
     -> CountTokens: estimate input tokens before inference
     -> Token limit check: block requests over MAX_INPUT_TOKENS
     -> Converse: call Amazon Bedrock when the request is allowed
     -> DynamoDB: store token usage metadata only
     -> CloudWatch Logs: print token usage summary only
~~~

## Data flow

1. The caller sends user_id, prompt, and optionally model_id.
2. Lambda builds a Converse-compatible message payload.
3. Lambda calls CountTokens with the same messages.
4. Lambda blocks the request if estimated input tokens exceed MAX_INPUT_TOKENS.
5. Lambda calls Bedrock Converse when the request is allowed.
6. Lambda extracts inputTokens, outputTokens, and totalTokens from the response usage field.
7. Lambda stores usage metadata in DynamoDB.
8. Lambda writes usage metadata to the default Lambda CloudWatch Logs group.

## Stored data

The DynamoDB record stores only metadata:

- request_id
- user_id
- model_id
- estimated_input_tokens
- input_tokens
- output_tokens
- total_tokens
- created_at

The example does not store the original prompt or model answer in DynamoDB or CloudWatch Logs.
