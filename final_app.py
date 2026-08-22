import gradio as gr
from transformers import pipeline


# Load the model once when the application starts.
text_generator = pipeline(
    "text-generation",
    model="gpt2",
)


PREWRITTEN_PROMPTS = [
    "None",
    "Explain machine learning using an everyday example.",
    "Write a short story about an unexpected journey.",
    "Suggest three ways to build a productive study routine.",
]


def generate_text(
    prewritten_prompt: str,
    custom_prompt: str,
    temperature: float,
    max_new_tokens: int,
    top_p: float,
) -> str:
    """Generate text from either a predefined or custom prompt."""

    prompt = (
        prewritten_prompt
        if prewritten_prompt and prewritten_prompt != "None"
        else custom_prompt
    )

    if not prompt or not prompt.strip():
        return "Please select a pre-written prompt or enter your own prompt."

    generation_kwargs = {
        "max_new_tokens": int(max_new_tokens),
        "pad_token_id": text_generator.tokenizer.eos_token_id,
    }

    # Temperature 0 uses greedy decoding.
    if temperature == 0:
        generation_kwargs["do_sample"] = False
    else:
        generation_kwargs.update(
            {
                "do_sample": True,
                "temperature": float(temperature),
                "top_p": float(top_p),
            }
        )

    output = text_generator(prompt.strip(), **generation_kwargs)

    return output[0]["generated_text"]


def main() -> None:
    interface = gr.Interface(
        fn=generate_text,
        inputs=[
            gr.Dropdown(
                choices=PREWRITTEN_PROMPTS,
                value="None",
                label="Pre-Written Prompt",
                info=(
                    "Select a sample prompt or choose 'None' "
                    "to enter a custom prompt."
                ),
            ),
            gr.Textbox(
                label="Custom Prompt",
                placeholder="Enter your prompt here...",
                lines=5,
            ),
            gr.Slider(
                minimum=0.0,
                maximum=2.0,
                value=1.0,
                step=0.1,
                label="Temperature",
            ),
            gr.Slider(
                minimum=1,
                maximum=256,
                value=50,
                step=1,
                label="Max New Tokens",
            ),
            gr.Slider(
                minimum=0.0,
                maximum=1.0,
                value=1.0,
                step=0.05,
                label="Top-p",
            ),
        ],
        outputs=gr.Textbox(label="Generated Text"),
        title="LLM Text Generation Interface",
        description=(
            "Generate text locally with GPT-2 using Hugging Face Transformers. "
            "Choose a sample prompt or enter your own, then adjust decoding "
            "parameters to explore different generation behaviors."
        ),
    )

    interface.launch()


if __name__ == "__main__":
    main()
