from django.db import models
from user.models import User

class Note(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField('标题',max_length=100)
    content=models.TextField('内容')
    created_time=models.DateTimeField('更新时间',auto_now_add=True)
    updata_time=models.DateTimeField('更新时间',auto_now=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        db_table='note'
        verbose_name_plural='笔记'