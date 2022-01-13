import random
import os
from discord.ext import commands

bot = commands.Bot(command_prefix ='!')

@bot.command(name="guess", help="Play a round of an over under guessing game!")
async def guess(ctx):
    number = random.randint(1, 100)
    counter = 0
    await ctx.send("Enter an integer from 1 to 100: or press q to quit")

    def check(msg):
        return msg.author == ctx.author

    while True:

        msg = await bot.wait_for("message", check=check)

        if msg.content == 'q':
            await ctx.send("You have quit the game")
            break
        elif int(msg.content) == number:
            await ctx.send(f"Your guess was correct! You got it in {counter} guesses!")
            break
        elif int(msg.content) > 101 or int(msg.content) < 0 or isinstance(msg.content, int) == True:
            await ctx.send("You made an invalid guess. Please enter an integer between 1 to 100")
        elif int(msg.content) < number:
            counter+=1
            await ctx.send(f"Your guess is low, you made {counter} guesses")
        elif int(msg.content) > number:
            counter+=1
            await ctx.send(f"Your guess is high, you made {counter} guesses")

with open("Bot_token.txt", "r") as token_file:
    TOKEN = token_file.read()
    bot.run(TOKEN)