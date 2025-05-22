# MCP Server Demo

This file strcture is created with "uv". Make sure that you have installed uv.

uv home - https://docs.astral.sh/uv/

On Power Shell
`powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`

PyPI
`pip install uv`

Check the list of all uv commands at https://docs.astral.sh/uv/reference/cli/


Create new project in current directory.

`uv init .` - Creates all required files.

`uv add "mcp[cli]"` - Adds MCP support.

`uv run mcp install main.py` - Install our demo mcp server.

Download & install Claude Desktop from https://claude.ai/download to interact with our demo mcp server.

Open Claude Desktop, go to File > Settings > Developer > Edit Config, it opens claude_desktop_config.json file for editing.
