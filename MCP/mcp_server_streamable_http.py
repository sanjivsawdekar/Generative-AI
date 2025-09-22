from fastmcp import FastMCP

mcp = FastMCP(name="json-server")

@mcp.tool()
def process_json(payload: dict) -> dict:
    result = {
        "user": payload.get("user"),
        "count": len(payload.get("values", [])),
        "sum": sum(payload.get("values", [])),
        "meta": payload.get("meta", {})
    }
    print("DEBUG: returning dict:", result, type(result))
    return result


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="localhost",
        port=8765,
        path="/mcp"
    )
