from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    name: str
    desc: str


class ItemCreate(ItemBase):
    id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class ItemUpdate(ItemBase):
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class Item(ItemBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
