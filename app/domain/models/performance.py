import datetime

from peewee import AutoField, BooleanField, DateTimeField, CharField, IntegerField
from peewee import ForeignKeyField

from app.domain.models.base import BaseModel
from app.domain.models.theater import Theater

DAY_OF_WEEK_CHOICES = [
    ('monday', 'Понедельник'),
    ('tuesday', 'Вторник'),
    ('wednesday', 'Среда'),
    ('thursday', 'Четверг'),
    ('friday', 'Пятница'),
    ('saturday', 'Суббота'),
    ('sunday', 'Воскресенье')
]

class Performance(BaseModel):
    """
        Модель объекта базы данных представления

        Attributes
        ----------
        id : AutoField
            Id представления
        theater : ForeignKeyField
            Театр, в котором будет представление
        title : CharField
            Название представления
        type : CharField
            Тип представления
        description : CharField
            Описание представления (nullable)
        age_restrictions : IntegerField
            Возрастные ограничения (nullable)
        release_at : DateTimeField
            Время начала представления
        preview_url : CharField
            Ссылка на превью (nullable)
        created_at : DateTimeField
            Время создание записи в базу данных
        is_expire : BooleanField
            Не прошло ли еще представление
        is_deleted : BooleanField
            Не удалена ли запись из базы данных
    """

    id = AutoField(primary_key=True)
    theater = ForeignKeyField(Theater)
    title = CharField()
    type = CharField()
    description = CharField(null=True)
    age_restrictions = IntegerField(null=True)
    release_at = DateTimeField()
    day_of_week = CharField(choices=DAY_OF_WEEK_CHOICES)
    preview_url = CharField(null=True)
    created_at = DateTimeField(default=datetime.datetime.now)
    is_expire = BooleanField(default=False)
    is_deleted = BooleanField(default=False)