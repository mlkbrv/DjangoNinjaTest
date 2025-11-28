from datetime import datetime
from ninja import Schema, ModelSchema
from tracks.models import Track
from ninja.orm import create_schema


# class TrackSchema(Schema):
#     title : str
#     artist : str
#     duration : float
#     last_play : datetime

TrackSchema = create_schema(Track,fields = [
            'title',
            'artist',
            'duration',
            'last_play'
        ])

# class TrackSchema(ModelSchema):
#     class Meta:
#         model = Track
#         fields = [
#             'title',
#             'artist',
#             'duration',
#             'last_play'
#         ]

class NotFoundSchema(Schema):
    message : str