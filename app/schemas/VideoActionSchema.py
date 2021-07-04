from app import ma


class VideoActionSchema(ma.Schema):
    class Meta:
        fields = ("id", "user_id", "device", "action", "date_actioned")

video_action_schema = VideoActionSchema()
video_actions_schema = VideoActionSchema(many=True)
