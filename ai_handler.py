from config import OPENAI_API_KEY, OPENAI_SETTINGS
from prompts import SYSTEM_PROMPT, REFINEMENT_PROMPT, REFINEMENT_SYSTEM_PROMPT
from tools import TOOLS, TOOLS_MAP
from speech_handler import SpeechHandler
from conversation_handler import ConversationHandler

import openai
import json


class AIHandler:
    def __init__(self):
        self.client = openai.OpenAI(api_key=OPENAI_API_KEY)
        self.speech_handler = SpeechHandler()
        self.conversation_handler = ConversationHandler()
        
        self.model = OPENAI_SETTINGS['model']
        self.temperature = OPENAI_SETTINGS['temperature']

    def process_query(self, query):
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        conversation_history = self.conversation_handler.get_conversation_history()
        messages.extend(conversation_history)
        messages.append({"role": "user", "content": query})
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            tools=TOOLS,
            tool_choice="auto",
            temperature=self.temperature
        )
        
        self.conversation_handler.add_message(query, "user")
        
        choice = response.choices[0]
        
        if choice.message.tool_calls:
            self.speech_handler.speak("Hold on a second...")
            tool_call = choice.message.tool_calls[0]
            result = self.execute_tool(tool_call)
            refined_response = self.refine_response(query, result)
            final_response = refined_response
        else:
            final_response = choice.message.content
        
        self.conversation_handler.add_message(final_response, "assistant")
        return final_response

    def execute_tool(self, tool_call):
        try:
            if not tool_call.type == "function":
                return "Sorry, only functions are supported at the moment"
            
            function_name = tool_call.function.name
            function_args = json.loads(tool_call.function.arguments)
            
            print("Executing function: ", function_name)
            print("Function arguments: ", function_args)
            
            if function_name not in TOOLS_MAP:
                raise ValueError(f"Function '{function_name}' not found in TOOLS_MAP")
            
            function = TOOLS_MAP[function_name]
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
            model=self.model,
            messages=messages,
            max_tokens=1000
        )
        
        return response.choices[0].message.content