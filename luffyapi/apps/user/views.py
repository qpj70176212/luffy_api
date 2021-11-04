from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    print(request.method)  # OPTIONS
    res = HttpResponse('hello world')
    # res['Access-Control-Allow-Origin'] = 'http://192.168.19.244:8080'
    # res['Access-Control-Allow-Origin'] = '*'

    # if request.method == 'OPTIONS':
    #     res['Access-Control-Allow-Methods'] = '*'
    #     res['Access-Control-Allow-Origin'] = '*'
    #     res['Access-Control-Allow-Headers'] = '*'
    return res