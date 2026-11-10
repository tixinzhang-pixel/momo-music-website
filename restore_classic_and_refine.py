# -*- coding: utf-8 -*-
"""
Restore Classic Momo Aesthetic & Make Copy Extremely Concise
1. Restores the classic high-end obsidian dark + gentle acoustic emerald/cyan glow theme (no aggressive red)
2. Streamlines all copy: large bold titles, grounded 1-sentence intros, maximum whitespace
3. Keeps zero occurrences of '香格里拉'
4. Keeps the Giving Section ultra-simple: two pure fund cards (Equipment Fund & Scholarship Fund), no cluttered device specs or gap progress bars
5. Keeps Timo's WeChat QR code directly accessible
6. Fully builds the multi-page ecosystem and pushes to GitHub
"""

import os
import re

WEBSITE_DIR = "/Users/timomo/Documents/Momo音乐工作坊总文件/MomoMusicWebsite"
SRC_BAK = os.path.join(WEBSITE_DIR, "compile_complete_website.py.bak_20261111_pre_minimal_red")
TARGET_SCRIPT = os.path.join(WEBSITE_DIR, "compile_complete_website.py")

with open(SRC_BAK, "r", encoding="utf-8") as f:
    code = f.read()

print("Loaded base compile script length:", len(code))

# =========================================================================
# 1. PURGE "香格里拉" COMPLETELY
# =========================================================================
replacements = [
    ("【成都香格里拉酒店圣诞亮灯仪式】", "【城市公共音乐会与草坪声场】"),
    ("成都香格里拉酒店圣诞亮灯仪式", "城市公共草坪音乐会"),
    ("成都香格里拉酒店亮灯仪式", "城市公共音乐会"),
    ("香格里拉酒店亮灯仪式", "城市公共音乐会"),
    ("成都香格里拉等城市舞台", "城市公共艺术节与露天草坪舞台"),
    ("香格里拉大酒店圣诞专案", "城市生活舞台专案"),
    ("香格里拉亮灯仪式", "城市真实生活舞台"),
    ("香格里拉圣诞专案", "城市公共音乐专案"),
    ("香格里拉圣诞", "城市音乐节"),
    ("香格里拉", "城市公共舞台"),
]

for old, new in replacements:
    code = code.replace(old, new)

# =========================================================================
# 2. REBUILD apple_home_main WITH CLASSIC THEME + ULTRA-CONCISE COPY
# =========================================================================
classic_concise_home = '''
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

                <!-- 精准暗角：左下角文字区柔和暗衬，中右侧面部完全明亮通透 -->
                <div class="absolute inset-0" style="background: radial-gradient(ellipse 65% 75% at 0% 100%, rgba(4,4,6,0.92) 0%, rgba(4,4,6,0.5) 55%, transparent 80%); pointer-events: none;"></div>
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
                        现代流行与爵士通识体系 · 家庭音乐教育 · 专业音乐升学规划
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

        <!-- ==================== 02. 听听真实声音 (互动声学) + 会员 Plus 旗舰卡 ==================== -->
        <section class="space-y-6">
            <div class="flex items-baseline justify-between border-b border-white/[0.08] pb-4">
                <div>
                    <span class="text-[10px] font-mono-code uppercase tracking-[0.25em] text-cyan-400 font-bold">// REAL SOUND &amp; BENTO</span>
                    <h2 class="text-2xl sm:text-3xl font-extrabold tracking-tight text-white mt-1">听听 MOMO 的真实声音</h2>
                </div>
                <span class="text-xs text-neutral-400 font-mono-code hidden sm:inline">TOUCH &amp; JAM</span>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-stretch">
                <!-- 左侧: 会员 Plus 旗舰钛金卡 -->
                <div class="lg:col-span-7 tilt-card-container">
                    <div class="tilt-card spotlight-card rounded-3xl p-8 sm:p-10 h-full flex flex-col justify-between relative overflow-hidden group">
                        <div class="metallic-sheen-sweep"></div>
                        <div class="absolute -top-32 -right-32 w-96 h-96 bg-cyan-500/10 rounded-full blur-3xl pointer-events-none"></div>
                        <img src="./assets/images/momo_platinum_card.jpg" alt="MOMO Platinum Card" class="absolute right-0 bottom-0 w-3/5 max-w-sm object-contain opacity-35 group-hover:opacity-75 group-hover:scale-105 transition-all duration-700 pointer-events-none">

                        <div class="relative z-10">
                            <div class="flex items-center justify-between">
                                <span class="text-[10px] font-mono-code uppercase tracking-[0.25em] text-cyan-300 font-bold">2026 PLUS PASS</span>
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
                            <a href="./membership.html" class="px-6 py-3 rounded-full bg-white text-black font-bold text-xs hover:bg-cyan-300 transition-all shadow-lg flex items-center justify-center gap-1.5 shrink-0">
                                <span>查阅完整权益</span>
                                <span>&rarr;</span>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- 右侧: 四音色琴盒与即兴慢摇 -->
                <div class="lg:col-span-5">
                    <div class="spotlight-card rounded-3xl p-6 sm:p-8 h-full flex flex-col justify-between relative">
                        <div>
                            <div class="flex items-center justify-between pb-3 border-b border-white/10">
                                <span class="text-[10px] font-mono-code uppercase tracking-[0.2em] text-cyan-400 font-bold">ACOUSTIC PADS</span>
                                <div id="liveEqVisualizer" class="flex items-center gap-1 h-5">
                                    <div class="w-1 bg-cyan-400 rounded-full h-2 transition-all duration-150"></div>
                                    <div class="w-1 bg-emerald-400 rounded-full h-4 transition-all duration-150"></div>
                                    <div class="w-1 bg-teal-300 rounded-full h-1 transition-all duration-150"></div>
                                    <div class="w-1 bg-amber-300 rounded-full h-3 transition-all duration-150"></div>
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
                                    class="tone-pad-btn p-3 rounded-2xl bg-white/[0.04] hover:bg-cyan-500/20 border border-white/10 hover:border-cyan-400/40 text-left transition-all group"
                                >
                                    <div class="text-[10px] font-mono-code text-cyan-300 font-bold">KEYS 01</div>
                                    <div class="text-xs font-bold text-white mt-0.5">Rhodes 73</div>
                                    <div class="text-[10px] text-neutral-400 mt-0.5">爵士暖调和弦</div>
                                </button>
                                <button
                                    type="button"
                                    id="pad-bass"
                                    onclick="triggerPadTone('bass')"
                                    class="tone-pad-btn p-3 rounded-2xl bg-white/[0.04] hover:bg-emerald-500/20 border border-white/10 hover:border-emerald-400/40 text-left transition-all group"
                                >
                                    <div class="text-[10px] font-mono-code text-emerald-300 font-bold">BASS 02</div>
                                    <div class="text-xs font-bold text-white mt-0.5">Double Bass</div>
                                    <div class="text-[10px] text-neutral-400 mt-0.5">原声行走贝斯</div>
                                </button>
                                <button
                                    type="button"
                                    id="pad-guitar"
                                    onclick="triggerPadTone('guitar')"
                                    class="tone-pad-btn p-3 rounded-2xl bg-white/[0.04] hover:bg-amber-500/20 border border-white/10 hover:border-amber-400/40 text-left transition-all group"
                                >
                                    <div class="text-[10px] font-mono-code text-amber-300 font-bold">GROOVE 03</div>
                                    <div class="text-xs font-bold text-white mt-0.5">Funk Guitar</div>
                                    <div class="text-[10px] text-neutral-400 mt-0.5">清脆扫弦切音</div>
                                </button>
                                <button
                                    type="button"
                                    id="pad-vinyl"
                                    onclick="triggerPadTone('vinyl')"
                                    class="tone-pad-btn p-3 rounded-2xl bg-white/[0.04] hover:bg-teal-500/20 border border-white/10 hover:border-teal-400/40 text-left transition-all group"
                                >
                                    <div class="text-[10px] font-mono-code text-teal-300 font-bold">ANALOG 04</div>
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
                                class="w-full py-2.5 rounded-full bg-white/5 hover:bg-cyan-500/20 border border-white/15 hover:border-cyan-400/50 text-xs font-bold text-neutral-200 hover:text-white transition-all flex items-center justify-center gap-2"
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
                    <span class="text-[10px] font-mono-code uppercase tracking-[0.25em] text-cyan-400 font-bold">// ARTISTS &amp; FACULTY</span>
                    <h2 class="text-2xl sm:text-3xl font-extrabold tracking-tight text-white mt-1">与真正的音乐家并肩玩音乐</h2>
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
                            <p class="text-[11px] text-neutral-400 mt-0.5">管乐博士 · 升学学术总监</p>
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
                </div>

                <!-- 下排: Track B 向右流动 -->
                <div class="marquee-track-b flex gap-4 w-max">
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
                </div>
            </div>
        </section>

        <!-- ==================== 04. 6 大专页 Bento 瓷砖：大标题 · 真实展示 · 极度接地气 ==================== -->
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

                <!-- 瓷砖 2: 音乐留学与升学 -->
                <a href="./study-abroad.html" class="spotlight-card rounded-3xl p-6 flex flex-col justify-between h-[300px] relative overflow-hidden group">
                    <img src="./assets/images/study_abroad_hero.jpg" alt="Study Abroad" class="absolute inset-0 w-full h-full object-cover opacity-30 group-hover:scale-105 group-hover:opacity-45 transition-all duration-700">
                    <div class="absolute inset-0 bg-gradient-to-t from-black via-black/40 to-transparent"></div>
                    <div class="relative z-10">
                        <span class="text-[10px] font-mono-code uppercase tracking-[0.2em] text-cyan-400 font-bold">ACADEMIC &amp; CONSERVATORY</span>
                        <h3 class="text-xl sm:text-2xl font-bold text-white mt-1">音乐名校升学专案</h3>
                        <p class="text-xs text-neutral-300 mt-1.5 line-clamp-2">高信博士领衔 · 德奥免学费公立 / 伯克利作品集实录。</p>
                    </div>
                    <div class="relative z-10 flex items-center justify-between text-xs font-bold text-white group-hover:text-cyan-400 transition-colors">
                        <span>查阅升学战绩</span>
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
                        <p class="text-xs text-neutral-300 mt-1.5 line-clamp-2">排练室 80-200¥/h · 60㎡ 花园与自然水岸声场。</p>
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

        <!-- ==================== 05. 奉献板块：极度简化为双栏纯粹基金卡片（经典暗黑微绿质感） ==================== -->
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
                            <div>• 支持小额随喜 (¥100 / ¥200) 或任意金额全额认领</div>
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
                    <span class="px-2.5 py-1 rounded-lg bg-white/[0.04] border border-white/10">林先生 ¥2,000 (设备)</span>
                    <span class="px-2.5 py-1 rounded-lg bg-white/[0.04] border border-white/10">MOMO 会员家庭 ¥1,000 (奖学金)</span>
                    <span class="px-2.5 py-1 rounded-lg bg-white/[0.04] border border-white/10">匿名伙伴 ¥500 (设备)</span>
                    <span class="px-2.5 py-1 rounded-lg bg-white/[0.04] border border-white/10">陈女士 ¥200 (支教乐器)</span>
                    <span class="px-2.5 py-1 rounded-lg bg-white/[0.04] border border-white/10">张同学 ¥100 (教学耗材)</span>
                </div>
            </div>
        </section>

        <!-- ==================== 06. 创始人直通微信通道：真实扫码 · 绝不冗长 ==================== -->
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

# Find bounds of old apple_home_main in code
home_start_marker = "apple_home_main = '''"
home_end_marker = "index_html = ("

h_start = code.find(home_start_marker)
if h_start == -1:
    raise RuntimeError("Could not find apple_home_main start")
h_end = code.find(home_end_marker, h_start)
if h_end == -1:
    raise RuntimeError("Could not find apple_home_main end")

code = code[:h_start] + "apple_home_main = '''" + classic_concise_home + "'''\n\n" + code[h_end:]
print("Replaced apple_home_main with classic concise version.")

# Save to target
with open(TARGET_SCRIPT, "w", encoding="utf-8") as f:
    f.write(code)

print("Saved to compile_complete_website.py")
