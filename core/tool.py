# Created by Rohtak Patwardhan. 2025. 

from typing import Dict, Any

class Tool:
    """

    A Tool is a controlled side-effect.

    Tools are registered, called via scheduler, and need a deterministic input. 

    """

    name: str

    def execute(self, input: Dict[str, Any]) -> Any:
        raise NotImplementedError

    # Tools must not access agent state, control time, or spawn threads and processes