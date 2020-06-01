from django.shortcuts import render
from .models import Post
from django.http import HttpResponse, JsonResponse
import json
from django.forms.models import model_to_dict


# Create your views here.
def blog_list(request):
    post = Post.objects.all()
    context = {
        'blog_list': post
    }
    return render(request, "blog/blog_list.html", context)
    #return JsonResponse([1,2,3], safe=False )#HttpResponse( "This is a test!")

def home(request):
    return JsonResponse([1,2,3], safe=False )