## 创建虚拟环境

```bash
python3 -m venv ll_env
```

## 激活虚拟环境

```bash
source ll_env/bin/activate
```

## 安装django

```bash
pip install django
```

## 创建项目

```bash
django-admin startproject learning_log .
```

## 创建数据库

```bash
python manage.py migrate
```

## 运行项目

```bash
python manage.py runserver
```


## 指定端口

```bash
python manage.py runserver 8001
```

```
python manage.py startapp learning_logs
```

```
python manage.py makemigrations learning_logs
```

```
python manage.py createsuperuser
```

```
python manage.py shell

>>> from learning_logs.models import Topic
>>> Topic.objects.all()
>>> topics = Topic.objects.all()
>>> for topic in topics:
...    print(topic.id, topic)

>>> t = Topic.objects.get(id=2)
>>> t.text
>>> t.date_added
>>> t.entry_set.all()

```

```
pip install black
```

```
>>> python manage.py shell
>>> from django.contrib.auth.models import User
>>> User.objects.all()
>>> for user in User.objects.all():
... 	print(user.username, user.id)

```