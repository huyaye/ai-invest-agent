from ai_invest_agent.core.llm import call_llm

def decision_agent(analysis: str, risk: str) -> str:
    prompt = f"""
    분석:
    {analysis}

    리스크:
    {risk}

    투자 관점에서 결론을 내려라.

    - 단기 / 장기 구분
    - 확신도 (높음/중간/낮음)
    """

    return call_llm(prompt)