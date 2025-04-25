import os
import google.generativeai as genai
from flask import Flask, request, jsonify, render_template
import sys
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()

app = Flask(__name__)

# 從環境變數獲取配置
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL")

# 配置 Gemini
try:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel(GEMINI_MODEL)
except Exception as e:
    print(f"Error configuring Gemini: {str(e)}")
    sys.exit(1)

def get_ai_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        if not data or 'message' not in data:
            return jsonify({'error': 'No message provided'}), 400
        
        user_input = data['message']
        if not user_input.strip():
            return jsonify({'error': 'Message cannot be empty'}), 400
            
        response = get_ai_response(user_input)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def cli_interface():
    print("Welcome to the AI Chat CLI! Type 'exit' to quit.")
    print("Type 'help' for available commands.")
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break
            elif user_input.lower() == 'help':
                print("\nAvailable commands:")
                print("- exit: Quit the program")
                print("- help: Show this help message")
                print("- clear: Clear the screen")
                continue
            elif user_input.lower() == 'clear':
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
                
            if not user_input:
                print("Please enter a message.")
                continue
                
            response = get_ai_response(user_input)
            print(f"\nAI: {response}\n")
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--cli':
        cli_interface()
    else:
        app.run(debug=True) 