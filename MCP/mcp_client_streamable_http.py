import asyncio
from fastmcp.client import Client
from fastmcp.client.transports import StreamableHttpTransport

async def main():
    transport = StreamableHttpTransport(url="http://localhost:8765/mcp")

    async with Client(transport=transport) as client:
        print("\n=== Connected to MCP server ===")

        tools = await client.list_tools()
        print("\n=== Available Tools ===")
        for t in tools:
            print(f"- {t.name}: {t.description}")

        res = await client.call_tool("process_json", {
                "payload": {"user": "alice", "values": [1, 2, 3], "meta": {"active": True}}
        })
        print("\n=== Raw Result ===")
        print(res)

        print("\n=== Processed Result by fields ===")
        if res.content:
            for item in res.content[0]:
                    print(f"{item[0]}: {item[1]}")
                    #print(item[0] , "=",item[1])
        else:
            print("No content returned")

        if res.structured_content:
            print("\n=== Structured JSON Output ===", type(res.structured_content))
            print(res.structured_content)

if __name__ == "__main__":
    asyncio.run(main())
