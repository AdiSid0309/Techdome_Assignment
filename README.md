```markdown
# ToDo App

A simple web application built with Flask that allows users to manage their tasks. The app includes user authentication and role-based access control, where admins can create, delete, and mark tasks as completed, while regular users can only view and mark tasks as completed.

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

```bash
git clone https://github.com/your-username/todo-app.git
```

2. Navigate to the project directory:

```bash
cd todo-app
```

3. Create a virtual environment (optional but recommended):

```bash
python3 -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the Flask application:

```bash
python app.py
```

2. Open your web browser and navigate to `http://localhost:5000`.
3. Register a new user or log in with an existing account.
4. If you have an admin account, you can create new tasks, mark tasks as completed, and delete tasks.
5. If you have a regular user account, you can view tasks and mark them as completed.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
```

This README file provides an overview of the ToDo App, its features, prerequisites, installation instructions, usage guidelines, and information on contributing and licensing. Feel free to modify it according to your needs.