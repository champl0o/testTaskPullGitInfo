from django.db import models


class GitHubUserRepoModel(models.Model):
    repo_name = models.CharField(max_length=100)

    def __str__(self):
        return self.repo_name

class GitHubUserModel(models.Model):
    name = models.CharField(max_length=30)
    repos = models.ForeignKey(GitHubUserRepoModel, on_delete=models.CASCADE)
