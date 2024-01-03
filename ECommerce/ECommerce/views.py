from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html',{
        'message': 'Listado de productos',
        'title':'D´Mare',
        'products':[
            {'title':'playera','price':5,'stock':True},
            {'title':'playera2','price':15,'stock':True},
            {'title':'playera3','price':20,'stock':False}
        ]
    })