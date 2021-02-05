import requests

from django.shortcuts import render

from .models import GitHubUserModel, GitHubUserRepoModel

def getGitHubUserInfo(request):
    userInfo = {}

    if request.method == 'GET':
        username = request.GET.get('user')

        req = requests.get('https://api.github.com/users/' + username)
        jsonList = req.json()
        name = jsonList['name']
        userInfo['name'] = name

        req = requests.get('https://api.github.com/users/' + username + '/repos')
        jsonList = req.json()

        userInfo['repos'] = []
        for info in jsonList:
            userInfo['repos'].append(info['name'])

    return render(request, 'results.html', {'data': userInfo})
