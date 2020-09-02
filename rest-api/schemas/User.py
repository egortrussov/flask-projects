from app import ma 

class UserSchema(ma.Schema):
    class Meta:
        fields = ['id', 'username', 'password'] 

user_schema = UserSchema()
users_schema = UserSchema(many=True)