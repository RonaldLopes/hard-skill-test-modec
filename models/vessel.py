from mongoengine import StringField

from mongoengine.document import Document

class Vessel(Document):
    code = StringField(max_length=10, required=True, unique=True)
    def to_json(self):
        return {"code": self.code, "id": str(self.id)}