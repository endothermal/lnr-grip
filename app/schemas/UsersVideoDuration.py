from app import ma


class UsersVideoDurationSchema(ma.Schema):
    class Meta:
        fields = ("user_id", "total_duration")

users_video_duration_schema = UsersVideoDurationSchema()
users_video_durations_schema = UsersVideoDurationSchema(many=True)
