## 项目信息
django + vue 前后端分离开发

根据课程进行代码编写, 希望能把这个项目搞通通

## 配置注意事项
django 配置xadmin需要绕过的坑坑
[link](https://blog.51cto.com/xvjunjie/2235370)

## django 根据model自动生成mysql表的操作
    注意点: 
        1. 如果从其他地方拷贝的代码, migrations 类里面dependencies = [    ]可能会用到没有的文件导致报错
        
        
## 本地superuser
可以执行在manage.py运行时运行命令createsuperuser, 给xadmin创建一个用户
前端代码在[link](https://github.com/Lysander686/vueDjangoShop-fr), 因为django makemigrations命令遇到node_modules 会卡住, 有没有朋友可以指教一下 怎么让manage.py不检测node_modules 这个文件夹