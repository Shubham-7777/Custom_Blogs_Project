from django.urls import include, path, re_path
from django.conf import settings

from .views import (blog_post_list_view,
                    blog_post_detail_view,
                    blog_post_update_view,
                    blog_post_delete_view,
                    contact_page_view,
                    about_page_view,
                    )

app_name = "my_app"

urlpatterns = [
    # path("create/", blog_post_create_view, name="blog_post_create_url"),
    path("", blog_post_list_view, name="blog_page_url"),
    path("<str:my_slug>/", blog_post_detail_view, name="blog_post_detail_url"),
    path("<slug:my_slug>/edit/", blog_post_update_view, name="blog_post_edit_url"),
    path("<slug:my_slug>/delete/", blog_post_delete_view, name="blog_post_delete_url"),

    # path("blog-create/", blog_post_create_view, name="blog_post_create_url"),
    # path("example/", views.example_page_view, name="example_page_url"),
    path("contact/", contact_page_view, name="contact_page_url"),
    path("about/", about_page_view, name="about_page_url"),

]
