# GPTSimple
GPTSimple is an easier version of the OpenAI python library with more capabilities
### Intallation
To get GPTSimple added to your project, download the GPTSimple.py and add it to the directory your project is in.
### Usage
```python
import GPTSimple as ai
chat = ai.conversation(base_url="deepinfra") #initialize the conversation
while True: #start the chat loop.
      question = input("> ") #get the user's question
      answer = chat.ask(question) #generate the answer
      print("\n")
      print(answer.text)
      print("\n")
```
GPTSimple also supports streaming, which lets you get the output before it is done generating
```python
import GPTSimple as ai
chat = ai.conversation(base_url="deepinfra") #initialize the conversation
while True: #start the chat loop.
      question = input("> ") #get the user's question
      print("\n")
      answer = chat.ask(question, stream=True) #generate the answer
      for token in answer: #loop through the tokens in the response
           ai.print_token(token) #print the token
      print("\n")
```
`ai.conversation` has many inputs this is an example of them
```python
#base_url
ai.conversation(base_url="openai")
ai.conversation(base_url="deepinfra")
ai.conversation(base_url="https://api.openai.com/v1/chat/completions")

#api_key (optinal for deepinfra, required for openai)
ai.conversation(api_key="<OpenAI api key>")

#model
ai.conversation(model="gpt-4")
ai.conversation(base_url="deepinfra", model="meta-llama/Llama-2-70b-chat-hf")
```
