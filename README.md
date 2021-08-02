# 系统个性化汇总
## 程序简介
### 背景
有一次在梦境中，有人问我有没有一站式个性化自己的系统（deepin、UOS）的程序，我当时说了没有，于是我醒来后就把这个程序写了出来……  
在此省略一万字  

### 介绍
<center><img src="https://d.store.deepinos.org.cn//store/themes/top.yzzi.isfriwidget/screen_1.png" alt="挂个图意思一下"></center>  
<center><b>（挂一个图意思一下）  </b></center><br/>
一个基于 python3 的 tkinter 构建了系统个性化的汇总程序<br/>
当前版本：1.0.0<br/>
（测试平台：deepin 20.2.2）<br/>
截图：

![1.0.0主界面](https://storage.deepin.org/thread/202108021706528672_截图_tk_20210802170559.png)

#### 项目提示  
有些地方需要 root，如你无法获得 root 权限则无法安装任何应用！  

#### 软件架构  
只要你能运行 python3 以及其需要的库就可以使用  

#### 更新内容：  
1.0.0没什么好更新的

## 运行  

### 安装  
1、安装所需依赖  
```bash
sudo apt install python3 python3-pip python3-tk python3-pil python3-pil.imagetk
python3 -m pip install ttkthemes
```  
2、获得文件  
```bash
git clone
# 下面的也可以
git clone
```  
3、运行文件  
```bash
cd system-personalized-summary
chmod 777 main.py
./main.py
# 或直接
# python3 main.py
```   
### 使用  
点击按钮进行操作，安装所需程序需要 root 权限
![输入密码](https://storage.deepin.org/thread/202108021715085872_截图_dde-polkit-agent_20210802171426.png)

### 更新  
留意哦  

### 故障排除
提 isscue 最好，当然有些问题自己无法解决，请大佬 push 一下
如果出现故障，尝试终端运行，如果是可以自行解决的问题，就**自行解决**，如果可以就**提 issues 并提供解决方案**，不行就**提 isscue 并提供程序和终端报错以及程序版本**

#### 已知问题
暂未发现

## 相关/使用项目  
| 项目名称 | 项目地址 |
|   :-:  |      :-:|
| 星火应用商店（的源） | https://gitee.com/deepin-community-store/spark-store/ |  
| oh my dde | https://gitee.com/Limexb/oh-my-dde |
| 一只动态壁纸 | https://gitee.com/spark-opensource/one-wallpaper |
| 自家壁纸库 | https://github.com/gfdgd-xi/deepin.background.github.io/ |
| DDE Top Panel | https://github.com/SeptemberHX/dde-top-panel |
| Candy 图标主题 | https://github.com/EliverLara/candy-icons |
| unsplash-wallpapers | https://github.com/soroushchehresa/unsplash-wallpapers/ |
| volantes 光标主题 | https://github.com/varlesh/volantes-cursors |
| Tela 图标主题 | https://github.com/vinceliuice/Tela-icon-theme |
| McMuse 图标主题 | https://github.com/yeyushengfan258/McMuse-icon-theme |
| 幻梦动态壁纸 | https://github.com/dependon/fantascene-dynamic-wallpaper/ |
| Bibata 光标主题 | https://github.com/ful1e5/Bibata_Cursor |
| unsplash4Deepin | https://github.com/shansb/unsplash4Deepin |
| macosbigsur 光标主题 | https://github.com/ful1e5/apple_cursor |
| …… | …… |