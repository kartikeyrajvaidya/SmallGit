from django.db import models
from django.contrib.auth.models import User


class SearchHistory(models.Model):

    search_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    search_category = models.CharField(max_length=200)
    search_query = models.CharField(max_length=200)

    def __str__(self):
        return self.search_query
