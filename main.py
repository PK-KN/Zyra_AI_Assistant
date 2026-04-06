from ai_brain import ask_ai


def run_zyra():
    print("""
====================================
        🤖 ZYRA AI (SECURE)
====================================
Type 'exit' to quit
====================================
""")

    while True:
        user_input = input("🧑 You: ").strip()

        if user_input.lower() == "exit":
            print("👋 Zyra: Bye!")
            break

        response = ask_ai(user_input)
        print(f"🤖 Zyra: {response}\n")


if __name__ == "__main__":
    run_zyra()
