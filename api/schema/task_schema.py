from flask_marshmallow import Schema
from marshmallow.fields import Str, Int, Bool


class TaskSchema(Schema):
    class Meta:
        # Fields to expose
        fields = ["user_id", "id", "title", "completed"]

    user_id = Int()
    id = Int()
    title = Str()
    completed = Bool()
