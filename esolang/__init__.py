from .esolang import Esolang


async def setup(bot):
    await bot.add_cog(Esolang(bot))
