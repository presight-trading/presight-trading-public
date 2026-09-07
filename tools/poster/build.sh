#!/usr/bin/env bash
# 生成五个语种的分享长图（PNG）与打印版（PDF）。
#
# 产物直接提交进仓库（assets/share/），因为站点是 GitHub Pages 纯静态托管，
# 没有构建环节——文件不在仓库里就没有下载地址。
#
# 出图前先跑 terms.py 核对关键数字：海报会被下载、转进微信、脱离官网独立
# 流传，改了官网忘了海报，外面就长期挂着一份旧条款，而且撤不回来。对不上
# 就直接退出，宁可出不来也不要出一张不一致的。
#
# 用法：bash tools/poster/build.sh            # 全部语种
#       bash tools/poster/build.sh en ja      # 只出指定语种
set -euo pipefail
cd "$(dirname "$0")"
ROOT=$(cd ../.. && pwd)
LANGS=${*:-"zh en ja vi th"}

CHROME=${CHROME:-"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"}
[ -x "$CHROME" ] || { echo "❌ 找不到 Chrome，可用 CHROME=/path/to/chrome 指定"; exit 1; }

echo "── 核对海报与官网是否一致"
python3 terms.py

echo "── 生成各语种二维码（指向自己那一版落地页的 #start-copy）"
uv run --with segno python - <<'PY'
import sys
sys.path.insert(0, '.')
import segno
from strings import SITES
for lang, (_, url) in SITES.items():
    segno.make(url, error='h').save(
        f'qr-{lang}.svg', kind='svg', scale=10, border=2,
        dark='#0a1020', light='#ffffff')
    print(f"  {lang} → {url}")
PY

for L in $LANGS; do
  echo "── ${L}"
  python3 render.py "$L" "_r-${L}.html"

  # 无头 Chrome 的 --screenshot 只截窗口大小，截不到整页：先把文档高度写进
  # title 读出来，再用它当窗口高度重截一次。
  H=$("$CHROME" --headless --disable-gpu --window-size=750,1000 \
        --virtual-time-budget=4000 --dump-dom "file://$PWD/_r-${L}.html" 2>/dev/null \
      | grep -o '<title>H=[0-9]*' | grep -o '[0-9]*')
  [ -n "$H" ] || { echo "❌ ${L}: 没量到文档高度"; exit 1; }

  "$CHROME" --headless --disable-gpu --hide-scrollbars --force-device-scale-factor=2 \
    --window-size=750,"$H" --virtual-time-budget=4000 \
    --screenshot="$ROOT/assets/share/presight-baopei-${L}.png" \
    "file://$PWD/_r-${L}.html" >/dev/null 2>&1

  "$CHROME" --headless --disable-gpu --no-pdf-header-footer \
    --virtual-time-budget=4000 \
    --print-to-pdf="$ROOT/assets/share/presight-baopei-${L}.pdf" \
    "file://$PWD/_r-${L}.html" >/dev/null 2>&1

  rm -f "_r-${L}.html"
done

# 中文那两份保留无后缀的副本：之前发出去的下载链接是无后缀的，
# 已经转到微信里的链接不该失效。
cp "$ROOT/assets/share/presight-baopei-zh.png" "$ROOT/assets/share/presight-baopei.png"
cp "$ROOT/assets/share/presight-baopei-zh.pdf" "$ROOT/assets/share/presight-baopei.pdf"

cd "$ROOT"
echo
echo "产物："
python3 - <<'PY'
import glob, os, struct
for f in sorted(glob.glob('assets/share/presight-baopei*')):
    size = os.path.getsize(f) / 1024
    dim = ''
    if f.endswith('.png'):
        d = open(f, 'rb').read(33)
        w, h = struct.unpack('>II', d[16:24])
        dim = f'  {w}x{h}'
    print(f"  {f:44} {size:7.0f} KB{dim}")
PY
