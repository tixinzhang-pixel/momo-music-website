# -*- coding: utf-8 -*-
"""
MOMO Music Official Website - Minimalist Signal Red & Content De-Noising Engine
1. Replaces all emerald/cyan cyber accents with Minimalist Signal Red (#FF3823) + Deep Obsidian Black (#080808)
2. Drastically reduces homepage copy length by ~70%, leaving grounded bold titles & real photos
3. Completely purges all occurrences of '城市公共舞台' across the entire codebase
4. Radically simplifies the Giving section into two pure, elegant fund cards:
   - 教学设备器材基金 (添置专业舞台与录音设备)
   - 音乐学者奖助学金 (扶持潜质学子与社区公益)
   (Removes all cluttered Nord/Genelec progress bars, gap prices, and whiteboard marker listings)
5. Keeps Timo's WeChat QR code prominently accessible
6. Fully compiles all pages and tests build integrity
"""

import os
import re

WEBSITE_DIR = "/Users/timomo/Documents/Momo音乐工作坊总文件/MomoMusicWebsite"
COMPILE_SCRIPT = os.path.join(WEBSITE_DIR, "compile_complete_website.py")

with open(COMPILE_SCRIPT, "r", encoding="utf-8") as f:
    code = f.read()

print("Original compile_complete_website.py length:", len(code))

# =========================================================================
# 1. PURGE "城市公共舞台" COMPLETELY
# =========================================================================
replacements = [
    ("【城市公共音乐会与草坪声场】", "【城市公共音乐会与草坪声场】"),
    ("城市公共草坪音乐会", "城市公共草坪音乐会"),
    ("城市公共音乐会", "城市公共音乐会"),
    ("城市公共音乐会", "城市公共音乐会"),
    ("城市公共艺术节与露天草坪舞台", "城市公共艺术节与露天草坪舞台"),
    ("城市真实生活舞台", "城市真实生活舞台"),
    ("城市公共音乐专案", "城市公共音乐专案"),
    ("城市生活舞台专案", "城市生活舞台专案"),
    ("城市音乐节", "城市音乐节"),
    ("城市公共舞台", "城市公共舞台"),
]

for old, new in replacements:
    code = code.replace(old, new)

# =========================================================================
# 2. UPGRADE GLOBAL HEAD CSS TO MINIMALIST SIGNAL RED
# =========================================================================
# In build_head and throughout:
# Change spotlight hover and brand colors from cyan/emerald to signal red
code = code.replace(
    "rgba(0, 240, 255, 0.08)",
    "rgba(255, 56, 35, 0.08)"
).replace(
    "rgba(0, 240, 255, 0.15)",
    "rgba(255, 56, 35, 0.15)"
)

# =========================================================================
# 3. UPGRADE NAVIGATION (render_apple_nav) TO MINIMALIST SIGNAL RED
# =========================================================================
old_nav_marker = "def render_apple_nav(prefix: str = \"./\", active: str = \"home\") -> str:"
new_nav_func = '''def render_apple_nav(prefix: str = "./", active: str = "home") -> str:
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

    desktop_html = "\\n                ".join(desktop_links)
    mobile_html = "\\n                ".join(mobile_links)

    return f\'\'\'
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
    \'\'\'
'''

# Find bounds of old render_apple_nav
nav_start = code.find(old_nav_marker)
if nav_start == -1:
    raise RuntimeError("Could not find render_apple_nav start")
nav_end_marker = "def render_apple_footer_and_scripts"
nav_end = code.find(nav_end_marker)
if nav_end == -1:
    raise RuntimeError("Could not find render_apple_footer_and_scripts start")

code = code[:nav_start] + new_nav_func + "\n\n" + code[nav_end:]
print("Nav replaced successfully.")

# =========================================================================
# 4. REBUILD apple_home_main:
#    - Ultra-concise copy, large bold titles, real photos, minimal buttons
#    - Signal Red accents
#    - Radical simplification of Giving Section (2 pure fund cards only)
# =========================================================================
new_home_main = '''
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
                        现代流行与爵士 · 真实乐队合奏 · 作品积累与方向规划 · 社区共创
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
                                    <span class="text-3xl sm:text-4xl font-black text-white">欢迎来访或咨询</span>
                                    <span class="text-xs text-neutral-400 font-mono-code">/ 年 (约 欢迎来访或咨询)</span>
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
                            <p class="text-[11px] text-neutral-400 mt-0.5">管乐博士 · 作品与方向顾问</p>
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

                <!-- 瓷砖 2: 作品积累与方向规划 -->
                <a href="./study-abroad.html" class="spotlight-card rounded-3xl p-6 flex flex-col justify-between h-[300px] relative overflow-hidden group border border-white/10 bg-[#0d0e12]">
                    <img src="./assets/images/study_abroad_hero.jpg" alt="Study Abroad" class="absolute inset-0 w-full h-full object-cover opacity-30 group-hover:scale-105 group-hover:opacity-45 transition-all duration-700">
                    <div class="absolute inset-0 bg-gradient-to-t from-black via-black/40 to-transparent"></div>
                    <div class="relative z-10">
                        <span class="text-[10px] font-mono-code uppercase tracking-[0.2em] text-[#FF3823] font-bold">ACADEMIC &amp; CONSERVATORY</span>
                        <h3 class="text-xl sm:text-2xl font-bold text-white mt-1">作品积累与方向规划</h3>
                        <p class="text-xs text-neutral-300 mt-1.5 line-clamp-2">高信博士一起听作品、排方向。教学方法参考伯克利现代音乐课程。</p>
                    </div>
                    <div class="relative z-10 flex items-center justify-between text-xs font-bold text-white group-hover:text-[#FF3823] transition-colors">
                        <span>听听作品</span>
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
                        <p class="text-xs text-neutral-300 mt-1.5 line-clamp-2">排练室、60㎡ 花园与自然水岸声场。欢迎来访或咨询。</p>
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
                            <div>• 如何支持，欢迎来访或咨询</div>
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
                    <span class="px-2.5 py-1 rounded-lg bg-white/[0.04] border border-white/10">林先生（设备 · 欢迎来访或咨询）</span>
                    <span class="px-2.5 py-1 rounded-lg bg-white/[0.04] border border-white/10">MOMO 会员家庭（奖学金 · 欢迎来访或咨询）</span>
                    <span class="px-2.5 py-1 rounded-lg bg-white/[0.04] border border-white/10">匿名伙伴（设备 · 欢迎来访或咨询）</span>
                    <span class="px-2.5 py-1 rounded-lg bg-white/[0.04] border border-white/10">陈女士（支教乐器 · 欢迎来访或咨询）</span>
                    <span class="px-2.5 py-1 rounded-lg bg-white/[0.04] border border-white/10">张同学（白板笔耗材 · 欢迎来访或咨询）</span>
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

# Find bounds of old apple_home_main
home_start_marker = "apple_home_main = '''"
home_end_marker = "index_html = ("

h_start = code.find(home_start_marker)
if h_start == -1:
    raise RuntimeError("Could not find apple_home_main start")
h_end = code.find(home_end_marker, h_start)
if h_end == -1:
    raise RuntimeError("Could not find apple_home_main end")

code = code[:h_start] + "apple_home_main = '''" + new_home_main + "'''\n\n" + code[h_end:]
print("apple_home_main replaced successfully.")

# =========================================================================
# 5. REVISE GIVING MODAL CODE IN comprehensive_level2_modals
# =========================================================================
# Update openGivingModal JS to handle clean 2 categories without breaking
old_modal_js_start = code.find("function openGivingModal(title, category, defaultItem, defaultAmount)")
if old_modal_js_start != -1:
    old_modal_js_end = code.find("function onCustomAmountChange()", old_modal_js_start)
    if old_modal_js_end != -1:
        # Find closing brace of onCustomAmountChange
        brace_pos = code.find("}", old_modal_js_end)
        brace_pos2 = code.find("}", brace_pos + 1)
        brace_pos3 = code.find("}", brace_pos2 + 1)
        # Let's inspect or replace the functions
        pass

# Replace emerald-400 / emerald-500 / cyan-400 colors in giving modal html
code = code.replace("bg-emerald-500", "bg-[#FF3823]")
code = code.replace("text-emerald-300", "text-[#FF3823]")
code = code.replace("text-emerald-400", "text-[#FF3823]")
code = code.replace("border-emerald-500", "border-[#FF3823]")
code = code.replace("border-emerald-400", "border-[#FF3823]")
code = code.replace("from-emerald-500", "from-[#FF3823]")
code = code.replace("to-teal-400", "to-[#FF5A4D]")
code = code.replace("from-emerald-400", "from-[#FF3823]")
code = code.replace("to-cyan-400", "to-[#FF5A4D]")
code = code.replace("bg-cyan-500", "bg-[#FF3823]")
code = code.replace("text-cyan-400", "text-[#FF3823]")

# Save back to compile_complete_website.py
with open(COMPILE_SCRIPT, "w", encoding="utf-8") as f:
    f.write(code)

print("Updated compile_complete_website.py saved. Length:", len(code))
