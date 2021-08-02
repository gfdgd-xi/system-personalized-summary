#########################################################
# 版本：1.0.0
#########################################################
#
#!/usr/bin/env python3
########################
# 程序所需库
########################
import os
import time
import json
import shutil
import requests
import ttkthemes
import threading
import traceback
import webbrowser
import subprocess
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox
import PIL.Image as Image
import PIL.ImageTk as ImageTk

#########################
# 程序所需事件
#########################
# 卸载顶栏
def DdeTopUninstall(event):
    InstallWindow.ShowWindows("pkexec apt purge dde-top-panel -y")

def DdeTopInstall():
    # 判断系统是否安装
    if os.path.exists("/usr/bin/dde-top-panel"):
        os.system("dde-top-panel &")
        return
    # 如果没有安装
    if messagebox.askyesno(title="提示", message="系统未安装顶栏，是否安装？"):
        # 获取下载地址
        try:
            settingJson = requests.get(programSetting["Url"]).text
            setting = json.loads(settingJson)
            url = setting["dde-top-panel"]["Deb Url"][0]
        except:
            traceback.print_exc()
            messagebox.showerror(title="错误", message="无法连接服务器，已停止安装！\n" + traceback.format_exc())
            return
        if os.path.exists("/tmp/Install-Command"):
            os.remove("/tmp/Install-Command")
        os.mknod("/tmp/Install-Command")
        ReadAndWriteFile.WriteTxt("/tmp/Install-Command", '''#!/bin/bash
        rm -rfv 'dde-top-panel-download-temp'
        wget '{}' -P '/tmp/dde-top-panel-download-temp'
        pkexec dpkg -i /tmp/dde-top-panel-download-temp/*
        pkexec apt install -f -y'''.format(url))
        os.chmod("/tmp/Install-Command", 777)
        InstallWindow.ShowWindows("pkexec /tmp/Install-Command".format(url))

def DdeDockUninstall(event):
    InstallWindow.ShowWindows("pkexec apt purge top.yzzi.youjian -y")

def DdeDockInstall():
    # 判断系统是否安装
    if os.path.exists("/opt/apps/top.yzzi.youjian/files/oh-my-dde"):
        os.system("/opt/apps/top.yzzi.youjian/files/oh-my-dde &")
        return
    # 如果没有安装
    if messagebox.askyesno(title="提示", message="系统未安装 oh my dde，是否安装？"):
        # 获取下载地址
        try:
            settingJson = requests.get(programSetting["Url"]).text
            setting = json.loads(settingJson)
            url = setting["top.yzzi.youjian"]["Deb Url"][0]
        except:
            traceback.print_exc()
            messagebox.showerror(title="错误", message="无法连接服务器，已停止安装！\n" + traceback.format_exc())
            return
        if os.path.exists("/tmp/Install-Command"):
            os.remove("/tmp/Install-Command")
        os.mknod("/tmp/Install-Command")
        ReadAndWriteFile.WriteTxt("/tmp/Install-Command", '''#!/bin/bash
        rm -rfv 'top.yzzi.youjian'
        wget '{}' -P '/tmp/top.yzzi.youjian'
        pkexec dpkg -i /tmp/top.yzzi.youjian/*
        pkexec apt install -f -y'''.format(url))
        os.chmod("/tmp/Install-Command", 777)
        InstallWindow.ShowWindows("pkexec /tmp/Install-Command".format(url))

def DdeUnderUninstall(event):
    InstallWindow.ShowWindows("pkexec apt purge plank -y")

def DdeUnderInstall():
    # 判断系统是否安装
    if os.path.exists("/usr/bin/plank"):
        os.system("plank &")
        return
    # 如果没有安装
    if messagebox.askyesno(title="提示", message="系统未安装底栏，是否安装？"):
        InstallWindow.ShowWindows("pkexec apt install plank -y")

class DdeMouseList():
    def ShowWindow():
        global list
        global lists
        global setting
        columns= ("number", "name", "about", "author")
        ddeMouseList = tk.Toplevel()
        ddeMouseList.iconphoto(False, tk.PhotoImage(file=iconPath))
        ddeMouseList.title("安装光标主题（请先单击要安装主题，再双击安装）")
        ddeMouseListFrame = ttk.Frame(ddeMouseList)
        list = ttk.Treeview(ddeMouseListFrame, columns=columns, show='headings')
        list.bind("<Double-Button-1>", DdeMouseList.Install)
        list.bind("<Double-Button-3>", DdeMouseList.Uninstall)
        list.column("number", anchor="center")
        list.column("name", anchor="center")
        list.column("about", anchor="center")
        list.column("author", anchor="center")
        # 设置表格头部标题
        list.heading("number", text="编号")
        list.heading("name", text="主题名称")
        list.heading("about", text="主题介绍")
        list.heading("author", text="作者")
        list.pack(expand='yes', fill='both')
        '''lists = [
            [1, "deepin", "about"],
            [2, "deepin", "about1"],
            [3, "deepin", "about2"]
        ]'''
        settingJson = requests.get(programSetting["Url"]).text
        setting = json.loads(settingJson)
        lists = setting["Mouse"]
        i = 1
        for v in lists:
            list.insert('', i, values=[i, v["Name"], v["About"], v["Author"]])
            i += 1
        ddeMouseListFrame.pack(expand='yes', fill='both')
        ddeMouseList.mainloop()

    def Install(event):
        global list
        global lists
        curItem = list.focus()
        values = list.item(curItem, option='values')
        number = int(values[0])
        thisList = lists[number - 1]
        url = thisList["Url"]
        package = thisList["Package"]
        if os.path.exists("/tmp/Install-Command"):
            os.remove("/tmp/Install-Command")
        os.mknod("/tmp/Install-Command")
        ReadAndWriteFile.WriteTxt("/tmp/Install-Command", '''#!/bin/bash
        rm -rfv '/tmp/{}'
        wget '{}' -P '/tmp/{}'
        pkexec dpkg -i /tmp/{}/*
        pkexec apt install -f -y'''.format(package, url, package, package))
        os.chmod("/tmp/Install-Command", 777)
        InstallWindow.ShowWindows("pkexec /tmp/Install-Command".format(url))

    def Uninstall(event):
        global list
        global lists
        curItem = list.focus()
        values = list.item(curItem, option='values')
        number = int(values[0])
        thisList = lists[number - 1]
        url = thisList["Url"]
        package = thisList["Package"]
        InstallWindow.ShowWindows("pkexec apt purge {} -y".format(package))

class DdeIconList():
    def ShowWindow():
        global list
        global lists
        global setting
        columns= ("number", "name", "about", "author")
        ddeIconList = tk.Toplevel()
        ddeIconList.iconphoto(False, tk.PhotoImage(file=iconPath))
        ddeIconList.title("安装图标主题（请先单击要安装主题，再双击安装）")
        ddeIconListFrame = ttk.Frame(ddeIconList)
        list = ttk.Treeview(ddeIconListFrame, columns=columns, show='headings')
        list.bind("<Double-Button-1>", DdeIconList.Install)
        list.bind("<Double-Button-3>", DdeIconList.Uninstall)
        list.column("number", anchor="center")
        list.column("name", anchor="center")
        list.column("about", anchor="center")
        list.column("author", anchor="center")
        # 设置表格头部标题
        list.heading("number", text="编号")
        list.heading("name", text="主题名称")
        list.heading("about", text="主题介绍")
        list.heading("author", text="作者")
        list.pack(expand='yes', fill='both')
        '''lists = [
            [1, "deepin", "about"],
            [2, "deepin", "about1"],
            [3, "deepin", "about2"]
        ]'''
        settingJson = requests.get(programSetting["Url"]).text
        setting = json.loads(settingJson)
        lists = setting["Icon"]
        i = 1
        for v in lists:
            list.insert('', i, values=[i, v["Name"], v["About"], v["Author"]])
            i += 1
        ddeIconListFrame.pack(expand='yes', fill='both')
        ddeIconList.mainloop()

    def Install(event):
        global list
        global lists
        curItem = list.focus()
        values = list.item(curItem, option='values')
        number = int(values[0])
        thisList = lists[number - 1]
        url = thisList["Url"]
        package = thisList["Package"]
        if os.path.exists("/tmp/Install-Command"):
            os.remove("/tmp/Install-Command")
        os.mknod("/tmp/Install-Command")
        ReadAndWriteFile.WriteTxt("/tmp/Install-Command", '''#!/bin/bash
        rm -rfv '/tmp/{}'
        wget '{}' -P '/tmp/{}'
        pkexec dpkg -i /tmp/{}/*
        pkexec apt install -f -y'''.format(package, url, package, package))
        os.chmod("/tmp/Install-Command", 777)
        InstallWindow.ShowWindows("pkexec /tmp/Install-Command".format(url))
        
    def Uninstall(event):
        global list
        global lists
        curItem = list.focus()
        values = list.item(curItem, option='values')
        number = int(values[0])
        thisList = lists[number - 1]
        url = thisList["Url"]
        package = thisList["Package"]
        InstallWindow.ShowWindows("pkexec apt purge {} -y".format(package))

class DdeDesktopTools():
    def ShowWindows():
        ddeDesktopToolsInstallWindow = tk.Toplevel()
        ddeDesktopToolsInstallWindow.iconphoto(False, tk.PhotoImage(file=iconPath))
        ddeDesktopToolsInstallWindow.title("选择小工具")
        ddeDesktopToolsInstallWindow.resizable(0, 0)
        ddeDesktopToolsInstallWindowFrame = ttk.Frame(ddeDesktopToolsInstallWindow)
        yiyanwidgetPictureImg = ImageTk.PhotoImage(Image.open(yiyanwidgetPicturePath))
        musicwidgetPictureImg = ImageTk.PhotoImage(Image.open(musicwidgetPicturePath))
        isfriwidgetPictureImg = ImageTk.PhotoImage(Image.open(isfriwidgetPicturePath))
        yiyanwidgetPicture = ttk.Label(ddeDesktopToolsInstallWindowFrame, image=yiyanwidgetPictureImg)
        musicwidgetPicture = ttk.Label(ddeDesktopToolsInstallWindowFrame, image=musicwidgetPictureImg)
        isfriwidgetPicture = ttk.Label(ddeDesktopToolsInstallWindowFrame, image=isfriwidgetPictureImg)
        yiyanwidgetButton = ttk.Button(ddeDesktopToolsInstallWindowFrame, text="一言小部件", command=DdeDesktopTools.YiyanwidgetInstall)
        musicwidgetButton = ttk.Button(ddeDesktopToolsInstallWindowFrame, text="音乐小部件", command=DdeDesktopTools.MusicwidgetInstall)
        isfriwidgetButton = ttk.Button(ddeDesktopToolsInstallWindowFrame, text="星期五小部件", command=DdeDesktopTools.IsfriwidgetInstall)
        yiyanwidgetPicture.grid(row=0, column=0)
        yiyanwidgetButton.grid(row=1, column=0)
        musicwidgetPicture.grid(row=0, column=1)
        musicwidgetButton.grid(row=1, column=1)
        isfriwidgetPicture.grid(row=0, column=2)
        isfriwidgetButton.grid(row=1, column=2)
        ddeDesktopToolsInstallWindowFrame.pack(expand='yes', fill='both')
        ddeDesktopToolsInstallWindow.mainloop()

    def YiyanwidgetInstall():
        # 判断系统是否安装
        if os.path.exists("/opt/apps/top.yzzi.yiyanwidget/files/Yiyan-Widget"):
            os.system("/opt/apps/top.yzzi.yiyanwidget/files/Yiyan-Widget &")
            return
        # 如果没有安装
        if messagebox.askyesno(title="提示", message="系统未安装一言小部件，是否安装？"):
            # 获取下载地址
            try:
                settingJson = requests.get(programSetting["Url"]).text
                setting = json.loads(settingJson)
                url = setting["top.yzzi.yiyanwidget"]["Deb Url"][0]
            except:
                traceback.print_exc()
                messagebox.showerror(title="错误", message="无法连接服务器，已停止安装！\n" + traceback.format_exc())
                return
            if os.path.exists("/tmp/Install-Command"):
                os.remove("/tmp/Install-Command")
            os.mknod("/tmp/Install-Command")
            ReadAndWriteFile.WriteTxt("/tmp/Install-Command", '''#!/bin/bash
            rm -rfv '/tmp/top.yzzi.yiyanwidget'
            wget '{}' -P '/tmp/top.yzzi.yiyanwidget'
            pkexec dpkg -i /tmp/top.yzzi.yiyanwidget/*
            pkexec apt install -f -y'''.format(url))
            os.chmod("/tmp/Install-Command", 777)
            InstallWindow.ShowWindows("pkexec /tmp/Install-Command".format(url))

    def MusicwidgetInstall():
        # 判断系统是否安装
        if os.path.exists("/opt/apps/top.yzzi.musicwidget/files/Music-Widget"):
            os.system("/opt/apps/top.yzzi.musicwidget/files/Music-Widget &")
            return
        # 如果没有安装
        if messagebox.askyesno(title="提示", message="系统未安装音乐小部件，是否安装？"):
            # 获取下载地址
            try:
                settingJson = requests.get(programSetting["Url"]).text
                setting = json.loads(settingJson)
                url = setting["top.yzzi.musicwidget"]["Deb Url"][0]
            except:
                traceback.print_exc()
                messagebox.showerror(title="错误", message="无法连接服务器，已停止安装！\n" + traceback.format_exc())
                return
            if os.path.exists("/tmp/Install-Command"):
                os.remove("/tmp/Install-Command")
            os.mknod("/tmp/Install-Command")
            ReadAndWriteFile.WriteTxt("/tmp/Install-Command", '''#!/bin/bash
            rm -rfv '/tmp/top.yzzi.musicwidget'
            wget "{}" -P "/tmp/top.yzzi.musicwidget"
            pkexec dpkg -i /tmp/top.yzzi.musicwidget/*
            pkexec apt install -f -y'''.format(url))
            os.chmod("/tmp/Install-Command", 777)
            InstallWindow.ShowWindows("pkexec /tmp/Install-Command".format(url))

    def IsfriwidgetInstall():
        # 判断系统是否安装
        if os.path.exists("/opt/apps/top.yzzi.isfriwidget/files/IsFRI-Widget"):
            os.system("/opt/apps/top.yzzi.isfriwidget/files/IsFRI-Widget &")
            return
        # 如果没有安装
        if messagebox.askyesno(title="提示", message="系统未安装星期五小部件，是否安装？"):
            # 获取下载地址
            try:
                settingJson = requests.get(programSetting["Url"]).text
                setting = json.loads(settingJson)
                url = setting["top.yzzi.isfriwidget"]["Deb Url"][0]
            except:
                traceback.print_exc()
                messagebox.showerror(title="错误", message="无法连接服务器，已停止安装！\n" + traceback.format_exc())
                return
            if os.path.exists("/tmp/Install-Command"):
                os.remove("/tmp/Install-Command")
            os.mknod("/tmp/Install-Command")
            ReadAndWriteFile.WriteTxt("/tmp/Install-Command", '''#!/bin/bash
            rm -rfv "/tmp/top.yzzi.isfriwidget"
            wget "{}" -P "/tmp/top.yzzi.isfriwidget"
            pkexec dpkg -i /tmp/top.yzzi.isfriwidget/*
            pkexec apt install -f -y'''.format(url))
            os.chmod("/tmp/Install-Command", 777)
            InstallWindow.ShowWindows("pkexec /tmp/Install-Command".format(url))

# 显示“提示”窗口
def helps()->"显示“提示”窗口":
    global tips
    messagebox.showinfo(title="提示", message=tips)

# 显示更新内容窗口
def UpdateThings()->"显示更新内容窗口":
    messagebox.showinfo(title="更新内容", message=updateThings)

# 打开程序官网
def OpenProgramURL()->"打开程序官网":
    webbrowser.open_new_tab(programUrl)

# 重启本应用程序
def ReStartProgram()->"重启本应用程序":
    python = sys.executable
    os.execl(python, python, * sys.argv)

# 显示“关于这个程序”窗口
def about_this_program()->"显示“关于这个程序”窗口":
    global about
    global title
    global iconPath
    mess = tk.Toplevel()
    message = ttk.Frame(mess)
    mess.resizable(0, 0)
    mess.title("关于 {}".format(title))
    mess.iconphoto(False, tk.PhotoImage(file=iconPath))
    img = ImageTk.PhotoImage(Image.open(iconPath))
    label1 = ttk.Label(message, image=img)
    label2 = ttk.Label(message, text=about)
    button1 = ttk.Button(message, text="确定", command=mess.withdraw)
    label1.pack()
    label2.pack()
    button1.pack(side="bottom")
    message.pack()
    mess.mainloop()

class WallpaperToolsInstall():
    def ShowWindows():
        wallpaperToolsInstallWindow = tk.Toplevel()
        wallpaperToolsInstallWindow.title("选择壁纸小工具")
        wallpaperToolsInstallWindow.resizable(0, 0)
        wallpaperToolsInstallWindow.iconphoto(False, tk.PhotoImage(file=iconPath))
        wallpaperToolsInstallWindowFrame = ttk.Frame(wallpaperToolsInstallWindow)
        unsplashPictureImg = ImageTk.PhotoImage(Image.open(unsplashPicturePath).resize((300, 300), Image.ANTIALIAS))
        unsplash4PictureImg = ImageTk.PhotoImage(Image.open(unsplash4PicturePath).resize((300, 300), Image.ANTIALIAS))
        webPictureImg = ImageTk.PhotoImage(Image.open(webPicturePath).resize((300, 300), Image.ANTIALIAS))
        faPictureImg = ImageTk.PhotoImage(Image.open(faPicturePath).resize((300, 300), Image.ANTIALIAS))
        toPictureImg = ImageTk.PhotoImage(Image.open(toPicturePath).resize((300, 300), Image.ANTIALIAS))
        wePictureImg = ImageTk.PhotoImage(Image.open(wePicturePath).resize((300, 300), Image.ANTIALIAS))
        unsplashPicture = ttk.Label(wallpaperToolsInstallWindowFrame, image=unsplashPictureImg)
        unsplash4Picture = ttk.Label(wallpaperToolsInstallWindowFrame, image=unsplash4PictureImg)
        webPicture = ttk.Label(wallpaperToolsInstallWindowFrame, image=webPictureImg)
        faPicture = ttk.Label(wallpaperToolsInstallWindowFrame, image=faPictureImg)
        toPicture = ttk.Label(wallpaperToolsInstallWindowFrame, image=toPictureImg)
        wePicture = ttk.Label(wallpaperToolsInstallWindowFrame, image=wePictureImg)
        unsplashButton = ttk.Button(wallpaperToolsInstallWindowFrame, text="unsplash-wallpapers", command=WallpaperToolsInstall.UnsplashInstall)
        unsplash4Button = ttk.Button(wallpaperToolsInstallWindowFrame, text="unsplash4deepin", command=WallpaperToolsInstall.Unsplash4deepinInstall)
        webButton = ttk.Button(wallpaperToolsInstallWindowFrame, text="极简壁纸（web）", command=WallpaperToolsInstall.WebInstall)
        faButton = ttk.Button(wallpaperToolsInstallWindowFrame, text="幻梦动态壁纸", command=WallpaperToolsInstall.FaInstall)
        toButton = ttk.Button(wallpaperToolsInstallWindowFrame, text="一只动态壁纸", command=WallpaperToolsInstall.ToInstall)
        weButton = ttk.Button(wallpaperToolsInstallWindowFrame, text="自家壁纸库", command=WallpaperToolsInstall.WeInstall)
        unsplashButton.bind("<Double-Button-3>", WallpaperToolsInstall.UnsplashUninstall)
        unsplash4Button.bind("<Double-Button-3>", WallpaperToolsInstall.Unsplash4deepinUninstall)
        faButton.bind("<Double-Button-3>", WallpaperToolsInstall.FaUninstall)
        toButton.bind("<Double-Button-3>", WallpaperToolsInstall.ToUninstall)
        unsplashPicture.grid(row=0, column=0)
        unsplashButton.grid(row=1, column=0)
        unsplash4Picture.grid(row=0, column=1)
        unsplash4Button.grid(row=1, column=1)
        webPicture.grid(row=0, column=2)
        webButton.grid(row=1, column=2)
        faPicture.grid(row=2, column=0)
        faButton.grid(row=3, column=0)
        toPicture.grid(row=2, column=1)
        toButton.grid(row=3, column=1)
        wePicture.grid(row=2, column=2)
        weButton.grid(row=3, column=2)
        wallpaperToolsInstallWindowFrame.pack(expand='yes', fill='both')
        wallpaperToolsInstallWindow.mainloop()

    def UnsplashUninstall(event):
        InstallWindow.ShowWindows("pkexec apt purge unsplash-wallpapers -y")

    def UnsplashInstall():
        # 判断系统是否安装
        if os.path.exists("/opt/Unsplash Wallpapers/unsplash-wallpapers"):
            os.system("/opt/Unsplash\ Wallpapers/unsplash-wallpapers &")
            return
        # 如果没有安装
        if messagebox.askyesno(title="提示", message="系统未安装 unsplash-wallpapers，是否安装？"):
            # 获取下载地址
            try:
                settingJson = requests.get(programSetting["Url"]).text
                setting = json.loads(settingJson)
                url = setting["unsplash-wallpapers"]["Deb Url"][0]
            except:
                traceback.print_exc()
                messagebox.showerror(title="错误", message="无法连接服务器，已停止安装！\n" + traceback.format_exc())
                return
            if os.path.exists("/tmp/Install-Command"):
                os.remove("/tmp/Install-Command")
            os.mknod("/tmp/Install-Command")
            ReadAndWriteFile.WriteTxt("/tmp/Install-Command", '''#!/bin/bash
            rm -rfv '/tmp/unsplash-wallpapers'
            wget '{}' -P '/tmp/unsplash-wallpapers'
            pkexec dpkg -i /tmp/unsplash-wallpapers/*
            pkexec apt install -f -y'''.format(url))
            os.chmod("/tmp/Install-Command", 777)
            InstallWindow.ShowWindows("pkexec /tmp/Install-Command".format(url))

    def Unsplash4deepinUninstall(event):
        InstallWindow.ShowWindows("pkexec apt purge unsplash4deepin -y")

    def Unsplash4deepinInstall():
        # 判断系统是否安装
        if os.path.exists("/opt/durapps/unsplash4deepin/unsplash4deepin"):
            os.system("/opt/durapps/unsplash4deepin/unsplash4deepin &")
            return
        # 如果没有安装
        if messagebox.askyesno(title="提示", message="系统未安装 unsplash4deepin，是否安装？"):
            # 获取下载地址
            try:
                settingJson = requests.get(programSetting["Url"]).text
                setting = json.loads(settingJson)
                url = setting["unsplash4deepin"]["Deb Url"][0]
            except:
                traceback.print_exc()
                messagebox.showerror(title="错误", message="无法连接服务器，已停止安装！\n" + traceback.format_exc())
                return
            if os.path.exists("/tmp/Install-Command"):
                os.remove("/tmp/Install-Command")
            os.mknod("/tmp/Install-Command")
            ReadAndWriteFile.WriteTxt("/tmp/Install-Command", '''#!/bin/bash
            rm -rfv '/tmp/unsplash4deepin'
            wget "{}" -P "/tmp/unsplash4deepin"
            pkexec dpkg -i /tmp/unsplash4deepin/*
            pkexec apt install -f -y'''.format(url))
            os.chmod("/tmp/Install-Command", 777)
            InstallWindow.ShowWindows("pkexec /tmp/Install-Command".format(url))

    def WebInstall():
        webbrowser.open_new_tab("https://bz.zzzmh.cn/")

    def WeInstall():
        webbrowser.open_new_tab("https://gfdgd-xi.github.io/deepin.background.github.io/")

    def FaUninstall(event):
        InstallWindow.ShowWindows("pkexec apt purge fantascene-dynamic-wallpaper -y")

    def FaInstall():
        # 判断系统是否安装
        if os.path.exists("/opt/durapps/fantascene-dynamic-wallpaper/fantascene-dynamic-wallpaper"):
            os.system("/opt/durapps/fantascene-dynamic-wallpaper/fantascene-dynamic-wallpaper &")
            return
        # 如果没有安装
        if messagebox.askyesno(title="提示", message="系统未安装幻梦动态壁纸，是否安装？"):
            # 获取下载地址
            try:
                settingJson = requests.get(programSetting["Url"]).text
                setting = json.loads(settingJson)
                url = setting["fantascene-dynamic-wallpaper"]["Deb Url"][0]
            except:
                traceback.print_exc()
                messagebox.showerror(title="错误", message="无法连接服务器，已停止安装！\n" + traceback.format_exc())
                return
            if os.path.exists("/tmp/Install-Command"):
                os.remove("/tmp/Install-Command")
            os.mknod("/tmp/Install-Command")
            ReadAndWriteFile.WriteTxt("/tmp/Install-Command", '''#!/bin/bash
            rm -rfv "/tmp/fantascene-dynamic-wallpaper"
            wget "{}" -P "/tmp/fantascene-dynamic-wallpaper"
            pkexec dpkg -i /tmp/fantascene-dynamic-wallpaper/*
            pkexec apt install -f -y'''.format(url))
            os.chmod("/tmp/Install-Command", 777)
            InstallWindow.ShowWindows("pkexec /tmp/Install-Command".format(url))

    def ToUninstall(event):
        InstallWindow.ShowWindows("pkexec apt purge top.yzzi.wallpaper -y")

    def ToInstall():
        # 判断系统是否安装
        if os.path.exists("/opt/apps/top.yzzi.wallpaper/files/OneWallpaper"):
            os.system("/opt/apps/top.yzzi.wallpaper/files/OneWallpaper &")
            return
        # 如果没有安装
        if messagebox.askyesno(title="提示", message="系统未安装一只动态壁纸，是否安装？"):
            # 获取下载地址
            try:
                settingJson = requests.get(programSetting["Url"]).text
                setting = json.loads(settingJson)
                url = setting["top.yzzi.wallpaper"]["Deb Url"][0]
            except:
                traceback.print_exc()
                messagebox.showerror(title="错误", message="无法连接服务器，已停止安装！\n" + traceback.format_exc())
                return
            if os.path.exists("/tmp/Install-Command"):
                os.remove("/tmp/Install-Command")
            os.mknod("/tmp/Install-Command")
            ReadAndWriteFile.WriteTxt("/tmp/Install-Command", '''#!/bin/bash
            rm -rfv "/tmp/top.yzzi.wallpaper"
            wget "{}" -P "/tmp/top.yzzi.wallpaper"
            pkexec dpkg -i /tmp/top.yzzi.wallpaper/*
            pkexec apt install -f -y'''.format(url))
            os.chmod("/tmp/Install-Command", 777)
            InstallWindow.ShowWindows("pkexec /tmp/Install-Command".format(url))

class ReadAndWriteFile():
    # 读取文本文档
    def ReadTxt(path):
        f = open(path,"r")  # 设置文件对象
        str = f.read()      # 获取内容
        f.close()           # 关闭文本对象
        return str          # 返回结果
    
    # 写入文本文档
    def WriteTxt(path, things):
        file = open(path, 'w', encoding='UTF-8')  # 设置文件对象
        file.write(things)                        # 写入文本
        file.close()                              # 关闭文本对象

class InstallWindow():
    def ShowWindows(command):
        global message
        global text
        global installTipsText
        global progressbar
        message = tk.Toplevel()
        message.iconphoto(False, tk.PhotoImage(file=iconPath))
        messageFrame = ttk.Frame(message)
        installTipsText = tk.StringVar()
        message.title("正在操作……")
        installTipsText.set("正在操作……")
        installTips = ttk.Label(messageFrame, textvariable=installTipsText)
        progressbar = ttk.Progressbar(messageFrame, length=500, mode='indeterminate')
        text = tk.Text(messageFrame)
        text.config(background="black", foreground="white")
        installTips.pack()
        progressbar.pack(fill="x")
        text.pack(expand='yes', fill='both')
        messageFrame.pack(expand='yes', fill='both')
        threading.Thread(target=InstallWindow.RunCommand, args=[command]).start()
        message.mainloop()
    
    def RunCommand(command):
        global message
        global text
        global progressbar
        global installTipsText
        InstallWindow.AddText("$>" + command + "\n")
        progressbar.start()
        result = subprocess.getoutput(command)
        InstallWindow.AddText(result)
        messagebox.showinfo(title="提示", message="操作完毕！")
        installTipsText.set("操作完毕！")
        message.title("操作完毕！")
        progressbar.stop()
        progressbar["value"] = 100

    def AddText(things):
        global text
        text.configure(state=tk.NORMAL)
        text.insert("end", things)
        text.configure(state=tk.DISABLED)

#########################
# 设置程序所需变量
#########################
programPath = os.path.split(os.path.realpath(__file__))[0]
yiyanwidgetPicturePath = programPath + "/Picture/top.yzzi.yiyanwidget.png"
musicwidgetPicturePath = programPath + "/Picture/top.yzzi.musicwidget.png"
isfriwidgetPicturePath = programPath + "/Picture/top.yzzi.isfriwidget.png"
desktopPicturePath = programPath + "/Picture/desktop.png"
unsplashPicturePath = programPath + "/Picture/unsplash-wallpapers.png"
unsplash4PicturePath = programPath + "/Picture/unsplash4deepin.png"
webPicturePath = programPath + "/Picture/web-jjbz.png"
faPicturePath = programPath + "/Picture/fantascene-dynamic-wallpaper.png"
toPicturePath = programPath + "/Picture/top.yzzi.wallpaper.png"
wePicturePath = programPath + "/Picture/web-picture.png"
programUrl = ["https://gitee.com/gfdgd-xi/system-personalized-summary"]
version = "1.0.0"
goodRunSystem = "Linux（deepin/UOS）"
about = '''一个基于 Python3 的 tkinter 制作的系统个性化汇总
版本：{}
适用平台：{}
tkinter 版本：{}
程序官网：{}
©2021-{} gfdgd xi'''.format(version, goodRunSystem, tk.TkVersion, programUrl, time.strftime("%Y"))
tips = '''提示：
1、右键双击可以卸载对应应用'''
updateThingsString = '''1、没有比 1.0.0 更早的版本'''
title = "系统个性化汇总 {}".format(version)
updateTime = "2021年8月2日"
updateThings = "{} 更新内容：\n{}\n更新时间：{}".format(version, updateThingsString, updateTime, time.strftime("%Y"))
iconPath = "{}/icon.png".format(os.path.split(os.path.realpath(__file__))[0])

#########################
# 读取程序配置
#########################
programSetting = json.loads(ReadAndWriteFile.ReadTxt(programPath + "/setting.json"))

#########################
# 设置并显示窗口
#########################
# 创建窗口
window = tk.Tk()  
win = ttk.Frame(window)
# 设置图片实例
img = ImageTk.PhotoImage(Image.open(desktopPicturePath).resize((800, 600), Image.ANTIALIAS))
# 创建控件
examplePicture = ttk.Label(win, image=img, compound='center')
ddeTop = ttk.Button(win, text="顶栏", command=DdeTopInstall)
ddeDesktopTools = ttk.Button(win, text="桌面小工具", command=DdeDesktopTools.ShowWindows)
ddeUnder = ttk.Button(win, text="底栏", command=DdeUnderInstall)
DdeIconButton = ttk.Button(win, text="图标主题", command=DdeIconList.ShowWindow)
ddeMouseListButton = ttk.Button(win, text="光标主题", command=DdeMouseList.ShowWindow)
ddeDockButton = ttk.Button(win, text="dock 栏", command=DdeDockInstall)
wallpaperButton = ttk.Button(win, text="壁纸", command=WallpaperToolsInstall.ShowWindows)
exitButton = ttk.Button(win, text="退出", command=quit)
# 设置菜单栏
menu = tk.Menu(window, background="white")  
programmenu = tk.Menu(menu, tearoff=0, background="white")       # 设置“程序”菜单栏
help = tk.Menu(menu, tearoff=0, background="white")              # 设置“帮助”菜单栏
menu.add_cascade(label="程序", menu=programmenu)
menu.add_cascade(label="帮助", menu=help)
programmenu.add_command(label="退出程序", command=quit)            # 设置“退出程序”项
help.add_command(label="程序官网", command=OpenProgramURL)         # 设置“程序官网”项
help.add_separator()
help.add_command(label="小提示", command=helps)                    # 设置“小提示”项
help.add_command(label="更新内容", command=UpdateThings)           # 设置“更新内容”项
help.add_command(label="关于这个程序", command=about_this_program)  # 设置“关于这个程序”项
menu.configure(activebackground="white")
help.configure(activebackground="white")
programmenu.configure(activebackground="white")
# 设置窗口属性
window.title("桌面个性化")
window.resizable(0, 0)
window.iconphoto(False, tk.PhotoImage(file=iconPath))
style = ttkthemes.ThemedStyle(window)
style.set_theme("ubuntu")
# 设置控件事件
ddeTop.bind("<Double-Button-3>", DdeTopUninstall)
ddeUnder.bind("<Double-Button-3>", DdeUnderUninstall)
ddeDockButton.bind("<Double-Button-3>", DdeDockUninstall)
# 显示控件和窗口
window.config(menu=menu)                                           # 显示菜单栏
examplePicture.grid(row=0, column=0, rowspan=8, sticky=tk.N+tk.S+tk.E+tk.W)
ddeTop.grid(row=0, column=1)
ddeDesktopTools.grid(row=1, column=1)
ddeUnder.grid(row=2, column=1)
DdeIconButton.grid(row=3, column=1)
ddeMouseListButton.grid(row=4, column=1)
ddeDockButton.grid(row=5, column=1)
wallpaperButton.grid(row=6, column=1)
exitButton.grid(row=7, column=1)
win.pack()
window.mainloop()