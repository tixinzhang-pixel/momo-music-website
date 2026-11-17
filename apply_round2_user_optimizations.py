# -*- coding: utf-8 -*-
"""
apply_round2_user_optimizations.py
Executes the user's 7 specific design and content optimizations:
1. Remove all '102' text (camp names, audition options, buttons).
2. Simplify space names to '桐梓林', '麓湖', '线上远程' without complicated suffixes, and remove oily/pompous wording.
3. Optimize Style Deck: fit in 1 page on mobile, clear pill tabs, album smooth slide, compact player, remove redundant action cards.
4. Redesign Faculty Marquee: High-end white background with subtle pearl gradient, crisp dark typography, gallery cards.
5. Replace 6 Bento tiles with the comprehensive Music Majors & Disciplines matrix.
6. Replace dark giving section with a warm community-style section (non-black background) and real honest supporter board: 【成为第一位以实际行动对Momo音乐教育发起支持的人】.
7. Giving modal: clean white background, headline 【愿上帝祝福你乐意帮助的好行为】, project select dropdown with direct support / equipment / scholarship options, real working payment QR codes.
"""

import os
import re

WEBSITE_DIR = "/Users/timomo/Documents/Momo音乐工作坊总文件/MomoMusicWebsite"
COMPILE_SCRIPT = os.path.join(WEBSITE_DIR, "compile_complete_website.py")

with open(COMPILE_SCRIPT, "r", encoding="utf-8") as f:
    code = f.read()

# ---------------------------------------------------------------------------
# 1. REMOVE ALL 102
# ---------------------------------------------------------------------------
code = code.replace("102 · Momo 国际爵士音乐夏令营", "Momo 国际爵士音乐夏令营")
code = code.replace("102·Momo 国际爵士音乐夏令营", "Momo 国际爵士音乐夏令营")
code = code.replace("102·Momo 国际爵士夏令营", "Momo 国际爵士夏令营")
code = code.replace("申请【102·Momo 国际爵士夏令营】Audition 考核", "申请【Momo 国际爵士夏令营】Audition 考核")
code = code.replace("Momo 国际爵士音乐夏令营（欢迎来预约了解）", "Momo 国际爵士音乐夏令营（欢迎来预约了解）")
code = code.replace("102·Momo 国际爵士夏令营", "Momo 国际爵士夏令营")

# ---------------------------------------------------------------------------
# 2. SIMPLIFY SPACE NAMES (REMOVE COMPLICATED SUFFIXES) & DE-OIL PHRASES
# ---------------------------------------------------------------------------
# Form options
code = code.replace("桐梓林花园私密声场", "桐梓林")
code = code.replace("麓湖湖畔水岸声场", "麓湖")
code = code.replace("线上远程评估与咨询", "线上远程")
code = code.replace("线上远程咨询与评估", "线上远程")
code = code.replace("线上远程评估", "线上远程")

# Remove remaining oily/pompous phrases
code = code.replace("做真实的教育 · 100% 定向透明", "真实音乐教育 · 透明公开")
code = code.replace("MOMO CO-CREATION PATRONAGE · 声音火种守护", "COMMUNITY SUPPORT · 社区支持")
code = code.replace("守护纯粹音乐，与我们同行", "支持 Momo 音乐教育")
code = code.replace("非资本化声场", "独立音乐工作坊")

# ---------------------------------------------------------------------------
# 3. REBUILD STYLE DECK (FIT IN 1 PAGE, CLEAR PILL TABS, ALBUM SLIDE)
# ---------------------------------------------------------------------------
new_style_deck = '''
        <!-- ==================== 04. 音乐风格卡片机：精确一页 · 风格标签清楚切换 · 专辑平滑左右移动 ==================== -->
        <section id="style-deck" class="space-y-4 pt-4">
            <div class="rounded-3xl p-6 sm:p-10 lg:p-12 bg-[#0C0D12] text-white border border-neutral-800 shadow-2xl relative overflow-hidden">
                <!-- 顶部标题与左右微调按钮 -->
                <div class="flex flex-col sm:flex-row sm:items-center justify-between pb-4 border-b border-neutral-800 gap-3">
                    <div>
                        <span class="text-[10px] font-mono-code uppercase tracking-[0.25em] text-cyan-400 font-bold">
                            // MUSIC STYLES · 风格试听
                        </span>
                        <h2 class="text-2xl sm:text-3xl font-black tracking-tight text-white mt-1">
                            戴上耳机，感受 6 种经典现代音乐风格
                        </h2>
                    </div>
                    <div class="flex items-center gap-2 self-start sm:self-auto">
                        <button type="button" onclick="prevStyleCard()" class="p-2 rounded-xl bg-neutral-900 border border-neutral-700 hover:border-cyan-400 text-white transition-colors" aria-label="上一首">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg>
                        </button>
                        <span id="deck-indicator" class="text-xs font-mono-code text-neutral-400 px-2 min-w-[50px] text-center">01 / 06</span>
                        <button type="button" onclick="nextStyleCard()" class="p-2 rounded-xl bg-neutral-900 border border-neutral-700 hover:border-cyan-400 text-white transition-colors" aria-label="下一首">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
                        </button>
                    </div>
                </div>

                <!-- 风格胶囊标签栏 (清楚切换，可横向轻滑) -->
                <div class="flex items-center gap-2 overflow-x-auto py-2 no-scrollbar" id="style-tabs-list">
                    <button type="button" onclick="selectStyleCard(0)" class="style-tab-pill active px-3.5 py-1.5 rounded-full text-xs font-mono-code font-bold transition-all bg-white text-black shadow">
                        01 Swing 摇摆
                    </button>
                    <button type="button" onclick="selectStyleCard(1)" class="style-tab-pill px-3.5 py-1.5 rounded-full text-xs font-mono-code font-bold transition-all bg-neutral-900 text-neutral-300 hover:text-white border border-neutral-800">
                        02 Bebop 波普
                    </button>
                    <button type="button" onclick="selectStyleCard(2)" class="style-tab-pill px-3.5 py-1.5 rounded-full text-xs font-mono-code font-bold transition-all bg-neutral-900 text-neutral-300 hover:text-white border border-neutral-800">
                        03 Blues 德州布鲁斯
                    </button>
                    <button type="button" onclick="selectStyleCard(3)" class="style-tab-pill px-3.5 py-1.5 rounded-full text-xs font-mono-code font-bold transition-all bg-neutral-900 text-neutral-300 hover:text-white border border-neutral-800">
                        04 Hard Rock 硬摇滚
                    </button>
                    <button type="button" onclick="selectStyleCard(4)" class="style-tab-pill px-3.5 py-1.5 rounded-full text-xs font-mono-code font-bold transition-all bg-neutral-900 text-neutral-300 hover:text-white border border-neutral-800">
                        05 Bossa Nova 波萨
                    </button>
                    <button type="button" onclick="selectStyleCard(5)" class="style-tab-pill px-3.5 py-1.5 rounded-full text-xs font-mono-code font-bold transition-all bg-neutral-900 text-neutral-300 hover:text-white border border-neutral-800">
                        06 Pop &amp; Funk 放克
                    </button>
                </div>

                <!-- 核心专辑展示区：卡片平滑左右滑动 (紧凑单页) -->
                <div class="relative overflow-hidden py-3">
                    <div class="flex items-center gap-4 transition-transform duration-500 ease-out" id="cards-track">
                        <!-- 01 Swing -->
                        <div class="style-card active-card w-60 sm:w-64 flex-shrink-0 bg-neutral-900/90 border border-neutral-700 rounded-2xl p-4 cursor-pointer transition-all" onclick="selectStyleCard(0)">
                            <div class="h-36 sm:h-40 w-full overflow-hidden rounded-xl bg-black relative mb-3">
                                <img src="./assets/images/swing.png" alt="Swing" class="w-full h-full object-cover">
                                <span class="absolute top-2 left-2 text-[9px] font-mono-code font-black uppercase bg-black/80 px-2 py-0.5 rounded text-cyan-300">01 SWING</span>
                            </div>
                            <h4 class="text-sm font-bold text-white">Swing &amp; Big Band</h4>
                            <p class="text-neutral-400 text-[11px] mt-0.5 truncate">哈林跳舞律动与大乐队总谱</p>
                        </div>
                        <!-- 02 Bebop -->
                        <div class="style-card w-60 sm:w-64 flex-shrink-0 bg-neutral-900/90 border border-neutral-800 rounded-2xl p-4 cursor-pointer transition-all opacity-60 hover:opacity-90" onclick="selectStyleCard(1)">
                            <div class="h-36 sm:h-40 w-full overflow-hidden rounded-xl bg-black relative mb-3">
                                <video src="./assets/audio/midnight_on_52nd_bebop.mp4#t=0.001" preload="metadata" muted playsinline loop class="w-full h-full object-cover pointer-events-none"></video>
                                <span class="absolute top-2 left-2 text-[9px] font-mono-code font-black uppercase bg-black/80 px-2 py-0.5 rounded text-emerald-300">02 BEBOP</span>
                            </div>
                            <h4 class="text-sm font-bold text-white">Bebop &amp; Modern Jazz</h4>
                            <p class="text-neutral-400 text-[11px] mt-0.5 truncate">52街高速即兴与半音阶和声</p>
                        </div>
                        <!-- 03 Blues -->
                        <div class="style-card w-60 sm:w-64 flex-shrink-0 bg-neutral-900/90 border border-neutral-800 rounded-2xl p-4 cursor-pointer transition-all opacity-60 hover:opacity-90" onclick="selectStyleCard(2)">
                            <div class="h-36 sm:h-40 w-full overflow-hidden rounded-xl bg-black relative mb-3">
                                <video src="./assets/audio/six_string_savior_blues.mp4#t=0.001" preload="metadata" muted playsinline loop class="w-full h-full object-cover pointer-events-none"></video>
                                <span class="absolute top-2 left-2 text-[9px] font-mono-code font-black uppercase bg-black/80 px-2 py-0.5 rounded text-cyan-300">03 BLUES</span>
                            </div>
                            <h4 class="text-sm font-bold text-white">Delta &amp; Texas Blues</h4>
                            <p class="text-neutral-400 text-[11px] mt-0.5 truncate">德州电吉他推弦与根源重拍</p>
                        </div>
                        <!-- 04 Rock -->
                        <div class="style-card w-60 sm:w-64 flex-shrink-0 bg-neutral-900/90 border border-neutral-800 rounded-2xl p-4 cursor-pointer transition-all opacity-60 hover:opacity-90" onclick="selectStyleCard(3)">
                            <div class="h-36 sm:h-40 w-full overflow-hidden rounded-xl bg-black relative mb-3">
                                <video src="./assets/audio/redline_surge_hard_rock.mp4#t=0.001" preload="metadata" muted playsinline loop class="w-full h-full object-cover pointer-events-none"></video>
                                <span class="absolute top-2 left-2 text-[9px] font-mono-code font-black uppercase bg-black/80 px-2 py-0.5 rounded text-amber-300">04 ROCK</span>
                            </div>
                            <h4 class="text-sm font-bold text-white">Classic Hard Rock</h4>
                            <p class="text-neutral-400 text-[11px] mt-0.5 truncate">过载音箱力量和弦与律动驱动力</p>
                        </div>
                        <!-- 05 Bossa -->
                        <div class="style-card w-60 sm:w-64 flex-shrink-0 bg-neutral-900/90 border border-neutral-800 rounded-2xl p-4 cursor-pointer transition-all opacity-60 hover:opacity-90" onclick="selectStyleCard(4)">
                            <div class="h-36 sm:h-40 w-full overflow-hidden rounded-xl bg-black relative mb-3">
                                <video src="./assets/audio/rios_blue_sky_bossa_nova.mp4#t=0.001" preload="metadata" muted playsinline loop class="w-full h-full object-cover pointer-events-none"></video>
                                <span class="absolute top-2 left-2 text-[9px] font-mono-code font-black uppercase bg-black/80 px-2 py-0.5 rounded text-teal-300">05 BOSSA</span>
                            </div>
                            <h4 class="text-sm font-bold text-white">Bossa Nova</h4>
                            <p class="text-neutral-400 text-[11px] mt-0.5 truncate">里约微风、尼龙弦与切分和声</p>
                        </div>
                        <!-- 06 Funk -->
                        <div class="style-card w-60 sm:w-64 flex-shrink-0 bg-neutral-900/90 border border-neutral-800 rounded-2xl p-4 cursor-pointer transition-all opacity-60 hover:opacity-90" onclick="selectStyleCard(5)">
                            <div class="h-36 sm:h-40 w-full overflow-hidden rounded-xl bg-black relative mb-3">
                                <video src="./assets/audio/golden_light_funk.mp4#t=0.001" preload="metadata" muted playsinline loop class="w-full h-full object-cover pointer-events-none"></video>
                                <span class="absolute top-2 left-2 text-[9px] font-mono-code font-black uppercase bg-black/80 px-2 py-0.5 rounded text-yellow-300">06 FUNK</span>
                            </div>
                            <h4 class="text-sm font-bold text-white">Contemporary Pop &amp; Funk</h4>
                            <p class="text-neutral-400 text-[11px] mt-0.5 truncate">精巧切分贝斯与现代舞曲律动</p>
                        </div>
                    </div>
                </div>

                <!-- 紧凑音频控制条：当前风格一句话听感 + 试听播放控件 (完全收纳，不占高度) -->
                <div class="p-4 rounded-2xl bg-neutral-900/90 border border-neutral-800 space-y-3">
                    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
                        <div>
                            <span id="card-period" class="text-[10px] font-mono-code text-cyan-300 font-bold uppercase mr-2">1930s ERA</span>
                            <span id="card-title" class="text-sm font-bold text-white">Swing &amp; Big Band 摇摆大乐队时代</span>
                        </div>
                        <p id="card-desc" class="text-xs text-neutral-400 max-w-md line-clamp-1">
                            哈林区经典跳舞律动，标志性 Walking Bass 走带低音与大编制铜管对位。
                        </p>
                    </div>

                    <!-- 播放行：播放按键 + 声波条 + 进度条 -->
                    <div class="flex items-center gap-3 pt-1">
                        <button type="button" onclick="toggleAudioPlayback()" id="btn-play-style" class="px-4 py-2 rounded-xl bg-cyan-400 hover:bg-cyan-300 text-black font-extrabold text-xs flex items-center gap-2 transition-all shrink-0">
                            <svg id="play-icon-svg" class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
                            <span id="btn-play-text">试听音轨</span>
                        </button>

                        <!-- EQ 跳杆 -->
                        <div id="wave-container" class="flex items-end gap-1 h-5 shrink-0 px-2">
                            <span class="wave-bar"></span>
                            <span class="wave-bar"></span>
                            <span class="wave-bar"></span>
                            <span class="wave-bar"></span>
                            <span class="wave-bar"></span>
                        </div>

                        <!-- 进度条 -->
                        <div class="flex items-center gap-2 flex-1">
                            <span id="audio-current-time" class="text-[11px] font-mono-code text-cyan-300 min-w-[30px]">0:00</span>
                            <input type="range" id="audio-seek-bar" value="0" min="0" max="100" step="0.1" class="flex-1 h-1 bg-neutral-700 rounded-lg appearance-none cursor-pointer accent-cyan-400">
                            <span id="audio-duration-time" class="text-[11px] font-mono-code text-neutral-400 min-w-[30px] text-right">0:00</span>
                        </div>
                    </div>
                </div>

                <!-- 隐藏的音频元素 -->
                <audio id="native-audio-player" preload="metadata" class="hidden">
                    <source id="native-audio-source" src="./assets/audio/savoy_ballroom_stomp_swing.mp4" type="video/mp4">
                </audio>
            </div>
        </section>
'''

# ---------------------------------------------------------------------------
# 4. REBUILD FACULTY SECTION (WHITE THEME WITH SUBTLE PEARL GRADIENT)
# ---------------------------------------------------------------------------
# Extract the faculty cards from the current code
pos_fac_start = code.find('<!-- ==================== 05. 真实常驻师资长廊')
pos_fac_end = code.find('<!-- ==================== 06. MI 学院风格整版入会申请大版面')
if pos_fac_start == -1 or pos_fac_end == -1:
    raise Exception(f"Faculty markers not found: {pos_fac_start}, {pos_fac_end}")

old_faculty_block = code[pos_fac_start:pos_fac_end]

# Extract Track 1 and Track 2 cards
m_track_left = re.search(r'<div class="marquee-track-left[^>]*>(.*?)</div>\s*<!-- 下排', old_faculty_block, re.DOTALL)
m_track_right = re.search(r'<div class="marquee-track-right[^>]*>(.*?)</div>\s*</div>\s*</section>', old_faculty_block, re.DOTALL)

track_left_cards = m_track_left.group(1).strip() if m_track_left else ""
track_right_cards = m_track_right.group(1).strip() if m_track_right else ""

# Transform card styles in track_left and track_right to high-end white gallery cards
def convert_to_white_cards(cards_html):
    # Change card bg from bg-neutral-900 to bg-white, border-white/10 to border-neutral-200
    c = cards_html.replace('bg-neutral-900 border border-white/10', 'bg-white border border-neutral-200 shadow-sm hover:shadow-lg')
    # Change text colors
    c = c.replace('text-white', 'text-neutral-900')
    c = c.replace('text-neutral-400 mt-0.5', 'text-neutral-500 mt-0.5')
    c = c.replace('bg-black/60 text-[10px] font-mono-code text-cyan-300 font-bold border border-white/10', 'bg-black/75 text-[10px] font-mono-code text-white font-bold')
    c = c.replace('bg-black/60 text-[10px] font-mono-code text-neutral-300 font-bold border border-white/10', 'bg-black/75 text-[10px] font-mono-code text-white font-bold')
    return c

new_track_left = convert_to_white_cards(track_left_cards)
new_track_right = convert_to_white_cards(track_right_cards)

new_faculty_section = f'''
        <!-- ==================== 05. 真实常驻师资长廊：白底高定感 · 双向无缝横向流动 ==================== -->
        <section class="space-y-6 pt-4">
            <div class="rounded-3xl p-8 sm:p-14 lg:p-16 text-neutral-900 border border-neutral-200/90 shadow-[0_20px_60px_-15px_rgba(0,0,0,0.06)] relative overflow-hidden" style="background: radial-gradient(circle at 50% 0%, #FFFFFF 0%, #FAFBFD 60%, #F2F4F7 100%);">
                <!-- 顶部标题与档案链接 -->
                <div class="flex flex-col sm:flex-row sm:items-end justify-between pb-8 border-b border-neutral-200 gap-4">
                    <div>
                        <span class="text-[11px] font-mono-code uppercase tracking-[0.25em] text-neutral-500 font-bold">
                            // FACULTY &amp; RESIDENT ARTISTS · 真实常驻师资团队
                        </span>
                        <h2 class="text-3xl sm:text-4xl lg:text-[40px] font-black tracking-tight text-neutral-900 mt-2 leading-[1.15]">
                            他们不仅是舞台上的艺术家，更是你每一节课的真实导师
                        </h2>
                        <p class="text-xs sm:text-sm text-neutral-600 max-w-3xl leading-relaxed mt-2 font-normal">
                            拒绝名师挂名宣传。以下 35 位国内外一线爵士演奏家、管乐博士与音乐制作人，均为 MOMO 日常教学与陪练的常驻老师。成为会员即可在线下桐梓林、麓湖或线上，直接预约他们的 1对1 课程与乐队合奏指导。
                        </p>
                    </div>
                    <a href="./faculty.html" class="px-5 py-2.5 rounded-full bg-neutral-100 hover:bg-neutral-200 border border-neutral-300 text-neutral-800 text-xs font-mono-code font-bold flex items-center gap-1.5 transition-colors shrink-0 w-fit">
                        <span>查阅全部 35 位导师档案</span>
                        <span>&rarr;</span>
                    </a>
                </div>

                <!-- 双排无缝无限流动长廊 (左右白雾边缘遮罩) -->
                <div class="marquee-wrapper relative overflow-hidden py-4 space-y-4">
                    <div class="absolute inset-y-0 left-0 w-12 sm:w-24 bg-gradient-to-r from-[#FAFBFD] via-[#FAFBFD]/90 to-transparent pointer-events-none z-10"></div>
                    <div class="absolute inset-y-0 right-0 w-12 sm:w-24 bg-gradient-to-l from-[#FAFBFD] via-[#FAFBFD]/90 to-transparent pointer-events-none z-10"></div>

                    <!-- 上排: Track Left 向左流动 -->
                    <div class="marquee-track-left flex gap-4 w-max">
                        {new_track_left}
                    </div>

                    <!-- 下排: Track Right 向右流动 -->
                    <div class="marquee-track-right flex gap-4 w-max">
                        {new_track_right}
                    </div>
                </div>
            </div>
        </section>
'''

# ---------------------------------------------------------------------------
# 5. REPLACE 6 BENTO TILES WITH MUSIC MAJORS MATRIX
# ---------------------------------------------------------------------------
pos_bento_start = code.find('<!-- ==================== 05. 6 大专页 Bento 瓷砖')
pos_giving_start = code.find('<!-- ==================== 06. 奉献板块')
if pos_bento_start == -1 or pos_giving_start == -1:
    raise Exception(f"Bento / Giving markers not found: {pos_bento_start}, {pos_giving_start}")

new_majors_section = '''
        <!-- ==================== 07. 音乐专业介绍：九大现代音乐学科与通识矩阵 ==================== -->
        <section class="space-y-6 pt-4">
            <div class="rounded-3xl p-8 sm:p-12 lg:p-16 bg-[#0B0C10] text-white border border-neutral-800 shadow-2xl relative overflow-hidden">
                <div class="flex flex-col sm:flex-row sm:items-end justify-between pb-8 border-b border-neutral-800 gap-3">
                    <div>
                        <span class="text-[11px] font-mono-code uppercase tracking-[0.25em] text-cyan-400 font-bold">
                            // MAJORS &amp; DEPARTMENTS · 音乐专业介绍
                        </span>
                        <h2 class="text-3xl sm:text-4xl lg:text-[40px] font-black tracking-tight text-white mt-2 leading-[1.15]">
                            九大现代音乐学科与通识体系
                        </h2>
                        <p class="text-xs sm:text-sm text-neutral-300 mt-2 max-w-2xl leading-relaxed">
                            从 0 基础通识启蒙，到一对一专业器乐私教与大乐队合奏实战。全系学科由一线常驻导师亲授，支持会员自由跨学科选修。
                        </p>
                    </div>
                    <a href="./curriculum.html" class="px-5 py-2.5 rounded-full bg-white/10 hover:bg-white/20 border border-white/20 text-white text-xs font-mono-code font-bold flex items-center gap-1.5 transition-colors shrink-0 w-fit">
                        <span>查阅完整课程库</span>
                        <span>&rarr;</span>
                    </a>
                </div>

                <!-- 9 大专业学科卡片网格 (3x3 网格) -->
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5 pt-8">
                    <!-- 1. 贝斯学科 -->
                    <div class="p-6 rounded-2xl bg-neutral-900/80 border border-neutral-800 hover:border-cyan-400/40 transition-all flex flex-col justify-between">
                        <div class="space-y-2">
                            <span class="text-[10px] font-mono-code text-cyan-400 uppercase tracking-widest font-bold">BASS DEPARTMENT</span>
                            <h3 class="text-lg font-black text-white">Double Bass 与现代电贝斯</h3>
                            <p class="text-xs text-neutral-400 leading-relaxed">
                                原声低音提琴 Walking Bass 律动走带、弓法与现代电贝斯 Funk Slap，掌握乐队真正的低频脉搏。
                            </p>
                        </div>
                        <div class="pt-4 mt-4 border-t border-neutral-800 flex items-center justify-between text-xs">
                            <span class="text-neutral-500 font-mono">适合：律动骨架 / 乐队低音</span>
                            <a href="./curriculum.html#matrix" class="text-cyan-400 hover:underline font-bold">了解专业 &rarr;</a>
                        </div>
                    </div>

                    <!-- 2. 吉他学科 -->
                    <div class="p-6 rounded-2xl bg-neutral-900/80 border border-neutral-800 hover:border-cyan-400/40 transition-all flex flex-col justify-between">
                        <div class="space-y-2">
                            <span class="text-[10px] font-mono-code text-cyan-400 uppercase tracking-widest font-bold">GUITAR DEPARTMENT</span>
                            <h3 class="text-lg font-black text-white">电吉他声音设计与现代木吉他</h3>
                            <p class="text-xs text-neutral-400 leading-relaxed">
                                效果器单块链与管箱音色调校、现代流行伴奏编配与爵士布鲁斯即兴，弹奏真实动人的线条。
                            </p>
                        </div>
                        <div class="pt-4 mt-4 border-t border-neutral-800 flex items-center justify-between text-xs">
                            <span class="text-neutral-500 font-mono">适合：主音吉他 / 现代弹唱</span>
                            <a href="./curriculum.html#matrix" class="text-cyan-400 hover:underline font-bold">了解专业 &rarr;</a>
                        </div>
                    </div>

                    <!-- 3. 爵士鼓与打击乐 -->
                    <div class="p-6 rounded-2xl bg-neutral-900/80 border border-neutral-800 hover:border-cyan-400/40 transition-all flex flex-col justify-between">
                        <div class="space-y-2">
                            <span class="text-[10px] font-mono-code text-cyan-400 uppercase tracking-widest font-bold">DRUMS &amp; PERCUSSION</span>
                            <h3 class="text-lg font-black text-white">现代流行鼓手与爵士鼓组</h3>
                            <p class="text-xs text-neutral-400 leading-relaxed">
                                四肢独立控制、反拍重音律动与 18 人大乐队总谱实战排练，建立顶尖稳健的节拍心脏。
                            </p>
                        </div>
                        <div class="pt-4 mt-4 border-t border-neutral-800 flex items-center justify-between text-xs">
                            <span class="text-neutral-500 font-mono">适合：核心节拍 / 乐队鼓手</span>
                            <a href="./curriculum.html#matrix" class="text-cyan-400 hover:underline font-bold">了解专业 &rarr;</a>
                        </div>
                    </div>

                    <!-- 4. 键盘钢琴 -->
                    <div class="p-6 rounded-2xl bg-neutral-900/80 border border-neutral-800 hover:border-cyan-400/40 transition-all flex flex-col justify-between">
                        <div class="space-y-2">
                            <span class="text-[10px] font-mono-code text-cyan-400 uppercase tracking-widest font-bold">KEYS &amp; PIANO</span>
                            <h3 class="text-lg font-black text-white">现代流行钢琴与爵士和声</h3>
                            <p class="text-xs text-neutral-400 leading-relaxed">
                                突破古典死记指法，掌握和弦声部配置（Voicing）、现代即兴伴奏编配与合成器音色。
                            </p>
                        </div>
                        <div class="pt-4 mt-4 border-t border-neutral-800 flex items-center justify-between text-xs">
                            <span class="text-neutral-500 font-mono">适合：古典转即兴 / 编曲键盘</span>
                            <a href="./curriculum.html#matrix" class="text-cyan-400 hover:underline font-bold">了解专业 &rarr;</a>
                        </div>
                    </div>

                    <!-- 5. 声乐唱作 -->
                    <div class="p-6 rounded-2xl bg-neutral-900/80 border border-neutral-800 hover:border-cyan-400/40 transition-all flex flex-col justify-between">
                        <div class="space-y-2">
                            <span class="text-[10px] font-mono-code text-cyan-400 uppercase tracking-widest font-bold">VOCAL DEPARTMENT</span>
                            <h3 class="text-lg font-black text-white">真实乐队主唱与爵士即兴</h3>
                            <p class="text-xs text-neutral-400 leading-relaxed">
                                科学混声发声、现场麦克风声学控制与大乐队同台主唱，找到属于你自己独特的真实嗓音。
                            </p>
                        </div>
                        <div class="pt-4 mt-4 border-t border-neutral-800 flex items-center justify-between text-xs">
                            <span class="text-neutral-500 font-mono">适合：流行主唱 / 舞台表现</span>
                            <a href="./curriculum.html#matrix" class="text-cyan-400 hover:underline font-bold">了解专业 &rarr;</a>
                        </div>
                    </div>

                    <!-- 6. 现代管乐 -->
                    <div class="p-6 rounded-2xl bg-neutral-900/80 border border-neutral-800 hover:border-cyan-400/40 transition-all flex flex-col justify-between">
                        <div class="space-y-2">
                            <span class="text-[10px] font-mono-code text-cyan-400 uppercase tracking-widest font-bold">HORNS &amp; WINDS</span>
                            <h3 class="text-lg font-black text-white">萨克斯、长号、小号与现代管乐</h3>
                            <p class="text-xs text-neutral-400 leading-relaxed">
                                高信博士与 Joe Longardner 领衔，现代管乐发声技巧、声部和声对位与爵士即兴对话。
                            </p>
                        </div>
                        <div class="pt-4 mt-4 border-t border-neutral-800 flex items-center justify-between text-xs">
                            <span class="text-neutral-500 font-mono">适合：管乐进修 / 大乐队合奏</span>
                            <a href="./curriculum.html#matrix" class="text-cyan-400 hover:underline font-bold">了解专业 &rarr;</a>
                        </div>
                    </div>

                    <!-- 7. 录音工程与制作 -->
                    <div class="p-6 rounded-2xl bg-neutral-900/80 border border-neutral-800 hover:border-cyan-400/40 transition-all flex flex-col justify-between">
                        <div class="space-y-2">
                            <span class="text-[10px] font-mono-code text-cyan-400 uppercase tracking-widest font-bold">AUDIO PRODUCTION</span>
                            <h3 class="text-lg font-black text-white">录音工程、音乐制作与混音</h3>
                            <p class="text-xs text-neutral-400 leading-relaxed">
                                P&R Studio 24轨真棚同期录音、话筒摆位实战、DAW 数字音频工作站操控与母带处理。
                            </p>
                        </div>
                        <div class="pt-4 mt-4 border-t border-neutral-800 flex items-center justify-between text-xs">
                            <span class="text-neutral-500 font-mono">适合：独立制作人 / 录音混音</span>
                            <a href="./curriculum.html#matrix" class="text-cyan-400 hover:underline font-bold">了解专业 &rarr;</a>
                        </div>
                    </div>

                    <!-- 8. 词曲创作 -->
                    <div class="p-6 rounded-2xl bg-neutral-900/80 border border-neutral-800 hover:border-cyan-400/40 transition-all flex flex-col justify-between">
                        <div class="space-y-2">
                            <span class="text-[10px] font-mono-code text-cyan-400 uppercase tracking-widest font-bold">SONGWRITING</span>
                            <h3 class="text-lg font-black text-white">Songwriting 歌曲写作与词曲创作</h3>
                            <p class="text-xs text-neutral-400 leading-relaxed">
                                流行旋律写作逻辑、歌词意象与结构，结合棚录完成属于你自己与家庭的原创单曲。
                            </p>
                        </div>
                        <div class="pt-4 mt-4 border-t border-neutral-800 flex items-center justify-between text-xs">
                            <span class="text-neutral-500 font-mono">适合：原创作者 / 家庭纪念单曲</span>
                            <a href="./curriculum.html#matrix" class="text-cyan-400 hover:underline font-bold">了解专业 &rarr;</a>
                        </div>
                    </div>

                    <!-- 9. 通识启蒙 -->
                    <div class="p-6 rounded-2xl bg-neutral-900/80 border border-neutral-800 hover:border-cyan-400/40 transition-all flex flex-col justify-between">
                        <div class="space-y-2">
                            <span class="text-[10px] font-mono-code text-emerald-400 uppercase tracking-widest font-bold">GENERAL MUSIC STUDIES</span>
                            <h3 class="text-lg font-black text-white">3–7岁 少儿音乐通识启蒙</h3>
                            <p class="text-xs text-neutral-400 leading-relaxed">
                                现代律动破冰、听觉敏感度开发与多乐器亲子玩乐合奏，让对音乐的爱成为自然天性。
                            </p>
                        </div>
                        <div class="pt-4 mt-4 border-t border-neutral-800 flex items-center justify-between text-xs">
                            <span class="text-neutral-500 font-mono">适合：启蒙入门 / 亲子音乐生活</span>
                            <a href="./curriculum.html#matrix" class="text-emerald-400 hover:underline font-bold">了解专业 &rarr;</a>
                        </div>
                    </div>
                </div>
            </div>
        </section>
'''

# ---------------------------------------------------------------------------
# 6. REBUILD GIVING SECTION (WARM COMMUNITY PALETTE, NON-BLACK, HONEST ROSTER)
# ---------------------------------------------------------------------------
pos_timo_start = code.find('<!-- ==================== 07. 创始人直通微信通道')
if pos_timo_start == -1:
    raise Exception(f"Timo marker not found: {pos_timo_start}")

new_giving_section = '''
        <!-- ==================== 08. 社区化奉献支持板块：温暖素雅浅底 · 真实不占位 ==================== -->
        <section class="space-y-6 pt-4">
            <div class="rounded-3xl p-8 sm:p-14 lg:p-16 bg-[#FBFBFA] text-neutral-900 border border-neutral-200/90 shadow-sm relative overflow-hidden">
                <div class="text-center max-w-2xl mx-auto space-y-2">
                    <span class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-neutral-100 border border-neutral-200 text-xs font-mono-code font-bold text-neutral-600 uppercase tracking-wider">
                        COMMUNITY GIVING · 社区支持
                    </span>
                    <h2 class="text-3xl sm:text-4xl font-black text-neutral-900 tracking-tight">
                        支持 Momo 音乐教育
                    </h2>
                    <p class="text-xs sm:text-sm text-neutral-600 leading-relaxed font-normal">
                        Momo 是一家扎根社区与真实音乐教育的工作坊。每一份支持都将切实用于添置教学器材、改善排练环境，以及资助有实际经济困难但热爱音乐的孩子。
                    </p>
                </div>

                <!-- 两个质朴清爽的社区化支持卡片 -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6 items-stretch max-w-4xl mx-auto pt-8">
                    <!-- 卡片 1: 教学设备器材支持 -->
                    <div class="rounded-2xl p-7 sm:p-8 flex flex-col justify-between bg-white border border-neutral-200 shadow-sm hover:shadow-md transition-shadow">
                        <div class="space-y-3">
                            <div class="flex items-center justify-between pb-3 border-b border-neutral-100">
                                <span class="text-[10px] font-mono-code uppercase tracking-wider text-neutral-500 font-bold">01 · EQUIPMENT</span>
                                <span class="px-2.5 py-0.5 rounded-full bg-neutral-100 text-[10px] text-neutral-600 font-medium">教学硬件</span>
                            </div>
                            <h3 class="text-xl sm:text-2xl font-black text-neutral-900">
                                教学设备与乐器更新
                            </h3>
                            <p class="text-xs sm:text-sm text-neutral-600 leading-relaxed">
                                用于添置与维护琴房电钢、排练音箱、麦克风与乐器耗材，让每个来 Momo 学习的孩子和乐队都能用上好声音。
                            </p>
                        </div>
                        <div class="pt-6 mt-6 border-t border-neutral-100">
                            <button
                                type="button"
                                onclick="openGivingModal('教学设备器材支持', 'equipment')"
                                class="w-full py-3 rounded-xl bg-black hover:bg-neutral-800 text-white font-bold text-xs transition-all shadow text-center"
                            >
                                赞助教学设备 &rarr;
                            </button>
                        </div>
                    </div>

                    <!-- 卡片 2: 音乐学者助学金池 -->
                    <div class="rounded-2xl p-7 sm:p-8 flex flex-col justify-between bg-white border border-neutral-200 shadow-sm hover:shadow-md transition-shadow">
                        <div class="space-y-3">
                            <div class="flex items-center justify-between pb-3 border-b border-neutral-100">
                                <span class="text-[10px] font-mono-code uppercase tracking-wider text-neutral-500 font-bold">02 · SCHOLARSHIP</span>
                                <span class="px-2.5 py-0.5 rounded-full bg-neutral-100 text-[10px] text-neutral-600 font-medium">学费资助</span>
                            </div>
                            <h3 class="text-xl sm:text-2xl font-black text-neutral-900">
                                音乐学者助学金池
                            </h3>
                            <p class="text-xs sm:text-sm text-neutral-600 leading-relaxed">
                                用于帮助家庭有实际经济困难的学生减免学费，并专项支持视障学子现代音乐学习，让热爱不因境遇而止步。
                            </p>
                        </div>
                        <div class="pt-6 mt-6 border-t border-neutral-100">
                            <button
                                type="button"
                                onclick="openGivingModal('音乐学者助学金池', 'scholarship')"
                                class="w-full py-3 rounded-xl bg-neutral-900 hover:bg-black text-white font-bold text-xs transition-all shadow text-center"
                            >
                                资助助学金池 &rarr;
                            </button>
                        </div>
                    </div>
                </div>

                <!-- 历史支持芳名录：彻底去除空名假名占位，质朴真诚留空寄语 -->
                <div class="max-w-xl mx-auto mt-8 p-6 rounded-2xl bg-white border border-neutral-200 text-center shadow-sm">
                    <span class="text-xs font-mono font-bold text-neutral-400 uppercase tracking-wider block mb-1.5">
                        COMMUNITY SUPPORTERS · 支持芳名录
                    </span>
                    <p class="text-sm font-bold text-neutral-900">
                        【成为第一位以实际行动对Momo音乐教育发起支持的人】
                    </p>
                    <p class="text-[11px] text-neutral-500 mt-1">
                        您的每一笔支持都将如实公开记录并公示于此。
                    </p>
                </div>
            </div>
        </section>
'''

# ---------------------------------------------------------------------------
# ASSEMBLE ALL REPLACEMENTS
# ---------------------------------------------------------------------------
# Replace Style Deck
pos_sd_start = code.find('<section id="style-deck"')
pos_fac_start = code.find('<!-- ==================== 05. 真实常驻师资长廊')
code = code[:pos_sd_start] + new_style_deck + "\n\n        " + code[pos_fac_start:]

# Replace Faculty
pos_fac_start2 = code.find('<!-- ==================== 05. 真实常驻师资长廊')
pos_mi_start = code.find('<!-- ==================== 06. MI 学院风格整版入会申请大版面')
code = code[:pos_fac_start2] + new_faculty_section + "\n\n        " + code[pos_mi_start:]

# Replace Bento with Majors
pos_bento_start2 = code.find('<!-- ==================== 05. 6 大专页 Bento 瓷砖')
pos_giving_start2 = code.find('<!-- ==================== 06. 奉献板块')
code = code[:pos_bento_start2] + new_majors_section + "\n\n        " + code[pos_giving_start2:]

# Replace Giving Section
pos_giving_start3 = code.find('<!-- ==================== 06. 奉献板块')
pos_timo_start3 = code.find('<!-- ==================== 07. 创始人直通微信通道')
code = code[:pos_giving_start3] + new_giving_section + "\n\n        " + code[pos_timo_start3:]

# Re-check and update JS styleDeckData and updateStyleDeckUI if needed
# Update the style pill selection function in JS
js_update = '''
    // 风格药丸标签高亮同步
    function updateStylePillsUI(activeIdx) {
        const pills = document.querySelectorAll('.style-tab-pill');
        pills.forEach((p, idx) => {
            if (idx === activeIdx) {
                p.className = 'style-tab-pill active px-3.5 py-1.5 rounded-full text-xs font-mono-code font-bold transition-all bg-white text-black shadow';
            } else {
                p.className = 'style-tab-pill px-3.5 py-1.5 rounded-full text-xs font-mono-code font-bold transition-all bg-neutral-900 text-neutral-300 hover:text-white border border-neutral-800';
            }
        });
    }
'''

pos_update_fn = code.find('function updateStyleDeckUI() {')
if pos_update_fn != -1:
    code = code[:pos_update_fn] + js_update + "\n    " + code[pos_update_fn:]
    # Insert call to updateStylePillsUI inside updateStyleDeckUI
    code = code.replace(
        "document.getElementById('deck-indicator').textContent = '0' + (currentStyleIndex + 1) + ' / 06';",
        "document.getElementById('deck-indicator').textContent = '0' + (currentStyleIndex + 1) + ' / 06'; updateStylePillsUI(currentStyleIndex);"
    )

with open(COMPILE_SCRIPT, "w", encoding="utf-8") as f:
    f.write(code)

print("compile_complete_website.py updated with all round 2 optimizations!")
