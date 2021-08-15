# blessing
七夕祝福

-----
## 把Python代码转成exe

  列表复制

- 安装pyintsaller包
```python
pip install pyinstaller
```
  * 国内镜像下载pyinstaller
    + 清华：https://pypi.tuna.tsinghua.edu.cn/simple
阿里云：http://mirrors.aliyun.com/pypi/simple/
中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
华中理工大学：http://pypi.hustunique.com/
山东理工大学：http://pypi.sdutlinux.org/
豆瓣：http://pypi.douban.com/simple/

- cmd中加入国内镜像下载工具包命令：**pip install -i url**


- cmd里输入打包成exe的命令
```python
pyinstaller -F xxxx.py(要打包的py文件)
pyinstaller -D xxxx.py(要打包的py文件)
```
***
### 补充
| 字符 | 功能 |
|--|--|
| -F |打包成一个文件  |
| -D |打包成一个文件夹  |
| -n |重新命名  |
| --noconsole | 去掉命令窗口 |
| -i | 加入图标，图标需要是ico格式 |
