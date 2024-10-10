import datetime

from peewee import AutoField, CharField, BooleanField, DateTimeField

from app.domain.models.base import BaseModel


class Theater(BaseModel):
    """
        Модель объекта базы данных театра
    """
    id = AutoField(primary_key=True)
    title = CharField()
    description = CharField(null=True)
    site_url = CharField(null=True)
    scrap_url = CharField()
    address = CharField(null=True)
    mobile_phone = CharField(null=True)
    created_at = DateTimeField(default=datetime.datetime.now)
    is_deleted = BooleanField(default=False)