#chat.py
from pprint import pprint
pprint("Welcome to the Simple Chat Agent!")
pprint("Type 'exit' to quit the program.")

from graph.graph import app
while True:
    user_input = input("\nUser: ")
    
    if user_input.lower() == "exit":
        break
    
    inputs = {"question": user_input}
    for output in app.stream(inputs):
        for key, value in output.items():
            pprint(f"Finished running: {key}:")
    pprint(value["generation"])
    print("\n", end="", flush=True)

pprint("\nThank you for using the Simple Chat Agent!")
