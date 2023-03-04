from discord.ext import commands
from discord.ext.commands import Context
import discord
import json
from helpers import checks


# Here we name the cog and create a new class for the cog.
class GoPlus(commands.Cog, name="goplus"):
    def __init__(self, bot):
        self.bot = bot

    # Here you can just add your own commands, you'll always need to provide "self" as first parameter.

    @commands.hybrid_command(
        name="testplus",
        description="This is a testing command that does nothing.",
    )
    # This will only allow non-blacklisted members to execute the command
    @checks.not_blacklisted()
    # This will only allow owners of the bot to execute the command -> config.json
    @checks.is_owner()
    async def testcommand(self, context: Context):
        """
        This is a testing command that does nothing.
        :param context: The application command context.
        """
        # Do your stuff here

        # Don't forget to remove "pass", I added this just because there's no content in the method.
        pass

    @commands.hybrid_command(
        name="cscan",
        description="Scan an address for contracts",
    )
    @checks.not_blacklisted()
    async def contractScan(self, context: Context, network: str, address: str = "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D"
                           ) -> None:
        """
        Kick a user out of the server.
        :param context: The hybrid command context.
        :param network: [1] Ethereum Mainnet
        :param address: .
        """
        import requests
        from helpers import goplusapicaller
        ret = goplusapicaller.getContractScan(network, address)
        pprint = json.dumps(ret, indent=2)

        embed = discord.Embed(
            title="Contract Information Card",
            color=0xE02B2B,
        )

        embed.add_field(name="address", value=address, inline=False)
        embed.add_field(name="holder_count",
                        value=ret[address.lower()]["holder_count"], inline=False)
        
        topHolders = ret[address.lower()]["holders"]
        for index, h in enumerate(topHolders[0:3]):
            holderEmbed = discord.Embed(
                title="Holder Card " + str(index + 1),
                color=0xE02B2B,
            )
            holderEmbed.add_field(
                name="name", value=h["address"], inline=False)
            holderEmbed.add_field(name="tag", value=h["tag"], inline=True)
            holderEmbed.add_field(name="is_contract",
                                  value=h["is_contract"], inline=True)
            holderEmbed.add_field(
                name="balance", value=h["balance"], inline=False)
            holderEmbed.add_field(
                name="percent", value=h["percent"], inline=True)
            await context.send(embed=holderEmbed)
        await context.send(embed=embed)


    @commands.hybrid_command(
        name="nftscan",
        description="Scan an nft for contracts",
    )
    @checks.not_blacklisted()
    async def nftContractScan(self, context: Context, network: str, address: str = "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D"
                           ) -> None:
        """
        Kick a user out of the server.
        :param context: The hybrid command context.
        :param network: [1] Ethereum Mainnet
        :param address: .
        """
        import requests
        from helpers import goplusapicaller
        ret = goplusapicaller.getnftSecurity(network, address)
        pprint = json.dumps(ret, indent=2)
        print(pprint)

        embed = discord.Embed(
            title="NFT Collection Card",
            color=0xE02B2B,
        )
        #embed NFT meta data into an embed
        for k, v in dict(ret).items():
            if type(v) is int or type(v) is float or type(v) is str:
                embed.add_field(name=k, value=v, inline=False)
     
        
        # topHolders = ret[address.lower()]["holders"]
        # for index, h in enumerate(topHolders[0:3]):
        #     holderEmbed = discord.Embed(
        #         title="Holder Card " + str(index + 1),
        #         color=0xE02B2B,
        #     )
        #     holderEmbed.add_field(
        #         name="name", value=h["address"], inline=False)
        #     holderEmbed.add_field(name="tag", value=h["tag"], inline=True)
        #     holderEmbed.add_field(name="is_contract",
        #                           value=h["is_contract"], inline=True)
        #     holderEmbed.add_field(
        #         name="balance", value=h["balance"], inline=False)
        #     holderEmbed.add_field(
        #         name="percent", value=h["percent"], inline=True)
        #     await context.send(embed=holderEmbed)
        await context.send(embed=embed)

# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
async def setup(bot):
    await bot.add_cog(GoPlus(bot))