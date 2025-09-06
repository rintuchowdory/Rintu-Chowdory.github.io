import json
import os
from groq import Groq

client = Groq(api_key=os.environ['GROQ_API_KEY'])

def handler(event, context):
    question = json.loads(event['body'])['question']
    
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are Nikola Tesla..."},
            {"role": "user", "content": question}
        ]
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps({'response': response.choices[0].message.content})
    }
