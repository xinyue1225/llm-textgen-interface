import os

import requests


API_URL = os.getenv("HF_ENDPOINT_URL")


def query(payload: dict) -> list:
    """Send a generation request to the configured inference endpoint."""

    if not API_URL:
        raise ValueError(
            "HF_ENDPOINT_URL is not configured. "
            "Set the environment variable before running this script."
        )

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    response = requests.post(
        API_URL,
        headers=headers,
        json=payload,
        timeout=60,
    )

    response.raise_for_status()

    result = response.json()

    if not isinstance(result, list) or not result:
        raise ValueError("Unexpected response format from inference endpoint.")

    return result


def extract_generated_text(result: list, prompt: str) -> str:
    """Extract newly generated text from the endpoint response."""

    generated_text = result[0].get("generated_text")

    if not generated_text:
        raise ValueError("No generated text returned by inference endpoint.")

    if generated_text.startswith(prompt):
        generated_text = generated_text[len(prompt):]

    return generated_text.strip()


def main() -> None:
    first_user_message = "Hello!"

    prompt_round1 = (
        "<|im_start|>user\n"
        f"{first_user_message}"
        "<|im_end|>\n"
        "<|im_start|>assistant\n"
    )

    result_round1 = query(
        {
            "inputs": prompt_round1,
            "parameters": {
                "max_new_tokens": 50,
            },
        }
    )

    assistant_response_1 = extract_generated_text(
        result_round1,
        prompt_round1,
    )

    second_user_message = "What is your name?"

    prompt_round2 = (
        f"{prompt_round1}"
        f"{assistant_response_1}<|im_end|>\n"
        "<|im_start|>user\n"
        f"{second_user_message}"
        "<|im_end|>\n"
        "<|im_start|>assistant\n"
    )

    result_round2 = query(
        {
            "inputs": prompt_round2,
            "parameters": {
                "max_new_tokens": 50,
            },
        }
    )

    assistant_response_2 = extract_generated_text(
        result_round2,
        prompt_round2,
    )

    print("----- Conversation Log -----")
    print(f"User (round 1): {first_user_message}")
    print(f"Assistant (round 1): {assistant_response_1}")
    print(f"User (round 2): {second_user_message}")
    print(f"Assistant (round 2): {assistant_response_2}")


if __name__ == "__main__":
    main()
