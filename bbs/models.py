from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# 継承元は（）の中に！
class Article(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # 投稿したら自動で詳細に飛んでくれるやーつ！
    def get_absolute_url(self):
        return reverse("bbs:detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.content
# Create your models here.
