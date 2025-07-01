# Echo Protocol Watcher

**Echo Protocol Watcher** is a lightweight Telegram bot for monitoring XRPL wallets, AMM pools, STB token stats, and price data in real time.

## 🚀 Features
- `/balance` – View XRP and token balances
- `/balancechart` – Pie chart of wallet holdings
- `/holderschart` – Token distribution chart
- `/wallet` – Recent transactions
- `/amm` – AMM pool stats
- `/liquidity` – Total liquidity
- `/price` – STB price feed
- `/status`, `/pause`, `/resume` – Bot controls

## 🛠 Setup
1. Clone the repo  
   `git clone https://github.com/yourusername/echo-protocol-watcher.git`

2. Install dependencies  
   `pip install -r requirements.txt`

3. Create a `.env` file with:
   ```env
   XRPL_RPC=https://xrplcluster.com
   XRPL_SEED=your_seed_here
   XRPL_WALLET_ADDRESS=your_wallet_address
   STB_CODE=STB
   STB_ISSUER=rw9kWBD9LwnCrvLEZFDApDDLYfwZFv1dNs
   TG_BOT_TOKEN=your_telegram_token
   TG_CHAT_ID=your_chat_id
   ```

4. Run the bot  
   `python echo_protocol_watcher.py`

---

Built for the XRPL by Echo Labs.
# Echo-Pro-Watcher
