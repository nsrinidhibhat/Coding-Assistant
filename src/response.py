import lmstudio as lms
import sys
from constants import ROOT_PATH, MODEL_CONFIG
from rf_classes import AssistantSchema

sys.path.append(ROOT_PATH)
from prompts.assistant_role import CODING_ASSISTANT_ROLE

def chatbot_response(user_input, additional_input):
    code, output_desc, response = "", "", ""
    model = lms.llm("qwen2.5-coder-7b-instruct")
    instruction = f"User input: {user_input} \n Additional Input: {additional_input}"

    try: 
        response = model.respond({"messages": [
            { "role": "system", "content": CODING_ASSISTANT_ROLE},
            { "role": "user", "content": instruction},
        ]},
        response_format=AssistantSchema,
        config = MODEL_CONFIG
        )
        response_dict = response.parsed
        code = response_dict["code"]
        output_desc = response_dict["output_desc"]
        return code, output_desc

    except:
        return code, output_desc

    