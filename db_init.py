import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

'''
Django 版本大于等于1.7的时候，需要加上下面两句
import django
django.setup()
否则会抛出错误 django.core.exceptions.AppRegistryNotReady: Models aren't loaded yet.
'''

import django

if django.VERSION >= (1, 7):  # 自动判断版本
    django.setup()


def main():
    from playtogether.models import BilliardsUser
    f = open('oldblog.txt')
    for line in f:
        title, content = line.split('****')
        BilliardsUser.objects.get_or_create(title=title, content=content)  #不会重复导入
    f.close()


if __name__ == "__main__":
    main()
    print('Done!')

# import os
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
# 
#
# def main():
#     from blog.models import Blog
#     f = open('oldblog.txt')
#     BlogList = []
#     for line in f:
#         title, content = line.split('****')
#         blog = Blog(title=title, content=content)
#         BlogList.append(blog)
#     f.close()
#
#     Blog.objects.bulk_create(BlogList)
#
#
# if __name__ == "__main__":
#     main()
#     print('Done!')