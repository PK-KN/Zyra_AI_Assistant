from config import model

chat = model.start_chat(history=[])


def ask_ai(user_input):
    try:
        response = chat.send_message(user_input)
        return response.text
    except Exception:
        return "⚠️ Error: Something went wrong."
