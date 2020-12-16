# discord bot concept - 01
# title - greetings

greetings = {}

username = "yashsehgal"

def discordBot():
  while True:
    message = input("> ")
    
    if "-greeter" in message:
      if "hello" in message:
        botReply("hey there")
    
      if "how are you" in message:
        botReply("I am fine, Trust you are good too.")
    
      if "what is your name" in message:
        botReply("I am Greeter, A bot program written in Python. Good to see you there @{}".format(username))
        
      if "disconnect" in message:
        botReply("Nice time spent here in this server, trust we will meet again soon")
        break

def botReply(message):
  print("greeter>>> {}".format(message))

if __name__ == "__main__":
  discordBot()