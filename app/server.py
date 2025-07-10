from typing import Union
from mcp.server.fastmcp import FastMCP,Context
from mcp.types import (
    Completion,
    CompletionArgument,
    CompletionContext,
    PromptReference,
    ResourceTemplateReference,
)
from services.db_executor import run_sql_query
from services.schema_loader import get_schema_context

mcp = FastMCP(name="mcptest")

@mcp.tool()
async def get_schema_context_tool():
    """Retrieve the entire sql schema base as a formatted string.

    Returns:
        A formatted sql db metadata
    """
    try:
        return await get_schema_context()
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
async def run_sql_query_tool(query: str):
    """Retrieve sql data base on sql query.

    Returns:
        Sql data base on sql query.
    """
    try:
        return await run_sql_query(query)
    except Exception as e:
        return f"Error: {str(e)}"


# Run the server
if __name__ == "__main__":
    mcp.run(transport="stdio",mount_path="/qmcp")