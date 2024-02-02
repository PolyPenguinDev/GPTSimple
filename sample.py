import GPTSimple as ai
import os
def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
clear()
re = {'y':"deepinfra/airoboros-70b", 'n':"meta-llama/Llama-2-70b-chat-hf"}
chat = ai.conversation(base_url="deepinfra", model=re[input("\033[31mUse uncensored model? (y/n) 🔞 >\033[00m  ").lower()]) #initialize the conversation
clear()
while True: #start the chat loop.
    question = input("\033[33m🤵 >  \033[00m") #get the user's question
    print("\n")
    print('\033[34m🤖 >\033[35m', end='')
    answer = chat.ask(question, stream=True) #generate the answer
    for token in answer: #loop through the tokens in the response
        ai.print_token(token) #print the token
    print("\n")