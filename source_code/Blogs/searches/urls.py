"""
from django.urls import include, path
from . import views

url_patterns = [
    path("search/", views.search_view, name="search_url")

]
"""