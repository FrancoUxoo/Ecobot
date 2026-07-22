import random
from discord.ext import commands

datos = [
    "🌳 Un árbol puede absorber alrededor de 22 kg de CO₂ al año.",
    "💧 Cerrar la llave mientras te cepillas los dientes puede ahorrar mucha agua.",
    "♻️ Reciclar una lata de aluminio ahorra hasta un 95% de energía.",
    "🌍 Cada pequeña acción cuenta para cuidar el planeta.",
    "🚲 Caminar o usar bicicleta reduce la contaminación."
]

retos = [
    "Usa una botella reutilizable hoy.",
    "Recoge tres papeles del suelo.",
    "Apaga las luces cuando salgas de una habitación.",
    "Evita usar bolsas plásticas durante un día.",
    "Separa la basura reciclable."
]

class MedioAmbiente(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dato(self, ctx):
        await ctx.send(random.choice(datos))

    @commands.command()
    async def reto(self, ctx):
        await ctx.send(
            "🌱 **Reto ecológico del día:**\n\n"
            + random.choice(retos)
        )

async def setup(bot):
    await bot.add_cog(MedioAmbiente(bot))
