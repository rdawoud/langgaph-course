#chat.py
# chat.py
from pprint import pprint

pprint("Welcome to the Knowledge chat Agent!")
pprint("Type 'exit' to quit the program.")

from graph.graph import app

chat_history = []

while True:
    user_input = input("\nUser: ")
    
    if user_input.lower() == "exit":
        break
    inputs = {"question": user_input, "chat_history": chat_history}
    for output in app.stream(inputs):
        for key, value in output.items():
            pprint(f"Finished running: {key}:")
    pprint(value["generation"])
    chat_history.append({"role": "user", "content": user_input})
    chat_history.append({"role": "assistant", "content": value["generation"]})
    print("\n", end="", flush=True)

pprint("Thank you for using the Knowledge Chat Agent!")
