import discord
from discord.ext import commands
from database import Database
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

db = Database()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='add_task')
async def add_task(ctx, *, description: str):
    task_id = db.add_task(description)
    await ctx.send(f'✅ Task added with ID: {task_id}')

@bot.command(name='delete_task')
async def delete_task(ctx, task_id: int):
    if db.delete_task(task_id):
        await ctx.send(f'✅ Task {task_id} has been deleted.')
    else:
        await ctx.send(f'❌ Task {task_id} not found.')

@bot.command(name='complete_task')
async def complete_task(ctx, task_id: int):
    if db.complete_task(task_id):
        await ctx.send(f'✅ Task {task_id} has been marked as completed.')
    else:
        await ctx.send(f'❌ Task {task_id} not found.')

@bot.command(name='show_tasks')
async def show_tasks(ctx):
    tasks = db.get_all_tasks()
    if not tasks:
        await ctx.send('No tasks found.')
        return

    embed = discord.Embed(
        title="📋 Task List",
        color=discord.Color.blue()
    )

    for task_id, description, completed in tasks:
        status = "✅" if completed else "⏳"
        embed.add_field(
            name=f"Task {task_id}",
            value=f"{status} {description}",
            inline=False
        )

    await ctx.send(embed=embed)

def main():
    token = os.getenv('DISCORD_TOKEN')
    if not token:
        raise ValueError("No Discord token found. Please set the DISCORD_TOKEN environment variable.")
    
    bot.run(token)

if __name__ == "__main__":
    main() 