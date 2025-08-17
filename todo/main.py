import click
import os

TODO_FILE = "todos.txt"

def load_todos():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_todos(todos):
    with open(TODO_FILE, "w") as f:
        f.write("\n".join(todos))

@click.group()
def cli():
    """Simple TODO CLI App"""
    pass

@cli.command()
@click.argument("task")
def add(task):
    """Add a new task"""
    todos = load_todos()
    todos.append(task)
    save_todos(todos)
    click.echo(f"✅ Task ditambahkan: {task}")

@cli.command()
def list():
    """List all tasks"""
    todos = load_todos()
    if not todos:
        click.echo("📭 Tidak ada task.")
    else:
        click.echo("📌 Daftar Task:")
        for i, task in enumerate(todos, 1):
            click.echo(f"{i}. {task}")

@cli.command()
@click.argument("index", type=int)
def remove(index):
    """Remove a task by its number"""
    todos = load_todos()
    if 0 < index <= len(todos):
        removed = todos.pop(index - 1)
        save_todos(todos)
        click.echo(f"❌ Task dihapus: {removed}")
    else:
        click.echo("⚠️ Index tidak valid.")
