# Day 2 学习目标 2：Git clone、branch、commit、push 和基本冲突处理

这份文件帮你准备 Git 相关练习：克隆仓库、创建分支、提交、推送，以及理解基本冲突处理。不直接给具体练习仓库的操作答案。

## 1. Git 是什么

Git 是版本控制工具，用来记录代码变化。

你可以把 Git 理解成项目的时间线：

- 每次 `commit` 是一个保存点。
- 每个 `branch` 是一条独立开发线。
- `push` 把本地提交上传到远程仓库。
- `pull` 把远程更新拉到本地。

## 2. 常见 Git 概念

工作区：

你正在编辑的文件。

暂存区：

准备用来提交的文件变化，通过 `git add` 放进去。

本地仓库：

你电脑上的 Git 提交历史。

远程仓库：

GitHub、GitLab 等平台上的仓库。

## 3. clone

`clone` 用来把远程仓库复制到本地。

格式：

```bash
git clone <repo-url>
```

示例：

```bash
git clone https://github.com/example/example-repo.git
```

克隆后进入项目：

```bash
cd example-repo
```

检查状态：

```bash
git status
```

## 4. branch

分支用于在不影响主线的情况下开发。

查看分支：

```bash
git branch
```

创建新分支：

```bash
git branch my-branch
```

切换分支：

```bash
git switch my-branch
```

创建并切换：

```bash
git switch -c my-branch
```

分支命名建议：

- `day2-practice`
- `learn-api`
- `fix-readme`
- `feature/user-script`

## 5. 修改文件后的基本流程

典型流程：

```bash
git status
git add <file>
git commit -m "message"
git push
```

查看具体变化：

```bash
git diff
```

查看已暂存的变化：

```bash
git diff --cached
```

## 6. add

把文件变化放入暂存区：

```bash
git add README.md
```

添加多个文件：

```bash
git add file1.py file2.md
```

添加当前目录所有变化：

```bash
git add .
```

学习阶段建议多用：

```bash
git status
```

确认你到底准备提交哪些文件。

## 7. commit

提交是保存一个版本点。

格式：

```bash
git commit -m "短句描述这次修改"
```

好的 commit message：

- `add day2 python notes`
- `create api practice script`
- `update yaml config example`

不太好的 commit message：

- `update`
- `fix`
- `aaa`

好的提交应该尽量小而清楚。

## 8. push

把本地提交推到远程：

```bash
git push
```

如果是第一次推送新分支，常见写法：

```bash
git push -u origin my-branch
```

这里：

- `origin` 通常表示默认远程仓库。
- `my-branch` 是你当前要推送的分支名。
- `-u` 会把本地分支和远程分支关联起来。

## 9. fork 的基本理解

Fork 是把别人的仓库复制一份到你的账号下面。

常见学习流程：

1. 在 GitHub 上 fork 一个公开仓库。
2. clone 自己 fork 后的仓库。
3. 在本地修改文件。
4. commit。
5. push 到自己 fork 的远程仓库。

注意：你一般没有权限直接 push 到别人的原始仓库，但可以 push 到自己的 fork。

## 10. remote

查看远程地址：

```bash
git remote -v
```

常见输出会包含：

- `origin`：你 clone 时默认配置的远程。
- `upstream`：有时用来表示原始仓库。

添加 upstream：

```bash
git remote add upstream <original-repo-url>
```

## 11. pull

拉取远程更新：

```bash
git pull
```

学习时建议在开始修改前先：

```bash
git status
git pull
```

如果你本地有未提交修改，`pull` 可能会被阻止或产生冲突。

## 12. 冲突是什么

冲突通常发生在：

- 你改了某一行。
- 别人也改了同一行。
- Git 不知道该保留哪一份。

冲突文件里会出现类似标记：

```text
<<<<<<< HEAD
本地版本
=======
远程版本
>>>>>>> branch-name
```

这些标记不是最终代码的一部分，你需要手动编辑文件，保留正确内容，删除冲突标记。

## 13. 处理冲突的基本流程

一般流程：

```bash
git status
```

打开冲突文件，手动修改内容。

修改完成后：

```bash
git add <conflict-file>
git commit
```

如果冲突来自 `merge` 或 `pull`，Git 有时会自动准备 commit message，你可以按情况使用。

## 14. 避免冲突的小习惯

- 开始改之前先 `git pull`。
- 每次提交尽量小。
- 不要同时多人改同一个大文件的同一块内容。
- 写清楚 commit message。
- 提交前先 `git status` 和 `git diff`。

## 15. 自查清单

做 Git 练习时检查：

- 当前目录是不是 Git 仓库。
- 当前分支是不是你想操作的分支。
- `git status` 是否干净或符合预期。
- commit message 是否能说明修改内容。
- push 的远程是不是自己的仓库或 fork。
- 遇到冲突时，是否删除了所有 `<<<<<<<`、`=======`、`>>>>>>>` 标记。
