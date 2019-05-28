from django.urls import path, re_path
from .views import AboutAPIView, TeamAPIView


urlpatterns = [
    re_path(r'about', AboutAPIView.as_view()),
    re_path(r'team', TeamAPIView.as_view()),
    #path('create/',StatusListSearchAPIView.as_view()),
    #re_path(r'^(?P<id>.*)/$', StatusCreateAPIVIew.as_view())
    #re_path(r'^(?P<id>.*)/update/$', StatusUpdateAPIVIew.as_view())
    #re_path(r'^(?P<id>.*)/delete/$', StatusDeleteAPIVIew.as_view())
]

'''
api/status -> List
api/status/create -> Create
api/status/12 -> Detail
api/status/12/update/ -> Update
api/status/12/delete/ -> Delete

'''