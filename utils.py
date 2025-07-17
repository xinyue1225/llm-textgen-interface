from typing import List


def format_as_chat(message: str, history: List[List[str]]) -> str:
    """
    Given a message and a history of previous messages, returns a string that formats the conversation as a chat.
    Uses the format expected by SmolLM2-135M-Instruct.

    :param message: A string containing the user's most recent message
    :param history: A list of lists of previous messages, where each sublist is a conversation turn:
        [[user_message1, assistant_reply1], [user_message2, assistant_reply2], ...]
    :return: A formatted string representing the entire conversation, ending with the assistant prompt
    """
    # Start with an empty string to accumulate the formatted conversation.
    formatted = ""
    # Loop over each conversation turn in the history.
    for turn in history:
        user_message, assistant_reply = turn
        formatted += "<|im_start|>user\n" + user_message + "<|im_end|>\n"
        formatted += "<|im_start|>assistant\n" + assistant_reply + "<|im_end|>\n"
    
    # Append the most recent user message.
    formatted += "<|im_start|>user\n" + message + "<|im_end|>\n"
    return formatted


