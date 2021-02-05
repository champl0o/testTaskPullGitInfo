from django.urls import path, include

from .views import getGitHubUserInfo

urlpatterns = [
    path('', getGitHubUserInfo, name='results'),

]
