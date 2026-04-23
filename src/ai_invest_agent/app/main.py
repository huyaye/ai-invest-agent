from ai_invest_agent.services.analysis_service import collect_data
from ai_invest_agent.agents.analyst_agent import analyst_agent
from ai_invest_agent.agents.risk_agent import risk_agent
from ai_invest_agent.agents.decision_agent import decision_agent

def run(ticker: str, company: str):
    data = collect_data(ticker, company)
    
    analysis = analyst_agent(data)
    risk = risk_agent(analysis)
    decision = decision_agent(analysis, risk)

    return decision

if __name__ == "__main__":
    result = run("005930.KS", "삼성전자")
    print(result)