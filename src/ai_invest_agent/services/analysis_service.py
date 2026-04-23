from ai_invest_agent.tools.stock_price import get_stock_price
from ai_invest_agent.tools.news import get_news

def collect_data(ticker: str, company: str) -> dict:
    return {
        "price": get_stock_price(ticker),
        "news": get_news(company)
    }