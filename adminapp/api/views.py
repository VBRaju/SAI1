from rest_framework import generics,mixins
from rest_framework.views import View
from rest_framework.response import Response
from adminapp.models import About_Us, Team_Members
from .serializers import AboutSerializer, TeamSerializer
from django.shortcuts import get_object_or_404
import json

# CreateModelMixin :: POST method
# UpdateModelMixin :: Put method
# DestroyModelMixin:: Delete method


def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except  ValueError:
        is_valid = False
    return is_valid

# About API

class AboutAPIView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin, 
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.ListAPIView):
    permission_classes      = []
    authentication_classes  = []
    serializer_class        = AboutSerializer
    passed_id               = None

    def get_queryset(self):
        request = self.request
        qs = About_Us.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(content=query)
        return qs

    def get_object(self):
        request     =   self.request
        passed_id   =   request.GET.get('id', None) or self.passed_id
        queryset    =   self.get_queryset()
        obj         =   None
        if passed_id is None:
            obj = get_object_or_404(queryset, id=passed_id)
            self.check_object_permissions(request,obj)
        return obj

    def perform_destroy(self, instance):
        if instance is not None:
            return  instance.delete()
        return None
            

    def get(self, request, *args, **kwargs):
        url_passed_id   =   request.GET.get('id', None)
        data            =   {}
        body_           = request.body
        if is_json(body_):
            data            =   json.loads(request.body)
        new_passed_id   =   data.get('id',None)
        # print(request.body)
        passed_id       =   url_passed_id or new_passed_id or None   
        self.passed_id  =   passed_id
        if passed_id is not None:
            return self.retrieve(request, *args, **kwargs)
        return super().get(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        url_passed_id   =   request.GET.get('id', None)
        data            =   {}
        body_           = request.body
        if is_json(body_):
            data            =   json.loads(request.body)
        new_passed_id   =   data.get('id',None)
        # print(request.body)
        passed_id       =   url_passed_id or new_passed_id or None
        self.passed_id  =   passed_id
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        url_passed_id   =   request.GET.get('id', None)
        data            =   {}
        body_           = request.body
        if is_json(body_):
            data            =   json.loads(request.body)
        new_passed_id   =   data.get('id',None)
        # print(request.body)
        passed_id       =   url_passed_id or new_passed_id or None
        self.passed_id  =   passed_id
        return self.update(request,*args, **kwargs)

    def delete(self, request, *args, **kwargs):
        url_passed_id   =   request.GET.get('id', None)
        data            =   {}
        body_           = request.body
        if is_json(body_):
            data            =   json.loads(request.body)
        new_passed_id   =   data.get('id',None)
        # print(request.body)
        passed_id       =   url_passed_id or new_passed_id or None
        self.passed_id  =   passed_id
        return self.destroy(request, *args, **kwargs)

# Team API
class TeamAPIView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin, 
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.ListAPIView):
    permission_classes      = []
    authentication_classes  = []
    serializer_class        = TeamSerializer
    passed_id               = None

    def get_queryset(self):
        request = self.request
        qs = Team_Members.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(content=query)
        return qs

    def get_object(self):
        request     =   self.request
        passed_id   =   request.GET.get('id', None) or self.passed_id
        queryset    =   self.get_queryset()
        obj         =   None
        if passed_id is None:
            obj = get_object_or_404(queryset, id=passed_id)
            self.check_object_permissions(request,obj)
        return obj

    def perform_destroy(self, instance):
        if instance is not None:
            return  instance.delete()
        return None
            

    def get(self, request, *args, **kwargs):
        url_passed_id   =   request.GET.get('id', None)
        data            =   {}
        body_           = request.body
        if is_json(body_):
            data            =   json.loads(request.body)
        new_passed_id   =   data.get('id',None)
        # print(request.body)
        passed_id       =   url_passed_id or new_passed_id or None   
        self.passed_id  =   passed_id
        if passed_id is not None:
            return self.retrieve(request, *args, **kwargs)
        return super().get(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        url_passed_id   =   request.GET.get('id', None)
        data            =   {}
        body_           = request.body
        if is_json(body_):
            data            =   json.loads(request.body)
        new_passed_id   =   data.get('id',None)
        # print(request.body)
        passed_id       =   url_passed_id or new_passed_id or None
        self.passed_id  =   passed_id
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        url_passed_id   =   request.GET.get('id', None)
        data            =   {}
        body_           = request.body
        if is_json(body_):
            data            =   json.loads(request.body)
        new_passed_id   =   data.get('id',None)
        # print(request.body)
        passed_id       =   url_passed_id or new_passed_id or None
        self.passed_id  =   passed_id
        return self.update(request,*args, **kwargs)

    def delete(self, request, *args, **kwargs):
        url_passed_id   =   request.GET.get('id', None)
        data            =   {}
        body_           = request.body
        if is_json(body_):
            data            =   json.loads(request.body)
        new_passed_id   =   data.get('id',None)
        # print(request.body)
        passed_id       =   url_passed_id or new_passed_id or None
        self.passed_id  =   passed_id
        return self.destroy(request, *args, **kwargs)

