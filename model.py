import datetime as dt
from marshmallow import Schema, fields , ValidationError
from pprint import pprint

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.created_at = dt.datetime.now()

    def __repr__(self):
        return "<User(name={self.name!r})>".format(self=self)

class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()

user = User(name="chithra",email="chi@gmail.com")
schema = UserSchema()
result = schema.dump(user)
print(result)

json_result = schema.dumps(user)
pprint(json_result)

user_data = {
    "name" : "lekha",
    "email" : "abc@gmail.com",
    "created_at" : "2021-12-03T16:30:26.988686"
}

result = schema.load(user_data)
print(result)

try:
    result = UserSchema().load({"name": "John", "email": "foo"})
except ValidationError as err:
    print(err.messages)  
    print(err.valid_data) 
