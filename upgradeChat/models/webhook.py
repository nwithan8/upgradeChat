# generated by datamodel-codegen:
#   filename:  model.json
#   timestamp: 2021-04-11T02:36:08+00:00

from __future__ import annotations

from typing import List, Optional
from uuid import UUID

from pydantic import AnyUrl, BaseModel, Field


class Webhook(BaseModel):
    id: Optional[UUID] = None
    uri: Optional[AnyUrl] = None


class Model(BaseModel):
    data: Optional[Webhook] = Field(None)

    def __str__(self):
        return f"<Webhook {self.data.id}>"
