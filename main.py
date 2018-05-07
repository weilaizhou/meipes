from flask import Flask
from config import DevConfig

app = Flask(__name__)

# Get the config from object of DevConfig
# 使用onfig.from_object() 而不使用app.config['DEBUG']是因为这样可以加载class DevConfig的配置变量集合，而不需要一项一项的添加和修改
app.config.from_object(DevConfig)

# 指定 URL='/'的路由规则
# 当访问 HTTP://server_ip/ GET(Default)时，call home()

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    # Entry the application
    app.run()
