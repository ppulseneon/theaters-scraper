import datetime

from peewee import AutoField, CharField, BooleanField, DateTimeField
from peewee_enum_field import EnumField

from app.enums.scrap_type import ScrapTypes
from app.domain.models.base import BaseModel

class Theater(BaseModel):
    """
        Модель объекта базы данных театра

        Attributes
        ----------
        id : AutoField
            Id театра
        title : CharField
            Название театра
        description : CharField
            Описание театра (nullable)
        site_url : CharField
            Ссылка на главный сайт (nullable)
        scrap_url : CharField
            Ссылка на страницу для скрапа
        image_url : CharField
            Ссылка на изображение театра (nullable)
        address : CharField
            Адрес театра (nullable)
        contact_phone : CharField
            Контактный номер телефона (nullable)
        created_at : DateTimeField
            Дата добавления театра
        is_deleted : BooleanField
            Не удален ли театр из базы
    """

    id: AutoField = AutoField(primary_key=True)
    title: CharField = CharField()
    description: CharField = CharField(null=True)
    site_url: CharField = CharField(null=True)
    scrap_url: CharField = CharField()
    scrap_type: EnumField = EnumField(ScrapTypes)
    image_url: CharField = CharField(null=True)
    address: CharField = CharField(null=True)
    contact_phone: CharField = CharField(null=True)
    created_at: DateTimeField = DateTimeField(default=datetime.datetime.now)
    is_deleted: BooleanField = BooleanField(default=False)

    @staticmethod
    def to_response_list(theaters: list['Theater']) -> list[dict]:
        return [Theater.to_response(theater) for theater in theaters]

    @staticmethod
    def to_response(theater) -> dict:
        return {
            'id': theater.id,
            'title': theater.title,
            'description': theater.description,
            'site_url': theater.site_url,
            'image_url': theater.image_url,
            'address': theater.address,
            'contact_phone': theater.contact_phone,
        }