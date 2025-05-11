# Discord Task Manager Bot

A Discord bot that helps small teams manage their to-do lists. The bot allows users to add, delete, complete, and view tasks through simple Discord commands.

## Features

- Add new tasks with descriptions
- Delete existing tasks
- Mark tasks as complete
- View all tasks with their status
- Persistent storage using SQLite database

## Installation

1. Clone this repository:

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your Discord bot token:
```
DISCORD_TOKEN=your_discord_bot_token_here
```

## Usage

1. Start the bot:
```bash
python bot.py
```

2. Available Commands:
- `!add_task <description>` - Add a new task
- `!delete_task <task_id>` - Delete a task
- `!complete_task <task_id>` - Mark a task as complete
- `!show_tasks` - Display all tasks

## Testing

Run the test suite using pytest:
```bash
pytest
```

## Project Structure

```
DiscordTaskManager/
├── bot.py              # Main bot logic and command handlers
├── database.py         # Database operations
├── run_tests.py        # Test runner
├── .env                # Environment variables
├── .gitignore          # Git ignore file
├── LICENSE             # License file
├── requirements.txt    # Project dependencies
├── tests/             # Test files
│   ├── test_add_task.py
│   ├── test_delete_task.py
│   ├── test_show_tasks.py
│   └── test_complete_task.py
└── README.md          # This file
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 