import asyncio
from fastmcp.client import Client
from fastmcp.client.transports import StreamableHttpTransport

host="localhost" # IP address of host or hostname
api_port=8000
mcp_port=8766

async def main():
    transport = StreamableHttpTransport(url=f"http://{host}:{mcp_port}/mcp")

    async with Client(transport=transport) as client:
        print("\n=== Connected to MCP server ===")

        tools = await client.list_tools()
        print("\n=== Available Tools ===\n")
        for index, t in enumerate(tools):
            print(f"============================\nTool#{index+1} - {t.name}:\n============================\n{t.description}\n")

        res = await client.call_tool("process_json_func", {
                "payload": {"user": "alice", "values": [1, 2, 3], "meta": {"active": True}}
        })
        print("\n=== Raw Result ===")
        print(res)

        print("\n=== Processed Result by fields ===")
        if res.content:
            for item in res.content[0]:
                    print(f"{item[0]}: {item[1]}")
        else:
            print("No content returned")

        if res.structured_content:
            print("\n=== Structured JSON Output ===", type(res.structured_content))
            print(res.structured_content)


    # ------------------------------
    # Calling the /process_json endpoint
    # ------------------------------
    import requests

    url = f"http://{host}:{api_port}/process_json"
    payload = {
        "user": "sanjiv",
        "values": [10, 20, 30],
        "meta": {"source": "python-client"}
    }

    response = requests.post(url, json=payload)
    print("\n=== Endpoint Output ===\n", response.json())


if __name__ == "__main__":
    asyncio.run(main())
