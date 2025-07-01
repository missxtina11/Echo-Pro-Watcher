# echo_protocol_watcher.py
import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message
from dotenv import load_dotenv

# Local helpers
from utils.chart_utils import plot_holder_distribution
from utils.price_utils import fetch_price
from utils.xrpl_utils import (
    get_whale_data,
    get_bubble_map,
    get_big_txns,
    get_sentiment,
    gpt_wallet_summary,
    gpt_token_holders_analysis,
    gpt_sentiment_from_trades,
)

# ──────────────────────────────────────────────────────────────────────
#  Setup
# ──────────────────────────────────────────────────────────────────────
load_dotenv()
logging.basicConfig(level=logging.INFO)

TG_BOT_TOKEN = os.getenv("TG_BOT_TOKEN")
XRPL_WALLET_ADDRESS = os.getenv("XRPL_WALLET_ADDRESS")  # optional default wallet

bot = Bot(
    token=TG_BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN),
)
dp = Dispatcher()

# ──────────────────────────────────────────────────────────────────────
#  Core commands
# ──────────────────────────────────────────────────────────────────────
@dp.message(Command("start"))
async def cmd_start(message: Message) -> None:
    await message.answer(
        "🤖 *Echo Protocol Watcher Activated!*\n"
        "Type /help to see available commands."
    )


@dp.message(Command("help"))
async def cmd_help(message: Message) -> None:
    await message.answer(
        """
*Echo Protocol Watcher — Commands*
/holderschart – STB holder distribution
/whales        – Top STB whale wallets
/bubbles       – Bubble-map cluster summary
/buysells      – Large buy/sell tracker
/sentiment     – AI wallet sentiment
/price         – STB price feed
/gptwallet     – GPT wallet insight
/gptholders    – GPT top-holders insight
/gptsentiment  – GPT trade-sentiment scan
/status        – Bot status
""".strip()
    )


@dp.message(Command("holderschart"))
async def cmd_holders_chart(message: Message) -> None:
    path = plot_holder_distribution()
    await message.answer_photo(types.FSInputFile(path))


@dp.message(Command("whales"))
async def cmd_whales(message: Message) -> None:
    await message.answer(await get_whale_data())


@dp.message(Command("bubbles"))
async def cmd_bubbles(message: Message) -> None:
    await message.answer(await get_bubble_map())


@dp.message(Command("buysells"))
async def cmd_buysells(message: Message) -> None:
    await message.answer(await get_big_txns())


@dp.message(Command("sentiment"))
async def cmd_sentiment(message: Message) -> None:
    await message.answer(await get_sentiment())


@dp.message(Command("price"))
async def cmd_price(message: Message) -> None:
    price = await fetch_price()
    await message.answer(f"💰 *STB Price:* `{price}`")


@dp.message(Command("status"))
async def cmd_status(message: Message) -> None:
    await message.answer("✅ Echo Protocol Watcher is online and operational.")

# ──────────────────────────────────────────────────────────────────────
#  GPT-powered commands
#   (replace helper stubs with real data fetchers in utils/xrpl_utils.py)
# ──────────────────────────────────────────────────────────────────────
async def _get_wallet_tx_history(wallet: str) -> str:
    """Placeholder – replace with real XRPL TX fetch."""
    return f"Sample TX history for wallet {wallet}."

async def _get_holder_list_summary() -> str:
    """Placeholder – replace with real holder list."""
    return "WalletA: 25%, WalletB: 18%, Others: 57%"

async def _get_recent_trade_logs() -> str:
    """Placeholder – replace with real trade logs."""
    return "BUY 100k, SELL 50k, BUY 80k …"

@dp.message(Command("gptwallet"))
async def cmd_gpt_wallet(message: Message) -> None:
    wallet = (
        message.text.split(" ")[1] if len(message.text.split()) > 1 else XRPL_WALLET_ADDRESS
    )
    tx_data = await _get_wallet_tx_history(wallet)
    response = await gpt_wallet_summary(tx_data)
    await message.answer(response)


@dp.message(Command("gptholders"))
async def cmd_gpt_holders(message: Message) -> None:
    holder_data = await _get_holder_list_summary()
    response = await gpt_token_holders_analysis(holder_data)
    await message.answer(response)


@dp.message(Command("gptsentiment"))
async def cmd_gpt_sentiment(message: Message) -> None:
    trade_logs = await _get_recent_trade_logs()
    response = await gpt_sentiment_from_trades(trade_logs)
    await message.answer(response)


# ──────────────────────────────────────────────────────────────────────
#  Entrypoint
# ──────────────────────────────────────────────────────────────────────
async def main() -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

