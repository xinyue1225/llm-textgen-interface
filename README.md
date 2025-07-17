# LLM Text Generation Interface

This project implements a modular and extensible interface for text generation using large language models (LLMs), built with [Gradio](https://www.gradio.app/) and [HuggingFace Transformers](https://huggingface.co/docs/transformers/). The interface supports both **local generation** using GPT-2 and **remote generation** via an API endpoint.

## Features

### 1. Final Local App (`final_app.py`)
- Interactive Gradio interface for text generation with:
  - Prompt input (manual or dropdown)
  - Sliders to control temperature, max length, and top-p
- Supports local model (`gpt2`, can be swapped)
- Demonstrates prompt selection + parameter tuning + UI customization

### 2. Remote API Chatbot (`chatbot.py`)
- Chat-style interface powered by a remote LLM via REST API
- Multi-turn conversation using formatted prompts
- Integrated with `utils.format_as_chat()` for proper context formatting

### 3. Prompting Logic + Multi-Turn API Test (`call_api.py`)
- Script that sends multi-turn prompts to a Hugging Face Inference Endpoint
- Shows how to manage context and prompt structure programmatically

### 4. Prompt Formatter Utility (`utils.py`)
- Generates correctly formatted chat-style prompts for instruct-tuned LLMs
- Easy to reuse for both API and chat interface

## Skills Demonstrated

- Gradio UI development
- HuggingFace Transformers
- RESTful API interaction (`requests`)
- Prompt engineering for conversational models
- Modular code organization (CLI, utils, separation of concerns)

## Requirements

```bash
pip install gradio transformers requests

## Sample Chat Interface

### Chatbot with Multi-Turn API Responses
![Chatbot Screenshot](https://github.com/user-attachments/assets/c5526666-3250-434a-87e0-06c67da65cc2)
![Dropdown Prompt Screenshot](https://github.com/user-attachments/assets/1f3135a7-a703-44ed-828d-f35951a2471c)





