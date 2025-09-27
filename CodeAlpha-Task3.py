import sys

def get_bot_response(user_input):
    """
    Determines the chatbot's response based on the user's input.
    """
    # Convert input to lowercase and remove leading/trailing whitespace 
    # for simpler and more robust matching.
    text = user_input.lower().strip()
    
    # 1. Check for a greeting
    if "hello" in text or "hi" in text:
        return "Hi there! How can I help you today?"
    
    # 2. Check for a status inquiry
    elif "how are you" in text or "how are u" in text:
        return "I'm doing great, thanks for asking! What about you?"
    
    # 3. Check for a farewell
    elif "bye" in text or "goodbye" in text or "exit" in text:
        # This response is used to break the loop outside the function
        return "Goodbye!" 
    
    # 4. Default response if no rule is matched
    else:
        return "I'm sorry, I don't quite understand that. Can you rephrase?"

def start_chatbot():
    """
    Main function to run the interactive chatbot loop.
    """
    print("🤖 Basic Chatbot Initialized.")
    print("Type 'bye' or 'exit' to end the conversation.")
    print("-" * 35)

    # 1. Use a loop to keep the conversation going
    while True:
        try:
            # 2. Input/Output: Get user input
            user_input = input("You: ")
            
            # Use the function to get the bot's response
            bot_response = get_bot_response(user_input)
            
            # Print the bot's response
            print(f"Bot: {bot_response}")
            
            # 3. Check if the conversation should end (part of the loop logic)
            if bot_response == "Goodbye!":
                break # Exit the while loop
                
        except EOFError:
            print("\nBot: Session ended by user input.")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            break

# Run the chatbot
if __name__ == "__main__":
    start_chatbot()