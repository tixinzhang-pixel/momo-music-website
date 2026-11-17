# -*- coding: utf-8 -*-
"""
Apply User Enhancements:
1. Restore faculty matrix infinite horizontal auto-scrolling (fix CSS class mismatch & clone tracks for seamless marquee)
2. Restore the full interactive Music Style Deck (s_style_deck with audio stream player & card switching) to replace the 4-pad chord box
3. Make the 6000 RMB Membership Section prominent, elegant, full-width, highlighting the physical member card with generous whitespace (no crowding)
"""

import os
import re

WEBSITE_DIR = "/Users/timomo/Documents/Momo音乐工作坊总文件/MomoMusicWebsite"
CURRICULUM_PATH = os.path.join(WEBSITE_DIR, "curriculum.html")
COMPILE_SCRIPT = os.path.join(WEBSITE_DIR, "compile_complete_website.py")

# 1. Read style deck HTML & JS from curriculum.html
with open(CURRICULUM_PATH, "r", encoding="utf-8") as f:
    curr_html = f.read()

# Extract style-deck HTML
start_deck = curr_html.find('id="style-deck"')
if start_deck == -1:
    raise RuntimeError("Could not find id='style-deck' in curriculum.html")
sec_start = curr_html.rfind('<section', 0, start_deck)
sec_end = curr_html.find('</section>', start_deck) + len('</section>')
style_deck_section = curr_html[sec_start:sec_end]

# Extract style deck JS
start_js = curr_html.find('const styleData = [')
end_js = curr_html.find('function toggleFaq', start_js)
if start_js == -1 or end_js == -1:
    raise RuntimeError("Could not find style deck JS in curriculum.html")
style_deck_js = curr_html[start_js:end_js]

print(f"Extracted style deck HTML ({len(style_deck_section)} bytes) and JS ({len(style_deck_js)} bytes).")

# Clean any remaining Shangri-la from style_deck_section just in case
style_deck_section = style_deck_section.replace("香格里拉", "城市公共舞台")

# 2. Build the new prominent, uncrowded 6000 RMB Membership Section
prominent_membership_section = '''
        <!-- ==================== 02. 2026 PLUS 会员旗舰：突出会员卡 · 清晰明了 · 宽阔不打挤 ==================== -->
        <section class="space-y-6">
            <div class="border-b border-white/[0.08] pb-4 flex items-baseline justify-between">
                <div>
                    <span class="text-[10px] font-mono-code uppercase tracking-[0.25em] text-cyan-300 font-bold">// FLAGSHIP MEMBERSHIP</span>
                    <h2 class="text-2xl sm:text-3xl font-extrabold tracking-tight text-white mt-1">MOMO 家庭音乐会员 (2026 Plus)</h2>
                </div>
                <span class="text-xs text-neutral-400 font-mono-code hidden sm:inline">ONE PASS · WHOLE FAMILY</span>
            </div>

            <div class="spotlight-card rounded-3xl p-8 sm:p-12 lg:p-14 border border-white/10 bg-[#0d0e12] relative overflow-hidden shadow-2xl">
                <!-- 漫反射钛金流光与环境微光 -->
                <div class="metallic-sheen-sweep"></div>
                <div class="absolute -top-40 -right-40 w-[500px] h-[500px] bg-cyan-500/10 rounded-full blur-3xl pointer-events-none"></div>
                <div class="absolute -bottom-40 -left-40 w-[400px] h-[400px] bg-emerald-500/10 rounded-full blur-3xl pointer-events-none"></div>

                <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-center relative z-10">
                    
                    <!-- 左侧 5 列：高亮突出实体黑金会员卡 (3D 微倾斜 + 大图立体感) -->
                    <div class="lg:col-span-5 tilt-card-container flex flex-col items-center">
                        <div class="tilt-card relative w-full max-w-sm rounded-3xl p-2 bg-gradient-to-br from-white/20 via-white/5 to-white/10 shadow-2xl border border-white/20 group cursor-pointer">
                            <div class="rounded-2xl overflow-hidden bg-black relative">
                                <img
                                    src="./assets/images/momo_platinum_card.jpg"
                                    alt="MOMO 2026 Plus 尊享黑金实体会员卡"
                                    class="w-full aspect-[1.58/1] object-cover group-hover:scale-105 transition-transform duration-700"
                                >
                                <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent"></div>
                                <div class="absolute bottom-3 left-4 right-4 flex items-center justify-between text-xs font-mono-code">
                                    <span class="text-white font-bold tracking-wider">2026 PLUS PASS</span>
                                    <span class="text-cyan-300 font-bold">MOMO FAMILY</span>
                                </div>
                            </div>
                        </div>

                        <!-- 卡片下方价格与保障标签 (清楚明了) -->
                        <div class="mt-6 text-center space-y-2">
                            <div class="flex items-baseline justify-center gap-2">
                                <span class="text-4xl sm:text-5xl font-black text-white tracking-tight">欢迎来访或咨询</span>
                                <span class="text-xs sm:text-sm text-neutral-400 font-mono-code">/ 年 (约 欢迎来访或咨询)</span>
                            </div>
                            <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-emerald-400/10 border border-emerald-500/30 text-[11px] text-emerald-300 font-medium">
                                <span>★</span>
                                <span>7 天无理由全额退款保障 · 赠定制文化衫</span>
                            </div>
                        </div>
                    </div>

                    <!-- 右侧 7 列：权益清楚明了 · 留白舒适 · 绝不打挤 -->
                    <div class="lg:col-span-7 space-y-6">
                        <div>
                            <span class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-cyan-400/10 border border-cyan-400/30 text-xs font-mono-code text-cyan-300 font-bold">
                                一人入会 · 全家共享
                            </span>
                            <h3 class="text-2xl sm:text-3xl lg:text-4xl font-extrabold text-white mt-3 tracking-tight leading-snug">
                                为全家构建 365 天真实音乐生活
                            </h3>
                            <p class="text-xs sm:text-sm text-neutral-300 mt-2.5 leading-relaxed font-light">
                                拒绝传统培训机构按次消课的焦虑与机械打卡。MOMO 年费会员是一套完整的家庭音乐生态底座，父母与孩子随时走进录音棚与排练室，与一线爵士音乐人同台。
                            </p>
                        </div>

                        <!-- 4 大核心权益清晰清单 (大行距，舒展大气) -->
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3.5 pt-2">
                            <div class="p-3.5 rounded-2xl bg-white/[0.03] border border-white/10 hover:border-cyan-400/40 transition-colors">
                                <div class="text-cyan-300 font-mono-code text-xs font-bold">01 / 专属指导</div>
                                <h4 class="text-sm font-bold text-white mt-1">12 次 1对1 深度定制课</h4>
                                <p class="text-[11px] text-neutral-400 mt-1 leading-snug">全系乐器、声乐与即兴创作自由选修，可跨乐器流转。</p>
                            </div>
                            <div class="p-3.5 rounded-2xl bg-white/[0.03] border border-white/10 hover:border-emerald-400/40 transition-colors">
                                <div class="text-emerald-300 font-mono-code text-xs font-bold">02 / 真实合奏</div>
                                <h4 class="text-sm font-bold text-white mt-1">4师1生 真实乐队合奏</h4>
                                <p class="text-[11px] text-neutral-400 mt-1 leading-snug">拒绝罐头伴奏带！鼓手、贝斯、吉他导师围着你合奏。</p>
                            </div>
                            <div class="p-3.5 rounded-2xl bg-white/[0.03] border border-white/10 hover:border-teal-400/40 transition-colors">
                                <div class="text-teal-300 font-mono-code text-xs font-bold">03 / 棚录单曲</div>
                                <h4 class="text-sm font-bold text-white mt-1">P&R Studio 录音棚单曲实录</h4>
                                <p class="text-[11px] text-neutral-400 mt-1 leading-snug">24轨真棚同期多麦实录 + 混音，发表全家年度纪念唱片。</p>
                            </div>
                            <div class="p-3.5 rounded-2xl bg-white/[0.03] border border-white/10 hover:border-amber-400/40 transition-colors">
                                <div class="text-amber-300 font-mono-code text-xs font-bold">04 / 全家共享</div>
                                <h4 class="text-sm font-bold text-white mt-1">家庭专属档案与空间通行</h4>
                                <p class="text-[11px] text-neutral-400 mt-1 leading-snug">桐梓林与麓湖双空间畅通，全家三代共享艺术沙龙。</p>
                            </div>
                        </div>

                        <!-- 操作按钮组 -->
                        <div class="pt-4 flex flex-wrap items-center gap-4">
                            <button
                                type="button"
                                onclick="openBookingModal('申请 2026 Plus 家庭音乐年费会员 (欢迎来访或咨询)')"
                                class="px-8 py-3.5 rounded-full bg-white text-black font-extrabold text-xs sm:text-sm hover:bg-cyan-300 transition-all shadow-xl shadow-white/10 flex items-center gap-2 cursor-pointer"
                            >
                                <span>立即申请入会席位</span>
                                <span>&rarr;</span>
                            </button>
                            <a
                                href="./membership.html"
                                class="px-6 py-3.5 rounded-full bg-white/5 hover:bg-white/10 border border-white/20 text-neutral-200 hover:text-white font-semibold text-xs sm:text-sm transition-all flex items-center gap-1.5"
                            >
                                <span>查阅完整会员权益手册</span>
                                <span>&rsaquo;</span>
                            </a>
                        </div>
                    </div>

                </div>
            </div>
        </section>
'''

# 3. Build seamless marquee tracks for the faculty section
# We clone each track items so 0% to -50% translates seamlessly without blank gaps!
track_a_cards = '''
                    <!-- 1. Timo -->
                    <div onclick="openFacultyDrawer(0)" class="w-48 sm:w-56 rounded-2xl overflow-hidden bg-neutral-900 border border-white/10 hover:border-cyan-400 transition-all cursor-pointer group shrink-0">
                        <div class="h-56 sm:h-64 overflow-hidden relative">
                            <img src="./assets/images/timo_card.jpg" alt="Timo" class="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-500">
                            <div class="absolute inset-0 bg-gradient-to-t from-black via-transparent to-transparent"></div>
                            <span class="absolute top-2.5 left-2.5 px-2 py-0.5 rounded-full bg-black/60 text-[10px] font-mono-code text-cyan-300 font-bold border border-white/10">FOUNDER</span>
                        </div>
                        <div class="p-3.5">
                            <h4 class="text-sm font-bold text-white">Timo</h4>
                            <p class="text-[11px] text-neutral-400 mt-0.5">品牌创始人 · 现代爵士人</p>
                        </div>
                    </div>
                    <!-- 2. 高信博士 -->
                    <div onclick="openFacultyDrawer(4)" class="w-48 sm:w-56 rounded-2xl overflow-hidden bg-neutral-900 border border-white/10 hover:border-cyan-400 transition-all cursor-pointer group shrink-0">
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
                    <div onclick="openFacultyDrawer(1)" class="w-48 sm:w-56 rounded-2xl overflow-hidden bg-neutral-900 border border-white/10 hover:border-cyan-400 transition-all cursor-pointer group shrink-0">
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
                    <div onclick="openFacultyDrawer(3)" class="w-48 sm:w-56 rounded-2xl overflow-hidden bg-neutral-900 border border-white/10 hover:border-cyan-400 transition-all cursor-pointer group shrink-0">
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
                    <div onclick="openFacultyDrawer(5)" class="w-48 sm:w-56 rounded-2xl overflow-hidden bg-neutral-900 border border-white/10 hover:border-cyan-400 transition-all cursor-pointer group shrink-0">
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
'''

track_b_cards = '''
                    <!-- 6. 段重生 -->
                    <div onclick="openFacultyDrawer(10)" class="w-48 sm:w-56 rounded-2xl overflow-hidden bg-neutral-900 border border-white/10 hover:border-cyan-400 transition-all cursor-pointer group shrink-0">
                        <div class="h-56 sm:h-64 overflow-hidden relative">
                            <img src="./assets/images/duan_chongsheng_card.jpg" alt="段重生" class="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-500">
                            <div class="absolute inset-0 bg-gradient-to-t from-black via-transparent to-transparent"></div>
                            <span class="absolute top-2.5 left-2.5 px-2 py-0.5 rounded-full bg-cyan-950/80 text-[10px] font-mono-code text-cyan-300 font-bold border border-cyan-500/30">MMus</span>
                        </div>
                        <div class="p-3.5">
                            <h4 class="text-sm font-bold text-white">段重生 (David)</h4>
                            <p class="text-[11px] text-neutral-400 mt-0.5">南安普顿硕士优等 · 盲人作曲家</p>
                        </div>
                    </div>
                    <!-- 7. 毛维 -->
                    <div onclick="openFacultyDrawer(6)" class="w-48 sm:w-56 rounded-2xl overflow-hidden bg-neutral-900 border border-white/10 hover:border-cyan-400 transition-all cursor-pointer group shrink-0">
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
                    <div onclick="openFacultyDrawer(2)" class="w-48 sm:w-56 rounded-2xl overflow-hidden bg-neutral-900 border border-white/10 hover:border-cyan-400 transition-all cursor-pointer group shrink-0">
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
                    <div onclick="openFacultyDrawer(8)" class="w-48 sm:w-56 rounded-2xl overflow-hidden bg-neutral-900 border border-white/10 hover:border-cyan-400 transition-all cursor-pointer group shrink-0">
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
                    <div onclick="openFacultyDrawer(9)" class="w-48 sm:w-56 rounded-2xl overflow-hidden bg-neutral-900 border border-white/10 hover:border-cyan-400 transition-all cursor-pointer group shrink-0">
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
'''

seamless_faculty_section = f'''
        <!-- ==================== 04. 导师长廊：双向无缝横向流动 · 触碰悬停定格 ==================== -->
        <section class="space-y-6">
            <div class="flex items-baseline justify-between border-b border-white/[0.08] pb-4">
                <div>
                    <span class="text-[10px] font-mono-code uppercase tracking-[0.25em] text-cyan-400 font-bold">// ARTISTS &amp; FACULTY</span>
                    <h2 class="text-2xl sm:text-3xl font-extrabold tracking-tight text-white mt-1">与真正的音乐家并肩玩音乐</h2>
                </div>
                <a href="./faculty.html" class="text-xs text-neutral-400 hover:text-white font-mono-code flex items-center gap-1 transition-colors">
                    <span>查阅全部 35 位导师档案</span>
                    <span>&rarr;</span>
                </a>
            </div>

            <!-- 双排无缝无限流动长廊 (CSS keyframe marquee + 双倍卡片无缝衔接) -->
            <div class="marquee-wrapper relative overflow-hidden py-2 space-y-4">
                <!-- 上排: Track Left 向左流动 (复制两组无缝衔接) -->
                <div class="marquee-track-left flex gap-4 w-max">
                    {track_a_cards}
                    {track_a_cards}
                </div>

                <!-- 下排: Track Right 向右流动 (复制两组无缝衔接) -->
                <div class="marquee-track-right flex gap-4 w-max">
                    {track_b_cards}
                    {track_b_cards}
                </div>
            </div>
        </section>
'''

# 4. Now read compile_complete_website.py and assemble the home page
with open(COMPILE_SCRIPT, "r", encoding="utf-8") as f:
    code = f.read()

# Assemble complete apple_home_main
new_apple_home = f'''
    <main class="max-w-7xl mx-auto px-4 sm:px-6 pt-4 sm:pt-6 space-y-16 sm:space-y-24 pb-16">
        <!-- ==================== 01. 首屏 4K 巨幕舞台微雕与呼吸状态胶囊 ==================== -->
        <section class="space-y-6">
            <div class="spotlight-card rounded-3xl h-[460px] sm:h-[540px] lg:h-[580px] relative overflow-hidden flex flex-col justify-end p-8 sm:p-14">
                <video
                    id="hero-bg-video"
                    autoplay
                    loop
                    muted
                    playsinline
                    preload="auto"
                    poster="./assets/images/hero_trumpet.jpg"
                    class="absolute inset-0 w-full h-full object-cover object-[62%_center] sm:object-center brightness-105"
                >
                    <source src="./assets/media/hero_stage_loop.mp4" type="video/mp4">
                    <source src="./assets/media/hero_stage_stream.mp4" type="video/mp4">
                </video>

                <!-- 暗角保护：仅左下角微暗，确保文字锋利，面部完全通透 -->
                <div class="absolute inset-0" style="background: radial-gradient(ellipse 65% 75% at 0% 100%, rgba(4,4,6,0.92) 0%, rgba(4,4,6,0.55) 55%, transparent 80%); pointer-events: none;"></div>
                <div class="absolute inset-x-0 bottom-0 h-36 bg-gradient-to-t from-[#040406] via-[#040406]/40 to-transparent pointer-events-none"></div>

                <!-- 浮动状态胶囊 -->
                <div class="absolute top-6 left-6 sm:top-8 sm:left-12 z-20">
                    <div class="inline-flex items-center gap-2.5 px-3.5 py-1.5 rounded-full bg-black/60 backdrop-blur-xl border border-white/15 text-xs text-neutral-200">
                        <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
                        <span class="text-emerald-300 font-semibold font-mono-code">A432Hz ON AIR</span>
                        <span class="text-neutral-500">|</span>
                        <span>桐梓林 × 麓湖双空间</span>
                    </div>
                </div>

                <div class="relative z-10 max-w-xl">
                    <p class="text-[11px] font-mono-code uppercase tracking-[0.25em] text-emerald-400 font-semibold">
                        KIND · TRUTH · PASSION
                    </p>
                    <h1 class="text-3xl sm:text-5xl lg:text-[54px] font-black tracking-tight leading-[1.08] text-white mt-2">
                        让音乐回到真实生活，<br>
                        <span class="bg-gradient-to-r from-cyan-300 via-emerald-300 to-amber-200 bg-clip-text text-transparent">让热爱自然发芽。</span>
                    </h1>
                    <p class="mt-3 text-xs sm:text-base text-neutral-200 font-light leading-relaxed max-w-lg">
                        现代流行与爵士通识体系 · 家庭音乐教育 · 作品积累与方向规划
                    </p>
                    <div class="mt-6 flex flex-wrap items-center gap-3">
                        <a href="./membership.html" class="px-6 py-2.5 rounded-full bg-white text-black font-bold text-xs hover:bg-cyan-300 transition-all shadow-lg flex items-center gap-1.5">
                            <span>探索会员 Plus</span>
                            <span>&rarr;</span>
                        </a>
                        <button type="button" onclick="openTimoModal()" class="px-5 py-2.5 rounded-full bg-emerald-500/20 hover:bg-emerald-500/30 border border-emerald-400/50 hover:border-emerald-300 text-xs font-bold text-emerald-300 hover:text-white transition-all flex items-center gap-2 shadow-[0_0_15px_rgba(16,185,129,0.25)]">
                            <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
                            <span>💬 直接加 Timo 创始人微信</span>
                        </button>
                        <button type="button" onclick="openGivingModal('我要支持 MOMO · 守护声音火种')" class="px-4 py-2.5 rounded-full bg-white/5 hover:bg-white/10 border border-white/15 text-xs font-semibold text-neutral-300 hover:text-white transition-all flex items-center gap-1.5">
                            <span>💖</span>
                            <span>支持 MOMO</span>
                        </button>
                    </div>
                </div>

                <!-- 右下角原声胶囊 -->
                <div class="absolute bottom-6 right-6 sm:bottom-8 sm:right-10 z-20">
                    <button
                        id="hero-sound-btn"
                        type="button"
                        onclick="toggleHeroSound()"
                        class="flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-black/65 backdrop-blur-md border border-white/20 text-xs text-neutral-300 hover:text-white hover:border-white/40 transition-all"
                    >
                        <span id="hero-sound-icon">🔇</span>
                        <span id="hero-sound-text">开启原声</span>
                    </button>
                </div>
            </div>
        </section>

{prominent_membership_section}

{style_deck_section}

{seamless_faculty_section}

        <!-- ==================== 05. 6 大专页 Bento 瓷砖：大标题 · 真实展示 · 极度接地气 ==================== -->
        <section class="space-y-6">
            <div class="border-b border-white/[0.08] pb-4">
                <span class="text-[10px] font-mono-code uppercase tracking-[0.25em] text-cyan-400 font-bold">// ECOSYSTEM TILES</span>
                <h2 class="text-2xl sm:text-3xl font-extrabold tracking-tight text-white mt-1">探索 MOMO 音乐世界</h2>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <!-- 瓷砖 1: 大乐队与 4师1生 -->
                <a href="./ensemble-lab.html" class="spotlight-card rounded-3xl p-6 flex flex-col justify-between h-[300px] relative overflow-hidden group">
                    <img src="./assets/images/real_ensemble_rehearsal.jpg" alt="Ensemble" class="absolute inset-0 w-full h-full object-cover opacity-30 group-hover:scale-105 group-hover:opacity-45 transition-all duration-700">
                    <div class="absolute inset-0 bg-gradient-to-t from-black via-black/40 to-transparent"></div>
                    <div class="relative z-10">
                        <span class="text-[10px] font-mono-code uppercase tracking-[0.2em] text-cyan-400 font-bold">ENSEMBLE LAB</span>
                        <h3 class="text-xl sm:text-2xl font-bold text-white mt-1">4师1生 真实乐队合奏</h3>
                        <p class="text-xs text-neutral-300 mt-1.5 line-clamp-2">四位真正音乐家围着你合奏，告别罐头伴奏带。</p>
                    </div>
                    <div class="relative z-10 flex items-center justify-between text-xs font-bold text-white group-hover:text-cyan-400 transition-colors">
                        <span>探索合奏实验室</span>
                        <span>&rarr;</span>
                    </div>
                </a>

                <!-- 瓷砖 2: 作品积累与方向规划 -->
                <a href="./study-abroad.html" class="spotlight-card rounded-3xl p-6 flex flex-col justify-between h-[300px] relative overflow-hidden group">
                    <img src="./assets/images/study_abroad_hero.jpg" alt="Study Abroad" class="absolute inset-0 w-full h-full object-cover opacity-30 group-hover:scale-105 group-hover:opacity-45 transition-all duration-700">
                    <div class="absolute inset-0 bg-gradient-to-t from-black via-black/40 to-transparent"></div>
                    <div class="relative z-10">
                        <span class="text-[10px] font-mono-code uppercase tracking-[0.2em] text-cyan-400 font-bold">ACADEMIC &amp; CONSERVATORY</span>
                        <h3 class="text-xl sm:text-2xl font-bold text-white mt-1">作品积累与方向规划</h3>
                        <p class="text-xs text-neutral-300 mt-1.5 line-clamp-2">高信博士一起听作品、排方向。教学方法参考伯克利现代音乐课程。</p>
                    </div>
                    <div class="relative z-10 flex items-center justify-between text-xs font-bold text-white group-hover:text-cyan-400 transition-colors">
                        <span>听听作品</span>
                        <span>&rarr;</span>
                    </div>
                </a>

                <!-- 瓷砖 3: 共享空间 -->
                <a href="./spaces.html" class="spotlight-card rounded-3xl p-6 flex flex-col justify-between h-[300px] relative overflow-hidden group">
                    <img src="./assets/images/tongzilin_real.jpg" alt="Spaces" class="absolute inset-0 w-full h-full object-cover opacity-30 group-hover:scale-105 group-hover:opacity-45 transition-all duration-700">
                    <div class="absolute inset-0 bg-gradient-to-t from-black via-black/40 to-transparent"></div>
                    <div class="relative z-10">
                        <span class="text-[10px] font-mono-code uppercase tracking-[0.2em] text-cyan-400 font-bold">STUDIOS &amp; SPACES</span>
                        <h3 class="text-xl sm:text-2xl font-bold text-white mt-1">桐梓林与麓湖双空间</h3>
                        <p class="text-xs text-neutral-300 mt-1.5 line-clamp-2">排练室、60㎡ 花园与自然水岸声场。欢迎来访或咨询。</p>
                    </div>
                    <div class="relative z-10 flex items-center justify-between text-xs font-bold text-white group-hover:text-cyan-400 transition-colors">
                        <span>预约空间使用</span>
                        <span>&rarr;</span>
                    </div>
                </a>

                <!-- 瓷砖 4: 大凉山音乐支教公益 -->
                <a href="./charity.html" class="spotlight-card rounded-3xl p-6 flex flex-col justify-between h-[300px] relative overflow-hidden group">
                    <img src="./assets/images/daliangshan_singing.jpg" alt="Charity" class="absolute inset-0 w-full h-full object-cover opacity-30 group-hover:scale-105 group-hover:opacity-45 transition-all duration-700">
                    <div class="absolute inset-0 bg-gradient-to-t from-black via-black/40 to-transparent"></div>
                    <div class="relative z-10">
                        <span class="text-[10px] font-mono-code uppercase tracking-[0.2em] text-emerald-400 font-bold">CHARITY &amp; HOPE</span>
                        <h3 class="text-xl sm:text-2xl font-bold text-white mt-1">大凉山音乐支教公益</h3>
                        <p class="text-xs text-neutral-300 mt-1.5 line-clamp-2">常态支教与乐器采购 · 守护大山深处真实歌声。</p>
                    </div>
                    <div class="relative z-10 flex items-center justify-between text-xs font-bold text-white group-hover:text-emerald-400 transition-colors">
                        <span>了解公益纪实</span>
                        <span>&rarr;</span>
                    </div>
                </a>

                <!-- 瓷砖 5: 通识学习与九大专业学科 -->
                <a href="./curriculum.html" class="spotlight-card rounded-3xl p-6 flex flex-col justify-between h-[300px] relative overflow-hidden group">
                    <img src="./assets/images/handwritten_score.jpg" alt="Curriculum" class="absolute inset-0 w-full h-full object-cover opacity-30 group-hover:scale-105 group-hover:opacity-45 transition-all duration-700">
                    <div class="absolute inset-0 bg-gradient-to-t from-black via-black/40 to-transparent"></div>
                    <div class="relative z-10">
                        <span class="text-[10px] font-mono-code uppercase tracking-[0.2em] text-cyan-400 font-bold">CURRICULUM MATRIX</span>
                        <h3 class="text-xl sm:text-2xl font-bold text-white mt-1">通识学习与专业学科</h3>
                        <p class="text-xs text-neutral-300 mt-1.5 line-clamp-2">3-7岁通识启蒙 · 吉他/贝斯/管乐/打击乐专业选修。</p>
                    </div>
                    <div class="relative z-10 flex items-center justify-between text-xs font-bold text-white group-hover:text-cyan-400 transition-colors">
                        <span>查阅完整课程库</span>
                        <span>&rarr;</span>
                    </div>
                </a>

                <!-- 瓷砖 6: 音乐周边美学商店 -->
                <a href="./store/index.html" class="spotlight-card rounded-3xl p-6 flex flex-col justify-between h-[300px] relative overflow-hidden group">
                    <img src="./assets/images/merch_vinyl.jpg" alt="Store" class="absolute inset-0 w-full h-full object-cover opacity-30 group-hover:scale-105 group-hover:opacity-45 transition-all duration-700">
                    <div class="absolute inset-0 bg-gradient-to-t from-black via-black/40 to-transparent"></div>
                    <div class="relative z-10">
                        <span class="text-[10px] font-mono-code uppercase tracking-[0.2em] text-amber-400 font-bold">MERCH STORE</span>
                        <h3 class="text-xl sm:text-2xl font-bold text-white mt-1">MOMO 音乐周边商店</h3>
                        <p class="text-xs text-neutral-300 mt-1.5 line-clamp-2">重磅文化衫 · 专业拔片 · 黑胶帆布包 · 利润支持公益。</p>
                    </div>
                    <div class="relative z-10 flex items-center justify-between text-xs font-bold text-white group-hover:text-amber-400 transition-colors">
                        <span>进入商店选购</span>
                        <span>&rarr;</span>
                    </div>
                </a>
            </div>
        </section>

        <!-- ==================== 06. 奉献板块：极度简化为双栏纯粹基金卡片 ==================== -->
        <section class="space-y-6">
            <div class="text-center max-w-2xl mx-auto space-y-2">
                <span class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-400/10 border border-emerald-500/30 text-xs font-mono-code font-bold text-emerald-300 uppercase tracking-widest">
                    <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-ping"></span>
                    MOMO CO-CREATION PATRONAGE · 声音火种守护
                </span>
                <h2 class="text-3xl sm:text-4xl font-black text-white tracking-tight">
                    守护纯粹音乐，与我们同行
                </h2>
                <p class="text-xs sm:text-sm text-neutral-300 leading-relaxed font-light">
                    MOMO 是一个扎根教育与共创的非资本化声场。每一份奉献都 100% 透明用于教学器材添置与热爱学子奖学金。
                </p>
            </div>

            <!-- 仅保留两个纯粹大气的基金卡片 (经典高定墨黑深邃质感) -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 items-stretch max-w-5xl mx-auto">
                <!-- 卡片 1: 教学设备器材基金 -->
                <div class="spotlight-card rounded-3xl p-8 sm:p-10 flex flex-col justify-between bg-gradient-to-b from-[#0c1813] via-[#09110d] to-[#050807] border border-emerald-500/30 relative group shadow-2xl">
                    <div class="absolute -top-24 -right-24 w-60 h-60 bg-emerald-500/10 rounded-full blur-3xl pointer-events-none"></div>
                    <div>
                        <div class="flex items-center justify-between pb-3 border-b border-white/10">
                            <span class="text-[10px] font-mono-code uppercase tracking-[0.2em] text-emerald-400 font-bold">01 · EQUIPMENT FUND</span>
                            <span class="px-2 py-0.5 rounded-full bg-white/[0.06] text-[10px] text-neutral-400">持续共建</span>
                        </div>
                        <h3 class="text-2xl sm:text-3xl font-black text-white mt-4 tracking-tight">
                            教学设备器材基金
                        </h3>
                        <p class="text-xs sm:text-sm text-neutral-300 mt-2.5 leading-relaxed">
                            为在 MOMO 研习的孩子与乐队添置专业旗舰舞台电钢、返听监听音箱、专业耳返与高品质录音器材，给学子提供世界一流的声场条件。
                        </p>
                        <div class="mt-4 p-3 rounded-2xl bg-black/40 border border-white/10 text-[11px] text-neutral-400 space-y-1 font-mono-code">
                            <div>• 如何支持，欢迎来访或咨询</div>
                            <div>• 款项定向注入乐器与声场器材采购</div>
                        </div>
                    </div>
                    <div class="pt-6 mt-6 border-t border-white/10">
                        <button
                            type="button"
                            onclick="openGivingModal('我要支持教学设备器材基金', 'equipment')"
                            class="w-full py-3.5 rounded-full bg-gradient-to-r from-emerald-400 to-teal-400 hover:from-emerald-300 hover:to-teal-300 text-black font-extrabold text-xs sm:text-sm transition-all shadow-[0_0_20px_rgba(16,185,129,0.35)] flex items-center justify-center gap-2 cursor-pointer"
                        >
                            <span>🎸 我要支持设备基金</span>
                            <span>&rarr;</span>
                        </button>
                    </div>
                </div>

                <!-- 卡片 2: 音乐学者奖助学金 -->
                <div class="spotlight-card rounded-3xl p-8 sm:p-10 flex flex-col justify-between bg-gradient-to-b from-[#14120c] via-[#0d0c08] to-[#070605] border border-amber-500/30 relative group shadow-2xl">
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
                        <div class="mt-4 p-3 rounded-2xl bg-black/40 border border-white/10 text-[11px] text-neutral-400 space-y-1 font-mono-code">
                            <div>• 支持全额/半额奖助学金及社区大师课专项</div>
                            <div>• 善款直达学子学费扶持与公开艺术课场地支持</div>
                        </div>
                    </div>
                    <div class="pt-6 mt-6 border-t border-white/10">
                        <button
                            type="button"
                            onclick="openGivingModal('资助音乐学者奖助学金', 'scholarship')"
                            class="w-full py-3.5 rounded-full bg-amber-400/20 hover:bg-amber-400/30 border border-amber-400/50 text-amber-300 font-bold text-xs sm:text-sm transition-all flex items-center justify-center gap-2 cursor-pointer"
                        >
                            <span>🎓 资助学者奖学金</span>
                            <span>&rarr;</span>
                        </button>
                    </div>
                </div>
            </div>

            <!-- 极简透明历史支持者名单轮播 -->
            <div class="max-w-3xl mx-auto p-4 rounded-2xl bg-black/60 border border-white/10 text-center">
                <div class="text-[11px] font-mono-code text-emerald-400 font-bold mb-2">★ 感谢每一位同行者 · 历史支持芳名录</div>
                <div class="flex flex-wrap items-center justify-center gap-2 sm:gap-4 text-xs text-neutral-300 font-mono-code">
                    <span class="px-2.5 py-1 rounded-lg bg-white/[0.04] border border-white/10">林先生（设备 · 欢迎来访或咨询）</span>
                    <span class="px-2.5 py-1 rounded-lg bg-white/[0.04] border border-white/10">MOMO 会员家庭（奖学金 · 欢迎来访或咨询）</span>
                    <span class="px-2.5 py-1 rounded-lg bg-white/[0.04] border border-white/10">匿名伙伴（设备 · 欢迎来访或咨询）</span>
                    <span class="px-2.5 py-1 rounded-lg bg-white/[0.04] border border-white/10">陈女士（支教乐器 · 欢迎来访或咨询）</span>
                    <span class="px-2.5 py-1 rounded-lg bg-white/[0.04] border border-white/10">张同学（教学耗材 · 欢迎来访或咨询）</span>
                </div>
            </div>
        </section>

        <!-- ==================== 07. 创始人直通微信通道：真实扫码 · 绝不冗长 ==================== -->
        <section class="space-y-6">
            <div class="spotlight-card rounded-3xl p-8 sm:p-12 border border-emerald-500/30 bg-gradient-to-b from-[#0c1612] via-[#09110d] to-[#060807] relative overflow-hidden shadow-2xl">
                <div class="absolute -top-32 -right-32 w-80 h-80 bg-emerald-500/10 rounded-full blur-3xl pointer-events-none"></div>
                <div class="max-w-4xl mx-auto flex flex-col md:flex-row items-center justify-between gap-8 relative z-10">
                    <div class="space-y-3 text-center md:text-left">
                        <span class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-400/10 border border-emerald-500/30 text-xs font-mono-code font-bold text-emerald-300">
                            <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-ping"></span>
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
                        <div class="w-44 p-3 bg-white rounded-2xl shadow-2xl shadow-black/80 mx-auto transform hover:scale-105 transition-transform duration-300">
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

# Replace apple_home_main in code
home_start_marker = "apple_home_main = '''"
home_end_marker = "index_html = ("

h_start = code.find(home_start_marker)
h_end = code.find(home_end_marker, h_start)
if h_start == -1 or h_end == -1:
    raise RuntimeError("Could not find apple_home_main marker in compile_complete_website.py")

code = code[:h_start] + "apple_home_main = '''" + new_apple_home + "'''\n\n" + code[h_end:]

# Also ensure style_deck_js is included in index.html footer scripts!
# In render_apple_footer_and_scripts:
footer_func_marker = "def render_apple_footer_and_scripts"
foot_pos = code.find(footer_func_marker)
# We can inject style_deck_js into creative_js or additional_scripts if on index
script_inject_marker = "creative_js = \"\"\""
script_pos = code.find(script_inject_marker)
if script_pos != -1:
    # Inject style_deck_js right before creative_js
    code = code[:script_pos] + f'''
    # 注入音乐风格卡片机配套原生音频 JS
    style_deck_runtime_js = """
<script>
{style_deck_js}
</script>
"""
    ''' + code[script_pos:]
    # And include style_deck_runtime_js in return
    return_marker = "return f'''"
    ret_pos = code.find(return_marker, script_pos)
    if ret_pos != -1:
        # replace {creative_js} with {style_deck_runtime_js}\n{creative_js}
        code = code.replace("{creative_js}", "{style_deck_runtime_js}\n{creative_js}", 1)

with open(COMPILE_SCRIPT, "w", encoding="utf-8") as f:
    f.write(code)

print("compile_complete_website.py updated with style deck and uncrowded membership section!")
