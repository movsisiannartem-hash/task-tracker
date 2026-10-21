# 📝 Task Tracker

A simple command-line task management application built with **Python** and **JSON**.

Task Tracker allows users to create, update, delete, and track tasks directly from the terminal. All tasks are stored locally in a JSON file.

## ✨ Features

- ➕ Add new tasks
- 📋 Display all tasks
- 🔍 Filter tasks by status
- ✏️ Update task descriptions
- 🗑️ Delete tasks
- 🔄 Mark tasks as in progress
- ✅ Mark tasks as completed
- 💾 Store tasks in a JSON file
- 🕒 Track task creation and update timestamps

## 🛠️ Technologies

- **Python** — application logic
- **JSON** — local data storage
- **Pathlib** — file system operations
- **Datetime** — timestamps
- **Argparse alternative: `sys.argv`** — command-line argument handling

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/task-tracker.git
```

### 2. Navigate to the project directory

```bash
cd task-tracker
```

### 3. Run the application

Python 3.10 or newer is recommended.

```bash
python main.py
```

No external dependencies are required.

## 📖 Usage

### Add a task

```bash
python main.py add "Learn Python"
```

### List all tasks

```bash
python main.py list
```

### Filter tasks by status

Display tasks that have not been started:

```bash
python main.py list todo
```

Display tasks currently in progress:

```bash
python main.py list in-progress
```

Display completed tasks:

```bash
python main.py list done
```

### Update a task

```bash
python main.py update 1 "Learn Python functions"
```

### Delete a task

```bash
python main.py delete 1
```

### Mark a task as in progress

```bash
python main.py mark-in-progress 1
```

### Mark a task as completed

```bash
python main.py mark-done 1
```

## 📊 Task Statuses

| Status | Description |
|---|---|
| `todo` | Task has not been started |
| `in-progress` | Task is currently in progress |
| `done` | Task has been completed |

## 📂 Project Structure

```text
task-tracker/
│
├── main.py       # Main application and CLI commands
├── tasks.json    # Local task storage (created automatically)
├── README.md     # Project documentation
└── .gitignore    # Files excluded from Git
```

## 💾 Data Storage

Tasks are stored in `tasks.json` as a JSON array.

Each task contains the following fields:

```json
{
    "id": 1,
    "description": "Learn Python",
    "status": "todo",
    "createdAt": "2026-10-21T12:00:00",
    "updatedAt": "2026-10-21T12:00:00"
}
```

- `id` — unique task identifier
- `description` — task description
- `status` — current task status
- `createdAt` — task creation date and time
- `updatedAt` — last modification date and time

## 🔮 Future Improvements

- [ ] Add task priorities
- [ ] Add due dates
- [ ] Improve error handling
- [ ] Add search functionality
- [ ] Add sorting by creation date
- [ ] Add automated tests
- [ ] Improve command-line interface using `argparse`

## 👨‍💻 Author

**YOUR NAME**

- GitHub: [@YOUR-USERNAME](https://github.com/YOUR-USERNAME)

---

*Built with Python as a portfolio project.*