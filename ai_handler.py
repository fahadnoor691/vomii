from config import OPENAI_API_KEY
from prompts import SYSTEM_PROMPT, REFINEMENT_PROMPT, REFINEMENT_SYSTEM_PROMPT
from tools import FUNCTIONS, FUNCTIONS_MAP
from speech_handler import SpeechHandler

import openai
import json

class AIHandler:
    def __init__(self):
        self.client = openai.OpenAI(api_key=OPENAI_API_KEY)
        self.speech_handler = SpeechHandler()

    def process_query(self, query):
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        messages.append({"role": "user", "content": query})
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            functions=FUNCTIONS,
            function_call="auto",
        )
        choice = response.choices[0]
        if choice.message.function_call:
            self.speech_handler.speak("Hold on a second...")
            function_call = choice.message.function_call
            result = self.execute_function(function_call)
            refined_response = self.refine_response(query, result)
            return refined_response
        return choice.message.content

    def execute_function(self, function_call):
        try:
            function_name = function_call.name
            function_args = json.loads(function_call.arguments)
            
            print("Executing function: ", function_name)
            print("Function arguments: ", function_args)
            
            if function_name not in FUNCTIONS_MAP:
                raise ValueError(f"Function '{function_name}' not found in FUNCTIONS_MAP")
            
            function = FUNCTIONS_MAP[function_name]
            result = function(**function_args)
            print("Function result: ", result)
            return result
            
        except json.JSONDecodeError as e:
            print(f"Error parsing function arguments: {e}")
            return f"Error: Invalid JSON in function arguments"
        except KeyError as e:
            print(f"Error: Missing required argument {e}")
            return f"Error: Missing required argument {e}"
        except Exception as e:
            print(f"Error executing function {function_name}: {e}")
            return f"Error: {str(e)}"

    def refine_response(self, user_query, response):
        refinement_prompt = REFINEMENT_PROMPT.format(user_query=user_query, response=response)
        messages = [
            {"role": "system", "content": REFINEMENT_SYSTEM_PROMPT},
            {"role": "user", "content": refinement_prompt}
        ]
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=1000
        )
        return response.choices[0].message.content
