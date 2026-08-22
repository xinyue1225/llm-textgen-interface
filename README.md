````markdown
# LLM Text Generation Interface

A lightweight Python project for experimenting with local and API-based language model inference.

The repository contains two interactive workflows: a local GPT-2 text generation interface built with Hugging Face Transformers and a multi-turn chatbot that communicates with a configurable remote inference endpoint.

## Features

- Local text generation with Hugging Face Transformers
- Interactive Gradio interfaces
- Configurable decoding parameters
- Pre-written and custom prompts
- Remote LLM inference through a REST API
- Multi-turn conversation history
- ChatML-style prompt formatting
- Environment-based endpoint configuration
- Simple command-line API conversation demo

## Project Context

This project was developed as a course project to explore practical language model inference, prompt formatting, decoding strategies, and user interface design.

The focus is on model inference and interaction workflows rather than model training or fine-tuning.

## Repository Structure

```text
llm-textgen-interface/
├── final_app.py
├── chatbot.py
├── call_api.py
├── utils.py
├── requirements.txt
└── README.md
```

### `final_app.py`

A Gradio interface for local text generation using GPT-2 through the Hugging Face Transformers pipeline.

Users can either select a predefined prompt or enter a custom prompt and control several decoding parameters:

- temperature
- top-p sampling
- maximum number of new tokens

When the temperature is set to `0`, the application switches to greedy decoding.

### `chatbot.py`

A Gradio-based multi-turn chat interface for a remote language model endpoint.

Conversation history is incorporated into each new prompt so that the remote inference API can support multi-turn interaction.

The endpoint URL is loaded from the `HF_ENDPOINT_URL` environment variable rather than being stored directly in the repository.

### `utils.py`

Contains the prompt-formatting utility used by the chatbot.

Conversation turns are converted into a ChatML-style format:

```text
<|im_start|>user
User message
<|im_end|>
<|im_start|>assistant
Assistant response
<|im_end|>
```

The current user message is followed by an assistant prompt so that the model can generate the next response.

### `call_api.py`

A minimal command-line example demonstrating direct REST API interaction with a remote inference endpoint.

The script performs a two-turn conversation and explicitly carries the first assistant response into the second prompt to demonstrate conversation-history construction.

## Requirements

Install the project dependencies with:

```bash
pip install -r requirements.txt
```

The main dependencies are:

```text
gradio
transformers
torch
requests
```

A corresponding `requirements.txt` can contain:

```text
gradio
transformers
torch
requests
```

## Quick Start

### 1. Local GPT-2 Interface

Run:

```bash
python final_app.py
```

The application loads GPT-2 locally and launches a Gradio interface.

You can select one of the sample prompts or enter your own prompt, then adjust the generation parameters before generating text.

## Remote Inference

The remote chatbot and API demo require an inference endpoint.

Set the endpoint URL through the `HF_ENDPOINT_URL` environment variable.

### Linux / macOS

```bash
export HF_ENDPOINT_URL="https://your-endpoint.example.com"
```

### Windows PowerShell

```powershell
$env:HF_ENDPOINT_URL="https://your-endpoint.example.com"
```

Private endpoint information should not be committed directly to the repository.

### 2. Multi-Turn Chat Interface

After configuring the endpoint, run:

```bash
python chatbot.py
```

The Gradio interface supports:

- multi-turn conversation
- conversation-history formatting
- example prompts
- undoing the most recent turn
- clearing the conversation

### 3. API Conversation Demo

To run the minimal two-turn API example:

```bash
python call_api.py
```

The script sends an initial user message to the configured endpoint, retrieves the generated response, and then includes that response in the prompt for the second conversation turn.

## Local Generation

The local interface uses:

```python
pipeline(
    "text-generation",
    model="gpt2",
)
```

GPT-2 is intentionally used as a lightweight demonstration model so that the project focuses on the inference workflow and interface rather than large-model deployment.

Generation behavior can be adjusted through parameters such as temperature and top-p.

## Multi-Turn Prompt Formatting

Remote model APIs are generally stateless unless conversation history is explicitly provided.

This project reconstructs the conversation before each request:

```text
User message 1
    ↓
Assistant response 1
    ↓
User message 2
    ↓
Assistant generation
```

The conversation is converted into a ChatML-style prompt before being sent to the inference endpoint.

This demonstrates a basic approach for implementing conversational behavior on top of a text-generation API.

## Skills Demonstrated

- Hugging Face Transformers inference
- Gradio interface development
- REST API integration with `requests`
- Multi-turn conversation handling
- Chat-style prompt formatting
- Decoding parameter control
- Environment variable configuration
- Basic API error handling
- Modular Python code organization

## Limitations

- GPT-2 is used only as a lightweight local demonstration model and is not instruction-tuned.
- Remote inference requires a separately configured and accessible endpoint.
- The remote API implementation assumes a compatible text-generation response format.
- Conversation history is reconstructed in the prompt rather than stored as persistent model memory.
- The project focuses on inference and interface workflows rather than model training, fine-tuning, or systematic model evaluation.

## Possible Extensions

Potential future improvements include:

- support for additional local language models
- configurable model selection
- token streaming
- improved generation controls
- persistent conversation storage
- support for additional inference providers
- more robust response parsing
- deployment as a hosted web application
````

