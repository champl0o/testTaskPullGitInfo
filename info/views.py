import requests
from django.shortcuts import render

def getGitHubUserInfo(request):
    user_info = {}

    if request.method == 'GET':
        username = request.GET.get('user')

        req = requests.get('https://api.github.com/users/' + username)
        if req.status_code == 200:
            json_list = req.json()
            name = json_list['name']
            user_info['name'] = name

            req = requests.get('https://api.github.com/users/' + username + '/repos')
            json_list = req.json()

            user_info['repos'] = []
            for info in json_list:
                user_info['repos'].append(info['name'])

    return render(request, 'results.html', {'data': user_info})