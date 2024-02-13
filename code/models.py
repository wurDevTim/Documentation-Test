""""Dataclasses for all the replies """
from __future__ import annotations

from dataclasses import dataclass
from typing import List
from typing import Any


@dataclass
class Variable:
    max: float
    min: float
    name: str
    unit: str
    value: float

    @staticmethod
    def from_dict(obj: Any) -> Variable:
        """"Convert json to Variable class

        Return:
            Variable"""
        return Variable(
            max=obj.get("Max"),
            min=obj.get("Min"),
            name=obj.get("Name"),
            unit=obj.get("Unit"),
            value=obj.get("Value"),
        )

@dataclass
class ExperimentIDs:
    """"List experiments"""
    @staticmethod
    def from_dict(obj: Any) -> List[int]:
        """"Convert json to python objects

        Return:
            List[int]"""
        if obj.get("json_experiment_id_result") is None:
            return []
        _ids = [int(y.get("experiment_id")) for y in obj.get("json_experiment_id_result")]
        return _ids
