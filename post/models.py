from django.db import models

# Create your models here.
class Category(models.Model):
    cname = models.CharField(max_length=30, unique=True, verbose_name='类别名称')

    def __str__(self):
        return f'<Category:{self.cname}>'

    class Meta:
        db_table = 't_category'
        verbose_name = u'类别'

class Tag(models.Model):
    tname = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f'<Tag:{self.tname}>'

    class Meta:
        db_table = 't_tag'
        verbose_name = u'标签'



from ckeditor_uploader.fields import RichTextUploadingField
class Post(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='标题')
    desc = models.CharField(max_length=200,verbose_name='简介')
    content = RichTextUploadingField(verbose_name='内容')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    isdelete = models.BooleanField(default=False, verbose_name='是否删除')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='所属内容')
    tag = models.ManyToManyField(Tag, verbose_name='所属标签')

    def __str__(self):
        return f'<Post:{self.title}>'

    class Meta:
        db_table = 't_post'
        verbose_name = u'帖子'



