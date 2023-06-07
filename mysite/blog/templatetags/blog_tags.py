from django import template
from django.utils.safestring import mark_safe  # 将结果标记为安全的HTML
import markdown
from django.db.models import Count
from ..models import Post

register = template.Library()  # 模板标签需要定义register作为有效的标签库

@register.simple_tag  # 简单标签，处理数据返回字符串
def total_posts():    # 默认使用函数名作为标签名
    return Post.published.count()


@register.inclusion_tag('blog/post/latest_posts.html')  # 处理数据返回显示的模板
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}

@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))