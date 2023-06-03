from discord.ext import commands
from discord.ext.commands import Context
import discord
from helpers import checks
from helpers import chainmetacaller
class ChainMeta(commands.Cog, name="chainmeta"):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(
        name="chainmeta",
        description="This command will return the chain meta data for the supported networks.",
    )
    async def chainmeta(self, ctx: Context, network : str, address: str):
        #from discord.ext.commands import Context as ctx
        ret = chainmetacaller.searchMeta(network, address)
        if ret == "[]":
            embed = discord.Embed(
            title="Error",
            color=0xE02B2B,
            )
            embed.add_field(name="Empty address", value="Maybe you added a wrong address or network? The current supported networks are ethereum_mainnet and bitcoin.", inline=True)
            await ctx.send(embed=embed)
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
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(ChainMeta(bot))
