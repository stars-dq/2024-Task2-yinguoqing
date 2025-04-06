一.所使用的 Git、Conda 命令并解释。
git init ：在当前目录初始化一个新的 Git 仓库，创建隐藏的.git文件夹用于存储版本控制信息。
git config --global user.name "Your Name" ：设置全局的用户名，用于标识提交者身份。
git config --global user.email "your_email@example.com" ：设置全局的用户邮箱，与用户名配合标识提交者。
git add <filename> ：将指定文件添加到暂存区；git add. 则是将当前目录下所有变动文件（新增、修改 ）添加到暂存区。
git commit -m "Commit message" ：提交暂存区的文件改动，-m 后接提交信息，描述此次提交内容。
git status ：查看当前工作目录和暂存区的状态，显示哪些文件被修改、新增、删除，以及是否已暂存等情况。
git branch <branch_name> ：创建一个新分支，不切换分支。
git checkout -b <branch_name> ：创建新分支并立即切换到该分支。
git checkout <branch_name> ，用于切换到指定分支。
git merge <branch_name> ，将指定分支合并到当前所在分支。比如在 dev 分支执行 git merge feature - plot ，可将 feature - plot 分支内容合并到 dev 分支 。
git remote add origin <repository_url> ：将本地仓库与远程仓库关联，origin 是远程仓库默认别名，<repository_url> 是远程仓库地址。
git push origin <branch_name> ：将本地指定分支推送到远程仓库 origin 。
git pull origin <branch_name> ：从远程仓库 origin 拉取指定分支内容并合并到本地当前分支。
git log ：查看提交历史记录，包括每次提交的哈希值、作者、日期、提交信息等。
git log --graph --decorate --oneline ：以图形化、简洁方式展示分支合并情况和提交历史，--graph 绘制图形，--decorate 显示分支和标签，--oneline 将每个提交显示为一行 。
conda create -n <env_name> python=<version> ：创建名为 <env_name> 的新虚拟环境，并指定 Python 版本为 <version> ，例如 conda create -n my_env python=3.9 。
conda create -n <env_name> --clone <existing_env> ：基于已有的 <existing_env> 克隆出一个新环境 <env_name> 。
activate <env_name> 激活环境
deactivate  退出环境
conda env remove -n <env_name> 删除环境
conda install <package_name> ：在当前激活环境中安装指定包，如 conda install numpy 。
conda install -n <env_name> <package_name> ：在指定的 <env_name> 环境中安装包。
conda install <package_name>=<version> ：安装指定版本的包，如 conda install numpy=1.21 。
二.Anaconda 环境配置的优点与难点。
优点
环境隔离：可以为不同项目创建独立的虚拟环境，避免不同项目间依赖冲突。例如，一个项目依赖 numpy 1.18 版本，另一个项目依赖 numpy 1.20 版本，通过 Anaconda 虚拟环境可以分别配置，互不干扰。
依赖管理方便：能快速安装、更新、卸载各种 Python 包，conda 命令自动处理包之间的依赖关系。比如安装 matplotlib 时，会自动安装其依赖的其他包。
难点
环境切换混乱：当同时管理多个虚拟环境时，容易混淆当前处于哪个环境，导致在错误环境中安装或运行代码。
包版本冲突解决复杂：虽然 conda 能处理大部分依赖，但遇到复杂的跨平台或多个包之间存在复杂依赖关系时，解决版本冲突可能比较棘手，有时需要花费较多时间排查和调整。
三.Git 分支管理中的经验
合理分支命名：采用有意义的命名方式，如功能分支以 feature - 开头，便于快速识别分支用途。
定期合并分支：及时将功能分支合并到开发分支或主分支，防止分支长期分离导致合并时冲突过多。
提交信息规范：撰写清晰、准确的提交信息，方便后续查看提交历史时能快速了解每次提交的内容和目的。
四.部署过程中遇到的问题及解决方案。
问题：在推送代码到 GitHub 时，出现 “Recv failure: Connection was reset” 错误。
解决方案：检查网络连接，确认网络正常后，排查代理设置，通过执行 git config --global --unset http.proxy 和 git config --global --unset https.proxy 取消代理（若不需要代理 ），最终成功推送代码。


