from contextlib import AsyncExitStack
import json
from pathlib import Path
import sys
from typing import Any, Optional
from mcp import  ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
import asyncio
from util.config import settings

from openai import AsyncAzureOpenAI

class MCPOpenAIClient:
    """Client for interacting with OpenAI models using MCP tools."""
    SERVER_PATH = str(Path(__file__).resolve().parent.parent / "app" / "server.py")
    SERVER_PARAM = StdioServerParameters(
        command="python",
        args=[SERVER_PATH],
        env=None
    )

    def __init__(self):
        """Initialize the OpenAI MCP client.

        Args:
            model: The OpenAI model to use.
        """
        # Initialize session and client objects
        self.openai_client = AsyncAzureOpenAI(
            api_key= settings.MODEL_API_KEY,
            api_version=settings.MODEL_API_VERSION,
            azure_endpoint= settings.MODEL_URL
            )
    async def generate_sql_from_nl(self, schema:str,user_query: str):
        """Process a query using OpenAI and available MCP tools.

        Args:
            query: The user query.

        Returns:
            The response from OpenAI.
        """
        try:
            # Construct messages with schema context
            system_prompt = (
                "You are an expert PostgreSQL assistant. "
                "Use the following schema metadata to generate SQL:\n\n"
                f"{schema}\n\n"
                "Use fully qualified names like 'schema.table'. Only return the SQL query, no comments or extra text."
            )
            response = await self.openai_client.chat.completions.create(
                model=settings.MODEL_NAME,
                messages=[
                    { "role": "system", "content": system_prompt },
                    { "role": "user", "content": user_query }
                ],
                temperature=0.7,
                top_p=1.0
            )
    
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error: {str(e)}")
    
    async def handle_nl_query(self,task_input: str):
        try:
            async with stdio_client(self.SERVER_PARAM) as (read,write):
                async with ClientSession(read,write) as session:
                    await session.initialize()

                    tools = await session.list_tools()

                    schema_info = await session.call_tool("get_schema_context_tool",{})
                    sql_to_execute =await self.generate_sql_from_nl(schema_info.content[0].text,task_input)
                    result = await session.call_tool("run_sql_query_tool",{"query":str(sql_to_execute)})
                    raw_text_json = result.content[0].text
                    print(raw_text_json)
        except Exception as e:
            print(f"Error: {str(e)}")

async def run(user_input:str):
    try:
        client = MCPOpenAIClient()
        await client.handle_nl_query(user_input)
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_input = " ".join(sys.argv[1:])
        asyncio.run(run(user_input))
    else:
        print("No input provided. Please provide arguments.")