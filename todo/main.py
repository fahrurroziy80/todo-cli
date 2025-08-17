import click

@click.command()
@click.option("--task", prompt="Task", help="Task to add to todo list")
def run(task):
    click.echo(f"✅ Task ditambahkan: {task}")
