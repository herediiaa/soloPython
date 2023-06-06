from django.shortcuts import redirect, render
from django.views.generic import View
from .forms import PostCreateForm
from .models import Post

# Create your views here.
class BlogListView(View):
    def get(self,request, *args, **kwargs):
        context = {
        'nombre':"Emmanuel"
        }
        return render(request,'blog_list.html',context )
    
class BlogCreateView(View):
    def get(self,request,*args,**kwargs):
        if request.method=='GET':
            print("ds")
        
        form=PostCreateForm() #inicializo el formulario
        context={
            'form':form #le paso los campos que renderiza el formulario
        }
        return render(request, 'blog_create.html', context)
    
    def post(self,request,*args,**kwargs):
        if request.method=='POST': #si se pide un POST a esta vista
            form=PostCreateForm(request.POST) #
            if form.is_valid(): #valido de que los datos ingresado sean los especificados en el modelo
                title = form.cleaned_data.get('title')
                description = form.cleaned_data.get('description')
                p, created = Post.objects.get_or_create(title=title,description=description)
                p.save()
                return redirect('blog:home')
        context={}
        return render(request, 'blog_create.html', context)