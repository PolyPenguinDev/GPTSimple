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
after a generation that doesn't use streaming, you will get a response object
```python
response.text #output text from the AI
response.json #exact output from the API
response.message #output text in the {'role':'assistant', 'content':'...'} format
response.output_tokens #amount of tokens in the output
#there are more but i can't find a use for them
```
If you use streaming, you will get a streamingResponse generator which, when iterated, will return a token object
```python
for token in response: #will be the number of tokens in the response and a extra token to show that it is over
      token.text #content of the token (will be None if the generation is over)
      token.model #will return the model you are using
      token.response #pure response from the API
      token.message #content of the token in the {'role':'assistant', 'content':'...'} format (will be {'role':'assistant', 'content':'None'} if the generation is over)
      ai.print_token(token) #will print the token in a way where you can see it write as it generates
```
There are a few varibles that might be useful to edit or see
```python
chat.model #change the model (great for compairing)
chat.base_url #only really used along side changing chat.model
chat.api_key
chat.history #set or view the chat history in OpenAI format
```
