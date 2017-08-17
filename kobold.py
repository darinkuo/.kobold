import asyncio
import discord
from discord.ext import commands

description = "A discord bot to assist with pen and paper roleplaying games."
command_prefix = "."
extensions = {
    "extensions.basics",
    "extensions.spells"
}
kobold = commands.Bot(description=description,command_prefix=command_prefix)

@kobold.event
async def on_ready():
    """ Called when the client is done preparing data recieved from Discord. """
    print("Logged In.")
    print("Name : {}".format(kobold.user.name))
    print("ID : {}".format(kobold.user.id))
    print("Discord Ver : {}".format(discord.__version__))

    for extension in extensions:
        try:
            kobold.load_extension(extension)
# If an exception is thrown, that exception is bound to the variable e.
        except Exception as e:
            exc= "{}:{}".format(type(e).__name__,e)
            print("Unable to load extension {}\n{}".format(extension,exc))

kobold.run('MzQ1NzA5NzQ1MDc4MDA5ODU2.DG_O3w.w8HFMcHSTG0whozlZBqTP8v2xj0')