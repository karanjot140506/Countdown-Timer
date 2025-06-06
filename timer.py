import time

def timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")  # Overwrites the line each second
        time.sleep(1)
        seconds -= 1
    print("!!!! Time's up !!!!")

def main():
    print("Countdown Timer")
    try:
        totalseconds = int(input("Enter time in seconds: "))
        timer(totalseconds)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
    
    
    
# def chatbot():
#     print("Hello! I'm ChatPy 🤖. Type 'bye' to end the chat.")
    
#     while True:
#         user_input = input("You: ").lower()

#         if user_input in ["hi", "hello", "hey"]:
#             print("ChatPy: Hello there! 👋")
#         elif "how are you" in user_input:
#             print("ChatPy: I'm just code, but I'm doing great! 😄")
#         elif "your name" in user_input:
#             print("ChatPy: I'm ChatPy, your Python chatbot.")
#         elif "bye" in user_input:
#             print("ChatPy: Goodbye! 👋 Have a great day.")
#             break
#         elif "help" in user_input:
#             print("ChatPy: You can ask me simple things like 'hello', 'how are you', or say 'bye' to exit.")
#         else:
#             print("ChatPy: I'm not sure how to respond to that. Try asking something else.")

# if __name__ == "__main__":
#     chatbot()
