#!/usr/bin/env bash
# 生成五个语种的 og:image（1200×630），输出到 assets/og-<lang>.png。
#
# 为什么要有这个：og:image 原来指向 assets/og.png，而那个文件根本不存在
# ——链接发到 Telegram / 微信里是一张空白卡片。分享是拉新的第一道门面，
# 空白等于白发。
#
# 用法：bash tools/og/build.sh          # 全部语种
#       bash tools/og/build.sh en ja    # 只出指定语种
set -euo pipefail
cd "$(dirname "$0")"
ROOT=$(cd ../.. && pwd)
LANGS=${*:-"zh en ja vi th"}

CHROME=${CHROME:-"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"}
[ -x "$CHROME" ] || { echo "❌ 找不到 Chrome，可用 CHROME=/path/to/chrome 指定"; exit 1; }

for L in $LANGS; do
  python3 render.py "$L" "_og-${L}.html"
  # 固定 1200×630 直接截，不需要像长图那样先量文档高度
  "$CHROME" --headless --disable-gpu --hide-scrollbars \
    --window-size=1200,630 --virtual-time-budget=3000 \
    --screenshot="$ROOT/assets/og-${L}.png" \
    "file://$PWD/_og-${L}.html" >/dev/null 2>&1
  rm -f "_og-${L}.html"
done

# 中文那份同时留一份无后缀的：og:image 的历史地址是 assets/og.png，
# 外面可能已经有抓过这个地址的缓存。
cp "$ROOT/assets/og-zh.png" "$ROOT/assets/og.png"

cd "$ROOT"
echo
python3 - <<'PY'
import glob, os, struct
for f in sorted(glob.glob('assets/og*.png')):
    d = open(f, 'rb').read(33)
    w, h = struct.unpack('>II', d[16:24])
    print(f"  {f:24} {os.path.getsize(f)/1024:6.0f} KB  {w}x{h}")
PY
