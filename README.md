使用 git push 时遇到如下报错：

Pushing to https://github.com/xxx/xxx.git

remote: Permission to xxx/xxx.git denied to Usernamexxx.

fatal: unable to access 'https://github.com/xxx/xxx.git/': The requested URL returned error: 403

已经使用如下命令去配置了全局用户：

git config --global user.name userA

git config --global user.email userA@Email.com



但是还是报错，解决方法如下：


git config credential.username UserB

or create a new repository on the command line：

echo "# 123" >> README.md

git init

git add README.md

git commit -m "first commit"

git branch -M main

git remote add origin https://github.com/zhangaifeng1982/123.git

git push -u origin main


or push an existing repository from the command line

git remote add origin https://github.com/zhangaifeng1982/123.git

git branch -M main

git push -u origin main


fatal: unable to access ‘https://github.com/…’: OpenSSL SSL_read: Connection was reset, errno 10054

【产生原因】一般是因为服务器的SSL证书没有经过第三方机构的签署，所以才报错

【解决方式】解除ssl验证后，再次git即可

git config --global http.sslVerify false

决git下载报错：fatal: unable to access ‘https://github.com/…/.git/’:…

1、在git中执行git config --global --unset http.proxy和git config --global --unset https.proxy

git config --global --unset http.proxy

git config --global --unset https.proxy

2、在cmd下执行ipconfig/flushdns 清理DNS缓存

ipconfig/flushdns


