# django_todo_app
A simple and efficient Django-based task management application.

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Contributors](https://img.shields.io/badge/contributors-3-orange)

This application allows users to add, update, and delete tasks. It’s styled for an elegant user experience and includes user authentication for personalized task management.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

  ## Features
- Add, update, and delete tasks
- User authentication and account management
- Responsive design with CSS styling
- REST API integration (if applicable)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Cynthia-Macharia/django_todo_app.git

2. Navigate to the project directory:
   ```bash
   cd django_todo_app
3. Build the Docker container (if using Docker):
     ```bash
   docker-compose up --build
4. Alternatively, set up a virtual environment and install dependencies:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     pip install -r requirements.txt
5. Run migrations:
    ```bash
    python manage.py migrate
6. Start the development server:
   ```bash
   python manage.py runserver

## Usage

1. **Start the Application**
   - If running locally:
     Open a terminal, navigate to the project directory, and run:
     ```bash
     python manage.py runserver
     ```
     The app will be available at `http://127.0.0.1:8000/`.

   - If running in a Docker container:
     The app is mapped to port 80 on your host machine. Open a browser and navigate to:
     ```
     http://<your-ec2-instance-public-ip>/
     ```

2. **Using the Todo App**
   - **Add a Task**: Enter the task details in the input field and click "Add Task."
   - **Mark a Task as Completed**: Click on the checkbox next to the task name.
   - **Update a Task**: Click the "Edit" button, modify the task details, and save.
   - **Delete a Task**: Click the "Delete" button to remove a task.

3. **Expected Outcomes**
   - Successfully added tasks appear in the task list.
   - Completed tasks are visually marked.
   - Updated tasks reflect the new details.
   - Deleted tasks are removed from the list.

4. **Troubleshooting**
   - If the app is not accessible, check the logs for errors using:
     ```bash
     docker logs <container_name>
     ```
   - Ensure the required ports are open in your EC2 instance's security group.

---



      
   

   
   


