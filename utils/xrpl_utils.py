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

