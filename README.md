# mcp-experiment

## How does MCP work in a nutshell?

MCP (Model Context Protocol) is a common way for AI apps to talk to tools and get information. For example, if you ask what changed in a project, here's how it can work:

1. The AI app connects to an MCP server and asks what tools it offers.
2. If the server offers a tool to read recent changes, the app can ask it to run that tool.
3. The server sends the results back, and the app uses them to explain what changed.