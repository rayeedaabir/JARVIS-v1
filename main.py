from modules.voiceinput import get_voice_input
from modules.textinput import get_text_input
from modules.nlp import process_command
from modules.response import respond

def main():
    print("Welcome to JARVIS!")
    while True:
        # Get input (voice or text)
        user_input = get_voice_input() or get_text_input()
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        # Process command and respond
        response = process_command(user_input)
        respond(response)

if __name__ == "__main__":
    main()
