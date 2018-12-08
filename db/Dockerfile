FROM mysql:5.6.40

#设置时区
ARG TZ=Asia/Shanghai
ENV TZ ${TZ}
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

#授权容器内mysql用户
RUN chown -R mysql:root /var/lib/mysql/

#初始化数据
COPY ./docker-entrypoint-initdb.d /docker-entrypoint-initdb.d/


EXPOSE 3306

CMD ["mysqld"]