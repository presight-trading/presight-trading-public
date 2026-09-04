#!/usr/bin/env bash
# 生成可下载分享的包赔长图（PNG）与打印版（PDF）。
#
# 产物直接提交进仓库（assets/share/），因为站点是 GitHub Pages 纯静态托管，
# 没有构建环节——文件不在仓库里就没有下载地址。
#
# 出图前先跑 terms.py 核对关键数字：海报会被下载、转进微信、脱离官网独立
# 流传，改了官网忘了海报，外面就长期挂着一份旧条款，而且撤不回来。对不上
# 就直接退出，宁可出不来也不要出一张不一致的。
#
# 用法：bash tools/poster/build.sh
set -euo pipefail
cd "$(dirname "$0")"
ROOT=$(cd ../.. && pwd)

CHROME=${CHROME:-"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"}
[ -x "$CHROME" ] || { echo "❌ 找不到 Chrome，可用 CHROME=/path/to/chrome 指定"; exit 1; }

echo "── 1/4 核对海报与官网是否一致"
python3 terms.py

echo "── 2/4 生成二维码（指向 #start-copy，扫码直接弹出「三步开始跟单」）"
uv run --with segno python - <<'PY'
import segno
segno.make('https://presighttrading.com/#start-copy', error='h').save(
    'qr.svg', kind='svg', scale=10, border=2, dark='#0a1020', light='#ffffff')
PY

echo "── 3/4 渲染长图 PNG"
# 无头 Chrome 的 --screenshot 只截窗口大小，截不到整页：先把文档高度写进
# title 读出来，再用它当窗口高度重截一次。
H=$("$CHROME" --headless --disable-gpu --window-size=1080,1000 \
      --virtual-time-budget=4000 --dump-dom "file://$PWD/poster.html" 2>/dev/null \
    | grep -o '<title>H=[0-9]*' | grep -o '[0-9]*')
[ -n "$H" ] || { echo "❌ 没量到文档高度"; exit 1; }
"$CHROME" --headless --disable-gpu --hide-scrollbars --force-device-scale-factor=2 \
  --window-size=1080,"$H" --virtual-time-budget=4000 \
  --screenshot="$ROOT/assets/share/presight-baopei.png" \
  "file://$PWD/poster.html" >/dev/null 2>&1

echo "── 4/4 渲染 PDF"
"$CHROME" --headless --disable-gpu --no-pdf-header-footer \
  --virtual-time-budget=4000 \
  --print-to-pdf="$ROOT/assets/share/presight-baopei.pdf" \
  "file://$PWD/poster.html" >/dev/null 2>&1

cd "$ROOT"
echo
echo "产物："
for f in assets/share/presight-baopei.png assets/share/presight-baopei.pdf; do
  printf "  %-42s %s\n" "$f" "$(du -h "$f" | cut -f1)"
done
python3 - <<'PY'
import struct
d = open('assets/share/presight-baopei.png','rb').read(33)
w,h = struct.unpack('>II', d[16:24])
print(f"  长图尺寸 {w}x{h}（微信里按屏宽缩放，2 倍图转几手仍清楚）")
PY
