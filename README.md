

# Simple Python Coder Chatbot

A chatbot that generates, modifies, and explains Python code using `qwen2.5-coder-7b-instruct`. Built with `Gradio` for an easy-to-use UI.

## Features

- **Code Generation**: Generate Python code based on user prompts.
- **Code Modification**: Provide additional instructions to modify existing code.
- **Code Explanation**: Understand what a given Python script does.

## Installation

### Prerequisites

- Python 3.8+
- `lmstudio` for running LLM models locally
- `gradio` for the UI

### Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

Run the chatbot UI with:

```bash
python gradio_interface.py
```

## How It Works

1. Enter a Python-related query or existing code in the **Input/Code** field.
2. (Optional) Provide additional instructions in the **Additional Input** field.
3. Click **Submit** to get generated code and an explanation.

## Tech Stack

- **Gradio**: Provides a simple UI.
- **qwen2.5-coder-7b-instruct**: LLM used for code generation.
- **lmstudio**: Manages model inference.

## Setting Up LM Studio

1. Install **LM Studio** from the official website.
2. Open **LM Studio** and select the **Power User** option at the bottom to enable developer options.
3. Go to **Discover** on the left panel, select a **code model**, and download it.
4. Navigate to **Developer Options** on the left panel.
5. Click on **Status** or press **Command + R** to start the local server.
6. At the top, select the **coder model** you downloaded. Alternatively, press **Command + L** to open the model selection menu and choose the coder model.
7. Once set up, run the chatbot UI with:

```bash
python gradio_interface.py
```

