# 安装
pip2 install supervisor

# 配置文件
echo_supervisord_conf > /etc/supervisord.conf
mkdir /etc/supervisor.d
在 supervisord.conf最后添加：
[include]
files = supervisor.d/*.conf

# 拷贝config文件
cp mcelery/celery.conf /etc/supervisor.d/

# 启动supervisor服务（如果已启动勿理会）
supervisord

# 变更配置文件之后,要加载最新的配置文件
supervisorctl update

# 查看celery状态，是否正常启动
supervisorctl status

# 如果有必要，重启celery
supervisorctl restart celery

