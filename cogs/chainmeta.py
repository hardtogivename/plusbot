from discord.ext import commands
from discord.ext.commands import Context
from discord import Interaction
from discord import app_commands
import discord
from helpers import chainmetacaller
intents = discord.Intents.default()
bot = commands.Bot(
    command_prefix='$',
    intents=intents,
    help_command=None, #todo add help command
)
class ChainMeta(commands.Cog, name="chainmeta"):
    def __init__(self, bot):
        self.bot = bot

    
    @bot.tree.command(name="chainmeta")
    #description="Scans the blockchain for metadata",
    async def chainmeta(self, ctx: Interaction, network : str, address: str):
        #from discord.ext.commands import Context as ctx
        ret = chainmetacaller.searchMeta(network, address)
        if ret == "[]":
            embed = discord.Embed(
            title="Error",
            color=0xE02B2B,
            )
            embed.add_field(name="Empty address", value="Maybe you added a wrong address or network? The current supported networks are ethereum_mainnet and bitcoin.", inline=True)
            await ctx.response.send_message(embed=embed, ephemeral=True)
            return None
        

        embed = discord.Embed(
            title="Contract MetaData",
            color=0xE02B2B,
        )
        labels = chainmetacaller.LabelParser.parse_labels(ret)
        '''
        self.chain = chain
        self.address = address
        self.entity = entity
        self.name = name
        self.categories = categories
        self.source = source
        self.submitted_by = submitted_by
        self.submitted_on = submitted_on
        '''

        for l in labels:
            # add each field of an object object
            embed.add_field(name="Entity", value=l.entity, inline=True)
            embed.add_field(name="Name", value=l.name, inline=True)
            embed.add_field(name="Categories", value=l.categories, inline=True)
            embed.add_field(name="Source", value=l.source, inline=True)
            embed.add_field(name="Submitted By", value=l.submitted_by, inline=True)
            embed.add_field(name="Submitted On", value=l.submitted_on, inline=True)
            embed.add_field(name=" ", value=" ", inline=False)
        await ctx.response.send_message(embed=embed, ephemeral=True)
async def setup(bot):
    await bot.add_cog(ChainMeta(bot))
