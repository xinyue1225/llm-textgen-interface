import gradio as gr
import requests
from utils import format_as_chat

API_URL = "https://ymgsslsjnx4ncugs.us-east-1.aws.endpoints.huggingface.cloud"
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
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


