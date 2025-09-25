from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import List, Dict, Optional
import uvicorn
import asyncio
from fastmcp import FastMCP

# ------------------------------
# Setup MCP server
# ------------------------------
mcp = FastMCP(name="json-server")
host="localhost" # IP address of host or hostname
api_port=8000
mcp_port=8766

# ------------------------------
# Pydantic Models
# ------------------------------

# Model for Tool 1: JSON Processing
# Input
class ProcessJsonRequest(BaseModel):
    user: str = Field(..., description="Name of the user")
    values: List[float] = Field(..., description="List of numeric values")
    meta: Optional[Dict] = Field(default_factory=dict, description="Optional metadata")

# Output
class ProcessJsonResponse(BaseModel):
    user: str
    count: int
    sum: float
    meta: Dict

# Model for Tool 2: Reverse String
# Input
class ReverseStringRequest(BaseModel):
    text: str = Field(..., description="Input string to reverse")
# Output
class ReverseStringResponse(BaseModel):
    reversed: str

# ------------------------------
# Tool 1: JSON Processing
# ------------------------------

def process_json_func(payload: ProcessJsonRequest) -> ProcessJsonResponse:
    """
    Processes JSON data.
    Args:
        payload: ProcessJsonRequest containing user, values, and optional meta.
    Returns:
        A ProcessJsonResponse with the user, count, sum, and meta.
    """
    return ProcessJsonResponse(
        user=payload.user,
        count=len(payload.values),
        sum=sum(payload.values),
        meta=payload.meta
    )

# Register tool with MCP (so client can see it in list_tools)
mcp.tool()(process_json_func)


# ------------------------------
# Tool 2: Reverse String
# ------------------------------
def reverse_string_func(payload: ReverseStringRequest) -> ReverseStringResponse:
    """
    Reverses the input string.
    Args:
        payload: ReverseStringRequest containing text to reverse.
    Returns:
        A ReverseStringResponse with the reversed text.
    """

    result = ReverseStringResponse(reversed=payload.text[::-1])
    print("DEBUG: reverse_string:", result.model_dump_json())
    return result

# Register tool with MCP
mcp.tool()(reverse_string_func)

# ------------------------------
# FastAPI App
# ------------------------------
app = FastAPI(title="MCP JSON Server with REST + MCP")

# Endpoint 1: process_json
@app.post("/process_json", response_model=ProcessJsonResponse)
async def process_json_endpoint(payload: ProcessJsonRequest):
    try:
        return JSONResponse(content=process_json_func(payload).dict())
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

# Endpoint 2: reverse_string
@app.post("/reverse_string", response_model=ReverseStringResponse)
async def reverse_string_endpoint(payload: ReverseStringRequest):
    try:
        return JSONResponse(content=reverse_string_func(payload).model_dump_json())
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

# ------------------------------
# Run both REST + MCP
# ------------------------------
@app.on_event("startup")
async def start_mcp_server():
    # Run MCP protocol server in parallel on another port
    asyncio.create_task(
        mcp.run_async(
            transport="streamable-http",   # MCP transport
            host=host,
            port=mcp_port,
            path="/mcp"                   # MCP endpoint
        )
    )

if __name__ == "__main__":
    # Start the FastAPI application using Uvicorn
    uvicorn.run(app, host=host, port=api_port)
