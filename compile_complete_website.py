# -*- coding: utf-8 -*-
"""
MOMO Family Music — Apple.com Minimalist Storefront & Full Multi-Page Ecosystem Builder
=======================================================================================
Architecture:
- index.html        : Ultra-clean Apple.com style flagship storefront (~650 CN chars vs 11,633 previously!)
                      4 Full-Width Hero Billboards + 6 Full-Bleed Promo Tiles (2x3 Grid) -> Dedicated Pages
- membership.html   : Dedicated Page — 2026 Plus 家庭音乐会员 (¥6,000/年)
- curriculum.html   : Dedicated Page — 《通识音乐学习》 + 九大现代专业学科选修矩阵 + 现代音乐风格试听卡片机
- ensemble-lab.html : Dedicated Page — 青少年现代爵士大乐队 (正在招募) & 4-on-1 职业乐队实验室
- faculty.html      : Dedicated Page — 一线艺术家导师智库 (5×2 大画幅全彩肖像矩阵 + 13位导师详情抽屉)
- study-abroad.html : Dedicated Page — 音乐升学与海外名校留学规划专案 (¥38,800 · 高信博士真实档案 & 24轨实录视频)
- spaces.html       : Dedicated Page — 桐梓林花园 × 麓湖私密声场与器材租用
- charity.html      : Dedicated Page — 声音火种与大凉山音乐支教公益 & 3天2晚音乐公益共修营
- store/*.html      : Dedicated Pages — Momo 音乐美学商店及 4 款单品独立页 (全局统一导航与预约)
"""

import os
import re

WEBSITE_DIR = "/Users/timomo/Documents/Momo音乐工作坊总文件/MomoMusicWebsite"
SINGLEPAGE_BAK = os.path.join(WEBSITE_DIR, "compile_complete_website.py.bak_singlepage")
SUBPAGE_BAK_DIR = os.path.join(WEBSITE_DIR, ".subpage_backups")

# ---------------------------------------------------------------------------
# 1. Load all curated data & HTML blocks from compile_complete_website.py.bak_singlepage
#    (Executes only up to `# Assemble the complete new index.html` so nothing is overwritten)
# ---------------------------------------------------------------------------
with open(SINGLEPAGE_BAK, "r", encoding="utf-8") as f:
    bak_code = f.read()

cutoff_marker = "# Assemble the complete new index.html"
cutoff_idx = bak_code.find(cutoff_marker)
if cutoff_idx == -1:
    raise RuntimeError("Could not find cutoff marker in compile_complete_website.py.bak_singlepage")

ns = {}
exec(compile(bak_code[:cutoff_idx], SINGLEPAGE_BAK, "exec"), ns)

head_section = ns["head_section"]
s_style_deck = ns["s_style_deck"]
s_matrix = ns["s_matrix"]
s_general_edu = ns["s_general_edu"]
s_big_band = ns["s_big_band"]
s_membership = ns["s_membership"]
s_giving = ns["s_giving"]

# 升级 s_giving 内部的四大通道按钮，直连具有留言与铭牌互动功能的官方奉献弹窗
s_giving = s_giving.replace(
    'onclick="openBookingModal(\'生态共建：捐赠支持大凉山音乐教育支教基金 / 乡村乐器\')"',
    'onclick="openGivingModal(\'支持大凉山常态化音乐教育支教基金\', \'支教乐器\')"'
).replace(
    'onclick="openBookingModal(\'生态共建：支持 Momo 专业教育板块专项教学奉献金\')"',
    'onclick="openGivingModal(\'支持盲人学子段重生与专业训练\', \'学子扶持\')"'
).replace(
    '支持凉山支教公益 &#8594;',
    '💖 支持支教与乐器 &#8594;'
).replace(
    '支持专项教学奉献金 &#8594;',
    '🎹 支持盲人学子 &#8594;'
)

# 为 charity.html 设计纯净全宽的双轨爱心共建呼唤展台（绝不直接裸露二维码，点击按钮优雅唤出带署名留言的官方收款弹窗）
giving_callout_banner = '''
                <!-- ==================== 官方爱心共建呼唤专区（全宽优雅展台 · 无生硬二维码裸露） ==================== -->
                <div class="mt-14 p-8 sm:p-12 rounded-3xl bg-gradient-to-b from-[#0c1813] via-[#09110d] to-[#060807] border border-[#FF3823]/30 relative overflow-hidden shadow-2xl text-center">
                    <div class="absolute -top-32 -right-32 w-80 h-80 bg-[#FF3823]/10 rounded-full blur-3xl pointer-events-none"></div>
                    <div class="absolute -bottom-32 -left-32 w-80 h-80 bg-amber-400/10 rounded-full blur-3xl pointer-events-none"></div>

                    <div class="relative z-10 max-w-3xl mx-auto space-y-4">
                        <span class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-emerald-400/10 border border-[#FF3823]/30 text-xs font-mono-code font-bold text-[#FF3823] uppercase tracking-widest">
                            <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
                            SOUND OF HOPE · 声音共建守护通道
                        </span>
                        <h3 class="text-2xl sm:text-4xl font-black text-white tracking-tight">
                            做真实的教育 · 每一份奉献都化作琴弦与希望
                        </h3>
                        <p class="text-neutral-300 text-xs sm:text-sm leading-relaxed max-w-xl mx-auto">
                            无需繁琐流程，点击下方按钮手触即可调出官方直连收款码（微信支付「MOMO 共创中心」/ 支付宝「Momo 音乐」），并可为此写下你的心愿寄语与署名，生成专属声音共建者电子纪念铭牌。
                        </p>

                        <div class="pt-3 flex flex-wrap items-center justify-center gap-4">
                            <button
                                type="button"
                                onclick="openGivingModal('我要支持教学设备共建', 'equipment', 'Nord Stage 4 舞台电钢', 200)"
                                class="px-7 py-3.5 rounded-full bg-gradient-to-r from-[#FF3823] to-[#FF5A4D] hover:from-emerald-300 hover:to-teal-300 text-black font-extrabold text-xs sm:text-sm shadow-[0_0_25px_rgba(16,185,129,0.35)] hover:scale-105 active:scale-95 transition-all flex items-center gap-2 cursor-pointer"
                            >
                                <span>🎸 我要支持教学设备器材 (Nord电钢/返听)</span>
                                <span>&rarr;</span>
                            </button>
                            <button
                                type="button"
                                onclick="openGivingModal('资助音乐学者奖助学金', 'scholarship', '年度声音火种·全额卓越奖学金', 6000)"
                                class="px-6 py-3.5 rounded-full bg-amber-400/20 hover:bg-amber-400/30 border border-amber-400/40 text-amber-300 font-semibold text-xs sm:text-sm hover:scale-105 active:scale-95 transition-all flex items-center gap-2 cursor-pointer"
                            >
                                <span>🎓 资助音乐学者奖助学金 / 公开课</span>
                                <span>&rsaquo;</span>
                            </button>
                        </div>
                        <div class="text-[11px] text-neutral-400 font-mono-code pt-2">
                            ✦ 款项 100% 定向透明注入真实教学设备添置与热爱学子奖助学金
                        </div>
                    </div>
                </div>
'''

last_sec_close = s_giving.rfind('</section>')
if last_sec_close != -1:
    s_giving = s_giving[:last_sec_close] + giving_callout_banner + '\n    </section>'

raw_new_faculty = ns["new_faculty"]
new_spaces = ns["new_spaces"]
new_merch_store = ns["new_merch_store"]
footer_and_scripts = ns["footer_and_scripts"]
comprehensive_level2_modals = ns["comprehensive_level2_modals"]
additional_scripts = ns["additional_scripts"]

# Fix the outer duplicate <section id="faculty"> wrapper that existed in raw_new_faculty
inner_fac_marker = "<!-- ==================== 10 位旗舰导师名师长廊 ==================== -->"
if inner_fac_marker in raw_new_faculty:
    clean_faculty_section = "\n        " + raw_new_faculty[raw_new_faculty.find(inner_fac_marker):]
else:
    clean_faculty_section = raw_new_faculty

# 全局更新导师卡片为超清无损单反母本肖像（彻底移除单块效果器与调音台占位）
clean_faculty_section = clean_faculty_section.replace(
    './assets/images/pedalboard.jpg', './assets/images/wang_chongen_card.jpg'
).replace(
    './assets/images/qi_ziyao_studio_console.jpg', './assets/images/qi_ziyao_card.jpg'
).replace(
    './assets/images/gao_xin_cover.jpg', './assets/images/gao_xin_card.jpg'
).replace(
    './assets/images/zhang_qian.jpg', './assets/images/zhang_qian_card.jpg'
).replace(
    './assets/images/mao_wei.jpg', './assets/images/mao_wei_card.jpg'
).replace(
    './assets/images/gou_hanning.jpg', './assets/images/gou_hanning_card.jpg'
).replace(
    './assets/images/joe_longardner.jpg', './assets/images/joe_longardner_card.jpg'
).replace(
    './assets/images/timo_square.jpg', './assets/images/timo_card.jpg'
).replace(
    './assets/images/carlos_square.jpg', './assets/images/carlos_card.jpg'
).replace(
    './assets/images/qiao_xiaoji.jpg', './assets/images/qiao_xiaoji_card.jpg'
)

# 增加第 11 位导师：段重生 (David Duan) 卡片到 clean_faculty_section
duan_card_html = '''
                    <!-- 11. 段重生 (David Duan) -->
                    <div onclick="openFacultyDrawer('duanchongsheng')" class="brutalist-border bg-neutral-950 rounded-lg overflow-hidden group hover:border-momo-mint transition-all duration-300 cursor-pointer flex flex-col justify-between">
                        <div class="aspect-[4/5] bg-neutral-900 overflow-hidden relative">
                            <img src="./assets/images/duan_chongsheng_card.jpg" alt="David Duan 段重生" class="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-500">
                            <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/25 to-transparent"></div>
                            <span class="absolute top-2.5 left-2.5 bg-black/80 backdrop-blur-sm text-[10px] font-mono text-momo-mint font-bold px-2 py-0.5 rounded border border-neutral-800">
                                11 · COMPOSER &amp; PRODUCER
                            </span>
                        </div>
                        <div class="p-4 flex flex-col justify-between flex-grow">
                            <div>
                                <div class="text-[10px] font-mono text-momo-mint uppercase tracking-wider font-semibold">SOUTHAMPTON MMus / PRODUCER</div>
                                <h4 class="text-base font-bold text-white mt-1 group-hover:text-momo-mint transition-colors">段重生 (David)</h4>
                                <p class="text-xs text-neutral-400 mt-1.5 line-clamp-2 leading-relaxed">英国南安普顿大学作曲硕士（Distinction优等） · 国际巡演盲人作曲家 · 听觉色彩大师</p>
                            </div>
                            <div class="mt-3 pt-2.5 border-t border-neutral-900 flex items-center justify-between text-[11px] font-mono text-neutral-400 group-hover:text-white transition-colors">
                                <span>艺术档案</span>
                                <span>&rarr;</span>
                            </div>
                        </div>
                    </div>
'''

target_qi_card_end = '''<p class="text-xs text-neutral-400 mt-1.5 line-clamp-2 leading-relaxed">美国洛杉矶音乐学院（LACM）制作与录音 · P&amp;R Studio 首席音频制作人</p>
                            </div>
                            <div class="mt-3 pt-2.5 border-t border-neutral-900 flex items-center justify-between text-[11px] font-mono text-neutral-400 group-hover:text-white transition-colors">
                                <span>艺术档案</span>
                                <span>&rarr;</span>
                            </div>
                        </div>
                    </div>'''

clean_faculty_section = clean_faculty_section.replace(
    "<!-- 10 位旗舰导师名师长廊 -->",
    "<!-- 11 位旗舰导师名师长廊 -->"
).replace(
    "// 10 FLAGSHIP ARTISTS ROSTER",
    "// 11 FLAGSHIP ARTISTS ROSTER"
).replace(
    "10位名师 · 严格5列×2排黄金矩阵",
    "11位中外名师智库底座"
).replace(
    target_qi_card_end,
    target_qi_card_end + "\n" + duan_card_html
).replace(
    """@media (min-width: 1024px) {
                    .faculty-card-grid {
                        grid-template-columns: repeat(5, minmax(0, 1fr)) !important;
                        gap: 1.5rem;
                    }
                }""",
    """@media (min-width: 1024px) {
                    .faculty-card-grid {
                        grid-template-columns: repeat(4, minmax(0, 1fr)) !important;
                        gap: 1.25rem;
                    }
                }
                @media (min-width: 1280px) {
                    .faculty-card-grid {
                        grid-template-columns: repeat(6, minmax(0, 1fr)) !important;
                        gap: 1.25rem;
                    }
                }"""
)

# 注入段重生（David Duan）完整学术履历至 facultyData
duan_faculty_data = '''        duanchongsheng: {
            name: '段重生 (David Duan)',
            tag: 'SOUTHAMPTON MMus (DISTINCTION) / COMPOSER & PRODUCER',
            title: '英国南安普顿大学作曲硕士（Distinction最高荣誉） · 国际巡演盲人作曲家 · 现代音乐制作人',
            img: './assets/images/duan_chongsheng.jpg',
            bio: `<div class="space-y-4 text-xs leading-relaxed text-neutral-300">
<div>
  <div class="text-[11px] font-mono text-momo-mint font-bold uppercase tracking-wider mb-1">// 教育背景与学术最高荣誉 ACADEMIC BACKGROUND</div>
  <p class="mb-1.5"><strong>英国南安普顿大学（University of Southampton）：</strong>作曲硕士学位（Master of Music in Composition, MMus）。在英深造期间，以严谨宏大的现代管弦配器逻辑与前沿声音设计脱颖而出，以全系最高等级 <strong>Distinction（优等）最高荣誉</strong> 毕业。</p>
  <p><strong>北京联合大学：</strong>音乐学专业学士（BA）。拥有扎实系统的现代作曲理论、曲式和声学底盘与敏锐绝伦的听觉色彩感知力。</p>
</div>

<div>
  <div class="text-[11px] font-mono text-momo-cyan font-bold uppercase tracking-wider mb-1">// 听觉洞察力与超凡艺术境界 INSPIRATIONAL MASTERY</div>
  <p>虽然双目失明，但上天赐予了他超越常人的敏锐听觉世界与纯粹透彻的艺术心灵。段重生精通主流数字音频工作站（DAW）与现代无障碍音乐制作工作流，擅长在黑白琴键与声音算法中调度纷繁复杂的复调和声与音色织体。他的作品结构严谨、音响层次极富诗意，以听觉构建色彩，以声波传递最深沉的生命力量。</p>
</div>

<div>
  <div class="text-[11px] font-mono text-neutral-400 font-bold uppercase tracking-wider mb-1">// 欧美多国巡演与国际艺术协作 GLOBAL TOURS & COLLABORATION</div>
  <p class="mb-1.5"><strong>美国多城巡演 (2026年3月-5月)：</strong>受邀于洛杉矶（Los Angeles）、杰克逊维尔（Jacksonville）、罗利（Raleigh）及亚特兰大（Atlanta）等多地展开高规格学术与现场艺术交流，担纲现场即兴伴奏与现代跨界合作。</p>
  <p class="mb-1.5"><strong>瑞典国际艺术节巡演 (2023年-2024年7月)：</strong>两度远赴北欧瑞典参加艺术节及现代音乐研讨，展现成熟跨文化语境下的音乐适应力与合作艺术。</p>
  <p><strong>英国伦敦系列专题演出 (2022年-2024年4月)：</strong>三次在伦敦核心高校与青年文化群体举办面向学生的现代作曲专题演出与讲座，推广现代音乐创作与编曲理念。</p>
</div>

<div class="p-3 bg-neutral-900/80 border border-neutral-800 rounded">
  <div class="text-[11px] font-mono text-momo-mint font-bold mb-1">★ 在 Momo 的领衔带教与协同赋能方向</div>
  <p class="text-[11px] text-neutral-400 leading-relaxed">
    • <strong>现代作曲与高级和声色彩研习</strong>：从动机发展、曲式结构到现代管弦/流行编曲的高阶技法传授<br>
    • <strong>DAW 数字音乐制作与音色设计实训</strong>：Logic Pro / Cubase / Pro Tools 音频工程与编曲实战<br>
    • <strong>即兴伴奏与合作艺术带教</strong>：培养超感听觉辨识度与极富生命力的现场即兴互动<br>
    • <strong>英美一流音乐学院作曲与制作硕士作品集学术指导</strong>
  </p>
</div>
</div>`,
            focus: `• <strong>现代作曲理论与高级和声构架</strong>（英国顶尖学府严谨曲式与现代听觉色彩）<br>
• <strong>数字音频工作站（DAW）编曲与音色设计</strong>（Logic Pro / Pro Tools 实体工程创作）<br>
• <strong>即兴伴奏与乐队合作艺术</strong>（敏锐听觉感知与现场多声部呼应）<br>
• <strong>欧美名校作曲与音乐制作作品集指导</strong>（对标英国罗素集团与全球名校标准）`
        },
'''

additional_scripts = additional_scripts.replace(
    "qiziyao: {",
    duan_faculty_data + "        qiziyao: {"
).replace(
    './assets/images/pedalboard.jpg', './assets/images/wang_chongen_card.jpg'
).replace(
    './assets/images/qi_ziyao_studio_console.jpg', './assets/images/qi_ziyao_card.jpg'
).replace(
    './assets/images/gao_xin_cover.jpg', './assets/images/gao_xin_card.jpg'
).replace(
    './assets/images/zhang_qian.jpg', './assets/images/zhang_qian_card.jpg'
).replace(
    './assets/images/mao_wei.jpg', './assets/images/mao_wei_card.jpg'
).replace(
    './assets/images/gou_hanning.jpg', './assets/images/gou_hanning_card.jpg'
).replace(
    './assets/images/joe_longardner.jpg', './assets/images/joe_longardner_card.jpg'
).replace(
    './assets/images/timo_square.jpg', './assets/images/timo_card.jpg'
).replace(
    './assets/images/carlos_square.jpg', './assets/images/carlos_card.jpg'
).replace(
    './assets/images/qiao_xiaoji.jpg', './assets/images/qiao_xiaoji_card.jpg'
)

# Extract modals + core scripts that appear after </footer> in footer_and_scripts
footer_close_idx = footer_and_scripts.find("</footer>")
if footer_close_idx == -1:
    raise RuntimeError("Could not find </footer> in footer_and_scripts")
modals_and_core_scripts = footer_and_scripts[footer_close_idx + len("</footer>"):]



# ---------------------------------------------------------------------------
# 2. Shared Apple.com Global Header, Global Footer & Head Helper
# ---------------------------------------------------------------------------
def build_head(page_title: str, prefix: str = "./") -> str:
    h = re.sub(
        r"<title>.*?</title>",
        f"<title>{page_title}</title>",
        head_section,
        count=1,
        flags=re.DOTALL,
    )
    extra_css = """
    <!-- Google Fonts: JetBrains Mono & Plus Jakarta Sans -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        /* Apple Pro Flagship Storefront & Creative Dynamic Engine */
        body {
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
            background-color: #040406;
            color: #FFFFFF;
        }

        .font-mono-code {
            font-family: 'JetBrains Mono', monospace;
        }

        /* 灵动悬浮导航岛 */
        .floating-nav-island {
            background: rgba(10, 10, 14, 0.78);
            backdrop-filter: blur(28px) saturate(200%);
            -webkit-backdrop-filter: blur(28px) saturate(200%);
            border: 1px solid rgba(255, 255, 255, 0.12);
            box-shadow: 0 16px 36px -10px rgba(0, 0, 0, 0.7), inset 0 1px 0 0 rgba(255, 255, 255, 0.15);
        }

        /* 3D 物理倾斜容器 */
        .tilt-card-container {
            perspective: 1400px;
        }

        .tilt-card {
            transition: transform 0.18s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s ease;
            transform-style: preserve-3d;
            will-change: transform;
        }

        /* 聚光灯流光层 */
        .spotlight-card {
            position: relative;
            background: rgba(14, 14, 18, 0.74);
            border: 1px solid rgba(255, 255, 255, 0.08);
            box-shadow: inset 0 1px 0 0 rgba(255, 255, 255, 0.12), 0 24px 48px -12px rgba(0, 0, 0, 0.6);
            backdrop-filter: blur(24px) saturate(190%);
            -webkit-backdrop-filter: blur(24px) saturate(190%);
            overflow: hidden;
        }

        .spotlight-card::before {
            content: '';
            position: absolute;
            inset: 0;
            background: radial-gradient(800px circle at var(--mouse-x, 50%) var(--mouse-y, 50%), rgba(255, 56, 35, 0.08), transparent 45%);
            pointer-events: none;
            opacity: 0;
            transition: opacity 0.4s ease;
            z-index: 2;
        }

        .spotlight-card:hover::before {
            opacity: 1;
        }

        /* 钛金属扫光光芒动画 */
        @keyframes metallicSheen {
            0% { transform: translateX(-150%) skewX(-20deg); }
            45%, 100% { transform: translateX(250%) skewX(-20deg); }
        }

        .metallic-sheen-sweep {
            position: absolute;
            top: 0;
            left: 0;
            width: 50%;
            height: 100%;
            background: linear-gradient(90deg, transparent 0%, rgba(255, 255, 255, 0.14) 50%, transparent 100%);
            pointer-events: none;
            animation: metallicSheen 6s ease-in-out infinite;
        }

        /* 黑胶唱片物理旋转 */
        @keyframes vinylSpin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .vinyl-disc {
            background: radial-gradient(circle at center, #111 0%, #050505 28%, #161616 29%, #080808 60%, #1c1c1c 61%, #040404 100%);
            box-shadow: 0 12px 36px rgba(0,0,0,0.9), inset 0 0 0 1.5px rgba(255,255,255,0.06);
        }

        .vinyl-spinning {
            animation: vinylSpin 6s linear infinite;
        }

        /* 黑胶唱片封套滑出视差 */
        .vinyl-sleeve-jacket {
            position: relative;
            overflow: visible;
        }

        .vinyl-sleeve-disc {
            position: absolute;
            right: 0;
            top: 50%;
            transform: translateY(-50%) translateX(10%);
            transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
            z-index: 1;
        }

        .vinyl-sleeve-jacket:hover .vinyl-sleeve-disc {
            transform: translateY(-50%) translateX(45%) rotate(45deg);
        }

        /* 双向流体跑马灯 */
        @keyframes marqueeScrollLeft {
            0% { transform: translateX(0%); }
            100% { transform: translateX(-50%); }
        }

        @keyframes marqueeScrollRight {
            0% { transform: translateX(-50%); }
            100% { transform: translateX(0%); }
        }

        .marquee-track-left {
            display: flex;
            width: max-content;
            animation: marqueeScrollLeft 38s linear infinite;
        }

        .marquee-track-right {
            display: flex;
            width: max-content;
            animation: marqueeScrollRight 38s linear infinite;
        }

        .marquee-wrapper:hover .marquee-track-left,
        .marquee-wrapper:hover .marquee-track-right {
            animation-play-state: paused;
        }

        /* 动态多轨均衡器声波 */
        .eq-bar {
            width: 3.5px;
            background: #00E5FF;
            border-radius: 2px;
            transition: height 0.1s ease;
            height: 4px;
        }

        .eq-active .eq-bar:nth-child(1) { animation: eqPulse 0.5s ease infinite alternate; }
        .eq-active .eq-bar:nth-child(2) { animation: eqPulse 0.7s ease infinite alternate 0.1s; }
        .eq-active .eq-bar:nth-child(3) { animation: eqPulse 0.4s ease infinite alternate 0.2s; }
        .eq-active .eq-bar:nth-child(4) { animation: eqPulse 0.6s ease infinite alternate 0.15s; }
        .eq-active .eq-bar:nth-child(5) { animation: eqPulse 0.8s ease infinite alternate 0.25s; }

        @keyframes eqPulse {
            0% { height: 4px; }
            100% { height: 26px; }
        }

        /* 打击垫按钮 */
        .sound-pad-btn {
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.08);
            transition: all 0.15s ease;
        }
        .sound-pad-btn:hover {
            background: rgba(255, 255, 255, 0.08);
            border-color: rgba(0, 240, 255, 0.4);
        }
        .sound-pad-btn:active, .sound-pad-btn.pad-active {
            background: rgba(0, 240, 255, 0.22);
            border-color: #00E5FF;
            transform: scale(0.96);
            box-shadow: 0 0 16px rgba(0, 240, 255, 0.35);
        }

        /* Apple.com Flagship Storefront Refinements */
        .apple-nav-glass {
            background: rgba(8, 8, 10, 0.82);
            backdrop-filter: saturate(180%) blur(20px);
            -webkit-backdrop-filter: saturate(180%) blur(20px);
        }
        .apple-link {
            display: inline-flex;
            align-items: center;
            gap: 0.25rem;
            font-weight: 500;
            transition: all 0.2s ease;
        }
        .apple-link:hover {
            text-decoration: underline;
            text-underline-offset: 4px;
        }
        .apple-tile {
            position: relative;
            overflow: hidden;
            border-radius: 1.25rem;
            border: 1px solid rgba(255, 255, 255, 0.08);
            transition: transform 0.45s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.3s ease;
        }
        .apple-tile:hover {
            border-color: rgba(0, 201, 255, 0.45);
        }
        .apple-tile:hover .apple-tile-bg {
            transform: scale(1.04);
        }
        .apple-tile-bg {
            transition: transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
        }
        .faculty-home-grid {
            display: grid !important;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 0.75rem;
        }
        @media (min-width: 640px) {
            .faculty-home-grid {
                grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
                gap: 0.875rem;
            }
        }
        @media (min-width: 900px) {
            .faculty-home-grid {
                grid-template-columns: repeat(4, minmax(0, 1fr)) !important;
                gap: 1rem;
            }
        }
        @media (min-width: 1180px) {
            .faculty-home-grid {
                grid-template-columns: repeat(6, minmax(0, 1fr)) !important;
                gap: 1rem;
            }
        }
    </style>
"""
    h = h.replace("</head>", extra_css + "</head>")
    if prefix != "./":
        h = h.replace("./assets/", f"{prefix}assets/")
    return h


def render_apple_nav(prefix: str = "./", active: str = "home") -> str:
    nav_items = [
        ("membership", "会员 Plus", f"{prefix}membership.html"),
        ("curriculum", "通识与学科", f"{prefix}curriculum.html"),
        ("ensemble", "乐团合奏", f"{prefix}ensemble-lab.html"),
        ("faculty", "导师智库", f"{prefix}faculty.html"),
        ("study", "名校规划", f"{prefix}study-abroad.html"),
        ("spaces", "共享空间", f"{prefix}spaces.html"),
        ("charity", "音乐公益", f"{prefix}charity.html"),
        ("store", "美学商店", f"{prefix}store/index.html"),
    ]

    desktop_links = []
    mobile_links = []
    for key, label, href in nav_items:
        is_act = (key == active)
        cls = "text-[#FF3823] font-bold" if is_act else "text-neutral-300 hover:text-white"
        desktop_links.append(f'<a href="{href}" class="{cls} transition-colors">{label}</a>')
        m_cls = "text-[#FF3823] font-bold bg-[#FF3823]/10 border border-[#FF3823]/30" if is_act else "text-neutral-300 hover:text-white bg-white/[0.04]"
        mobile_links.append(f'<a href="{href}" class="p-2.5 rounded-xl text-center {m_cls} transition-colors">{label}</a>')

    desktop_html = "\n                ".join(desktop_links)
    mobile_html = "\n                ".join(mobile_links)

    return f'''
    <!-- Apple 极简灵动悬浮导航岛 (Minimalist Signal Red Nav) -->
    <nav class="sticky top-3.5 z-50 px-4 sm:px-6 pointer-events-none">
        <div class="max-w-5xl mx-auto floating-nav-island rounded-full px-4 sm:px-5 py-2 sm:py-2.5 flex items-center justify-between pointer-events-auto border border-white/10 bg-[#0a0a0c]/85 backdrop-blur-2xl">
            <!-- 品牌标识 -->
            <a href="{prefix}index.html" class="flex items-center gap-2.5 group focus:outline-none">
                <span class="w-7 h-7 rounded-full bg-[#FF3823] text-white font-black text-xs flex items-center justify-center shadow-[0_0_12px_rgba(255,56,35,0.4)]">
                    M
                </span>
                <span class="text-sm font-extrabold tracking-tight text-white group-hover:text-[#FF3823] transition-colors">
                    MOMO
                </span>
            </a>

            <!-- 核心导航链接 (桌面端) -->
            <div class="hidden md:flex items-center gap-6 text-xs font-medium">
                {desktop_html}
            </div>

            <!-- 右侧微信直连 + 奉献支持 + 预约 + 移动端菜单 -->
            <div class="flex items-center gap-1.5 sm:gap-2">
                <button
                    type="button"
                    onclick="openTimoModal()"
                    class="px-2.5 sm:px-3 py-1 rounded-full bg-[#FF3823]/10 hover:bg-[#FF3823]/20 border border-[#FF3823]/30 hover:border-[#FF3823] text-[11px] font-bold text-[#FF3823] hover:text-white transition-all flex items-center gap-1.5 shadow-sm"
                    title="添加 Timo 创始人个人微信，直接沟通"
                >
                    <span class="w-1.5 h-1.5 rounded-full bg-[#FF3823] animate-pulse"></span>
                    <span>微信聊聊</span>
                </button>
                <button
                    type="button"
                    onclick="openGivingModal('我要支持 MOMO · 声音火种计划')"
                    class="px-2.5 sm:px-3.5 py-1 rounded-full bg-[#FF3823] hover:bg-[#E02E24] text-[11px] font-bold text-white transition-all flex items-center gap-1.5 shadow-[0_0_16px_rgba(255,56,35,0.35)]"
                    title="爱心支持 MOMO 教学设备与奖学金"
                >
                    <span>💖</span>
                    <span class="tracking-tight">支持MOMO</span>
                </button>
                <button
                    type="button"
                    onclick="openBookingModal('导航快捷预约：体验与咨询')"
                    class="hidden sm:inline-flex px-3.5 py-1 rounded-full border border-white/20 bg-white/5 hover:bg-white/15 text-white font-semibold text-xs transition-all shadow-sm"
                >
                    预约
                </button>
                <!-- 移动端汉堡折叠按钮 -->
                <button
                    type="button"
                    onclick="toggleMobileMenu()"
                    class="md:hidden p-1.5 rounded-full text-neutral-300 hover:text-white bg-white/[0.06] border border-white/[0.08]"
                    aria-label="Toggle Menu"
                >
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"></path>
                    </svg>
                </button>
            </div>
        </div>

        <!-- 移动端展开抽屉 -->
        <div id="appleMobileMenu" class="hidden max-w-5xl mx-auto mt-2 p-4 rounded-3xl floating-nav-island border border-white/10 bg-[#0a0a0c]/95 backdrop-blur-2xl pointer-events-auto">
            <div class="grid grid-cols-2 gap-2 text-xs font-medium">
                {mobile_html}
            </div>
            <div class="mt-3 pt-3 border-t border-white/10 grid grid-cols-2 gap-2">
                <button
                    type="button"
                    onclick="openTimoModal(); toggleMobileMenu()"
                    class="w-full py-2.5 rounded-xl bg-[#FF3823]/15 border border-[#FF3823]/40 text-[#FF3823] font-bold text-xs flex items-center justify-center gap-1.5"
                >
                    <span class="w-1.5 h-1.5 rounded-full bg-[#FF3823]"></span>
                    <span>加 Timo 微信</span>
                </button>
                <button
                    type="button"
                    onclick="openGivingModal('我要支持 MOMO · 声音火种计划'); toggleMobileMenu()"
                    class="w-full py-2.5 rounded-xl bg-[#FF3823] text-white font-bold text-xs flex items-center justify-center gap-1.5 shadow-md shadow-[#FF3823]/20"
                >
                    <span>💖 支持 MOMO</span>
                </button>
            </div>
        </div>
    </nav>
    <script>
        function toggleMobileMenu() {{
            const m = document.getElementById('appleMobileMenu');
            if (m) m.classList.toggle('hidden');
        }}
    </script>
    '''


def render_apple_footer_and_scripts(
    prefix: str = "./",
    include_drawers: bool = False,
) -> str:
    footer_html = f'''
    <!-- Apple 极简全局页脚 -->
    <footer class="bg-[#050507] text-neutral-400 pt-16 pb-12 px-6 md:px-12 border-t border-white/[0.08] text-xs">
        <div class="max-w-6xl mx-auto">
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-8 pb-12 border-b border-white/[0.08]">
                <div class="space-y-2.5">
                    <div class="text-white font-semibold">探索生态</div>
                    <ul class="space-y-2 text-neutral-400">
                        <li><a href="{prefix}membership.html" class="hover:text-white transition-colors">2026 Plus 会员</a></li>
                        <li><a href="{prefix}curriculum.html" class="hover:text-white transition-colors">《通识音乐学习》</a></li>
                        <li><a href="{prefix}curriculum.html#matrix" class="hover:text-white transition-colors">九大现代学科选修</a></li>
                        <li><a href="{prefix}curriculum.html#style-deck" class="hover:text-white transition-colors">音乐风格在线试听</a></li>
                    </ul>
                </div>

                <div class="space-y-2.5">
                    <div class="text-white font-semibold">合奏与深造</div>
                    <ul class="space-y-2 text-neutral-400">
                        <li><a href="{prefix}ensemble-lab.html#big-band" class="hover:text-white transition-colors">青少年现代爵士大乐队</a></li>
                        <li><a href="{prefix}ensemble-lab.html#lab-detail" class="hover:text-white transition-colors">4-on-1 职业乐队实验室</a></li>
                        <li><a href="{prefix}faculty.html" class="hover:text-white transition-colors">艺术家导师智库</a></li>
                        <li><a href="{prefix}study-abroad.html" class="hover:text-white transition-colors">海外名校留学规划专案</a></li>
                    </ul>
                </div>

                <div class="space-y-2.5">
                    <div class="text-white font-semibold">空间、公益与生活</div>
                    <ul class="space-y-2 text-neutral-400">
                        <li><a href="{prefix}spaces.html" class="hover:text-white transition-colors">桐梓林花园声场</a></li>
                        <li><a href="{prefix}spaces.html" class="hover:text-white transition-colors">麓湖湖畔声场</a></li>
                        <li><a href="{prefix}charity.html" class="hover:text-white transition-colors">声音火种与大凉山支教</a></li>
                        <li><a href="javascript:void(0)" onclick="openGivingModal('MOMO 官方爱心奉献窗口')" class="text-[#FF3823] hover:text-white transition-colors font-medium flex items-center gap-1"><span>✦ 官方爱心奉献窗口</span></a></li>
                        <li><a href="{prefix}store/index.html" class="hover:text-white transition-colors">Momo 音乐美学商店</a></li>
                    </ul>
                </div>

                <div class="space-y-2.5 col-span-2 sm:col-span-1">
                    <div class="text-white font-semibold">成都双空间 · 创始人直接沟通</div>
                    <p class="leading-relaxed text-neutral-400">
                        桐梓林：武侯区银都花园14栋2单元101<br>
                        麓湖：天府新区麓坊中心A座1栋811<br>
                        主理人电邮：tixinzhang@gmail.com
                    </p>
                    <div class="pt-1 flex flex-col gap-2">
                        <button type="button" onclick="openTimoModal()" class="px-3.5 py-1.5 rounded-full bg-[#FF3823]/20 hover:bg-[#FF3823]/30 border border-[#FF3823]/40 text-[#FF3823] hover:text-white text-xs font-semibold flex items-center justify-center gap-1.5 transition-all w-fit">
                            <span>💬 添加 Timo 创始人微信 (MO 酱~)</span>
                        </button>
                        <button type="button" onclick="openBookingModal('页脚快速预约到店体验')" class="apple-link text-[#FF3823] hover:text-cyan-300 text-left">
                            <span>预约来空间喝杯咖啡</span><span>&rsaquo;</span>
                        </button>
                    </div>
                </div>
            </div>

            <div class="pt-6 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 text-neutral-400">
                <div>Copyright &copy; 2026 Momo Family Music Studio. 保留所有权利。</div>
                <div class="font-mono-code tracking-wider">KIND • TRUTH • PASSION · CHENGDU</div>
            </div>
        </div>
    </footer>
'''
    core = modals_and_core_scripts
    core = core.replace(
        '<form id="booking-form"',
        '''<div class="mb-4 p-3 rounded-2xl bg-emerald-950/40 border border-[#FF3823]/30 text-xs text-neutral-300 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-2.5">
            <div class="flex items-center gap-2">
                <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                <span class="text-neutral-300">如需爱心奉献支持大山支教与教学基金：</span>
            </div>
            <button type="button" onclick="closeBookingModal(); openGivingModal(\'MOMO 官方爱心奉献窗口\')" class="px-3 py-1 rounded-full bg-[#FF3823] hover:bg-emerald-400 text-black font-bold text-[11px] transition-all shadow-sm shrink-0">
                打开直接收款码 &rsaquo;
            </button>
        </div>
        <form id="booking-form"'''
    )
    extra_modals = comprehensive_level2_modals if include_drawers else ""
    extra_js = additional_scripts.replace(
        "声音: 已开启原声 (再次点击静音)", "原声播放中"
    ).replace(
        "声音: 静音 (点击开启原声)", "开启原声"
    )

    if prefix != "./":
        core = core.replace("./assets/", f"{prefix}assets/")
        extra_modals = extra_modals.replace("./assets/", f"{prefix}assets/").replace("./store/", f"{prefix}store/")
        extra_js = extra_js.replace("./assets/", f"{prefix}assets/").replace("./store/", f"{prefix}store/")

    creative_js = """
<script>
    // 1. 聚光灯流光跟随 (Spotlight Cursor Tracker)
    document.querySelectorAll('.spotlight-card').forEach(card => {
        card.addEventListener('mousemove', e => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            card.style.setProperty('--mouse-x', `${x}px`);
            card.style.setProperty('--mouse-y', `${y}px`);
        });
    });

    // 2. 3D 物理微倾斜 (Tilt Card Effect)
    document.querySelectorAll('.tilt-card-container').forEach(container => {
        const card = container.querySelector('.tilt-card');
        if (!card) return;

        container.addEventListener('mousemove', e => {
            const rect = container.getBoundingClientRect();
            const x = e.clientX - rect.left - rect.width / 2;
            const y = e.clientY - rect.top - rect.height / 2;
            const rotateX = -(y / (rect.height / 2)) * 4.5;
            const rotateY = (x / (rect.width / 2)) * 4.5;
            card.style.transform = `rotateX(${rotateX.toFixed(2)}deg) rotateY(${rotateY.toFixed(2)}deg) scale3d(1.01, 1.01, 1.01)`;
        });

        container.addEventListener('mouseleave', () => {
            card.style.transform = 'rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)';
        });
    });

    // 3. Web Audio 引擎与可演奏琴盒
    let sharedAudioCtx = null;
    function getAudioContext() {
        if (!sharedAudioCtx) {
            const AudioContextClass = window.AudioContext || window.webkitAudioContext;
            sharedAudioCtx = new AudioContextClass();
        }
        if (sharedAudioCtx.state === 'suspended') {
            sharedAudioCtx.resume();
        }
        return sharedAudioCtx;
    }

    function triggerVisualizer() {
        const eq = document.getElementById('liveEqVisualizer');
        const vinyl = document.getElementById('miniVinylDisc');
        if (eq) {
            eq.classList.add('eq-active');
            setTimeout(() => { if (!isJamming) eq.classList.remove('eq-active'); }, 2200);
        }
        if (vinyl) {
            vinyl.classList.add('vinyl-spinning');
            setTimeout(() => { if (!isJamming) vinyl.classList.remove('vinyl-spinning'); }, 2600);
        }
    }

    function playAcousticSample(type) {
        const ctx = getAudioContext();
        const now = ctx.currentTime;
        triggerVisualizer();

        const lbl = document.getElementById('currentToneLabel');
        const name = document.getElementById('currentToneName');

        if (type === 'rhodes') {
            if (lbl) lbl.textContent = 'TONE #01 · FENDER RHODES';
            if (name) name.textContent = 'Cmaj9 爵士电钢琴和弦';
            const chord = [164.81, 196.00, 246.94, 293.66, 329.63];
            chord.forEach((freq, idx) => {
                const osc = ctx.createOscillator();
                const gain = ctx.createGain();
                osc.type = 'sine';
                osc.frequency.setValueAtTime(freq, now + idx * 0.035);

                gain.gain.setValueAtTime(0, now + idx * 0.035);
                gain.gain.linearRampToValueAtTime(0.14, now + idx * 0.035 + 0.03);
                gain.gain.exponentialRampToValueAtTime(0.0001, now + idx * 0.035 + 2.4);

                osc.connect(gain);
                gain.connect(ctx.destination);
                osc.start(now + idx * 0.035);
                osc.stop(now + idx * 0.035 + 2.5);
            });
        } else if (type === 'bass') {
            if (lbl) lbl.textContent = 'TONE #02 · DOUBLE BASS';
            if (name) name.textContent = 'Walking Bass 爵士低音提琴走音';
            const notes = [41.20, 55.00];
            notes.forEach((freq, idx) => {
                const osc = ctx.createOscillator();
                const gain = ctx.createGain();
                osc.type = 'triangle';
                osc.frequency.setValueAtTime(freq, now + idx * 0.4);

                gain.gain.setValueAtTime(0, now + idx * 0.4);
                gain.gain.linearRampToValueAtTime(0.25, now + idx * 0.4 + 0.02);
                gain.gain.exponentialRampToValueAtTime(0.001, now + idx * 0.4 + 0.6);

                osc.connect(gain);
                gain.connect(ctx.destination);
                osc.start(now + idx * 0.4);
                osc.stop(now + idx * 0.4 + 0.65);
            });
        } else if (type === 'guitar') {
            if (lbl) lbl.textContent = 'TONE #03 · FUNK GUITAR';
            if (name) name.textContent = 'Funk 16分切分扫弦音色';
            const freqs = [329.63, 392.00, 493.88];
            [0, 0.12, 0.22].forEach((offset) => {
                freqs.forEach((freq) => {
                    const osc = ctx.createOscillator();
                    const gain = ctx.createGain();
                    osc.type = 'sawtooth';
                    osc.frequency.setValueAtTime(freq, now + offset);

                    gain.gain.setValueAtTime(0, now + offset);
                    gain.gain.linearRampToValueAtTime(0.08, now + offset + 0.01);
                    gain.gain.exponentialRampToValueAtTime(0.0001, now + offset + 0.18);

                    osc.connect(gain);
                    gain.connect(ctx.destination);
                    osc.start(now + offset);
                    osc.stop(now + offset + 0.2);
                });
            });
        } else if (type === 'vinyl') {
            if (lbl) lbl.textContent = 'TONE #04 · VINYL CRACKLE & A432';
            if (name) name.textContent = 'A432Hz 黑胶温暖正弦声学基频';
            const osc = ctx.createOscillator();
            const gain = ctx.createGain();
            osc.type = 'sine';
            osc.frequency.setValueAtTime(432.0, now);

            gain.gain.setValueAtTime(0, now);
            gain.gain.linearRampToValueAtTime(0.12, now + 0.05);
            gain.gain.exponentialRampToValueAtTime(0.0001, now + 2.0);

            osc.connect(gain);
            gain.connect(ctx.destination);
            osc.start(now);
            osc.stop(now + 2.1);
        }
    }

    // 4. JAM MODE 自动即兴循环慢摇
    let jamTimer = null;
    let isJamming = false;
    function toggleJamMode() {
        const btn = document.getElementById('jamModeBtn');
        const dot = document.getElementById('jamDot');
        const txt = document.getElementById('jamText');
        const eq = document.getElementById('liveEqVisualizer');
        const vinyl = document.getElementById('miniVinylDisc');

        if (isJamming) {
            isJamming = false;
            if (jamTimer) clearInterval(jamTimer);
            if (dot) dot.classList.remove('animate-ping', 'bg-emerald-400');
            if (dot) dot.classList.add('bg-cyan-400');
            if (txt) txt.textContent = '开启 JAM MODE (4小节爵士慢摇即兴)';
            if (eq) eq.classList.remove('eq-active');
            if (vinyl) vinyl.classList.remove('vinyl-spinning');
            const lbl = document.getElementById('currentToneLabel');
            const name = document.getElementById('currentToneName');
            if (lbl) lbl.textContent = 'JAM PAUSED';
            if (name) name.textContent = '点击音色按键即兴弹奏';
        } else {
            isJamming = true;
            if (dot) dot.classList.add('animate-ping', 'bg-emerald-400');
            if (txt) txt.textContent = 'JAM PLAYING · 点击停止慢摇即兴';
            if (eq) eq.classList.add('eq-active');
            if (vinyl) vinyl.classList.add('vinyl-spinning');
            const lbl = document.getElementById('currentToneLabel');
            const name = document.getElementById('currentToneName');
            if (lbl) lbl.textContent = 'JAM MODE ACTIVE // 4-BAR CHILL GROOVE';
            if (name) name.textContent = '正在播放：成都午后 Chill Jazz 即兴循环';

            playAcousticSample('rhodes');
            setTimeout(() => { if (isJamming) playAcousticSample('bass'); }, 800);
            setTimeout(() => { if (isJamming) playAcousticSample('guitar'); }, 1600);

            jamTimer = setInterval(() => {
                if (!isJamming) return;
                playAcousticSample('rhodes');
                setTimeout(() => { if (isJamming) playAcousticSample('bass'); }, 800);
                setTimeout(() => { if (isJamming) playAcousticSample('guitar'); }, 1600);
            }, 3200);
        }
    }

    // 5. 顶部灵动导航岛 A432Hz 开关
    let navAmbientPlaying = false;
    let navOsc = null;
    let navGain = null;
    function toggleNavAmbient() {
        const dot = document.getElementById('navSoundDot');
        const lbl = document.getElementById('navSoundLabel');
        const ctx = getAudioContext();

        if (navAmbientPlaying) {
            navAmbientPlaying = false;
            if (navGain) {
                navGain.gain.setValueAtTime(navGain.gain.value, ctx.currentTime);
                navGain.gain.linearRampToValueAtTime(0.0001, ctx.currentTime + 0.4);
                setTimeout(() => { if (navOsc) navOsc.stop(); }, 450);
            }
            if (dot) dot.classList.remove('bg-emerald-400', 'animate-pulse');
            if (dot) dot.classList.add('bg-cyan-400');
            if (lbl) lbl.textContent = 'A432Hz';
        } else {
            navAmbientPlaying = true;
            navOsc = ctx.createOscillator();
            navGain = ctx.createGain();
            navOsc.type = 'sine';
            navOsc.frequency.setValueAtTime(432.0, ctx.currentTime);

            navGain.gain.setValueAtTime(0.0001, ctx.currentTime);
            navGain.gain.linearRampToValueAtTime(0.06, ctx.currentTime + 1.2);

            navOsc.connect(navGain);
            navGain.connect(ctx.destination);
            navOsc.start();

            if (dot) dot.classList.remove('bg-cyan-400');
            if (dot) dot.classList.add('bg-emerald-400', 'animate-pulse');
            if (lbl) lbl.textContent = '432Hz PLAYING';
        }
    }

    // 7. 全局爱心奉献窗口 (Giving Modal) 双轨共建交互引擎
    let currentGivingCategory = 'equipment'; // 'equipment' | 'scholarship'
    let currentGivingItem = 'Nord Stage 4 舞台电钢';
    let currentItemGap = 9500;
    let currentItemMemo = '设备·Nord';
    let currentGivingAmount = 200;

    function openGivingModal(title, category, defaultItem, defaultAmount) {
        const modal = document.getElementById('giving-modal');
        if (!modal) return;
        if (title) {
            const titleEl = document.getElementById('giving-modal-title');
            if (titleEl) {
                titleEl.innerHTML = '<span>💖</span> <span>' + title + '</span>';
            }
        }
        modal.classList.remove('hidden');
        modal.classList.add('flex');
        document.body.style.overflow = 'hidden';

        if (category) {
            selectGivingCategory(category);
        } else {
            selectGivingCategory('equipment');
        }

        if (defaultItem) {
            if (defaultItem.indexOf('Nord') !== -1) {
                selectGivingItem('Nord Stage 4 舞台电钢', 9500, '设备·Nord');
            } else if (defaultItem.indexOf('Genelec') !== -1 || defaultItem.indexOf('监听') !== -1 || defaultItem.indexOf('返听') !== -1) {
                selectGivingItem('Genelec 8030 监听返听箱', 7600, '设备·Genelec');
            } else if (defaultItem.indexOf('白板笔') !== -1 || defaultItem.indexOf('耗材') !== -1) {
                selectGivingItem('无尘白板笔教学耗材组', 260, '设备·白板笔');
            } else if (defaultItem.indexOf('全额') !== -1 || defaultItem.indexOf('卓越') !== -1) {
                selectGivingItem('年度声音火种·全额卓越奖学金', 6000, '奖学金·全额');
            } else if (defaultItem.indexOf('半额') !== -1 || defaultItem.indexOf('助学') !== -1) {
                selectGivingItem('家庭音乐伙伴·半额成长助学金', 3000, '助学金·半额');
            } else if (defaultItem.indexOf('公开课') !== -1 || defaultItem.indexOf('大师课') !== -1) {
                selectGivingItem('社区公开大师课专项基金', 1000, '公开课·社区');
            }
        }

        if (defaultAmount && Number(defaultAmount) > 0) {
            setGivingAmount(Number(defaultAmount));
        } else {
            setGivingAmount(200);
        }

        switchGivingChannel('wechat');
    }

    function closeGivingModal(e) {
        if (e && e.target !== e.currentTarget) return;
        const modal = document.getElementById('giving-modal');
        if (modal) {
            modal.classList.add('hidden');
            modal.classList.remove('flex');
            document.body.style.overflow = '';
        }
    }

    function switchGivingChannel(channel) {
        const wechatTab = document.getElementById('giving-tab-wechat');
        const alipayTab = document.getElementById('giving-tab-alipay');
        const wechatCard = document.getElementById('giving-card-wechat');
        const alipayCard = document.getElementById('giving-card-alipay');

        if (channel === 'wechat') {
            if (wechatTab) wechatTab.className = 'flex-1 py-1.5 rounded-lg bg-[#FF3823] text-white font-bold transition-all flex items-center justify-center gap-1.5 shadow';
            if (alipayTab) alipayTab.className = 'flex-1 py-1.5 rounded-lg text-neutral-400 hover:text-white transition-all flex items-center justify-center gap-1.5';
            if (wechatCard) wechatCard.classList.remove('hidden');
            if (alipayCard) alipayCard.classList.add('hidden');
        } else {
            if (alipayTab) alipayTab.className = 'flex-1 py-1.5 rounded-lg bg-[#FF3823] text-white font-bold transition-all flex items-center justify-center gap-1.5 shadow';
            if (wechatTab) wechatTab.className = 'flex-1 py-1.5 rounded-lg text-neutral-400 hover:text-white transition-all flex items-center justify-center gap-1.5';
            if (alipayCard) alipayCard.classList.remove('hidden');
            if (wechatCard) wechatCard.classList.add('hidden');
        }
    }

    function selectGivingCategory(category) {
        currentGivingCategory = category;
        const eqBtn = document.getElementById('cat-btn-equipment');
        const scBtn = document.getElementById('cat-btn-scholarship');
        const eqSub = document.getElementById('subitems-equipment');
        const scSub = document.getElementById('subitems-scholarship');

        if (category === 'equipment') {
            if (eqBtn) eqBtn.className = 'py-2.5 px-3 rounded-xl border border-[#FF3823]/50 bg-[#FF3823]/20 text-[#FF3823] font-bold transition-all flex items-center justify-center gap-2 shadow-sm';
            if (scBtn) scBtn.className = 'py-2.5 px-3 rounded-xl border border-white/10 bg-white/[0.04] text-neutral-300 hover:text-white transition-all flex items-center justify-center gap-2';
            if (eqSub) eqSub.classList.remove('hidden');
            if (scSub) scSub.classList.add('hidden');
            selectGivingItem('Nord Stage 4 舞台电钢', 9500, '设备·Nord');
        } else {
            if (scBtn) scBtn.className = 'py-2.5 px-3 rounded-xl border border-amber-500/50 bg-amber-500/20 text-amber-300 font-bold transition-all flex items-center justify-center gap-2 shadow-sm';
            if (eqBtn) eqBtn.className = 'py-2.5 px-3 rounded-xl border border-white/10 bg-white/[0.04] text-neutral-300 hover:text-white transition-all flex items-center justify-center gap-2';
            if (scSub) scSub.classList.remove('hidden');
            if (eqSub) eqSub.classList.add('hidden');
            selectGivingItem('年度声音火种·全额卓越奖学金', 6000, '奖学金·全额');
        }
    }

    function selectGivingItem(itemName, gapAmount, memoCode) {
        currentGivingItem = itemName;
        currentItemGap = gapAmount;
        currentItemMemo = memoCode;

        // 更新按钮选中状态
        const buttons = document.querySelectorAll('.giving-item-btn');
        buttons.forEach(btn => {
            if (btn.textContent.indexOf(itemName.slice(0, 4)) !== -1 || (itemName.indexOf('Nord') !== -1 && btn.textContent.indexOf('Nord') !== -1) || (itemName.indexOf('Genelec') !== -1 && btn.textContent.indexOf('真力') !== -1)) {
                btn.className = 'giving-item-btn p-2 rounded-xl border border-[#FF3823]/50 bg-[#FF3823]/20 text-[#FF3823] font-bold transition-all text-center leading-tight shadow-sm';
            } else {
                btn.className = 'giving-item-btn p-2 rounded-xl border border-white/10 bg-white/[0.03] text-neutral-300 hover:text-white transition-all text-center leading-tight';
            }
        });

        const claimBtn = document.getElementById('btn-claim-remaining');
        if (claimBtn) {
            claimBtn.textContent = '全额认领(¥' + gapAmount + ')';
        }

        updateGivingPlaque();
    }

    function setGivingAmount(amt) {
        currentGivingAmount = amt;
        const customInput = document.getElementById('giving-custom-amount');
        if (customInput) customInput.value = amt;

        // 更新预设金额按钮激活态
        const amtBtns = document.querySelectorAll('.giving-amt-btn');
        amtBtns.forEach(b => {
            if (b.textContent.trim() === '¥' + amt) {
                b.className = 'giving-amt-btn py-1.5 rounded-lg border border-[#FF3823]/50 bg-[#FF3823]/20 text-[#FF3823] font-bold transition-all text-center';
            } else {
                b.className = 'giving-amt-btn py-1.5 rounded-lg border border-white/15 bg-white/[0.04] text-neutral-200 hover:text-white hover:border-[#FF3823] transition-all text-center';
            }
        });

        updateGivingPlaque();
    }

    function claimRemainingDifference() {
        setGivingAmount(currentItemGap);
    }

    function onCustomAmountChange() {
        const customInput = document.getElementById('giving-custom-amount');
        if (customInput && customInput.value) {
            currentGivingAmount = Math.max(1, Number(customInput.value));
            // 清除预设按钮激活态
            const amtBtns = document.querySelectorAll('.giving-amt-btn');
            amtBtns.forEach(b => {
                if (b.textContent.trim() === '¥' + currentGivingAmount) {
                    b.className = 'giving-amt-btn py-1.5 rounded-lg border border-[#FF3823]/50 bg-[#FF3823]/20 text-[#FF3823] font-bold transition-all text-center';
                } else {
                    b.className = 'giving-amt-btn py-1.5 rounded-lg border border-white/15 bg-white/[0.04] text-neutral-200 hover:text-white transition-all text-center';
                }
            });
            updateGivingPlaque();
        }
    }

    function updateGivingPlaque() {
        const nameInput = document.getElementById('giving-donor-name');
        const memoInput = document.getElementById('giving-donor-memo');
        const donorDisplay = document.getElementById('plaque-donor-display');
        const memoDisplay = document.getElementById('plaque-memo-display');
        const amountDisplay = document.getElementById('plaque-amount-display');
        const honorTitle = document.getElementById('plaque-honor-title');
        const purposeTag = document.getElementById('plaque-purpose-tag');
        const memoSuggested = document.getElementById('giving-suggested-memo');

        const donorName = (nameInput && nameInput.value.trim()) ? nameInput.value.trim() : '一位热爱音乐的朋友';
        const donorMemo = (memoInput && memoInput.value.trim()) ? memoInput.value.trim() : '做真实的教育，让真诚的音符在每一个心灵自由发芽。';

        if (donorDisplay) donorDisplay.textContent = donorName;
        if (memoDisplay) memoDisplay.textContent = '“' + donorMemo + '”';
        if (amountDisplay) amountDisplay.textContent = '共建助力：¥' + currentGivingAmount;
        if (purposeTag) purposeTag.textContent = currentGivingItem;

        if (honorTitle) {
            if (currentGivingCategory === 'equipment') {
                honorTitle.textContent = 'MOMO 声音设备奠基人';
            } else {
                honorTitle.textContent = 'MOMO 2026 年度学者守护者';
            }
        }

        if (memoSuggested) {
            memoSuggested.textContent = currentItemMemo + '·' + donorName + '·¥' + currentGivingAmount;
        }
    }

    function copyGivingMemo() {
        const memoSuggested = document.getElementById('giving-suggested-memo');
        const label = document.getElementById('memo-copy-label');
        if (!memoSuggested) return;

        const textToCopy = memoSuggested.textContent.trim();
        if (navigator.clipboard && navigator.clipboard.writeText) {
            navigator.clipboard.writeText(textToCopy).then(() => {
                if (label) {
                    label.textContent = '已复制 ✓';
                    setTimeout(() => { label.textContent = '复制'; }, 2000);
                }
            }).catch(() => {
                if (label) {
                    label.textContent = '长按复制';
                    setTimeout(() => { label.textContent = '复制'; }, 2000);
                }
            });
        } else {
            if (label) {
                label.textContent = '长按复制';
                setTimeout(() => { label.textContent = '复制'; }, 2000);
            }
        }
    }

    function submitGivingPlaque() {
        const preview = document.getElementById('giving-plaque-preview');
        const feedback = document.getElementById('giving-submit-feedback');
        const btn = document.getElementById('giving-submit-btn');

        if (preview) {
            preview.classList.add('ring-2', 'ring-emerald-400', 'shadow-[0_0_30px_rgba(16,185,129,0.4)]');
        }
        if (feedback) {
            feedback.classList.remove('hidden');
        }
        if (btn) {
            btn.innerHTML = '<span>✓ 铭牌已记录在案 · 再次感谢同行</span>';
            btn.classList.remove('from-[#FF3823]', 'to-teal-500');
            btn.classList.add('bg-neutral-800', 'text-[#FF3823]');
        }
    }

    // 8. 全局 Timo 创始人微信弹窗控制
    function openTimoModal() {
        const modal = document.getElementById('timo-contact-modal');
        if (modal) {
            modal.classList.remove('hidden');
            modal.classList.add('flex');
            document.body.style.overflow = 'hidden';
        }
    }

    function closeTimoModal(e) {
        if (e && e.target !== e.currentTarget) return;
        const modal = document.getElementById('timo-contact-modal');
        if (modal) {
            modal.classList.add('hidden');
            modal.classList.remove('flex');
            document.body.style.overflow = '';
        }
    }

    // 6. 移动端折叠导航切换
    function toggleMobileMenu() {
        const panel = document.getElementById('mobile-menu');
        if (panel) {
            panel.classList.toggle('hidden');
        }
    }
</script>
"""

    # Inject extra_js, creative_js, giving_modal and timo_contact_modal safely right before </body>
    with open(os.path.join(WEBSITE_DIR, "assets/snippets/giving_modal.html"), "r", encoding="utf-8") as gmf:
        giving_modal_raw = gmf.read()
    with open(os.path.join(WEBSITE_DIR, "assets/snippets/timo_contact_modal.html"), "r", encoding="utf-8") as tmf:
        timo_contact_modal_raw = tmf.read()
    if prefix != "./":
        giving_modal_raw = giving_modal_raw.replace("./assets/", f"{prefix}assets/")
        timo_contact_modal_raw = timo_contact_modal_raw.replace("./assets/", f"{prefix}assets/")
    combined = extra_modals + "\n" + giving_modal_raw + "\n" + timo_contact_modal_raw + "\n" + footer_html + "\n" + core
    b_idx = combined.rfind("</body>")
    if b_idx != -1:
        combined = combined[:b_idx] + "\n" + creative_js + "\n" + extra_js + "\n" + combined[b_idx:]
    else:
        combined = combined + "\n" + creative_js + "\n" + extra_js + "\n</body>\n</html>"
    return combined


# ---------------------------------------------------------------------------
# 3. BUILD PAGE 1: index.html (Apple Pro Flagship Storefront with Syncopated Bento)
# ---------------------------------------------------------------------------
apple_home_main = '''
    <main class="max-w-7xl mx-auto px-4 sm:px-6 pt-4 sm:pt-6 space-y-16 sm:space-y-24 pb-16">
        <!-- ==================== 01. 首屏 4K 巨幕：大标题 · 真实展示 · 绝不挡脸 ==================== -->
        <section class="space-y-6">
            <div class="spotlight-card rounded-3xl h-[460px] sm:h-[540px] lg:h-[580px] relative overflow-hidden flex flex-col justify-end p-8 sm:p-14 border border-white/10 bg-black">
                <video
                    id="hero-bg-video"
                    autoplay
                    loop
                    muted
                    playsinline
                    preload="auto"
                    poster="./assets/images/hero_trumpet.jpg"
                    class="absolute inset-0 w-full h-full object-cover object-[65%_center] sm:object-center brightness-105"
                >
                    <source src="./assets/media/hero_stage_loop.mp4" type="video/mp4">
                    <source src="./assets/media/hero_stage_stream.mp4" type="video/mp4">
                </video>

                <!-- 暗角保护：仅左下角微暗，确保文字锋利，菲比与乐手面部完全通透 -->
                <div class="absolute inset-0" style="background: radial-gradient(ellipse 65% 75% at 0% 100%, rgba(5,5,8,0.92) 0%, rgba(5,5,8,0.5) 55%, transparent 80%); pointer-events: none;"></div>
                <div class="absolute inset-x-0 bottom-0 h-36 bg-gradient-to-t from-[#060608] via-[#060608]/40 to-transparent pointer-events-none"></div>

                <!-- 顶部状态胶囊 -->
                <div class="absolute top-6 left-6 sm:top-8 sm:left-12 z-20">
                    <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-black/60 backdrop-blur-xl border border-white/15 text-xs text-neutral-200">
                        <span class="w-2 h-2 rounded-full bg-[#FF3823] animate-pulse"></span>
                        <span class="text-[#FF3823] font-bold font-mono-code">A432Hz ON STAGE</span>
                        <span class="text-neutral-500">|</span>
                        <span>桐梓林 × 麓湖双空间</span>
                    </div>
                </div>

                <div class="relative z-10 max-w-xl">
                    <p class="text-[11px] font-mono-code uppercase tracking-[0.25em] text-[#FF3823] font-bold">
                        KIND · TRUTH · PASSION
                    </p>
                    <h1 class="text-3xl sm:text-5xl lg:text-6xl font-black tracking-tight leading-[1.05] text-white mt-2">
                        让音乐回到真实生活。
                    </h1>
                    <p class="mt-3 text-xs sm:text-base text-neutral-200 font-normal leading-relaxed max-w-lg">
                        现代流行与爵士 · 真实乐队合奏 · 国际升学规划 · 社区共创
                    </p>
                    <div class="mt-6 flex flex-wrap items-center gap-3">
                        <a href="./membership.html" class="px-6 py-2.5 rounded-full bg-white text-black font-bold text-xs hover:bg-neutral-200 transition-all shadow-lg flex items-center gap-1.5">
                            <span>探索 2026 Plus 会员</span>
                            <span>&rarr;</span>
                        </a>
                        <button type="button" onclick="openTimoModal()" class="px-5 py-2.5 rounded-full bg-[#FF3823]/15 hover:bg-[#FF3823]/25 border border-[#FF3823]/50 text-xs font-bold text-[#FF3823] hover:text-white transition-all flex items-center gap-2 shadow-[0_0_15px_rgba(255,56,35,0.25)]">
                            <span class="w-1.5 h-1.5 rounded-full bg-[#FF3823] animate-pulse"></span>
                            <span>💬 微信直连主理人 Timo</span>
                        </button>
                        <button type="button" onclick="openGivingModal('我要支持 MOMO · 声音火种计划')" class="px-4 py-2.5 rounded-full bg-[#FF3823] hover:bg-[#E02E24] text-xs font-bold text-white transition-all flex items-center gap-1.5 shadow-md shadow-[#FF3823]/25">
                            <span>💖 支持 MOMO</span>
                        </button>
                    </div>
                </div>

                <!-- 右下角原声胶囊 -->
                <div class="absolute bottom-6 right-6 sm:bottom-8 sm:right-10 z-20">
                    <button
                        id="hero-sound-btn"
                        type="button"
                        onclick="toggleHeroSound()"
                        class="flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-black/70 backdrop-blur-md border border-white/20 text-xs text-neutral-300 hover:text-white hover:border-[#FF3823] transition-all"
                    >
                        <span id="hero-sound-icon">🔇</span>
                        <span id="hero-sound-text">开启原声</span>
                    </button>
                </div>
            </div>
        </section>

        <!-- ==================== 02. 摸摸好和弦 (互动声学) + 会员 Plus 旗舰卡 ==================== -->
        <section class="space-y-6">
            <div class="flex items-baseline justify-between border-b border-white/[0.08] pb-4">
                <div>
                    <span class="text-[10px] font-mono-code uppercase tracking-[0.25em] text-[#FF3823] font-bold">// REAL SOUND</span>
                    <h2 class="text-2xl sm:text-3xl font-extrabold tracking-tight text-white mt-1">听听 MOMO 的真实声音</h2>
                </div>
                <span class="text-xs text-neutral-400 font-mono-code hidden sm:inline">TOUCH &amp; JAM</span>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-stretch">
                <!-- 左侧: 会员 Plus 旗舰卡 -->
                <div class="lg:col-span-7 tilt-card-container">
                    <div class="tilt-card spotlight-card rounded-3xl p-8 sm:p-10 h-full flex flex-col justify-between relative overflow-hidden group border border-white/10 bg-[#0d0e12]">
                        <div class="metallic-sheen-sweep"></div>
                        <div class="absolute -top-32 -right-32 w-80 h-80 bg-[#FF3823]/10 rounded-full blur-3xl pointer-events-none"></div>
                        <img src="./assets/images/momo_platinum_card.jpg" alt="MOMO Platinum Card" class="absolute right-0 bottom-0 w-3/5 max-w-sm object-contain opacity-30 group-hover:opacity-60 group-hover:scale-105 transition-all duration-700 pointer-events-none">

                        <div class="relative z-10">
                            <div class="flex items-center justify-between">
                                <span class="text-[10px] font-mono-code uppercase tracking-[0.25em] text-[#FF3823] font-bold">2026 PLUS PASS</span>
                                <span class="px-2.5 py-0.5 rounded-full bg-white/[0.08] text-[10px] text-neutral-300 border border-white/[0.1]">一人入会 · 全家共享</span>
                            </div>
                            <h3 class="text-2xl sm:text-4xl font-extrabold tracking-tight text-white mt-4 leading-tight">
                                MOMO 家庭音乐会员
                            </h3>
                            <p class="text-xs sm:text-sm text-neutral-300 mt-2 max-w-md leading-relaxed">
                                365 天家庭音乐生态底座：12 次专属指导、4 师 1 生真乐队合奏、录音棚单曲实录与专属家庭档案。
                            </p>
                        </div>

                        <div class="relative z-10 pt-6 mt-6 border-t border-white/10 flex flex-col sm:flex-row sm:items-end justify-between gap-4">
                            <div>
                                <div class="flex items-baseline gap-2">
                                    <span class="text-3xl sm:text-4xl font-black text-white">¥6,000</span>
                                    <span class="text-xs text-neutral-400 font-mono-code">/ 年 (约 ¥16.4/天)</span>
                                </div>
                                <div class="text-[11px] text-neutral-400 mt-1">✦ 7 天无理由全额退款保障 · 赠定制文化衫</div>
                            </div>
                            <a href="./membership.html" class="px-6 py-3 rounded-full bg-white text-black font-bold text-xs hover:bg-[#FF3823] hover:text-white transition-all shadow-lg flex items-center justify-center gap-1.5 shrink-0">
                                <span>查阅完整权益</span>
                                <span>&rarr;</span>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- 右侧: 四音色琴盒与即兴慢摇 -->
                <div class="lg:col-span-5">
                    <div class="spotlight-card rounded-3xl p-6 sm:p-8 h-full flex flex-col justify-between border border-white/10 bg-[#0d0e12] relative">
                        <div>
                            <div class="flex items-center justify-between pb-3 border-b border-white/10">
                                <span class="text-[10px] font-mono-code uppercase tracking-[0.2em] text-[#FF3823] font-bold">ACOUSTIC PADS</span>
                                <div id="liveEqVisualizer" class="flex items-center gap-1 h-5">
                                    <div class="w-1 bg-[#FF3823] rounded-full h-2 transition-all duration-150"></div>
                                    <div class="w-1 bg-[#FF3823] rounded-full h-4 transition-all duration-150"></div>
                                    <div class="w-1 bg-[#FF3823] rounded-full h-1 transition-all duration-150"></div>
                                    <div class="w-1 bg-[#FF3823] rounded-full h-3 transition-all duration-150"></div>
                                </div>
                            </div>
                            <h4 class="text-lg font-bold text-white mt-3">摸摸好和弦</h4>
                            <p class="text-xs text-neutral-400 mt-1">点击按键，感受不同乐器的真实律动：</p>

                            <!-- 4 块触感音色键位 -->
                            <div class="grid grid-cols-2 gap-2.5 mt-4">
                                <button
                                    type="button"
                                    id="pad-rhodes"
                                    onclick="triggerPadTone('rhodes')"
                                    class="tone-pad-btn p-3 rounded-2xl bg-white/[0.04] hover:bg-[#FF3823]/20 border border-white/10 hover:border-[#FF3823]/40 text-left transition-all group"
                                >
                                    <div class="text-[10px] font-mono-code text-[#FF3823] font-bold">KEYS 01</div>
                                    <div class="text-xs font-bold text-white mt-0.5">Rhodes 73</div>
                                    <div class="text-[10px] text-neutral-400 mt-0.5">爵士暖调和弦</div>
                                </button>
                                <button
                                    type="button"
                                    id="pad-bass"
                                    onclick="triggerPadTone('bass')"
                                    class="tone-pad-btn p-3 rounded-2xl bg-white/[0.04] hover:bg-[#FF3823]/20 border border-white/10 hover:border-[#FF3823]/40 text-left transition-all group"
                                >
                                    <div class="text-[10px] font-mono-code text-[#FF3823] font-bold">BASS 02</div>
                                    <div class="text-xs font-bold text-white mt-0.5">Double Bass</div>
                                    <div class="text-[10px] text-neutral-400 mt-0.5">原声行走贝斯</div>
                                </button>
                                <button
                                    type="button"
                                    id="pad-guitar"
                                    onclick="triggerPadTone('guitar')"
                                    class="tone-pad-btn p-3 rounded-2xl bg-white/[0.04] hover:bg-[#FF3823]/20 border border-white/10 hover:border-[#FF3823]/40 text-left transition-all group"
                                >
                                    <div class="text-[10px] font-mono-code text-[#FF3823] font-bold">GROOVE 03</div>
                                    <div class="text-xs font-bold text-white mt-0.5">Funk Guitar</div>
                                    <div class="text-[10px] text-neutral-400 mt-0.5">清脆扫弦切音</div>
                                </button>
                                <button
                                    type="button"
                                    id="pad-vinyl"
                                    onclick="triggerPadTone('vinyl')"
                                    class="tone-pad-btn p-3 rounded-2xl bg-white/[0.04] hover:bg-[#FF3823]/20 border border-white/10 hover:border-[#FF3823]/40 text-left transition-all group"
                                >
                                    <div class="text-[10px] font-mono-code text-[#FF3823] font-bold">ANALOG 04</div>
                                    <div class="text-xs font-bold text-white mt-0.5">Vinyl A432</div>
                                    <div class="text-[10px] text-neutral-400 mt-0.5">黑胶温暖底噪</div>
                                </button>
                            </div>
                        </div>

                        <!-- 慢摇即兴开关 -->
                        <div class="mt-4 pt-3 border-t border-white/10">
                            <button
                                type="button"
                                id="jamModeBtn"
                                onclick="toggleJamMode()"
                                class="w-full py-2.5 rounded-full bg-white/5 hover:bg-[#FF3823]/20 border border-white/15 hover:border-[#FF3823]/50 text-xs font-bold text-neutral-200 hover:text-white transition-all flex items-center justify-center gap-2"
                            >
                                <span id="jamDot" class="w-2 h-2 rounded-full bg-neutral-500"></span>
                                <span id="jamText">开启 JAM MODE (4小节爵士慢摇)</span>
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ==================== 03. 导师长廊：大画幅肖像 · 拒绝长篇大论 ==================== -->
        <section class="space-y-6">
            <div class="flex items-baseline justify-between border-b border-white/[0.08] pb-4">
                <div>
                    <span class="text-[10px] font-mono-code uppercase tracking-[0.25em] text-[#FF3823] font-bold">// ARTISTS &amp; FACULTY</span>
                    <h2 class="text-2xl sm:text-3xl font-extrabold tracking-tight text-white mt-1">与真正的音乐家并肩</h2>
                </div>
                <a href="./faculty.html" class="text-xs text-neutral-400 hover:text-white font-mono-code flex items-center gap-1 transition-colors">
                    <span>查阅全部 35 位导师档案</span>
                    <span>&rarr;</span>
                </a>
            </div>

            <!-- 双排反向交错流动长廊 -->
            <div class="relative overflow-hidden py-2 space-y-4">
                <!-- 上排: Track A 向左流动 -->
                <div class="marquee-track-a flex gap-4 w-max">
                    <!-- 1. Timo -->
                    <div onclick="openFacultyDrawer(0)" class="w-48 sm:w-56 rounded-2xl overflow-hidden bg-neutral-900 border border-white/10 hover:border-[#FF3823] transition-all cursor-pointer group shrink-0">
                        <div class="h-56 sm:h-64 overflow-hidden relative">
                            <img src="./assets/images/timo_card.jpg" alt="Timo" class="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-500">
                            <div class="absolute inset-0 bg-gradient-to-t from-black via-transparent to-transparent"></div>
                            <span class="absolute top-2.5 left-2.5 px-2 py-0.5 rounded-full bg-black/60 text-[10px] font-mono-code text-[#FF3823] font-bold border border-white/10">FOUNDER</span>
                        </div>
                        <div class="p-3.5">
                            <h4 class="text-sm font-bold text-white">Timo</h4>
                            <p class="text-[11px] text-neutral-400 mt-0.5">品牌创始人 · 现代爵士人</p>
                        </div>
                    </div>
                    <!-- 2. 高信博士 -->
                    <div onclick="openFacultyDrawer(4)" class="w-48 sm:w-56 rounded-2xl overflow-hidden bg-neutral-900 border border-white/10 hover:border-[#FF3823] transition-all cursor-pointer group shrink-0">
                        <div class="h-56 sm:h-64 overflow-hidden relative">
                            <img src="./assets/images/gao_xin_card.jpg" alt="高信博士" class="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-500">
                            <div class="absolute inset-0 bg-gradient-to-t from-black via-transparent to-transparent"></div>
                            <span class="absolute top-2.5 left-2.5 px-2 py-0.5 rounded-full bg-black/60 text-[10px] font-mono-code text-neutral-300 font-bold border border-white/10">PH.D</span>
                        </div>
                        <div class="p-3.5">
                            <h4 class="text-sm font-bold text-white">高信博士</h4>
                            <p class="text-[11px] text-neutral-400 mt-0.5">管乐博士 · 升学学术总监</p>
                        </div>
                    </div>
                    <!-- 3. Joe Longardner -->
                    <div onclick="openFacultyDrawer(1)" class="w-48 sm:w-56 rounded-2xl overflow-hidden bg-neutral-900 border border-white/10 hover:border-[#FF3823] transition-all cursor-pointer group shrink-0">
                        <div class="h-56 sm:h-64 overflow-hidden relative">
                            <img src="./assets/images/joe_longardner_card.jpg" alt="Joe Longardner" class="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-500">
                            <div class="absolute inset-0 bg-gradient-to-t from-black via-transparent to-transparent"></div>
                            <span class="absolute top-2.5 left-2.5 px-2 py-0.5 rounded-full bg-black/60 text-[10px] font-mono-code text-neutral-300 font-bold border border-white/10">SAX</span>
                        </div>
                        <div class="p-3.5">
                            <h4 class="text-sm font-bold text-white">Joe Longardner</h4>
                            <p class="text-[11px] text-neutral-400 mt-0.5">萨克斯大师 · 大乐队总监</p>
                        </div>
                    </div>
                    <!-- 4. Carlos -->
                    <div onclick="openFacultyDrawer(3)" class="w-48 sm:w-56 rounded-2xl overflow-hidden bg-neutral-900 border border-white/10 hover:border-[#FF3823] transition-all cursor-pointer group shrink-0">
                        <div class="h-56 sm:h-64 overflow-hidden relative">
                            <img src="./assets/images/carlos_card.jpg" alt="Carlos" class="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-500">
                            <div class="absolute inset-0 bg-gradient-to-t from-black via-transparent to-transparent"></div>
                            <span class="absolute top-2.5 left-2.5 px-2 py-0.5 rounded-full bg-black/60 text-[10px] font-mono-code text-neutral-300 font-bold border border-white/10">LATIN</span>
                        </div>
                        <div class="p-3.5">
                            <h4 class="text-sm font-bold text-white">Carlos</h4>
                            <p class="text-[11px] text-neutral-400 mt-0.5">拉丁爵士吉他大师</p>
                        </div>
                    </div>
                    <!-- 5. 张茜 -->
                    <div onclick="openFacultyDrawer(5)" class="w-48 sm:w-56 rounded-2xl overflow-hidden bg-neutral-900 border border-white/10 hover:border-[#FF3823] transition-all cursor-pointer group shrink-0">
                        <div class="h-56 sm:h-64 overflow-hidden relative">
                            <img src="./assets/images/zhang_qian_card.jpg" alt="张茜" class="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-500">
                            <div class="absolute inset-0 bg-gradient-to-t from-black via-transparent to-transparent"></div>
                            <span class="absolute top-2.5 left-2.5 px-2 py-0.5 rounded-full bg-black/60 text-[10px] font-mono-code text-neutral-300 font-bold border border-white/10">VOCAL</span>
                        </div>
                        <div class="p-3.5">
                            <h4 class="text-sm font-bold text-white">张茜</h4>
                            <p class="text-[11px] text-neutral-400 mt-0.5">声乐专家 · 伯克利研修</p>
                        </div>
                    </div>
                </div>

                <!-- 下排: Track B 向右流动 -->
                <div class="marquee-track-b flex gap-4 w-max">
                    <!-- 6. 段重生 -->
                    <div onclick="openFacultyDrawer(10)" class="w-48 sm:w-56 rounded-2xl overflow-hidden bg-neutral-900 border border-white/10 hover:border-[#FF3823] transition-all cursor-pointer group shrink-0">
                        <div class="h-56 sm:h-64 overflow-hidden relative">
                            <img src="./assets/images/duan_chongsheng_card.jpg" alt="段重生" class="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-500">
                            <div class="absolute inset-0 bg-gradient-to-t from-black via-transparent to-transparent"></div>
                            <span class="absolute top-2.5 left-2.5 px-2 py-0.5 rounded-full bg-[#FF3823]/80 text-[10px] font-mono-code text-white font-bold border border-white/10">MMus</span>
                        </div>
                        <div class="p-3.5">
                            <h4 class="text-sm font-bold text-white">段重生 (David)</h4>
                            <p class="text-[11px] text-neutral-400 mt-0.5">南安普顿硕士优等 · 盲人作曲家</p>
                        </div>
                    </div>
                    <!-- 7. 毛维 -->
                    <div onclick="openFacultyDrawer(6)" class="w-48 sm:w-56 rounded-2xl overflow-hidden bg-neutral-900 border border-white/10 hover:border-[#FF3823] transition-all cursor-pointer group shrink-0">
                        <div class="h-56 sm:h-64 overflow-hidden relative">
                            <img src="./assets/images/mao_wei_card.jpg" alt="毛维" class="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-500">
                            <div class="absolute inset-0 bg-gradient-to-t from-black via-transparent to-transparent"></div>
                            <span class="absolute top-2.5 left-2.5 px-2 py-0.5 rounded-full bg-black/60 text-[10px] font-mono-code text-neutral-300 font-bold border border-white/10">DRUMS</span>
                        </div>
                        <div class="p-3.5">
                            <h4 class="text-sm font-bold text-white">毛维</h4>
                            <p class="text-[11px] text-neutral-400 mt-0.5">爵士鼓大师 · 律动核心</p>
                        </div>
                    </div>
                    <!-- 8. 乔晓记 -->
                    <div onclick="openFacultyDrawer(2)" class="w-48 sm:w-56 rounded-2xl overflow-hidden bg-neutral-900 border border-white/10 hover:border-[#FF3823] transition-all cursor-pointer group shrink-0">
                        <div class="h-56 sm:h-64 overflow-hidden relative">
                            <img src="./assets/images/qiao_xiaoji_card.jpg" alt="乔晓记" class="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-500">
                            <div class="absolute inset-0 bg-gradient-to-t from-black via-transparent to-transparent"></div>
                            <span class="absolute top-2.5 left-2.5 px-2 py-0.5 rounded-full bg-black/60 text-[10px] font-mono-code text-neutral-300 font-bold border border-white/10">BASS</span>
                        </div>
                        <div class="p-3.5">
                            <h4 class="text-sm font-bold text-white">乔晓记</h4>
                            <p class="text-[11px] text-neutral-400 mt-0.5">克拉科夫海归 · 原声贝斯</p>
                        </div>
                    </div>
                    <!-- 9. 王崇恩 -->
                    <div onclick="openFacultyDrawer(8)" class="w-48 sm:w-56 rounded-2xl overflow-hidden bg-neutral-900 border border-white/10 hover:border-[#FF3823] transition-all cursor-pointer group shrink-0">
                        <div class="h-56 sm:h-64 overflow-hidden relative">
                            <img src="./assets/images/wang_chongen_card.jpg" alt="王崇恩" class="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-500">
                            <div class="absolute inset-0 bg-gradient-to-t from-black via-transparent to-transparent"></div>
                            <span class="absolute top-2.5 left-2.5 px-2 py-0.5 rounded-full bg-black/60 text-[10px] font-mono-code text-neutral-300 font-bold border border-white/10">GUITAR</span>
                        </div>
                        <div class="p-3.5">
                            <h4 class="text-sm font-bold text-white">王崇恩</h4>
                            <p class="text-[11px] text-neutral-400 mt-0.5">巡演吉他手 · 音色极客</p>
                        </div>
                    </div>
                    <!-- 10. 祁子垚 -->
                    <div onclick="openFacultyDrawer(9)" class="w-48 sm:w-56 rounded-2xl overflow-hidden bg-neutral-900 border border-white/10 hover:border-[#FF3823] transition-all cursor-pointer group shrink-0">
                        <div class="h-56 sm:h-64 overflow-hidden relative">
                            <img src="./assets/images/qi_ziyao_card.jpg" alt="祁子垚" class="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-500">
                            <div class="absolute inset-0 bg-gradient-to-t from-black via-transparent to-transparent"></div>
                            <span class="absolute top-2.5 left-2.5 px-2 py-0.5 rounded-full bg-black/60 text-[10px] font-mono-code text-neutral-300 font-bold border border-white/10">PRODUCER</span>
                        </div>
                        <div class="p-3.5">
                            <h4 class="text-sm font-bold text-white">祁子垚</h4>
                            <p class="text-[11px] text-neutral-400 mt-0.5">制作人 · 录音棚声学总监</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ==================== 04. 6 大专页 Bento 瓷砖：大标题 · 真实展示 · 极度接地气 ==================== -->
        <section class="space-y-6">
            <div class="border-b border-white/[0.08] pb-4">
                <span class="text-[10px] font-mono-code uppercase tracking-[0.25em] text-[#FF3823] font-bold">// ECOSYSTEM TILES</span>
                <h2 class="text-2xl sm:text-3xl font-extrabold tracking-tight text-white mt-1">探索 MOMO 音乐世界</h2>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <!-- 瓷砖 1: 大乐队与 4师1生 -->
                <a href="./ensemble-lab.html" class="spotlight-card rounded-3xl p-6 flex flex-col justify-between h-[300px] relative overflow-hidden group border border-white/10 bg-[#0d0e12]">
                    <img src="./assets/images/real_ensemble_rehearsal.jpg" alt="Ensemble" class="absolute inset-0 w-full h-full object-cover opacity-30 group-hover:scale-105 group-hover:opacity-45 transition-all duration-700">
                    <div class="absolute inset-0 bg-gradient-to-t from-black via-black/40 to-transparent"></div>
                    <div class="relative z-10">
                        <span class="text-[10px] font-mono-code uppercase tracking-[0.2em] text-[#FF3823] font-bold">ENSEMBLE LAB</span>
                        <h3 class="text-xl sm:text-2xl font-bold text-white mt-1">4师1生 真实乐队合奏</h3>
                        <p class="text-xs text-neutral-300 mt-1.5 line-clamp-2">四位真正音乐家围着你合奏，告别罐头伴奏带。</p>
                    </div>
                    <div class="relative z-10 flex items-center justify-between text-xs font-bold text-white group-hover:text-[#FF3823] transition-colors">
                        <span>探索合奏实验室</span>
                        <span>&rarr;</span>
                    </div>
                </a>

                <!-- 瓷砖 2: 音乐留学与升学 -->
                <a href="./study-abroad.html" class="spotlight-card rounded-3xl p-6 flex flex-col justify-between h-[300px] relative overflow-hidden group border border-white/10 bg-[#0d0e12]">
                    <img src="./assets/images/study_abroad_hero.jpg" alt="Study Abroad" class="absolute inset-0 w-full h-full object-cover opacity-30 group-hover:scale-105 group-hover:opacity-45 transition-all duration-700">
                    <div class="absolute inset-0 bg-gradient-to-t from-black via-black/40 to-transparent"></div>
                    <div class="relative z-10">
                        <span class="text-[10px] font-mono-code uppercase tracking-[0.2em] text-[#FF3823] font-bold">ACADEMIC &amp; CONSERVATORY</span>
                        <h3 class="text-xl sm:text-2xl font-bold text-white mt-1">音乐名校升学专案</h3>
                        <p class="text-xs text-neutral-300 mt-1.5 line-clamp-2">高信博士领衔 · 德奥免学费公立 / 伯克利作品集实录。</p>
                    </div>
                    <div class="relative z-10 flex items-center justify-between text-xs font-bold text-white group-hover:text-[#FF3823] transition-colors">
                        <span>查阅升学战绩</span>
                        <span>&rarr;</span>
                    </div>
                </a>

                <!-- 瓷砖 3: 共享空间 -->
                <a href="./spaces.html" class="spotlight-card rounded-3xl p-6 flex flex-col justify-between h-[300px] relative overflow-hidden group border border-white/10 bg-[#0d0e12]">
                    <img src="./assets/images/tongzilin_real.jpg" alt="Spaces" class="absolute inset-0 w-full h-full object-cover opacity-30 group-hover:scale-105 group-hover:opacity-45 transition-all duration-700">
                    <div class="absolute inset-0 bg-gradient-to-t from-black via-black/40 to-transparent"></div>
                    <div class="relative z-10">
                        <span class="text-[10px] font-mono-code uppercase tracking-[0.2em] text-[#FF3823] font-bold">STUDIOS &amp; SPACES</span>
                        <h3 class="text-xl sm:text-2xl font-bold text-white mt-1">桐梓林与麓湖双空间</h3>
                        <p class="text-xs text-neutral-300 mt-1.5 line-clamp-2">排练室 80-200¥/h · 60㎡ 花园与自然水岸声场。</p>
                    </div>
                    <div class="relative z-10 flex items-center justify-between text-xs font-bold text-white group-hover:text-[#FF3823] transition-colors">
                        <span>预约空间使用</span>
                        <span>&rarr;</span>
                    </div>
                </a>

                <!-- 瓷砖 4: 大凉山音乐支教公益 -->
                <a href="./charity.html" class="spotlight-card rounded-3xl p-6 flex flex-col justify-between h-[300px] relative overflow-hidden group border border-white/10 bg-[#0d0e12]">
                    <img src="./assets/images/daliangshan_singing.jpg" alt="Charity" class="absolute inset-0 w-full h-full object-cover opacity-30 group-hover:scale-105 group-hover:opacity-45 transition-all duration-700">
                    <div class="absolute inset-0 bg-gradient-to-t from-black via-black/40 to-transparent"></div>
                    <div class="relative z-10">
                        <span class="text-[10px] font-mono-code uppercase tracking-[0.2em] text-[#FF3823] font-bold">CHARITY &amp; HOPE</span>
                        <h3 class="text-xl sm:text-2xl font-bold text-white mt-1">大凉山音乐支教公益</h3>
                        <p class="text-xs text-neutral-300 mt-1.5 line-clamp-2">常态支教与乐器采购 · 守护大山深处真实歌声。</p>
                    </div>
                    <div class="relative z-10 flex items-center justify-between text-xs font-bold text-white group-hover:text-[#FF3823] transition-colors">
                        <span>了解公益纪实</span>
                        <span>&rarr;</span>
                    </div>
                </a>

                <!-- 瓷砖 5: 通识学习与九大专业学科 -->
                <a href="./curriculum.html" class="spotlight-card rounded-3xl p-6 flex flex-col justify-between h-[300px] relative overflow-hidden group border border-white/10 bg-[#0d0e12]">
                    <img src="./assets/images/handwritten_score.jpg" alt="Curriculum" class="absolute inset-0 w-full h-full object-cover opacity-30 group-hover:scale-105 group-hover:opacity-45 transition-all duration-700">
                    <div class="absolute inset-0 bg-gradient-to-t from-black via-black/40 to-transparent"></div>
                    <div class="relative z-10">
                        <span class="text-[10px] font-mono-code uppercase tracking-[0.2em] text-[#FF3823] font-bold">CURRICULUM MATRIX</span>
                        <h3 class="text-xl sm:text-2xl font-bold text-white mt-1">通识学习与专业学科</h3>
                        <p class="text-xs text-neutral-300 mt-1.5 line-clamp-2">3-7岁通识启蒙 · 吉他/贝斯/管乐/打击乐专业选修。</p>
                    </div>
                    <div class="relative z-10 flex items-center justify-between text-xs font-bold text-white group-hover:text-[#FF3823] transition-colors">
                        <span>查阅完整课程库</span>
                        <span>&rarr;</span>
                    </div>
                </a>

                <!-- 瓷砖 6: 音乐周边美学商店 -->
                <a href="./store/index.html" class="spotlight-card rounded-3xl p-6 flex flex-col justify-between h-[300px] relative overflow-hidden group border border-white/10 bg-[#0d0e12]">
                    <img src="./assets/images/merch_vinyl.jpg" alt="Store" class="absolute inset-0 w-full h-full object-cover opacity-30 group-hover:scale-105 group-hover:opacity-45 transition-all duration-700">
                    <div class="absolute inset-0 bg-gradient-to-t from-black via-black/40 to-transparent"></div>
                    <div class="relative z-10">
                        <span class="text-[10px] font-mono-code uppercase tracking-[0.2em] text-[#FF3823] font-bold">MERCH STORE</span>
                        <h3 class="text-xl sm:text-2xl font-bold text-white mt-1">MOMO 音乐周边商店</h3>
                        <p class="text-xs text-neutral-300 mt-1.5 line-clamp-2">重磅文化衫 · 专业拔片 · 黑胶帆布包 · 利润支持公益。</p>
                    </div>
                    <div class="relative z-10 flex items-center justify-between text-xs font-bold text-white group-hover:text-[#FF3823] transition-colors">
                        <span>进入商店选购</span>
                        <span>&rarr;</span>
                    </div>
                </a>
            </div>
        </section>

        <!-- ==================== 05. 奉献板块：极度简化为双栏纯粹基金卡片（去除非必要设备细节） ==================== -->
        <section class="space-y-6">
            <div class="text-center max-w-2xl mx-auto space-y-2">
                <span class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#FF3823]/10 border border-[#FF3823]/30 text-xs font-mono-code font-bold text-[#FF3823] uppercase tracking-widest">
                    <span class="w-1.5 h-1.5 rounded-full bg-[#FF3823] animate-pulse"></span>
                    MOMO PATRONAGE · 声音火种守护
                </span>
                <h2 class="text-3xl sm:text-4xl font-black text-white tracking-tight">
                    守护纯粹音乐，与我们同行
                </h2>
                <p class="text-xs sm:text-sm text-neutral-400 leading-relaxed font-light">
                    MOMO 是一个扎根教育与共创的非资本化声场。每一份奉献都 100% 透明用于教学器材添置与热爱学子奖学金。
                </p>
            </div>

            <!-- 仅保留两个纯粹大气的基金卡片 -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 items-stretch max-w-5xl mx-auto">
                <!-- 卡片 1: 教学设备器材基金 -->
                <div class="spotlight-card rounded-3xl p-8 sm:p-10 flex flex-col justify-between border border-white/10 bg-[#0d0e12] relative group">
                    <div class="absolute -top-24 -right-24 w-60 h-60 bg-[#FF3823]/10 rounded-full blur-3xl pointer-events-none"></div>
                    <div>
                        <div class="flex items-center justify-between pb-3 border-b border-white/10">
                            <span class="text-[10px] font-mono-code uppercase tracking-[0.2em] text-[#FF3823] font-bold">01 · EQUIPMENT FUND</span>
                            <span class="px-2 py-0.5 rounded-full bg-white/[0.06] text-[10px] text-neutral-400">持续共建</span>
                        </div>
                        <h3 class="text-2xl sm:text-3xl font-black text-white mt-4 tracking-tight">
                            教学设备器材基金
                        </h3>
                        <p class="text-xs sm:text-sm text-neutral-300 mt-2.5 leading-relaxed">
                            为在 MOMO 研习的孩子与乐队添置专业旗舰舞台电钢、返听监听音箱、专业耳返与高品质录音器材，给学子提供世界一流的声场条件。
                        </p>
                        <div class="mt-4 p-3 rounded-2xl bg-white/[0.03] border border-white/[0.06] text-[11px] text-neutral-400 space-y-1 font-mono-code">
                            <div>• 支持小额随喜 (¥100 / ¥200) 或任意金额全额认领</div>
                            <div>• 款项定向注入乐器与声场器材采购</div>
                        </div>
                    </div>
                    <div class="pt-6 mt-6 border-t border-white/10">
                        <button
                            type="button"
                            onclick="openGivingModal('我要支持教学设备器材基金', 'equipment')"
                            class="w-full py-3.5 rounded-full bg-[#FF3823] hover:bg-[#E02E24] text-white font-bold text-xs sm:text-sm transition-all shadow-[0_0_20px_rgba(255,56,35,0.35)] flex items-center justify-center gap-2 cursor-pointer"
                        >
                            <span>💖 我要支持设备基金</span>
                            <span>&rarr;</span>
                        </button>
                    </div>
                </div>

                <!-- 卡片 2: 音乐学者奖助学金 -->
                <div class="spotlight-card rounded-3xl p-8 sm:p-10 flex flex-col justify-between border border-white/10 bg-[#0d0e12] relative group">
                    <div class="absolute -top-24 -right-24 w-60 h-60 bg-amber-500/10 rounded-full blur-3xl pointer-events-none"></div>
                    <div>
                        <div class="flex items-center justify-between pb-3 border-b border-white/10">
                            <span class="text-[10px] font-mono-code uppercase tracking-[0.2em] text-amber-400 font-bold">02 · SCHOLARSHIP FUND</span>
                            <span class="px-2 py-0.5 rounded-full bg-white/[0.06] text-[10px] text-neutral-400">生命托举</span>
                        </div>
                        <h3 class="text-2xl sm:text-3xl font-black text-white mt-4 tracking-tight">
                            音乐学者奖助学金
                        </h3>
                        <p class="text-xs sm:text-sm text-neutral-300 mt-2.5 leading-relaxed">
                            为真正热爱音乐但有经济压力的家庭学子减免年费，并专项扶持视障学子与举办公益公开课，让更多有才华的音乐学子不因境遇而止步。
                        </p>
                        <div class="mt-4 p-3 rounded-2xl bg-white/[0.03] border border-white/[0.06] text-[11px] text-neutral-400 space-y-1 font-mono-code">
                            <div>• 支持全额/半额奖助学金及社区大师课专项</div>
                            <div>• 善款直达学子学费扶持与公开艺术课场地支持</div>
                        </div>
                    </div>
                    <div class="pt-6 mt-6 border-t border-white/10">
                        <button
                            type="button"
                            onclick="openGivingModal('资助音乐学者奖助学金', 'scholarship')"
                            class="w-full py-3.5 rounded-full bg-white/10 hover:bg-[#FF3823] hover:text-white border border-white/20 text-white font-bold text-xs sm:text-sm transition-all flex items-center justify-center gap-2 cursor-pointer"
                        >
                            <span>🎓 资助学者奖学金</span>
                            <span>&rarr;</span>
                        </button>
                    </div>
                </div>
            </div>

            <!-- 极简透明历史支持者名单轮播 -->
            <div class="max-w-3xl mx-auto p-4 rounded-2xl bg-black/60 border border-white/10 text-center">
                <div class="text-[11px] font-mono-code text-[#FF3823] font-bold mb-2">★ 感谢每一位同行者 · 历史支持芳名录</div>
                <div class="flex flex-wrap items-center justify-center gap-2 sm:gap-4 text-xs text-neutral-300 font-mono-code">
                    <span class="px-2.5 py-1 rounded-lg bg-white/[0.04] border border-white/10">林先生 ¥2,000 (设备)</span>
                    <span class="px-2.5 py-1 rounded-lg bg-white/[0.04] border border-white/10">MOMO 会员家庭 ¥1,000 (奖学金)</span>
                    <span class="px-2.5 py-1 rounded-lg bg-white/[0.04] border border-white/10">匿名伙伴 ¥500 (设备)</span>
                    <span class="px-2.5 py-1 rounded-lg bg-white/[0.04] border border-white/10">陈女士 ¥200 (支教乐器)</span>
                    <span class="px-2.5 py-1 rounded-lg bg-white/[0.04] border border-white/10">张同学 ¥100 (白板笔耗材)</span>
                </div>
            </div>
        </section>

        <!-- ==================== 06. 创始人直通微信通道：真实扫码 · 绝不冗长 ==================== -->
        <section class="space-y-6">
            <div class="spotlight-card rounded-3xl p-8 sm:p-12 border border-[#FF3823]/30 bg-gradient-to-b from-[#140b0b] via-[#0d0909] to-[#080808] relative overflow-hidden shadow-2xl">
                <div class="absolute -top-32 -right-32 w-80 h-80 bg-[#FF3823]/10 rounded-full blur-3xl pointer-events-none"></div>
                <div class="max-w-4xl mx-auto flex flex-col md:flex-row items-center justify-between gap-8 relative z-10">
                    <div class="space-y-3 text-center md:text-left">
                        <span class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#FF3823]/15 border border-[#FF3823]/40 text-xs font-mono-code font-bold text-[#FF3823]">
                            <span class="w-1.5 h-1.5 rounded-full bg-[#FF3823] animate-pulse"></span>
                            FOUNDER DIRECT CHANNEL
                        </span>
                        <h2 class="text-2xl sm:text-4xl font-black text-white tracking-tight">
                            直接添加主理人 Timo 微信
                        </h2>
                        <p class="text-xs sm:text-sm text-neutral-300 max-w-lg leading-relaxed">
                            我是 Timo。无论是为家庭咨询音乐通识教育、预约 4 师 1 生试奏，还是商讨海外名校留学作品集或空间探访，随时微信聊聊。
                        </p>
                        <div class="pt-2 flex flex-wrap items-center justify-center md:justify-start gap-4 text-xs font-mono-code text-neutral-400">
                            <div>• 微信号：tixinzhang</div>
                            <div>• 邮箱：tixinzhang@gmail.com</div>
                        </div>
                    </div>

                    <!-- 真实二维码立牌 -->
                    <div class="shrink-0 text-center">
                        <div class="w-44 p-3 bg-white rounded-2xl shadow-2xl shadow-[#FF3823]/20 mx-auto transform hover:scale-105 transition-transform duration-300">
                            <img src="./assets/images/contact/timo_wechat_qr.png" alt="Timo 微信二维码" class="w-full aspect-square object-contain rounded-lg">
                            <div class="mt-2 text-[11px] font-bold text-black tracking-tight">
                                Timo · 主理人微信
                            </div>
                        </div>
                        <p class="text-[10px] text-neutral-500 font-mono-code mt-2">扫一扫或长按保存识别</p>
                    </div>
                </div>
            </div>
        </section>
    </main>
'''

index_html = (
    build_head("MOMO 音乐生活服务品牌 | 属于家庭与艺术家的真实声音场")
    + render_apple_nav("./", active="home")
    + apple_home_main
    + render_apple_footer_and_scripts("./", include_drawers=False)
)

with open(os.path.join(WEBSITE_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)


# ---------------------------------------------------------------------------
# 4. BUILD PAGE 2: curriculum.html (《通识音乐学习》 + 九大专业学科矩阵 + 风格卡片机)
# ---------------------------------------------------------------------------
curriculum_hero = '''
    <main class="pt-14 bg-black text-white">
        <!-- 课程专页顶部导览横幅 -->
        <section class="py-16 sm:py-20 px-6 md:px-12 bg-gradient-to-b from-[#0d0e14] to-[#08080a] border-b border-neutral-900 text-center">
            <div class="max-w-4xl mx-auto">
                <p class="text-xs font-mono uppercase tracking-[0.22em] text-momo-mint mb-3">
                    // MOMO CURRICULUM &amp; HOLISTIC IMMERSION
                </p>
                <h1 class="text-3xl sm:text-5xl md:text-6xl font-black tracking-tight text-white leading-tight">
                    先通识，后专业：<br>
                    <span class="gradient-text">现代流行与专业爵士教育体系</span>
                </h1>
                <p class="mt-4 text-sm sm:text-lg text-neutral-400 font-light max-w-2xl mx-auto leading-relaxed">
                    打破单一乐器枯燥死磕，先在真实声场中建立全景立体的音乐认知框架，再水到渠成选修九大现代音乐学科。
                </p>
                <!-- 页内快速锚点胶囊 -->
                <div class="mt-8 inline-flex flex-wrap items-center justify-center gap-3">
                    <a href="#general-education" class="rounded-full px-5 py-2 bg-momo-mint/15 border border-momo-mint/40 text-momo-mint text-xs font-semibold hover:bg-momo-mint hover:text-black transition-all">
                        01 · 《通识音乐学习》
                    </a>
                    <a href="#matrix" class="rounded-full px-5 py-2 bg-white/5 border border-white/15 text-white text-xs font-semibold hover:border-momo-cyan transition-all">
                        02 · 九大选修专业学科矩阵
                    </a>
                    <a href="#style-deck" class="rounded-full px-5 py-2 bg-white/5 border border-white/15 text-white text-xs font-semibold hover:border-momo-cyan transition-all">
                        03 · 音乐风格在线试听机
                    </a>
                </div>
            </div>
        </section>
'''

curriculum_html = (
    build_head("《通识音乐学习》与九大现代专业学科矩阵 | Momo 音乐生活服务品牌")
    + render_apple_nav("./", active="curriculum")
    + curriculum_hero
    + s_general_edu
    + s_matrix
    + s_style_deck
    + "\n    </main>\n"
    + render_apple_footer_and_scripts("./", include_drawers=True)
)

with open(os.path.join(WEBSITE_DIR, "curriculum.html"), "w", encoding="utf-8") as f:
    f.write(curriculum_html)


# ---------------------------------------------------------------------------
# 5. BUILD PAGE 3: faculty.html (艺术家导师智库 · 5×2 全彩大画幅矩阵 + 13位导师详情抽屉)
# ---------------------------------------------------------------------------
faculty_hero = '''
    <main class="pt-14 bg-[#080808] text-white">
        <section class="py-16 sm:py-20 px-6 md:px-12 bg-gradient-to-b from-[#0e0f14] to-[#080808] border-b border-neutral-900 text-center">
            <div class="max-w-4xl mx-auto">
                <p class="text-xs font-mono uppercase tracking-[0.22em] text-momo-cyan mb-3">
                    // MASTERCLASS ARTISTS &amp; SCHOLARS ROSTER
                </p>
                <h1 class="text-3xl sm:text-5xl md:text-6xl font-black tracking-tight text-white">
                    与真正的音乐家并肩合奏
                </h1>
                <p class="mt-4 text-sm sm:text-lg text-neutral-400 font-light max-w-2xl mx-auto leading-relaxed">
                    拒绝传统琴房流水线兼职助教。点击任意导师全彩肖像卡片，即可查阅详细学术履历、代表舞台现场，并直接预约一对一面谈或合奏席位。
                </p>
            </div>
        </section>
'''

faculty_auto_open_script = '''
<script>
    window.addEventListener('DOMContentLoaded', function() {
        const params = new URLSearchParams(window.location.search);
        const artist = params.get('artist') || (window.location.hash ? window.location.hash.replace('#', '') : '');
        if (artist && typeof facultyData !== 'undefined' && facultyData[artist]) {
            setTimeout(() => openFacultyDrawer(artist), 180);
        }
    });
</script>
'''

faculty_html = (
    build_head("一线艺术家导师智库与履历档案 | Momo 音乐生活服务品牌")
    + render_apple_nav("./", active="faculty")
    + faculty_hero
    + clean_faculty_section
    + "\n    </main>\n"
    + faculty_auto_open_script
    + render_apple_footer_and_scripts("./", include_drawers=True)
)

with open(os.path.join(WEBSITE_DIR, "faculty.html"), "w", encoding="utf-8") as f:
    f.write(faculty_html)


# ---------------------------------------------------------------------------
# 6. BUILD PAGE 4: ensemble-lab.html (青少年爵士大乐队 & 4-on-1 职业乐队实验室双轨专页)
# ---------------------------------------------------------------------------
with open(os.path.join(SUBPAGE_BAK_DIR, "ensemble-lab.html"), "r", encoding="utf-8") as f:
    orig_lab = f.read()

# Extract the <main>...</main> + handleLabBooking script from orig_lab
m_lab_main = re.search(r"<main[^>]*>(.*?)</main>", orig_lab, flags=re.DOTALL)
lab_inner_html = m_lab_main.group(1) if m_lab_main else ""

ensemble_page_body = f'''
    <main class="pt-14 bg-black text-white">
        <!-- 双旗舰合奏顶部导览 -->
        <section class="py-16 sm:py-20 px-6 md:px-12 bg-gradient-to-b from-[#0d0e14] to-black border-b border-neutral-900 text-center">
            <div class="max-w-4xl mx-auto">
                <p class="text-xs font-mono uppercase tracking-[0.22em] text-amber-300 mb-3">
                    // DUAL ENSEMBLE ENGINES · 正在火热招募与开放预约
                </p>
                <h1 class="text-3xl sm:text-5xl md:text-6xl font-black tracking-tight text-white leading-tight">
                    青少年现代爵士大乐队<br>
                    <span class="gradient-text">&amp; 4-on-1 职业乐队实验室</span>
                </h1>
                <p class="mt-4 text-sm sm:text-lg text-neutral-400 font-light max-w-2xl mx-auto">
                    告别一个人面对节拍器的孤独练琴。无论是 17 人标准爵士交响大乐队，还是 4 位职业音乐家围着你一人的真棚合奏，音乐都在现场真实发生。
                </p>
                <div class="mt-8 inline-flex flex-wrap items-center justify-center gap-3">
                    <a href="#big-band" class="rounded-full px-5 py-2 bg-amber-400/15 border border-amber-400/40 text-amber-300 text-xs font-semibold hover:bg-amber-400 hover:text-black transition-all">
                        01 · 青少年现代爵士大乐队 (正在招募)
                    </a>
                    <a href="#lab-detail" class="rounded-full px-5 py-2 bg-momo-cyan/15 border border-momo-cyan/40 text-momo-cyan text-xs font-semibold hover:bg-momo-cyan hover:text-black transition-all">
                        02 · 4-on-1 职业乐队实验室 (¥400 / 会员划扣)
                    </a>
                </div>
            </div>
        </section>

        <!-- Part 1: 青少年现代爵士大乐队 & 月度重奏总览 -->
        {s_big_band}

        <!-- Part 2: 4-on-1 职业乐队实验室深度拆解与在线预约 -->
        <section id="lab-detail" class="max-w-7xl mx-auto px-6 md:px-12 py-20">
            {lab_inner_html}
        </section>
    </main>
    <script>
        function handleLabBooking(e) {{
            e.preventDefault();
            const name = document.getElementById('lab-name').value;
            const phone = document.getElementById('lab-phone').value;
            const inst = document.getElementById('lab-instrument').value;
            if (typeof showToast === 'function') {{
                showToast('合奏预约已受理！', '主理人 Timo 与导师组将尽快联络 ' + name + '（' + phone + '）安排【' + inst + '】档期。');
            }} else {{
                alert('合奏预约已受理！主理人 Timo 与导师组将尽快联络 ' + name + '（' + phone + '）。');
            }}
        }}
    </script>
'''

ensemble_html = (
    build_head("青少年现代爵士大乐队 & 4-on-1 职业乐队实验室 | Momo 音乐生活服务品牌")
    + render_apple_nav("./", active="ensemble")
    + ensemble_page_body
    + render_apple_footer_and_scripts("./", include_drawers=False)
)

with open(os.path.join(WEBSITE_DIR, "ensemble-lab.html"), "w", encoding="utf-8") as f:
    f.write(ensemble_html)


# ---------------------------------------------------------------------------
# 7. BUILD PAGE 5: charity.html (声音火种与大凉山音乐教育支教公益 & 3天2晚共修营专页)
# ---------------------------------------------------------------------------
charity_body = f'''
    <main class="pt-14 bg-black text-white">
        <section class="py-16 sm:py-20 px-6 md:px-12 bg-gradient-to-b from-[#0c1210] to-black border-b border-neutral-900 text-center">
            <div class="max-w-4xl mx-auto">
                <p class="text-xs font-mono uppercase tracking-[0.22em] text-momo-mint mb-3">
                    // SOUND OF HOPE · DALIANGSHAN MUSIC CHARITY
                </p>
                <h1 class="text-3xl sm:text-5xl md:text-6xl font-black tracking-tight text-white leading-tight">
                    声音火种与大凉山音乐支教
                </h1>
                <p class="mt-4 text-sm sm:text-lg text-neutral-400 font-light max-w-2xl mx-auto leading-relaxed">
                    用真实的音乐技能服务他人，在付出与合奏中收获生命成长。Momo 音乐美学商店所有周边净收益全额定向注入青少年合奏基金与大凉山乡村音乐教室。
                </p>
            </div>
        </section>

        <!-- 声音火种与支教全景纪实 -->
        {s_giving}

        <!-- 3天2晚 大凉山音乐公益共修营 深度专案 -->
        <section id="retreat" class="py-24 px-6 md:px-12 bg-[#070709] border-t border-neutral-900">
            <div class="max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
                <div class="lg:col-span-6 rounded-2xl overflow-hidden border border-white/10 shadow-2xl">
                    <img src="./assets/images/daliangshan_charity_4k.jpg" alt="大凉山 3天2晚 音乐公益共修营" class="w-full h-full object-cover">
                </div>
                <div class="lg:col-span-6 space-y-5">
                    <span class="inline-block px-3 py-1 rounded-full bg-momo-mint/15 border border-momo-mint/40 text-momo-mint text-xs font-mono font-bold">
                        ¥4,000 / 人 · 满 3–4 人即成团出发 · 会员家庭优先
                    </span>
                    <h2 class="text-3xl sm:text-4xl font-black text-white tracking-tight">
                        大凉山 3天2晚 音乐公益共修营
                    </h2>
                    <p class="text-sm text-neutral-300 leading-relaxed">
                        由品牌创始人 Timo 与艺术家导师亲自带队，带着家人与乐器深入大凉山乡村小学。在松林与阳光下，与当地孩子们围坐在一起弹吉他、打非洲鼓、合唱歌谣——不是居高临下的施予，而是生命与生命之间最真诚的看见与合奏。
                    </p>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-2 text-xs text-neutral-300 font-mono">
                        <div class="p-3.5 rounded-xl bg-neutral-950 border border-neutral-800">✦ 含全程领队协调与在地食宿交通统筹</div>
                        <div class="p-3.5 rounded-xl bg-neutral-950 border border-neutral-800">✦ 含捐赠给山区学校的随行尤克里里/打击乐</div>
                        <div class="p-3.5 rounded-xl bg-neutral-950 border border-neutral-800">✦ 行前 Momo 空间公益曲目排练准备</div>
                        <div class="p-3.5 rounded-xl bg-neutral-950 border border-neutral-800">✦ 真实支教影像纪录与社会实践证明</div>
                    </div>
                    <div class="pt-4 flex flex-wrap gap-4">
                        <button type="button" onclick="openBookingModal('申请报名：大凉山 3天2晚 音乐公益共修营 (¥4,000/人)')" class="rounded-full gradient-bg text-black px-8 py-3.5 text-xs font-black uppercase tracking-wider hover:brightness-110 transition-all cursor-pointer">
                            申请同行席位 / 咨询近期出团排期 &rarr;
                        </button>
                        <a href="./store/index.html" class="rounded-full border border-neutral-700 hover:border-momo-mint text-neutral-300 hover:text-white px-6 py-3.5 text-xs font-mono transition-all">
                            选购公益周边支持山区教室 &rsaquo;
                        </a>
                    </div>
                </div>
            </div>
        </section>
    </main>
'''

charity_html = (
    build_head("声音火种与大凉山音乐教育支教公益 | Momo 音乐生活服务品牌")
    + render_apple_nav("./", active="charity")
    + charity_body
    + render_apple_footer_and_scripts("./", include_drawers=False)
)

with open(os.path.join(WEBSITE_DIR, "charity.html"), "w", encoding="utf-8") as f:
    f.write(charity_html)


# ---------------------------------------------------------------------------
# 8. UPGRADE PAGE 6: study-abroad.html (高信博士真实肖像与舞台照 + 24轨实录视频 + 统一导航)
# ---------------------------------------------------------------------------
with open(os.path.join(SUBPAGE_BAK_DIR, "study-abroad.html"), "r", encoding="utf-8") as f:
    orig_study = f.read()

m_study_main = re.search(r"(<main[^>]*>.*?</main>)", orig_study, flags=re.DOTALL)
study_main_html = m_study_main.group(1) if m_study_main else ""

# Upgrade hero visual in study-abroad.html to feature Dr. Gao Xin's authentic cover & stage live photos + portfolio video
old_study_right = '''            <div class="lg:col-span-5">
                <div class="aspect-[4/3] brutalist-border bg-neutral-950 overflow-hidden relative">
                    <img src="./assets/images/conservatory_mentorship_hero.jpg" alt="Conservatory Prep" class="w-full h-full object-cover">
                </div>
                <div class="text-[11px] font-mono text-neutral-500 mt-3 text-center">
                    // P&amp;R STUDIO 24-TRACK RECORDING FACILITY · 录音棚同期实录作品集
                </div>
            </div>'''

new_study_right = '''            <div class="lg:col-span-5 space-y-4">
                <div class="aspect-[4/5] max-h-[420px] mx-auto rounded-2xl brutalist-border bg-neutral-950 overflow-hidden relative">
                    <img src="./assets/images/gao_xin_card.jpg" alt="高信博士 Dr. Gao Xin" class="w-full h-full object-cover object-top">
                    <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-transparent to-transparent"></div>
                    <div class="absolute bottom-4 left-4 right-4">
                        <div class="text-[10px] font-mono text-[#D4AF37] uppercase tracking-widest">ACADEMIC DIRECTOR · 学术总领衔</div>
                        <div class="text-lg font-black text-white">高信博士 (Dr. Gao Xin)</div>
                        <div class="text-xs text-neutral-300 mt-0.5">奥地利格拉茨国立音乐与表演艺术大学博士 · 旅欧双簧管演奏家</div>
                    </div>
                </div>
                <div class="text-center">
                    <a href="./faculty.html?artist=gaoxin" class="text-xs font-mono text-[#D4AF37] hover:underline">查阅高信博士完整学术履历与舞台档案 &rsaquo;</a>
                </div>
            </div>'''

study_portfolio_showcase = '''
        <!-- 真实 24 轨同期作品集实录现场与舞台实景 -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-20 pb-16 border-b border-neutral-900">
            <div class="space-y-3">
                <div class="text-xs font-mono text-momo-mint uppercase tracking-wider">// 欧洲音乐学院硕士申请实录案例 (24轨真乐队同期直录)</div>
                <div class="aspect-video bg-black rounded-xl overflow-hidden border border-neutral-800">
                    <video controls playsinline preload="metadata" class="w-full h-full object-cover">
                        <source src="./留学作品集/10月7日.mp4" type="video/mp4">
                    </video>
                </div>
                <p class="text-xs text-neutral-400">P&amp;R Studio 工业级 24 轨同期实录 · 零修音一次成型，满足欧美考官严苛声学审听标准。</p>
            </div>
            <div class="space-y-3">
                <div class="text-xs font-mono text-[#D4AF37] uppercase tracking-wider">// 欧洲交响与室内乐舞台视野 · 德奥公立免学费与英美名校双轨覆盖</div>
                <div class="aspect-video bg-black rounded-xl overflow-hidden border border-neutral-800">
                    <img src="./assets/images/gao_xin_stage_live.jpg" alt="高信博士欧洲舞台演出全景" class="w-full h-full object-cover">
                </div>
                <p class="text-xs text-neutral-400">直连奥地利、德国公立音乐学院及伯克利、NEC、英皇等欧美顶尖院校在职教授资源。</p>
            </div>
        </div>
'''

study_main_html = study_main_html.replace(old_study_right, new_study_right)
study_main_html = study_main_html.replace(
    "高信博士（管乐与和声学博士 · 升学首席学术顾问）",
    "高信博士（奥地利格拉茨国立音乐与表演艺术大学博士 · 旅欧双簧管演奏家 · 升学首席学术顾问）"
)
study_main_html = study_main_html.replace(
    "<!-- 交付内容 5 大板块 -->",
    study_portfolio_showcase + "\n        <!-- 交付内容 5 大板块 -->"
)
study_main_html = study_main_html.replace(
    '<main class="max-w-7xl mx-auto px-6 md:px-12 py-12">',
    '<main class="max-w-7xl mx-auto px-6 md:px-12 pt-24 pb-12">'
)

study_script = '''
    <script>
        function handleStudyForm(e) {
            e.preventDefault();
            const phone = document.getElementById('study-phone').value;
            if (typeof showToast === 'function') {
                showToast('升学评估申请已受理！', '高信博士与 Timo 主理人将在 12 小时内联络您（' + phone + '）。');
            } else {
                alert('升学评估申请已受理！高信博士与 Timo 主理人将在 12 小时内亲自联络您（' + phone + '）。');
            }
        }
    </script>
'''

study_html = (
    build_head("音乐升学与海外名校留学规划专案 (¥38,800) | 高信博士领衔 · Momo")
    + render_apple_nav("./", active="study")
    + study_main_html
    + study_script
    + render_apple_footer_and_scripts("./", include_drawers=False)
)

with open(os.path.join(WEBSITE_DIR, "study-abroad.html"), "w", encoding="utf-8") as f:
    f.write(study_html)


# ---------------------------------------------------------------------------
# 9. UPGRADE PAGE 7 & 8: membership.html & spaces.html (全局统一导航、页脚与预约弹窗)
# ---------------------------------------------------------------------------
def upgrade_existing_subpage(filename: str, active_key: str, page_title: str):
    with open(os.path.join(SUBPAGE_BAK_DIR, filename), "r", encoding="utf-8") as f:
        raw = f.read()
    m_main = re.search(r"(<main[^>]*>.*?</main>)", raw, flags=re.DOTALL)
    main_block = m_main.group(1) if m_main else ""
    main_block = main_block.replace(
        '<main class="max-w-7xl mx-auto px-6 md:px-12 py-12">',
        '<main class="max-w-7xl mx-auto px-6 md:px-12 pt-24 pb-12">'
    )
    # Replace legacy ./index.html#booking links with in-page openBookingModal
    main_block = re.sub(
        r'href="\./index\.html#booking"',
        'href="#booking" onclick="event.preventDefault(); openBookingModal(\'预约来空间喝杯咖啡 / 现场体验沟通\');"',
        main_block,
    )
    # Preserve inline <script> between </main> and <footer
    m_inline_script = re.search(r"</main>\s*(<script>.*?</script>)", raw, flags=re.DOTALL)
    inline_script = m_inline_script.group(1) if m_inline_script else ""

    out = (
        build_head(page_title)
        + render_apple_nav("./", active=active_key)
        + main_block
        + "\n"
        + inline_script
        + "\n"
        + render_apple_footer_and_scripts("./", include_drawers=False)
    )
    with open(os.path.join(WEBSITE_DIR, filename), "w", encoding="utf-8") as f:
        f.write(out)


upgrade_existing_subpage(
    "membership.html",
    "membership",
    "MOMO 家庭音乐会员 Plus (¥6,000/年) · 一人入会 全家共享",
)
upgrade_existing_subpage(
    "spaces.html",
    "spaces",
    "桐梓林 × 麓湖城市音乐共享空间与器材租用 | Momo 音乐生活服务品牌",
)


# ---------------------------------------------------------------------------
# 10. UPGRADE STORE PAGES: store/index.html, tshirt.html, tote.html, picks.html, vinyl.html
# ---------------------------------------------------------------------------
store_files = ["index.html", "tshirt.html", "tote.html", "picks.html", "vinyl.html"]
for sf in store_files:
    src_sf = os.path.join(SUBPAGE_BAK_DIR, "store", sf)
    if not os.path.exists(src_sf):
        continue
    with open(src_sf, "r", encoding="utf-8") as f:
        raw_sf = f.read()
    m_title = re.search(r"<title>(.*?)</title>", raw_sf, flags=re.DOTALL)
    sf_title = m_title.group(1).strip() if m_title else "Momo 音乐美学商店"

    m_main = re.search(r"(<main[^>]*>.*?</main>)", raw_sf, flags=re.DOTALL)
    sf_main = m_main.group(1) if m_main else ""
    sf_main = sf_main.replace(
        '<main class="max-w-7xl mx-auto px-6 md:px-12 py-12">',
        '<main class="max-w-7xl mx-auto px-6 md:px-12 pt-24 pb-12">'
    )
    sf_main = sf_main.replace(
        'href="../index.html#booking"',
        'href="#booking" onclick="event.preventDefault(); openBookingModal(\'Momo 音乐美学商店订购与咨询\');"'
    )
    m_script = re.search(r"</main>\s*(<script>.*?</script>)", raw_sf, flags=re.DOTALL)
    sf_script = m_script.group(1) if m_script else ""

    sf_out = (
        build_head(sf_title, prefix="../")
        + render_apple_nav("../", active="store")
        + sf_main
        + "\n"
        + sf_script
        + "\n"
        + render_apple_footer_and_scripts("../", include_drawers=False)
    )
    with open(os.path.join(WEBSITE_DIR, "store", sf), "w", encoding="utf-8") as f:
        f.write(sf_out)

print("SUCCESS: Apple.com Storefront index.html + All 8 Dedicated Subpages + Store Ecosystem Built!")
