from django.db.models import Count
from django.db import connection
from django.db.models.functions import TruncMonth

from .models import *

def getRightInfo(request):
    #分类
    r_cate_post = Post.objects.values('category__cname','category').annotate(c=Count('*')).order_by('-c')

    #近期文章
    r_recent_post = Post.objects.order_by('-created')[:3]

    cursor = connection.cursor()
    filepost = Post.objects.annotate(month=TruncMonth('created')).values('month').annotate(count=Count('id')).order_by(
        '-count')
    r_file_post = list(filepost)

    # print(r_file_post)
    return {"r_cate_post": r_cate_post, "r_recent_post":r_recent_post, "r_file_post":r_file_post}