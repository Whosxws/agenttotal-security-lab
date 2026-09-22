"""Toy MCP reader for STATIC analysis only; do not import or start this server.
Security assumption: fixtures is a trusted immutable directory, no symlink swaps.
All fixtures contain synthetic study text, never credentials.
"""
from pathlib import Path
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("round1-file-reader")
ROOT = (Path(__file__).parent / "fixtures").resolve()

@mcp.tool()
def read_test_file(path: str) -> str:
    """Read a synthetic text file from the allowed fixtures directory."""
    candidate = (ROOT / path).resolve()
    return candidate.read_text(encoding="utf-8")
