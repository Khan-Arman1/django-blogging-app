from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Blogs, BlogReview
from .forms import BlogsForm, RegisterUser, BlogReviewForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q # for multiple search query

# Create your views here.
def bloghome(request):
    blogs = Blogs.objects.all().order_by('-blog_upload')
    return render(request, 'blog_list.html',{'blogs':blogs})

@login_required
def create_blog(request):
    if request.method == "POST":
        form = BlogsForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            form.save()
            return redirect('bloghome')
    else:
        form = BlogsForm()

    return render(request, 'create_blog.html',{'form':form})


@login_required
def edit_blog(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id, user = request.user)
    if request.method == "POST":
        form = BlogsForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            form.save()
            return redirect('bloghome')
    else:
        form = BlogsForm(instance=blog)
    return render(request, 'create_blog.html', {'form':form})

@login_required
def delete_blog(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id, user= request.user)
    if request.method == 'POST':
        blog.delete()
        return redirect('bloghome')
    else: return render(request, 'dlt_blog.html', {'blog': blog})


def blog_detials(request, blog_id):
    blog = get_object_or_404(Blogs, pk = blog_id)
    # print(blog)
    reviews = None
    # @login_required
    if request.method == 'POST':
        form = BlogReviewForm(request.POST)
        print(form)
        if form.is_valid():
            reviewform = form.save(commit=False)
            # making relation ship that this comment is for this blog
            reviewform.r_blog = blog
            form.save(commit=True)
            return redirect('blog_detials' , blog_id = blog.id)
    else: 
        form = BlogReviewForm()
        reviews = BlogReview.objects.all().order_by('-r_date')#.filter(r_blog = blog).order_by('-r_date') 
        # print(reviews)
    return render(request, 'blog_detials.html', {'blog': blog, 'reviewform': form, 'reviews': reviews})



def delete_comment(request, comment_id):
    blogr = get_object_or_404(BlogReview, pk=comment_id)
    print(comment_id)
    print(blogr.r_blog.id)
    print(blogr)
    blogr.delete()
    return redirect('blog_detials', blog_id = blogr.r_blog.id)
    # else:
    #     return redirect('blog_detials', blog_id = comment_id)



def register(request):
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterUser()
    return render(request, 'registration/register.html', {'form':form})


def search(request):
    try:
        if request.method == "GET":
            query = request.GET.get('q')
            form = Blogs.objects.all()
            if query:
                blog = form.filter(Q(blog_title__icontains = query) | Q(blog_text__icontains = query) | Q(user__username__icontains = query))
                return render(request, 'search.html', {'blog':blog})
    except:
        return HttpResponse("<h1>Please enter a valid search querry.</h1>")
    else:
        blog = Blogs.objects.all()
        return render(request, 'search.html', {'blog': blog})
    
@login_required
def dashboard(request):
    blogs = Blogs.objects.all().order_by('-blog_upload')
    return render(request, 'dashboard/dashboard.html', {'blogs':blogs})
