# GPTSimple
GPTSimple is an easier version of the OpenAI python library with more capabilities
### Intallation
To get GPTSimple added to your project, download the GPTSimple.py and add it to the directory your project is in.
### Usage
```python
import GPTSimple as ai
chat = ai.conversation(base_url="deepinfra") #initialize the conversation
while True: #start the chat loop.
      question = input("> ")
      answer = chat.ask(question)
      print("\n")
      print(answer)
      print("\n")
```
