from django.db import models

# Create your models here.
from user.models import User
class Note(models.Model):
    title = models.CharField('标题',max_length=10)
    content = models.TextField('内容')
    created_time = models.DateTimeField('创建时间',auto_now_add=True)
    updated_time = models.DateTimeField('修改时间',auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 第二个参数保障删除时一起删
    is_active = models.BooleanField('是否活跃',default=True)