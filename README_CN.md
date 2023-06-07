# pyvarmilo

[English](README.md) | 简体中文

**pyvarmilo** 是一个用于配置阿米洛键盘的 Python 库。它使用 [hidapi Python 库](https://pypi.org/project/hidapi/) 向键盘发送命令。其API可以参考 [hidapi C 库](https://github.com/libusb/hidapi)。

# 依赖

首先运行以下命令：

```
pip install hidapi
```
还可以在[这里](https://pypi.org/project/hidapi/#toc-entry-4)查看安装步骤。

# 支持的型号
* VDG87（仅在 VDG87TTJ 上进行了测试）
* VDG104（未经测试，但应该可用）
* 其他由阿米洛 [VDG104/87自定义键值、灯效软件](https://cn.varmilo.com/keyboardproscenium/upload/Varmilo-Keyboard.rar) 支持的型号



# 示例

列出所有 USB 键盘并根据 `vendor_id` 或 `product_id` 进行过滤
```
python main.py -l
python main.py -l -i 0x4d9,
python main.py -l -i ,0x8008
python main.py -l -m vdg87ttj
```

打印默认键映射
```
python main.py -p -m vdg87ttj
```

将键映射设置为默认值
```
python main.py -v -d -m vdg87ttj
```

交换 LEFTALT 和 LEFTMETA，RIGHTALT 和 RIGHTMETA
```
python main.py -v -m vdg87ttj -k 1:0=LEFTALT,2:0=LEFTMETA,9:0=RIGHTMETA,10:0=RIGHTALT
```

# 如何贡献

* 增加修饰键支持
* 增加 LED 灯光支持
* 寻找 `FIXME` 并解决相应问题
* 欢迎发送 pull request

# 开发

## 在开始之前

* 下载您键盘对应型号的说明书
* 找到如何恢复出厂设置，一般是长按`Fn+D`

## 我的键盘是否受支持？

* 下载阿米洛 [VDG104/87自定义键值、灯效软件](https://cn.varmilo.com/keyboardproscenium/upload/Varmilo-Keyboard.rar
* 安装并打开 `Varmilo-Keyboard.exe`。如果窗口右下角显示绿色的亮灯图标和 "ON"，则表示您的键盘受支持。
* 如果您的键盘不受支持，您仍然使用本程序可以自行承担风险向其发送数据。因为这可能会导致键盘变砖。

## 捕获键盘的 HID 数据

如果您的键盘固件带有重新映射功能，我怀疑键映射数据在所有键盘型号上都是相同的。但我仍建议您捕获 HID 数据。

1. 安装 Visual Studio 和 Windows SDK
2. 检出 [hidapi C 库](https://github.com/libusb/hidapi)
3. 应用补丁 `misc\hidapi.patch`
4. 打开 `windows\hidapi.sln` 并进行构建
5. 将 `windows\Debug\hidapi.dll` 复制到 `C:\Program Files (x86)\VarmiloKeyboard\`
6. 打开 `Varmilo-Keyboard.exe`，然后点击 "按键定义" -> 勾选 "电竞模式"。
7. 点击一个按键并将其映射到其他按键，然后点击 "√" 确认。现在软件应该使用 `hidapi.dll` 向您的键盘发送数据。
8. 然后通过点击 "√" 旁边的 "刷新" 按钮恢复默认设置，然后再次点击 "√"。该软件的工作效果不好，但这并不重要，因为我们想要的是软件发送的数据。
9. 通过点击右上角按钮退出软件
10. 打开 `testlog.txt` 并找到软件发送的 feature report 数据和键映射数据。

键映射数据的结构很直观。它从左到右按列排列，从底部到顶部按键排列。每个键码占据 4 个字节，最后一个字节是 USB HID 键码。详细信息请参阅 `map_vdg87tti.py`。

## 为新型号创建键映射

一旦您捕获了自己型号的数据，请按照 `map_vdg87tti.py` 的示例创建您自己的 `map_MODEL.py` 文件。