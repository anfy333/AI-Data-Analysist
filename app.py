from flask import Flask, render_template, request
from openai import OpenAI
import time
import re

app = Flask(__name__)
asst_id = "asst_z6YJHscX2lXzhm5vQNDjJJa5"
client = OpenAI(api_key="sk-proj-pA3BSdMbPaiyEsE11IKrT3BlbkFJB6uCq3oWNJ00Z3V8qKZL")

@app.route("/", methods=["GET", "POST"])
def hello_world():
    response = None
    if request.method == "POST":
        prompt = request.form["prompt"]
        response = model(prompt)
    return render_template("index.html", response=response)


def model(prompt):
    thread = client.beta.threads.create()
    message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content=prompt
    )
    run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=asst_id,
    )
    while run.status != "completed":
        time.sleep(1)
        run = client.beta.threads.runs.retrieve(run.id, thread_id=thread.id)
        print(f"Run Status: {run.status}")

    if run.status == 'completed': 
        messages = client.beta.threads.messages.list(
            thread_id=thread.id
        )
        for msg in messages.data:
                if msg.role == 'assistant':
                    for content_block in msg.content:
                        if content_block.type == 'text':
                            code = extract_code(content_block.text.value)
                            return (content_block.text.value)
    else:
        return (run.status)

def extract_code(text):
    # Regular expression to extract code within ```python ... ```
    code_match = re.search(r'```python\s+([\s\S]*?)\s+```', text)
    if code_match:
        exec(code_match.group(1))
        
if __name__ == "__main__":
    app.run(debug=True)