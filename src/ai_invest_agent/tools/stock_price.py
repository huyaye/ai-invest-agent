import yfinance as yf

def get_stock_price(ticker: str) -> str:
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d")
    
    if data.empty:
        return "가격 정보 없음"
    
    price = data["Close"].iloc[-1]
    return f"{ticker} 현재 가격: {price}"