from typing import Any, Dict

class State:
    """
    Holds the runtime state for agents.
    State is serializable and deterministic.
    """

    def __init__(self, data: Dict[str, Any] = None):
        self.data: Dict[str, Any] = data or {}
        self.step_count: int = 0

    def get(self, key: str, default: Any = None) -> Any:
        return self.data.get(key, default)

    def set(self, key: str, value: Any) -> None:
        self.data[key] = value

    def increment(self, key: str, amount: int = 1) -> int:
        self.data[key] = self.data.get(key, 0) + amount
        return self.data[key]

    def __repr__(self) -> str:
        return f"State(step_count={self.step_count}, data={self.data})"
