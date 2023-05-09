import openai

def chat_completion(image,text) :
    openai.api_key = "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"
    completion = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo',
    messages = [
    {'role': 'user', 'content': text+image}
    ],
    temperature = 0  
    )

    print(completion['choices'][0]['message']['content'])
    with open('file.txt','w') as file :
        file.write(completion['choices'][0]['message']['content'])

