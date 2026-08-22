def format_as_chat(message: str, history: list[list[str]]) -> str:
    """Format conversation history using a ChatML-style prompt."""

    formatted_messages = []

    for user_message, assistant_reply in history:
        formatted_messages.append(
            f"<|im_start|>user\n{user_message}<|im_end|>"
        )
        formatted_messages.append(
            f"<|im_start|>assistant\n{assistant_reply}<|im_end|>"
        )

    formatted_messages.append(
        f"<|im_start|>user\n{message}<|im_end|>"
    )
    formatted_messages.append(
        "<|im_start|>assistant\n"
    )

    return "\n".join(formatted_messages)
    
