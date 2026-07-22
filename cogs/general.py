from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hola(self, ctx):
        await ctx.send(f"¡Hola {ctx.author.mention}! Soy Ecobot.👋")

    @commands.command()
    async def ayuda(self,ctx):
        mensaje = """
🌱 **Comandos disponibles**

$hola
$dato
$reto
$reciclar
$quiz
$puntos
"""

        await ctx.send(mensaje)

async def setup(bot):
    await bot.add_cog(General(bot))
