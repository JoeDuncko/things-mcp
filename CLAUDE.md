# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

### Development Setup
```bash
# Install dependencies (uses uv package manager)
uv sync

# Run the MCP server
uv run things_server.py
```

### Testing

The project includes a comprehensive unit test suite covering URL scheme construction and data formatting functions.

```bash
# Install test dependencies
uv sync --extra test

# Run all tests
uv run pytest

# Run tests with verbose output
uv run pytest -v

# Run specific test file
uv run pytest tests/test_url_scheme.py

# Run tests matching a pattern
uv run pytest -k "test_format"
```

Test coverage includes:
- All URL construction functions (add, update, show, search)
- Authentication token handling
- Data formatting for todos, projects, areas, and tags
- Error handling and edge cases
- Mock external dependencies (Things.py, AppleScript)

## Architecture Overview

This is a Model Context Protocol (MCP) server that bridges Claude Desktop with the Things 3 task management app on macOS. The architecture consists of:

1. **things_server.py** - Main MCP server implementation using FastMCP framework
   - Defines all MCP tools for interacting with Things
   - List views (inbox, today, upcoming, etc.)
   - CRUD operations for todos/projects/areas
   - Search and tag operations
   - Things URL scheme integration

2. **url_scheme.py** - Things URL scheme implementation
   - Constructs Things URLs for various operations
   - Uses AppleScript to execute URLs without bringing Things to foreground
   - Handles authentication tokens for update operations

3. **formatters.py** - Data formatting utilities
   - Converts Things database objects to human-readable text
   - Handles nested data (projects within areas, checklist items, etc.)

4. **tests/** - Unit test suite
   - **conftest.py** - Pytest fixtures and mock data
   - **test_url_scheme.py** - Tests for URL construction (25 test cases)
   - **test_formatters.py** - Tests for data formatting (26 test cases)

## Key Implementation Details

- Uses things.py library for reading Things SQLite database
- Write operations use Things URL scheme API
- FastMCP provides the MCP protocol implementation
- All tools return formatted text strings suitable for Claude
- Error handling for invalid UUIDs and missing parameters
- Supports filtering and including nested items via parameters
- Unit tests mock all external dependencies (Things.py, AppleScript)
- Pytest configuration in pyproject.toml with async support

## Things URL Scheme Authentication

For update operations, the server automatically fetches and includes the auth-token from things.py. This allows updating existing items without user intervention.