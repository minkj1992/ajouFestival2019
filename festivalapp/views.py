from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post, Comment, Pub
from django.urls import reverse_lazy
from .forms import PubForm
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os


# Create your views here.
def home(request):
    return render(request, 'home.html')

def programmerintro(request):
    return render(request, 'programmerintro.html')

# def pubintro(request):
#     pubs = Pub.objects.all()
#     return render(request, 'pubintro.html',{'pubs':pubs})
def pubintro(request,pk):
    if pk==1:
        pubs = Pub.objects.filter(date1=1)
    elif pk==2:
        pubs = Pub.objects.filter(date2=1)
    else:
        pubs = Pub.objects.filter(date3=1)
    return render(request, 'pubintro.html',{'pubs':pubs})

# class pubList(ListView):
#     model = Pub
#     templates = './pubintro.html'


def shareboard(request):
    # posts = Post.objects.all()
    posts = Post.objects.order_by('-id')
    return render(request, 'board_list.html',{'posts' : posts})

def newboard(request):
    if request.method == "GET":
        return render(request, 'board_create.html')
    else:
                
        new_post = Post()
        new_post.title = request.POST['title']
        new_post.owner_name = request.POST['owner_name']
        new_post.contents = request.POST['contents']
        new_post.owner_pwd = request.POST['owner_pwd']
        # a=request.POST['picture']
        # a=request.POST
        # a=request.POST['csrfmiddlewaretoken']
        # a=request.POST.get('picture', '')
        # a=type(request.FILES)
        # new_post.image = request.FILES

        # a="asd"
        new_post.save()
        a=request.FILES['picture']
        os.makedirs(("static/userimage/user"+str(new_post.id)))
        new_post.image_url = "userimage/user"+str(new_post.id)+"/"+a.name
        fs=FileSystemStorage()
        fn=fs.save("user"+str(new_post.id)+"/"+a.name,a)

        # a=fs.url(fn)
        # new_post.image_url = a
        
        new_post.save()

        posts = Post.objects.all()
    # return render(request, 'post_list.html',{'posts' : posts})
        return redirect('shareboard')

def finishboard(request, pk):
    if request.method == "GET":
        return render(request, 'board_password.html')
    else:
        post = Post.objects.get(id=pk)
        if post.owner_pwd == request.POST['input_pwd']:
            post.is_finish = 1
            post.save()
        
        return redirect('shareboard')

def detailboard(request):
    return render(request, 'board_detail.html')

# def writingarea(request):
#     if request.method == 'POST': # POST형식으로 값이 들어왔을때만 url에 접근 가능
#         form = PubForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('pubintro')
#     else: 
#         form = PubForm()
#         return render(request, 'writingarea.html',{'form':form})

def writingarea(request):
    if request.method == 'GET': # POST형식으로 값이 들어왔을때만 url에 접근 가능
        
        return render(request, 'writingarea.html')
        
    else:
        pub=Pub()
        pub.name=request.POST['name']
        pub.description=request.POST['description']
        pub.section=request.POST['section']
        pub.location=request.POST['location']
        pub.time=request.POST['time']
        try:
            pub.date1=request.POST['date1']
        except:
            pass
        try:
            pub.date2=request.POST['date2']
        except:
            pass
        try:
            pub.date3=request.POST['date3']
        except:
            pass

        pub.save()

        a=request.FILES['picture']
        os.makedirs(("static/userimage/booth"+str(pub.id)))
        pub.image_booth = "userimage/booth"+str(pub.id)+"/"+a.name
        fs=FileSystemStorage()
        fn=fs.save("booth"+str(pub.id)+"/"+a.name,a)

        pub.save()
        return redirect('pubintro', pk=1)
        

def writingcheck(request):
    if request.method == 'POST': # POST형식으로 값이 들어왔을때만 url에 접근 가능
        post_pw = request.POST['post_pw'].strip()
        if post_pw == 'ajou2019festival' :
            return redirect('writingarea')
        else : # 비밀번호가 틀린 경우
            return redirect('writingpw')
    else: # POST값 없이 url을 통해 접근을 시도한경우
        return redirect('writingpw')

def writingpw(request):
    return render(request, 'writingpw.html')
