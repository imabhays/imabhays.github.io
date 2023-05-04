import datetime

now = datetime.datetime.now()
date_format = now.strftime("%Y-%m-%d")

title = input("Enter post title: ")
filename = f"_posts/{date_format}-{title}.md"

print(f"Post filename: {filename}")
