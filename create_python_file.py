import os

def create_python_file():
    file_name = input("Geben Sie den Namen der neuen Python-Datei ein: ")
    if not file_name.endswith(".py"):
        file_name += ".py"
    
    with open(file_name, 'w') as file:
        file.write("# imports\n")
    
    print(f"Datei '{file_name}' wurde erstellt.")

if __name__ == "__main__":
    create_python_file()