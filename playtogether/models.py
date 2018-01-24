from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from django.contrib.auth.models import User

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

SKILL_LEVEL = (('职业','职业'), ('业余顶级','业余顶级'), ('一般水平','一般水平'), ('新手','新手'))

#用户
class BilliardsUser(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.EmailField()  #邮箱
    telephone = models.CharField(max_length=32)  #手机号
    created = models.DateTimeField(auto_now_add=True)  #用户创建时间
    level = models.CharField(choices=SKILL_LEVEL, default=("一般水平","一般水平"),max_length=32)  # 实力分级
    location = models.CharField(default="shanghai",max_length=32)  # 用户所在地
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    signature = models.CharField(max_length=128,default="新人驾到") #说点什么吧，让大家认识你
    headshow = models.ImageField(upload_to="upload_imgs/", default="upload_imgs/user0.png") #头像

    class Meta:
        ordering = ('created',)  # order method

    def __str__(self):
        return self.user.username  # print username
#创建的邀请
class BilliardsInvite(models.Model):  # 桌球约单
    id = models.IntegerField(primary_key=True)  # 主键 约单序号
    created = models.DateTimeField(auto_now_add=True)  # 邀请发布的时间
    play_time = models.DateTimeField()  # 打球时间
    play_location = models.CharField(max_length=32)  # 打球场馆
    play_type = models.CharField(max_length=32) #玩法类型 特定类型 后期补充
    description = models.CharField(default="附近的球友一起来玩啦",max_length=32) #说点什么让大家更乐意一起
    total_number = models.IntegerField(default=2) #球友数量,发布人决定 ，至少 2人
    currentuser_number = models.IntegerField(default=1) #初始为1，不能超过 total_number
    create_user = models.ForeignKey(BilliardsUser, on_delete=models.CASCADE)  # 发布人 belong to
#每个邀请参与人员
class BilliardsJoin(models.Model):
    id = models.IntegerField(primary_key=True)
    invite = models.ManyToManyField(BilliardsInvite)   # 参与人 每人可以参加多个邀请，每个邀请可以有多个人
    user = models.OneToOneField(BilliardsUser, on_delete=models.CASCADE)   #对应的人

#-----------------
##参考

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = models.ForeignKey('auth.User', related_name='playtogether', on_delete=models.CASCADE)
    highlighted = models.TextField()

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)
