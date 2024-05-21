from openai import OpenAI
import time

asst_id = "asst_z6YJHscX2lXzhm5vQNDjJJa5"
client = OpenAI(api_key="sk-proj-pA3BSdMbPaiyEsE11IKrT3BlbkFJB6uCq3oWNJ00Z3V8qKZL")

thread = client.beta.threads.create()
message = client.beta.threads.messages.create(
  thread_id=thread.id,
  role="user",
  content="What is the average aboveground biomass in the dataset?"
)
run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id=asst_id,
)
print(f"Run ID: {run.id}, Status: {run.status}")
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
                    print(content_block.text.value)
else:
  print(run.status)