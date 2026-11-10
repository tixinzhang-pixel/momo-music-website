# -*- coding: utf-8 -*-
"""
Generate membership.html and ensemble-lab.html:
1. membership.html:
   - 2026 Plus Family Membership official page
   - Platinum Titanium 3D card display
   - Philosophy statement (因为音乐需要大家一起玩起来)
   - 「会员包含的核心实战项目与尊享权益大赏」:
     Uses the exact brutalist card format from Timo's screenshot:
     #01 4-on-1 职业乐队实验室 (¥400/30min 或 会员直接划扣1次额度)
     #02 3-7岁 全家庭周末合奏包 (400¥/45min 或 会员直接划扣)
     #03 P&R Studio 24轨现场唱片级录制 (仅耗 1 次课时)
     #04 城市真实舞台通行证 (香格里拉圣诞专案 · 非内卷选拔 · 自然登台)
     #05 3次 全年家庭音乐成长与教育规划深度诊断 (3小时面对面)
     #06 城市音乐共享空间与琴房 5 折特权 (琴房40/h, 排练100/h, 录音250/h)
     #07 会员专属礼遇：MOMO 纯黑刺绣重磅文化衫 (免费赠送 · 标价¥260)
   - 2026 Plus 五大核心保障
   - 入会预约申请表单 + 7天无理由退款承诺 + FAQ
2. ensemble-lab.html:
   - Dedicated deep-dive page for 4-on-1 职业乐队实验室
   - Real recording studio photography (real_ensemble_rehearsal.jpg)
   - Band rhythm section breakdown (鼓手、贝斯、吉他、键盘)
   - Dual-track access: 单次体验 ¥400/30min vs 年费会员 ¥6,000 划扣
   - Direct seat reservation form
"""

import os

WEBSITE_DIR = "/Users/timomo/Documents/Momo音乐工作坊总文件/MomoMusicWebsite"

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

def get_shared_header(current_page="membership", depth=0):
    root = "./" if depth == 0 else "../"
    store_href = f"{root}store/index.html"
    mem_href = f"{root}membership.html"
    study_href = f"{root}study-abroad.html"
    space_href = f"{root}spaces.html"
    home_href = f"{root}index.html"

    return f'''
    <header class="fixed top-0 left-0 w-full z-50 bg-[#080808]/90 backdrop-blur-md border-b border-neutral-900 transition-all duration-300 py-3.5 px-6 md:px-12">
        <div class="max-w-7xl mx-auto flex items-center justify-between">
            <a href="{home_href}" class="flex items-center gap-3 group text-left focus:outline-none">
                {COMMON_SVG_LOGO}
                <div class="flex flex-col">
                    <span class="text-base sm:text-lg font-black tracking-tight leading-none text-white uppercase group-hover:text-momo-cyan transition-colors">
                        Momo Family
                    </span>
                    <span class="text-[9px] sm:text-[10px] uppercase font-bold tracking-widest text-neutral-400 mt-0.5">
                        Music Studio • Chengdu &amp; Global
                    </span>
                </div>
            </a>

            <nav class="hidden lg:flex items-center gap-7">
                <a href="{home_href}#offerings" class="text-xs uppercase font-bold tracking-widest text-neutral-300 hover:text-momo-cyan transition-colors flex items-center gap-1.5">
                    <span>产品货架</span>
                    <span class="text-[9px] px-1.5 py-0.5 rounded bg-neutral-800 text-momo-mint font-mono">OFFERINGS</span>
                </a>
                <a href="{mem_href}" class="text-xs uppercase font-bold tracking-widest {'text-momo-cyan' if current_page=='membership' else 'text-neutral-300'} hover:text-momo-cyan transition-colors flex items-center gap-1.5">
                    <span>年费会员 PLUS</span>
                    <span class="text-[9px] px-1.5 py-0.5 rounded bg-neutral-800 text-momo-cyan font-mono">¥6,000</span>
                </a>
                <a href="{study_href}" class="text-xs uppercase font-bold tracking-widest text-neutral-300 hover:text-[#D4AF37] transition-colors flex items-center gap-1.5">
                    <span>音乐留学规划</span>
                    <span class="text-[9px] px-1.5 py-0.5 rounded bg-neutral-800 text-[#D4AF37] font-mono">¥38,800</span>
                </a>
                <a href="{space_href}" class="text-xs uppercase font-bold tracking-widest text-neutral-300 hover:text-momo-cyan transition-colors flex items-center gap-1.5">
                    <span>空间与乐器租用</span>
                    <span class="text-[9px] px-1.5 py-0.5 rounded bg-neutral-800 text-neutral-400 font-mono">SPACES</span>
                </a>
                <a href="{store_href}" class="text-xs uppercase font-bold tracking-widest text-neutral-300 hover:text-momo-cyan transition-colors flex items-center gap-1.5">
                    <span>Momo 音乐美学商店</span>
                    <span class="text-[9px] px-1.5 py-0.5 rounded bg-neutral-800 text-neutral-400 font-mono">STORE</span>
                </a>
            </nav>

            <div class="flex items-center gap-3">
                <a href="{mem_href}#apply-form" class="gradient-bg text-black px-4 sm:px-5 py-2 font-black text-xs uppercase tracking-wider hover:opacity-95 transform active:scale-95 transition-all shadow-lg shadow-momo-teal/20">
                    申请加入 2026 Plus
                </a>
            </div>
        </div>
    </header>
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
                        <li><a href="{mem_href}" class="hover:text-momo-cyan text-momo-mint font-bold">家庭年费会员 Plus (¥6,000)</a></li>
                        <li><a href="{study_href}" class="hover:text-[#D4AF37] text-[#D4AF37] font-bold">国际音乐留学规划 (¥38,800)</a></li>
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

def build_membership_page():
    path = os.path.join(WEBSITE_DIR, "membership.html")
    html = f'''<!DOCTYPE html>
<html lang="zh-CN" class="dark scroll-smooth">
<head>
    <title>Momo 家庭音乐年费会员 Plus (2026 Plus 官方专页) · 一人缴费 全家共享</title>
    {COMMON_HEAD_DEFS}
</head>
<body class="bg-black text-white antialiased font-sans pt-24 selection:bg-momo-cyan selection:text-black">
    {get_shared_header(current_page="membership", depth=0)}

    <main class="max-w-7xl mx-auto px-6 md:px-12 py-12">
        <!-- 顶部 Hero: 3D 白金钛金卡与理念 -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center mb-16 pb-16 border-b border-neutral-900">
            <div class="lg:col-span-7 space-y-6">
                <div class="inline-flex items-center gap-2 px-3 py-1 bg-neutral-900 border border-neutral-800 rounded text-xs font-mono font-bold text-momo-cyan">
                    <span>// GLOBAL FAMILY MEMBERSHIP PLUS 2026</span>
                </div>
                <h1 class="text-3xl sm:text-5xl md:text-6xl font-black uppercase tracking-tight text-white leading-tight">
                    因为音乐需要大家一起玩起来：<br>
                    <span class="gradient-text">用一份年费，激活全家的整个音乐生态</span>。
                </h1>
                <p class="text-neutral-300 text-sm sm:text-base leading-relaxed">
                    音乐从来不是靠独自机械堆砌课时学出来的——<strong>因为音乐的本质，最终是需要大家一起玩起来的。</strong>
                </p>
                <p class="text-neutral-400 text-xs sm:text-sm leading-relaxed">
                    通过成为我们的年费会员，可以非常顺畅地让我们为您调动起全工作室的艺术家老师、排练与合奏实验室，以及我们持续推出的创新音乐产品，带着大家一起把音乐鲜活地玩起来，形成一个长期浸润的教育环境。加入我们，不仅对您自己的家庭成长有益，更能汇聚成滋养整个平台与社群的力量——<strong>每个人只要稍微投入一点，最终不仅能收获自己的音乐成果，更能带动整个平台所有的师资、舞台与社群资源为大家所用。</strong>因此，这 ¥6,000 元所开启的，绝对是远远超越 ¥6,000 元本身的长期价值。
                </p>
                <div class="flex items-baseline gap-4 pt-4">
                    <span class="text-5xl font-black font-mono text-white">¥6,000</span>
                    <span class="text-sm font-mono text-neutral-400">/ 年 (365天有效 · 一人缴费全家共用)</span>
                </div>
                <div class="text-xs text-momo-mint font-semibold flex items-center gap-2">
                    <span class="w-2 h-2 rounded-full bg-momo-mint animate-pulse"></span>
                    <span>折合每天仅约 ¥16.4 · 调动全平台艺术家导师、月度合奏舞台与专属家庭智囊团</span>
                </div>
                <div class="pt-4 flex flex-wrap gap-4">
                    <a href="#signature-gallery" class="px-6 py-3.5 bg-neutral-900 hover:bg-neutral-800 border border-neutral-700 text-white font-mono text-xs uppercase tracking-wider transition-all">
                        浏览包含的核心实战项目 &darr;
                    </a>
                    <a href="#apply-form" class="gradient-bg text-black px-6 py-3.5 font-black text-xs uppercase tracking-wider hover:opacity-95 transition-all">
                        立即申请入会席位 &rarr;
                    </a>
                </div>
            </div>

            <!-- 右侧 3D 悬浮白金卡 -->
            <div class="lg:col-span-5 flex flex-col items-center">
                <div class="w-full max-w-md aspect-[1.58/1] rounded-2xl overflow-hidden shadow-2xl shadow-cyan-500/10 brutalist-border relative group">
                    <img src="./assets/images/momo_platinum_card.jpg" alt="MOMO Platinum Titanium Membership Card" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
                    <div class="absolute bottom-4 left-4 right-4 flex justify-between items-end bg-black/70 backdrop-blur-md p-3.5 rounded border border-neutral-800">
                        <div>
                            <div class="text-[9px] font-mono text-momo-mint font-bold uppercase tracking-widest">PHYSICAL TITANIUM CARD</div>
                            <div class="text-xs font-bold text-white">MOMO FAMILY 2026 PLUS</div>
                        </div>
                        <div class="text-xs font-mono text-neutral-300">MEMBER SINCE 2026</div>
                    </div>
                </div>
                <div class="text-xs font-mono text-neutral-400 mt-4 text-center space-y-1">
                    <div class="text-momo-mint font-bold">★ 入会即赠：专属白金金属实体会员卡 + MOMO 纯黑刺绣文化衫一件 (免费附赠)</div>
                    <div class="text-[11px] text-neutral-500">365天有效期 · 全家直系亲属共用 · 7天不满意全额退款保障</div>
                </div>
            </div>
        </div>

        <!-- ==================== 会员包含的核心实战项目与权益大赏 ==================== -->
        <section id="signature-gallery" class="mb-24 pt-8">
            <div class="flex flex-col md:flex-row md:items-end justify-between mb-12 pb-6 border-b border-neutral-800">
                <div>
                    <span class="text-xs font-mono font-bold text-momo-cyan uppercase tracking-widest block mb-2">// INCLUDED LABS &amp; SIGNATURE EXPERIENCES</span>
                    <h2 class="text-3xl sm:text-5xl font-black uppercase text-white tracking-tight">
                        会员包含的核心实战项目与尊享特权
                    </h2>
                </div>
                <p class="mt-4 md:mt-0 text-xs sm:text-sm font-mono text-neutral-400 max-w-md">
                    以下所有先锋实战与空间权益，全部无缝接入 ¥6,000 年费会员体系，支持课时自由划扣或专享会员折扣。
                </p>
            </div>

            <!-- 卡片大赏网格 (使用 Timo 认可的 #03 格式) -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">

                <!-- 01. 4-ON-1 职业乐队实验室 (Timo 截屏同款) -->
                <div class="brutalist-border bg-[#0b0b0d] flex flex-col justify-between relative group hover:border-momo-cyan transition-all">
                    <div class="absolute top-0 right-0 bg-neutral-900 border-l border-b border-neutral-800 text-neutral-300 font-mono text-[10px] px-3.5 py-1.5 uppercase tracking-widest z-10">
                        #01 ENSEMBLE LAB
                    </div>
                    <div class="p-6">
                        <div class="aspect-[16/10] bg-neutral-900 rounded-lg overflow-hidden mb-6 border border-neutral-800 relative">
                            <img src="./assets/images/real_ensemble_rehearsal.jpg" alt="4-on-1 Band Rehearsal" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                            <div class="absolute bottom-3 left-3 px-3 py-1 bg-black/80 backdrop-blur-md rounded border border-neutral-700 text-xs font-mono text-momo-cyan font-bold">
                                真实录音棚合奏 · 4位导师伴奏
                            </div>
                        </div>

                        <div class="text-xs font-mono text-momo-cyan uppercase tracking-widest font-bold">LABORATORY</div>
                        <h3 class="text-2xl font-black text-white mt-1 group-hover:text-momo-cyan transition-colors">
                            4-ON-1 职业乐队实验室
                        </h3>
                        <p class="text-xs text-neutral-400 mt-2.5 leading-relaxed">
                            4位一线音乐家（爵士鼓、低音提琴/贝斯、电吉他、键盘）围着你一人合奏。不再一个人孤独练琴，直接在真乐队声浪中体会呼吸与动态。
                        </p>
                        <div class="mt-4 text-xs font-mono space-y-1.5 pt-3 border-t border-neutral-900">
                            <div class="text-neutral-300">• 适用：流行主唱 / 电吉他 / 贝斯 / 鼓手实战</div>
                            <div class="text-momo-mint font-bold">• 会员权益：直接划扣 1 次课时额度</div>
                            <div class="text-neutral-500 text-[11px]">• 非会员单次：¥400 / 30min</div>
                        </div>
                    </div>

                    <div class="p-6 pt-4 border-t border-neutral-900 flex items-baseline justify-between bg-black/40">
                        <div>
                            <span class="text-2xl font-black font-mono text-white">划扣 1 课时</span>
                            <span class="text-[11px] text-neutral-400 font-mono"> / 或 ¥400/30min</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <a href="./ensemble-lab.html" class="text-xs font-mono text-momo-cyan hover:underline">
                                实验室专页 &rarr;
                            </a>
                        </div>
                    </div>
                </div>

                <!-- 02. 3–7岁 全家庭周末合奏包 -->
                <div class="brutalist-border bg-[#0b0b0d] flex flex-col justify-between relative group hover:border-momo-mint transition-all">
                    <div class="absolute top-0 right-0 bg-neutral-900 border-l border-b border-neutral-800 text-neutral-300 font-mono text-[10px] px-3.5 py-1.5 uppercase tracking-widest z-10">
                        #02 FAMILY WORKSHOP
                    </div>
                    <div class="p-6">
                        <div class="aspect-[16/10] bg-neutral-900 rounded-lg overflow-hidden mb-6 border border-neutral-800 relative">
                            <img src="./assets/images/real_daliangshan_charity.jpg" alt="Family Ensemble" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                            <div class="absolute bottom-3 left-3 px-3 py-1 bg-black/80 backdrop-blur-md rounded border border-neutral-700 text-xs font-mono text-momo-mint font-bold">
                                亲子沉浸 · 人生第一首家庭合奏
                            </div>
                        </div>

                        <div class="text-xs font-mono text-momo-mint uppercase tracking-widest font-bold">EARLY EXPLORATION</div>
                        <h3 class="text-2xl font-black text-white mt-1 group-hover:text-momo-mint transition-colors">
                            3–7岁 全家庭周末合奏包
                        </h3>
                        <p class="text-xs text-neutral-400 mt-2.5 leading-relaxed">
                            爸爸妈妈与孩子一同拿起乐器！在专业导师温柔引导下，全家共同体验音高、节奏与律动呼应。拒绝功利机械考级，在家庭默契与欢笑中种下音乐种子。
                        </p>
                        <div class="mt-4 text-xs font-mono space-y-1.5 pt-3 border-t border-neutral-900">
                            <div class="text-neutral-300">• 适用：3-7岁幼儿家庭 / 亲子双向声部启蒙</div>
                            <div class="text-momo-mint font-bold">• 会员权益：直接划扣 1 次课时额度</div>
                            <div class="text-neutral-500 text-[11px]">• 非会员单次：¥400 / 45min</div>
                        </div>
                    </div>

                    <div class="p-6 pt-4 border-t border-neutral-900 flex items-baseline justify-between bg-black/40">
                        <div>
                            <span class="text-2xl font-black font-mono text-white">划扣 1 课时</span>
                            <span class="text-[11px] text-neutral-400 font-mono"> / 或 ¥400/45min</span>
                        </div>
                        <a href="#apply-form" class="text-xs font-mono text-momo-mint hover:underline">
                            预约周末合奏 &rarr;
                        </a>
                    </div>
                </div>

                <!-- 03. P&R Studio 24轨现场唱片级录制 -->
                <div class="brutalist-border bg-[#0b0b0d] flex flex-col justify-between relative group hover:border-momo-cyan transition-all">
                    <div class="absolute top-0 right-0 bg-neutral-900 border-l border-b border-neutral-800 text-neutral-300 font-mono text-[10px] px-3.5 py-1.5 uppercase tracking-widest z-10">
                        #03 RECORDING SESSION
                    </div>
                    <div class="p-6">
                        <div class="aspect-[16/10] bg-neutral-900 rounded-lg overflow-hidden mb-6 border border-neutral-800 relative">
                            <img src="./assets/images/real_momo_vinyl.jpg" alt="MOMO Vinyl Recording" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                            <div class="absolute bottom-3 left-3 px-3 py-1 bg-black/80 backdrop-blur-md rounded border border-neutral-700 text-xs font-mono text-momo-cyan font-bold">
                                专业棚同期多轨实录 · 声音成长唱片
                            </div>
                        </div>

                        <div class="text-xs font-mono text-momo-cyan uppercase tracking-widest font-bold">LIVE SESSION</div>
                        <h3 class="text-2xl font-black text-white mt-1 group-hover:text-momo-cyan transition-colors">
                            P&amp;R Studio 现场作品记录
                        </h3>
                        <p class="text-xs text-neutral-400 mt-2.5 leading-relaxed">
                            当您或孩子打磨好一首心爱的作品，导师团队进棚现场伴奏，使用专业 Neumann / AKG 经典话筒与专业声卡多轨同期收音并完成母带校准。
                        </p>
                        <div class="mt-4 text-xs font-mono space-y-1.5 pt-3 border-t border-neutral-900">
                            <div class="text-neutral-300">• 产出：高保真 24-bit 现场母带分轨 + 混音档案</div>
                            <div class="text-momo-mint font-bold">• 会员超值礼遇：仅需消耗 1 次常规会员课时</div>
                            <div class="text-neutral-500 text-[11px]">• 市场同等标准棚费与乐手费通常高达数千元</div>
                        </div>
                    </div>

                    <div class="p-6 pt-4 border-t border-neutral-900 flex items-baseline justify-between bg-black/40">
                        <div>
                            <span class="text-2xl font-black font-mono text-white">仅划扣 1 课时</span>
                            <span class="text-[11px] text-neutral-400 font-mono"> (免高昂棚费)</span>
                        </div>
                        <a href="#apply-form" class="text-xs font-mono text-momo-cyan hover:underline">
                            锁定录音档期 &rarr;
                        </a>
                    </div>
                </div>

                <!-- 04. 城市真实舞台通行证 (香格里拉圣诞/城市音乐节专案) -->
                <div class="brutalist-border bg-[#0b0b0d] flex flex-col justify-between relative group hover:border-[#D4AF37] transition-all">
                    <div class="absolute top-0 right-0 bg-neutral-900 border-l border-b border-neutral-800 text-[#D4AF37] font-mono text-[10px] px-3.5 py-1.5 uppercase tracking-widest z-10">
                        #04 STAGE PASS
                    </div>
                    <div class="p-6">
                        <div class="aspect-[16/10] bg-neutral-900 rounded-lg overflow-hidden mb-6 border border-neutral-800 relative">
                            <img src="./assets/images/conservatory_mentorship_hero.jpg" alt="Urban Stage" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                            <div class="absolute bottom-3 left-3 px-3 py-1 bg-black/80 backdrop-blur-md rounded border border-neutral-700 text-xs font-mono text-[#D4AF37] font-bold">
                                城市真实舞台 · 拒绝内卷选拔
                            </div>
                        </div>

                        <div class="text-xs font-mono text-[#D4AF37] uppercase tracking-widest font-bold">REAL STAGE</div>
                        <h3 class="text-2xl font-black text-white mt-1 group-hover:text-[#D4AF37] transition-colors">
                            城市真实舞台通行证
                        </h3>
                        <p class="text-xs text-neutral-400 mt-2.5 leading-relaxed">
                            <strong>拒绝功利“选拔”两个字！</strong>演出是一个自然生长的呈现：刚好甲方需要，而你又刚刚准备好。我们在香格里拉大酒店圣诞专案、城市公园音乐节等真实舞台，为会员提供真实登台演练机会。
                        </p>
                        <div class="mt-4 text-xs font-mono space-y-1.5 pt-3 border-t border-neutral-900">
                            <div class="text-neutral-300">• 场景：香格里拉圣诞专案 / 自由声波城市开放麦</div>
                            <div class="text-momo-mint font-bold">• 会员权益：活动规划包含，每年 4 次+舞台优先通告</div>
                            <div class="text-neutral-500 text-[11px]">• 导师登台护航，在真实观众掌声中锻造从容台风</div>
                        </div>
                    </div>

                    <div class="p-6 pt-4 border-t border-neutral-900 flex items-baseline justify-between bg-black/40">
                        <div>
                            <span class="text-2xl font-black font-mono text-[#D4AF37]">会员包含</span>
                            <span class="text-[11px] text-neutral-400 font-mono"> (每年4次+舞台)</span>
                        </div>
                        <a href="#apply-form" class="text-xs font-mono text-[#D4AF37] hover:underline">
                            舞台排期咨询 &rarr;
                        </a>
                    </div>
                </div>

                <!-- 05. 3次 全年家庭音乐成长与教育规划深度诊断 -->
                <div class="brutalist-border bg-[#0b0b0d] flex flex-col justify-between relative group hover:border-momo-mint transition-all">
                    <div class="absolute top-0 right-0 bg-neutral-900 border-l border-b border-neutral-800 text-neutral-300 font-mono text-[10px] px-3.5 py-1.5 uppercase tracking-widest z-10">
                        #05 DIAGNOSIS
                    </div>
                    <div class="p-6">
                        <div class="aspect-[16/10] bg-neutral-900 rounded-lg overflow-hidden mb-6 border border-neutral-800 relative">
                            <img src="./assets/images/momo_garden_space.jpg" alt="Family Diagnosis" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                            <div class="absolute bottom-3 left-3 px-3 py-1 bg-black/80 backdrop-blur-md rounded border border-neutral-700 text-xs font-mono text-momo-mint font-bold">
                                面对面亲诊 · 避免走弯路与花冤枉钱
                            </div>
                        </div>

                        <div class="text-xs font-mono text-momo-mint uppercase tracking-widest font-bold">STRATEGY</div>
                        <h3 class="text-2xl font-black text-white mt-1 group-hover:text-momo-mint transition-colors">
                            家庭音乐成长深度诊断 (3次)
                        </h3>
                        <p class="text-xs text-neutral-400 mt-2.5 leading-relaxed">
                            由主理人 Timo 与资深音乐教育导师提供全年 3 次深度面对面诊断会议（共 3 小时）。量身定制家庭音乐声场、乐器选购、国内外升学方向与阶段性合奏目标。
                        </p>
                        <div class="mt-4 text-xs font-mono space-y-1.5 pt-3 border-t border-neutral-900">
                            <div class="text-neutral-300">• 形式：线上/线下桐梓林花园私享沙龙面对面</div>
                            <div class="text-momo-mint font-bold">• 会员权益：年费包含 3 次深度诊断 (共3小时)</div>
                            <div class="text-neutral-500 text-[11px]">• 单独咨询市场价：¥1,000 / 小时</div>
                        </div>
                    </div>

                    <div class="p-6 pt-4 border-t border-neutral-900 flex items-baseline justify-between bg-black/40">
                        <div>
                            <span class="text-2xl font-black font-mono text-white">会员包含</span>
                            <span class="text-[11px] text-neutral-400 font-mono"> (价值 ¥3,000)</span>
                        </div>
                        <a href="#apply-form" class="text-xs font-mono text-momo-mint hover:underline">
                            预约本季度亲诊 &rarr;
                        </a>
                    </div>
                </div>

                <!-- 06. 城市音乐共享空间与琴房 5 折特权 -->
                <div class="brutalist-border bg-[#0b0b0d] flex flex-col justify-between relative group hover:border-momo-cyan transition-all">
                    <div class="absolute top-0 right-0 bg-neutral-900 border-l border-b border-neutral-800 text-neutral-300 font-mono text-[10px] px-3.5 py-1.5 uppercase tracking-widest z-10">
                        #06 SPACES PRIVILEGE
                    </div>
                    <div class="p-6">
                        <div class="aspect-[16/10] bg-neutral-900 rounded-lg overflow-hidden mb-6 border border-neutral-800 relative">
                            <img src="./assets/images/momo_garden_space.jpg" alt="Momo Garden Space" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                            <div class="absolute bottom-3 left-3 px-3 py-1 bg-black/80 backdrop-blur-md rounded border border-neutral-700 text-xs font-mono text-momo-cyan font-bold">
                                桐梓林+麓湖双空间 · 全线半价
                            </div>
                        </div>

                        <div class="text-xs font-mono text-momo-cyan uppercase tracking-widest font-bold">VENUE DISCOUNT</div>
                        <h3 class="text-2xl font-black text-white mt-1 group-hover:text-momo-cyan transition-colors">
                            共享空间与乐器 5 折特权
                        </h3>
                        <p class="text-xs text-neutral-400 mt-2.5 leading-relaxed">
                            隐于成熟小区的私密声场，自带中央咖啡吧台与 60㎡ 阳光私家花园。会员享所有场地与乐器租借统一 5 折结算，并享周末热门黄金档优先锁档特权。
                        </p>
                        <div class="mt-4 text-xs font-mono space-y-1.5 pt-3 border-t border-neutral-900">
                            <div class="text-neutral-300">• 琴房练琴：会员 <strong>¥40/h</strong> (对外 ¥80/h)</div>
                            <div class="text-neutral-300">• 乐队排练：会员 <strong>¥100/h</strong> (对外 ¥200/h)</div>
                            <div class="text-momo-mint font-bold">• 录音棚/会议/包场派对/乐器租用全部半价</div>
                        </div>
                    </div>

                    <div class="p-6 pt-4 border-t border-neutral-900 flex items-baseline justify-between bg-black/40">
                        <div>
                            <span class="text-2xl font-black font-mono text-white">全线 5 折</span>
                            <span class="text-[11px] text-neutral-400 font-mono"> + 优先锁档</span>
                        </div>
                        <a href="./spaces.html" class="text-xs font-mono text-momo-cyan hover:underline">
                            空间价目表 &rarr;
                        </a>
                    </div>
                </div>

                <!-- 07. MOMO 纯黑刺绣文化衫免费礼遇 -->
                <div class="brutalist-border bg-[#0b0b0d] flex flex-col justify-between relative group hover:border-white transition-all">
                    <div class="absolute top-0 right-0 bg-neutral-900 border-l border-b border-neutral-800 text-white font-mono text-[10px] px-3.5 py-1.5 uppercase tracking-widest z-10">
                        #07 MEMBER GIFT
                    </div>
                    <div class="p-6">
                        <div class="aspect-[16/10] bg-neutral-900 rounded-lg overflow-hidden mb-6 border border-neutral-800 relative">
                            <img src="./assets/images/momo_tshirt_te_style.jpg" alt="Momo T-shirt" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                            <div class="absolute bottom-3 left-3 px-3 py-1 bg-black/80 backdrop-blur-md rounded border border-neutral-700 text-xs font-mono text-white font-bold">
                                成为会员 · 免费赠送一件
                            </div>
                        </div>

                        <div class="text-xs font-mono text-neutral-300 uppercase tracking-widest font-bold">MEMBERSHIP WELCOME</div>
                        <h3 class="text-2xl font-black text-white mt-1 group-hover:text-momo-cyan transition-colors">
                            MOMO 纯黑刺绣重磅文化衫
                        </h3>
                        <p class="text-xs text-neutral-400 mt-2.5 leading-relaxed">
                            成为会员，即赠送一件 MOMO 纯黑限定文化衫（标价 ¥260）。选用特选 280g 重磅有机精梳棉，胸前哑光低调刺绣 MOMO 盾徽，兼具乐手排练与日常出街美学。
                        </p>
                        <div class="mt-4 text-xs font-mono space-y-1.5 pt-3 border-t border-neutral-900">
                            <div class="text-neutral-300">• 材质：280g 重磅双纱有机棉 / 微落肩版型</div>
                            <div class="text-momo-mint font-bold">• 会员礼遇：开卡即赠一件（自选尺码）</div>
                            <div class="text-neutral-500 text-[11px]">• 亦可在 Momo 音乐美学商店单买（¥260）</div>
                        </div>
                    </div>

                    <div class="p-6 pt-4 border-t border-neutral-900 flex items-baseline justify-between bg-black/40">
                        <div>
                            <span class="text-2xl font-black font-mono text-white">入会免费赠送</span>
                            <span class="text-[11px] text-neutral-400 font-mono"> (价值 ¥260)</span>
                        </div>
                        <a href="./store/tshirt.html" class="text-xs font-mono text-white hover:underline">
                            文化衫详情 &rarr;
                        </a>
                    </div>
                </div>

            </div>
        </section>

        <!-- ==================== 2026 Plus 五大核心保障 ==================== -->
        <section class="mb-20 pt-8 border-t border-neutral-900">
            <div class="text-center max-w-3xl mx-auto mb-14">
                <span class="text-xs font-mono font-bold text-momo-mint uppercase tracking-widest block mb-2">// FIVE CORE ASSURANCES</span>
                <h2 class="text-3xl sm:text-4xl font-black uppercase text-white">2026 Plus 核心机制与信赖保障</h2>
                <p class="text-xs sm:text-sm text-neutral-400 mt-2">拒绝机构套路捆绑 · 让家庭拥有专属的音乐朋友圈与成长底座</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                <!-- 01 -->
                <div class="brutalist-border bg-[#0d0d0d] p-8 space-y-4">
                    <div class="text-xs font-mono font-black text-momo-cyan border border-neutral-800 bg-neutral-900 px-2 py-1 inline-block">01</div>
                    <h3 class="text-lg font-bold text-white">12 次 1对1 艺术家专属定制指导</h3>
                    <p class="text-xs text-neutral-400 leading-relaxed">
                        单次 60 分钟。线下双空间沉浸 / 线上全球陪伴自由切换。涵盖全系器乐精修、即兴创作、流行爵士合奏与审美启发，支持全家成员共用额度。
                    </p>
                    <div class="text-[11px] font-mono text-momo-mint pt-2 border-t border-neutral-900">
                        ※ 12 次消完后，全年尊享会员专属优惠单价灵活续充，轻松自在无负担。
                    </div>
                </div>

                <!-- 02 -->
                <div class="brutalist-border bg-[#0d0d0d] p-8 space-y-4">
                    <div class="text-xs font-mono font-black text-momo-mint border border-neutral-800 bg-neutral-900 px-2 py-1 inline-block">02</div>
                    <h3 class="text-lg font-bold text-white">3 次 全年家庭音乐成长与教育规划深度诊断</h3>
                    <p class="text-xs text-neutral-400 leading-relaxed">
                        共 3 小时深度咨询。由主理人 Timo 与资深音乐教育规划导师提供 1对1 深度规划会议，量身定制家庭音乐氛围搭建、乐器配置、国内外升学方向与阶段性合奏目标。
                    </p>
                    <div class="text-[11px] font-mono text-neutral-400 pt-2 border-t border-neutral-900">
                        精准切中痛点，避免家庭走弯路、花冤枉钱。
                    </div>
                </div>

                <!-- 03 -->
                <div class="brutalist-border bg-[#0d0d0d] p-8 space-y-4">
                    <div class="text-xs font-mono font-black text-momo-cyan border border-neutral-800 bg-neutral-900 px-2 py-1 inline-block">03 · 核心护航</div>
                    <h3 class="text-lg font-bold text-white">365 天 专属一户一群协同护航</h3>
                    <p class="text-xs text-neutral-400 leading-relaxed">
                        为每个家庭单独建立专属微信陪伴群！主理人 Timo 与 3~5 位不同声部的艺术家导师全员入驻，相当于您的家庭拥有了一群懂音乐的“自己人”，随时解答练琴困惑、督促自学、分享精选曲谱。
                    </p>
                    <div class="text-[11px] font-mono text-momo-cyan pt-2 border-t border-neutral-900">
                        365天全天候守护 · 杜绝单一教师盲盒主观偏见。
                    </div>
                </div>

                <!-- 04 -->
                <div class="brutalist-border bg-[#0d0d0d] p-8 space-y-4">
                    <div class="text-xs font-mono font-black text-momo-mint border border-neutral-800 bg-neutral-900 px-2 py-1 inline-block">04</div>
                    <h3 class="text-lg font-bold text-white">全年 4 次+ 音乐社群活动与城市舞台优先特权</h3>
                    <p class="text-xs text-neutral-400 leading-relaxed">
                        优先参与每月【师生重奏实验室】、【自由声波开放麦】、【青少年现代音乐先锋社团】以及桐梓林/麓湖双空间主题音乐沙龙与大师工作坊。
                    </p>
                    <div class="text-[11px] font-mono text-neutral-400 pt-2 border-t border-neutral-900">
                        让音乐在真实的舞台与人群中流淌。
                    </div>
                </div>

                <!-- 05 -->
                <div class="brutalist-border bg-[#0d0d0d] p-8 space-y-4">
                    <div class="text-xs font-mono font-black text-momo-cyan border border-neutral-800 bg-neutral-900 px-2 py-1 inline-block">05 · 超值礼遇</div>
                    <h3 class="text-lg font-bold text-white">P&amp;R Studio 录音棚 Live Session 现场作品记录</h3>
                    <p class="text-xs text-neutral-400 leading-relaxed">
                        当您或孩子打磨好一首心爱的作品，<strong>仅需消耗 1 次常规会员课时额度</strong>，即可调用多位导师组成现场伴奏乐队，在 Momo 专业录音棚完成多轨同期实录与混音校准，为家庭珍藏每年一张的声音成长唱片。
                    </p>
                    <div class="text-[11px] font-mono text-momo-mint pt-2 border-t border-neutral-900">
                        坚决向外界数千上万的高昂乐手棚费说不！
                    </div>
                </div>

                <!-- 06 -->
                <div class="brutalist-border bg-[#0d0d0d] p-8 space-y-4">
                    <div class="text-xs font-mono font-black text-white border border-neutral-800 bg-neutral-900 px-2 py-1 inline-block">06 · 赠品与保障</div>
                    <h3 class="text-lg font-bold text-white">赠送文化衫 + 7天安心退费</h3>
                    <p class="text-xs text-neutral-400 leading-relaxed">
                        入会即赠送 MOMO 纯黑重磅刺绣文化衫一件（标价 ¥260）。同时享有 <strong>7 天冷静期全额退费保障</strong>：开通后 7 天内若感到理念不合或体验不适，无隐形门槛全额退费。
                    </p>
                    <div class="text-[11px] font-mono text-white pt-2 border-t border-neutral-900">
                        真实信赖始于坦荡透明 · 365天长效陪伴。
                    </div>
                </div>
            </div>
        </section>

        <!-- 申请入会与咨询表单 -->
        <div id="apply-form" class="max-w-2xl mx-auto brutalist-border bg-neutral-950 p-8 sm:p-12 mb-20">
            <div class="text-center mb-8">
                <span class="text-xs font-mono uppercase tracking-widest text-momo-cyan">// JOIN MOMO FAMILY</span>
                <h3 class="text-2xl font-black uppercase text-white mt-1">申请开通 2026 Plus 家庭会员</h3>
                <p class="text-xs font-mono text-neutral-400 mt-2">
                    ¥6,000/年 · 365天全家共享 · 主理人 Timo 亲自主理交付
                </p>
            </div>

            <form onsubmit="handleMemberApply(event)" class="space-y-5">
                <div>
                    <label class="text-xs font-mono text-neutral-400 block mb-1">家长 / 会员姓名 *</label>
                    <input type="text" id="member-name" required placeholder="如：李先生 / 陈女士" class="w-full bg-neutral-900 border border-neutral-800 px-4 py-3 text-xs text-white focus:outline-none focus:border-momo-cyan">
                </div>
                <div>
                    <label class="text-xs font-mono text-neutral-400 block mb-1">手机号 / 微信号 *</label>
                    <input type="text" id="member-phone" required placeholder="如：13900000000 (微信同号)" class="w-full bg-neutral-900 border border-neutral-800 px-4 py-3 text-xs text-white focus:outline-none focus:border-momo-cyan">
                </div>
                <div>
                    <label class="text-xs font-mono text-neutral-400 block mb-1">家庭主要期望探索的乐器或合奏方向</label>
                    <input type="text" id="member-interest" placeholder="如：孩子吉他+妈妈钢琴 / 爵士大乐队 / 乐队合奏" class="w-full bg-neutral-900 border border-neutral-800 px-4 py-3 text-xs text-white focus:outline-none focus:border-momo-cyan">
                </div>
                <div class="text-[11px] text-neutral-500 font-mono">
                    ※ 提交后，主理人 Timo 与顾问团队将在 2 小时内与您联络，安排面对面建档及专属微信群建立。开通后享 7 天无忧退费。
                </div>
                <button type="submit" class="w-full gradient-bg text-black py-4 font-black text-xs uppercase tracking-wider hover:opacity-95">
                    确认提交入会申请 (¥6,000/年) &rarr;
                </button>
            </form>
        </div>

        <!-- 常见问题解答 (FAQ) -->
        <div class="max-w-4xl mx-auto mb-20">
            <h3 class="text-2xl font-black uppercase text-white text-center mb-8">关于年费会员的常见问题</h3>
            <div class="space-y-4 text-xs">
                <div class="brutalist-border bg-neutral-950 p-6 space-y-2">
                    <div class="font-bold text-white text-sm">Q：我们全家两个人甚至三个人都可以用这 12 次课时吗？</div>
                    <div class="text-neutral-400 leading-relaxed">
                        是的！MOMO 倡导全家庭音乐浸润。12 次专属指导额度可以在全家直系亲属间自由分配，例如孩子学架子鼓或吉他，爸爸妈妈学钢琴或贝斯，也可以用于家庭全员周末合奏。
                    </div>
                </div>
                <div class="brutalist-border bg-neutral-950 p-6 space-y-2">
                    <div class="font-bold text-white text-sm">Q：12次消完之后怎么办？需要重新交 6000 吗？</div>
                    <div class="text-neutral-400 leading-relaxed">
                        不需要！12次额度是年费内包含的基础课时。消完后，在 365 天会员有效期内，您可以继续享受会员专属的超值单课续充价，无需再次缴纳年费，丰俭由人。
                    </div>
                </div>
                <div class="brutalist-border bg-neutral-950 p-6 space-y-2">
                    <div class="font-bold text-white text-sm">Q：什么是 7 天无理由全额退费保障？</div>
                    <div class="text-neutral-400 leading-relaxed">
                        自您开通会员之日起 7 天内，如果您觉得教学理念与家庭期待不符，或者时间无法协调，只需与主理人 Timo 微信说明，扣除已实际发生的单次课时费后，剩余款项 100% 原路返还，无任何捆绑手续费。
                    </div>
                </div>
            </div>
        </div>
    </main>

    <script>
        function handleMemberApply(e) {{
            e.preventDefault();
            const name = document.getElementById('member-name').value;
            const phone = document.getElementById('member-phone').value;
            alert('感谢您对 Momo 音乐理念的认同！\\n我们已收到 ' + name + '（' + phone + '）的 2026 Plus 会员开通申请。\\n主理人 Timo 将在 2 小时内亲自与您微信联络，安排入会礼盒寄送与一户一群建档！');
        }}
    </script>

    {get_shared_footer(depth=0)}
</body>
</html>
'''
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("SUCCESS: membership.html compiled!")

def build_ensemble_lab_page():
    path = os.path.join(WEBSITE_DIR, "ensemble-lab.html")
    html = f'''<!DOCTYPE html>
<html lang="zh-CN" class="dark scroll-smooth">
<head>
    <title>4-on-1 职业乐队实验室 · 真实录音棚 4位音乐家围着你合奏 · Momo</title>
    {COMMON_HEAD_DEFS}
</head>
<body class="bg-black text-white antialiased font-sans pt-24 selection:bg-momo-cyan selection:text-black">
    {get_shared_header(current_page="ensemble_lab", depth=0)}

    <main class="max-w-7xl mx-auto px-6 md:px-12 py-12">
        <!-- 顶部面包屑与标题 -->
        <div class="mb-12">
            <div class="flex items-center gap-2 text-xs font-mono text-neutral-400 mb-4">
                <a href="./index.html" class="hover:text-white">首页</a>
                <span>/</span>
                <a href="./membership.html" class="hover:text-white">家庭年费会员</a>
                <span>/</span>
                <span class="text-momo-cyan">4-on-1 职业乐队实验室</span>
            </div>
            <div class="inline-block px-3 py-1 bg-neutral-900 border border-neutral-800 text-xs font-mono text-momo-cyan uppercase tracking-widest mb-3">
                // SIGNATURE EXPERIENCE #01 · 真实录音棚真声场
            </div>
            <h1 class="text-3xl sm:text-5xl md:text-6xl font-black uppercase tracking-tight text-white">
                4-ON-1 职业乐队实验室
            </h1>
            <p class="text-neutral-400 text-sm sm:text-base mt-3 max-w-3xl leading-relaxed">
                4位一线职业音乐家（爵士鼓、低音提琴/贝斯、电吉他、键盘）围着你一人合奏。<br>
                <strong>不再一个人孤独练琴，直接在真乐队声浪中体会呼吸与动态。</strong>
            </p>
        </div>

        <!-- 视觉展示大图 -->
        <div class="brutalist-border rounded-xl overflow-hidden mb-16 relative">
            <img src="./assets/images/real_ensemble_rehearsal.jpg" alt="Real 4-on-1 Ensemble Rehearsal Studio" class="w-full h-auto max-h-[600px] object-cover">
            <div class="absolute bottom-4 left-4 right-4 sm:bottom-6 sm:left-6 sm:right-6 flex flex-col sm:flex-row justify-between items-start sm:items-end gap-3 bg-black/80 backdrop-blur-md p-4 sm:p-6 rounded-lg border border-neutral-800">
                <div>
                    <span class="text-xs font-mono text-momo-cyan font-bold block mb-1">RECORDING STUDIO LIVE IMMERSION</span>
                    <div class="text-lg sm:text-xl font-bold text-white">桐梓林 &amp; 麓湖 专业录音棚实拍</div>
                    <div class="text-xs text-neutral-300 mt-1">真鼓真实声场 · 电子管管箱真实反馈 · 监听系统精准同步</div>
                </div>
                <div class="flex items-baseline gap-3">
                    <span class="text-3xl font-black font-mono text-white">¥400</span>
                    <span class="text-xs font-mono text-neutral-400">/ 30min 体验</span>
                    <span class="text-xs font-mono text-momo-mint font-bold px-2 py-0.5 bg-momo-mint/10 border border-momo-mint/30 rounded">年费会员直接划扣</span>
                </div>
            </div>
        </div>

        <!-- 核心痛点与理念：为什么需要真乐队围合？ -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 mb-20 pb-16 border-b border-neutral-900">
            <div class="lg:col-span-5 space-y-5">
                <span class="text-xs font-mono text-momo-mint uppercase tracking-widest font-bold">// THE PEDAGOGICAL BREAKTHROUGH</span>
                <h2 class="text-2xl sm:text-4xl font-black uppercase text-white leading-tight">
                    为什么一个人孤独练琴<br>
                    总是容易枯燥与停滞？
                </h2>
                <p class="text-neutral-400 text-xs sm:text-sm leading-relaxed">
                    在传统音乐学习中，学生 90% 的时间都在琴房面对节拍器或冰冷的伴奏音频独自弹奏。一旦离开谱子，就失去了对音乐律动（Groove）、声部互动与呼吸感的感知。
                </p>
                <p class="text-neutral-400 text-xs sm:text-sm leading-relaxed">
                    <strong>但在 Momo 的 4-on-1 实验室里，你不是在“交作业”，你是在与真正的乐手共同创造音乐。</strong>你弹错一个拍子，贝斯会温柔地托住你；你想要渐强，鼓手的鼓刷会随着你的情绪瞬间推高。这才是音乐真正的生命力。
                </p>
            </div>

            <!-- 4位导师配置解析 -->
            <div class="lg:col-span-7 grid grid-cols-1 sm:grid-cols-2 gap-6">
                <!-- 01 鼓手 -->
                <div class="brutalist-border bg-neutral-950 p-6 space-y-3">
                    <div class="flex justify-between items-center">
                        <span class="text-xs font-mono font-bold text-momo-cyan">DRUMS · 爵士鼓手</span>
                        <span class="text-[10px] font-mono text-neutral-500">RHYTHM BACKBONE</span>
                    </div>
                    <h3 class="text-lg font-bold text-white">律动与节拍骨架</h3>
                    <p class="text-xs text-neutral-400 leading-relaxed">
                        告别死板机械节拍器。导师通过真实的重音切分、鼓刷扫弦与过门，教你如何在速度变化中稳定掌控身体律动。
                    </p>
                </div>

                <!-- 02 贝斯手 -->
                <div class="brutalist-border bg-neutral-950 p-6 space-y-3">
                    <div class="flex justify-between items-center">
                        <span class="text-xs font-mono font-bold text-momo-mint">BASS · 低音提琴/电贝斯</span>
                        <span class="text-[10px] font-mono text-neutral-500">HARMONIC ROOT</span>
                    </div>
                    <h3 class="text-lg font-bold text-white">低频中流砥柱</h3>
                    <p class="text-xs text-neutral-400 leading-relaxed">
                        连接鼓手节奏与主奏乐器的核心枢纽。贝斯导师的饱满根音与 Walking Bass，将瞬间帮你建立极度坚固的调性安全感。
                    </p>
                </div>

                <!-- 03 吉他手 -->
                <div class="brutalist-border bg-neutral-950 p-6 space-y-3">
                    <div class="flex justify-between items-center">
                        <span class="text-xs font-mono font-bold text-momo-cyan">GUITAR · 电吉他/木吉他</span>
                        <span class="text-[10px] font-mono text-neutral-500">CHORDAL TEXTURE</span>
                    </div>
                    <h3 class="text-lg font-bold text-white">和声色彩与织体</h3>
                    <p class="text-xs text-neutral-400 leading-relaxed">
                        爵士半空心吉他或纯净原声扫弦，为你铺陈丰富的现代和声张力，教你倾听伴奏吉他留白时的声部呼应。
                    </p>
                </div>

                <!-- 04 键盘手 -->
                <div class="brutalist-border bg-neutral-950 p-6 space-y-3">
                    <div class="flex justify-between items-center">
                        <span class="text-xs font-mono font-bold text-momo-mint">KEYS · Nord键盘/电钢</span>
                        <span class="text-[10px] font-mono text-neutral-500">DYNAMIC COMPING</span>
                    </div>
                    <h3 class="text-lg font-bold text-white">即兴对话与补空</h3>
                    <p class="text-xs text-neutral-400 leading-relaxed">
                        资深键盘导师随时根据你的旋律即兴加花与 Comping 和弦伴奏，激发你大胆即兴 Solo 与表达内心情感的勇气。
                    </p>
                </div>
            </div>
        </div>

        <!-- 两种参与途径：单次试奏 vs 年费会员 -->
        <div class="mb-20">
            <div class="text-center max-w-2xl mx-auto mb-12">
                <span class="text-xs font-mono font-bold text-momo-cyan uppercase tracking-widest block mb-2">// FLEXIBLE ACCESS MODES</span>
                <h2 class="text-3xl font-black uppercase text-white">两种参与 4-on-1 实验室的方式</h2>
                <p class="text-xs text-neutral-400 mt-2">丰俭由人 · 支持低门槛单次体验，更推荐年费深度共创</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-4xl mx-auto">
                <!-- 途径 A: 单次体验 -->
                <div class="brutalist-border bg-neutral-950 p-8 flex flex-col justify-between">
                    <div class="space-y-4">
                        <span class="text-xs font-mono text-neutral-400 uppercase tracking-widest">OPTION A · 低门槛初体验</span>
                        <h3 class="text-2xl font-black text-white">单次体验合奏席位</h3>
                        <p class="text-xs text-neutral-400 leading-relaxed">
                            无需缴纳年费。挑选一首你目前正在练习的曲目，直接进棚与 4 位导师开展 30 分钟的高密度即兴实战演练，感受真乐队声浪的震撼。
                        </p>
                        <div class="pt-4 border-t border-neutral-900 space-y-2 text-xs font-mono text-neutral-300">
                            <div>• 包含 30 分钟真乐队围合实战</div>
                            <div>• 4 位导师当场口头复盘与练习建议</div>
                            <div>• 获得单次排练现场手机高清实况录像</div>
                        </div>
                    </div>
                    <div class="pt-8 border-t border-neutral-900 mt-8 flex items-baseline justify-between">
                        <div>
                            <span class="text-4xl font-black font-mono text-white">¥400</span>
                            <span class="text-xs text-neutral-400 font-mono"> / 30min</span>
                        </div>
                        <a href="#lab-book-form" class="px-5 py-2.5 bg-neutral-900 hover:bg-neutral-800 border border-neutral-700 text-white font-mono text-xs uppercase">
                            预约单次试奏 &rarr;
                        </a>
                    </div>
                </div>

                <!-- 途径 B: 会员划扣 (极力推荐) -->
                <div class="brutalist-border bg-neutral-950 p-8 flex flex-col justify-between border-momo-mint/60 relative">
                    <div class="absolute -top-3 right-6 bg-momo-mint text-black text-[10px] font-mono font-black px-3 py-1 uppercase rounded-full">
                        RECOMMENDED · 尊享性价比
                    </div>
                    <div class="space-y-4">
                        <span class="text-xs font-mono text-momo-mint uppercase tracking-widest">OPTION B · 家庭年费会员划扣</span>
                        <h3 class="text-2xl font-black text-white">加入 2026 Plus 会员体系</h3>
                        <p class="text-xs text-neutral-400 leading-relaxed">
                            办理 ¥6,000 家庭年费会员，享 12 次 1对1 定制课时额度。<strong>可直接将额度划扣用于 4-on-1 乐队实验室</strong>，更有 365 天一户一群导师随时辅导、3次成长亲诊与全套多轨分轨录音！
                        </p>
                        <div class="pt-4 border-t border-neutral-900 space-y-2 text-xs font-mono text-momo-mint">
                            <div>★ 12次额度自由支配（支持4-on-1划扣）</div>
                            <div>★ 赠送 MOMO 纯黑刺绣重磅文化衫 (¥260)</div>
                            <div>★ P&amp;R 录音棚 Live Session 唱片级录音</div>
                            <div>★ 享桐梓林/麓湖双空间租用 5 折特权</div>
                        </div>
                    </div>
                    <div class="pt-8 border-t border-neutral-900 mt-8 flex items-baseline justify-between">
                        <div>
                            <span class="text-4xl font-black font-mono text-white">¥6,000</span>
                            <span class="text-xs text-neutral-400 font-mono"> / 年 (折合 ¥16.4/天)</span>
                        </div>
                        <a href="./membership.html" class="gradient-bg text-black px-5 py-2.5 font-black text-xs uppercase tracking-wider hover:opacity-90">
                            开通年费会员 &rarr;
                        </a>
                    </div>
                </div>
            </div>
        </div>

        <!-- 预约席位表单 -->
        <div id="lab-book-form" class="max-w-2xl mx-auto brutalist-border bg-neutral-950 p-8 sm:p-12 mb-20">
            <div class="text-center mb-8">
                <span class="text-xs font-mono text-momo-cyan uppercase tracking-widest">// BOOK YOUR SEAT</span>
                <h3 class="text-2xl font-black uppercase text-white mt-1">预约 4-on-1 乐队实验室席位</h3>
                <p class="text-xs font-mono text-neutral-400 mt-2">
                    单次试奏 ¥400 / 或会员划扣 · 桐梓林与麓湖双空间可选
                </p>
            </div>

            <form onsubmit="handleLabBooking(event)" class="space-y-5">
                <div>
                    <label class="text-xs font-mono text-neutral-400 block mb-1">姓名 / 称呼 *</label>
                    <input type="text" id="lab-name" required placeholder="如：陈同学 / 张先生" class="w-full bg-neutral-900 border border-neutral-800 px-4 py-3 text-xs text-white focus:outline-none focus:border-momo-cyan">
                </div>
                <div>
                    <label class="text-xs font-mono text-neutral-400 block mb-1">微信号 / 手机号 *</label>
                    <input type="text" id="lab-phone" required placeholder="如：13800000000 (微信同号)" class="w-full bg-neutral-900 border border-neutral-800 px-4 py-3 text-xs text-white focus:outline-none focus:border-momo-cyan">
                </div>
                <div>
                    <label class="text-xs font-mono text-neutral-400 block mb-1">你负责的主奏声部 / 乐器 *</label>
                    <select id="lab-instrument" class="w-full bg-neutral-900 border border-neutral-800 px-4 py-3 text-xs text-white focus:outline-none focus:border-momo-cyan">
                        <option value="流行主唱 (Vocals)">流行主唱 (Vocals)</option>
                        <option value="电吉他 / 木吉他 (Guitar)">电吉他 / 木吉他 (Guitar)</option>
                        <option value="电贝斯 / 低音提琴 (Bass)">电贝斯 / 低音提琴 (Bass)</option>
                        <option value="架子鼓 (Drums)">架子鼓 (Drums)</option>
                        <option value="键盘 / 钢琴 (Keys)">键盘 / 钢琴 (Keys)</option>
                        <option value="萨克斯 / 吹奏乐器 (Sax/Brass)">萨克斯 / 吹奏乐器 (Sax/Brass)</option>
                    </select>
                </div>
                <div>
                    <label class="text-xs font-mono text-neutral-400 block mb-1">期望排练曲目与排期</label>
                    <input type="text" id="lab-song" placeholder="如：Autumn Leaves / 陶喆《爱很简单》/ 预计本周六" class="w-full bg-neutral-900 border border-neutral-800 px-4 py-3 text-xs text-white focus:outline-none focus:border-momo-cyan">
                </div>
                <button type="submit" class="w-full gradient-bg text-black py-4 font-black text-xs uppercase tracking-wider hover:opacity-95">
                    提交合奏席位预约申请 &rarr;
                </button>
            </form>
        </div>
    </main>

    <script>
        function handleLabBooking(e) {{
            e.preventDefault();
            const name = document.getElementById('lab-name').value;
            const phone = document.getElementById('lab-phone').value;
            const inst = document.getElementById('lab-instrument').value;
            alert('合奏预约已受理！\\n主理人 Timo 与导师组将在 2 小时内联络 ' + name + '（' + phone + '）\\n为您安排【' + inst + '】的专属 4-on-1 导师排练档期！');
        }}
    </script>

    {get_shared_footer(depth=0)}
</body>
</html>
'''
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("SUCCESS: ensemble-lab.html compiled!")

if __name__ == "__main__":
    build_membership_page()
    build_ensemble_lab_page()
