import json
from pathlib import Path
from typing import Any

class DataStorage:
    """Handles storage of NBA data."""

    def __init__(self, base_path: str = "data"):
        self.base_path = Path(base_path)
        self.base_path.mkdir(exist_ok=True)

    def save_json(self, filename: str, data: Any) -> None:
        """Saves data to a JSON file."""
        file_path = self.base_path / filename
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
