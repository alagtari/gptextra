import openai

def chat_completion(text) :
    openai.api_key = "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"
    completion = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo',
    messages = [
    {'role': 'user', 'content': text}
    ],
    temperature = 0  
    )

    return completion['choices'][0]['message']['content']

