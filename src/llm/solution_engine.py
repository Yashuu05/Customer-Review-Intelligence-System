from ollama import chat
import os 
import sys 
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
import json

def stream_ollama(customer_data, llm="llama3.1:8b", system_instruction="You are a helpful assistant"):
    
    prompt = f"""Analyse the given customer data provided to you and provide professional business solution.
    Customer Data: {customer_data}"""
    
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
    
    try:
        # load system prompt
        print("loading system prompt...")
        with open(file=os.path.join(project_root, "configs","system_prompt.md"), mode="+r") as f:
            sys_prompt = f.read()

        # load customer data
        print("loading customer data...")
        with open(file="dummy_data.json", mode="+r") as file:
            data = json.load(file)

        # stream llm response
        print("LLM thinking...")
        stream_ollama(
            customer_data=data,
            system_instruction=sys_prompt
        )

    except Exception as e:
        print(f"Error: {e}")