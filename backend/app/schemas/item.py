from pydantic import BaseModel, ConfigDict 
from typing import Optional

class ItemBase(BaseModel):
  title: str 
  discriptions: Optional[str] = None 

class ItemCreate(ItemBase):
  pass

class ItemRead(ItemBase):
  id: int 
  owner_id: int 

  model_config = ConfigDict(from_attributes=True)