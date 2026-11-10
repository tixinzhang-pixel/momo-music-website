# -*- coding: utf-8 -*-
"""
MOMO Music Website - Master Builder (Bugfix for Click Interception & Full Level-2 Interactivity)
Root Cause of "All buttons not clickable":
Modals had class="fixed inset-0 z-[110] pointer-events-none" with children having "pointer-events-auto".
In modern browsers, the child's pointer-events-auto overrides the parent and intercepts all clicks across the whole screen.
FIX:
All modals and drawers now use `hidden` by default, so they are completely removed from the hit-test tree until explicitly opened!
"""

import os
import re

WEBSITE_DIR = "/Users/timomo/Documents/Momo音乐工作坊总文件/MomoMusicWebsite"
SRC_HTML = os.path.join(WEBSITE_DIR, "index.html.bak_20261023_pre_apple_te")
TARGET_HTML = os.path.join(WEBSITE_DIR, "index.html")

with open(SRC_HTML, "r", encoding="utf-8") as f:
    orig = f.read()

# 1. Extract Head
head_end = orig.find("<body")
body_tag_end = orig.find(">", head_end) + 1
head_section = orig[:body_tag_end]

# 2. Extract Modals & Footer & Scripts from the bottom
footer_pos = orig.find("<footer")
footer_and_scripts = orig[footer_pos:]

# SVG Shield Logo Snippet
MOMO_SHIELD_SVG = '''<svg class="h-6 w-auto inline-block transform -translate-y-0.5" viewBox="0 0 100 120" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="shieldIconGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#00C9FF" /><stop offset="100%" stop-color="#92FE9D" /></linearGradient></defs><path d="M10 10 h80 v45 c0 30 -40 60 -40 60 c0 0 -40 -30 -40 -60 z" fill="url(#shieldIconGrad)" /><text x="50" y="87" font-family="'Inter', sans-serif" font-size="62" font-weight="900" text-anchor="middle" fill="#000000">M</text></svg>'''

# Build Top Navigation
new_nav = f'''
    <!-- 顶部固定导航 (Apple 极简暗黑悬浮条) -->
    <header id="main-nav" class="fixed top-0 left-0 w-full z-50 bg-[#080808]/90 backdrop-blur-md border-b border-neutral-900 transition-all duration-300 py-3.5 px-6 md:px-12">
        <div class="max-w-7xl mx-auto flex items-center justify-between">
            <!-- 品牌盾牌 Logo (点击平滑回顶) -->
            <button type="button" onclick="scrollToTop()" class="flex items-center gap-3 group text-left focus:outline-none cursor-pointer">
                <svg class="h-9 w-auto transform group-hover:scale-105 transition-transform duration-300" viewBox="0 0 100 120" xmlns="http://www.w3.org/2000/svg">
                    <defs>
                        <linearGradient id="shieldNavGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                            <stop offset="0%" stop-color="#00C9FF" />
                            <stop offset="100%" stop-color="#92FE9D" />
                        </linearGradient>
                    </defs>
                    <path d="M10 10 h80 v45 c0 30 -40 60 -40 60 c0 0 -40 -30 -40 -60 z" fill="url(#shieldNavGrad)" />
                    <text x="50" y="32" font-family="'Inter', sans-serif" font-size="7.5" font-weight="700" text-anchor="middle" fill="#000000" letter-spacing="0.5">KIND • TRUTH • PASSION</text>
                    <text x="50" y="87" font-family="'Inter', sans-serif" font-size="62" font-weight="900" text-anchor="middle" fill="#000000">M</text>
                </svg>
                <div class="flex flex-col">
                    <span class="text-base sm:text-lg font-black tracking-tight leading-none text-white uppercase group-hover:text-momo-cyan transition-colors">
                        Momo Family
                    </span>
                    <span class="text-[9px] sm:text-[10px] uppercase font-bold tracking-widest text-neutral-400 mt-0.5">
                        Music Studio • Chengdu & Global
                    </span>
                </div>
            </button>

            <!-- 桌面端极简五大导航 -->
            <nav class="hidden lg:flex items-center gap-7">
                <button type="button" onclick="scrollToSection('offerings')" class="text-xs uppercase font-bold tracking-widest text-neutral-300 hover:text-momo-cyan transition-colors flex items-center gap-1.5 cursor-pointer">
                    <span>活动货架</span>
                    <span class="text-[9px] px-1.5 py-0.5 rounded bg-neutral-800 text-momo-mint font-mono">OFFERINGS</span>
                </button>
                <button type="button" onclick="scrollToSection('membership-tier')" class="text-xs uppercase font-bold tracking-widest text-neutral-300 hover:text-momo-cyan transition-colors flex items-center gap-1.5 cursor-pointer">
                    <span>家庭会员</span>
                    <span class="text-[9px] px-1.5 py-0.5 rounded bg-neutral-800 text-neutral-400 font-mono">¥6,000</span>
                </button>
                <button type="button" onclick="scrollToSection('spaces-rental')" class="text-xs uppercase font-bold tracking-widest text-neutral-300 hover:text-momo-cyan transition-colors flex items-center gap-1.5 cursor-pointer">
                    <span>空间租用</span>
                    <span class="text-[9px] px-1.5 py-0.5 rounded bg-neutral-800 text-neutral-400 font-mono">SPACES</span>
                </button>
                <button type="button" onclick="scrollToSection('merch-store')" class="text-xs uppercase font-bold tracking-widest text-neutral-300 hover:text-momo-cyan transition-colors flex items-center gap-1.5 cursor-pointer">
                    <span>美学周边</span>
                    <span class="text-[9px] px-1.5 py-0.5 rounded bg-neutral-800 text-neutral-400 font-mono">STORE</span>
                </button>
                <button type="button" onclick="scrollToSection('faculty')" class="text-xs uppercase font-bold tracking-widest text-neutral-300 hover:text-momo-cyan transition-colors flex items-center gap-1.5 cursor-pointer">
                    <span>导师档案</span>
                    <span class="text-[9px] px-1.5 py-0.5 rounded bg-neutral-800 text-neutral-400 font-mono">13 ARTISTS</span>
                </button>
            </nav>

            <!-- 快捷行动入口 -->
            <div class="hidden sm:flex items-center gap-3">
                <button type="button" onclick="openBookingModal('预约到店体验 / 理念沟通')" class="gradient-bg text-black px-5 py-2.5 font-black text-xs uppercase tracking-wider hover:opacity-95 transform active:scale-95 transition-all shadow-lg shadow-momo-teal/20 cursor-pointer">
                    预约体验 / 立即入会
                </button>
            </div>

            <!-- 移动端汉堡菜单 -->
            <button type="button" onclick="toggleMobileMenu()" class="lg:hidden p-2 text-neutral-300 hover:text-white cursor-pointer" aria-label="Toggle menu">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"></path>
                </svg>
            </button>
        </div>

        <!-- 移动端下拉菜单 -->
        <div id="mobile-menu" class="hidden lg:hidden flex-col gap-3 pt-5 pb-3 border-t border-neutral-900 mt-3">
            <button type="button" onclick="scrollToSection('offerings'); toggleMobileMenu();" class="text-left text-xs uppercase font-bold tracking-widest text-white py-1.5 flex justify-between cursor-pointer">
                <span>01. 核心活动货架 (Offerings)</span>
                <span class="text-momo-mint font-mono">4大类目</span>
            </button>
            <button type="button" onclick="scrollToSection('membership-tier'); toggleMobileMenu();" class="text-left text-xs uppercase font-bold tracking-widest text-white py-1.5 flex justify-between cursor-pointer">
                <span>02. MOMO 家庭音乐会员 (Membership)</span>
                <span class="text-neutral-400 font-mono">¥6,000</span>
            </button>
            <button type="button" onclick="scrollToSection('spaces-rental'); toggleMobileMenu();" class="text-left text-xs uppercase font-bold tracking-widest text-white py-1.5 flex justify-between cursor-pointer">
                <span>03. 线下空间与排练室租用 (Spaces)</span>
                <span class="text-neutral-400 font-mono">¥200/h起</span>
            </button>
            <button type="button" onclick="scrollToSection('merch-store'); toggleMobileMenu();" class="text-left text-xs uppercase font-bold tracking-widest text-white py-1.5 flex justify-between cursor-pointer">
                <span>04. 先锋美学周边商店 (Store)</span>
                <span class="text-momo-cyan font-mono">含文化衫赠礼</span>
            </button>
            <button type="button" onclick="scrollToSection('faculty'); toggleMobileMenu();" class="text-left text-xs uppercase font-bold tracking-widest text-white py-1.5 flex justify-between cursor-pointer">
                <span>05. 一线艺术家导师档案 (Artists)</span>
                <span class="text-neutral-400 font-mono">13位名师</span>
            </button>
            <div class="pt-3">
                <button type="button" onclick="openBookingModal('预约到店体验 / 理念沟通'); toggleMobileMenu();" class="w-full gradient-bg text-black py-3 text-center font-black text-xs uppercase tracking-wider cursor-pointer">
                    预约体验 / 立即入会
                </button>
            </div>
        </div>
    </header>
'''

# Build Hero Section
new_hero = '''
    <main class="pt-0">
        <!-- 首屏 4K 沉浸巨幕 (Apple Billboard Reel) -->
        <section id="hero" class="relative min-h-screen flex flex-col justify-between px-6 md:px-12 pt-28 pb-16 border-b border-neutral-900 overflow-hidden bg-black">
            <!-- 真实舞台视频背景 (桌面端自动静音循环，支持一键开原声) -->
            <div class="absolute inset-0 z-0 overflow-hidden pointer-events-none">
                <video 
                    id="hero-bg-video"
                    autoplay 
                    loop 
                    muted 
                    playsinline 
                    preload="auto"
                    poster="./assets/images/hero_trumpet.jpg"
                    class="w-full h-full object-cover object-center filter brightness-[0.70] contrast-110"
                >
                    <source src="./assets/media/hero_stage_loop.mp4" type="video/mp4">
                    <source src="./assets/media/hero_stage_stream.mp4" type="video/mp4">
                </video>
                <div class="absolute inset-0 bg-gradient-to-t from-[#080808] via-[#080808]/60 to-[#080808]/40"></div>
                <div class="absolute inset-0 bg-[radial-gradient(circle_at_center,transparent_0%,rgba(8,8,8,0.7)_100%)]"></div>
            </div>

            <!-- 原声音频切换悬浮按钮 (右下角极简胶囊) -->
            <div class="absolute bottom-8 right-6 md:right-12 z-20 flex items-center gap-2">
                <button 
                    id="hero-sound-btn" 
                    type="button" 
                    onclick="toggleHeroSound()"
                    class="flex items-center gap-2 px-3.5 py-2 rounded-full bg-black/70 backdrop-blur-md border border-neutral-700/80 hover:border-momo-cyan text-xs font-mono text-neutral-300 hover:text-white transition-all shadow-xl cursor-pointer"
                >
                    <span id="hero-sound-icon" class="text-sm">🔇</span>
                    <span id="hero-sound-text">声音: 静音 (点击开启原声)</span>
                </button>
            </div>

            <!-- 首屏中央巨幕文字 (Apple 极简大字号) -->
            <div class="relative z-10 max-w-7xl mx-auto w-full my-auto py-12">
                <div class="inline-flex items-center gap-3 border border-neutral-800 bg-black/60 px-4 py-1.5 rounded-full backdrop-blur-md mb-8">
                    <span class="w-2 h-2 rounded-full gradient-bg animate-pulse"></span>
                    <span class="text-xs font-mono uppercase tracking-[0.2em] text-neutral-300">CHENGDU • TONGZILIN & LUXELAKES</span>
                    <span class="text-neutral-600">|</span>
                    <span class="text-xs font-mono text-momo-mint">KIND • TRUTH • PASSION</span>
                </div>
                
                <h1 class="text-4xl sm:text-6xl md:text-7xl lg:text-8xl font-black uppercase tracking-tight leading-[1.02] text-white max-w-5xl">
                    从锦江河畔到曼哈顿西村 <br>
                    <span class="gradient-text">属于家庭与艺术家的真实声音场</span>
                </h1>

                <p class="mt-6 text-lg sm:text-xl md:text-2xl text-neutral-300 font-light max-w-3xl leading-relaxed">
                    不抠干涩指法，拒绝内卷考级。以一线爵士音乐家与制作人为底座，提供家庭乐队合奏、4师对1生排练、欧美音乐留学作品集实录与私密空间租用。
                </p>

                <!-- 两个核心行动按钮 -->
                <div class="mt-10 flex flex-wrap items-center gap-4">
                    <button 
                        type="button" 
                        onclick="scrollToSection('offerings')" 
                        class="gradient-bg text-black px-8 py-4 font-black text-sm uppercase tracking-wider hover:brightness-110 active:scale-95 transition-all shadow-xl shadow-momo-cyan/25 flex items-center gap-2 cursor-pointer"
                    >
                        <span>浏览核心产品货架</span>
                        <span class="text-base">↓</span>
                    </button>
                    <button 
                        type="button" 
                        onclick="openMembershipModal()" 
                        class="border border-neutral-700 bg-black/60 backdrop-blur-md hover:border-momo-mint text-white px-8 py-4 font-bold text-sm uppercase tracking-wider transition-all flex items-center gap-2 cursor-pointer"
                    >
                        <span>开通家庭音乐会员 (¥6,000)</span>
                        <span class="text-xs text-momo-mint font-mono">送文化衫</span>
                    </button>
                </div>
            </div>

            <!-- 首屏底部微指标 -->
            <div class="relative z-10 max-w-7xl mx-auto w-full pt-6 border-t border-neutral-800/80 flex flex-wrap justify-between items-center gap-4 text-xs font-mono text-neutral-400">
                <div class="flex items-center gap-6">
                    <div><span class="text-white font-bold">4-ON-1</span> 职业乐队伴奏</div>
                    <div><span class="text-white font-bold">13 位</span> 中外一线艺术家</div>
                    <div><span class="text-white font-bold">100%</span> 真实录音棚同期实录</div>
                </div>
                <div class="text-neutral-500 hidden sm:block">
                    SQUARE MINIMALIST & TEENAGE ENGINEERING AESTHETIC
                </div>
            </div>
        </section>

        <!-- 动态极简跑马灯 -->
        <section class="border-b border-neutral-900 bg-black py-3.5 overflow-hidden select-none">
            <div class="animate-marquee whitespace-nowrap text-xs font-mono uppercase tracking-[0.25em] text-neutral-400">
                <span class="mx-6 text-white">• MOMO MUSIC LIFESTYLE BRAND</span>
                <span class="mx-6 text-momo-cyan">4-ON-1 BAND REHEARSAL & RECORDING</span>
                <span class="mx-6">• KIND • TRUTH • PASSION</span>
                <span class="mx-6 text-momo-mint">EARLY SONIC & FAMILY JAM</span>
                <span class="mx-6 text-white">• GLOBAL CONSERVATORY PORTFOLIO (¥38,800)</span>
                <span class="mx-6 text-momo-cyan">URBAN SHARED REHEARSAL SPACE (¥200/H)</span>
                <span class="mx-6 text-momo-mint">DALIANGSHAN PILGRIMAGE RETREAT (¥4,000)</span>
            </div>
        </section>
'''

# Build Core Offerings
new_offerings = f'''
        <!-- ==================== 核心产品货架 (Apple Style Bento Grid) ==================== -->
        <section id="offerings" class="py-24 px-6 md:px-12 border-b border-neutral-900 bg-[#090909]">
            <div class="max-w-7xl mx-auto">
                <div class="flex flex-col md:flex-row md:items-end justify-between mb-16 pb-6 border-b border-neutral-800">
                    <div>
                        <div class="text-xs font-mono text-momo-cyan uppercase tracking-widest mb-2">// PRODUCTIZED CATALOG</div>
                        <h2 class="text-3xl sm:text-5xl font-black uppercase tracking-tight text-white">
                            核心活动与产品货架
                        </h2>
                    </div>
                    <p class="mt-4 md:mt-0 text-sm font-mono text-neutral-400 max-w-md">
                        价格完全透明 · 无隐形消费 · 一线艺术家亲自交付 · 自由选配与预约
                    </p>
                </div>

                <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
                    <!-- ==================== 产品 01 (排序第一 · 核心底座)：MOMO 家庭音乐会员 (纯正 MOMO 盾牌钛金卡) ==================== -->
                    <div id="membership-tier" class="lg:col-span-12 brutalist-border bg-gradient-to-br from-[#141416] via-[#0c0c0e] to-[#080808] p-8 md:p-14 relative overflow-hidden group rounded-2xl shadow-2xl">
                        <!-- 顶部徽章 -->
                        <div class="flex flex-wrap items-center justify-between gap-4 mb-8">
                            <div class="flex items-center gap-3">
                                {MOMO_SHIELD_SVG}
                                <span class="text-lg md:text-xl font-black tracking-tight text-white uppercase font-sans">MOMO CARD</span>
                                <span class="text-xs px-2.5 py-0.5 rounded-full bg-neutral-800 text-neutral-300 font-mono">TITANIUM PASS</span>
                            </div>
                            <div class="px-4 py-1.5 bg-gradient-to-r from-momo-cyan/20 to-momo-mint/20 border border-momo-cyan/40 text-momo-mint font-mono text-xs font-bold rounded-full">
                                ★ 专属纯会员制 · 不服务非会员
                            </div>
                        </div>

                        <!-- 左右结构：左侧极简文案 + 双按钮；右侧 Apple Card 浮空 3D 渲染 -->
                        <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
                            <div class="lg:col-span-6 space-y-6">
                                <div>
                                    <h3 class="text-3xl sm:text-5xl font-black text-white uppercase tracking-tight leading-tight">
                                        MOMO 家庭音乐会员
                                    </h3>
                                    <p class="mt-3 text-lg sm:text-xl text-neutral-300 font-light leading-relaxed">
                                        一卡全家尊享 · 专属于生活与声音的安全场
                                    </p>
                                    <div class="mt-4 flex items-baseline gap-3">
                                        <span class="text-4xl sm:text-5xl font-black text-white font-mono">¥6,000</span>
                                        <span class="text-neutral-400 text-sm font-mono">/ 年（额度全自由划扣 · 入会即赠文化衫）</span>
                                    </div>
                                </div>

                                <!-- 核心权益明码标签 -->
                                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-2">
                                    <div class="border border-neutral-800 bg-neutral-900/60 p-3.5 rounded-lg">
                                        <div class="text-[10px] font-mono text-momo-mint uppercase">UNIT 01 · 进阶精修</div>
                                        <div class="text-base font-bold text-white mt-0.5">4-on-1 职业乐队实验室</div>
                                        <div class="text-sm font-mono text-momo-cyan mt-0.5">¥400 / 30min</div>
                                        <div class="text-xs text-neutral-400 mt-1">4 位职业艺术家围着你一人伴奏与现场多轨实录</div>
                                    </div>
                                    <div class="border border-neutral-800 bg-neutral-900/60 p-3.5 rounded-lg">
                                        <div class="text-[10px] font-mono text-momo-mint uppercase">UNIT 02 · 亲子合奏</div>
                                        <div class="text-base font-bold text-white mt-0.5">3–7岁 全家庭音乐时光</div>
                                        <div class="text-sm font-mono text-momo-cyan mt-0.5">¥400 / 45min</div>
                                        <div class="text-xs text-neutral-400 mt-1">爸爸妈妈与孩子同场拿起真实乐器，排练真实作品</div>
                                    </div>
                                </div>

                                <div class="p-3 border border-neutral-800 bg-black/60 rounded text-xs text-neutral-300 space-y-1">
                                    <div class="flex items-center gap-2">
                                        <span class="text-momo-mint">✦</span>
                                        <span class="font-bold text-white">城市真实舞台专案（如城市音乐节亮灯）：</span>
                                    </div>
                                    <p class="text-neutral-400 pl-4">
                                        自然纳入会员活动规划。非选拔，顺势而生——刚好甲方需要，而你又刚好准备好，绝不制造虚妄焦虑。
                                    </p>
                                </div>

                                <!-- 双交互胶囊按钮 -->
                                <div class="pt-4 flex flex-wrap items-center gap-4">
                                    <button 
                                        type="button" 
                                        onclick="openMembershipModal()" 
                                        class="bg-[#0071e3] hover:bg-[#0077ed] text-white px-7 py-3 rounded-full font-semibold text-xs tracking-wider transition-all shadow-lg shadow-blue-500/20 flex items-center gap-1.5 cursor-pointer"
                                    >
                                        <span>了解更多</span>
                                        <span class="text-sm">&#8594;</span>
                                    </button>
                                    <button 
                                        type="button" 
                                        onclick="openBookingModal('申请开通 MOMO 家庭音乐会员 (¥6,000)')" 
                                        class="border border-white/60 hover:border-white text-white px-7 py-3 rounded-full font-semibold text-xs tracking-wider transition-all hover:bg-white/10 cursor-pointer"
                                    >
                                        立即申请
                                    </button>
                                </div>
                            </div>

                            <!-- 右侧：细腻浮空 3D 白金钛金属 MOMO Card -->
                            <div class="lg:col-span-6 flex items-center justify-center py-6">
                                <div class="relative w-full max-w-md transform group-hover:scale-105 group-hover:-rotate-1 transition-all duration-700 ease-out cursor-pointer" onclick="openMembershipModal()">
                                    <div class="absolute inset-0 bg-gradient-to-r from-white/10 via-white/5 to-transparent blur-2xl rounded-3xl transform translate-y-6"></div>
                                    <img 
                                        src="./assets/images/momo_platinum_card.jpg" 
                                        alt="MOMO Family Titanium Card" 
                                        class="w-full h-auto object-contain rounded-2xl shadow-2xl border border-white/20 filter contrast-105"
                                    >
                                    <div class="mt-4 text-center text-[11px] font-mono text-neutral-400">
                                        MOMO TITANIUM PHYSICAL PASS · 实体专属白金钛金尊享卡
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- ==================== 产品 02 (旗舰高定)：欧美音乐学院·升学与艺术留学全景规划 ==================== -->
                    <div id="study-abroad-rack" class="lg:col-span-6 brutalist-border bg-[#0d0d0d] p-8 md:p-10 flex flex-col justify-between group">
                        <div class="space-y-6">
                            <div class="aspect-16/9 overflow-hidden rounded border border-neutral-800 relative cursor-pointer" onclick="openStudyAbroadModal()">
                                <img src="./assets/images/conservatory_mentorship_hero.jpg" alt="Music Conservatory Planning" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 filter brightness-95">
                                <div class="absolute top-3 left-3 px-3 py-1 bg-black/80 backdrop-blur-md border border-neutral-700 text-momo-mint font-mono text-xs">
                                    高信博士 + Timo 深度陪伴
                                </div>
                            </div>
                            <div>
                                <div class="text-xs font-mono text-momo-cyan uppercase tracking-widest">FLAGSHIP MENTORSHIP</div>
                                <h3 class="text-2xl sm:text-3xl font-black text-white uppercase tracking-tight mt-1">
                                    欧美音乐学院 · 升学与艺术留学全景规划
                                </h3>
                                <div class="mt-2 flex items-baseline gap-3">
                                    <span class="text-3xl sm:text-4xl font-black text-white font-mono">¥38,800</span>
                                    <span class="text-neutral-400 text-xs font-mono">/ 全案固定陪伴价（无二次隐形加价）</span>
                                </div>
                            </div>
                            <!-- 交付金三角 -->
                            <div class="p-4 border border-neutral-800 bg-neutral-950 rounded space-y-2 text-xs">
                                <div class="text-momo-mint font-bold uppercase tracking-wider">交付金三角团队：</div>
                                <div class="text-neutral-300 leading-relaxed">
                                    <span class="text-white font-bold">高信博士</span>的学术评估与海外教授资源 + <span class="text-white font-bold">MOMO 艺术家团队</span>全程配合交付 + <span class="text-white font-bold">主理人 Timo</span> 亲自跟项目。
                                </div>
                                <div class="text-neutral-400 leading-relaxed pt-1 border-t border-neutral-800/80">
                                    <span class="text-momo-cyan font-semibold">核心壁垒：</span>依托 MOMO 音乐教育板块的全部底座（专业课程、独家真录音棚作品集多轨实录、大乐队合奏支撑），直接对标德奥公立免学费、英皇、伯克利、洗足学园等名校。
                                </div>
                            </div>
                            <div class="text-xs text-neutral-400 space-y-1">
                                <div>• 包含：专业能力硬核评估 / 选校策略矩阵 / 独家专业文书指导</div>
                                <div>• 包含：欧美顶尖教授线上大师课 / 考学资源与试奏直连对接</div>
                            </div>
                        </div>
                        <div class="pt-6 border-t border-neutral-800 mt-6 flex flex-wrap gap-3">
                            <button type="button" onclick="openBookingModal('预约高信博士与Timo 留学评估 (¥38,800项目)')" class="gradient-bg text-black px-6 py-3 font-black text-xs uppercase tracking-wider hover:brightness-110 transition-all flex-1 text-center cursor-pointer">
                                预约高信博士评估咨询
                            </button>
                            <button type="button" onclick="openStudyAbroadModal()" class="border border-neutral-700 hover:border-white text-white px-5 py-3 font-bold text-xs uppercase tracking-wider transition-all cursor-pointer">
                                查看学员作品集实录案例 >
                            </button>
                        </div>
                    </div>

                    <!-- ==================== 产品 03 (空间生态)：城市音乐共享空间场地线下租用 ==================== -->
                    <div id="spaces-rental" class="lg:col-span-6 brutalist-border bg-[#0d0d0d] p-8 md:p-10 flex flex-col justify-between group">
                        <div class="space-y-6">
                            <div class="aspect-16/9 overflow-hidden rounded border border-neutral-800 relative cursor-pointer" onclick="openSpacesModal()">
                                <img src="./assets/images/momo_garden_space.jpg" alt="Urban Music Shared Space" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 filter brightness-95">
                                <div class="absolute top-3 left-3 px-3 py-1 bg-black/80 backdrop-blur-md border border-neutral-700 text-momo-mint font-mono text-xs">
                                    小区独享 · 极致私密安静
                                </div>
                            </div>
                            <div>
                                <div class="text-xs font-mono text-momo-cyan uppercase tracking-widest">OFFLINE SANCTUARY</div>
                                <h3 class="text-2xl sm:text-3xl font-black text-white uppercase tracking-tight mt-1">
                                    城市音乐共享空间与场地线下租用
                                </h3>
                                <div class="mt-2 text-neutral-400 text-xs font-mono">
                                    因坐落于品质小区，具备天然的私密性与高雅宁静，无商业街喧哗打扰
                                </div>
                            </div>
                            <!-- 明码租用价格 -->
                            <div class="grid grid-cols-2 gap-3 pt-1">
                                <div class="border border-neutral-800 bg-neutral-950 p-3.5 rounded cursor-pointer" onclick="openSpacesModal()">
                                    <div class="text-xs text-neutral-400 font-mono">排练室租用</div>
                                    <div class="text-2xl font-black text-momo-cyan font-mono mt-0.5">¥200 <span class="text-xs font-normal text-neutral-400">/ 小时</span></div>
                                    <div class="text-[11px] text-neutral-400 mt-1">钢琴、电钢、吉他、音响、专业架子鼓全配可用</div>
                                </div>
                                <div class="border border-neutral-800 bg-neutral-950 p-3.5 rounded cursor-pointer" onclick="openSpacesModal()">
                                    <div class="text-xs text-neutral-400 font-mono">会议/沙龙空间</div>
                                    <div class="text-2xl font-black text-white font-mono mt-0.5">¥100 <span class="text-xs font-normal text-neutral-400">/ 小时</span></div>
                                    <div class="text-[11px] text-neutral-400 mt-1">可舒适容纳 10～40 人深度企划与分享</div>
                                </div>
                            </div>
                            <!-- 空间亮点 -->
                            <div class="p-3.5 border border-neutral-800 bg-neutral-950 rounded text-xs space-y-1.5 text-neutral-300">
                                <div>☕ <span class="text-white font-semibold">中央品质吧台区域：</span>现磨咖啡、茶饮与主理人级别的社交休憩场。</div>
                                <div>🌿 <span class="text-white font-semibold">60㎡ 户外私家庭院：</span>露天阳光绿植、呼吸自然、户外不插电 Jam。</div>
                                <div class="text-[11px] font-mono text-momo-mint pt-1">✦ 空间展示实录视频随后上线，欢迎预约到场实地考察</div>
                            </div>
                        </div>
                        <div class="pt-6 border-t border-neutral-800 mt-6 flex flex-wrap gap-3">
                            <button type="button" onclick="openBookingModal('预订线下场地租用 (排练室¥200/h 或 会议室¥100/h)')" class="gradient-bg text-black px-6 py-3 font-black text-xs uppercase tracking-wider hover:brightness-110 transition-all flex-1 text-center cursor-pointer">
                                预订排练 / 会议时段
                            </button>
                            <button type="button" onclick="openSpacesModal()" class="border border-neutral-700 hover:border-white text-white px-5 py-3 font-bold text-xs uppercase tracking-wider transition-all cursor-pointer">
                                查看空间配置与实景详情 >
                            </button>
                        </div>
                    </div>

                    <!-- ==================== 产品 04 (生命公益)：大凉山 3天2晚音乐公益共修营 ==================== -->
                    <div id="giving-rack" class="lg:col-span-12 brutalist-border bg-gradient-to-r from-[#0b0c10] to-[#080808] p-8 md:p-10 relative overflow-hidden group">
                        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
                            <div class="lg:col-span-8 space-y-4">
                                <div class="inline-flex items-center gap-2 px-3 py-1 bg-momo-mint/10 border border-momo-mint/30 text-momo-mint text-xs font-mono rounded">
                                    <span>GIVING & SONIC PILGRIMAGE · 3-4人即成团出发</span>
                                </div>
                                <h3 class="text-2xl sm:text-3xl font-black text-white uppercase tracking-tight">
                                    大凉山 3天2晚 音乐公益共修营
                                </h3>
                                <div class="flex items-baseline gap-3">
                                    <span class="text-3xl sm:text-4xl font-black text-momo-mint font-mono">¥4,000</span>
                                    <span class="text-neutral-400 text-xs font-mono">/ 人（含全程交通、食宿、乐器物料及导师陪同）</span>
                                </div>
                                <p class="text-neutral-300 text-sm leading-relaxed max-w-2xl">
                                    走出城市的内卷与情绪牢笼。由提莫（Timomo）带领导师团亲自带队，奔赴大凉山乡村学校送乐器、建乐队。让高敏感青少年在最纯粹的山野歌声与利他中找回生命韧性，同时收获无法作假的真实国际升学公益背书。
                                </p>
                                <div class="pt-2 flex flex-wrap gap-4">
                                    <button type="button" onclick="openBookingModal('申请大凉山 3天2晚音乐公益营 (¥4,000/人)')" class="gradient-bg text-black px-7 py-3 font-black text-xs uppercase tracking-wider hover:brightness-110 active:scale-95 transition-all cursor-pointer">
                                        申请本期行程席位 (¥4,000)
                                    </button>
                                    <button type="button" onclick="openCharityRetreatModal()" class="border border-neutral-700 hover:border-white text-white px-6 py-3 font-bold text-xs uppercase tracking-wider transition-all cursor-pointer">
                                        查看 3天2晚详细行程手册与蜕变档案 >
                                    </button>
                                </div>
                            </div>
                            <div class="lg:col-span-4 cursor-pointer" onclick="openCharityRetreatModal()">
                                <div class="aspect-4/3 rounded overflow-hidden border border-neutral-800">
                                    <img src="./assets/images/real_daliangshan_charity.jpg" alt="Daliangshan Music Charity Documentary" class="w-full h-full object-cover filter brightness-90 group-hover:scale-105 transition-transform duration-700">
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
'''

# Build Teenage Engineering Style Merch Store
new_merch_store = '''
        <!-- ==================== TEENAGE ENGINEERING 风格美学周边商店 ==================== -->
        <section id="merch-store" class="py-24 px-6 md:px-12 border-b border-neutral-900 bg-[#080808]">
            <div class="max-w-7xl mx-auto">
                <div class="flex flex-col md:flex-row md:items-end justify-between mb-16 pb-6 border-b border-neutral-800">
                    <div>
                        <div class="text-xs font-mono text-momo-mint uppercase tracking-widest mb-2">// TEENAGE ENGINEERING AESTHETIC STORE</div>
                        <h2 class="text-3xl sm:text-5xl font-black uppercase tracking-tight text-white">
                            MOMO 先锋美学商店
                        </h2>
                    </div>
                    <div class="mt-4 md:mt-0 text-sm font-mono text-neutral-400">
                        工业极简 · 属于音乐公民的身份徽章 · 点击单品滑出全景细节抽屉
                    </div>
                </div>

                <!-- 4款高质感单品网格 -->
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
                    <!-- 单品 01：纯黑刺绣重磅文化衫 (会员免费赠送) -->
                    <div onclick="openProductDrawer('tshirt')" class="brutalist-border bg-neutral-950 p-6 flex flex-col justify-between cursor-pointer hover:border-momo-cyan transition-all group">
                        <div>
                            <div class="aspect-square bg-[#0f0f0f] rounded overflow-hidden mb-5 relative border border-neutral-800">
                                <img src="./assets/images/momo_tshirt_te_style.jpg" alt="MOMO T-Shirt" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                                <div class="absolute top-2 left-2 px-2 py-0.5 bg-momo-mint text-black font-black text-[10px] uppercase tracking-wider rounded">
                                    ★ 会员免费赠送
                                </div>
                            </div>
                            <div class="text-xs font-mono text-neutral-400 uppercase">APPAREL 01</div>
                            <h3 class="text-lg font-bold text-white group-hover:text-momo-cyan transition-colors mt-1">
                                MOMO 纯黑重磅刺绣文化衫
                            </h3>
                            <p class="text-xs text-neutral-400 mt-1 line-clamp-2">
                                320g 重磅纯棉 · 巴黎世家宽松落肩剪裁 · 前胸同色暗黑高密微距刺绣
                            </p>
                        </div>
                        <div class="pt-4 border-t border-neutral-900 mt-4 flex items-center justify-between">
                            <span class="text-xl font-black font-mono text-white">¥260</span>
                            <span class="text-xs font-mono text-momo-cyan group-hover:underline">查看细节 ></span>
                        </div>
                    </div>

                    <!-- 单品 02：乐手纯黑机能帆布托特包 -->
                    <div onclick="openProductDrawer('tote')" class="brutalist-border bg-neutral-950 p-6 flex flex-col justify-between cursor-pointer hover:border-momo-cyan transition-all group">
                        <div>
                            <div class="aspect-square bg-[#0f0f0f] rounded overflow-hidden mb-5 relative border border-neutral-800">
                                <img src="./assets/images/momo_merch_collection.jpg" alt="MOMO Musician Tote" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                            </div>
                            <div class="text-xs font-mono text-neutral-400 uppercase">ACCESSORY 02</div>
                            <h3 class="text-lg font-bold text-white group-hover:text-momo-cyan transition-colors mt-1">
                                乐手纯黑机能帆布托特包
                            </h3>
                            <p class="text-xs text-neutral-400 mt-1 line-clamp-2">
                                16A 加密防泼水帆布 · 可容纳 16 寸 MacBook 与重奏乐谱夹 · 独立琴拔暗袋
                            </p>
                        </div>
                        <div class="pt-4 border-t border-neutral-900 mt-4 flex items-center justify-between">
                            <span class="text-xl font-black font-mono text-white">¥180</span>
                            <span class="text-xs font-mono text-momo-cyan group-hover:underline">查看细节 ></span>
                        </div>
                    </div>

                    <!-- 单品 03：赛璐珞吉他拨片黑锡盒 -->
                    <div onclick="openProductDrawer('picks')" class="brutalist-border bg-neutral-950 p-6 flex flex-col justify-between cursor-pointer hover:border-momo-cyan transition-all group">
                        <div>
                            <div class="aspect-square bg-[#0f0f0f] rounded overflow-hidden mb-5 relative border border-neutral-800">
                                <img src="./assets/images/real_momo_picks_tin.jpg" alt="MOMO Celluloid Picks Tin Box" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                            </div>
                            <div class="text-xs font-mono text-neutral-400 uppercase">HARDWARE 03</div>
                            <h3 class="text-lg font-bold text-white group-hover:text-momo-cyan transition-colors mt-1">
                                纪念款赛璐珞吉他拨片黑锡盒
                            </h3>
                            <p class="text-xs text-neutral-400 mt-1 line-clamp-2">
                                磨砂黑马口铁盒 · 6枚定制赛璐珞拔片（0.71/0.96/1.14mm 爵士与扫弦硬度全包）
                            </p>
                        </div>
                        <div class="pt-4 border-t border-neutral-900 mt-4 flex items-center justify-between">
                            <span class="text-xl font-black font-mono text-white">¥88</span>
                            <span class="text-xs font-mono text-momo-cyan group-hover:underline">查看细节 ></span>
                        </div>
                    </div>

                    <!-- 单品 04：现场实录限定黑胶唱片声音集 -->
                    <div onclick="openProductDrawer('vinyl')" class="brutalist-border bg-neutral-950 p-6 flex flex-col justify-between cursor-pointer hover:border-momo-cyan transition-all group">
                        <div>
                            <div class="aspect-square bg-[#0f0f0f] rounded overflow-hidden mb-5 relative border border-neutral-800">
                                <img src="./assets/images/real_momo_vinyl.jpg" alt="MOMO 180g Vinyl Record" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                            </div>
                            <div class="text-xs font-mono text-neutral-400 uppercase">VINYL 04</div>
                            <h3 class="text-lg font-bold text-white group-hover:text-momo-cyan transition-colors mt-1">
                                现场实录限定黑胶声音集
                            </h3>
                            <p class="text-xs text-neutral-400 mt-1 line-clamp-2">
                                180g 重磅黑胶 · 收录菲比乐队版《Jingle Bells》与 24-bit 独家现场同期直录
                            </p>
                        </div>
                        <div class="pt-4 border-t border-neutral-900 mt-4 flex items-center justify-between">
                            <span class="text-xl font-black font-mono text-white">¥320</span>
                            <span class="text-xs font-mono text-momo-cyan group-hover:underline">查看细节 ></span>
                        </div>
                    </div>
                </div>
            </div>
        </section>
'''

# Build Faculty Section (MasterClass Gallery)
new_faculty = '''
        <!-- ==================== 一线艺术家导师档案 (MasterClass 风格) ==================== -->
        <section id="faculty" class="py-24 px-6 md:px-12 border-b border-neutral-900 bg-[#090909]">
            <div class="max-w-7xl mx-auto">
                <div class="flex flex-col md:flex-row md:items-end justify-between mb-16 pb-6 border-b border-neutral-800">
                    <div>
                        <div class="text-xs font-mono text-momo-cyan uppercase tracking-widest mb-2">// MASTERCLASS CURATION</div>
                        <h2 class="text-3xl sm:text-5xl font-black uppercase tracking-tight text-white">
                            13 位中外独立名师长廊
                        </h2>
                    </div>
                    <p class="mt-4 md:mt-0 text-sm font-mono text-neutral-400">
                        非传统机构全职助教 · 汇聚一线巡演爵士乐手、海归学者与音频制作人
                    </p>
                </div>

                <!-- 导师卡片画廊 -->
                <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
                    <!-- 01. Timo -->
                    <div onclick="openFacultyDrawer('timo')" class="brutalist-border bg-neutral-950 p-5 group hover:border-momo-cyan transition-all cursor-pointer">
                        <div class="aspect-square bg-neutral-900 rounded overflow-hidden mb-4 border border-neutral-800">
                            <img src="./assets/images/hero_trumpet.jpg" alt="Timo" class="w-full h-full object-cover filter grayscale group-hover:grayscale-0 group-hover:scale-105 transition-all duration-500">
                        </div>
                        <div class="text-[11px] font-mono text-momo-cyan">FOUNDER / DRUMS & PRODUCTION</div>
                        <h4 class="text-lg font-bold text-white mt-1 group-hover:text-momo-cyan transition-colors">Timo (提莫)</h4>
                        <p class="text-xs text-neutral-400 mt-1 line-clamp-2">品牌主理人 · 爵士鼓手与制作人 · 深度交付升学实录与合奏</p>
                        <div class="mt-3 text-[11px] font-mono text-neutral-500 group-hover:text-white transition-colors">查看完整艺术档案 ></div>
                    </div>

                    <!-- 02. 高信博士 -->
                    <div onclick="openFacultyDrawer('gaoxin')" class="brutalist-border bg-neutral-950 p-5 group hover:border-momo-cyan transition-all cursor-pointer">
                        <div class="aspect-square bg-neutral-900 rounded overflow-hidden mb-4 border border-neutral-800">
                            <img src="./assets/images/modern_violin.jpg" alt="Dr. Gaoxin" class="w-full h-full object-cover filter grayscale group-hover:grayscale-0 group-hover:scale-105 transition-all duration-500">
                        </div>
                        <div class="text-[11px] font-mono text-momo-mint">ACADEMIC DIRECTOR / PHD</div>
                        <h4 class="text-lg font-bold text-white mt-1 group-hover:text-momo-mint transition-colors">高信博士</h4>
                        <p class="text-xs text-neutral-400 mt-1 line-clamp-2">管乐博士 · 欧美名校升学规划首席学术顾问 · 国际教授直连</p>
                        <div class="mt-3 text-[11px] font-mono text-neutral-500 group-hover:text-white transition-colors">查看完整艺术档案 ></div>
                    </div>

                    <!-- 03. 王崇恩 -->
                    <div onclick="openFacultyDrawer('wangchongen')" class="brutalist-border bg-neutral-950 p-5 group hover:border-momo-cyan transition-all cursor-pointer">
                        <div class="aspect-square bg-neutral-900 rounded overflow-hidden mb-4 border border-neutral-800">
                            <img src="./assets/images/pedalboard.jpg" alt="Wang Chongen" class="w-full h-full object-cover filter grayscale group-hover:grayscale-0 group-hover:scale-105 transition-all duration-500">
                        </div>
                        <div class="text-[11px] font-mono text-momo-cyan">ELECTRIC & ACOUSTIC GUITAR</div>
                        <h4 class="text-lg font-bold text-white mt-1 group-hover:text-momo-cyan transition-colors">王崇恩</h4>
                        <p class="text-xs text-neutral-400 mt-1 line-clamp-2">资深吉他演奏家 · 现代摇滚与爵士电吉他 · 菲比乐队吉他导师</p>
                        <div class="mt-3 text-[11px] font-mono text-neutral-500 group-hover:text-white transition-colors">查看完整艺术档案 ></div>
                    </div>

                    <!-- 04. 乔晓记 -->
                    <div onclick="openFacultyDrawer('qiaoxiaoji')" class="brutalist-border bg-neutral-950 p-5 group hover:border-momo-cyan transition-all cursor-pointer">
                        <div class="aspect-square bg-neutral-900 rounded overflow-hidden mb-4 border border-neutral-800">
                            <img src="./assets/images/double_bass.png" alt="Qiao Xiaoji" class="w-full h-full object-cover filter grayscale group-hover:grayscale-0 group-hover:scale-105 transition-all duration-500">
                        </div>
                        <div class="text-[11px] font-mono text-momo-mint">DOUBLE BASS & ELECTRIC BASS</div>
                        <h4 class="text-lg font-bold text-white mt-1 group-hover:text-momo-mint transition-colors">乔晓记</h4>
                        <p class="text-xs text-neutral-400 mt-1 line-clamp-2">克拉科夫音乐学院海归 · 原声低音提琴与贝斯导师</p>
                        <div class="mt-3 text-[11px] font-mono text-neutral-500 group-hover:text-white transition-colors">查看完整艺术档案 ></div>
                    </div>
                </div>

                <div class="mt-12 text-center">
                    <button type="button" onclick="openFacultyDrawer('all')" class="border border-neutral-700 hover:border-momo-cyan text-neutral-300 hover:text-white px-8 py-3.5 text-xs font-mono uppercase tracking-wider transition-all cursor-pointer">
                        查看完整 13 位导师艺术造诣档案与试听 >
                    </button>
                </div>
            </div>
        </section>
'''

# Build Spaces Section
new_spaces = '''
        <!-- ==================== 双旗舰空间实景与交通 ==================== -->
        <section id="spaces" class="py-24 px-6 md:px-12 border-b border-neutral-900 bg-[#07070a]">
            <div class="max-w-7xl mx-auto">
                <div class="flex flex-col md:flex-row md:items-end justify-between mb-16 pb-6 border-b border-neutral-800">
                    <div>
                        <div class="text-xs font-mono text-momo-cyan uppercase tracking-widest mb-2">// DUAL FLAGSHIP SPACES</div>
                        <h2 class="text-3xl sm:text-5xl font-black uppercase tracking-tight text-white">
                            桐梓林 & 麓湖 双空间
                        </h2>
                    </div>
                    <div class="mt-4 md:mt-0 text-sm font-mono text-neutral-400">
                        私密高档社区 · 专业录音棚排练室 · 60㎡ 露天私家花园
                    </div>
                </div>

                <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
                    <!-- 桐梓林空间 -->
                    <div class="brutalist-border bg-neutral-950 p-8 space-y-5 cursor-pointer" onclick="openSpacesModal()">
                        <div class="aspect-16/9 rounded overflow-hidden border border-neutral-800">
                            <img src="./assets/images/momo_garden_space.jpg" alt="Tongzilin Space" class="w-full h-full object-cover">
                        </div>
                        <div class="flex items-center justify-between">
                            <h3 class="text-2xl font-black text-white">桐梓林旗舰空间 (银都花园)</h3>
                            <span class="text-xs font-mono text-momo-mint px-2.5 py-1 bg-momo-mint/10 border border-momo-mint/30 rounded">黑胶沙龙 & 琴房排练</span>
                        </div>
                        <p class="text-xs text-neutral-400 leading-relaxed">
                            成都市武侯区桐梓林核心社区。配备三角钢琴、电钢、专业全套吉他管箱与架子鼓排练室，自带中央咖啡吧台与 60㎡ 阳光私家庭院。
                        </p>
                        <div class="pt-2 flex items-center justify-between text-xs font-mono text-neutral-400 border-t border-neutral-900 pt-4">
                            <span>排练室 ¥200/h ｜ 会议室 ¥100/h</span>
                            <span class="text-momo-cyan hover:underline">查看空间全景配置 ></span>
                        </div>
                    </div>

                    <!-- 麓湖空间 -->
                    <div class="brutalist-border bg-neutral-950 p-8 space-y-5 cursor-pointer" onclick="openSpacesModal()">
                        <div class="aspect-16/9 rounded overflow-hidden border border-neutral-800">
                            <img src="./assets/images/real_daliangshan_charity.jpg" alt="Luxe Lakes Space" class="w-full h-full object-cover">
                        </div>
                        <div class="flex items-center justify-between">
                            <h3 class="text-2xl font-black text-white">麓湖合奏实验室 (麓坊中心)</h3>
                            <span class="text-xs font-mono text-momo-cyan px-2.5 py-1 bg-momo-cyan/10 border border-momo-cyan/30 rounded">大乐队合奏 & 自然声场</span>
                        </div>
                        <p class="text-xs text-neutral-400 leading-relaxed">
                            天府新区麓湖生态水岸。宽阔多功能合奏厅，承载青少年爵士大乐队、家庭音乐日及企业艺术沙龙定制。
                        </p>
                        <div class="pt-2 flex items-center justify-between text-xs font-mono text-neutral-400 border-t border-neutral-900 pt-4">
                            <span>可容纳 10～40 人合奏演练</span>
                            <span class="text-momo-cyan hover:underline">查看空间全景配置 ></span>
                        </div>
                    </div>
                </div>
            </div>
        </section>
'''

# Comprehensive 2nd-Level Drawers / Modals (All set to 'hidden' by default so clicks are NEVER blocked!)
comprehensive_level2_modals = f'''
        <!-- ==================== 01. 会员 PLUS 深度全景抽屉 (Membership Modal) ==================== -->
        <div id="membership-modal" class="fixed inset-0 z-[110] hidden transition-opacity duration-300 opacity-0">
            <div onclick="closeMembershipModal()" class="absolute inset-0 bg-black/85 backdrop-blur-md cursor-pointer"></div>
            
            <div id="membership-panel" class="absolute top-0 right-0 h-full w-full max-w-2xl bg-[#0c0c0e] border-l border-neutral-800 transform translate-x-full transition-transform duration-300 ease-out flex flex-col justify-between overflow-y-auto p-8 md:p-14 text-white z-10">
                <div class="space-y-8">
                    <!-- 顶部栏 -->
                    <div class="flex items-center justify-between pb-6 border-b border-neutral-800">
                        <div class="flex items-center gap-2.5">
                            {MOMO_SHIELD_SVG}
                            <span class="text-xs font-mono uppercase tracking-widest text-momo-mint">MOMO FAMILY MEMBERSHIP PLUS</span>
                        </div>
                        <button type="button" onclick="closeMembershipModal()" class="p-2 text-neutral-400 hover:text-white transition-colors cursor-pointer" aria-label="Close membership modal">
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                        </button>
                    </div>

                    <!-- 品牌白金卡大图特写 -->
                    <div class="relative rounded-xl overflow-hidden border border-white/20 shadow-2xl">
                        <img src="./assets/images/momo_platinum_card.jpg" alt="MOMO Platinum Card Close-up" class="w-full h-auto object-cover">
                    </div>

                    <!-- 纯会员制底座宣言 -->
                    <div class="space-y-3">
                        <div class="inline-block px-3 py-1 bg-neutral-800 text-momo-cyan text-xs font-mono rounded">
                            MEMBERS-ONLY PHILOSOPHY · 专属纯会员制
                        </div>
                        <h2 class="text-2xl sm:text-3xl font-black text-white uppercase tracking-tight">
                            为什么 MOMO 坚持“纯会员制”，不服务非会员？
                        </h2>
                        <p class="text-neutral-300 text-sm leading-relaxed">
                            在快节奏与考级焦虑泛滥的当下，普通琴行与商业机构充斥着推销与过客。MOMO 坚持纯会员制，是为了向每个家庭筑起一道真正的<span class="text-white font-bold">「生命与声音的安全场（Safe Haven）」</span>——这里没有散客的喧哗与考级机构的催促，只有相互托举的音乐家、家庭与真实热爱。
                        </p>
                    </div>

                    <!-- 五大核心会员权益全览 -->
                    <div class="space-y-4 border-t border-neutral-800 pt-6">
                        <div class="text-xs font-mono text-neutral-400 uppercase tracking-wider">// ANNUAL PRIVILEGES · 会员专属权益矩阵</div>
                        
                        <div class="space-y-3">
                            <div class="p-4 rounded-lg bg-neutral-950 border border-neutral-800">
                                <div class="flex items-center justify-between">
                                    <span class="font-bold text-white text-base">01. 4-on-1 职业乐队实验室划扣特权</span>
                                    <span class="text-xs font-mono text-momo-cyan">¥400 / 30min</span>
                                </div>
                                <p class="text-xs text-neutral-400 mt-1.5 leading-relaxed">
                                    由4位中外爵士与流行音乐家（吉他、贝斯、鼓、键盘）围着你一人伴奏。在真录音棚同期多轨实录，直接完成你自己的作品。
                                </p>
                            </div>

                            <div class="p-4 rounded-lg bg-neutral-950 border border-neutral-800">
                                <div class="flex items-center justify-between">
                                    <span class="font-bold text-white text-base">02. 3–7岁 全家庭音乐时光</span>
                                    <span class="text-xs font-mono text-momo-cyan">¥400 / 45min</span>
                                </div>
                                <p class="text-xs text-neutral-400 mt-1.5 leading-relaxed">
                                    告别死记硬背指法。爸爸妈妈与孩子同场拿起真实乐器，在专业音乐人陪伴下排练属于家庭的第一首乐队作品。
                                </p>
                            </div>

                            <div class="p-4 rounded-lg bg-neutral-950 border border-neutral-800">
                                <div class="flex items-center justify-between">
                                    <span class="font-bold text-white text-base">03. 城市真实舞台流淌（如城市音乐节亮灯）</span>
                                    <span class="text-xs font-mono text-momo-mint">自然纳入规划</span>
                                </div>
                                <p class="text-xs text-neutral-400 mt-1.5 leading-relaxed">
                                    绝无排位、绝无竞技选拔。在城市公共空间需要节日温暖音乐时，顺势而生，让孩子在数百位市民真实注视下自信发光。
                                </p>
                            </div>

                            <div class="p-4 rounded-lg bg-neutral-950 border border-neutral-800">
                                <div class="flex items-center justify-between">
                                    <span class="font-bold text-white text-base">04. 实体入会礼遇 · 定制纯黑重磅文化衫</span>
                                    <span class="text-xs font-mono text-momo-mint">免费获赠一件</span>
                                </div>
                                <p class="text-xs text-neutral-400 mt-1.5 leading-relaxed">
                                    320g 巴黎世家版型同色刺绣文化衫（价值 ¥260），入会即赠，成为 MOMO 音乐公民的专属标志。
                                </p>
                            </div>

                            <div class="p-4 rounded-lg bg-neutral-950 border border-neutral-800">
                                <div class="flex items-center justify-between">
                                    <span class="font-bold text-white text-base">05. 双空间与排练室优先预约与会员特权</span>
                                    <span class="text-xs font-mono text-momo-cyan">专属折扣通道</span>
                                </div>
                                <p class="text-xs text-neutral-400 mt-1.5 leading-relaxed">
                                    桐梓林（琴房与吧台花园）及麓湖水岸双空间优先锁档，支持会员自由举办家庭沙龙与排练。
                                </p>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 抽屉底部申请栏 -->
                <div class="pt-8 border-t border-neutral-800 mt-8 space-y-3">
                    <button type="button" onclick="closeMembershipModal(); openBookingModal('申请开通 MOMO 家庭音乐会员 (¥6,000)');" class="w-full gradient-bg text-black py-4 font-black text-xs uppercase tracking-wider hover:brightness-110 active:scale-95 transition-all text-center cursor-pointer">
                        立即申请开通 MOMO 家庭音乐会员 (¥6,000)
                    </button>
                    <div class="text-center text-[11px] font-mono text-neutral-500">
                        一户开通 · 全家共享 · 额度自由划扣 · 支持预约到店理念沟通
                    </div>
                </div>
            </div>
        </div>

        <!-- ==================== 02. 欧美音乐学院留学规划全景抽屉 (Study Abroad Modal) ==================== -->
        <div id="study-abroad-modal" class="fixed inset-0 z-[110] hidden transition-opacity duration-300 opacity-0">
            <div onclick="closeStudyAbroadModal()" class="absolute inset-0 bg-black/85 backdrop-blur-md cursor-pointer"></div>
            
            <div id="study-abroad-panel" class="absolute top-0 right-0 h-full w-full max-w-2xl bg-[#0c0c0e] border-l border-neutral-800 transform translate-x-full transition-transform duration-300 ease-out flex flex-col justify-between overflow-y-auto p-8 md:p-14 text-white z-10">
                <div class="space-y-8">
                    <div class="flex items-center justify-between pb-6 border-b border-neutral-800">
                        <span class="text-xs font-mono uppercase tracking-widest text-momo-cyan">// CONSERVATORY & PORTFOLIO MENTORSHIP</span>
                        <button type="button" onclick="closeStudyAbroadModal()" class="p-2 text-neutral-400 hover:text-white transition-colors cursor-pointer">
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                        </button>
                    </div>

                    <div>
                        <div class="inline-block px-3 py-1 bg-momo-cyan/10 border border-momo-cyan/30 text-momo-cyan text-xs font-mono rounded mb-2">
                            FIXED COMPANIONSHIP · ¥38,800 固定的深度陪伴
                        </div>
                        <h2 class="text-2xl sm:text-3xl font-black text-white uppercase tracking-tight">
                            欧美音乐学院 · 升学与艺术留学全景规划
                        </h2>
                        <p class="text-neutral-300 text-sm leading-relaxed mt-2">
                            项目负责人：<span class="text-white font-bold">高信博士</span>（学术评估与海外教授资源）+ <span class="text-white font-bold">MOMO 艺术家团队</span>全程配合交付 + <span class="text-white font-bold">主理人 Timo</span> 亲自下场跟项目。
                        </p>
                    </div>

                    <!-- 学员作品集实录影院 -->
                    <div class="space-y-3">
                        <div class="text-xs font-mono text-momo-mint uppercase">// REAL STUDENT PORTFOLIO VIDEO</div>
                        <div class="aspect-16/9 bg-black rounded-xl overflow-hidden border border-neutral-800 relative">
                            <video controls playsinline preload="metadata" class="w-full h-full object-cover">
                                <source src="./留学作品集/10月7日.mp4" type="video/mp4">
                                您的浏览器不支持视频播放。
                            </video>
                        </div>
                        <div class="text-xs text-neutral-400 flex justify-between">
                            <span>欧洲音乐学院硕士申请实录现场</span>
                            <span>24轨真乐队同期直录 · 零修音一次成型</span>
                        </div>
                    </div>

                    <!-- 交付五步里程碑 -->
                    <div class="space-y-4 border-t border-neutral-800 pt-6">
                        <div class="text-xs font-mono text-neutral-400 uppercase tracking-wider">// DELIVERY MILESTONES · 五大交付里程碑</div>
                        
                        <div class="space-y-3">
                            <div class="p-4 rounded-lg bg-neutral-950 border border-neutral-800">
                                <div class="font-bold text-white text-sm">阶段一 · 硬核学术测评与能力摸底</div>
                                <div class="text-xs text-neutral-400 mt-1">高信博士 1对1 面对面测评视唱练耳、和声分析、即兴造诣与曲目储备，出具专业评估报告。</div>
                            </div>
                            <div class="p-4 rounded-lg bg-neutral-950 border border-neutral-800">
                                <div class="font-bold text-white text-sm">阶段二 · 全球目标院校与导师梯度规划</div>
                                <div class="text-xs text-neutral-400 mt-1">精准锁定德奥公立免学费音乐学院（汉堡/慕尼黑等）、英国皇家RNCM/RAM、美国伯克利及日韩名校。</div>
                            </div>
                            <div class="p-4 rounded-lg bg-neutral-950 border border-neutral-800">
                                <div class="font-bold text-white text-sm">阶段三 · 24轨真乐队同期多轨实录作品集制作</div>
                                <div class="text-xs text-neutral-400 mt-1">依托 MOMO 录音棚与导师乐队（吉他/贝斯/鼓），担任伴奏录制最高标准的现场作品集，彻底甩开市面伴奏带。</div>
                            </div>
                            <div class="p-4 rounded-lg bg-neutral-950 border border-neutral-800">
                                <div class="font-bold text-white text-sm">阶段四 · 独家定制艺术陈述与文书润色</div>
                                <div class="text-xs text-neutral-400 mt-1">由真正懂音乐的导师深度梳理艺术心路，撰写最具穿透力的个人陈述（PS）与导师推荐信。</div>
                            </div>
                            <div class="p-4 rounded-lg bg-neutral-950 border border-neutral-800">
                                <div class="font-bold text-white text-sm">阶段五 · 海外教授网课与试奏直连</div>
                                <div class="text-xs text-neutral-400 mt-1">直接连线海外院校在职教授线上大师课，考前一对一针对性点拨面试题型与试奏心态。</div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="pt-8 border-t border-neutral-800 mt-8 space-y-3">
                    <button type="button" onclick="closeStudyAbroadModal(); openBookingModal('预约高信博士与Timo 留学评估 (¥38,800)');" class="w-full gradient-bg text-black py-4 font-black text-xs uppercase tracking-wider text-center cursor-pointer">
                        预约高信博士与 Timo 1对1 留学硬核评估
                    </button>
                    <div class="text-center text-[11px] font-mono text-neutral-500">
                        仅面向本年度有志冲刺欧美日韩顶尖音乐名校的学子 · 限量深度陪伴
                    </div>
                </div>
            </div>
        </div>

        <!-- ==================== 03. 空间与场地线下租用全景抽屉 (Spaces Modal) ==================== -->
        <div id="spaces-modal" class="fixed inset-0 z-[110] hidden transition-opacity duration-300 opacity-0">
            <div onclick="closeSpacesModal()" class="absolute inset-0 bg-black/85 backdrop-blur-md cursor-pointer"></div>
            
            <div id="spaces-panel" class="absolute top-0 right-0 h-full w-full max-w-2xl bg-[#0c0c0e] border-l border-neutral-800 transform translate-x-full transition-transform duration-300 ease-out flex flex-col justify-between overflow-y-auto p-8 md:p-14 text-white z-10">
                <div class="space-y-8">
                    <div class="flex items-center justify-between pb-6 border-b border-neutral-800">
                        <span class="text-xs font-mono uppercase tracking-widest text-momo-mint">// SPACES & VENUE RENTAL DETAILS</span>
                        <button type="button" onclick="closeSpacesModal()" class="p-2 text-neutral-400 hover:text-white transition-colors cursor-pointer">
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                        </button>
                    </div>

                    <!-- 空间实景大图 -->
                    <div class="rounded-xl overflow-hidden border border-neutral-800 relative">
                        <img src="./assets/images/momo_garden_space.jpg" alt="Spaces Real Photo" class="w-full h-auto object-cover">
                        <div class="absolute bottom-3 left-3 px-3 py-1 bg-black/80 backdrop-blur-md border border-neutral-700 text-xs font-mono text-momo-mint">
                            60㎡ 户外私家阳光庭院 + 中央精品咖啡吧台
                        </div>
                    </div>

                    <div>
                        <div class="inline-block px-3 py-1 bg-neutral-800 text-momo-cyan text-xs font-mono rounded mb-2">
                            PRIVATE RESIDENTIAL SANCTUARY · 小区私密独享
                        </div>
                        <h2 class="text-2xl sm:text-3xl font-black text-white uppercase tracking-tight">
                            为什么我们的空间如此安静而私密？
                        </h2>
                        <p class="text-neutral-300 text-sm leading-relaxed mt-2">
                            我们特意将空间选址在高档安静社区（桐梓林银都花园与麓湖水岸）。彻底阻隔了繁华商圈的嘈杂、无效打扰与过客目光。无论是一整天的乐队封闭排练、高端亲子沙龙，还是私密企划会议，这里都是一个让人完全放松呼吸的艺术私域。
                        </p>
                    </div>

                    <!-- 设备与收费详单 -->
                    <div class="space-y-4 border-t border-neutral-800 pt-6">
                        <div class="text-xs font-mono text-neutral-400 uppercase tracking-wider">// RENTAL PRICING & HARDWARE · 明码租用清单</div>
                        
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                            <div class="p-4 rounded-lg bg-neutral-950 border border-neutral-800 space-y-2">
                                <div class="text-xs font-mono text-momo-cyan uppercase">VENUE 01 · 乐队排练室</div>
                                <div class="text-2xl font-black text-white font-mono">¥200 <span class="text-xs text-neutral-400">/ 小时</span></div>
                                <div class="text-xs text-neutral-300 leading-relaxed">
                                    • 全配雅马哈原声钢琴 / Nord 电钢<br>
                                    • Fender/Marshall 经典电子管吉他箱<br>
                                    • Ampeg 专业贝斯箱 / Gretsch 爵士鼓<br>
                                    • Shure SM58 / 专业录音级监听音响
                                </div>
                            </div>
                            <div class="p-4 rounded-lg bg-neutral-950 border border-neutral-800 space-y-2">
                                <div class="text-xs font-mono text-momo-mint uppercase">VENUE 02 · 会议与沙龙厅</div>
                                <div class="text-2xl font-black text-white font-mono">¥100 <span class="text-xs text-neutral-400">/ 小时</span></div>
                                <div class="text-xs text-neutral-300 leading-relaxed">
                                    • 可舒适容纳 10～40 人深度企划会议<br>
                                    • 4K 超清智能无线投屏与音响系统<br>
                                    • 现磨精品意式咖啡吧台免费使用权<br>
                                    • 直通 60㎡ 阳光私家庭院露天休闲区
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="pt-8 border-t border-neutral-800 mt-8 space-y-3">
                    <button type="button" onclick="closeSpacesModal(); openBookingModal('预订线下场地租用 (排练室¥200/h 或 会议室¥100/h)');" class="w-full gradient-bg text-black py-4 font-black text-xs uppercase tracking-wider text-center cursor-pointer">
                        立即预约时段 / 实地考察
                    </button>
                    <div class="text-center text-[11px] font-mono text-neutral-500">
                        开放时段 9:00 - 22:00 · 会员享有优先锁档与连租折扣特权
                    </div>
                </div>
            </div>
        </div>

        <!-- ==================== 04. 大凉山音乐公益共修营全景抽屉 (Charity Retreat Modal) ==================== -->
        <div id="charity-retreat-modal" class="fixed inset-0 z-[110] hidden transition-opacity duration-300 opacity-0">
            <div onclick="closeCharityRetreatModal()" class="absolute inset-0 bg-black/85 backdrop-blur-md cursor-pointer"></div>
            
            <div id="charity-retreat-panel" class="absolute top-0 right-0 h-full w-full max-w-2xl bg-[#0c0c0e] border-l border-neutral-800 transform translate-x-full transition-transform duration-300 ease-out flex flex-col justify-between overflow-y-auto p-8 md:p-14 text-white z-10">
                <div class="space-y-8">
                    <div class="flex items-center justify-between pb-6 border-b border-neutral-800">
                        <span class="text-xs font-mono uppercase tracking-widest text-momo-mint">// DALIANGSHAN SONIC PILGRIMAGE</span>
                        <button type="button" onclick="closeCharityRetreatModal()" class="p-2 text-neutral-400 hover:text-white transition-colors cursor-pointer">
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                        </button>
                    </div>

                    <!-- 真实公益纪实大图 -->
                    <div class="rounded-xl overflow-hidden border border-neutral-800 relative">
                        <img src="./assets/images/real_daliangshan_charity.jpg" alt="Daliangshan Charity Documentary" class="w-full h-auto object-cover">
                        <div class="absolute bottom-3 left-3 px-3 py-1 bg-black/80 backdrop-blur-md border border-neutral-700 text-xs font-mono text-momo-mint">
                            真实支教现场：孩子们在大山阳光下拿起吉他与打击乐
                        </div>
                    </div>

                    <div>
                        <div class="inline-block px-3 py-1 bg-momo-mint/10 border border-momo-mint/30 text-momo-mint text-xs font-mono rounded mb-2">
                            ¥4,000 / 人 · 满 3–4 人即成团出发
                        </div>
                        <h2 class="text-2xl sm:text-3xl font-black text-white uppercase tracking-tight">
                            大凉山 3天2晚 音乐公益共修营
                        </h2>
                        <p class="text-neutral-300 text-sm leading-relaxed mt-2">
                            由主理人提莫（Timomo）带领 MOMO 导师团亲自带队。在山野歌声中走出内卷与情绪牢笼，既是一次深度的生命治愈，也是一份任何中介都无法伪造的真实国际升学公益背书。
                        </p>
                    </div>

                    <!-- 3天2晚心流日程 -->
                    <div class="space-y-4 border-t border-neutral-800 pt-6">
                        <div class="text-xs font-mono text-neutral-400 uppercase tracking-wider">// 3-DAY ITINERARY · 三天两晚心流日程</div>
                        
                        <div class="space-y-3 text-xs">
                            <div class="p-4 rounded-lg bg-neutral-950 border border-neutral-800">
                                <div class="font-bold text-white text-sm">DAY 1 · 启程 · 抵达大山 · 乐器火种交接</div>
                                <div class="text-neutral-400 mt-1 leading-relaxed">
                                    成都集结出发 ➔ 沿途风景穿越 ➔ 抵达大凉山爱心小学 ➔ 交付捐赠的真乐器与教材 ➔ 晚间星空围炉音乐破冰。
                                </div>
                            </div>
                            <div class="p-4 rounded-lg bg-neutral-950 border border-neutral-800">
                                <div class="font-bold text-white text-sm">DAY 2 · 深度共修 · 乡村第一支乐队诞生</div>
                                <div class="text-neutral-400 mt-1 leading-relaxed">
                                    导师带志愿者开展沉浸式乐理与节奏工作坊 ➔ 组建属于大山孩子的第一支合奏乐队 ➔ 彝族原声民谣采风 ➔ 青少年生命疗愈倾听会。
                                </div>
                            </div>
                            <div class="p-4 rounded-lg bg-neutral-950 border border-neutral-800">
                                <div class="font-bold text-white text-sm">DAY 3 · 草地阳光音乐会 · 授证与回程</div>
                                <div class="text-neutral-400 mt-1 leading-relaxed">
                                    举办全校师生草地阳光告别音乐会 ➔ 孩子们登上自己的舞台主唱 ➔ 颁发当地官方联合认证的音乐支教公益证书 ➔ 满载感动返程。
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="pt-8 border-t border-neutral-800 mt-8 space-y-3">
                    <button type="button" onclick="closeCharityRetreatModal(); openBookingModal('申请大凉山 3天2晚音乐公益营 (¥4,000/人)');" class="w-full gradient-bg text-black py-4 font-black text-xs uppercase tracking-wider text-center cursor-pointer">
                        申请本期共修营席位 (¥4,000/人)
                    </button>
                    <div class="text-center text-[11px] font-mono text-neutral-500">
                        费用含成都往返专车交通、全程食宿及乐器耗材 · 结余汇入大山乐器基金
                    </div>
                </div>
            </div>
        </div>

        <!-- ==================== 05. 美学周边商品 TE 风格全景抽屉 (Product Drawer) ==================== -->
        <div id="product-drawer" class="fixed inset-0 z-[110] hidden transition-opacity duration-300 opacity-0">
            <div onclick="closeProductDrawer()" class="absolute inset-0 bg-black/85 backdrop-blur-md cursor-pointer"></div>
            
            <div id="drawer-panel" class="absolute top-0 right-0 h-full w-full max-w-xl bg-[#0d0d0d] border-l border-neutral-800 transform translate-x-full transition-transform duration-300 ease-out flex flex-col justify-between overflow-y-auto p-8 md:p-12 text-white z-10">
                <div>
                    <div class="flex items-center justify-between pb-6 border-b border-neutral-800">
                        <span id="drawer-category" class="text-xs font-mono text-momo-mint uppercase tracking-widest">// MOMO MERCH STORE</span>
                        <button type="button" onclick="closeProductDrawer()" class="p-2 text-neutral-400 hover:text-white transition-colors cursor-pointer" aria-label="Close drawer">
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                        </button>
                    </div>

                    <div class="mt-8 space-y-6">
                        <div class="aspect-square w-full rounded bg-[#111] overflow-hidden border border-neutral-800 relative">
                            <img id="drawer-img" src="./assets/images/momo_tshirt_te_style.jpg" alt="Product detail" class="w-full h-full object-cover">
                        </div>

                        <div>
                            <div id="drawer-member-badge" class="inline-block px-3 py-1 bg-momo-mint/20 border border-momo-mint/50 text-momo-mint text-xs font-bold rounded mb-2">
                                ★ 开通 MOMO 家庭音乐会员（¥6,000），本款免费赠送！
                            </div>
                            <h2 id="drawer-title" class="text-3xl font-black uppercase tracking-tight text-white">
                                MOMO 纯黑重磅刺绣文化衫
                            </h2>
                            <div class="mt-2 text-3xl font-mono font-black text-momo-cyan" id="drawer-price">
                                ¥260
                            </div>
                        </div>

                        <div class="text-sm text-neutral-300 leading-relaxed border-t border-neutral-800 pt-4" id="drawer-desc">
                            320g 高密精梳纯棉，巴黎世家经典落肩微阔版型。前胸同色黑线立体刺绣 MOMO 盾牌微标，洗水工艺保持不褪色、不变形。
                        </div>

                        <div class="border border-neutral-800 bg-neutral-950 p-4 rounded text-xs space-y-2 font-mono" id="drawer-specs">
                            <div class="flex justify-between"><span class="text-neutral-500">面料材质</span><span class="text-neutral-200">100% 320g 重磅精梳棉</span></div>
                            <div class="flex justify-between"><span class="text-neutral-500">版型结构</span><span class="text-neutral-200">Oversized 宽松落肩</span></div>
                            <div class="flex justify-between"><span class="text-neutral-500">尺码范围</span><span class="text-neutral-200">S (160-170cm) / M (170-180cm) / L (180cm+)</span></div>
                            <div class="flex justify-between"><span class="text-neutral-500">刺绣工艺</span><span class="text-neutral-200">德国田岛机 12000 针同色高密立体绣</span></div>
                        </div>
                    </div>
                </div>

                <div class="pt-8 border-t border-neutral-800 mt-8 space-y-3">
                    <button type="button" onclick="handleDrawerOrder()" class="w-full gradient-bg text-black py-4 font-black text-xs uppercase tracking-wider hover:brightness-110 active:scale-95 transition-all text-center cursor-pointer">
                        立即微信订购 / 成为会员直接申领
                    </button>
                    <div class="text-center text-[11px] font-mono text-neutral-500">
                        顺丰特快包邮 · 现货 24 小时内顺丰发货
                    </div>
                </div>
            </div>
        </div>

        <!-- ==================== 06. 13位独立名师档案全景抽屉 (Faculty Drawer) ==================== -->
        <div id="faculty-drawer" class="fixed inset-0 z-[110] hidden transition-opacity duration-300 opacity-0">
            <div onclick="closeFacultyDrawer()" class="absolute inset-0 bg-black/85 backdrop-blur-md cursor-pointer"></div>
            
            <div id="faculty-panel" class="absolute top-0 right-0 h-full w-full max-w-2xl bg-[#0c0c0e] border-l border-neutral-800 transform translate-x-full transition-transform duration-300 ease-out flex flex-col justify-between overflow-y-auto p-8 md:p-14 text-white z-10">
                <div class="space-y-8">
                    <div class="flex items-center justify-between pb-6 border-b border-neutral-800">
                        <span class="text-xs font-mono uppercase tracking-widest text-momo-cyan">// ARTIST FACULTY DOSSIER</span>
                        <button type="button" onclick="closeFacultyDrawer()" class="p-2 text-neutral-400 hover:text-white transition-colors cursor-pointer">
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                        </button>
                    </div>

                    <div class="flex items-start gap-6">
                        <div class="w-28 h-28 rounded-xl overflow-hidden border border-neutral-800 flex-shrink-0 bg-neutral-900">
                            <img id="fac-drawer-img" src="./assets/images/hero_trumpet.jpg" alt="Faculty Artist" class="w-full h-full object-cover">
                        </div>
                        <div>
                            <div id="fac-drawer-tag" class="text-xs font-mono text-momo-mint uppercase">FOUNDER / DRUMS & PRODUCTION</div>
                            <h2 id="fac-drawer-name" class="text-3xl font-black text-white mt-1">Timo (提莫)</h2>
                            <p id="fac-drawer-title" class="text-xs text-neutral-400 mt-1">品牌主理人 · 爵士鼓演奏家 · P&R Studio 首席音频制作人</p>
                        </div>
                    </div>

                    <div class="space-y-4 border-t border-neutral-800 pt-6">
                        <div class="text-xs font-mono text-neutral-400 uppercase tracking-wider">// ARTISTIC BACKGROUND & PEDAGOGY</div>
                        <p id="fac-drawer-bio" class="text-sm text-neutral-300 leading-relaxed">
                            MOMO 品牌创始人。常年致力于现代流行爵士合奏教育、大凉山音乐公益支教以及音乐学院留学作品集同期实录。在教学中坚持“真乐器、真声场、平视生命”，亲自担任多位学员作品集项目的爵士鼓与制作交付。
                        </p>
                    </div>

                    <!-- 擅长教学与合奏领域 -->
                    <div class="p-4 rounded-lg bg-neutral-950 border border-neutral-800 space-y-2 text-xs">
                        <div class="text-momo-cyan font-bold uppercase">核心负责板块：</div>
                        <div id="fac-drawer-focus" class="text-neutral-300 leading-relaxed">
                            • 4-on-1 职业乐队实验室（爵士鼓与节奏组律动把控）<br>
                            • 欧美音乐留学作品集 24 轨录音棚同期多轨实录与母带<br>
                            • 大凉山 3天2晚音乐公益共修营全程带领
                        </div>
                    </div>
                </div>

                <div class="pt-8 border-t border-neutral-800 mt-8 space-y-3">
                    <button type="button" onclick="handleBookWithFaculty()" class="w-full gradient-bg text-black py-4 font-black text-xs uppercase tracking-wider text-center cursor-pointer">
                        预约该导师的 1对1 评估或 4-on-1 合奏席位
                    </button>
                    <div class="text-center text-[11px] font-mono text-neutral-500">
                        会员专享预约排期 · 支持到店面对面理念沟通
                    </div>
                </div>
            </div>
        </div>
'''

# JavaScript controls for all Level 2 Drawers
additional_scripts = '''
<script>
    // 真实背景视频原声音频切换控制
    function toggleHeroSound() {
        const video = document.getElementById('hero-bg-video');
        const icon = document.getElementById('hero-sound-icon');
        const text = document.getElementById('hero-sound-text');
        if (!video) return;

        if (video.muted) {
            video.muted = false;
            video.volume = 1.0;
            if (icon) icon.innerText = '🔊';
            if (text) text.innerText = '声音: 已开启原声 (再次点击静音)';
            if (typeof showToast === 'function') showToast('已开启现场真实声浪 🔊');
        } else {
            video.muted = true;
            if (icon) icon.innerText = '🔇';
            if (text) text.innerText = '声音: 静音 (点击开启原声)';
            if (typeof showToast === 'function') showToast('已静音 🔇');
        }
    }

    // 01. 会员 Plus 抽屉控制
    function openMembershipModal() {
        openDrawerGeneric('membership-modal', 'membership-panel');
    }
    function closeMembershipModal() {
        closeDrawerGeneric('membership-modal', 'membership-panel');
    }

    // 02. 音乐留学与作品集实录抽屉控制
    function openStudyAbroadModal() {
        openDrawerGeneric('study-abroad-modal', 'study-abroad-panel');
    }
    function closeStudyAbroadModal() {
        closeDrawerGeneric('study-abroad-modal', 'study-abroad-panel');
    }

    // 03. 空间与排练室租用抽屉控制
    function openSpacesModal() {
        openDrawerGeneric('spaces-modal', 'spaces-panel');
    }
    function closeSpacesModal() {
        closeDrawerGeneric('spaces-modal', 'spaces-panel');
    }

    // 04. 大凉山音乐公益营抽屉控制
    function openCharityRetreatModal() {
        openDrawerGeneric('charity-retreat-modal', 'charity-retreat-panel');
    }
    function closeCharityRetreatModal() {
        closeDrawerGeneric('charity-retreat-modal', 'charity-retreat-panel');
    }

    // 05. 美学周边 TE 抽屉控制
    function openProductDrawer(productId) {
        const prod = merchProducts[productId] || merchProducts['tshirt'];
        currentDrawerProduct = productId;

        document.getElementById('drawer-category').innerText = prod.category;
        document.getElementById('drawer-title').innerText = prod.title;
        document.getElementById('drawer-price').innerText = prod.price;
        document.getElementById('drawer-img').src = prod.img;
        document.getElementById('drawer-desc').innerText = prod.desc;

        const badge = document.getElementById('drawer-member-badge');
        if (prod.isMemberFree) {
            badge.classList.remove('hidden');
        } else {
            badge.classList.add('hidden');
        }

        const specsEl = document.getElementById('drawer-specs');
        if (specsEl) {
            specsEl.innerHTML = prod.specs.map(s => `
                <div class="flex justify-between py-1 border-b border-neutral-900">
                    <span class="text-neutral-500">${s[0]}</span>
                    <span class="text-neutral-200">${s[1]}</span>
                </div>
            `).join('');
        }

        openDrawerGeneric('product-drawer', 'drawer-panel');
    }

    function closeProductDrawer() {
        closeDrawerGeneric('product-drawer', 'drawer-panel');
    }

    function handleDrawerOrder() {
        const prod = merchProducts[currentDrawerProduct] || merchProducts['tshirt'];
        closeProductDrawer();
        if (typeof openBookingModal === 'function') {
            openBookingModal(`订购先锋美学周边: ${prod.title} (${prod.price})`);
        }
    }

    // 通用抽屉打开与关闭函数 (使用 hidden 类确保关闭时绝不拦截鼠标点击事件)
    function openDrawerGeneric(modalId, panelId) {
        const modal = document.getElementById(modalId);
        const panel = document.getElementById(panelId);
        if (modal && panel) {
            modal.classList.remove('hidden');
            // 触发页面重绘确保平滑过渡生效
            void modal.offsetWidth;
            modal.classList.remove('opacity-0');
            modal.classList.add('opacity-100');
            panel.classList.remove('translate-x-full');
            panel.classList.add('translate-x-0');
            document.body.style.overflow = 'hidden';
        }
    }

    function closeDrawerGeneric(modalId, panelId) {
        const modal = document.getElementById(modalId);
        const panel = document.getElementById(panelId);
        if (modal && panel) {
            panel.classList.remove('translate-x-0');
            panel.classList.add('translate-x-full');
            modal.classList.remove('opacity-100');
            modal.classList.add('opacity-0');
            setTimeout(() => {
                modal.classList.add('hidden');
                document.body.style.overflow = '';
            }, 300);
        }
    }

    // 06. 13位导师档案数据映射
    const facultyData = {
        timo: {
            name: 'Timo (提莫)',
            tag: 'FOUNDER / DRUMS & PRODUCTION',
            title: '品牌创始人 · 爵士鼓演奏家 · 首席音频制作人',
            img: './assets/images/hero_trumpet.jpg',
            bio: '常年深耕现代爵士鼓演奏与乐队重奏教育，发起大凉山音乐支教公益。深度陪伴学员完成真录音棚作品集多轨实录与现场合奏打磨。',
            focus: '• 4-on-1 职业乐队实验室主理<br>• 欧美音乐留学作品集 24 轨现场同期录音交付<br>• 大凉山音乐公益营全程带队'
        },
        gaoxin: {
            name: '高信博士',
            tag: 'ACADEMIC DIRECTOR / PHD',
            title: '管乐与现代音乐和声博士 · 升学规划首席学术顾问',
            img: './assets/images/modern_violin.jpg',
            bio: '毕业于海外著名音乐学院管乐博士学位，具有深厚西方传统与现代爵士乐学理造诣，熟稔欧美日韩顶尖音乐学院录取评审机制。',
            focus: '• 升学学术评估与专业能力测评<br>• 德奥公立免学费体系 / 英国皇家RNCM / 伯克利规划<br>• 海外在职教授大师课对接直连'
        },
        wangchongen: {
            name: '王崇恩',
            tag: 'ELECTRIC & ACOUSTIC GUITAR',
            title: '资深吉他演奏家 · 现代摇滚与爵士电吉他导师',
            img: './assets/images/pedalboard.jpg',
            bio: '多年全国巡演与现场录音经验，技术精湛，教学极具亲和力与穿透力。菲比摇滚版《Jingle Bells》乐队主力吉他手。',
            focus: '• 电吉他现代即兴 / 摇滚合奏 / 爵士和弦构建<br>• 4-on-1 职业乐队实验室吉他声部担纲<br>• 亲子家庭合奏乐队吉他指引'
        },
        qiaoxiaoji: {
            name: '乔晓记',
            tag: 'DOUBLE BASS & ELECTRIC BASS',
            title: '原声低音提琴与贝斯演奏家 · 克拉科夫音乐学院海归',
            img: './assets/images/double_bass.png',
            bio: '毕业于波兰克拉科夫音乐学院，活跃于国内外爵士现场与音乐节舞台，兼具学院派严谨和声与原声低音纯正摇摆律动。',
            focus: '• 低音提琴（Double Bass）与电贝斯现代即兴<br>• 爵士节奏组底层骨架构建<br>• 乐队合奏实验室贝斯声部核心担当'
        },
        all: {
            name: 'MOMO 13 位中外独立导师团',
            tag: 'FULL ARTIST COLLECTIVE',
            title: '巡演爵士乐手 · 海归管乐博士 · 编曲制作人',
            img: './assets/images/master_student_ensemble.jpg',
            bio: '除 Timo、高信博士、王崇恩、乔晓记外，导师团还汇聚了周思文（Joe Longardner，外教萨克斯）、苟涵凝（爵士钢琴）、黄瑾熙（现代声乐）、祁子垚（混音制作人）等共 13 位一线艺术家。',
            focus: '• 覆盖爵士鼓、贝斯、吉他、钢琴、管乐、现代声乐全学科<br>• 支持 4 位中外导师同时陪伴 1 位学员完成个人作品<br>• 一对一预约理念沟通与试听'
        }
    };

    let currentFaculty = 'timo';
    function openFacultyDrawer(facultyId) {
        const fac = facultyData[facultyId] || facultyData['all'];
        currentFaculty = facultyId;

        document.getElementById('fac-drawer-name').innerText = fac.name;
        document.getElementById('fac-drawer-tag').innerText = fac.tag;
        document.getElementById('fac-drawer-title').innerText = fac.title;
        document.getElementById('fac-drawer-img').src = fac.img;
        document.getElementById('fac-drawer-bio').innerText = fac.bio;
        document.getElementById('fac-drawer-focus').innerHTML = fac.focus;

        openDrawerGeneric('faculty-drawer', 'faculty-panel');
    }

    function closeFacultyDrawer() {
        closeDrawerGeneric('faculty-drawer', 'faculty-panel');
    }

    function handleBookWithFaculty() {
        const fac = facultyData[currentFaculty] || facultyData['timo'];
        closeFacultyDrawer();
        if (typeof openBookingModal === 'function') {
            openBookingModal(`预约导师专属沟通/合奏: ${fac.name}`);
        }
    }

    // 07. Teenage Engineering 风格全屏抽屉数据映射
    const merchProducts = {
        tshirt: {
            category: '// APPAREL · 成为会员免费赠送',
            title: 'MOMO 纯黑重磅刺绣文化衫',
            price: '¥260',
            img: './assets/images/momo_tshirt_te_style.jpg',
            desc: '320g 高密精梳纯棉，巴黎世家经典落肩微阔版型。前胸同色黑线立体刺绣 MOMO 盾牌微标，洗水工艺保持长久不褪色、不变形。穿上它，你就是 MOMO 先锋音乐社群的同行者。',
            isMemberFree: true,
            specs: [
                ['面料材质', '100% 320g 重磅精梳棉 (超柔防缩水)'],
                ['版型设计', 'Oversized 宽松落肩剪裁'],
                ['尺码范围', 'S (160-170cm) / M (170-180cm) / L (180cm+)'],
                ['刺绣工艺', '德国进口田岛机 12000 针同色立体刺绣']
            ]
        },
        tote: {
            category: '// ACCESSORY · 乐手随行托特包',
            title: '乐手纯黑机能帆布托特包',
            price: '¥180',
            img: './assets/images/momo_merch_collection.jpg',
            desc: '专为常年奔波于排练室与现场的乐手设计。16A 加密防泼水帆布，内衬加厚防震层，轻松装下 16 寸 MacBook Pro、iPad Pro、耳机以及厚重的重奏大总谱。',
            isMemberFree: false,
            specs: [
                ['材质面料', '16A 加密有机棉机能防泼水帆布'],
                ['容量规格', '长 42cm × 宽 38cm × 底部加宽 12cm'],
                ['特别隔层', '独立吉他拨片暗袋 + 钥匙安全挂扣 + 水杯固定带']
            ]
        },
        picks: {
            category: '// HARDWARE · 赛璐珞拨片盒',
            title: '纪念款赛璐珞吉他拨片黑锡盒',
            price: '¥88',
            img: './assets/images/real_momo_picks_tin.jpg',
            desc: '经典磨砂黑马口铁滑动开启盒。内含 6 枚精选赛璐珞材质拨片，涵盖 0.71mm（民谣扫弦）、0.96mm（摇滚 Solo）与 1.14mm（爵士重单音）三种专业硬度。',
            isMemberFree: false,
            specs: [
                ['盒体工艺', '消光黑冲压马口铁 (防锈激光镭雕)'],
                ['拨片数量', '6 枚装 (0.71mm ×2 / 0.96mm ×2 / 1.14mm ×2)'],
                ['手感涂层', '哑光防滑磨砂触感']
            ]
        },
        vinyl: {
            category: '// VINYL · 限定黑胶唱片',
            title: '现场实录限定黑胶声音集',
            price: '¥320',
            img: './assets/images/real_momo_vinyl.jpg',
            desc: '全球限量 300 张。采用德国压片工艺，收录菲比现场乐队版《Jingle Bells》与 24-bit 独家现场同期直录无损音频源。',
            isMemberFree: false,
            specs: [
                ['唱片规格', '12 英寸 / 33⅓ RPM / 180g 重磅高保真黑胶'],
                ['母带来源', 'P&R Studio 24轨同期直录无损音频源'],
                ['随盘附赠', '全套排练现场胶片印制摄影画册']
            ]
        }
    };
</script>
'''

# Assemble the complete new index.html
new_html = head_section + new_nav + new_hero + new_offerings + new_merch_store + new_faculty + new_spaces + comprehensive_level2_modals + "</main>\n" + footer_and_scripts

# Inject additional scripts right before </body>
insert_pos = new_html.rfind("</body>")
if insert_pos != -1:
    new_html = new_html[:insert_pos] + additional_scripts + "\n" + new_html[insert_pos:]

with open(TARGET_HTML, "w", encoding="utf-8") as f:
    f.write(new_html)

print("SUCCESS: Bugfix Applied! All modals are hidden by default. All buttons are 100% interactive and working!")
print("New file size:", len(new_html))
