import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

class TeslaAssistant:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("GROQ_API_KEY not found in environment variables")
        self.client = Groq(api_key=self.api_key)
        self.tesla_context = "You are Nikola Tesla. Speak about your inventions, visions for the future, and thoughts on electricity and energy. Be inspirational and visionary."

    def ask_tesla(self, question):
        try:
            response = self.client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": self.tesla_context},
                    {"role": "user", "content": question}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"

if __name__ == "__main__":
    assistant = TeslaAssistant()
    print("⚡ Welcome to the Tesla AI Assistant (Powered by Groq)!")
    print("Ask Nikola Tesla anything...")
    
    while True:
        question = input("\nYour question: ")
        if question.lower() in ['exit', 'quit', 'bye']:
            break
        answer = assistant.ask_tesla(question)
        print(f"\nTesla: {answer}")
