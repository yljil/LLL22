"""
URL configuration for bloge project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path  # 导入 re_path
from django.conf import settings  # 使用正确的导入方式
from django.conf.urls.static import static  # 用于静态文件服务

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('search/', include('haystack.urls'))
]

# 开发环境下处理媒体文件的服务
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
