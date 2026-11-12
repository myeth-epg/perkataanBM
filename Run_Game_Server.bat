@echo off
chcp 65001 >nul
echo =======================================================
echo 启动 华小国语词汇学习游戏 (Perkataan BM) 本地服务器
echo Permainan Pembelajaran Kosa Kata Bahasa Melayu SJK(C)
echo =======================================================
echo.
echo 游戏进行时，请保持此窗口开启。
echo.
echo 正在打开浏览器...
start http://localhost:8082/index.html

python -m http.server 8082
pause
