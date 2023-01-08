# short_url

一个带有混淆视听功能的在线链接缩短小工具!

### 等下...混淆视听好像没有用!🥲

## 什么是混淆视听

一些社交软件会有链接预览功能, 这个小工具提供了可以自定义预览文字的功能!

比方说缩短一个rick roll的链接, 原本的youtube链接在软件中会直接预览到视频的一些数据.

使用这个工具就不会有这种情况啦!

## 如何使用

打开此demo站即可使用:

https://wzk0.pythonanywhere.com

> 因为我没钱买域名, 所以经过缩短的链接好像还是很长...

## 开发

* 若要在本地运行, 只需要:

0. clone此仓库;
1. pip3 install -r requirements.txt;
2. export FLASK_APP=app.py;
3. export FLASK_ENV=development;
4. flask run.

* 若在部署在服务器上, 只需要:

0. 在服务器上clone此仓库;
1. 修改app.py第7~10行的信息(有注释);
2. 上面的步骤.

运行思路:

前端传入`url`和`preview_word`两个数据, 后端判断是否是链接, 是否存在.

短链实际上是一个空白网页, 有重定向代码, 以及网页描述以实现混淆视听的功能.