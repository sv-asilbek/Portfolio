from django.db import models


# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=212)
    image = models.ImageField(upload_to='author', null=True, blank=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=212)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=212)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post', null=True, blank=True)
    profession = models.CharField(max_length=212)
    description = models.TextField()
    tag = models.ManyToManyField(Tag)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=212)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Resume(models.Model):
    image = models.ImageField(upload_to='resume', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
