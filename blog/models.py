from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
#分类
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
#标签
class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

#文章
class Post(models.Model):
    title = models.CharField(max_length=100)
    #正文
    boby = models.TextField()
    #创建时间
    created_time = models.DateTimeField()
    #修改时间
    modified_time = models.DateTimeField()
    #文章摘要
    excperpt = models.CharField(max_length=100)
    #分类外键
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    #标签外键多对多
    tags = models.ManyToManyField(Tag, blank=True)
    #作者外键
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
