# utils/xrpl_utils.py
"""
Placeholder helpers for Echo Protocol Watcher.

⚠️  These currently return static strings.
Swap in real XRPL calls (or a DB) later.
"""

# ───────────────────────────────────────────────────────────
#  Core analytics
# ───────────────────────────────────────────────────────────
async def get_whale_data() -> str:
    return (
        "🐋 *Top STB Whale Wallets*\n"
        "1. rXXXX...   · 25 %\n"
        "2. rYYYY...   · 18 %\n"
        "3. rZZZZ...   · 10 %\n"
    )


async def get_bubble_map() -> str:
    return (
        "🧩 *Bubble Map Clusters*\n"
        "• Cluster A – 12 wallets (42 % share)\n"
        "• Cluster B –  8 wallets (30 %)\n"
        "• Cluster C –  6 wallets (18 %)\n"
        "• Long tail  – others\n"
    )


async def get_big_txns() -> str:
    return (
        "💸 *Large Buys / Sells*\n"
        "• Buy 120 k STB @ 0.000065\n"
        "• Sell  80 k STB @ 0.000067\n"
        "• Buy  70 k STB @ 0.000066\n"
    )


async def get_sentiment() -> str:
    return (
        "🧠 *AI Wallet Sentiment*\n"
        "• Trend: **Bullish**  \n"
        "• Confidence: 72 %  \n"
        "• Note: Top wallets accumulating on dips."
    )

import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
GPT_MODEL = os.getenv("GPT_MODEL", "gpt-4o")
GPT_ENABLED = os.getenv("ENABLE_GPT_WALLET_INSIGHTS", "false").lower() == "true"

async def gpt_wallet_summary(wallet_data: str):
    if not GPT_ENABLED:
        return "🧠 GPT Wallet Insights are disabled."

    prompt = (
        "You are an expert blockchain analyst. Analyze the following XRPL wallet activity. "
        "Summarize the wallet’s behavior, risk profile, trading habits, and potential classification "
        "(e.g., holder, sniper, whale, bot, LP provider).\n\n"
        f"{wallet_data}"
    )
    try:
        response = openai.ChatCompletion.create(
            model=GPT_MODEL,
            messages=[
                {"role": "system", "content": "You are a blockchain wallet analyst."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=400,
            temperature=0.6,
        )
        return "🧠 GPT Insight:\n" + response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ GPT error: {str(e)}"

async def gpt_token_holders_analysis(holder_data: str):
    if not GPT_ENABLED:
        return "🧠 GPT Token Holder Analysis is disabled."

    prompt = (
        "You are an expert XRPL token analyst. Analyze this list of token holders and their holdings. "
        "Identify possible whales, influencers, suspicious patterns, and concentration risk:\n\n"
        f"{holder_data}"
    )
    try:
        response = openai.ChatCompletion.create(
            model=GPT_MODEL,
            messages=[
                {"role": "system", "content": "You analyze token holder distribution."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=350,
            temperature=0.5,
        )
        return "📊 Holder Analysis:\n" + response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ GPT error: {str(e)}"

async def gpt_sentiment_from_trades(trade_logs: str):
    if not GPT_ENABLED:
        return "🧠 GPT Sentiment Scan is disabled."

    prompt = (
        "You are a sentiment AI. Given this recent trading log from the XRPL, determine whether the market "
        "is trending bullish, bearish, or uncertain. Provide a brief justification:\n\n"
        f"{trade_logs}"
    )
    try:
        response = openai.ChatCompletion.create(
            model=GPT_MODEL,
            messages=[
                {"role": "system", "content": "You analyze crypto trading sentiment."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=250,
            temperature=0.4,
        )
        return "📈 Sentiment Analysis:\n" + response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ GPT error: {str(e)}"

