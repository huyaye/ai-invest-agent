def get_news(company: str) -> str:
    news_db = {
        "삼성전자": "HBM 수요 증가로 반도체 업황 개선 기대",
        "엔비디아": "AI 수요 증가로 실적 급증",
        "애플": "아이폰 판매 둔화 우려"
    }

    return news_db.get(company, "관련 뉴스 없음")