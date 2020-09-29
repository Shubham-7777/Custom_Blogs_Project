from django.db import models
from django.conf import settings

USER = settings.AUTH_USER_MODEL


# Create your models here.


class SearchQuery(models.Model):
    query = models.CharField(max_length=100)
    user = models.ForeignKey(USER, blank=True, null=True, on_delete=models.SET_NULL)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.query

    def get_search_url(self):
        return {self.query}
