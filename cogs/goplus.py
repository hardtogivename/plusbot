""""
Copyright © Krypton 2019-2023 - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
🐍 A simple template to start to code your own and personalized discord bot in Python programming language.

Version: 5.5.0
"""

from discord.ext import commands
from discord.ext.commands import Context
import discord
import json
from helpers import checks
from discord import app_commands


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
    async def contractScan(self, context: Context, network: str = "1", address: str = "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D"
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
        ret = goplusapicaller.getNFTSecurity(network, address)
        pprint = json.dumps(ret, indent=2)
        print(pprint)

        embed = discord.Embed(
            title="NFT Collection Card",
            color=0xE02B2B,
        )
        # embed NFT meta data into an embed
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
@commands.hybrid_command(
        name="bitcoin",
        description="Get the current price of bitcoin.",
    )
@checks.not_blacklisted()
async def bitcoin(self, context: Context) -> None:
        """
        Get the current price of bitcoin.

        :param context: The hybrid command context.
        """
        # This will prevent your bot from stopping everything when doing a web request - see: https://discordpy.readthedocs.io/en/stable/faq.html#how-do-i-make-a-web-request
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
            ) as request:
                if request.status == 200:
                    data = await request.json(
                        content_type="application/javascript"
                    )  # For some reason the returned content is of type JavaScript
                    embed = discord.Embed(
                        title="Bitcoin price",
                        description=f"The current price is {data['bpi']['USD']['rate']} :dollar:",
                        color=0x9C84EF,
                    )
                else:
                    embed = discord.Embed(
                        title="Error!",
                        description="There is something wrong with the API, please try again later",
                        color=0xE02B2B,
                    )
                await context.send(embed=embed)
# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
async def setup(bot):
    await bot.add_cog(GoPlus(bot))
