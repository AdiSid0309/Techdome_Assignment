function addTask() {
    const inputBox = document.getElementById('input-box');
    const taskContent = inputBox.value;

    fetch('/add_task', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ content: taskContent })
    })
    .then(response => response.json())
    .then(tasks => updateTaskList(tasks));

    inputBox.value = '';
}

function completeTask(id) {
    fetch('/complete_task', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ id: id })
    })
    .then(response => {
        if (response.status === 403) {
            alert('Permission denied');
            return;
        }
        return response.json();
    })
    .then(tasks => updateTaskList(tasks));
}


function deleteTask(id) {
    fetch('/delete_task', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ id: id })
    })
    .then(response => response.json())
    .then(tasks => updateTaskList(tasks));
}

function updateTaskList(tasks) {
    const listContainer = document.getElementById('list-container');
    const role = document.body.getAttribute('data-role'); // Assuming you set the role as a data attribute on the body
    listContainer.innerHTML = '';

    tasks.forEach(task => {
        const listItem = document.createElement('li');
        listItem.className = 'list-group-item d-flex justify-content-between align-items-center';
        listItem.textContent = task.content;

        const buttonGroup = document.createElement('div');
        buttonGroup.className = 'btn-group';

        const completeButton = document.createElement('button');
        completeButton.className = 'btn btn-sm btn-success';
        completeButton.textContent = task.completed ? 'Mark Uncompleted' : 'Mark Completed';
        completeButton.onclick = () => completeTask(task.id);
        buttonGroup.appendChild(completeButton);

        if (role === 'admin') {
            const deleteButton = document.createElement('button');
            deleteButton.className = 'btn btn-sm btn-danger';
            deleteButton.textContent = 'Delete';
            deleteButton.onclick = () => deleteTask(task.id);
            buttonGroup.appendChild(deleteButton);
        }

        listItem.appendChild(buttonGroup);
        listContainer.appendChild(listItem);
    });

    updateCounters(tasks);
}

function updateCounters(tasks) {
    const completedCounter = document.getElementById('completed-counter');
    const uncompletedCounter = document.getElementById('uncompleted-counter');

    const completedTasks = tasks.filter(task => task.completed).length;
    const uncompletedTasks = tasks.length - completedTasks;

    completedCounter.textContent = completedTasks;
    uncompletedCounter.textContent = uncompletedTasks;
}

// Load tasks when the page loads
window.onload = () => {
    fetch('/tasks')
    .then(response => response.json())
    .then(tasks => updateTaskList(tasks));
};
