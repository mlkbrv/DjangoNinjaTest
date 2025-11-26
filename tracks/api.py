from typing import List, Optional
from ninja import NinjaAPI
from .models import Track
from .schema import TrackSchema,NotFoundSchema

api = NinjaAPI()

@api.get('/tracks',response=List[TrackSchema])
def tracks(request,title: Optional[str] = None):
    if title:
        return Track.objects.filter(title__icontains=title)
    return Track.objects.all()

@api.get("/tracks/{id}",response={200: TrackSchema,404: NotFoundSchema})
def track(request, id:int):
    try:
        track = Track.objects.get(pk=id)
        return 200, track
    except Track.DoesNotExist as e:
        return 404, {"message": str(e)}