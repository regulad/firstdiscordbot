from shelve import Shelf
from typing import override

from aiocoingecko import AsyncCoinGeckoAPISession
from discord.ext.commands import Bot


class MyBot(Bot):
    db: Shelf
    cg: AsyncCoinGeckoAPISession

    @override
    async def close(self) -> None:
        await super().close()
        await self.cg.close()  # close CoinGecko session to prevent memory leak


__all__ = ("MyBot",)
