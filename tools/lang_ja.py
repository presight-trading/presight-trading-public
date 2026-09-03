"""日本語。キーは英語版の innerHTML そのまま。

固有名詞は訳さない：PRESIGHT ALPHA-1 / DecodeFX / @PresightAdminBot /
presighttrading_com - signal 1 / Autoscale / Value by asset / Ratio。
これらは画面上でそのまま入力・検索する文字列なので、訳すと操作できなくなる。
"""

META = {
    "lang": "ja",
    "label": "日本語",
    "dir": "ja",
    "share": "https://presighttrading.com/ja/#partner",
    "title_index": "Presight Trading Institute — 先を見て、先に動く。",
    "desc_index": "先を見て、先に動く。自己資金で運用するコピートレード用クオンツ戦略。"
                  "約定はすべて公開。マルチアセットのシグナルコミュニティは無料。",
    "title_prot": "コピートレード損失補償 · プログラム規約 — PRESIGHT Trading Institute",
    "desc_prot": "Presight コピートレード損失補償プログラムの完全規約："
                 "口座の届出、1 か月の保護期間、基準資金、補償額の計算、除外事由、確認手続き。",
    "og_title": "Presight Trading Institute — 先を見て、先に動く。",
    "og_desc": "先を見て、先に動く。",
}

INDEX = {
    # ---- ナビゲーション ----
    "Loss coverage": "損失補償",
    "Strategy": "戦略",
    "Community": "コミュニティ",
    "Get started": "始め方",
    "FAQ": "よくある質問",
    'Start copying <span class="arw">→</span>': 'コピーを始める <span class="arw">→</span>',

    # ---- ヒーロー ----
    "FIG. <b>00</b> — PRESIGHT": "FIG. <b>00</b> — PRESIGHT",
    'See first.<br/><span class="fx">Move first.</span>':
        '先を見て、<br/><span class="fx">先に動く。</span>',
    "The strategy runs on our own capital, with every fill published and no losing trade "
    "filtered out. If you finish the copy period down, we <b>refund that loss in cash</b>.":
        "戦略は自己資金で実運用しています。約定はすべて公開し、負けトレードも一件も伏せません。"
        "コピー期間を終えて口座が負けていれば、その損失を<b>現金で返金</b>します。",
    "Losses covered": "損失補償",
    "your loss, refunded<i>/</i>paid in cash":
        "負けた分を返金<i>/</i>現金で着金",
    "Full terms →": "規約全文 →",
    'How coverage works <span class="arw">→</span>':
        '補償のしくみ <span class="arw">→</span>',
    "Browse past signals": "過去のシグナルを見る",
    "Live account · fills sync every 60s · coverage is capped at your base capital and does "
    "not remove trading risk · leveraged trading can cost you your entire deposit":
        "実口座で運用 · 約定は 60 秒ごとに同期 · 補償は基準資金が上限で、取引リスクをなくすものではありません "
        "· レバレッジ取引では預託金の全額を失う可能性があります",
    '<span><i class="sw"></i> REALIZED</span>\n<span><i class="sw d"></i> PROJECTED</span>':
        '<span><i class="sw"></i> 実績</span>\n<span><i class="sw d"></i> モデル予測</span>',

    # ---- 指標ストリップ ----
    "Live Since": "運用日数",
    "Total Return": "累計リターン",
    "Win Rate": "勝率",
    "Loss Cover": "損失補償",
    "Cash refund": "現金返金",

    # ---- 補償セクション ----
    "FIG. <b>01</b> — HEADLINE OFFER": "FIG. <b>01</b> — 主要プログラム",
    "Loss coverage on copied trades": "コピートレード損失補償",
    "Copy within the rules and we cover the loss. This is not a promise that you cannot lose "
    "— we share the downside of that period, once leverage and manual intervention are "
    "constrained. The conditions are specific because that is the only way the commitment "
    "stays payable.":
        "ルールどおりにコピーして負けたら、こちらが補償します。「絶対に負けない」という約束ではありません。"
        "レバレッジと手動介入を縛ったうえで、その期間の下振れを一緒に負う、という話です。"
        "条件を細かく書いているのは、そうしないと約束が支払えなくなるからです。",
    "1:1 copy ratio, no scaling up": "1:1 でコピー、建玉を拡大しない",
    "All you set is the 1:1 ratio. Per-trade risk and aggregate exposure are <b>managed by us "
    "at the copy-account level</b> — ALPHA-1 is a quantitative strategy, and holding several "
    "positions at once is normal structure, not something you need to configure.":
        "あなたが設定するのは 1:1 の比率だけです。1 トレードあたりのリスクと合計エクスポージャーは"
        "<b>こちらがコピー口座の側で一括管理</b>します。ALPHA-1 はクオンツ戦略で、"
        "同時に複数のポジションを持つのは正常な構造です。あなたが設定する必要はありません。",
    "Account-level drawdown control": "口座単位のドローダウン管理",
    "The strategy account has drawdown thresholds; on breach it automatically reduces size or "
    "stops opening new positions, and copy accounts follow. The strategy never averages down.":
        "戦略口座にはドローダウンの閾値があり、触れると自動でロットを落とすか新規建てを止めます。"
        "コピー口座もこれに追随します。戦略はナンピンも両建て平均化も行いません。",
    "One month, net loss refunded": "1 か月で、純損失を現金返金",
    "A full month of copying from the moment you report your MT5 account ID in the community, "
    "with no manual intervention and no withdrawals. If equity ends below base capital, the "
    "shortfall is refunded in <b>USD cash</b> within 10 business days of verification. Losses "
    "on positions you closed by hand are not covered.":
        "MT5 口座 ID を届け出た時点から、手動介入も出金もせずに 1 か月コピーを続けます。"
        "期間終了時の有効証拠金が基準資金を下回っていれば、その差額を<b>米ドル現金</b>で、"
        "確認完了後 10 営業日以内に返金します。ご自身で手仕舞いした建玉の損失は対象外です。",
    '<span class="mono">⚠</span> Before you join': '<span class="mono">⚠</span> 参加する前に',
    "Coverage is limited to <b>the full amount of your base capital</b>. Once copying starts "
    "you must <b>report your MT5 account ID</b> to <span class=\"mono\">@PresightAdminBot</span> "
    "on Telegram — an unreported account is not eligible, and losses incurred before you report "
    "are not covered. Opening trades manually, raising the Ratio above 1, or withdrawing during "
    "the period all void eligibility, and <b>losses on positions you close by hand are never "
    "refunded</b>.":
        "補償の上限は<b>基準資金の全額</b>です。コピーを始めたら、Telegram で "
        '<span class="mono">@PresightAdminBot</span> に<b>MT5 口座 ID を届け出て</b>ください。'
        "届出のない口座は対象外で、届出より前に生じた損失も補償されません。"
        "手動での新規建て、Ratio を 1 より大きくすること、期間中の出金は、いずれも資格を失います。"
        "また<b>ご自身で手仕舞いした建玉の損失は一切返金されません</b>。",
    "Full terms and exclusions →": "規約全文と除外事由 →",
    'Open an account &amp; copy <span class="arw">→</span>':
        '口座開設してコピーする <span class="arw">→</span>',
    "Read the full terms": "規約全文を読む",

    # ---- 戦略セクション ----
    "FIG. <b>02</b> — FLAGSHIP": "FIG. <b>02</b> — 主力",
    "Copy-trading strategy": "コピートレード戦略",
    "A multi-asset quant strategy running on a live account. Once linked, entries and exits "
    "mirror to your account automatically — no direction calls, no screen time. The table below "
    "is that account’s complete fill history. Losing trades included.":
        "実口座で運用しているマルチアセットのクオンツ戦略です。紐付けが済めば、"
        "新規建てと決済が自動であなたの口座に反映されます。方向を当てる必要も、"
        "画面に張り付く必要もありません。下の表はその口座の全約定履歴です。負けトレードも含みます。",
    "Low-to-mid frequency trend following with a volatility filter. Major pairs, metals and "
    "indices. Fixed risk per position, no averaging down.":
        "ボラティリティ・フィルターを備えた中低頻度のトレンドフォロー。主要通貨ペア、貴金属、株価指数。"
        "1 ポジションあたりのリスクは固定、ナンピンなし。",
    "Full terms": "規約全文",
    "MULTI-ASSET": "マルチアセット",
    "AUTO-COPY": "自動コピー",
    "FIXED RISK": "リスク固定",
    "Net P&amp;L": "純損益",
    "Win rate": "勝率",
    "Max drawdown": "最大ドローダウン",
    "Profit factor": "プロフィットファクター",
    "Trades": "トレード数",
    "Fill history · last 12": "約定履歴 · 直近 12 件",
    "Closed": "決済日時",
    "Symbol": "銘柄",
    "Side": "売買",
    "Lots": "ロット",
    "Entry": "建値",
    "Exit": "決済値",
    "Pips": "pips",
    "P&amp;L (USD)": "損益（USD）",
    "Copy trading runs inside the partner platform. Only accounts registered through the link "
    "below can subscribe to this strategy.":
        "コピートレードは提携プラットフォーム内で完結します。下のリンクから登録した口座だけが"
        "この戦略を購読できます。",
    'Register and link account <span class="arw">→</span>':
        '口座開設してコピーを紐付ける <span class="arw">→</span>',

    # ---- コミュニティ ----
    "FIG. <b>03</b> — FLAGSHIP": "FIG. <b>03</b> — 主力",
    "Presight Trading Community": "Presight トレーディング・コミュニティ",
    "<span>$0</span><s>free, permanently</s>": "<span>$0</span><s>ずっと無料</s>",
    "No courses for sale, no membership fees, no call groups. Everything in the community is "
    "open, including the signals the live strategy runs on.":
        "教材販売なし、会費なし、有料サロンなし。実運用中の戦略が使っているシグナルも含め、"
        "コミュニティの中身はすべて公開です。",
    'Public signal channel <span class="arw">→</span>':
        '公開シグナルチャンネル <span class="arw">→</span>',
    "Trading Institute — open to all": "Trading Institute — 誰でも参加可",
    "<b>Scan to open the signal channel</b>\n            This is the main public entry point "
    "— no application needed.\n            Community discussion lives at "
    "<b>@presight_institute</b>, also open.\n            <span class=\"h\">Or search "
    "@presight_signals in Telegram</span>":
        "<b>読み取るとシグナルチャンネルが開きます</b>\n            これが対外的な入口です。申請は不要です。"
        "\n            議論の場は<b>@presight_institute</b>、こちらも公開です。"
        '\n            <span class="h">Telegram で @presight_signals を検索してもかまいません</span>',
    "01 / SIGNALS": "01 / シグナル",
    "Multi-asset signals": "マルチアセットのシグナル",
    "FX, metals, oil, indices and crypto. Every signal carries an entry range, stop, target and "
    "model confidence, pushed to Telegram and the community channel.":
        "FX、貴金属、原油、株価指数、暗号資産。各シグナルにはエントリー範囲、損切り、"
        "目標、モデルの確信度が付きます。Telegram とコミュニティチャンネルに配信します。",
    "02 / RESEARCH": "02 / リサーチ",
    "Market analysis": "相場分析",
    "Daily pre-market briefs and a weekly macro review, explaining what drove the move rather "
    "than fitting a story to it afterwards.":
        "毎日の寄り付き前ブリーフと週次のマクロ振り返り。後付けの物語ではなく、"
        "何がその値動きを起こしたのかを説明します。",
    "03 / TRAINING": "03 / 教育",
    "Trading education": "トレード教育",
    "From what spread and slippage actually cost you, through position sizing and spotting "
    "overfitting in a backtest. Full course and live Q&amp;A, all open.":
        "スプレッドとスリッページが実際いくらの負担になるかから、ロット設計、"
        "バックテストの過剰最適化の見抜き方まで。講座も生 Q&amp;A も全部公開です。",
    "04 / EVENTS": "04 / イベント",
    "Events": "イベント",
    "Demo competitions, live-account challenges and open strategy builds. Prize money and funded "
    "accounts. No entry requirement.":
        "デモ大会、実口座チャレンジ、戦略の共同開発。賞金と資金提供口座あり。参加条件はありません。",

    # ---- 始め方 ----
    "FIG. <b>04</b> — PROCESS": "FIG. <b>04</b> — 手順",
    "Four steps to start copying": "4 ステップでコピーを開始",
    "Register through the link": "リンクから口座開設",
    "Open an account with the partner platform using the link on this site and complete "
    "verification. Only accounts opened this way can subscribe to the strategy.":
        "当サイトのリンクから提携プラットフォームで口座を開設し、本人確認を完了してください。"
        "この経路で開いた口座だけが戦略を購読できます。",
    "Fund and subscribe": "入金して購読",
    'Log in at <span class="mono">secure.decodefx.com</span> → <b>Copy Trading</b>, sign in with '
    'your MT5 copy account credentials, open <b>New subscription</b>, and set Provider to '
    '<span class="mono">presighttrading_com - signal 1</span>. Copy settings: <b>Autoscale</b>, '
    '<b>Value by asset</b>, <b>Ratio 1</b> (a 1:1 mirror, no scaling up). Per-trade risk is set '
    'on our side — you do not configure it.':
        '<span class="mono">secure.decodefx.com</span> にログイン → <b>Copy Trading</b>、'
        'MT5 コピー口座の ID とパスワードでサインイン、<b>New subscription</b> を開き、'
        'Provider に <span class="mono">presighttrading_com - signal 1</span> を入力。'
        '設定は <b>Autoscale</b>、<b>Value by asset</b>、<b>Ratio 1</b>（1:1、拡大しない）。'
        '1 トレードあたりのリスクはこちらで設定するので、あなたが触る必要はありません。',
    "Report your MT5 account ID": "MT5 口座 ID を届け出る",
    'Message <span class="mono">@PresightAdminBot</span> on Telegram with your MT5 account ID '
    '(login number); it replies with a receipt immediately. The protection period starts from '
    'that moment — an unreported account is not eligible, and losses before you report are not '
    'covered.':
        'Telegram で <span class="mono">@PresightAdminBot</span> に MT5 口座 ID（ログイン番号）'
        'を送ってください。その場で受付の返信が届きます。保護期間はこの瞬間から始まります。'
        '届出のない口座は対象外で、届出より前の損失は補償されません。',
    "Copy for a month": "1 か月コピーする",
    "Every entry and exit mirrors to your account; a full month of continuous copying completes "
    "the protection period. You can pause or unlink at any time from inside the platform, but "
    "doing so ends coverage for that enrolment.":
        "新規建てと決済はすべてあなたの口座に反映されます。1 か月続けてコピーすると"
        "保護期間が満了します。プラットフォーム内でいつでも停止・解除できますが、"
        "その時点でその回の補償は終了します。",

    # ---- FAQ ----
    "FIG. <b>05</b> — FAQ": "FIG. <b>05</b> — よくある質問",
    "About the strategy and copy trading": "戦略とコピートレードについて",
    "How is the loss coverage triggered and calculated?": "補償はどう発生し、どう計算しますか？",
    "What do I have to do to qualify?": "対象になる条件は？",
    "Do I have to use the specified platform?": "指定のプラットフォームでないと駄目ですか？",
    "Yes. Copy trading is a signal-sync mechanism inside the platform, and only accounts "
    "registered through this site’s link appear on the subscription list. Accounts you already "
    "hold elsewhere cannot be connected.":
        "はい。コピートレードはプラットフォーム内部のシグナル同期のしくみで、"
        "当サイトのリンクから登録した口座だけが購読リストに載ります。"
        "他所で既にお持ちの口座は接続できません。",
    "How do you make money? Why is the community free?":
        "収益源は？なぜコミュニティは無料なのですか？",
    "Copy-trading revenue comes from partner rebates and a share of strategy performance, "
    "scaling with copied volume. When the strategy earns nothing, neither do we — our incentives "
    "point the same way as yours. The community is an acquisition channel and is not billed "
    "separately.":
        "収益は提携先からのリベートと戦略成績の分配で、コピー規模に連動します。"
        "戦略が稼がなければ、こちらの収益もゼロです。利害の向きが同じということです。"
        "コミュニティは集客の入口であって、別途課金はしません。",
    "Is the track record filtered?": "実績は選別されていませんか？",
    "The fills on this page come straight from the strategy’s live account with no filtering, "
    "and losing trades are listed alongside the rest. Past performance does not indicate future "
    "results, and every strategy has drawdown periods.":
        "このページの約定は戦略の実口座から無選別でそのまま出しており、負けトレードも並べています。"
        "過去の成績は将来の結果を示すものではなく、どんな戦略にもドローダウン期間があります。",
    "What is the minimum deposit?": "最低入金額はいくらですか？",
    "[Fill in the minimum deposit.] Note that below a certain account size, lot rounding pushes "
    "the actual copy ratio away from the one you set, which can push the effective ratio away "
    "from 1:1 and <b>void your coverage</b>. Leave headroom; ask in the community for the "
    "current threshold.":
        "【最低入金額をここに記入】ご注意：口座残高が一定を下回ると、ロットの丸めによって"
        "実際のコピー比率が設定値からずれ、実効比率が 1:1 から外れて<b>補償の対象外</b>に"
        "なることがあります。余裕を持って入金してください。現在の目安はコミュニティでお尋ねください。",
    '<span class="mono">⚠</span> Risk warning': '<span class="mono">⚠</span> リスク警告',
    "Contracts for difference, foreign exchange and other leveraged products carry a high level "
    "of risk and can result in the loss of all invested capital. They are not suitable for every "
    "investor. Before trading, make sure you understand the risks involved and consider your "
    "experience, financial position and tolerance for loss.":
        "差金決済取引、外国為替その他のレバレッジ商品は高いリスクを伴い、"
        "投下資金の全額を失う可能性があります。すべての投資家に適した商品ではありません。"
        "取引の前にリスクを理解し、ご自身の経験、財務状況、損失に耐えられる度合いをご検討ください。",
    "Signals, analysis and educational material on this site are provided for information only "
    "and do not constitute investment advice, an offer or a solicitation. Past performance does "
    "not indicate future results. Your trading decisions and their outcomes are your own.":
        "当サイトのシグナル、分析、教育コンテンツは情報提供のみを目的としており、"
        "投資助言、申込みの勧誘のいずれでもありません。過去の成績は将来の結果を示しません。"
        "取引の判断とその結果はご自身に帰属します。",
    "[Add here: the operating entity’s full legal name and place of registration, its licensing "
    "status or an explicit statement that it is unlicensed, the partner platform and its "
    "regulator, and any territorial restrictions.]":
        "【ここに追記：運営主体の正式名称と登記地、ライセンスの有無（無登録ならその旨を明記）、"
        "提携プラットフォーム名とその監督当局、および地域制限】",

    # ---- IB ----
    "FIG. <b>06</b> — PARTNERS": "FIG. <b>06</b> — パートナー",
    "Introducing brokers": "紹介パートナー（IB）",
    "Bring people to Presight and keep half the commission. The clients you introduce are "
    "covered by the loss-coverage programme too.":
        "Presight を紹介して、手数料の半分を受け取ってください。"
        "紹介したお客様も損失補償プログラムの対象になります。",
    "Commission": "報酬",
    '<span class="u">50%</span> revenue share': '<span class="u">50%</span> レベニューシェア',
    "Half of the commission your clients generate is yours. Settlement and statements live in "
    "the partner platform’s back office; we never touch the money.":
        "あなたのお客様が生む手数料の半分があなたのものです。精算と明細は提携プラットフォームの"
        "管理画面にあり、資金を Presight が預かることはありません。",
    "Coverage": "補償",
    "Your clients get loss coverage": "紹介したお客様も補償対象",
    "Clients who register through your link and copy the strategy fall under the same "
    "loss-coverage programme, on the terms published here.":
        "あなたのリンクから登録してコピーを始めたお客様は、当サイト掲載の規約どおり、"
        "同じ損失補償プログラムの対象になります。",
    "Threshold": "条件",
    '<span class="u">3</span> clients · <span class="u">USD 500</span> each':
        '<span class="u">3</span> 名 · 各 <span class="u">500 米ドル</span>',
    "What unlocks that coverage: at least 3 clients under you, each funding the account with no "
    "less than USD 500.":
        "補償が有効になる条件：あなたの下に 3 名以上のお客様がいて、"
        "それぞれが 500 米ドル以上を入金していること。",
    "Register on the partner link": "パートナー用リンクから登録",
    "The link below is <b>not the same one</b> clients use. Register on the wrong one and the "
    "application button never appears — you would have to start over.":
        "下のリンクは、お客様が使うものとは<b>別のリンク</b>です。間違えて登録すると"
        "管理画面に申請ボタンが出ず、口座を取り直すしかなくなります。",
    "Apply in the back office": "管理画面から IB を申請",
    "Log in to the DecodeFX back office and press “Apply to become an IB”. Once approved you get "
    "a referral link of your own.":
        "DecodeFX の管理画面にログインし、「Apply to become an IB」を押してください。"
        "承認されると、あなた専用の紹介リンクが発行されます。",
    "Invite with your own link": "自分のリンクで紹介",
    "Everyone who registers through your link counts as yours, at a 50% revenue share. "
    "Statements are in the back office.":
        "以後あなたのリンクから登録した人はすべてあなたの実績になり、報酬は 50% です。"
        "明細は管理画面で確認できます。",
    "Share this link to recruit IBs": "IB 募集にはこのリンク",
    "Copy": "コピー",
    'Register and apply <span class="arw">→</span>':
        '登録して IB を申請する <span class="arw">→</span>',
    "Read the coverage terms": "先に補償規約を読む",
    '<span class="mono">⚠</span> Notes': '<span class="mono">⚠</span> 注意事項',
    "published programme terms": "掲載中のプログラム規約",
    "Promotion must not use language such as “guaranteed profit” or “risk-free”, and must not "
    "involve trading on a client’s behalf or holding client funds. We end partnerships that do.":
        "販促にあたって「必ず儲かる」「元本保証」といった表現は使えません。"
        "また、お客様に代わって売買すること、お客様の資金を預かることも禁止です。"
        "違反があった提携関係は終了します。",

    # ---- フッター ----
    "See first. Move first.": "先を見て、先に動く。",
    "Presight Trading Institute · Quantitative strategy and trading education":
        "Presight Trading Institute · クオンツ戦略とトレード教育",
    "Product": "プロダクト",
    "Partner programme": "紹介パートナー",
    "Copy trading": "コピートレード",
    "Community signals": "コミュニティ・シグナル",
    "Education": "トレード教育",
    "Resources": "資料",
    "Coverage terms": "補償プログラム規約",
    "Strategy factsheet": "戦略説明書",
    "Track record (CSV)": "実績データ（CSV）",
    "Contact": "連絡先",
    "Public signal channel": "公開シグナルチャンネル",
    "Trading Institute": "Trading Institute",
    "Email": "メール",
    "Partnerships": "業務提携",
    "<span>© 2026 PRESIGHT TRADING INSTITUTE</span>\n<span>Trading involves risk</span>":
        "<span>© 2026 PRESIGHT TRADING INSTITUTE</span>\n<span>取引にはリスクが伴います</span>",

    # ---- モーダル ----
    "FIG. <b>00</b> — GETTING STARTED": "FIG. <b>00</b> — 始め方",
    "Three steps to start copying": "3 ステップでコピーを開始",
    "Ten minutes, start to finish. <b>Step 3 is what makes you eligible for coverage</b> — do "
    "not skip it.":
        "全部で 10 分ほどです。<b>補償の対象になるかどうかはステップ 3 で決まります</b>。"
        "飛ばさないでください。",
    "Open an account and fund it": "口座開設して入金",
    "Only a <b>new account</b> opened through this link is on the subscription list. Complete "
    "verification (KYC), then deposit.":
        "購読リストに載るのは、このリンクから開いた<b>新規口座</b>だけです。"
        "本人確認（KYC）を済ませてから入金してください。",
    'Register with DecodeFX <span class="arw">→</span>':
        'DecodeFX で登録する <span class="arw">→</span>',
    "Subscribe to PRESIGHT ALPHA-1": "PRESIGHT ALPHA-1 を購読",
    "<b>secure.decodefx.com</b> → Copy Trading → sign in with your MT5 copy account → New "
    "subscription<br/>\n            Provider: <b>presighttrading_com - signal 1</b><br/>\n"
    "            Settings: <b>Autoscale</b> · <b>Value by asset</b> · <b>Ratio = 1</b>":
        "<b>secure.decodefx.com</b> → Copy Trading → MT5 コピー口座でサインイン → New "
        "subscription<br/>\n            Provider：<b>presighttrading_com - signal 1</b><br/>\n"
        "            設定：<b>Autoscale</b> · <b>Value by asset</b> · <b>Ratio = 1</b>",
    "Ratio 1 is a 1:1 mirror. Anything above 1 scales up your position and voids coverage "
    "outright.":
        "Ratio 1 が 1:1 です。1 より大きくすると建玉を拡大したことになり、"
        "その時点で補償の対象外になります。",
    "Report your MT5 account ID to the bot": "MT5 口座 ID を bot に届け出る",
    "Send it your login number — just the digits — and you get an immediate receipt. <b>The "
    "protection period starts from that moment</b>; losses before it are not covered, so report "
    "as soon as the account is open.":
        "ログイン番号（数字だけ）を送れば、その場で受付の返信が届きます。"
        "<b>保護期間はその瞬間から始まります</b>。それ以前の損失は補償されないので、"
        "口座ができたらすぐに届け出てください。",
    'Message @PresightAdminBot <span class="arw">→</span>':
        '@PresightAdminBot に送る <span class="arw">→</span>',
    "Send the login number only — <b>never your password</b>. We will never ask you for a "
    "password, a verification code or funds.":
        "送るのはログイン番号だけです。<b>パスワードは絶対に送らないでください</b>。"
        "こちらからパスワード、認証コード、資金をお願いすることは一切ありません。",
    "Questions? Join the community": "質問があればコミュニティへ",
    "Full programme terms →": "プログラム規約全文 →",

    # ---- 属性 ----
    "@Presight Trading Institute home": "Presight Trading Institute ホーム",
    "@Strategy equity curve. Solid line is realized, dashed line is the model projection.":
        "戦略の資産推移。実線が実績、破線がモデル予測です。",
    "@Cumulative strategy equity curve": "戦略の累積資産推移",
    "@Scan to open the Presight signal channel":
        "読み取ると Presight のシグナルチャンネルが開きます",
    "@Close": "閉じる",
}

PROTECTION = {
    "FIG. A — PROGRAMME TERMS": "FIG. A — プログラム規約",
    "Loss coverage on copied trades": "コピートレード損失補償",
    "If you copy the strategy under the conditions below for a full month and the account is "
    "still down at the end of the protection period, we refund that loss in cash.":
        "以下の条件どおりに 1 か月コピーを続け、保護期間の終了時点で口座がなお負けていれば、"
        "その損失を現金で返金します。",
    "The programme is built on <b>shared downside</b>, not a promise that you cannot lose. The "
    "conditions are specific because the commitment is only payable if leverage and manual "
    "intervention are constrained — otherwise participants who scale up would file claims far "
    "beyond what the programme can absorb, and everyone in it would lose out. Please read it in "
    "full before joining.":
        "この制度の考え方は<b>下振れを一緒に負う</b>ことであって、「絶対に負けない」ではありません。"
        "条件を細かく書いているのは、レバレッジと手動介入を縛らないと約束が支払えなくなるからです。"
        "縛らなければ建玉を拡大した参加者から制度が吸収できない額の請求が来て、"
        "最後に損をするのは参加者全員です。参加前に最後までお読みください。",
    "In one sentence": "ひとことで言うと",
    "Eligibility": "参加条件",
    "<b>All</b> of the following must hold. Any one of them failing puts you outside the "
    "coverage.":
        "以下を<b>すべて</b>満たす必要があります。一つでも欠ければ補償の対象外です。",
    "A <b>new account</b> with the partner platform, opened through an official Presight link "
    "and KYC-verified. Existing accounts cannot be enrolled.":
        "Presight の公式リンクから開設し、本人確認（KYC）を完了した提携プラットフォームの"
        "<b>新規口座</b>であること。既存口座は登録できません。",
    "Risk control happens on our side": "リスク管理はコピー口座の側でこちらが行う",
    "ALPHA-1 is a quantitative strategy and may hold several positions at once — that is how the "
    "strategy is built, not a sign that risk is loose. So we <b>do not ask you to set your own "
    "per-trade risk or position-count limits</b>. Those parameters are not really under your "
    "control, and putting them in the terms would only create grounds for arguing after the fact.":
        "ALPHA-1 はクオンツ戦略で、同時に複数のポジションを持つことがあります。"
        "これは戦略の構造であって、リスク管理が緩いわけではありません。"
        "ですから<b>1 トレードあたりのリスクや同時保有数の上限をあなたに設定させることはしません</b>。"
        "それらは実際にはあなたが制御できないもので、規約に書けば事後の言い争いの材料になるだけです。",
    "Risk is managed by us at the <b>copy-account level</b>:":
        "リスクは<b>コピー口座の側</b>でこちらが一括管理します：",
    "<b>Drawdown control</b>: the strategy account has drawdown thresholds; on breach it "
    "automatically reduces size or stops opening new positions, and copy accounts follow.":
        "<b>ドローダウン管理</b>：戦略口座には閾値があり、触れると自動でロットを落とすか"
        "新規建てを止めます。コピー口座も追随します。",
    "<b>Fixed per-trade risk</b>: exposure per trade is set on the master account and mirrored "
    "to yours at a 1:1 ratio. It does not scale up with your balance.":
        "<b>1 トレードのリスクは固定</b>：エクスポージャーはマスター口座側で決まり、"
        "1:1 であなたの口座に反映されます。残高が増えても拡大しません。",
    "<b>Aggregate exposure monitored</b>: total risk across open positions is managed by the "
    "strategy, so it does not stack linearly with position count.":
        "<b>合計エクスポージャーを監視</b>：保有中の全ポジションの合計リスクは戦略側で管理しており、"
        "建玉数に比例して積み上がることはありません。",
    "<b>No averaging down</b>: the strategy does not add to losing positions and does not "
    "martingale.":
        "<b>ナンピンしない</b>：戦略は含み損のポジションに追加せず、マーチンゲールも行いません。",
    "All you need to do is set the copy ratio to 1:1 and leave it alone.":
        "あなたがやることは、コピー比率を 1:1 にして、あとは触らないことだけです。",
    "Protection period": "保護期間",
    "Starts": "起算",
    "Length": "期間",
    "<b>One month &mdash; 30 consecutive calendar days</b>":
        "<b>1 か月 &mdash; 連続 30 暦日</b>",
    "Before reporting": "届出より前",
    "Extension": "延長",
    "Termination": "終了",
    "Pausing or unsubscribing during the period voids coverage; nothing is payable":
        "期間中に停止または解除すると補償は即座に失効し、支払いは行われません",
    "Base capital": "基準資金",
    "Protected amount": "補償上限",
    "<b>The full amount of base capital</b>": "<b>基準資金の全額</b>",
    "Withdrawals": "出金",
    "A withdrawal during the period recalculates base capital to the lowest post-withdrawal "
    "equity and voids that enrolment":
        "期間中に出金があった場合、基準資金は出金後の最低有効証拠金で再計算され、"
        "その回の参加資格は失われます",
    "How the payout is calculated": "補償額の計算",
    "<b>Net loss = base capital &minus; account equity at the end of the protection period</b>":
        "<b>純損失 = 基準資金 &minus; 保護期間終了時の有効証拠金</b>",
    "Net loss &le; 0 (account flat or in profit): nothing is payable.":
        "純損失 &le; 0（口座が同値または利益）：支払いは発生しません。",
    "Trades closed by the strategy are collectively in profit: nothing is payable.":
        "戦略が決済したトレードの合計が利益：支払いは発生しません。",
    "Both are losses: the smaller of the two amounts is paid.":
        "どちらも損失の場合：小さいほうの金額を支払います。",
    "Form of payment": "支払い方法",
    "<b>USD cash</b>, to a payment method you nominate":
        "<b>米ドル現金</b>、ご指定の受取方法へ",
    "Timing": "着金",
    "Within <b>10 business days</b> of verification": "確認完了後 <b>10 営業日</b>以内",
    "Fees": "手数料",
    "Borne by Presight, excluding third-party charges arising from your chosen payment method":
        "Presight 負担。ただし受取方法に起因する第三者手数料は除きます",
    "Exclusions": "除外事由",
    "Any of the following voids eligibility for that enrolment:":
        "以下のいずれかに該当すると、その回の参加は補償対象外になります：",
    "Less than a full month of copying, or pausing or unsubscribing during the period.":
        "コピーが 1 か月に満たない、または期間中に停止・解除した場合。",
    "Entering positions manually, or manually altering positions created by copying (stops, "
    "targets, copy settings).":
        "手動で新規建てをした、またはコピーで生じた建玉を手で変更した（損切り、利確、コピー設定）場合。",
    "A withdrawal during the protection period.": "保護期間中に出金した場合。",
    "Multiple accounts enrolled under the same identity or the same payment method.":
        "同一人物または同一の受取方法で複数口座が重複参加している場合。",
    "Conduct prohibited by the partner platform (latency arbitrage, hedged scalping, slippage "
    "abuse and similar).":
        "提携プラットフォームが禁止する行為（レイテンシー・アービトラージ、両建てスキャルピング、"
        "スリッページの悪用など）。",
    "Providing false information, or declining to cooperate with verification.":
        "虚偽の情報を提供した、または確認に協力しない場合。",
    "Losses caused by partner-platform outages, quote errors or force majeure. These are handled "
    "case by case and fall outside the automatic payout.":
        "提携プラットフォームの障害、レート異常、不可抗力による損失。"
        "これらは個別協議とし、本制度の自動支払いの対象外です。",
    "Verification": "確認手続き",
    "Submit a claim through the community or by email within <b>5 calendar days</b> of the "
    "period ending.":
        "保護期間の終了後 <b>5 暦日</b>以内に、コミュニティまたはメールで申請してください。",
    "Provide a <b>complete account statement</b> from the platform (all fills plus all deposits "
    "and withdrawals), or authorise the platform to share read-only data with Presight.":
        "プラットフォームの<b>取引報告書一式</b>（全約定と全入出金）を提出するか、"
        "プラットフォームから Presight への読み取り専用データ提供を許可してください。",
    "If verification passes, we pay under section 06. If it does not, we set out the reason in "
    "writing.":
        "確認を通れば第 06 条に従って支払います。通らない場合は理由を書面でお伝えします。",
    "Other terms": "その他の定め",
    "This programme is <b>not investment advice</b> and does not guarantee the strategy will be "
    "profitable. It is a compensation arrangement for losses under specific conditions.":
        "本制度は<b>投資助言ではなく</b>、戦略が利益を上げることを保証するものでもありません。"
        "特定の条件下での損失を補填する取り決めにすぎません。",
    "Presight may amend or end the programme at any time. Doing so <b>does not affect "
    "participants already inside a protection period</b>, whose entitlement follows the terms in "
    "force when they enrolled.":
        "Presight は本制度をいつでも変更・終了できます。ただし<b>すでに保護期間に入っている参加者には"
        "影響しません</b>。その権利は参加時点で有効だった規約に従います。",
    "The programme is independent of any promotion run by the partner platform, which bears no "
    "responsibility for it.":
        "本制度は提携プラットフォームが行う各種キャンペーンとは独立しており、"
        "同プラットフォームは本制度について責任を負いません。",
    "The Chinese version of these terms governs. This English version is provided for reference.":
        "本規約は中国語版を正文とします。この日本語版は参考訳です。",
    '<span class="mono">⚠</span> Risk warning and conflict-of-interest disclosure':
        '<span class="mono">⚠</span> リスク警告と利益相反の開示',
    "CFDs, foreign exchange and leveraged products carry a high level of risk, can cost you your "
    "entire deposit, and are not suitable for every investor. Coverage under this programme is "
    "limited to base capital and <b>does not remove trading risk</b>.":
        "CFD、外国為替、レバレッジ商品は高いリスクを伴い、預託金の全額を失う可能性があり、"
        "すべての投資家に適した商品ではありません。本制度の補償は基準資金が上限であり、"
        "<b>取引リスクをなくすものではありません</b>。",
    "Presight has an introducing-broker / affiliate relationship with the partner trading "
    "platform. If you open an account through our link we may receive commission from the "
    "platform. This does not increase your trading costs, but you should be aware the "
    "relationship exists.":
        "Presight は提携取引プラットフォームと紹介（IB／アフィリエイト）関係にあります。"
        "当方のリンクから口座を開設された場合、プラットフォームから手数料を受け取ることがあります。"
        "これによりお客様の取引コストが増えることはありませんが、この関係があることはご承知おきください。",
    "Past performance does not indicate future results. You are responsible for determining "
    "whether trading of this kind is permitted in your jurisdiction, and for your own trading "
    "decisions.":
        "過去の成績は将来の結果を示しません。この種の取引がご自身の居住法域で認められているかの確認、"
        "および取引判断とその結果は、いずれもお客様の責任です。",
    "[Add here: the operating entity’s full legal name and place of registration, its licensing "
    "status or an explicit statement that it is unlicensed, the partner platform and its "
    "regulator, and any territorial restrictions.]":
        "【ここに追記：運営主体の正式名称と登記地、ライセンスの有無（無登録ならその旨を明記）、"
        "提携プラットフォーム名とその監督当局、および地域制限】",
    "&larr; Home": "&larr; ホームへ",
    "Ask in the community &rarr;": "コミュニティで質問する &rarr;",
    "<span>© 2026 PRESIGHT TRADING INSTITUTE</span>\n<span>Trading involves risk</span>":
        "<span>© 2026 PRESIGHT TRADING INSTITUTE</span>\n<span>取引にはリスクが伴います</span>",
}

# ---- build.py が報告した残りの断片（キーは英語版そのまま） ----
INDEX.update({
    '<a href="#protection">Loss coverage</a>\n<a href="#strategy">Strategy</a>\n'
    '<a href="#community">Community</a>\n<a href="#start">Get started</a>\n'
    '<a href="#faq">FAQ</a>':
        '<a href="#protection">損失補償</a>\n<a href="#strategy">戦略</a>\n'
        '<a href="#community">コミュニティ</a>\n<a href="#start">始め方</a>\n'
        '<a href="#faq">よくある質問</a>',

    '<b>Losses covered</b>\n<span class="cond">your loss, refunded<i>/</i>paid in cash</span>\n'
    '<a href="protection.html">Full terms →</a>':
        '<b>損失補償</b>\n<span class="cond">負けた分を返金<i>/</i>現金で着金</span>\n'
        '<a href="protection.html">規約全文 →</a>',

    '<a class="btn big" href="#protection">How coverage works <span class="arw">→</span></a>\n'
    '<a class="btn big ghost" data-link="channel" href="#" rel="noopener" target="_blank">'
    'Browse past signals</a>':
        '<a class="btn big" href="#protection">補償のしくみ <span class="arw">→</span></a>\n'
        '<a class="btn big ghost" data-link="channel" href="#" rel="noopener" target="_blank">'
        '過去のシグナルを見る</a>',

    'This is not investment advice and does not guarantee the strategy will be profitable. '
    'Presight receives introducing-broker commission from the partner platform. '
    '<a href="protection.html" style="color:var(--amber);font-weight:600">'
    'Full terms and exclusions →</a>':
        'これは投資助言ではなく、戦略が利益を上げることを保証するものでもありません。'
        'Presight は提携プラットフォームから紹介手数料を受け取ります。'
        '<a href="protection.html" style="color:var(--amber);font-weight:600">'
        '規約全文と除外事由 →</a>',

    '<a class="btn big" data-link="broker" href="#" rel="noopener" target="_blank">'
    'Open an account &amp; copy <span class="arw">→</span></a>\n'
    '<a class="btn big ghost" href="protection.html">Read the full terms</a>':
        '<a class="btn big" data-link="broker" href="#" rel="noopener" target="_blank">'
        '口座開設してコピーする <span class="arw">→</span></a>\n'
        '<a class="btn big ghost" href="protection.html">規約全文を読む</a>',

    '<span class="tag hero-tag">Loss coverage · <a href="protection.html">Full terms</a></span>\n'
    '<span class="tag">MULTI-ASSET</span>\n<span class="tag">AUTO-COPY</span>\n'
    '<span class="tag">FIXED RISK</span>':
        '<span class="tag hero-tag">損失補償 · <a href="protection.html">規約全文</a></span>\n'
        '<span class="tag">マルチアセット</span>\n<span class="tag">自動コピー</span>\n'
        '<span class="tag">リスク固定</span>',

    '<a class="btn big" data-link="channel" href="#" rel="noopener" target="_blank">'
    'Public signal channel <span class="arw">→</span></a>\n'
    '<a class="btn big ghost" data-link="community" href="#" rel="noopener" target="_blank">'
    'Trading Institute — open to all</a>':
        '<a class="btn big" data-link="channel" href="#" rel="noopener" target="_blank">'
        '公開シグナルチャンネル <span class="arw">→</span></a>\n'
        '<a class="btn big ghost" data-link="community" href="#" rel="noopener" target="_blank">'
        'Trading Institute — 誰でも参加可</a>',

    '<b>Base capital</b> is your account equity at the moment the protection period starts — '
    'when you report your MT5 account ID. If equity at the end of the protection period is '
    'below base capital, that shortfall is the net loss and is refunded in <b>USD cash</b> '
    'within 10 business days of verification. Coverage applies only to trades the strategy '
    'closed itself — <b>losses on positions you closed by hand are not refunded</b>. Nothing '
    'is owed if you finish flat or in profit. Coverage is limited to the full amount of base '
    'capital. <a href="protection.html">Full terms and exclusions →</a>':
        '<b>基準資金</b>とは、保護期間が始まった時点——つまり MT5 口座 ID を届け出た時点——の'
        '有効証拠金です。保護期間終了時の有効証拠金がこれを下回っていれば、その差額が純損失で、'
        '確認完了後 10 営業日以内に<b>米ドル現金</b>で返金します。補償の対象は戦略自身が決済した'
        'トレードだけで、<b>ご自身で手仕舞いした建玉の損失は返金されません</b>。'
        '同値または利益で終えた場合は支払いは発生しません。補償の上限は基準資金の全額です。'
        '<a href="protection.html">規約全文と除外事由 →</a>',

    'Five things: a <b>new account</b> opened through our link and KYC-verified; copy settings '
    'of <b>Autoscale / Value by asset / Ratio 1</b> (a 1:1 mirror, no scaling up); <b>report '
    'your MT5 account ID</b> to <span class="mono">@PresightAdminBot</span> once copying starts; '
    '<b>a full month of continuous copying</b> from that report; and <b>no manual intervention '
    'and no withdrawals</b> during that window.<br/><br/>Reporting is the gate: we cannot verify '
    'an account we were never told about, and losses incurred before you report are outside the '
    'coverage. Closing a position by hand is the one carve-out — it does not void the enrolment, '
    'but the loss on that trade is not refunded.<br/><br/>Per-trade risk and aggregate exposure '
    'are <b>not yours to set</b> — we manage them at the copy-account level. ALPHA-1 is a '
    'quantitative strategy and holding several positions at once is normal. The strategy account '
    'has drawdown thresholds that cut size or halt new entries on breach, and it never averages '
    'down.':
        '5 つです。当方のリンクから開設し KYC を済ませた<b>新規口座</b>であること。'
        'コピー設定が <b>Autoscale / Value by asset / Ratio 1</b>（1:1、拡大しない）であること。'
        'コピー開始後に <span class="mono">@PresightAdminBot</span> へ<b>MT5 口座 ID を届け出る</b>こと。'
        'その届出から<b>まる 1 か月</b>コピーを続けること。そして期間中は'
        '<b>手動介入も出金もしない</b>こと。<br/><br/>届出が入口です。'
        '知らされていない口座は確認のしようがなく、届出より前に生じた損失は補償の外です。'
        '手仕舞いだけは例外扱いで、参加そのものは無効になりませんが、そのトレードの損失は返金されません。'
        '<br/><br/>1 トレードあたりのリスクと合計エクスポージャーは<b>あなたが設定するものではなく</b>、'
        'こちらがコピー口座の側で管理します。ALPHA-1 はクオンツ戦略で、同時に複数のポジションを'
        '持つのは正常です。戦略口座にはドローダウンの閾値があり、触れるとロットを落とすか'
        '新規建てを止めます。ナンピンは行いません。',

    '<a class="btn big" data-link="ib" href="#" rel="noopener" target="_blank">'
    'Register and apply <span class="arw">→</span></a>\n'
    '<a class="btn big ghost" href="protection.html">Read the coverage terms</a>':
        '<a class="btn big" data-link="ib" href="#" rel="noopener" target="_blank">'
        '登録して IB を申請する <span class="arw">→</span></a>\n'
        '<a class="btn big ghost" href="protection.html">先に補償規約を読む</a>',

    'Revenue share and IB status are calculated and paid by the partner trading platform '
    '(DecodeFX); Presight never handles the funds. Coverage for your clients follows the '
    '<a href="protection.html" style="color:var(--amber);font-weight:600">'
    'published programme terms</a> — each client still has to report their own MT5 account ID '
    'and meet every other condition.':
        'レベニューシェアと IB 資格の算定・支払いは提携取引プラットフォーム（DecodeFX）が行い、'
        'Presight が資金を預かることはありません。紹介したお客様の補償は'
        '<a href="protection.html" style="color:var(--amber);font-weight:600">'
        '掲載中のプログラム規約</a>に従います。お客様ご本人が MT5 口座 ID を届け出て、'
        'その他の条件も満たす必要があります。',

    '<a class="btn ghost" data-link="community" rel="noopener" target="_blank">'
    'Questions? Join the community</a>\n'
    '<a class="mlink" href="protection.html">Full programme terms →</a>':
        '<a class="btn ghost" data-link="community" rel="noopener" target="_blank">'
        '質問があればコミュニティへ</a>\n'
        '<a class="mlink" href="protection.html">プログラム規約全文 →</a>',
})

PROTECTION.update({
    "← Home": "← ホームへ",
    '<a class="backlink" href="index.html">← Home</a>':
        '<a class="backlink" href="index.html">← ホームへ</a>',
    "Ask in the community →": "コミュニティで質問する →",

    '<span class="no">01</span>In one sentence': '<span class="no">01</span>ひとことで言うと',
    '<span class="no">02</span>Eligibility': '<span class="no">02</span>参加条件',
    '<span class="no">03</span>Risk control happens on our side':
        '<span class="no">03</span>リスク管理はこちらがコピー口座の側で行う',
    '<span class="no">04</span>Protection period': '<span class="no">04</span>保護期間',
    '<span class="no">05</span>Base capital': '<span class="no">05</span>基準資金',
    '<span class="no">06</span>How the payout is calculated':
        '<span class="no">06</span>補償額の計算',
    '<span class="no">07</span>Exclusions': '<span class="no">07</span>除外事由',
    '<span class="no">08</span>Verification': '<span class="no">08</span>確認手続き',
    '<span class="no">09</span>Other terms': '<span class="no">09</span>その他の定め',

    'Open an account with the partner platform through a Presight link, subscribe to PRESIGHT '
    'ALPHA-1 at a <b>1:1 copy ratio</b>, <b>report your MT5 account ID</b> to '
    '<span class="mono">@PresightAdminBot</span> on Telegram once copying has started, and keep '
    'copying for <b>a full month</b> without manual intervention or withdrawals. If the account '
    'is down when the period ends, we refund the loss in <b>cash</b>.':
        'Presight のリンクから提携プラットフォームで口座を開き、<b>1:1 のコピー比率</b>で '
        'PRESIGHT ALPHA-1 を購読します。コピーを始めたら Telegram で '
        '<span class="mono">@PresightAdminBot</span> に<b>MT5 口座 ID を届け出て</b>、'
        '手動介入も出金もせずに<b>まる 1 か月</b>コピーを続けてください。'
        '期間終了時に口座が負けていれば、その損失を<b>現金</b>で返金します。',

    'Two boundaries to note up front: coverage applies only to losses incurred <b>after you '
    'report the account</b>, and only to trades <b>the strategy itself closed</b> — losses on '
    'positions you closed by hand are not covered.':
        '先に押さえておくべき境界が二つあります。補償の対象は<b>口座を届け出た後</b>に生じた損失'
        'だけで、しかも<b>戦略自身が決済した</b>トレードだけです。'
        'ご自身で手仕舞いした建玉の損失は対象外です。',

    "A subscription to <b>PRESIGHT ALPHA-1</b> inside the platform's copy-trading system, "
    "configured as below.\n            The path: log in at "
    '<span class="mono">secure.decodefx.com</span> → <b>Copy Trading</b> →\n'
    '            sign in with your <b>MT5 copy account</b> login and password → '
    '<b>New subscription</b> →\n            set Provider to '
    '<span class="mono">presighttrading_com - signal 1</span>\n'
    "            (the platform's name for PRESIGHT ALPHA-1).":
        'プラットフォームのコピートレード機能で <b>PRESIGHT ALPHA-1</b> を購読し、'
        '下記のとおり設定すること。\n            手順：'
        '<span class="mono">secure.decodefx.com</span> にログイン → <b>Copy Trading</b> →\n'
        '            <b>MT5 コピー口座</b>の ID とパスワードでサインイン → '
        '<b>New subscription</b> →\n            Provider に '
        '<span class="mono">presighttrading_com - signal 1</span> を入力\n'
        '            （これが PRESIGHT ALPHA-1 のプラットフォーム上の名称です）。',

    'Copy settings: <b>Autoscale</b>, <b>Value by asset</b>, <b>Ratio = 1</b> — a 1:1 mirror.\n'
    "            The master account's position sizing must not be scaled up; a ratio above 1 "
    'voids eligibility outright.':
        'コピー設定は <b>Autoscale</b>、<b>Value by asset</b>、<b>Ratio = 1</b>、'
        'すなわち 1:1 のミラーであること。\n'
        '            マスター口座のロットを拡大してはいけません。Ratio が 1 を超えた時点で'
        '資格を失います。',

    'Once copying has started, <b>report your MT5 account ID (login number)</b> by direct message '
    'to <span class="mono">@PresightAdminBot</span> on Telegram — it replies with a receipt '
    'immediately.\n            We cannot verify an account that was never reported, so an '
    'unreported account <b>is not eligible</b>; for reported accounts,\n            coverage '
    'runs from the moment of reporting — losses incurred before that fall outside it.':
        'コピーを始めたら、Telegram で <span class="mono">@PresightAdminBot</span> に'
        '<b>MT5 口座 ID（ログイン番号）</b>をダイレクトメッセージで届け出ること。'
        'その場で受付の返信が届きます。\n            届出のない口座は確認のしようがないため'
        '<b>対象外</b>です。届け出た口座については、\n            補償は届出の瞬間から'
        '走ります。それより前に生じた損失は対象外です。',

    '<b>A full month of continuous copying</b>, without pausing or unsubscribing.':
        '<b>まる 1 か月、続けてコピーする</b>こと。途中で停止・解除しないこと。',

    'During the period: <b>no manual entries, no manual changes to stops or targets, no changes '
    'to copy settings</b>.\n            (Closing a position by hand does not void the whole '
    'enrolment, but the loss on that trade is not covered — see section 06.)':
        '期間中は<b>手動で新規建てをしない、損切り・利確を手で動かさない、コピー設定を変えない</b>'
        'こと。\n            （手仕舞いだけは参加そのものを無効にしませんが、'
        'そのトレードの損失は補償されません。第 06 条参照。）',

    'During the period: <b>no withdrawals</b>.': '期間中は<b>出金しない</b>こと。',

    'When you <b>report your MT5 account ID</b> in the community; if you report before your first '
    'copied fill, it starts at that first fill instead (whichever comes later)':
        '<b>MT5 口座 ID を届け出た</b>時点。初回のコピー約定より前に届け出た場合は、'
        'その初回約定の時点（いずれか遅いほう）',

    '<b>One month — 30 consecutive calendar days</b>': '<b>1 か月 — 連続 30 暦日</b>',

    'Losses incurred before you report the account are <b>not covered</b> and do not enter the '
    'base-capital comparison':
        '届出より前に生じた損失は<b>補償の対象外</b>で、基準資金の比較にも入りません',

    'If positions are still open on day 30, the period extends until they are all closed, for at '
    'most 3 further trading days':
        '30 日目に未決済の建玉が残っている場合、すべて決済されるまで期間を延長します。'
        '延長は最長 3 営業日',

    'Account equity at the moment the protection period starts — that is, when you report your '
    'MT5 account ID (or at your first copied fill, if you reported before it)':
        '保護期間が始まった時点の有効証拠金。つまり MT5 口座 ID を届け出た時点'
        '（届出のほうが先なら、初回のコピー約定の時点）',

    '<b>Net loss = base capital − account equity at the end of the protection period</b>':
        '<b>純損失 = 基準資金 − 保護期間終了時の有効証拠金</b>',

    'Coverage applies only to trades <b>the strategy closed itself</b>. Positions you closed by '
    'hand are excluded either way —\n         you chose the exit, so that result is yours. '
    'Therefore:':
        '補償の対象は<b>戦略自身が決済した</b>トレードだけです。ご自身で手仕舞いした建玉は'
        '損益にかかわらず除外します。\n         降りる時機を選んだのはあなたであり、'
        'その結果もあなたのものだからです。したがって：',

    '<b>Payout = the combined loss on trades closed by the strategy during the protection period, '
    'capped at the net loss above.</b>':
        '<b>補償額 = 保護期間中に戦略が決済したトレードの損失合計。'
        '上限は前項の純損失。</b>',

    'Net loss ≤ 0 (account flat or in profit): nothing is payable.':
        '純損失 ≤ 0（口座が同値または利益）：支払いは発生しません。',

    'Example 1: base capital USD 10,000; equity at the end of the period USD 9,150; every '
    'position was closed by the strategy;\n         net loss USD 850; payout <b>USD 850</b>.':
        '例 1：基準資金 10,000 米ドル、期間終了時 9,150 米ドル、建玉はすべて戦略が決済。'
        '\n         純損失 850 米ドル、補償は<b>850 米ドル</b>。',

    'Example 2: the same USD 850 loss, but USD 300 of it came from a position you closed by hand; '
    'the strategy-closed trades\n         lost USD 550; payout <b>USD 550</b>.':
        '例 2：同じく 850 米ドルの負けだが、うち 300 米ドルはご自身で手仕舞いした建玉のもの。'
        '戦略が決済した分の損失は\n         550 米ドルなので、補償は<b>550 米ドル</b>。',

    '<b>Failing to report your MT5 account ID</b> to '
    '<span class="mono">@PresightAdminBot</span>, or reporting an ID that does not match the '
    'account you claim on.':
        '<span class="mono">@PresightAdminBot</span> に<b>MT5 口座 ID を届け出ていない</b>、'
        'または届け出た ID が請求する口座と一致しない場合。',

    "A <b>Ratio above 1</b> — that is, scaling up the master account's sizing.":
        '<b>Ratio が 1 を超えている</b>、つまりマスター口座のロットを拡大している場合。',

    'Losses not attributable to PRESIGHT ALPHA-1 — for example trading instruments the strategy '
    'does not cover.':
        'PRESIGHT ALPHA-1 に起因しない損失。たとえば戦略が扱わない銘柄をご自身で売買した場合。',

    '<b>Closing by hand is the one exception</b>: it does not void the enrolment, but the loss on '
    'any position you closed yourself is never covered, and the rest of the account is still '
    'assessed under section 06.':
        '<b>手仕舞いだけは例外です</b>。参加そのものは無効になりませんが、'
        'ご自身で決済した建玉の損失は一切補償されず、口座の残りの部分は第 06 条どおりに判定します。',

    'We verify when the account was reported, the historical copy settings, the fills and the '
    'deposit/withdrawal record, and identify trade by trade which positions the strategy closed '
    'and which you closed yourself.':
        '届出の時刻、コピー設定の履歴、約定明細、入出金記録を確認し、'
        'どの建玉を戦略が決済し、どれをご自身が決済したかを 1 件ずつ切り分けます。',

    "[Add here: the operating entity's full legal name and place of registration, its licensing "
    "status or an explicit statement that it is unlicensed, the partner platform and its "
    "regulator, and any territorial restrictions.]":
        '【ここに追記：運営主体の正式名称と登記地、ライセンスの有無（無登録ならその旨を明記）、'
        '提携プラットフォーム名とその監督当局、および地域制限】',
})

PROTECTION.update({
    '<a class="backlink" href="index.html">← Home</a>\n         \xa0\xa0 '
    '<a class="backlink" data-link="community" href="#">Ask in the community →</a>':
        '<a class="backlink" href="index.html">← ホームへ</a>\n         \xa0\xa0 '
        '<a class="backlink" data-link="community" href="#">コミュニティで質問する →</a>',
})

# 信号频道合并之后英文页改了两处，旧键随之失效（build.py --check 会报出来）
INDEX.update({
    '<a class="btn big" data-link="channel" href="#" rel="noopener" target="_blank">'
    'Open the signal channel <span class="arw">→</span></a>\n'
    '<a class="btn big ghost" data-link="community" href="#" rel="noopener" target="_blank">'
    'Trading Institute — open to all</a>':
        '<a class="btn big" data-link="channel" href="#" rel="noopener" target="_blank">'
        'シグナルチャンネルを開く <span class="arw">→</span></a>\n'
        '<a class="btn big ghost" data-link="community" href="#" rel="noopener" target="_blank">'
        'Trading Institute — 誰でも参加可</a>',

    '<b>Scan to open the signal channel</b>\n            This is the main public entry point — '
    'live signals, no application needed.\n            Community discussion lives at '
    '<b>@presight_institute</b>, also open.\n            <span class="h">Or search '
    '@presight_signals in Telegram</span>':
        '<b>読み取るとシグナルチャンネルが開きます</b>\n            これが対外的な入口です。'
        'リアルタイムのシグナルを公開しており、申請は要りません。\n            議論の場は'
        '<b>@presight_institute</b>、こちらも公開です。\n            <span class="h">'
        'Telegram で @presight_signals を検索してもかまいません</span>',
})

# 合作伙伴板块新增：入金门槛提高 + 首月保收益 1%
INDEX.update({
    '<span class="u">3</span> clients · <span class="u">USD 5,000</span> each':
        '<span class="u">3</span> 名 · 各 <span class="u">5,000 米ドル</span>',
    'At least 3 clients under you, each funding the account with no less than USD 5,000 — the threshold for both loss coverage and the return floor.':
        'あなたの下に 3 名以上のお客様がいて、それぞれが 5,000 米ドル以上を入金していること——損失補償と初月リターン保証はどちらもこの条件で有効になります。',
    'NEW · CLIENTS OF PARTNERS ONLY':
        '新設 · パートナー名下のお客様限定',
    'First-month return floor':
        '初月リターン保証 1%',
    'On top of loss coverage, your clients get one more layer: <b>if the first month of copying returns less than 1%, we pay back 1% of the copied amount in cash.</b>':
        '損失補償に加えて、あなたのお客様にはもう一段の保証が付きます。<b>コピー開始から 1 か月のリターンが 1% に届かなかった場合、コピー金額の 1% を現金でお返しします。</b>',
    'Copied amount = the sum of the daily copy balance over the first 30 days ÷ 30 (i.e. the daily average)':
        'コピー金額 = 初月 30 日間の日次コピー残高の合計 ÷ 30（つまり日次平均）',
})

INDEX.update({
    'Bring people to Presight and keep half the commission. The clients you introduce get the loss-coverage programme and a <b>1% floor on their first month</b>.':
        'Presight を紹介して、手数料の半分を受け取ってください。紹介したお客様は損失補償に加えて、<b>初月リターン 1% の下支え</b>も受けられます。',
})

# 门槛口径更正：5,000 美元是名下用户的入金合计，不是每人
INDEX.update({
    '<span class="u">3</span> clients · <span class="u">USD 5,000</span> combined':
        '<span class="u">3</span> 名 · 入金合計 <span class="u">5,000 米ドル</span>',
    'At least 3 clients under you, funding <b>USD 5,000 between them</b> — the threshold for both loss coverage and the return floor.':
        'あなたの下に 3 名以上のお客様がいて、<b>入金の合計が 5,000 米ドル以上</b>であること——損失補償と初月リターン保証はどちらもこの条件で有効になります。',
})

# 顶栏加了「邀请合作」快捷入口
INDEX.update({
    '<a href="#protection">Loss coverage</a>\n<a href="#strategy">Strategy</a>\n<a href="#community">Community</a>\n<a href="#start">Get started</a>\n<a href="#faq">FAQ</a>\n<a class="hot" href="#partner">Partners</a>':
        '<a href="#protection">損失補償</a>\n<a href="#strategy">戦略</a>\n<a href="#community">コミュニティ</a>\n<a href="#start">始め方</a>\n<a href="#faq">よくある質問</a>\n<a class="hot" href="#partner">パートナー募集</a>',
})

# IB 洽谈联系方式
INDEX.update({
    'To discuss an IB partnership, message <a href="https://t.me/presighttrading" rel="noopener" target="_blank">@presighttrading</a> on Telegram':
        'IB 提携のご相談は Telegram の <a href="https://t.me/presighttrading" rel="noopener" target="_blank">@presighttrading</a> までご連絡ください',
})

# 策略细节 / 定制策略的洽谈入口
INDEX.update({
    'Want the details behind the strategy, or a <b>bespoke strategy</b> for your own client base? Message <a href="https://t.me/presighttrading" rel="noopener" target="_blank">@presighttrading</a> on Telegram as well':
        '戦略の詳細を知りたい方、あるいはご自身の顧客向けに<b>専用戦略</b>をご希望の方も、Telegram の <a href="https://t.me/presighttrading" rel="noopener" target="_blank">@presighttrading</a> までご連絡ください',
})
