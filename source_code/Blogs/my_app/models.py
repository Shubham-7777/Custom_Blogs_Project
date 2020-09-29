from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

User = settings.AUTH_USER_MODEL

"""class BlogPostManager(models.Manager):
    def published(self):
        now = timezone.now()
        return self.get_queryset().filter(publish_date__lte=now)
"""


class BlogPostQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(publish_date__lte=now)

    def search(self, query):
        return self.filter(title__icontains=query)


class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self.db)

    def published(self):
        return self.get_queryset().published()

    def search(self, query):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().published().search(query)


class BlogPost(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    # content_id = models.TextField(unique=True
    content = models.TextField(null=True, blank=True)
    publish_date = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = BlogPostManager()

    class Meta:
        ordering = ["-publish_date", "-updated", "-time_stamp"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f" /blog/{self.slug}/"
        # return f"/my_app/{self.slug}/"

    def get_edit_url(self):
        return f" /blog/{self.slug}/edit/"
        # return f"{self.get_absolute_url()}/edit/"

    # return f"edit/"""

    def get_delete_url(self):
        return f" /blog/{self.slug}/delete/"
    # return f"{self.get_absolute_url()}/delete/"
