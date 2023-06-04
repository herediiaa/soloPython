from django.shortcuts import render, redirect
from django.views.generic import View

class HomeView(View):
    def get(self,request, *args, **kwargs):
        context= {
            'nombre':"Emmanuel"
        }
        return render(request, 'index.html', context)


