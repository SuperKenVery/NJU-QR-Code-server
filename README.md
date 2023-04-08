# 在网页上显示你的南京大学校园码

朋友入校还要审批？不存在的。

## 使用

```shell
git clone https://github.com/SuperKenVery/qr-code-server.git
cd qr-code-server
git submodule update --init --recursive
```

在`qr_code_server/configuration.py`中放入自己的用户名、密码，并设置访问路径。路径要设复杂点，是当密码用的。

然后：

```shell
sudo docker-compose up -d
```

然后还可以配置一下内网穿透和https反向代理。（可选）

### 内网穿透
推荐tailscale的funnel

### https反向代理
推荐caddy，不过tailscale也可以干这个事，如果只是临时搭这一个网页的话应该还是tailscale自带的比较方便。
