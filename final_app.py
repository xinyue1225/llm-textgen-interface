import gradio as gr
from transformers import pipeline

# -------------------------
# 1) Load the text generation pipeline (outside of the interface function)
# -------------------------
text_generator = pipeline(
    "text-generation",
    model="gpt2",
)

def generate_text(prewritten_prompt, custom_prompt, temperature, max_length, top_p):
    """
    Generates text using the chosen prompt (either from a dropdown or user input).
    If temperature=0, we do greedy decoding (do_sample=False).
    """

    # If the user has selected a non-empty prewritten prompt, use it; otherwise, use the custom prompt
    if prewritten_prompt and prewritten_prompt != "None":
        prompt = prewritten_prompt
    else:
        prompt = custom_prompt

    do_sample = (temperature != 0)

    output = text_generator(
        prompt,
        max_length=int(max_length),
        top_p=float(top_p),
        temperature=float(temperature),
        do_sample=do_sample,
    )

    # output is a list of dicts like [{"generated_text": "..."}]
    generated_text = output[0]["generated_text"]
    return generated_text

def main():
    # 2) Define the new feature: a dropdown of pre-written prompts
    prewritten_prompt_dropdown = gr.Dropdown(
        label="Choose a Pre-Written Prompt",
        choices=["None", "Tell me how to deal with relationship.", "Write a short story about BL.", "Explain machine learning using life examples."],
        value="None",  # Default selection
        info="Select one of the prewritten prompts from the dropdown or leave it at 'None' to type your own prompt below."
    )

    # 3) Existing prompt textbox for custom prompts
    custom_prompt_input = gr.Textbox(
        label="Or Type Your Own Prompt",
        placeholder="Type your custom prompt here...",
        lines=5
    )

    temperature_slider = gr.Slider(
        minimum=0.0,
        maximum=2.0,
        value=1.0,
        step=0.1,
        label="Temperature"
    )

    max_length_slider = gr.Slider(
        minimum=1,
        maximum=256,
        value=16,
        step=1,
        label="Max Length"
    )

    top_p_slider = gr.Slider(
        minimum=0.0,
        maximum=1.0,
        value=1.0,
        step=0.1,
        label="Top-p"
    )

    output_text = gr.Textbox(
        label="Generated Text"
    )

    # 4) Add an info text (description) about the new feature
    description_text = (
        "A Gradio interface that uses a local GPT-2 model to generate text. "
        "You can select a prewritten prompt or type your own custom prompt. "
        "Experiment with Temperature and Top-p for deterministic vs. varied outputs."
    )

    interface = gr.Interface(
        fn=generate_text,
        inputs=[
            prewritten_prompt_dropdown,
            custom_prompt_input,
            temperature_slider,
            max_length_slider,
            top_p_slider
        ],
        outputs=output_text,
        title="Final Text Generation App with Custom Feature",
        description=description_text,
    )

    interface.launch()

if __name__ == "__main__":
    main()
