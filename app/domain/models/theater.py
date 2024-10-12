import datetime

from peewee import AutoField, CharField, BooleanField, DateTimeField

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
    id = AutoField(primary_key=True)
    title = CharField()
    description = CharField(null=True)
    site_url = CharField(null=True)
    scrap_url = CharField()
    image_url = CharField(null=True)
    address = CharField(null=True)
    contact_phone = CharField(null=True)
    created_at = DateTimeField(default=datetime.datetime.now)
    is_deleted = BooleanField(default=False)

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