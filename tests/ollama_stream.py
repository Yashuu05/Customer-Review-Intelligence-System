from ollama import chat

def stream_ollama(prompt: str, llm="llama3.1:8b", system_instruction="You are a helpful assistant"):
    try:
        stream = chat(
            model=llm,
            messages=[
            {"role": "system", "content": system_instruction},
            {'role': 'user', 'content': prompt}],
            stream=True,
        )

        for chunk in stream:
            print(chunk['message']['content'], end='', flush=True)

    except Exception as e:
        print(f"Error! {e}")

if __name__ == "__main__":
    stream_ollama(prompt="what is machine learning and its types?")
