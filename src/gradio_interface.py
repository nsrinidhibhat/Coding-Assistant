from response import chatbot_response
import gradio as gr

interface = gr.Interface(
    fn=chatbot_response,
    inputs=[
        gr.Textbox(label="Input/Code"),
        gr.Textbox(label="Additional Input")
    ],
    outputs=[
        gr.Markdown(label="Code"),
        gr.Textbox(label="Output Description")
    ],
    title="Simple Python Coder Chatbot",
    description="""<div style='text-align: center;'>Use the message box to ask a question
    for the LLM to generate Python code, or input existing Python code and use the additional input field
    to request modifications or corrections.</div> 
    <div style='text-align: center;'>You can ask explanations for your code too!</div>
    """,
    article="This chatbot is powered by <i>qwen2.5-coder-7b-instruct</i> LLM designed for code generation and modifications."
)

if __name__ == "__main__":
    interface.launch()
