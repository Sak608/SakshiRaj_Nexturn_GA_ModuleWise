<<<<<<< HEAD
document.addEventListener('DOMContentLoaded', () => {
    const taskInput = document.getElementById('new-task');
    const addTaskButton = document.getElementById('add-task');
    const taskList = document.getElementById('task-list');
    const pendingTasks = document.getElementById('pending-tasks');

    let tasks = JSON.parse(localStorage.getItem('tasks')) || [];

    const updatePendingTasks = () => {
        const pendingCount = tasks.filter(task => !task.completed).length;
        pendingTasks.textContent = `Pending Tasks: ${pendingCount}`;
    };

    const saveTasksToLocalStorage = () => {
        localStorage.setItem('tasks', JSON.stringify(tasks));
    };

    const renderTasks = () => {
        taskList.innerHTML = '';
        tasks.forEach((task, index) => {
            const taskItem = document.createElement('li');
            taskItem.className = `task-item ${task.completed ? 'completed' : ''}`;
            taskItem.innerHTML = `
                <span>${task.name}</span>
                <div>
                    <button onclick = "toggleTask(${index})">${task.completed ? 'Undo' : 'Done'}</button>
                    <button onClick = "deleteTask(${index})">Delete</button>
                </div>    
            `;
            taskList.appendChild(taskItem);
        });
        updatePendingTasks();
    };

    window.toggleTask = (index) => {
        tasks[index].completed = !tasks[index].completed;
        saveTasksToLocalStorage();
        renderTasks();
    };

    window.deleteTask = (index) => {
        tasks.splice(index, 1);
        saveTasksToLocalStorage();
        renderTasks();
    };

    addTaskButton.addEventListener('click', () => {
        const taskName = taskInput.value.trim();
        if (taskName) {
            tasks.push({ name: taskName, completed: false});
            taskInput.value = '';
            saveTasksToLocalStorage();
            renderTasks();
        }
    });

    renderTasks();
=======
document.addEventListener('DOMContentLoaded', () => {
    const taskInput = document.getElementById('new-task');
    const addTaskButton = document.getElementById('add-task');
    const taskList = document.getElementById('task-list');
    const pendingTasks = document.getElementById('pending-tasks');

    let tasks = JSON.parse(localStorage.getItem('tasks')) || [];

    const updatePendingTasks = () => {
        const pendingCount = tasks.filter(task => !task.completed).length;
        pendingTasks.textContent = `Pending Tasks: ${pendingCount}`;
    };

    const saveTasksToLocalStorage = () => {
        localStorage.setItem('tasks', JSON.stringify(tasks));
    };

    const renderTasks = () => {
        taskList.innerHTML = '';
        tasks.forEach((task, index) => {
            const taskItem = document.createElement('li');
            taskItem.className = `task-item ${task.completed ? 'completed' : ''}`;
            taskItem.innerHTML = `
                <span>${task.name}</span>
                <div>
                    <button onclick = "toggleTask(${index})">${task.completed ? 'Undo' : 'Done'}</button>
                    <button onClick = "deleteTask(${index})">Delete</button>
                </div>    
            `;
            taskList.appendChild(taskItem);
        });
        updatePendingTasks();
    };

    window.toggleTask = (index) => {
        tasks[index].completed = !tasks[index].completed;
        saveTasksToLocalStorage();
        renderTasks();
    };

    window.deleteTask = (index) => {
        tasks.splice(index, 1);
        saveTasksToLocalStorage();
        renderTasks();
    };

    addTaskButton.addEventListener('click', () => {
        const taskName = taskInput.value.trim();
        if (taskName) {
            tasks.push({ name: taskName, completed: false});
            taskInput.value = '';
            saveTasksToLocalStorage();
            renderTasks();
        }
    });

    renderTasks();
>>>>>>> 57b7dc5ce798bd88ebe3fc187d9051b5072f06d2
});