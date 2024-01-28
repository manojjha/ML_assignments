import pytchat

chat = pytchat.create(video_id = "JVzyjMkQwrQ")

while chat.is_alive():
    for c in chat.get().sync_items():
        print(f"{c.message}")