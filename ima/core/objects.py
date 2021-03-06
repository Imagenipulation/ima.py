"""
Objects described in the API.

These objects are used internally. You don't need to instantiate them manually.
"""

from typing import Tuple, Optional
from dataclasses import dataclass

__all__ = ["Action", "Parameter", "Factory"]


@dataclass
class Action:
    """Represents the `Action` object of the API.

    Attributes
    ----------
    name : str
        The name of action.
    description : Optional[str]
        The description of the action. Can be `None`.
    """
    name:        str
    description: Optional[str]

    @classmethod
    def from_dict(cls, d: dict):
        temp = {}
        temp["name"]        = d["name"]
        temp["description"] = d.get("description")

        return cls(**temp)


@dataclass
class Parameter:
    """Represents the `Parameter` object of the API.

    Attributes
    ----------
    name : str
        The name of parameter.
    description : Optional[str]
        The description of the parameter. Can be `None`.
    actions : Optional[Tuple[Action]]
        All actions of the parameter.
    """
    name:        str
    description: Optional[str]
    actions:     Optional[Tuple[Action]]

    @classmethod
    def from_dict(cls, d: dict):
        temp = {}
        temp["name"]        = d["name"]
        temp["description"] = d.get("description")

        actions = d.get("actions")
        if actions is not None:
            actions = map(Action.from_dict, actions)
            actions = tuple(actions)

        temp["actions"] = actions

        return cls(**temp)


@dataclass
class Factory:
    """Represents the `Factory` object of the API.

    Attributes
    ----------
    id_ : str
        The id_ of factory.
    image_url : Optional[str]
        An Image URL for the factory. Can be `None`.
    description : Optional[str]
        The description of the factory. Can be `None`.
    parameters: Optional[Tuple[Parameter]]
        All parameters of the factory. Can be `None`.
    """
    id_:         str
    image_url:   Optional[str]
    description: Optional[str]
    parameters:  Optional[Tuple[Parameter]]

    @classmethod
    def from_dict(cls, d: dict):
        temp = {}
        temp["id_"]         = d["id"]
        temp["image_url"]   = d.get("image_url")
        temp["description"] = d.get("description")

        parameters = d.get("parameters")
        if parameters is not None:
            parameters = map(Parameter.from_dict, parameters)
            parameters = tuple(parameters)

        temp["parameters"] = parameters

        return cls(**temp)
