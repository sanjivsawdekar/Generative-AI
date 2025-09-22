from fastmcp import FastMCP

transport="streamable-http" # other options are "stdio"/"sse"/"http"
host="localhost"
port=8765

# Create an instance of FastMCP with a name
mcp = FastMCP(name="my-server")

# Define tools using the @mcp.tool() decorator

@mcp.tool
def greet(name: str) -> str:
    """
    Generates a personalized greeting message.
    Args:
        name: The name to greet.
    Returns:
        A string containing the greeting.
    """
    return f"Hello, {name}! Welcome to the FastMCP server."

@mcp.tool
def add_numbers(a: int, b: int) -> int:
    """
    Adds two integer numbers together.
    Args:
        a: The first integer.
        b: The second integer.
    Returns:
        The sum of the two integers.
    """
    return a + b

if __name__ == "__main__":
    # Run the server using selected transport
    mcp.run(transport=transport, host=host, port=port)
