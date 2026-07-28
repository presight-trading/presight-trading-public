# 先见交易学院 · Presight Trading Institute

静态官网。无构建步骤、无依赖，纯 HTML / CSS / 原生 JS，任何静态托管都能直接部署。

---

## 文件结构

```
presight-site/
├── index.html                    首页
├── 404.html                      错误页
├── assets/
│   ├── css/style.css             全部样式
│   ├── js/config.js              ← 上线前只需要改这个文件
│   ├── js/app.js                 渲染逻辑，一般不用动
│   └── favicon.svg               站点图标
├── .github/workflows/deploy.yml  GitHub Pages 自动部署
├── .nojekyll                     关闭 Jekyll 处理
└── robots.txt
```

---

## 一、部署到 GitHub Pages

```bash
git init
git add .
git commit -m "init: presight trading institute"
git branch -M main
git remote add origin git@github.com:<你的账号>/<仓库名>.git
git push -u origin main
```

然后在仓库里打开 **Settings → Pages**，把 **Source** 设为 **GitHub Actions**。

推送后 Actions 会自动跑 `deploy.yml`，一两分钟内站点上线，地址是
`https://<你的账号>.github.io/<仓库名>/`

### 绑定自己的域名

1. 仓库根目录新建 `CNAME` 文件，内容一行，写你的域名（不带 `https://`、不带斜杠）：

   ```
   presighttrading.com
   ```

2. DNS 侧添加记录：

   | 类型 | 主机 | 值 |
   |---|---|---|
   | A | `@` | `185.199.108.153` |
   | A | `@` | `185.199.109.153` |
   | A | `@` | `185.199.110.153` |
   | A | `@` | `185.199.111.153` |
   | CNAME | `www` | `<你的账号>.github.io` |

3. 回到 Settings → Pages 填入域名，等证书签发后勾上 **Enforce HTTPS**。

> GitHub 的 Pages IP 偶尔会调整，配置前建议对一下官方文档的当前值。

### 换成 Cloudflare Pages / Vercel / Netlify

这三家都不需要改任何代码：连接仓库，**Build command 留空**，**Output directory 填 `/`**（根目录），保存即可。国内访问速度考虑，Cloudflare Pages 通常比 GitHub Pages 稳。

---

## 二、上线前必须改的地方

### 1. `assets/js/config.js`

```js
const CONFIG = {
  tradesEndpoint : '',   // 你的成交记录 API，留空则显示演示数据
  brokerSignupUrl: '',   // 交易平台注册链接（带你的推广参数）
  communityUrl   : '',   // Telegram / 社区入口
  refreshMs      : 60000,
  rowLimit       : 12,
};
```

**接入你的 API**：把 `tradesEndpoint` 填上，页面会每 60 秒拉一次。期望的返回格式（数组，按平仓时间倒序）：

```json
[
  {
    "closedAt"  : "2026-07-28T09:41:00Z",
    "symbol"    : "XAUUSD",
    "side"      : "buy",
    "lots"      : 0.40,
    "openPrice" : 2412.35,
    "closePrice": 2419.80,
    "pips"      : 74.5,
    "pnl"       : 298.00
  }
]
```

字段名不一样也没关系，改 `config.js` 里的 `normalize()` 一个函数即可，渲染逻辑不用碰。

指标区（净收益 / 胜率 / 最大回撤 / 盈亏比 / 成交笔数）和净值曲线都是**从这份成交记录实时算出来的**，不是写死的数字。

**注意 CORS**：API 需要对你的站点域名返回 `Access-Control-Allow-Origin`，否则浏览器会拦掉请求。前端拿不到数据时页面会显示重试提示，不会白屏。

### 2. `index.html` 里的三处占位

搜索 `【` 就能定位，共三处：

- **赔付条款**（FAQ 第一条）—— 需写明触发条件、计算基准、赔付上限、到账周期、除外情形
- **最低入金要求**（FAQ 最后一条）
- **运营主体信息**（风险提示第三段）—— 主体全称、注册地、持牌情况或明确的未持牌声明、合作平台及其监管机构、地区限制

### 3. 分享卡片

`index.html` 的 `<head>` 里有 Open Graph 标签，把 `og:url` 和 `og:image` 换成你的正式域名。`og:image` 需要你自己出一张 **1200×630 的 PNG**，放到 `assets/og.png`。目前这个路径下没有文件，微信和 Telegram 转发时不会有预览图。

---

## 三、设计说明

整站是一张**绘图画布**：方格纸底纹、坐标轴刻度、图注式小标题（FIG. 01 / 02）。凡是出现真实数据的区块（策略面板、成交表、净值曲线）都嵌一块深色仪表盘——营销层明亮，数据层像终端。

签名元素是**实线转虚线**：钴蓝实线代表已实现，品红虚线代表模型前瞻，中间一条 `NOW` 分割线。这是绘图库里「实际值 vs 预测值」的通用画法，也正是「先见」两个字。这个母题重复在 logo、首屏图和章节分隔线上。

| | |
|---|---|
| 画布 | `#EDF0F4` 冷调白，非米色 |
| 墨色 | `#0A111E` |
| 已实现 | `#1B3BD8` 钴蓝 |
| 前瞻 | `#D6188A` 品红，**永远虚线** |
| 深色面板 | `#0A111E` / `#141E33` |
| 提示 | `#C97A05` |
| 字体 | Archivo（标题正文）+ JetBrains Mono（数据）+ 系统中文栈 |

中文标题有独立字级（`.display.han`），比拉丁字母小一档、行高更宽——全宽字用拉丁字体的紧行距会挤成一坨。

已处理：移动端响应式、键盘焦点可见、`prefers-reduced-motion` 生效、加载 / 失败 / 空数据三种状态。

中文正文走系统字体栈（PingFang SC / 微软雅黑 / 思源黑体），没有引入中文 Web 字体——一个中文字重动辄几 MB，不值得。

---

## 四、合规提醒

首屏的「跟单亏损包赔」标签是按需求做进去的，但请注意：

- **保证不亏损**类表述在 ASIC、MAS、FCA、CySEC 等辖区对金融产品营销基本属于禁止范围
- Google Ads 与 Meta 的金融服务政策明确禁止保证收益类宣称，挂着这个标签大概率投不了广告
- 合作交易平台的合规部门看到自己的推广页写着包赔，有可能直接停掉你的推广链接

页面里已经预留了缓冲：标签后面挂了「赔付条款」锚点，FAQ 第一条就是条款位。**务必写成有明确边界的有限赔付承诺**——条款写细，法律上安全得多，转化上也比含糊的「包赔」更有说服力。

---

## License

私有项目，未开放许可。
