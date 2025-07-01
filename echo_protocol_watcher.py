# echo_protocol_watcher.py
import logging
import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import BotCommand
from aiogram.filters import Command
from aiogram import F
from aiogram.utils.markdown import hbold
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv

from utils.xrpl_utils import (
    get_wallet_balances, get_latest_transactions, get_amm_info,
    get_liquidity, get_holder_distribution, get_wallet_analysis,
)
from utils.chart_utils import plot_pie_chart, plot_holder_distribution
from utils.price_utils import fetch_price

load_dotenv()
logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv("TG_BOT_TOKEN"), default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("🤖 *Echo Protocol Watcher Activated!*
Use /help to see available commands.")

@dp.message(Command("help"))
async def help_cmd(message: types.Message):
    await message.answer("""*Echo Protocol Watcher Commands*
/price – STB price
/balance – wallet balances
/balancechart – pie chart of wallet
/holderschart – STB holder distribution
/wallet – latest wallet TXs
/amm – STB AMM stats
/liquidity – AMM liquidity
/status – bot status
/logs – recent logs
/pause or /resume – control bot
/help – this help page
""")

@dp.message(Command("price"))
async def price_cmd(message: types.Message):
    price = await fetch_price()
    await message.answer(f"💰 *STB Price:* `{price}`")

@dp.message(Command("balance"))
async def balance_cmd(message: types.Message):
    wallet = os.getenv("XRPL_WALLET_ADDRESS")
    balances = await get_wallet_balances(wallet)
    await message.answer(balances)

@dp.message(Command("balancechart"))
async def chart_cmd(message: types.Message):
    wallet = os.getenv("XRPL_WALLET_ADDRESS")
    path = plot_pie_chart(wallet)
    await message.answer_photo(types.FSInputFile(path))

@dp.message(Command("holderschart"))
async def holders_cmd(message: types.Message):
    path = plot_holder_distribution()
    await message.answer_photo(types.FSInputFile(path))

@dp.message(Command("wallet"))
async def wallet_cmd(message: types.Message):
    wallet = os.getenv("XRPL_WALLET_ADDRESS")
    txs = await get_latest_transactions(wallet)
    await message.answer(txs)

@dp.message(Command("amm"))
async def amm_cmd(message: types.Message):
    info = await get_amm_info()
    await message.answer(info)

@dp.message(Command("liquidity"))
async def liq_cmd(message: types.Message):
    liq = await get_liquidity()
    await message.answer(f"🌊 *Total Liquidity:* `{liq}`")

@dp.message(Command("status"))
async def status_cmd(message: types.Message):
    await message.answer("✅ Echo Protocol Watcher is online and operational.")

@dp.message(Command("logs"))
async def logs_cmd(message: types.Message):
    await message.answer("📄 Latest logs not implemented yet.")

@dp.message(Command("pause"))
async def pause_cmd(message: types.Message):
    await message.answer("⏸️ Background tasks paused.")

@dp.message(Command("resume"))
async def resume_cmd(message: types.Message):
    await message.answer("▶️ Background tasks resumed.")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
