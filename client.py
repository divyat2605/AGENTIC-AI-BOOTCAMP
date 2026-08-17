# should be able to interact with weather.py and mathserver.py server
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

import asyncio
async def main():
    client=MultiServerMCPClient(
        {
            "math" : {
                "command" : "python",
                "args" : ["mathserver.py"], #always give absolute path
                "transport": "stdio",

            },
            "weather" : {
                "url" : "http://localhost:8000/mcp", #ensure server is running here
                "transport" : "streamable_http"
            }
        }
    )
    import os 
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    tools = await client.get_tools()
    model = ChatGroq(model= "qwen/qwen3.6-27b")
    agent = create_react_agent(
        model,tools
    )
    math_response = await agent.ainvoke(
        {"messages" : [{"role" : "user" , "content" : "what is (3+5) x 12?"}]}
    )
    print("Math response:", math_response['messages'][-1].content)

    #content - will give output of maths response
asyncio.run(main())