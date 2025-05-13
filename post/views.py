from django.db.models.functions import math
from django.shortcuts import render, redirect
from django.views import View
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class IndexView(View):
    def get(self, request, num=1):
        try:
            num = int(num)
        except ValueError:
            num = 1

        postList = Post.objects.all().order_by('-created')
        paginator = Paginator(postList, 1)

        try:
            page_obj = paginator.page(num)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)

        # 传递 page_obj.object_list 作为 postList
        return render(request, 'index.html', {'postList': page_obj.object_list, 'page_obj': page_obj})

class DetailView(View):
    def get(self, request, postid):
        postid = int(postid)
        post_obj = Post.objects.get(id=postid)

        return render(request,'detail.html',{"post_obj":post_obj})


def getPostByCid(request, cid):
    cid = int(cid)
    c_post = Post.objects.filter(category_id=cid)
    return render(request,'postlist.html',{"c_post":c_post})


def getPostByCreated(request,year=1,month=1):
    if year == 1 and month == 1:
        c_post = Post.objects.all().order_by('-created')
    else:
        c_post = Post.objects.filter(created__year=year,created__month=month)

    return render(request, 'postlist.html', {"c_post": c_post})

