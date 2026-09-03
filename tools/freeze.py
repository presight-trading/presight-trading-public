"""把按序号写的译文固化成按英文原文索引的字典。

序号只在「写第一版」时好用。英文页一旦插入或删除片段，后面所有序号
就整体平移——而平移之后每个序号依然能命中某个片段，只是命中错的那个。
不会报错，页面上却会出现译文和内容对不上，这是最难发现的一种坏法。

所以序号是一次性的脚手架：写完立刻用这个脚本冻结，之后语言文件里只
留英文原文当键，改英文页时 build.py --check 会老老实实报出哪条失效。

用法（--from 指向写译文时那一版英文页所在的 git 版本）：
  uv run --with beautifulsoup4 python tools/freeze.py vi --from dd56393
"""
from __future__ import annotations

import importlib.util
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build import ROOT, ordered_keys                     # noqa: E402


def at_revision(rev: str, path: str) -> Path:
    blob = subprocess.run(["git", "show", f"{rev}:{path}"], cwd=ROOT,
                          capture_output=True, text=True, check=True).stdout
    tmp = Path(tempfile.mkdtemp()) / Path(path).name
    tmp.write_text(blob, encoding="utf-8")
    return tmp


def main() -> None:
    code = sys.argv[1]
    rev = sys.argv[sys.argv.index("--from") + 1]
    spec = importlib.util.spec_from_file_location(
        f"lang_{code}", ROOT / "tools" / f"lang_{code}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    out = ['"""自动固化自序号版本，键为英文原文。请勿再按序号编辑。"""',
           "", f"META = {mod.META!r}", ""]
    for attr, page, name in (("INDEX_BY_NO", "en/index.html", "INDEX"),
                             ("PROTECTION_BY_NO", "en/protection.html",
                              "PROTECTION")):
        by_no = getattr(mod, attr, {})
        keys = ordered_keys(at_revision(rev, page))
        merged = dict(getattr(mod, name, {}))
        for no, text in sorted(by_no.items()):
            if not 1 <= no <= len(keys):
                raise SystemExit(f"❌ {code} {attr}: 序号 {no} 超出 {len(keys)}")
            merged[keys[no - 1]] = text
        out.append(f"{name} = {{")
        for k, v in merged.items():
            out.append(f"    {k!r}:\n        {v!r},")
        out.append("}")
        out.append("")
        print(f"  {code}.{name}：固化 {len(merged)} 条")

    (ROOT / "tools" / f"lang_{code}.py").write_text("\n".join(out) + "\n",
                                                    encoding="utf-8")
    print(f"✅ tools/lang_{code}.py 已改为按英文原文索引")


main()
