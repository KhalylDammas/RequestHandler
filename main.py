# We will need 2 packages
# 1. JSON package to read and write JSON files.
import json
# 2. Path from pathlib package to handle files and paths.
from pathlib import Path

# Create the request handler class
class RequestHandler():
    def __init__(self): # define the constructor
        # Set the data directory path
        self.data_dir = Path(__file__).parent / "data"
        self.data_dir.mkdir(exist_ok=True) # Check if the data direory exists. If it does not make it

        self.data_file = self.data_dir / "data.json"

        if not self.data_file.exists():
            self._create_data_file()

    def add_request(self, title, description):
        # This method adds new requests
        with open(self.data_file, mode='r') as f: # Read the data file
            data = json.load(f) # Load the entire data and store it in `data` variable
        data.append( # Add on top of the previously loaded data, the new request details
            {
                "id": len(data) + 1, # Request ID will be the length of the list (# of the requests), then add 1.
                "title": title, # The request title
                "desc": description, # The request description
                "status": "New" # The request status (will always be "New")
            }
        )

        with open(self.data_file, mode='w') as f: # Open the data file in wrte mode
            json.dump(data, f, indent=2) # Dump (Store) the data in the file with 2 indentation (just to prettify it).
        print("New request added!\n")

    def view_request(self):
        with open(self.data_file, mode='r') as f:
            data = json.load(f)
            if len(data) == 0:
                print("No requests found!")
                print('-'*10)
                print()
                return
            self._pretty_print(data)

    def _pretty_print(self, data):
        for request in data:
            print(f"Request #{request['id']}")
            print(f"Title: {request['title']}")
            print(f"Description: {request['desc']}")
            print(f"Status: {request['status']}\n")
        print('-'*10)

    def _create_data_file(self):
        # This tool will create a json file
        with open(self.data_file, mode='w') as f: 
            json.dump([], f) # Enter a JSON object on a json file (If the file does not exit create it)

def _print_menu():
    print("1. Create Request")
    print("2. View Requests")
    print("3. Exit")

def main():
    handler = RequestHandler()
    program_title = "Request Management System"
    print(program_title)
    print("-"*len(program_title))
    print() # new line

    while True:
        _print_menu()
        choice = input("Choose an option: ")
        print() # print a new line
        if choice == "1":
            title = input("Enter request title: ")
            desc = input("Enter request description: ")
            handler.add_request(title, desc)
        elif choice == "2":
            handler.view_request()
        elif choice == "3":
            return
        else:
            print("Invalid Value\nTry Again")

if __name__ == "__main__":
    main()