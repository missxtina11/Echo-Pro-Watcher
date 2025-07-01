# echo_protocol_watcher.py
import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv

from utils.chart_utils import plot_holder_distribution
from utils.xrpl_utils import (
    get_whale_data,
    get_bubble_map,
    get_big_txns,
    get_sentiment,
)
from utils.price_utils import fetch_price  # optional if you still want /price

# ──────────────────────────────────────────────────────────────────────
#  Setup
# ──────────────────────────────────────────────────────────────────────
load_dotenv()
logging.basicConfig(level=logging.INFO)

bot = Bot(
    token=os.getenv("TG_BOT_TOKEN"),
    default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN),
)
dp = Dispatcher()

# ──────────────────────────────────────────────────────────────────────
#  Commands
# ──────────────────────────────────────────────────────────────────────
@dp.message(Command("start"))
async def start_cmd(message: types.Message) -> None:
    await message.answer(
        "🤖 *Echo Protocol Watcher Activated!*\n"
        "Type /help to see available commands."
    )


@dp.message(Command("help"))
async def help_cmd(message: types.Message) -> None:
    await message.answer(
        """
*Echo Protocol Watcher — Commands*
/holderschart – STB holder distribution
/whales        – Top STB whale wallets
/bubbles       – Bubble-map cluster summary
/buysells      – Large buy/sell tracker
/sentiment     – AI wallet sentiment
/price         – STB price   (optional)
/status        – Bot status
""".strip()
    )


@dp.message(Command("holderschart"))
async def holderschart_cmd(message: types.Message) -> None:
    path = plot_holder_distribution()
    await message.answer_photo(types.FSInputFile(path))


@dp.message(Command("whales"))
async def whales_cmd(message: types.Message) -> None:
    await message.answer(await get_whale_data())


@dp.message(Command("bubbles"))
async def bubbles_cmd(message: types.Message) -> None:
    await message.answer(await get_bubble_map())


@dp.message(Command("buysells"))
async def buysells_cmd(message: types.Message) -> None:
    await message.answer(await get_big_txns())


@dp.message(Command("sentiment"))
async def sentiment_cmd(message: types.Message) -> None:
    await message.answer(await get_sentiment())


@dp.message(Command("price"))
async def price_cmd(message: types.Message) -> None:
    price = await fetch_price()
    await message.answer(f"💰 *STB Price:* `{price}`")


@dp.message(Command("status"))
async def status_cmd(message: types.Message) -> None:
    await message.answer("✅ Echo Protocol Watcher is online and operational.")

# ──────────────────────────────────────────────────────────────────────
#  Entrypoint
# ──────────────────────────────────────────────────────────────────────
async def main() -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

