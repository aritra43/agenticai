import openai

# Set your API key
openai.api_key = "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"

# List available models (new API method)
response = openai.ChatCompletion.list()

# Print the available models
for model in response['data']:
    print(model['id'])