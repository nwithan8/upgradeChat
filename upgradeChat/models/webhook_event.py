# generated by datamodel-codegen:
#   filename:  model.json
#   timestamp: 2021-04-11T02:41:02+00:00

from __future__ import annotations

from datetime import date
from enum import Enum
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, Field


class Type(Enum):
    order_created = 'order.created'
    order_updated = 'order.updated'
    order_deleted = 'order.deleted'


class PaymentProcessor(Enum):
    PAYPAL = 'PAYPAL'
    STRIPE = 'STRIPE'


class User(BaseModel):
    discord_id: Optional[UUID] = None
    username: Optional[str] = None


class Type1(Enum):
    UPGRADE = 'UPGRADE'
    SHOP = 'SHOP'


class Interval(Enum):
    day = 'day'
    week = 'week'
    month = 'month'
    year = 'year'


class Type2(Enum):
    UPGRADE = 'UPGRADE'
    SHOP = 'SHOP'


class DiscordRole(BaseModel):
    discord_id: Optional[str] = None
    name: Optional[str] = None


class ProductType(Enum):
    DISCORD_ROLE = 'DISCORD_ROLE'
    SHOP_PRODUCT = 'SHOP_PRODUCT'


class Product(BaseModel):
    uuid: Optional[UUID] = None
    name: Optional[str] = None


class OrderItem(BaseModel):
    price: Optional[float] = None
    quantity: Optional[float] = None
    interval: Optional[Interval] = None
    interval_count: Optional[float] = None
    free_trial_length: Optional[float] = None
    is_time_limited: Optional[bool] = None
    type: Optional[Type2] = None
    discord_roles: Optional[List[DiscordRole]] = None
    product_types: Optional[List[ProductType]] = Field(
        None,
        description='The types of the product. A product purchased through the shop will be a shop product. All other types are upgrades.',
    )
    product: Optional[Product] = Field(None, description='An Upgrade.Chat product')


class Body(BaseModel):
    uuid: Optional[str] = None
    purchased_at: Optional[date] = None
    payment_processor: Optional[PaymentProcessor] = None
    payment_processor_record_id: Optional[str] = None
    user: Optional[User] = None
    subtotal: Optional[float] = None
    discount: Optional[float] = None
    total: Optional[float] = None
    type: Optional[Type1] = None
    is_subscription: Optional[bool] = None
    cancelled_at: Optional[date] = Field(
        None, description='The date when the subscription was cancelled'
    )
    deleted: Optional[date] = Field(
        None, description='The date when the subscription expired'
    )
    order_items: Optional[List[OrderItem]] = None


class WebhookEvent(BaseModel):
    id: Optional[UUID] = None
    webhook_id: Optional[UUID] = None
    type: Optional[Type] = None
    body: Optional[Body] = None
    attempts: Optional[float] = None


class Model(BaseModel):
    data: Optional[WebhookEvent] = Field(None)

    def __str__(self):
        return f"<Webhook Event {self.data.id}>"
