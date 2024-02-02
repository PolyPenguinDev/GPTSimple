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
`ai.conversation` has many inputs, this is an example of them
```python
#base_url
ai.conversation(base_url="openai")
ai.conversation(base_url="deepinfra")
ai.conversation(base_url="https://api.openai.com/v1/chat/completions")

#api_key (optinal for deepinfra, required for openai)
ai.conversation(api_key="<OpenAI api key>")

#model
ai.conversation(model="gpt-4")
ai.conversation(base_url="deepinfra", model="deepinfra/airoboros-70b")

#system_prompt
ai.conversation(system_prompt="you will taunt the user and make them sad")

#history (overrides system_prompt)
ai.conversation(history=[{"role":"user", "content":"hi"},{"role":"assistant", "content":"i hate you"},{"role":"user", "content":"RUDE!"}])
```
after you define the conversation, there are two methods to it 
```python
#ask
chat.ask("what is your name?") #ask a question and add it to history and get the output
chat.ask("what is your name?", stream=True) #get output as it's generating
chat.ask("what is your name?", invisible=True) #get output without adding it to the history
chat.ask("what is your name?", stream=True, invisible=True)

#generate
chat.generate() #generate the output just from the history, without a question
chat.generate(stream=True) #get output as it's generating
chat.generate(invisible=True) #get output without adding it to the history
chat.generate(stream=True, invisible=True)
```


