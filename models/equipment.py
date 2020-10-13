
from mongoengine import StringField, ReferenceField, CASCADE, BooleanField
from mongoengine.document import Document

# import mongoengine_goodjson as Document

class Equipment(Document):
    name = StringField(required=True)
    code = StringField(max_length=20, required=True, unique=True)
    location = StringField(required=False)
    status = BooleanField(default=True)

    vessel = ReferenceField('Vessel', reverse_delete_rule=CASCADE,required=True)
    def to_json(self):
        return {"name": self.name,
                "code": self.code,
                "location": self.location,
                "status": self.status,
                "id": str(self.id)}