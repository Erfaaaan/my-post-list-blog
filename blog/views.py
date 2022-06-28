from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,account,comment
from django.http import HttpResponse
from .forms import *
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import  ListView
from django.core.mail import send_mail
from taggit.models import Tag


def index(request):
    return HttpResponse("welcome to Erfan Kiani's blog !")

def postlist(request,tag_slug=None):
    posts=Post.objects.filter(status='draft')
    tag=None
    if tag_slug:
        tag=Tag.objects.get(slug=tag_slug)
        posts=posts.filter(tags__in=[tag])
    paginator=Paginator(posts,1)
    page=request.GET.get('page')
    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        posts=paginator.page(1)
    except EmptyPage:
        posts=paginator.page(paginator.num_pages)
    return render(request,'blog/post/list.html', {'posts': posts, 'page': page,'tag':tag})
# class PostListView(ListView):
#     queryset = Post.objects.all()
#     context_object_name = 'posts'
#     paginate_by = 1
#     template_name = 'blog/post/list.html'


def postdetail(request,slug,pk):
    post=get_object_or_404(Post,slug=slug,id=pk)
    comments=post.comments.filter(active=True)
    new_comment=None
    if request.method=='POST':
        comment_form=commentform(request.POST)
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.post=post
            new_comment.save()
    else:
        comment_form=commentform()
    context={
        'post':post,
        'new_comment':new_comment,
        'comments':comments,
        'comment_form':comment_form
    }
    return render(request,'blog/post/detail.html',context)

def useraccount(request):
    User=request.user

    try:
        Account=account.objects.get(user=User)
    except:
        Account=account.objects.create(user=User)
    if request.method=="POST":
        form=accountform(request.POST)
        if form.is_valid():
            User.first_name=form.cleaned_data['firstname']
            User.last_name=form.cleaned_data['lastname']
            Account.sex=form.cleaned_data['sex']
            Account.age = form.cleaned_data['age']
            Account.address=form.cleaned_data['address']
            Account.phone = form.cleaned_data['phone']
            User.save()
            Account.save()
            return redirect('blog:index')
        else:
            return render(request, 'blog/form/accountform.html', {'form': form,'account':Account})
    form=accountform()
    return  render(request,'blog/form/accountform.html',{'form':form,'account':Account})





def contactus(request):
    sent=False
    if request.method=='POST':
        form=contactusform(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            name=cd['name']
            phone=cd['phone']
            email=cd['email']
            subject=cd['subject']
            message=cd['message']
            msg = 'subject : {0}\nname : {1}\nphone : {2}\nemail : {3}\n{4}'.format(subject, name, phone, email, message)
            sent=True
            send_mail(subject,msg,'erfankiani10@gmail.com',['erfankiani10@gmail.com'],fail_silently=False)
    else:
        form=contactusform()
    return render(request, 'blog/form/contactus.html', {'form':form,'sent':sent})

def share(request,post_id):
    post=get_object_or_404(Post,id=post_id)
    sent=False
    if request.method=='POST':
        form=Shareform(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            name=cd['name']
            to=cd['to']
            post_url=request.build_absolute_uri(post.get_absolute_url())
            msg = 'Hi ! Tap this link to see my post . {0}{1}'.format('\n',post_url)
            subject='my post'
            sent=True
            send_mail(subject,msg,'erfankiani10@gmail.com',[to],fail_silently=False)
    else:
        form=Shareform()
    return render(request, 'blog/form/share.html', {'form':form,'sent':sent,'post':post})
