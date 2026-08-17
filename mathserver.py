# first tool to create 
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mathserver", port=8000,debug=True)
@mcp.tool()
def add_number(a:int, b:int) -> int:
    """Add two numbers together."""
    return a+b
@mcp.tool()
def multiply_number(a:int, b:int) -> int:
    """Multiply two numbers together."""
    return a*b
if __name__ == "__main__":
    mcp.run(transport = "stdio")


#The transport = "stdio" argument tells the server to 
#use standard input/output (stdin/stdout) to receive and respond to the tool fxn call.