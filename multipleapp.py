from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
memory = ConversationBufferMemory()
llm = ChatOpenAI ()
tools = load_tools([
    'wikipedia'
    '11m-math'
    'google-search',
    'python_rept',
    'wolfram-alpha',
    'terminal',
    'news-api',
    'podcast-api'
    'openweathermap-api'
], llm=llm)
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    verbose=True,
    memory=memory)
agent.run( "What's up ChatGPT?")
