# API Documentation

This document describes the API interface for the CodeLlama fine-tuned model.

## Overview

The CodeLlama model can be served via a REST API for integration with the VS Code extension and other applications.

## Endpoints

### POST /generate

Generates code completion or continuation based on the provided prompt.

#### Request

```json
{
  "prompt": "def factorial(n):",
  "max_length": 150,
  "temperature": 0.7,
  "top_p": 0.9,
  "num_return_sequences": 1
}
```

#### Parameters

- `prompt` (string, required): The input code or description to complete
- `max_length` (integer, optional): Maximum length of generated text (default: 100)
- `temperature` (float, optional): Sampling temperature (default: 0.7)
- `top_p` (float, optional): Nucleus sampling parameter (default: 0.9)
- `num_return_sequences` (integer, optional): Number of sequences to generate (default: 1)

#### Response

```json
{
  "generated_text": "\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n-1)",
  "prompt": "def factorial(n):",
  "model_info": {
    "model_name": "codellama-finetuned",
    "version": "1.0.0"
  }
}
```

#### Error Response

```json
{
  "error": "Invalid request",
  "message": "Prompt cannot be empty",
  "code": 400
}
```

## Usage Examples

### Python

```python
import requests

response = requests.post('http://localhost:8000/generate', json={
    'prompt': 'def fibonacci(n):',
    'max_length': 100,
    'temperature': 0.5
})

result = response.json()
print(result['generated_text'])
```

### JavaScript

```javascript
const response = await fetch('http://localhost:8000/generate', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        prompt: 'function quickSort(arr) {',
        max_length: 200,
        temperature: 0.6
    })
});

const result = await response.json();
console.log(result.generated_text);
```

### cURL

```bash
curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "class Calculator:",
    "max_length": 150,
    "temperature": 0.7
  }'
```

## Rate Limiting

The API implements rate limiting to ensure fair usage:

- **Rate Limit**: 100 requests per minute per IP
- **Burst Limit**: 10 requests per second

When rate limits are exceeded, the API returns a 429 status code.

## Authentication

Currently, the API does not require authentication for local development. For production deployments, consider implementing API key authentication.

## Error Codes

| Code | Description |
|------|-------------|
| 200  | Success |
| 400  | Bad Request - Invalid parameters |
| 429  | Too Many Requests - Rate limit exceeded |
| 500  | Internal Server Error |

## Model Information

The fine-tuned model is based on CodeLlama-7b and has been trained on Java code summarization tasks. It performs best with:

- Java code snippets
- Function definitions
- Class declarations
- Code documentation generation

## Performance Considerations

- **Latency**: Typical response time is 1-3 seconds depending on prompt length
- **Throughput**: Can handle approximately 10-20 requests per minute on standard hardware
- **Memory**: Requires approximately 14GB of GPU memory for optimal performance

