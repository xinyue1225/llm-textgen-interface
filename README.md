# LLM Text Generation Interface

A lightweight interface for experimenting with local and API-based language model inference.

The project demonstrates practical workflows for running language models through Hugging Face Transformers and remote inference APIs, with simple Gradio interfaces for interactive text generation.

## Features

- Local text generation with Hugging Face Transformers
- Remote LLM inference through REST APIs
- Gradio-based interactive interfaces
- Multi-turn prompt formatting
- Configurable decoding parameters
- Modular separation of interface, API, and utility functions

## Project Context

This project was developed as a course project to explore practical LLM inference, prompt formatting, and interface design using local and remote language models.

The focus is on building a lightweight inference workflow rather than model training or fine-tuning.

## Local Text Generation

The local interface uses Hugging Face Transformers to load a language model and generate text directly.

A lightweight GPT-2 model is used as the default example so that the application can be tested without requiring large computational resources.

Typical generation parameters include:

- maximum generation length
- temperature
- top-k sampling
- top-p sampling

These parameters can be adjusted through the interface to explore different decoding behaviors.

## API-Based Generation

The project also supports sending prompts to a remote language model through a REST API.

The API workflow is separated from the user interface so that different inference endpoints can be integrated without changing the overall application structure.

For endpoints requiring authentication, credentials should be configured through environment variables rather than stored directly in the repository.

Example:

```bash
HF_API_TOKEN=your_token
HF_ENDPOINT_URL=your_endpoint
```

## Multi-Turn Interaction

The chatbot interface maintains conversation history and formats previous user and model messages into the prompt used for subsequent generation.

This provides a simple demonstration of how a stateless language-model inference endpoint can be used to support multi-turn interaction.

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

### Main Files

- `final_app.py` — Gradio interface for local text generation
- `chatbot.py` — interface for multi-turn chatbot interaction
- `call_api.py` — utilities for remote API-based inference
- `utils.py` — shared helper functions
- `requirements.txt` — Python dependencies

## Requirements

Install the required dependencies with:

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

## Quick Start

### Local Text Generation

Run the local text-generation interface:

```bash
python final_app.py
```

The Gradio application will start locally and provide an interactive interface for entering prompts and adjusting generation parameters.

### Chatbot Interface

Run the chatbot interface:

```bash
python chatbot.py
```

## Remote Inference Configuration

If using a remote inference endpoint, configure the required environment variables before running the application.

Linux/macOS:

```bash
export HF_API_TOKEN="your_token"
export HF_ENDPOINT_URL="your_endpoint"
```

Windows PowerShell:

```powershell
$env:HF_API_TOKEN="your_token"
$env:HF_ENDPOINT_URL="your_endpoint"
```

API credentials and private endpoint information should not be committed to the repository.

## Skills Demonstrated

- Hugging Face Transformers inference
- Gradio interface development
- REST API integration
- Multi-turn prompt formatting
- Decoding parameter control
- Environment-based API configuration
- Modular Python code organization

## Limitations

- The local demo uses GPT-2 as a lightweight example model.
- Output quality therefore reflects the capabilities of the selected model rather than a modern instruction-tuned LLM.
- Remote generation requires a separately configured inference endpoint.
- Conversation history is handled through prompt construction rather than persistent memory.
- The project focuses on inference and interface workflows rather than model training or fine-tuning.

## Possible Extensions

Potential extensions include:

- support for additional Hugging Face models
- streaming generation
- improved conversation-history management
- configurable model selection
- additional inference providers
- deployment as a hosted web application

