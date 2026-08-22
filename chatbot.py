import gradio as gr
import requests
from utils import format_as_chat

API_URL = "https://ymgsslsjnx4ncugs.us-east-1.aws.endpoints.huggingface.cloud"
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"import os

import gradio as gr
import requests

from utils import format_as_chat


API_URL = os.getenv("HF_ENDPOINT_URL")


def query_api(prompt: str) -> str:
    """Send a formatted prompt to the configured inference endpoint."""

    if not API_URL:
        raise ValueError(
            "HF_ENDPOINT_URL is not configured. "
            "Set the environment variable before starting the application."
        )

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    response = requests.post(
        API_URL,
        headers=headers,
        json={
            "inputs": prompt,
            "parameters": {
                "max_new_tokens": 100,
            },
        },
        timeout=60,
    )

    response.raise_for_status()

    result = response.json()

    if not isinstance(result, list) or not result:
        raise ValueError("Unexpected response format from inference endpoint.")

    generated_text = result[0].get("generated_text")

    if not generated_text:
        raise ValueError("No generated text returned by inference endpoint.")

    return generated_text


def respond(message: str, chat_history: list) -> str:
    """Generate a response using the current conversation history."""

    prompt = format_as_chat(
        message,
        [[user_message, assistant_message]
         for user_message, assistant_message in chat_history],
    )

    full_response = query_api(prompt)

    # The endpoint may return the complete formatted prompt together
    # with the newly generated assistant response.
    if "<|im_end|>" in full_response:
        return full_response.split("<|im_end|>")[-1].strip()

    return full_response.strip()


def on_submit(message: str, chat_history: list):
    """Add a user message and generated response to the conversation."""

    if not message.strip():
        return "", chat_history

    try:
        response = respond(message, chat_history)
    except (requests.RequestException, ValueError) as error:
        response = f"Error: {error}"

    chat_history.append((message, response))

    return "", chat_history


def remove_last_turn(chat_history: list):
    """Remove the most recent conversation turn."""

    if not chat_history:
        return []

    return chat_history[:-1]


with gr.Blocks() as demo:
    gr.Markdown(
        """
        # Remote LLM Chat Interface

        A lightweight multi-turn chat interface using a configured
        Hugging Face inference endpoint.
        """
    )

    chatbot = gr.Chatbot()

    with gr.Row():
        undo = gr.Button("↩️ Undo")
        clear = gr.Button("🗑️ Clear")

    with gr.Row():
        user_input = gr.Textbox(
            placeholder="Type a message...",
            label="Your Message",
            interactive=True,
        )
        submit = gr.Button("Submit", variant="primary")

    gr.Examples(
        [
            "Explain machine learning in simple terms.",
            "Recommend a science fiction book.",
            "Write a short story about space exploration.",
        ],
        inputs=user_input,
    )

    submit.click(
        on_submit,
        inputs=[user_input, chatbot],
        outputs=[user_input, chatbot],
    )

    user_input.submit(
        on_submit,
        inputs=[user_input, chatbot],
        outputs=[user_input, chatbot],
    )

    undo.click(
        remove_last_turn,
        inputs=chatbot,
        outputs=chatbot,
    )

    clear.click(
        lambda: [],
        outputs=chatbot,
    )


if __name__ == "__main__":
    demo.launch()
}

def query_api(prompt):
    response = requests.post(API_URL, headers=headers, json={
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 100
        }
    })
    response_json = response.json()
    return response_json[0]["generated_text"]

def respond(message, chat_history):
    # Convert chat history to (role, text) list
    messages = []
    for user_msg, assistant_msg in chat_history:
        messages.append(("user", user_msg))
        messages.append(("assistant", assistant_msg))
    messages.append(("user", message))

    prompt = format_as_chat(message, [[u, a] for u, a in chat_history])
    full_response = query_api(prompt)

    # Extract only the assistant's new reply without showing prompt structure
    assistant_reply = full_response.split("<|im_end|>")[-1].strip()
    return assistant_reply

with gr.Blocks() as demo:
    gr.Markdown("# SmolLM2 360M Instruct")
    chatbot = gr.Chatbot()
    
    with gr.Row():
        retry = gr.Button("🔄 Retry")
        undo = gr.Button("↩️ Undo")
        clear = gr.Button("🗑️ Clear")
    
    with gr.Row():
        user_input = gr.Textbox(placeholder="Type a message...", label="Your Message", interactive=True)
        submit = gr.Button("Submit", variant="primary")
    
    examples = gr.Examples(["Tell me a joke", "What's the weather like?", "Recommend a book"], inputs=[user_input])
    
    def on_submit(message, chat_history):
        response = respond(message, chat_history)
        chat_history.append((message, response))
        return "", chat_history
    
    submit.click(on_submit, inputs=[user_input, chatbot], outputs=[user_input, chatbot])
    retry.click(lambda chat_history: chat_history[:-1], inputs=[chatbot], outputs=[chatbot])
    undo.click(lambda chat_history: chat_history[:-1], inputs=[chatbot], outputs=[chatbot])
    clear.click(lambda: [], outputs=[chatbot])

demo.launch()


