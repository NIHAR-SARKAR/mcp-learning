# mcp-learning: 
Natural Language Database Querying with MCP Server and LLMs

This repository serves as a testing ground and implementation example for interacting with a database using natural language queries, facilitated by an **MCP (Model Context Protocol) server** and a **Large Language Model (LLM)**. The core idea is to enable users to ask questions about a database in plain human text, and the application, leveraging the power of the LLM and the MCP server, will retrieve and present the appropriate data.


## 🛠️ Technologies Used

* **Python 3.8+:** The primary programming language.

* **`asyncio`:** For asynchronous programming.

* **`openai` library:** For interacting with Azure OpenAI (or compatible) LLM services.

* **`psycopg2` (or similar):** For PostgreSQL database connectivity.

* **MCP Server Implementation:** The underlying framework for managing model context and interactions. (Specific details depend on your exact MCP server implementation, which is being tested here).

* **PostgreSQL:** The relational database system.

## ⚙️ Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

* **Python 3.8+** installed on your system.

* **Git** for cloning the repository.

* **An Azure Account** with access to Azure OpenAI Service. You will need:

    * Your **Azure OpenAI Endpoint URL**.

    * Your **Azure OpenAI API Key**.

    * The **Deployment ID** of your LLM model (e.g., `gpt-35-turbo-deployment`).

    * The **API Version** for your Azure OpenAI deployment (e.g., `2024-02-15-preview`).

* **A PostgreSQL Database** instance. You will need:

    * Database Host

    * Database Port

    * Database Name

    * Database User

    * Database Password
 
git clone https://github.com/NIHAR-SARKAR/mcp-learning.git
cd mcp-learning


### 2. Set up a Virtual Environment

It's highly recommended to use a virtual environment to manage project dependencies:

python3 -m venv .venv


Activate the virtual environment:

* **On macOS/Linux:**

    ```
    source .venv/bin/activate
    
    ```

* **On Windows (Command Prompt):**

    ```
    .venv\Scripts\activate.bat
    
    ```

* **On Windows (PowerShell):**

    ```
    .venv\Scripts\Activate.ps1
    
    ```

### 3. Install Dependencies

Install the required Python packages using `pip`:

pip install -r requirements.txt


**Note:** If `requirements.txt` is missing, you'll need to create it. A good starting point would be:

openai
psycopg2-binary # Or psycopg2 if you have build tools
asyncio

Add any other libraries your project uses

### 4. Configuration

This project relies on environment variables or a `settings.py` file to configure access to your Azure AI service and PostgreSQL database.

**Recommended: Using Environment Variables**

Create a `.env` file in the root of your project (or set these directly in your shell/system environment) and populate it with your credentials:

.env file content
Azure OpenAI Credentials
MODEL_URL="https://your-resource-name.openai.azure.com/"
MODEL_API_KEY="your_azure_openai_api_key_here"
MODEL_API_VERSION="2024-02-15-preview" # Or your specific version
AZURE_OPENAI_DEPLOYMENT_ID="your-llm-deployment-name" # e.g., gpt-35-turbo-deployment


###The application will then:

1.  Send your query to the LLM.

2.  The LLM will generate a SQL query.

3.  The application will execute the SQL query against your PostgreSQL database.

4.  The results will be displayed in your terminal.

## 💡 Troubleshooting

* **`mcp.shared.exceptions.McpError: Connection closed`**:

    * **Verify your Azure OpenAI Endpoint, API Key, and API Version** in your `.env` file. A common cause is a typo or incorrect version.

    * **Check network connectivity:** Ensure your machine can reach the Azure OpenAI endpoint (e.g., `ping your-resource-name.openai.azure.com`).

    * **Firewall/Proxy:** Ensure no local or corporate firewall/proxy is blocking the connection.

    * **Asynchronous Client Setup:** Ensure your client initialization follows the recommended asynchronous context manager pattern, as discussed in recent updates to the `openai` library:

        ```
        # Example from previous discussion
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(
                read, write, sampling_callback=handle_sampling_message
            ) as session:
                await session.initialize()
                # ... proceed with session operations
        
        ```

* **Database Connection Errors:** Double-check your `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, and `DB_PASSWORD` in your `.env` file. Ensure your database server is running and accessible from your machine.

* **SQL Generation Issues:** If the LLM generates incorrect SQL, you might need to refine your prompts or provide more context/examples to the LLM.

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements, bug fixes, or new features, please open an issue or submit a pull request.
