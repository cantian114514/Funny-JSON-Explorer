## 中山大学2024年软件工程作业：Funny JSON Explorer

### 运行命令

在命令行中，进入到包含这些文件的目录，然后运行以下命令：
python main.py -f example.json -s tree -i poker

参数说明：

`-f` 或 `--file`: 指定要读取的 JSON 文件路径。

`-s` 或 `--style`: 指定风格，可以是 `tree` 或 `rectangle`。

`-i` 或 `--icon`: 指定图标族，可以是 `default`（默认图标族）或 `poker`（扑克图标族）。若不指定，默认为 `default`。

### 举例如下
### 使用树形风格和扑克图标族
python main.py -f example.json -s tree -i poker
### 使用矩形风格和默认图标族
python main.py -f example.json -s rectangle
