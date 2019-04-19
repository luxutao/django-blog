from django.db import models


# Create your models here.


# 基本的对象模型
class BaseManager(models.Manager):
    pass


# 标签模型
class Tag(models.Model):
    objects = BaseManager()

    showname = models.CharField(max_length=255, null=False, unique=True)
    valuename = models.CharField(max_length=255, null=False, unique=True)
    introduction = models.CharField(max_length=255)

    def __repr__(self):
        return '<Tag {0}>'.format(self.showname)


# 文章模型
class Article(models.Model):
    objects = BaseManager()

    title = models.CharField(max_length=255, db_index=True, null=False, unique=True)
    subtitle = models.CharField(max_length=255, db_index=True, null=True)
    content = models.TextField()
    views = models.IntegerField(default=0)
    publish_time = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    tag = models.ManyToManyField(to=Tag, related_name='%(app_label)s_%(class)s_related')

    def __repr__(self):
        return '<Article {0}>'.format(self.title)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.subtitle:
            self.subtitle = self.title
        return super(Article, self).save(force_insert, force_update, using, update_fields)


# 评论模型
class Comment(models.Model):
    objects = BaseManager()

    floor = models.IntegerField()
    email = models.EmailField()
    name = models.CharField(max_length=255)
    content = models.TextField()
    comment_time = models.DateTimeField(auto_now=True)
    avatar_url = models.URLField(max_length=255)
    article = models.ForeignKey(to=Article, to_field='id', related_name='%(app_label)s_%(class)s_related',
                                on_delete=models.CASCADE)

    def __repr__(self):
        return '<Comment {0}>'.format(self.email)


# 插图模型
class Illustration(models.Model):
    objects = BaseManager()

    file = models.ImageField(upload_to='illustration/%Y/%m/%d/')
    insert_time = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return '<Illustration {0}>'.format(self.file.name)
