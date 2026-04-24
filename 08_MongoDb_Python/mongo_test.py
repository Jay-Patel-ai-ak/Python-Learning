from pymongo import MongoClient
uri = "mongodb://127.0.0.1:27017/"
client = MongoClient(uri)

db = client.todo_db
task_collection = db.tasks

# Insert function to add new task to DB
def create_task(description):
    task = {"description": description}
    result = task_collection.insert_one(task)
    print(f"Task created with ID: {result.inserted_id}")
    
# Read the tasks from the DB
def view_tasks():
    tasks = task_collection.find()
    for docs in tasks:
        print(f"{docs['_id']}: {docs['description']}")

# Its repetative task, so its need to keep going
while True:
    print ("\n1. Create Task")
    print ("2. View Tasks")
    print ("3. Update Task")
    print ("4. Delete Task")
    print ("5. Exit")
    
# Take user input for the choice
    choice = input("Enter your choice: ")
    
    if choice == '1':
        description = input("Enter your task: ")
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        print()
    elif choice == '4':
        print()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")