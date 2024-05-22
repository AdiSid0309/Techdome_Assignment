# ToDo App
Dployed on PYTHONANYWHERE and here is the working link for the same - http://adisid.pythonanywhere.com/login
A simple web application built with Flask that allows users to manage their tasks. The app includes user authentication and 
role-based access control, where admins can create, delete, and mark tasks as completed, while regular users can only view and mark tasks as completed.

## Features

- User registration and authentication
- Admin and user roles
- Create new tasks (admins only)
- Mark tasks as completed
- Delete tasks (admins only)
- View all tasks

## Prerequisites

- Python 3.x
- Flask
- SQLite3

## Installation

1. Clone the repository:


```
git clone https://github.com/AdiSid0309/todo-app.git
```

2. Navigate to the project directory:

```
cd todo-app
```

3. Create a virtual environment (optional but recommended):

```
python3 -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```

4. Install the required dependencies:

```
pip install -r requirements.txt
```

## Usage

1. Run the Flask application:

```
python app.py
```

2. Open your web browser and navigate to `http://localhost:5000`.
3. Register a new user or log in with an existing account.
4. If you have an admin account, you can create new tasks, mark tasks as completed, and delete tasks.
5. If you have a regular user account, you can view tasks and mark them as completed.


## Working

User Page
![user](https://github.com/AdiSid0309/Techdome_Assignment/assets/50744962/e97a3e0d-ab5c-4d6f-81c6-d724e80a89d8)

Register PAge
![register](https://github.com/AdiSid0309/Techdome_Assignment/assets/50744962/8d8bcd79-a52d-4b8b-b80c-0c9790634eb5)

Login Page
![login](https://github.com/AdiSid0309/Techdome_Assignment/assets/50744962/8a21be48-db09-4551-8563-76c734a840e4)

Admin Page
![admin](https://github.com/AdiSid0309/Techdome_Assignment/assets/50744962/5e9eecec-e4b9-4afc-968e-8e8bb6490e05)

