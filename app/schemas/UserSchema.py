from app import ma


class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "first_name", "last_name", "created_at", "updated_at", "deleted_at")

user_schema = UserSchema()
users_schema = UserSchema(many=True)
