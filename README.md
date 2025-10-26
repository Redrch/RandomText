# RandomText

RandomText是一个自动生成控制台内容的软件



## 安装

在软件Release界面即可下载软件



## 使用

双击exe文件即可

**参数**

`--mode, -m` 这个参数有2个值，0或1，为0的时候会输出随机乱码，为1的时候会输出以Download,Update,Delete开头的提示，默认值为0

**start.sh**

这个文件用于以 `--mode 1`参数启动软件，方便多开



## 打包

本软件采用Python3.13编写

`git clone https://github.com/Redrch/RandomText.git`即可将仓库的main分支克隆至本地，建议克隆main分支，较稳定，dev分支为开发分支

**Windows教程**

`python -m venv .venv`创建虚拟环境，然后`.venv\Scripts\activate`激活虚拟环境

`pip install -r requirments.txt`安装依赖库

`nuitka main.py --standalone --onefile --include-data-dir=D:\Develop\Python\RandomText\nltk=nltk --windows-icon-from-ico=logo.png` 使用nuitka打包程序，主目录下的main.exe文件即为打包后的输出文件

**Mac教程**

敬请期待（根本没做mac版本，懒 ^__^ ）

**Linux**

敬请期待（其实只有Windows版本，其他系统的版本在鸽）



