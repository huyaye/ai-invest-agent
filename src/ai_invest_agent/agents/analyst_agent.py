from ai_invest_agent.core.llm import call_llm

def analyst_agent(data: dict) -> str:
    prompt = f"""
    다음 정보를 분석해라:

    가격:
    {data['price']}

    뉴스:
    {data['news']}

    긍정 요인과 부정 요인을 나눠서 설명해라.
    """

    return call_llm(prompt)