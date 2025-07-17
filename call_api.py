import requests

API_URL = "https://ymgsslsjnx4ncugs.us-east-1.aws.endpoints.huggingface.cloud"
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def main():
    # 1) In the first conversation
    # user: Hello!
    prompt_round1 = "<|im_start|>user\nHello!<|im_end|>\n<|im_start|>assistant\n"
    data_round1 = {
        "inputs": prompt_round1,
        "parameters": {
            "max_new_tokens": 50
        }
    }

    result_round1 = query(data_round1)
    assistant_response_1 = result_round1[0]["generated_text"].replace(prompt_round1, "")

    # 2) In the second conversation, merge the previous assistant response with the user’s message.
    # for example, user replies: "What is your name?"
    user_reply_2 = "What is your name?"
    prompt_round2 = (
        f"{prompt_round1}{assistant_response_1}<|im_end|>\n"
        f"<|im_start|>user\n{user_reply_2}<|im_end|>\n"
        f"<|im_start|>assistant\n"
    )
    data_round2 = {
        "inputs": prompt_round2,
        "parameters": {
            "max_new_tokens": 50
        }
    }

    result_round2 = query(data_round2)
    assistant_response_2 = result_round2[0]["generated_text"].replace(prompt_round2, "")

    # 3) print conversation log
    print("----- Conversation Log -----")
    print("User (round 1): Hello!")
    print("Assistant (round 1):", assistant_response_1)
    print("User (round 2):", user_reply_2)
    print("Assistant (round 2):", assistant_response_2)

if __name__ == "__main__":
    main()
