import json
from pathlib import Path

FILE = Path("history.json")

def save_history(entry):
    history = []
    if FILE.exists():
        history = json.loads(FILE.read_text())
    history.append(entry)
    FILE.write_text(json.dumps(history, indent=2))

def show_history():
    if FILE.exists():
        for h in json.loads(FILE.read_text()):
            print(h)
    else:
        print("No history yet.")

if __name__ == "__main__":
    while True:
        expr = input("Enter calculation (or 'history' / 'quit'): ")
        if expr == "quit":
            break
        elif expr == "history":
            show_history()
        else:
            try:
                result = eval(expr)
                print("Result:", result)
                save_history(f"{expr} = {result}")
            except:
                print("Invalid expression")
