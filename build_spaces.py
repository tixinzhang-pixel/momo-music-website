# -*- coding: utf-8 -*-
"""
Generate spaces.html:
Includes:
- 隐于成熟小区的私密声场：排练、会议、录音与 60㎡ 户外花园
- 空间使用不在页面标金额，欢迎来访或咨询
- 乐器使用不在页面标金额，欢迎来访或咨询
- 会员专享 欢迎来访或咨询特权与优先锁档
- 预约表单与客服
"""

import os

WEBSITE_DIR = "/Users/timomo/Documents/Momo音乐工作坊总文件/MomoMusicWebsite"
TARGET_FILE = os.path.join(WEBSITE_DIR, "spaces.html")

COMMON_HEAD_DEFS = '''
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;700;800&family=Noto+Sans+SC:wght@300;400;500;700;900&family=Playfair+Display:ital,wght@0,600;0,900;1,600&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        momo: {
                            cyan: '#00C9FF',
                            mint: '#92FE9D',
                            teal: '#00dfd8',
                            dark: '#080808',
                            card: '#0f0f0f',
                            border: '#1f1f1f'
                        }
                    },
                    fontFamily: {
                        sans: ['Inter', 'Noto Sans SC', 'system-ui', 'sans-serif'],
                        mono: ['JetBrains Mono', 'monospace'],
                        serif: ['Playfair Display', 'serif']
                    }
                }
            }
        }
    </script>
    <style>
        .gradient-text {
            background: linear-gradient(135deg, #00C9FF 0%, #92FE9D 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .gradient-bg {
            background: linear-gradient(135deg, #00C9FF 0%, #92FE9D 100%);
        }
        .brutalist-border {
            border: 1px solid #222222;
            transition: all 0.25s ease;
        }
        .brutalist-border:hover {
            border-color: #00C9FF;
        }
    </style>
'''

COMMON_SVG_LOGO = '''
<svg class="h-8 w-auto transform group-hover:scale-105 transition-transform duration-300" viewBox="0 0 100 120" xmlns="http://www.w3.org/2000/svg">
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
'''

def get_shared_footer(depth=0):
    root = "./" if depth == 0 else "../"
    home_href = f"{root}index.html"
    mem_href = f"{root}membership.html"
    study_href = f"{root}study-abroad.html"
    space_href = f"{root}spaces.html"
    store_href = f"{root}store/index.html"

    return f'''
    <footer class="bg-black text-white pt-20 pb-12 px-6 md:px-12 border-t border-neutral-900 mt-20">
        <div class="max-w-7xl mx-auto">
            <div class="grid grid-cols-1 md:grid-cols-12 gap-12 pb-14 border-b border-neutral-800">
                <div class="md:col-span-5 space-y-6">
                    <div class="flex items-center gap-3">
                        {COMMON_SVG_LOGO}
                        <span class="text-2xl font-black uppercase tracking-tight">Momo Family Music</span>
                    </div>
                    <p class="text-neutral-400 text-xs leading-relaxed max-w-sm">
                        KIND • TRUTH • PASSION。<br>
                        <strong>CO-CREATE THE SOUND OF LIFE.</strong> 作为成都先锋音乐生活服务品牌，我们以爵士音乐艺术家与专业音乐制作人团队为底座，带领每个家庭与个体在真乐队合奏与创作中共创美好的音乐生活。
                    </p>
                    <div class="text-xs text-neutral-500 font-mono">
                        Chengdu Avant-Garde Music Lifestyle Brand &amp; Global Conservatory Prep.
                    </div>
                </div>

                <div class="md:col-span-2 space-y-3">
                    <h4 class="text-xs font-black uppercase tracking-widest text-neutral-400">核心生态与服务</h4>
                    <ul class="text-xs space-y-2 text-neutral-300">
                        <li><a href="{home_href}#offerings" class="hover:text-momo-cyan">产品与活动总览</a></li>
                        <li><a href="{mem_href}" class="hover:text-momo-cyan text-momo-mint font-bold">家庭年费会员 Plus (欢迎来访或咨询)</a></li>
                        <li><a href="{study_href}" class="hover:text-[#D4AF37] text-[#D4AF37] font-bold">作品与方向 (欢迎来访或咨询)</a></li>
                        <li><a href="{space_href}" class="hover:text-momo-cyan">空间与乐器租用</a></li>
                        <li><a href="{store_href}" class="hover:text-momo-cyan">Momo 音乐美学商店</a></li>
                    </ul>
                </div>

                <div class="md:col-span-2 space-y-3">
                    <h4 class="text-xs font-black uppercase tracking-widest text-neutral-400">学术、学科与公益</h4>
                    <ul class="text-xs space-y-2 text-neutral-300">
                        <li><a href="{home_href}#style-deck" class="hover:text-momo-mint">音乐风格声波卡片机</a></li>
                        <li><a href="{home_href}#matrix" class="hover:text-momo-mint">全系现代乐器矩阵</a></li>
                        <li><a href="{home_href}#faculty" class="hover:text-momo-mint">13位艺术家导师长廊</a></li>
                        <li><a href="{home_href}#charity" class="hover:text-momo-mint">大凉山音乐支教共修营</a></li>
                    </ul>
                </div>

                <div class="md:col-span-3 space-y-4">
                    <h4 class="text-xs font-black uppercase tracking-widest text-neutral-400">联络与主理人直通</h4>
                    <div class="text-xs text-neutral-300 space-y-2 font-mono">
                        <div class="text-momo-cyan font-bold">Timo 品牌创始人: tixinzhang@gmail.com</div>
                        <div class="text-neutral-400">学术顾问与艺术家导师团全程配合</div>
                        <div class="text-[11px] leading-relaxed text-neutral-400 pt-1">
                            📍 桐梓林空间: 成都市武侯区银都花园14栋2单元101<br>
                            📍 麓湖空间: 成都市天府新区麓坊中心A座1栋811
                        </div>
                    </div>
                    <a href="{home_href}#booking" class="block text-center gradient-bg text-black font-black text-xs uppercase py-3 tracking-wider hover:opacity-90">
                        预约到店体验 / 线上理念沟通 &#8594;
                    </a>
                </div>
            </div>

            <div class="pt-8 text-center text-xs font-mono text-neutral-600">
                &copy; 2026 MOMO FAMILY MUSIC STUDIO · KIND • TRUTH • PASSION. ALL RIGHTS RESERVED.
            </div>
        </div>
    </footer>
    '''

def build_spaces():
    html = f'''<!DOCTYPE html>
<html lang="zh-CN" class="dark scroll-smooth">
<head>
    <title>城市音乐共享空间与专业乐器租用 · 桐梓林与麓湖双空间 · Momo</title>
    {COMMON_HEAD_DEFS}
</head>
<body class="bg-black text-white antialiased font-sans pt-24 selection:bg-momo-cyan selection:text-black">
    <header class="fixed top-0 left-0 w-full z-50 bg-[#080808]/90 backdrop-blur-md border-b border-neutral-900 py-3.5 px-6 md:px-12">
        <div class="max-w-7xl mx-auto flex items-center justify-between">
            <a href="./index.html" class="flex items-center gap-3 group text-left">
                {COMMON_SVG_LOGO}
                <div class="flex flex-col">
                    <span class="text-base sm:text-lg font-black tracking-tight leading-none text-white uppercase group-hover:text-momo-cyan transition-colors">
                        Momo Family
                    </span>
                    <span class="text-[9px] sm:text-[10px] uppercase font-bold tracking-widest text-neutral-400 mt-0.5">
                        Music Studio • Chengdu & Global
                    </span>
                </div>
            </a>

            <nav class="hidden lg:flex items-center gap-7">
                <a href="./index.html#offerings" class="text-xs uppercase font-bold tracking-widest text-neutral-300 hover:text-momo-cyan transition-colors">
                    产品货架
                </a>
                <a href="./membership.html" class="text-xs uppercase font-bold tracking-widest text-neutral-300 hover:text-momo-cyan transition-colors">
                    年费会员 PLUS (欢迎来访或咨询)
                </a>
                <a href="./study-abroad.html" class="text-xs uppercase font-bold tracking-widest text-neutral-300 hover:text-[#D4AF37] transition-colors">
                    作品与方向
                </a>
                <a href="./spaces.html" class="text-xs uppercase font-bold tracking-widest text-momo-mint font-mono">
                    空间与乐器租用
                </a>
                <a href="./store/index.html" class="text-xs uppercase font-bold tracking-widest text-neutral-300 hover:text-momo-cyan transition-colors">
                    Momo 音乐美学商店
                </a>
            </nav>

            <a href="./index.html#booking" class="gradient-bg text-black px-5 py-2 font-black text-xs uppercase tracking-wider hover:opacity-90">
                预约体验 / 租用咨询
            </a>
        </div>
    </header>

    <main class="max-w-7xl mx-auto px-6 md:px-12 py-12">
        <!-- 头部 Hero -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center mb-16 pb-16 border-b border-neutral-900">
            <div class="lg:col-span-7 space-y-6">
                <span class="text-xs font-mono font-bold uppercase tracking-widest text-momo-mint block">// URBAN PRIVATE MUSIC SALON &amp; REHEARSAL &amp; GEAR RENTAL</span>
                <h1 class="text-3xl sm:text-5xl md:text-6xl font-black uppercase tracking-tight text-white leading-tight">
                    隐于成熟小区的私密声场：<br>
                    <span class="gradient-text">排练、会议、录音与 60㎡ 户外花园</span>
                </h1>
                <p class="text-neutral-300 text-sm sm:text-base leading-relaxed">
                    桐梓林空间位于成都市武侯区银都花园14栋2单元101，是一处隐秘于高端成熟居民小区内的私密独栋音乐沙龙。远离闹市喧嚣，拥有独立的中央吧台、专业声学隔音琴房与排练大厅，并独享 60 平方米私家庭院花园。
                </p>
                <div class="inline-flex items-center gap-2 px-3 py-1.5 bg-momo-mint/10 border border-momo-mint/30 rounded text-momo-mint text-xs font-mono">
                    <span>空间与乐器如何使用，欢迎来访或咨询。</span>
                </div>
            </div>

            <div class="lg:col-span-5">
                <div class="aspect-[4/3] brutalist-border bg-neutral-950 overflow-hidden relative">
                    <img src="./assets/images/momo_garden_space.jpg" alt="Momo Garden Space" class="w-full h-full object-cover">
                </div>
                <div class="text-[11px] font-mono text-neutral-500 mt-3 text-center">
                    // TONGZILIN GARDEN MUSIC SALON · 60㎡ 私家庭院与中央吧台
                </div>
            </div>
        </div>

        <!-- 空间场地使用 (6大类目) -->
        <div class="mb-20">
            <div class="flex flex-col sm:flex-row sm:items-end justify-between mb-8 pb-4 border-b border-neutral-800">
                <div>
                    <span class="text-xs font-mono text-momo-cyan uppercase tracking-widest">// VENUE RENTALS</span>
                    <h2 class="text-2xl sm:text-4xl font-black uppercase text-white mt-1">空间线下场地租用明细</h2>
                </div>
                <span class="text-xs font-mono text-neutral-400 mt-2 sm:mt-0">欢迎来访或咨询</span>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <!-- 01: 琴房练琴 -->
                <div class="brutalist-border bg-neutral-950 p-6 flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between">
                            <span class="text-xs font-mono text-momo-cyan font-bold uppercase">VENUE 01</span>
                            <span class="text-[10px] font-mono px-2 py-0.5 bg-neutral-900 text-neutral-300 border border-neutral-800">专业隔音</span>
                        </div>
                        <h3 class="text-xl font-black text-white mt-2">琴房日常练琴</h3>
                        <p class="text-xs text-neutral-400 mt-2 leading-relaxed">
                            独立声学隔音舱，免受外界打扰。备有声学原声钢琴、Nord 电钢、吉他与监听耳机，适合个人练琴与声乐开嗓。
                        </p>
                    </div>
                    <div class="pt-6 border-t border-neutral-900 mt-6 flex items-baseline justify-between">
                        <div class="text-3xl font-black text-white">欢迎来访或咨询</div>
                        <span class="text-xs font-mono text-momo-mint font-bold">欢迎来访或咨询</span>
                    </div>
                </div>

                <!-- 02: 乐队排练 -->
                <div class="brutalist-border bg-neutral-950 p-6 flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between">
                            <span class="text-xs font-mono text-momo-mint font-bold uppercase">VENUE 02</span>
                            <span class="text-[10px] font-mono px-2 py-0.5 bg-momo-mint/10 text-momo-mint border border-momo-mint/30">全套乐器全配</span>
                        </div>
                        <h3 class="text-xl font-black text-white mt-2">乐队封闭排练</h3>
                        <p class="text-xs text-neutral-400 mt-2 leading-relaxed">
                            全套 Gretsch 爵士套鼓、Fender/Marshall 电子管吉他箱、Ampeg 贝斯箱、Nord 电钢及专业 PA 监听系统，乐手到场插线即开演。
                        </p>
                    </div>
                    <div class="pt-6 border-t border-neutral-900 mt-6 flex items-baseline justify-between">
                        <div class="text-3xl font-black text-white">欢迎来访或咨询</div>
                        <span class="text-xs font-mono text-momo-mint font-bold">欢迎来访或咨询</span>
                    </div>
                </div>

                <!-- 03: 乐队现场录音 -->
                <div class="brutalist-border bg-neutral-950 p-6 flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between">
                            <span class="text-xs font-mono text-[#D4AF37] font-bold uppercase">VENUE 03</span>
                            <span class="text-[10px] font-mono px-2 py-0.5 bg-[#D4AF37]/10 text-[#D4AF37] border border-[#D4AF37]/30">P&R 录音师掌舵</span>
                        </div>
                        <h3 class="text-xl font-black text-white mt-2">乐队现场多轨录音</h3>
                        <p class="text-xs text-neutral-400 mt-2 leading-relaxed">
                            由 P&amp;R Studio 首席音频工程师掌舵，开启工业级 24 轨数字/模拟同期录音系统，现场同期捕捉真乐队演奏呼吸与动态。
                        </p>
                    </div>
                    <div class="pt-6 border-t border-neutral-900 mt-6 flex items-baseline justify-between">
                        <div class="text-3xl font-black text-white">欢迎来访或咨询</div>
                        <span class="text-xs font-mono text-neutral-400">含分轨工程文件导出</span>
                    </div>
                </div>

                <!-- 04: 会议 & 沙龙 -->
                <div class="brutalist-border bg-neutral-950 p-6 flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between">
                            <span class="text-xs font-mono text-momo-cyan font-bold uppercase">VENUE 04</span>
                            <span class="text-[10px] font-mono px-2 py-0.5 bg-neutral-900 text-neutral-300 border border-neutral-800">10～40 人容量</span>
                        </div>
                        <h3 class="text-xl font-black text-white mt-2">企划会议 &amp; 文化沙龙</h3>
                        <p class="text-xs text-neutral-400 mt-2 leading-relaxed">
                            配备 4K 智能无线投屏系统、专业无线麦克风与独立空调。中央实木吧台现磨咖啡全天候供应，直通室外私家花园。
                        </p>
                    </div>
                    <div class="pt-6 border-t border-neutral-900 mt-6 flex items-baseline justify-between">
                        <div class="text-3xl font-black text-white">欢迎来访或咨询</div>
                        <span class="text-xs font-mono text-momo-mint font-bold">欢迎来访或咨询</span>
                    </div>
                </div>

                <!-- 05: 室内音乐会 -->
                <div class="brutalist-border bg-neutral-950 p-6 flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between">
                            <span class="text-xs font-mono text-momo-mint font-bold uppercase">VENUE 05</span>
                            <span class="text-[10px] font-mono px-2 py-0.5 bg-momo-mint/10 text-momo-mint border border-momo-mint/30">30-50 观众席位</span>
                        </div>
                        <h3 class="text-xl font-black text-white mt-2">室内私密音乐会</h3>
                        <p class="text-xs text-neutral-400 mt-2 leading-relaxed">
                            打造小而美的高质感现场！提供观众席位编排、舞台暖光氛围、现场收音与中央吧台迎宾服务，适合乐手个人专场与小型室内乐发表。
                        </p>
                    </div>
                    <div class="pt-6 border-t border-neutral-900 mt-6 flex items-baseline justify-between">
                        <div class="text-3xl font-black text-white">欢迎来访或咨询</div>
                        <span class="text-xs font-mono text-neutral-400">单场约 2.5 小时演展</span>
                    </div>
                </div>

                <!-- 06: 音乐派对全空间包场 -->
                <div class="brutalist-border bg-neutral-950 p-6 flex flex-col justify-between border-momo-cyan/40">
                    <div>
                        <div class="flex items-center justify-between">
                            <span class="text-xs font-mono text-momo-cyan font-bold uppercase">VENUE 06 · VIP</span>
                            <span class="text-[10px] font-mono px-2 py-0.5 bg-momo-cyan text-black font-black uppercase">全场通包</span>
                        </div>
                        <h3 class="text-xl font-black text-white mt-2">音乐派对全空间整场包场</h3>
                        <p class="text-xs text-neutral-400 mt-2 leading-relaxed">
                            排练大厅 + 隔音琴房 + 中央精品咖啡吧台 + 60㎡ 阳光庭院整场私密独享！专属门禁密码，支持家庭庆典、周年派对、企业高端定制。
                        </p>
                    </div>
                    <div class="pt-6 border-t border-neutral-900 mt-6 flex items-baseline justify-between">
                        <div class="text-3xl font-black text-white">欢迎来访或咨询</div>
                        <span class="text-xs font-mono text-momo-mint font-bold">超值包场特权</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- 专业乐器使用 (6大硬件) -->
        <div class="mb-20">
            <div class="flex flex-col sm:flex-row sm:items-end justify-between mb-8 pb-4 border-b border-neutral-800">
                <div>
                    <span class="text-xs font-mono text-momo-mint uppercase tracking-widest">// GEAR RENTAL</span>
                    <h2 class="text-2xl sm:text-4xl font-black uppercase text-white mt-1">专业乐器对外租用明细</h2>
                </div>
                <span class="text-xs font-mono text-neutral-400 mt-2 sm:mt-0">巡演级硬件 · 支持日租与按周长租</span>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
                <!-- 01: 架子鼓全套 -->
                <div class="brutalist-border bg-[#0d0d0d] p-6 space-y-4">
                    <div class="text-xs font-mono text-momo-mint font-bold uppercase">DRUM KIT · 01</div>
                    <h3 class="text-xl font-bold text-white">专业架子鼓全套</h3>
                    <p class="text-xs text-neutral-400 leading-relaxed">
                        经典 Gretsch 爵士/流行套鼓，配全套 Zildjian/Sabian 专业合金镲片、踩槌底鼓与稳固硬件支架，声音饱满，现场炸裂。
                    </p>
                    <div class="pt-4 border-t border-neutral-900 flex justify-between items-baseline">
                        <span class="text-2xl font-black text-white">欢迎来访或咨询</span>
                        <span class="text-xs font-mono text-neutral-500">押金随租随退</span>
                    </div>
                </div>

                <!-- 02: 满氏木吉他 -->
                <div class="brutalist-border bg-[#0d0d0d] p-6 space-y-4">
                    <div class="text-xs font-mono text-momo-cyan font-bold uppercase">ACOUSTIC GUITAR · 02</div>
                    <h3 class="text-xl font-bold text-white">满氏手工全单木吉他</h3>
                    <p class="text-xs text-neutral-400 leading-relaxed">
                        独立制琴名家手工打造，精选全单云杉配玫瑰木背侧，低频沉稳通透，高频如水晶般温润，专为舞台指弹与高阶弹唱而备。
                    </p>
                    <div class="pt-4 border-t border-neutral-900 flex justify-between items-baseline">
                        <span class="text-2xl font-black text-white">欢迎来访或咨询</span>
                        <span class="text-xs font-mono text-neutral-500">含原装加厚琴包</span>
                    </div>
                </div>

                <!-- 03: 经典电吉他 -->
                <div class="brutalist-border bg-[#0d0d0d] p-6 space-y-4">
                    <div class="text-xs font-mono text-momo-mint font-bold uppercase">ELECTRIC GUITAR · 03</div>
                    <h3 class="text-xl font-bold text-white">经典电吉他 (Fender / Gibson)</h3>
                    <p class="text-xs text-neutral-400 leading-relaxed">
                        涵盖 Stratocaster / Les Paul 经典型号，弦距经过资深琴匠严谨调校，手感舒适，音色极具穿透力，适应摇滚、流行与现代爵士。
                    </p>
                    <div class="pt-4 border-t border-neutral-900 flex justify-between items-baseline">
                        <span class="text-2xl font-black text-white">欢迎来访或咨询</span>
                        <span class="text-xs font-mono text-neutral-500">含高品质音频线</span>
                    </div>
                </div>

                <!-- 04: 专业电钢琴 -->
                <div class="brutalist-border bg-[#0d0d0d] p-6 space-y-4">
                    <div class="text-xs font-mono text-momo-cyan font-bold uppercase">STAGE PIANO · 04</div>
                    <h3 class="text-xl font-bold text-white">专业舞台电钢琴 (Nord / Roland)</h3>
                    <p class="text-xs text-neutral-400 leading-relaxed">
                        88 键全配重重锤琴键，逼真还原声学大三角钢琴手感，内置顶级古典钢琴与经典 Rhodes 复古电钢琴音色，配延音踏板与支架。
                    </p>
                    <div class="pt-4 border-t border-neutral-900 flex justify-between items-baseline">
                        <span class="text-2xl font-black text-white">欢迎来访或咨询</span>
                        <span class="text-xs font-mono text-neutral-500">含原装延音踏板</span>
                    </div>
                </div>

                <!-- 05: 低音贝斯 -->
                <div class="brutalist-border bg-[#0d0d0d] p-6 space-y-4">
                    <div class="text-xs font-mono text-[#D4AF37] font-bold uppercase">BASS DEPARTMENT · 05</div>
                    <h3 class="text-xl font-bold text-white">低音贝斯 (Double Bass / 电贝斯)</h3>
                    <p class="text-xs text-neutral-400 leading-relaxed">
                        提供稀缺的<strong>原声低音提琴 Double Bass（爵士/古典名琴）</strong>或 <strong>Fender 经典 Jazz Bass 电贝斯</strong>，经过声学拾音调校，低频雄浑扎实。
                    </p>
                    <div class="pt-4 border-t border-neutral-900 flex justify-between items-baseline">
                        <span class="text-2xl font-black text-white">欢迎来访或咨询</span>
                        <span class="text-xs font-mono text-neutral-500">稀缺大师级专业低音</span>
                    </div>
                </div>

                <!-- 06: 罗兰 Cube 音响 -->
                <div class="brutalist-border bg-[#0d0d0d] p-6 space-y-4">
                    <div class="text-xs font-mono text-momo-mint font-bold uppercase">AMPLIFIER · 06</div>
                    <h3 class="text-xl font-bold text-white">罗兰 Roland Cube 经典便携音响</h3>
                    <p class="text-xs text-neutral-400 leading-relaxed">
                        街头巡演与移动展演的传奇设备！支持电池供电与交流电源，配备麦克风与乐器双通道独立混音，内置经典空间混响与和声效果。
                    </p>
                    <div class="pt-4 border-t border-neutral-900 flex justify-between items-baseline">
                        <span class="text-2xl font-black text-white">欢迎来访或咨询</span>
                        <span class="text-xs font-mono text-neutral-500">户外展演利器</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- 空间与乐器租用预约表单 -->
        <div class="max-w-2xl mx-auto brutalist-border bg-neutral-950 p-8 sm:p-12 mb-16">
            <h3 class="text-2xl font-black uppercase text-white text-center mb-2">预约空间场地或租借专业乐器</h3>
            <p class="text-xs font-mono text-neutral-400 text-center mb-8">场地与乐器安排，欢迎来访或咨询</p>
            <form onsubmit="handleSpaceForm(event)" class="space-y-4">
                <div>
                    <label class="text-xs font-mono text-neutral-400 block mb-1">预约人称呼 / 乐队名称 *</label>
                    <input type="text" id="space-name" required placeholder="如：李先生 / Blue Note Trio" class="w-full bg-neutral-900 border border-neutral-800 px-4 py-3 text-xs text-white focus:outline-none focus:border-momo-cyan">
                </div>
                <div>
                    <label class="text-xs font-mono text-neutral-400 block mb-1">微信号 / 手机号 *</label>
                    <input type="text" id="space-phone" required placeholder="如：13900000000 (微信同号)" class="w-full bg-neutral-900 border border-neutral-800 px-4 py-3 text-xs text-white focus:outline-none focus:border-momo-cyan">
                </div>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div>
                        <label class="text-xs font-mono text-neutral-400 block mb-1">预约租用类目</label>
                        <select id="space-type" class="w-full bg-neutral-900 border border-neutral-800 px-3 py-3 text-xs text-white">
                            <optgroup label="—— 空间场地租用 ——">
                                <option value="琴房练琴（欢迎来访或咨询）">琴房练琴（欢迎来访或咨询）</option>
                                <option value="乐队排练（欢迎来访或咨询）">乐队排练（欢迎来访或咨询）</option>
                                <option value="现场录音（欢迎来访或咨询）">乐队现场多轨录音（欢迎来访或咨询）</option>
                                <option value="会议沙龙（欢迎来访或咨询）">企划会议与沙龙（欢迎来访或咨询）</option>
                                <option value="室内音乐会（欢迎来访或咨询）">室内音乐会（欢迎来访或咨询）</option>
                                <option value="全空间包场（欢迎来访或咨询）">全空间包场（欢迎来访或咨询）</option>
                            </optgroup>
                            <optgroup label="—— 专业乐器租用 ——">
                                <option value="全套架子鼓（欢迎来访或咨询）">全套架子鼓（欢迎来访或咨询）</option>
                                <option value="满氏木吉他（欢迎来访或咨询）">满氏手工木吉他（欢迎来访或咨询）</option>
                                <option value="经典电吉他（欢迎来访或咨询）">经典电吉他（欢迎来访或咨询）</option>
                                <option value="专业电钢琴（欢迎来访或咨询）">专业舞台电钢琴（欢迎来访或咨询）</option>
                                <option value="低音贝斯（欢迎来访或咨询）">低音贝斯（欢迎来访或咨询）</option>
                                <option value="罗兰Cube音响（欢迎来访或咨询）">罗兰 Roland Cube 音响（欢迎来访或咨询）</option>
                            </optgroup>
                        </select>
                    </div>
                    <div>
                        <label class="text-xs font-mono text-neutral-400 block mb-1">期望使用日期与预计时长</label>
                        <input type="text" id="space-date" placeholder="如：本周六 14:00-17:00 (排练3小时)" class="w-full bg-neutral-900 border border-neutral-800 px-4 py-3 text-xs text-white focus:outline-none focus:border-momo-cyan">
                    </div>
                </div>
                <button type="submit" class="w-full gradient-bg text-black py-4 font-black text-xs uppercase tracking-wider hover:opacity-95">
                    提交租用预约申请 &rarr;
                </button>
            </form>
        </div>
    </main>

    <script>
        function handleSpaceForm(e) {{
            e.preventDefault();
            const phone = document.getElementById('space-phone').value;
            const item = document.getElementById('space-type').value;
            alert('租用申请已受理！【' + item + '】\\n主理人团队将在 2 小时内与您联络（' + phone + '）确认档期与自提/门禁安排。');
        }}
    </script>

    {get_shared_footer(depth=0)}
</body>
</html>
'''
    with open(TARGET_FILE, "w", encoding="utf-8") as f:
        f.write(html)
    print("SUCCESS: spaces.html compiled!")

if __name__ == "__main__":
    build_spaces()
