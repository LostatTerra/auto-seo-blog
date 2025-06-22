import openai
from datetime import datetime
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

# Create the content using the new v1.0+ API format
client = openai.OpenAI()

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a professional SEO blog writer."},
        {"role": "user", "content": "Write an engaging blog post on a trending topic that drives traffic."}
    ],
    max_tokens=800
)

post_content = response.choices[0].message.content

# Save to a markdown file
today = datetime.today().strftime('%Y-%m-%d')
filename = f"posts/{today}-some-topic.md"
os.makedirs("posts", exist_ok=True)

with open(filename, "w") as f:
    f.write(post_content)

print(f"✅ Blog post saved to {filename}")
