from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect, HttpResponse, Http404
from .forms import BlogPostModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils import timezone
from django.template.loader import get_template
# Create your views here.
from .models import BlogPost


def blog_post_list_view(request):
    now = timezone.now()
    obj = BlogPost.objects.all().published()
    if request.user.is_authenticated:
        my_qs = BlogPost.objects.filter(user=request.user)
        obj = (obj | my_qs).distinct()
    # obj = BlogPost.objects.all()
    # obj = BlogPost.objects.filter(publish_date__lte=now)
    # obj =  BlogPost.objects.filter(title__icontains="A")
    template_name = 'blog.html'
    context = {"object": obj}
    return render(request, template_name, context)


"""def home_page_view(request):
    # now = timezone.now()
    obj = BlogPost.objects.all().published()[:5]
    template_name = "home.html"
    context = {"home_object": obj,
               "title": "Welcome to the Home Page"}
    return render(request, template_name, context)"""


@login_required()
def blog_post_create_view(request):
    form = BlogPostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        """
        obj = form.save(commit=False)
        obj.title = form.cleaned_data.get("title") + "0"
        obj.save()
        """
        form = BlogPostModelForm()
    # print(request.title)
    template_name = "forms.html"
    context = {"my_form": form}
    return render(request, template_name, context)


"""
    try:
        BlogPost.objects.get(slug = my_slug) # (id = my_id)
    except BlogPost.DoesNotExist:
        raise Http404
"""


@login_required()
def blog_post_update_view(request, my_slug):
    # data = get_list_or_404(BlogPost, slug=my_slug)
    data = get_object_or_404(BlogPost, slug=my_slug)
    form = BlogPostModelForm(request.POST or None, instance=data)
    if form.is_valid():
        form.save()
        form = BlogPostModelForm()
    template_name = "forms.html"
    context = {"my_form": form, "object_data": data}
    return render(request, template_name, context)


def blog_post_detail_view(request, my_slug):
    obj = get_object_or_404(BlogPost, slug=my_slug)
    template_name = "detail.html"
    context = {"obj": obj}
    return render(request, template_name, context)
    # obj = get_object_or_404(BlogPost, id=my_id)
    # obj = BlogPost.objects.get(id=my_id)
    # obj = get_list_or_404(BlogPost, slug=my_slug)


@login_required()
def blog_post_delete_view(request, my_slug):
    obj = get_object_or_404(BlogPost, slug=my_slug)
    if request.method == "POST":
        obj.delete()
        return redirect('/blog/')
    template_name = "delete.html"
    context = {"delete_obj": obj}

    return render(request, template_name, context)


# ----------------------------------------------------------------- #

def contact_page_view(request):
    my_title = "Contact Page"
    context = {"title": my_title}
    return render(request, "contact.html", context)


def about_page_view(request):
    my_title = "About Page"
    context = {"title": my_title}
    return render(request, "about.html", context)


# example of how rendering works
"""
def example_page_view(request):
    # my_title = "rendered string from txt file"
    context = {"title": "rendered string from txt file"}
    template_name = "example.txt"o
    template_obj = get_template(template_name)
    template_rendering = template_obj.render(context)
    print("Example of rendered txt")
    return render(request, "example.html", {"title": template_rendering})
"""
# example of how rendering works
"""
def example_page_view(request):
    context         = {"title" : "rendered successfully"}
    something_here  = "example.html"
    template_obj    = get_template(something_here)
    return HttpResponse(template_obj.render(context))
"""
