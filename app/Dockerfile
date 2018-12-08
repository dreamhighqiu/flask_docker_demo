#构建镜像的来源（Father）
FROM python:3.7.1-slim-stretch

#把当前目录添加到容器里的"/code"路径里
COPY ./ /code

#设置容器里的上下文工作目录
WORKDIR /code

#安装依赖
RUN pip install flask
RUN pip install requests
RUN pip install PyMySQL

#声明内部端口
EXPOSE 5000

#启动服务器
CMD ["python", "app.py"]