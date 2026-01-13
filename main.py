
def add():
    title = input('Enter task title: ')
    
    with open('to_do_list.txt', 'a', encoding='utf-8') as f:

        f.write(title+'\n')
        
    
    print("✅ Task added successfully!")


def view():
    with open('to_do_list.txt', 'r', encoding='utf-8') as f:

        tasks=(f.readlines())

    print('\n Your Tasks: ')    
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task.strip()}")    
def update():
    update = int(input('Enter Task Number to Update: '))
    new_title = input('Enter new task title: ')
    with open('to_do_list.txt', 'r', encoding='utf-8') as f:

        tasks = f.readlines()
    view()    
    tasks[update - 1] = new_title + '\n'
    with open('to_do_list.txt', 'w', encoding='utf-8') as f:

        f.writelines(tasks)
    print(" Task updated successfully!")

def mark_completed():
    complete = int(input("Enter Task number to mark as completed: "))
    with open('to_do_list.txt', 'r', encoding='utf-8') as f:

        tasks = f.readlines()
    view()
    tasks[complete - 1] = tasks[complete - 1].strip() + " ✅\n"
    with open('to_do_list.txt', 'w', encoding='utf-8') as f:

        f.writelines(tasks)
    print("✅ Task marked as completed!")

def delete():
    delete = int(input("Enter Task number to delete: "))
    with open('to_do_list.txt', 'r', encoding='utf-8') as f:

        tasks = f.readlines()
    view()
    tasks.pop(delete - 1)
    with open('to_do_list.txt', 'w', encoding='utf-8') as f:

        f.writelines(tasks)
    print("✅ Task deleted successfully!")


print("----- TO DO LIST APPLICATION -----\n")

print('''1. Add a task
2. View tasks
3. Update a task
4. Delete a task
5. Mark task as completed      
6. To Exit\n''')
while True:
    try:
        user_input = int(input('Enter your choice number: '))
    except ValueError:
        print('\nEnter only the choice number!\n')
        continue    
    if user_input ==1:
        add()
    elif user_input ==2:   
        view()
    elif user_input ==3: 
        update()
    elif user_input ==4: 
        delete()
    elif user_input ==5:
        mark_completed()      

    elif user_input == 6:
        print('''👋 Thank you for using To-Do List App!
Tasks saved successfully.''')
        break
