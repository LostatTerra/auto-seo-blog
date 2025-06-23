import openai
from datetime import datetime
import os

# Replace keywords in blog with affiliate links
def inject_affiliate_links(text):
    for keyword, link in AFFILIATE_LINKS.items():
        if keyword in text:
            text = text.replace(keyword, link, 1)  # Replace first occurrence only
    return text

# Define affiliate keywords and links
AFFILIATE_LINKS = {
    "laptop": "[laptop](https://www.amazon.com/dp/B09XYZ1234?tag=yourtag-20)",
    "headphones": "[headphones](https://www.amazon.com/dp/B07XYZ4567?tag=yourtag-20)",
    "web hosting": "[web hosting](https://www.bluehost.com/track/yourtag)",
    "camera": "[camera](https://www.amazon.com/dp/B08XYZ8910?tag=yourtag-20)",
    "supplements": "[supplements](https://www.amazon.com/dp/B07ABC1234?tag=yourtag-20)",
    "ergonomic chair": "[ergonomic chair](https://www.amazon.com/dp/B07DEF5678?tag=yourtag-20)",
    "gaming monitor": "[gaming monitor](https://www.amazon.com/dp/B09GHI9012?tag=yourtag-20)",
    "coffee maker": "[coffee maker](https://www.amazon.com/dp/B07JKL3456?tag=yourtag-20)",
    "smartwatch": "[smartwatch](https://www.amazon.com/dp/B08MNO7890?tag=yourtag-20)"
}

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
post_content = inject_affiliate_links(post_content)

# Save to a markdown file
today = datetime.today().strftime('%Y-%m-%d')
filename = f"posts/{today}-some-topic.md"
os.makedirs("posts", exist_ok=True)

with open(filename, "w") as f:
    f.write(post_content)

print(f"✅ Blog post saved to {filename}")
