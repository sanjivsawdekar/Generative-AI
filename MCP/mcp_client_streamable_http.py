from fastmcp.client import Client
from fastmcp.client.transports import StreamableHttpTransport
import asyncio

async def main():
    # Connect to running MCP server over Streamable HTTP
    transport = StreamableHttpTransport(url="http://localhost:8765/mcp")

    # Create client with that transport
    async with Client(transport=transport) as client:
        # List tools
        tools = await client.list_tools()
        #print("Available tools:", [t.name for t in tools])
        print("Available tools with description:")
        for tool in tools:
            # tool.name → tool name
            # tool.description → description (set in server with @tool docstring)
            print(f"- {tool.name}: {tool.description}")
            
        # Call greet
        res1 = await client.call_tool("greet", {"name": "Sanjiv"})
        print("\ngreet('Sanjiv') → ", res1.structured_content['result'])

        # Call add_numbers
        res2 = await client.call_tool("add_numbers", {"a": 5, "b": 10})
        print("\nadd_numbers(5, 10) →", res2.structured_content['result'])

if __name__ == "__main__":
    asyncio.run(main())
