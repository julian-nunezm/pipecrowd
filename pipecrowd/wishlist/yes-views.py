from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Prospect
from django.views.generic import TemplateView
from django.forms.models import model_to_dict
import json
from django.views.decorators.csrf import csrf_exempt    # ToDo: Remove it
from google.cloud import storage    # Test
from tools import email

# Create your views here.
class Prospect_List(TemplateView):
    def get_all(request):
        prospects = Prospect.objects.all()
        wishlist = dict()
        init = []
        for prospect in prospects:
            detail = dict()
            detail['first_name'] = prospect.first_name
            detail['last_name'] = prospect.last_name
            detail['email'] = prospect.email
            detail['type'] = prospect.type
            detail['brief'] = prospect.brief
            detail['confirmed'] = prospect.confirmed
            init.append(detail)
        wishlist["results"] = init
        # ToDo Make model_to_dict works
        #wishlist = dict()
        #wishlist['result'] = 'Test'

        
        storage_client = storage.Client() # Test
        buckets =  list(storage_client.list_buckets()) # Test
        print(buckets) # Test

        return JsonResponse(wishlist, safe = True)
    
    @csrf_exempt
    def register_beta(request):
        new_user = json.loads(request.body)
        print(new_user)
        user_first_name = new_user.get('first_name', '')
        user_last_name = new_user.get('last_name', '')
        user_name = user_first_name + ' ' + user_last_name
        user_email = new_user.get('email', '')
        user_type = new_user.get('type', '')
        user_brief = new_user.get('brief', '')
        if ('' in [user_first_name, user_last_name, user_email, user_type]):
            return HttpResponse(IOError)
        user = Prospect (first_name=user_first_name, last_name=user_last_name, email=user_email, type=user_type, brief=user_brief)
        user.save()
        print('User created!')
        print('Sending email...')
        email.send_confirmation_email(user_email, user_name)
        print('Email sent!')
        return HttpResponse("")