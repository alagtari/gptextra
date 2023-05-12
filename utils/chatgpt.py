import openai

def chat_completion(text) :
    openai.api_key = "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"
    completion = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo',
    messages = [
    {'role': 'system', 'content': text}
    ],
    temperature = 0.5
    )

    return completion['choices'][0]['message']['content']

