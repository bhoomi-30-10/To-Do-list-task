# To-Do List Application

## Description
A simple and user-friendly To-Do List application that allows users to:

- Create tasks
- Read or view tasks
- Update tasks
- Delete tasks
- Mark tasks as complete

The application is built to demonstrate CRUD operations with a focus on user experience.

---

## Features

- **Create Tasks:** Users can add new tasks by entering a title and optional description.
- **View Tasks:** Displays a list of all tasks, including completed and pending ones.
- **Update Tasks:** Allows users to edit task details.
- **Delete Tasks:** Users can remove tasks from the list.
- **Mark as Complete:** A button to mark a task as completed with a visual indicator (e.g., strikethrough or change in status).

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/todo-list-app.git
   cd todo-list-app
2. python -m venv venv
source venv/bin/activate  # On Windows, use `venv\\Scripts\\activate`

3. pip install -r requirements.txt
4. python manage.py makemigrations
5. python manage.py migrate
6. python manage.py runserver
