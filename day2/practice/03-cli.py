#windows 下创建目录
# New-Item -ItemType Directory -Path project,project\src,project\tests,project\docs

# windows 下创建文件
#  New-Item -ItemType File -Path project\src\hello.py

# windows 下编辑文件内容
# set-content project\src\hello.py 'print("hello world")'

# 下运行文件
# python project\src\hello.py

# windows 下将输出写入到文件
# python project\src\hello.py > project\docs\output.txt

# windows 查看文件
# Get-Content project\docs\output.txt
