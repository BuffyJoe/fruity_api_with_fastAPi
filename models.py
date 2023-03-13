from pydantic import BaseModel, UUID4
from typing import Optional
# from fastapi import

from enum import Enum

class Condition(str, Enum):
    ripe = 'ripe'
    unripe = 'unripe'
    overripe = 'overripe'

class Fruits(BaseModel):
    # id: UUID4()
    name: str
    day_last_seen: Optional[str]
    price: Optional[str]
    day_first_seen: str
    condition: Condition
    # location: str
    image: Optional[str]


class updateFruits(BaseModel):
    # id: UUID4()
    day_last_seen: Optional[str]
    price: Optional[str]
    condition: Optional[str]
    image: Optional[str]