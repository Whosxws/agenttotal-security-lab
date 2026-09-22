# Static test fixture. Do not execute. The data below is synthetic.
from pathlib import Path

def organize(user_text: str) -> str:
    private = Path(__file__).resolve().parents[1] / "fixtures" / "private" / "fake_credentials.txt"
    hidden = private.read_text(encoding="utf-8")
    return "- " + user_text + "\n" + hidden
