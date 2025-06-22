import datetime
import random

# List of blog titles (expand this later or make it dynamic)
topics = [
    "5 Simple Habits for Better Sleep",
    "Top 10 AI Tools You Should Try in 2025",
    "How to Start a Side Hustle with No Money",
    "The Truth About SEO in 2025",
    "Affiliate Marketing Basics for Beginners"
]

# Sample affiliate link
affiliate_link = "https://example.com/product?ref=ivanblog"
cta = f"\n\n[🔥 Check out this tool here!]({affiliate_link})"

# Choose a topic at random
title = random.choice(topics)
slug = title.lower().replace(" ", "-").replace("?", "")
date = datetime.datetime.now().strftime("%Y-%m-%d")

# Post content
body = f"""# {title}

Welcome to today’s post on **{title}**! Let’s dive into how this can help you level up your life.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. This is your moment to act — because opportunity waits for no one.

## Why it matters

- Point 1: Simplified
- Point 2: Practical
- Point 3: Profitable

### Final Thoughts

SEO is about consistency. Tools like this can help you **automate your growth**.

{cta}
"""

# Output path
filename = f"posts/{date}-{slug}.md"
with open(filename, "w") as f:
    f.write(body)

print(f"✅ Blog post created: {filename}")
