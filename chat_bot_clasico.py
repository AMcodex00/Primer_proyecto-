# chatbot_basico.py

def chatbot():
    print("Hola, soy tu primer chatbot. Escribe 'salir' para terminar.")
    while True:
        user_input = input("Tú: ")
        if user_input.lower() == "salir":
            print("Chatbot: ¡Adiós!")
            break
        elif "hola" in user_input.lower():
            print("Chatbot: ¡Hola! ¿Cómo estás?")
        elif "bien" in user_input.lower():
            print("Chatbot: Me alegra escuchar eso.")
        else:
            print("Chatbot: No entiendo, pero sigo aprendiendo.")

if __name__ == "__main__":
    chatbot()
