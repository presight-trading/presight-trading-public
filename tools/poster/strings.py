"""分享长图的五语文案。键与 poster.tpl.html 里的 {{占位符}} 一一对应。

固有名词一律不翻：PRESIGHT ALPHA-1 / DecodeFX / @PresightAdminBot /
secure.decodefx.com / Copy Trading / New subscription / Autoscale /
Value by asset / Ratio / Activate / follower。这些是用户要在平台上逐字
输入或点击的字符串，翻了就照着做不出来。

四格标签（COPY RATIO / DURATION / COVERAGE / PAYOUT）也保持英文：它们是
版面上的等宽小标，各语种混排反而乱，且都是通用金融词。
"""

# 各语种落地页与二维码目标。二维码指向 #start-copy，扫码直接弹出
# 「三步开始跟单」——扫码的人手里没有页面上下文，落在首页顶部还得自己找
# 入口，一步都不该多。
SITES = {
    "zh": ("", "https://presighttrading.com/#start-copy"),
    "en": ("en", "https://presighttrading.com/en/#start-copy"),
    "ja": ("ja", "https://presighttrading.com/ja/#start-copy"),
    "vi": ("vi", "https://presighttrading.com/vi/#start-copy"),
    "th": ("th", "https://presighttrading.com/th/#start-copy"),
}

HTML_LANG = {"zh": "zh-CN", "en": "en", "ja": "ja", "vi": "vi", "th": "th"}

L = {}

L["zh"] = dict(
    title="跟单亏损包赔 · 分享长图",
    brand_sub="Presight Trading Institute · 先见交易学院",
    badge="跟单亏损包赔",
    h1a="按规则跟单", h1b="亏了我们赔",
    lead="以 <b>1:1</b> 跟单 PRESIGHT ALPHA-1，报备 MT5 账户 ID 后连续跟单<b>满 1 个月</b>，"
         "期间不手动干预、不出金。期末账户若为净亏损，我们<b>按实际亏损金额现金返还</b>。",
    s1="不放大仓位", s2v="1 个月", s2="自报备起 30 天",
    s3v="基准资金", s3="全额保护", s4v="现金", s4="10 个工作日",
    sec1="四步开始", sec2="怎么赔",
    a1t='通过官网链接注册<span class="em">新账户</span>并入金',
    a1d="完成身份认证（KYC）。只有走官网链接注册的新账户才在订阅名单里",
    a2t='订阅 <span class="em">PRESIGHT ALPHA-1</span>',
    a2d="secure.decodefx.com → Copy Trading → 先注册 follower 账户 → New subscription → "
        "参数 <b>Autoscale / Value by asset / Ratio = 1</b> → 在 Action 栏点 <b>Activate</b>。"
        "不点 Activate 跟单不生效",
    a3t='私信 <span class="em">@PresightAdminBot</span> 报备 MT5 账户 ID',
    a3d="<b>保护期从这一刻起算</b>，没报备的账户不具备赔付资格，报备之前的亏损也不赔",
    a4t='放着不动，满 <span class="em">1 个月</span>',
    a4d="期间不手动开仓、不改止损止盈、不调参数、不出金、不暂停或解除跟单",
    b1t="净亏损 = 基准资金 − 期末净值",
    b1d="基准资金取报备时的账户净值，保护额度为其全额",
    b2t='<span class="em">只赔由策略自动平仓的交易</span>',
    b2d="你手动平仓的持仓无论盈亏都不计入——离场时机是你自己决定的。"
        "举例：期末净亏 850 美元，若全部由策略平仓则赔 850；其中 300 来自你手动平掉的一笔，则赔 550",
    b3t='美元现金返还，<span class="em">10 个工作日</span>内到账',
    b3d="保护期结束后 5 个自然日内提交申请，附完整交易报表；核验通过后打款，手续费我们承担",
    hltag="推广合作伙伴专享", hlh="名下用户首月保收益",
    hlp="推广合作伙伴（IB）名下的用户，除了跟单亏损包赔，还多一层："
        "<b>跟单满第一个月时若收益不足 1%，按跟单金额的 1% 返现。</b>"
        "佣金另有 <b>50% 分成</b>，门槛为名下至少 3 名用户、入金合计 ≥ 5,000 美元。",
    hlf="跟单金额 = 首月 30 天每日跟单余额之和 ÷ 30（日均余额）",
    qralt="扫码开始跟单", qrh="扫码直接开始 / SCAN TO START", qrbig="扫一扫，三步开始跟单",
    k_site="官网", k_ch="信号频道", k_inst="交易学院", k_bot="报备账号",
    riskh="风险提示与利益披露",
    risk1="差价合约、外汇及杠杆产品具有高风险，可能导致您损失全部本金，并不适合所有投资者。"
          "本计划赔付以基准资金为限，<b>并不消除交易风险</b>。历史业绩不代表未来表现。",
    risk2="Presight 与合作交易平台存在推荐（IB/联盟）返佣关系。您通过我们的链接开户后，"
          "我们可能从平台获得佣金——这不增加您的交易成本，但请知悉此利益关系。",
    risk3="本图为摘要，<b>条款以官网发布的完整细则为准</b>：presighttrading.com/protection.html",
    foot="交易有风险 · 入市需谨慎<br>细则以官网版本为准",
)

L["en"] = dict(
    title="Loss coverage on copied trades · shareable one-pager",
    brand_sub="Presight Trading Institute",
    badge="LOSS COVERAGE",
    h1a="Copy within the rules.", h1b="We cover the loss.",
    lead="Copy PRESIGHT ALPHA-1 at <b>1:1</b>, report your MT5 account ID, then keep copying "
         "<b>for a full month</b> with no manual intervention and no withdrawals. If the account "
         "ends down, we <b>refund that loss in cash</b>.",
    s1="no scaling up", s2v="1 month", s2="30 days from your report",
    s3v="Base capital", s3="covered in full", s4v="Cash", s4="10 business days",
    sec1="Four steps to start", sec2="How the payout works",
    a1t='Open a <span class="em">new account</span> through our link and fund it',
    a1d="Complete KYC. Only accounts opened through the site link are on the subscription list",
    a2t='Subscribe to <span class="em">PRESIGHT ALPHA-1</span>',
    a2d="secure.decodefx.com → Copy Trading → register a follower account first → "
        "New subscription → settings <b>Autoscale / Value by asset / Ratio = 1</b> → "
        "press <b>Activate</b> in the Action column. Nothing is copied until you do",
    a3t='Report your MT5 account ID to <span class="em">@PresightAdminBot</span>',
    a3d="<b>The protection period starts at that moment.</b> An unreported account is not "
        "eligible, and losses before you report are not covered",
    a4t='Leave it alone for <span class="em">one month</span>',
    a4d="No manual entries, no changes to stops or targets or copy settings, no withdrawals, "
        "no pausing or unsubscribing",
    b1t="Net loss = base capital − equity at the end",
    b1d="Base capital is your equity at the moment you report; coverage is its full amount",
    b2t='<span class="em">Only trades the strategy closed itself are covered</span>',
    b2d="Positions you closed by hand are excluded either way — you chose the exit. Example: "
        "USD 850 net loss, all closed by the strategy → USD 850 paid; if USD 300 of it came from "
        "a position you closed yourself → USD 550 paid",
    b3t='Refunded in USD cash within <span class="em">10 business days</span>',
    b3d="Submit within 5 calendar days of the period ending with a full account statement; "
        "we pay after verification and cover the fees",
    hltag="PARTNER CLIENTS ONLY", hlh="1% floor on your clients' first month",
    hlp="Clients introduced by a partner (IB) get one more layer on top of loss coverage: "
        "<b>if the first month of copying returns less than 1%, we pay back 1% of the copied "
        "amount.</b> Commission is a <b>50% revenue share</b>; the threshold is at least "
        "3 clients funding USD 5,000 between them.",
    hlf="Copied amount = sum of the daily copy balance over the first 30 days ÷ 30 (daily average)",
    qralt="Scan to start copying", qrh="SCAN TO START",
    qrbig="Scan for the three steps to start",
    k_site="Website", k_ch="Signals", k_inst="Community", k_bot="Report to",
    riskh="Risk warning and conflict-of-interest disclosure",
    risk1="CFDs, foreign exchange and leveraged products carry a high level of risk, can cost you "
          "your entire deposit, and are not suitable for every investor. Coverage is limited to "
          "base capital and <b>does not remove trading risk</b>. Past performance does not "
          "indicate future results.",
    risk2="Presight has an introducing-broker / affiliate relationship with the partner platform. "
          "If you open an account through our link we may receive commission — this does not "
          "increase your trading costs, but you should know the relationship exists.",
    risk3="This image is a summary. <b>The published terms govern</b>: "
          "presighttrading.com/en/protection.html",
    foot="Trading involves risk<br>The published terms govern",
)

L["ja"] = dict(
    title="コピートレード損失補償 · 共有用ロング画像",
    brand_sub="Presight Trading Institute",
    badge="損失補償",
    h1a="ルールどおりに、", h1b="負けたら補償します",
    lead="PRESIGHT ALPHA-1 を <b>1:1</b> でコピーし、MT5 口座 ID を届け出たうえで"
         "<b>1 か月</b>、手動介入も出金もせずに続けます。期間終了時に口座が負けていれば、"
         "その損失を<b>現金で返金</b>します。",
    s1="拡大しない", s2v="1 か月", s2="届出から 30 日",
    s3v="基準資金", s3="全額を保護", s4v="現金", s4="10 営業日",
    sec1="4 ステップで開始", sec2="補償のしくみ",
    a1t='公式リンクから<span class="em">新規口座</span>を開き入金',
    a1d="本人確認（KYC）を完了。公式リンクから開いた新規口座だけが購読リストに載ります",
    a2t='<span class="em">PRESIGHT ALPHA-1</span> を購読',
    a2d="secure.decodefx.com → Copy Trading → まずフォロワー口座を登録 → New subscription → "
        "設定は <b>Autoscale / Value by asset / Ratio = 1</b> → Action 列の <b>Activate</b> を押す。"
        "押すまでコピーは始まりません",
    a3t='<span class="em">@PresightAdminBot</span> に MT5 口座 ID を届け出る',
    a3d="<b>保護期間はこの瞬間から始まります。</b>届出のない口座は対象外で、"
        "届出より前の損失も補償されません",
    a4t='<span class="em">1 か月</span>、そのままにしておく',
    a4d="手動での新規建て、損切り・利確やコピー設定の変更、出金、停止・解除はいずれも不可",
    b1t="純損失 = 基準資金 − 期間終了時の有効証拠金",
    b1d="基準資金は届出時点の有効証拠金。保護額はその全額です",
    b2t='<span class="em">補償は戦略自身が決済した取引だけ</span>',
    b2d="ご自身で手仕舞いした建玉は損益にかかわらず対象外です——降りる時機を選んだのはあなたです。"
        "例：期末の純損失 850 ドルが全て戦略の決済なら 850 ドル返金、"
        "うち 300 ドルが手仕舞い分なら 550 ドル返金",
    b3t='<span class="em">10 営業日</span>以内に米ドル現金で返金',
    b3d="期間終了後 5 暦日以内に取引報告書を添えて申請。確認後に送金し、手数料は当方負担",
    hltag="パートナー顧客限定", hlh="紹介先の初月リターン 1% 保証",
    hlp="紹介パートナー（IB）名義のお客様は、損失補償に加えてもう一段："
        "<b>コピー開始から 1 か月のリターンが 1% に届かなければ、コピー金額の 1% を返金します。</b>"
        "報酬は別途 <b>50% のレベニューシェア</b>。条件は名下に 3 名以上、"
        "入金合計 5,000 米ドル以上です。",
    hlf="コピー金額 = 初月 30 日間の日次コピー残高の合計 ÷ 30（日次平均）",
    qralt="読み取ってコピーを開始", qrh="読み取ってすぐ開始 / SCAN TO START",
    qrbig="読み取れば 3 ステップで開始",
    k_site="公式サイト", k_ch="シグナル", k_inst="コミュニティ", k_bot="届出先",
    riskh="リスク警告と利益相反の開示",
    risk1="CFD・外国為替・レバレッジ商品は高いリスクを伴い、預託金の全額を失う可能性があり、"
          "すべての投資家に適した商品ではありません。補償は基準資金が上限であり、"
          "<b>取引リスクをなくすものではありません</b>。過去の成績は将来の結果を示しません。",
    risk2="Presight は提携取引プラットフォームと紹介（IB／アフィリエイト）関係にあります。"
          "当方のリンクから口座を開設された場合、手数料を受け取ることがあります——"
          "お客様の取引コストは増えませんが、この関係があることはご承知おきください。",
    risk3="本画像は要約です。<b>条項は公式サイトの完全版が優先されます</b>："
          "presighttrading.com/ja/protection.html",
    foot="取引にはリスクが伴います<br>条項は公式サイト版が優先",
)

L["vi"] = dict(
    title="Bảo hiểm thua lỗ sao chép · ảnh chia sẻ",
    brand_sub="Presight Trading Institute",
    badge="BẢO HIỂM THUA LỖ",
    h1a="Sao chép đúng luật,", h1b="lỗ chúng tôi bù.",
    lead="Sao chép PRESIGHT ALPHA-1 ở tỷ lệ <b>1:1</b>, khai báo MT5 account ID rồi duy trì "
         "<b>đủ một tháng</b>, không can thiệp thủ công và không rút tiền. Nếu cuối kỳ tài khoản "
         "âm, chúng tôi <b>hoàn khoản lỗ đó bằng tiền mặt</b>.",
    s1="không phóng đại", s2v="1 tháng", s2="30 ngày kể từ khi khai báo",
    s3v="Vốn gốc", s3="bảo vệ toàn phần", s4v="Tiền mặt", s4="10 ngày làm việc",
    sec1="Bốn bước để bắt đầu", sec2="Bồi thường thế nào",
    a1t='Mở <span class="em">tài khoản mới</span> qua liên kết của chúng tôi và nạp tiền',
    a1d="Hoàn tất KYC. Chỉ tài khoản mở qua liên kết trên trang mới nằm trong danh sách đăng ký",
    a2t='Đăng ký <span class="em">PRESIGHT ALPHA-1</span>',
    a2d="secure.decodefx.com → Copy Trading → đăng ký tài khoản follower trước → New subscription → "
        "cấu hình <b>Autoscale / Value by asset / Ratio = 1</b> → bấm <b>Activate</b> ở cột Action. "
        "Chưa bấm thì chưa sao chép gì cả",
    a3t='Khai báo MT5 account ID cho <span class="em">@PresightAdminBot</span>',
    a3d="<b>Thời gian bảo vệ bắt đầu từ khoảnh khắc đó.</b> Tài khoản chưa khai báo thì không đủ "
        "điều kiện, và khoản lỗ trước lúc khai báo cũng không được bảo hiểm",
    a4t='Để yên <span class="em">đủ một tháng</span>',
    a4d="Không tự mở lệnh, không sửa dừng lỗ/chốt lời hay cấu hình sao chép, không rút tiền, "
        "không tạm dừng hay huỷ đăng ký",
    b1t="Lỗ ròng = vốn gốc − vốn chủ sở hữu cuối kỳ",
    b1d="Vốn gốc là vốn chủ sở hữu tại thời điểm bạn khai báo; bảo hiểm bằng toàn bộ số đó",
    b2t='<span class="em">Chỉ bồi thường các lệnh do chính chiến lược đóng</span>',
    b2d="Vị thế bạn tự tay đóng đều bị loại ra, lãi hay lỗ cũng vậy — bạn chọn thời điểm thoát. "
        "Ví dụ: lỗ ròng 850 USD, nếu đều do chiến lược đóng thì trả 850; nếu 300 USD trong đó là "
        "lệnh bạn tự đóng thì trả 550",
    b3t='Hoàn bằng tiền mặt USD trong <span class="em">10 ngày làm việc</span>',
    b3d="Nộp trong 5 ngày lịch kể từ khi kỳ hạn kết thúc, kèm sao kê tài khoản đầy đủ; "
        "chúng tôi trả sau khi xác minh và chịu phí",
    hltag="CHỈ DÀNH CHO KHÁCH CỦA ĐỐI TÁC", hlh="Bảo đảm 1% cho tháng đầu của khách",
    hlp="Khách do đối tác (IB) giới thiệu còn có thêm một lớp ngoài bảo hiểm thua lỗ: "
        "<b>nếu tháng đầu sao chép mà lợi nhuận không đạt 1%, chúng tôi hoàn 1% số tiền sao chép.</b> "
        "Hoa hồng là <b>50% chia sẻ doanh thu</b>; ngưỡng là ít nhất 3 khách với tổng nạp "
        "từ 5.000 USD.",
    hlf="Số tiền sao chép = tổng số dư sao chép mỗi ngày trong 30 ngày đầu ÷ 30 (trung bình ngày)",
    qralt="Quét để bắt đầu sao chép", qrh="QUÉT ĐỂ BẮT ĐẦU / SCAN TO START",
    qrbig="Quét mã, ba bước là xong",
    k_site="Website", k_ch="Kênh tín hiệu", k_inst="Cộng đồng", k_bot="Khai báo tới",
    riskh="Cảnh báo rủi ro và công bố xung đột lợi ích",
    risk1="CFD, ngoại hối và các sản phẩm đòn bẩy có mức rủi ro cao, có thể khiến bạn mất toàn bộ "
          "tiền ký quỹ và không phù hợp với mọi nhà đầu tư. Bảo hiểm tối đa bằng vốn gốc và "
          "<b>không xoá bỏ rủi ro giao dịch</b>. Hiệu quả quá khứ không phản ánh kết quả tương lai.",
    risk2="Presight có quan hệ đối tác giới thiệu (IB/affiliate) với nền tảng đối tác. Nếu bạn mở "
          "tài khoản qua liên kết của chúng tôi, chúng tôi có thể nhận hoa hồng — điều này không "
          "làm tăng chi phí giao dịch của bạn, nhưng bạn nên biết quan hệ đó tồn tại.",
    risk3="Ảnh này là bản tóm tắt. <b>Điều khoản công bố trên trang web mới là bản có hiệu lực</b>: "
          "presighttrading.com/vi/protection.html",
    foot="Giao dịch luôn có rủi ro<br>Điều khoản trên trang web là bản có hiệu lực",
)

L["th"] = dict(
    title="ประกันขาดทุนจากการก๊อปปี้เทรด · ภาพสำหรับแชร์",
    brand_sub="Presight Trading Institute",
    badge="ประกันขาดทุน",
    h1a="ก๊อปปี้ตามกติกา", h1b="ขาดทุนเราชดเชย",
    lead="ก๊อปปี้ PRESIGHT ALPHA-1 ที่อัตรา <b>1:1</b> แจ้ง MT5 account ID แล้วก๊อปปี้ต่อเนื่อง"
         "<b>ครบหนึ่งเดือน</b> โดยไม่แทรกแซงด้วยมือและไม่ถอนเงิน ถ้าจบรอบแล้วบัญชีติดลบ "
         "เรา<b>คืนส่วนที่ขาดทุนเป็นเงินสด</b>",
    s1="ไม่ขยายสถานะ", s2v="1 เดือน", s2="30 วันนับจากที่แจ้ง",
    s3v="เงินทุนตั้งต้น", s3="คุ้มครองเต็มจำนวน", s4v="เงินสด", s4="10 วันทำการ",
    sec1="สี่ขั้นตอนเริ่มต้น", sec2="ชดเชยอย่างไร",
    a1t='เปิด<span class="em">บัญชีใหม่</span>ผ่านลิงก์ของเราและฝากเงิน',
    a1d="ยืนยันตัวตน (KYC) ให้เสร็จ เฉพาะบัญชีใหม่ที่เปิดผ่านลิงก์บนเว็บเท่านั้นที่อยู่ในรายชื่อผู้สมัคร",
    a2t='สมัคร <span class="em">PRESIGHT ALPHA-1</span>',
    a2d="secure.decodefx.com → Copy Trading → สมัครบัญชี follower ก่อน → New subscription → "
        "ตั้งค่า <b>Autoscale / Value by asset / Ratio = 1</b> → กด <b>Activate</b> ในคอลัมน์ Action "
        "ไม่กดก็ยังไม่เริ่มก๊อปปี้",
    a3t='แจ้ง MT5 account ID กับ <span class="em">@PresightAdminBot</span>',
    a3d="<b>ระยะคุ้มครองเริ่มนับจากวินาทีนั้น</b> บัญชีที่ไม่ได้แจ้งจะไม่เข้าเกณฑ์ "
        "และขาดทุนก่อนแจ้งก็ไม่ได้รับความคุ้มครอง",
    a4t='ปล่อยไว้ให้ครบ <span class="em">หนึ่งเดือน</span>',
    a4d="ห้ามเปิดออเดอร์เอง ห้ามแก้จุดตัดขาดทุน/เป้าหมายหรือการตั้งค่าก๊อปปี้ ห้ามถอนเงิน "
        "ห้ามหยุดชั่วคราวหรือยกเลิก",
    b1t="ขาดทุนสุทธิ = เงินทุนตั้งต้น − อิควิตี้ตอนจบรอบ",
    b1d="เงินทุนตั้งต้นคืออิควิตี้ ณ ตอนที่คุณแจ้งบัญชี คุ้มครองเต็มจำนวนนั้น",
    b2t='<span class="em">ชดเชยเฉพาะออเดอร์ที่กลยุทธ์ปิดเอง</span>',
    b2d="สถานะที่คุณปิดเองไม่นับ ไม่ว่าจะกำไรหรือขาดทุน — คุณเป็นคนเลือกจังหวะออก "
        "ตัวอย่าง: ขาดทุนสุทธิ 850 ดอลลาร์ ถ้ากลยุทธ์ปิดทั้งหมดก็จ่าย 850 "
        "ถ้า 300 ดอลลาร์มาจากสถานะที่คุณปิดเองก็จ่าย 550",
    b3t='คืนเป็นเงินสดดอลลาร์ภายใน <span class="em">10 วันทำการ</span>',
    b3d="ยื่นภายใน 5 วันปฏิทินหลังจบรอบ พร้อมรายงานบัญชีฉบับสมบูรณ์ "
        "เราจ่ายหลังตรวจสอบและรับผิดชอบค่าธรรมเนียม",
    hltag="เฉพาะลูกค้าของพันธมิตร", hlh="รับประกัน 1% เดือนแรกของลูกค้าคุณ",
    hlp="ลูกค้าที่พันธมิตร (IB) แนะนำมาจะได้อีกชั้นหนึ่งนอกเหนือจากประกันขาดทุน: "
        "<b>ถ้าเดือนแรกของการก๊อปปี้ได้ผลตอบแทนไม่ถึง 1% เราคืน 1% ของยอดเงินที่ใช้ก๊อปปี้</b> "
        "ค่าคอมมิชชันแบ่ง <b>50%</b> เกณฑ์คือมีลูกค้าอย่างน้อย 3 ราย ยอดฝากรวม 5,000 ดอลลาร์ขึ้นไป",
    hlf="ยอดเงินที่ใช้ก๊อปปี้ = ผลรวมยอดคงเหลือรายวันใน 30 วันแรก ÷ 30 (ค่าเฉลี่ยต่อวัน)",
    qralt="สแกนเพื่อเริ่มก๊อปปี้", qrh="สแกนเริ่มได้เลย / SCAN TO START",
    qrbig="สแกน แล้วเริ่มใน 3 ขั้นตอน",
    k_site="เว็บไซต์", k_ch="แชนเนลสัญญาณ", k_inst="คอมมูนิตี้", k_bot="แจ้งบัญชีที่",
    riskh="คำเตือนความเสี่ยงและการเปิดเผยผลประโยชน์ทับซ้อน",
    risk1="CFD ฟอเร็กซ์ และผลิตภัณฑ์เลเวอเรจมีความเสี่ยงสูง อาจทำให้คุณเสียเงินฝากทั้งหมด "
          "และไม่เหมาะกับนักลงทุนทุกคน ความคุ้มครองจำกัดที่เงินทุนตั้งต้นและ"
          "<b>ไม่ได้ลบความเสี่ยงในการเทรด</b> ผลงานในอดีตไม่ได้บอกผลในอนาคต",
    risk2="Presight มีความสัมพันธ์แบบผู้แนะนำ (IB/affiliate) กับแพลตฟอร์มพันธมิตร "
          "หากคุณเปิดบัญชีผ่านลิงก์ของเรา เราอาจได้รับค่าคอมมิชชัน — "
          "สิ่งนี้ไม่ได้เพิ่มต้นทุนการเทรดของคุณ แต่คุณควรทราบว่าความสัมพันธ์นี้มีอยู่",
    risk3="ภาพนี้เป็นเพียงบทสรุป <b>เงื่อนไขที่ประกาศบนเว็บไซต์เป็นฉบับที่มีผลบังคับ</b>: "
          "presighttrading.com/th/protection.html",
    foot="การเทรดมีความเสี่ยง<br>ยึดตามเงื่อนไขบนเว็บไซต์",
)
