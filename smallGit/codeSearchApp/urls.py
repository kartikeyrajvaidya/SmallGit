
from django.urls import path
from . import views

app_name = "codeSearchApp"
urlpatterns = [
    path('',views.HomePage.as_view(),name='codeSearchHome'),
    path('storesearch/', views.SearchHistoryList.as_view(), name="store_search"),
    path('search/users/<str:query>', views.get_user_from_git, name="get_user_data"),
    path('search/repositories/<str:query>', views.get_repositories_from_git, name="get_repositories_data"),
]
