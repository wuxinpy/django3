# 虚拟环境
python -m -venv name

# 激活环境
source name/bin/activate

# git 基本操作
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/wuxinpy/django3.git
git push -u origin main

# django操纵
创建项目
django-admin startproject name
本地语言中间件
django.middleware.locale.LocaleMiddleware 

可自定义主机端口设置文件
python manage.py runserver 127.0.0.1:8001 \--settings=mysite.settings

针对某个项目做数据迁移
python manage.py makemigrations blog

查看迁移过程中的SQL代码
python manage.py sqlmigrate blog 0001

启动开发服务器
python manage.py shell


# handle error
处理站点地图的时候遇到了这个问题
maps = sitemaps.values() 'function' object has no attribute 'values'


# postgres数据库
psql -U postgres
口令是 root

# wsl安装redis
wsl --install
sudo apt-add-repository ppa:redislabs/redis
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install redis-server
sudo service redis-server start
redis-cli



python manage.py runserver_plus --cert-file cert.crt
