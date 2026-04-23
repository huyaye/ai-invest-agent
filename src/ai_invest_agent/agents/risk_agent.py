from ai_invest_agent.core.llm import call_llm

def risk_agent(analysis: str) -> str:
    prompt = f"""
    다음 분석에서 리스크만 추출해라:

    {analysis}
    """

    return call_llm(prompt)