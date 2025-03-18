from pydantic import BaseModel

# A class based schema for the coding assistant output
class AssistantSchema(BaseModel):
    code: str
    output_desc: str