# -*- coding: utf-8 -*-
"""
MOMO Music Website - Master Ecosystem Builder
Comprehensive standalone pages:
1. store/index.html (Momo 音乐美学商店)
2. store/tshirt.html (文化衫)
3. store/picks.html (拨片盒)
4. store/vinyl.html (限定黑胶)
5. store/tote.html (乐手托特包)
6. membership.html (家庭年费会员 Plus 2026 官方大页，含 4-on-1 同款高能卡片全集)
7. ensemble-lab.html (4-on-1 职业乐队实验室专页)
8. study-abroad.html (留学规划专案 欢迎来访或咨询)
9. spaces.html (空间租用 6大项目 + 专业乐器租用 6大硬件全费率)
"""

import os

WEBSITE_DIR = "/Users/timomo/Documents/Momo音乐工作坊总文件/MomoMusicWebsite"
STORE_DIR = os.path.join(WEBSITE_DIR, "store")
os.makedirs(STORE_DIR, exist_ok=True)

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

def get_shared_header(current_page="home", depth=0):
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
                        Music Studio • Chengdu & Global
                    </span>
                </div>
            </a>

            <nav class="hidden lg:flex items-center gap-7">
                <a href="{home_href}#offerings" class="text-xs uppercase font-bold tracking-widest text-neutral-300 hover:text-momo-cyan transition-colors flex items-center gap-1.5">
                    <span>产品货架</span>
                    <span class="text-[9px] px-1.5 py-0.5 rounded bg-neutral-800 text-momo-mint font-mono">OFFERINGS</span>
                </a>
                <a href="{mem_href}" class="text-xs uppercase font-bold tracking-widest text-neutral-300 hover:text-momo-cyan transition-colors flex items-center gap-1.5">
                    <span>年费会员 PLUS</span>
                    <span class="text-[9px] px-1.5 py-0.5 rounded bg-neutral-800 text-momo-cyan font-mono">欢迎来访或咨询</span>
                </a>
                <a href="{study_href}" class="text-xs uppercase font-bold tracking-widest text-neutral-300 hover:text-[#D4AF37] transition-colors flex items-center gap-1.5">
                    <span>音乐留学规划</span>
                    <span class="text-[9px] px-1.5 py-0.5 rounded bg-neutral-800 text-[#D4AF37] font-mono">欢迎来访或咨询</span>
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
                <a href="{home_href}#booking" class="gradient-bg text-black px-4 sm:px-5 py-2 font-black text-xs uppercase tracking-wider hover:opacity-95 transform active:scale-95 transition-all shadow-lg shadow-momo-teal/20">
                    预约咨询 / 申请入会
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
                        <li><a href="{mem_href}" class="hover:text-momo-cyan text-momo-mint font-bold">家庭年费会员 Plus (欢迎来访或咨询)</a></li>
                        <li><a href="{study_href}" class="hover:text-[#D4AF37] text-[#D4AF37] font-bold">国际音乐留学规划 (欢迎来访或咨询)</a></li>
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

# -------------------------------------------------------------
# Store Pages
# -------------------------------------------------------------
def build_store_index():
    path = os.path.join(STORE_DIR, "index.html")
    html = f'''<!DOCTYPE html>
<html lang="zh-CN" class="dark scroll-smooth">
<head>
    <title>Momo 音乐美学商店 · 独立设计与教育公益周边</title>
    {COMMON_HEAD_DEFS}
</head>
<body class="bg-black text-white antialiased font-sans pt-24 selection:bg-momo-cyan selection:text-black">
    {get_shared_header("store", depth=1)}

    <main class="max-w-7xl mx-auto px-6 md:px-12 py-12">
        <div class="brutalist-border bg-[#0b0b0b] p-8 md:p-14 mb-16 relative overflow-hidden">
            <div class="max-w-3xl">
                <span class="text-xs font-mono text-momo-mint uppercase tracking-widest block mb-3">// BRAND MANIFESTO &amp; COMMUNITY SUPPORT</span>
                <h1 class="text-3xl md:text-5xl font-black uppercase tracking-tight text-white leading-tight">
                    一件周边背后的<br>
                    <span class="gradient-text">独立文化坚守与教育托举</span>
                </h1>
                <p class="text-neutral-300 text-sm md:text-base leading-relaxed mt-5">
                    在 Momo，我们从不生产廉价的流水线快时尚宣发品。每一件物件——无论是重达 320g 的精梳棉刺绣 T 恤、滑动开合的磨砂马口铁拨片盒，还是 180g 重磅黑胶声音集，都凝聚了我们对爵士即兴生活方式与 Teenage Engineering 工业设计的审美追求。
                </p>
                <div class="mt-6 border-l-2 border-momo-cyan pl-5 py-2 space-y-3 bg-neutral-900/60 p-4 rounded-r">
                    <p class="text-white text-xs md:text-sm font-bold">
                        ✦ 购买周边的核心意义：
                    </p>
                    <p class="text-neutral-300 text-xs md:text-sm leading-relaxed">
                        <strong>1. 独立文化的真实共鸣</strong>：将爵士即兴与当代先锋音乐态度穿在身上、带进日常。<br>
                        <strong>2. 用实际行动支持 Momo 的音乐教育事业</strong>：美学商店所有单品的销售净利润，将全额定向注入 <strong>Momo 青少年现代乐队合奏基金</strong> 与 <strong>大凉山乡村音乐教室教育支教</strong>。您的每一次下单，都在实打实托举一个孩子的音乐梦想与真实的乐队合奏舞台！
                    </p>
                </div>
                <div class="mt-8 flex flex-wrap items-center gap-4">
                    <div class="inline-flex items-center gap-2 px-3 py-1.5 bg-momo-mint/10 border border-momo-mint/30 rounded text-momo-mint text-xs font-mono">
                        <span>家庭会员可以聊到一件 Momo 纯黑刺绣文化衫。周边怎么取，欢迎来访或咨询</span>
                    </div>
                </div>
            </div>
        </div>

        <div class="mb-12 flex items-center justify-between border-b border-neutral-800 pb-4">
            <h2 class="text-2xl font-black uppercase text-white tracking-tight">精选周边单品 (4 ITEMS)</h2>
            <span class="text-xs font-mono text-neutral-400">点击进入专属产品大页查看参数与工艺</span>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
            <a href="./tshirt.html" class="brutalist-border bg-neutral-950 p-6 flex flex-col justify-between hover:border-momo-cyan group transition-all">
                <div>
                    <div class="aspect-square bg-[#0f0f0f] rounded overflow-hidden mb-5 relative border border-neutral-800">
                        <img src="../assets/images/momo_tshirt_te_style.jpg" alt="MOMO T-Shirt" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                        <div class="absolute top-2 left-2 px-2 py-0.5 bg-momo-mint text-black text-[10px] font-black uppercase rounded">
                            ★ 会员免费赠送
                        </div>
                    </div>
                    <div class="text-xs font-mono text-neutral-400 uppercase">APPAREL 01</div>
                    <h3 class="text-xl font-bold text-white group-hover:text-momo-cyan transition-colors mt-1">
                        MOMO 纯黑重磅刺绣文化衫
                    </h3>
                    <p class="text-xs text-neutral-400 mt-2 leading-relaxed">
                        320g 重磅精梳纯棉 · 巴黎世家经典落肩微阔版型 · 前胸同色暗黑高密立体微标刺绣
                    </p>
                </div>
                <div class="pt-5 border-t border-neutral-900 mt-5 flex items-center justify-between">
                    <span class="text-2xl font-black font-mono text-white">欢迎来访或咨询</span>
                    <span class="text-xs font-mono text-momo-cyan group-hover:underline">查阅参数 & 购买 &rarr;</span>
                </div>
            </a>

            <a href="./tote.html" class="brutalist-border bg-neutral-950 p-6 flex flex-col justify-between hover:border-momo-cyan group transition-all">
                <div>
                    <div class="aspect-square bg-[#0f0f0f] rounded overflow-hidden mb-5 relative border border-neutral-800">
                        <img src="../assets/images/momo_merch_collection.jpg" alt="MOMO Musician Tote" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                    </div>
                    <div class="text-xs font-mono text-neutral-400 uppercase">ACCESSORY 02</div>
                    <h3 class="text-xl font-bold text-white group-hover:text-momo-cyan transition-colors mt-1">
                        乐手纯黑机能帆布托特包
                    </h3>
                    <p class="text-xs text-neutral-400 mt-2 leading-relaxed">
                        16A 加密防泼水帆布 · 专为装载 16寸 MacBook 与大总谱设计 · 独立拨片暗袋
                    </p>
                </div>
                <div class="pt-5 border-t border-neutral-900 mt-5 flex items-center justify-between">
                    <span class="text-2xl font-black font-mono text-white">欢迎来访或咨询</span>
                    <span class="text-xs font-mono text-momo-cyan group-hover:underline">查阅参数 & 购买 &rarr;</span>
                </div>
            </a>

            <a href="./picks.html" class="brutalist-border bg-neutral-950 p-6 flex flex-col justify-between hover:border-momo-cyan group transition-all">
                <div>
                    <div class="aspect-square bg-[#0f0f0f] rounded overflow-hidden mb-5 relative border border-neutral-800">
                        <img src="../assets/images/real_momo_picks_tin.jpg" alt="MOMO Celluloid Picks" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                    </div>
                    <div class="text-xs font-mono text-neutral-400 uppercase">HARDWARE 03</div>
                    <h3 class="text-xl font-bold text-white group-hover:text-momo-cyan transition-colors mt-1">
                        纪念款赛璐珞吉他拨片黑锡盒
                    </h3>
                    <p class="text-xs text-neutral-400 mt-2 leading-relaxed">
                        消光磨砂马口铁滑动盒 · 6枚精选赛璐珞（0.71/0.96/1.14mm 扫弦与爵士重单音硬度全包）
                    </p>
                </div>
                <div class="pt-5 border-t border-neutral-900 mt-5 flex items-center justify-between">
                    <span class="text-2xl font-black font-mono text-white">欢迎来访或咨询</span>
                    <span class="text-xs font-mono text-momo-cyan group-hover:underline">查阅参数 & 购买 &rarr;</span>
                </div>
            </a>

            <a href="./vinyl.html" class="brutalist-border bg-neutral-950 p-6 flex flex-col justify-between hover:border-momo-cyan group transition-all">
                <div>
                    <div class="aspect-square bg-[#0f0f0f] rounded overflow-hidden mb-5 relative border border-neutral-800">
                        <img src="../assets/images/real_momo_vinyl.jpg" alt="MOMO Vinyl Record" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                        <div class="absolute top-2 left-2 px-2 py-0.5 bg-neutral-900/90 border border-neutral-700 text-momo-cyan text-[10px] font-black uppercase rounded">
                            限量 300 张
                        </div>
                    </div>
                    <div class="text-xs font-mono text-neutral-400 uppercase">VINYL 04</div>
                    <h3 class="text-xl font-bold text-white group-hover:text-momo-cyan transition-colors mt-1">
                        现场实录限定黑胶声音集
                    </h3>
                    <p class="text-xs text-neutral-400 mt-2 leading-relaxed">
                        180g 重磅黑胶德国压盘 · 收录菲比现场摇滚版《Jingle Bells》与 P&amp;R 24-bit 无损母带
                    </p>
                </div>
                <div class="pt-5 border-t border-neutral-900 mt-5 flex items-center justify-between">
                    <span class="text-2xl font-black font-mono text-white">欢迎来访或咨询</span>
                    <span class="text-xs font-mono text-momo-cyan group-hover:underline">查阅参数 & 购买 &rarr;</span>
                </div>
            </a>
        </div>
    </main>

    {get_shared_footer(depth=1)}
</body>
</html>
'''
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Generated store index:", path)

def build_product_pages():
    products = [
        {
            "id": "tshirt",
            "file": "tshirt.html",
            "name": "MOMO 纯黑重磅刺绣文化衫",
            "category": "APPAREL 01 · 官方文化穿戴",
            "price": "欢迎来访或咨询",
            "isMemberFree": True,
            "img": "../assets/images/momo_tshirt_te_style.jpg",
            "tagline": "320g 高密精梳纯棉 · 巴黎世家微落肩版型 · 德机 12000 针同色暗黑刺绣",
            "desc": "我们坚信，一件真正代表独立音乐精神的文化衫，应当具备经久耐穿的物理质感。选用 100% 320g 重磅精梳棉，经特殊预缩与酵素洗水处理，洗涤数十次依然保持挺阔质感。胸前采用德国进口田岛绣花机精密绣制 MOMO 盾牌暗黑微标，在不同光线下折射出若隐若现的光泽，低调内敛，专为乐手与音乐同行者而生。",
            "specs": [
                ("面料克重", "100% 320g 高密精梳纯棉 (超柔防缩水洗水工艺)"),
                ("版型裁剪", "Classic Oversized 巴黎世家落肩微阔剪裁"),
                ("刺绣工艺", "德国田岛机 12,000 针同色暗黑立体刺绣"),
                ("尺码选择", "S (适合 160-170cm) / M (适合 170-180cm) / L (适合 180cm+)"),
                ("养护建议", "反面常温机洗，中温熨烫，不建议强力烘干")
            ],
            "meaning": "这件文化衫和青年乐队的耗材、大凉山课堂的乐谱有关。怎么参与，欢迎来访或咨询。"
        },
        {
            "id": "picks",
            "file": "picks.html",
            "name": "纪念款赛璐珞吉他拨片黑锡盒",
            "category": "HARDWARE 03 · 乐手随行金属 EDC",
            "price": "欢迎来访或咨询",
            "isMemberFree": False,
            "img": "../assets/images/real_momo_picks_tin.jpg",
            "tagline": "消光磨砂马口铁盒 · 6枚定制赛璐珞拔片 · 爵士与扫弦硬度全包",
            "desc": "吉他手口袋里永远少一枚趁手的拨片。我们选用消光黑冲压马口铁制作这款推拉式滑动锡盒，单手轻推即可顺畅开启。内含 6 枚精挑细选的高级赛璐珞拨片，覆盖 0.71mm、0.96mm 与 1.14mm 三种硬度，表面烫印银箔 MOMO 微标，带来温润而清晰的触弦回弹感。",
            "specs": [
                ("盒体材质", "消光黑冲压马口铁 (滑轨阻尼手感良好，防刮耐磨)"),
                ("拨片数量", "6 枚装 (0.71mm ×2 / 0.96mm ×2 / 1.14mm ×2)"),
                ("拨片材质", "进口经典赛璐珞 (Celluloid · 经典温润音色)"),
                ("烫印工艺", "德国库尔兹冷烫哑光银箔微标"),
                ("适用场景", "民谣扫弦、摇滚切音、爵士单音速弹全天候随行")
            ],
            "meaning": "每卖出一盒拨片盒，我们将为大凉山山村学校的孩子们捐出一套木吉他琴弦和调音夹。小拨片，大心意。"
        },
        {
            "id": "vinyl",
            "file": "vinyl.html",
            "name": "现场实录限定黑胶声音集",
            "category": "VINYL 04 · 收藏级声音黑胶",
            "price": "欢迎来访或咨询",
            "isMemberFree": False,
            "img": "../assets/images/real_momo_vinyl.jpg",
            "tagline": "180g 重磅高保真黑胶 · 德国压片 · P&R Studio 24-bit 现场同期直录",
            "desc": "声音是有实体重量的。全球限量压制 300 张，采用 180g 重磅 Audiophile 纯黑黑胶材质。A面完整收录菲比与 Momo 艺术家团队在排练现场实录的摇滚版《Jingle Bells》及两首未公开的现场即兴 Jam；B面收录 18 人现代爵士大乐队作品。封套附赠 24 页全彩排练纪实胶片摄影画册。",
            "specs": [
                ("唱片规格", "12 英寸 / 33⅓ RPM / 180g 高密度重磅 Audiophile 黑胶"),
                ("母带来源", "P&R Studio 24-bit / 96kHz 模拟与数字混合同期直录"),
                ("压盘工厂", "德国顶级专业黑胶压片车间"),
                ("随盘附赠", "24P 纯质纸排练现场胶片印制摄影画册 + 独家数字无损母带下载码"),
                ("限量发行", "全球手工独立编号限量 300 张")
            ],
            "meaning": "黑胶唱片的全部收益直接汇入 Momo 青年原创音乐录音基金，用于扶持优秀学员免费完成人生第一张个人原创作品的多轨棚录。"
        },
        {
            "id": "tote",
            "file": "tote.html",
            "name": "乐手纯黑机能帆布托特包",
            "category": "ACCESSORY 02 · 乐手机能装备",
            "price": "欢迎来访或咨询",
            "isMemberFree": False,
            "img": "../assets/images/momo_merch_collection.jpg",
            "tagline": "16A 加密防泼水帆布 · 容纳 16寸电脑与乐谱大夹 · 独立拨片暗袋",
            "desc": "专为常年穿梭在排练室、录音棚与现场演出的音乐人量身设计。选用 16A 重磅加密纯棉机能帆布，具备微米级防泼水涂层。内部加厚防震隔层可轻松容纳 16 寸 MacBook Pro、iPad 与大总谱夹，侧边设有水杯固定扣，内里更有专属拉链拨片与耳机暗袋。",
            "specs": [
                ("主体材质", "16A 加密纯棉机能帆布 (微米级防泼水涂层)"),
                ("外部尺寸", "高 42cm × 宽 38cm × 底部加厚 12cm"),
                ("收纳布局", "16寸电脑加厚防震仓 + 乐谱主仓 + 独立拨片耳机拉链暗袋"),
                ("提带承重", "加固十字车线纯棉织带，经 15kg 抗拉疲劳测试"),
                ("颜色款式", "MOMO 经典炭黑 (Obsidian Black)")
            ],
            "meaning": "每一次购买托特包，都在以实打实的物资投入支持 Momo 独立音乐人社群的巡演与交流活动。"
        }
    ]

    for p in products:
        path = os.path.join(STORE_DIR, p["file"])
        member_badge = '<div class="inline-block px-3 py-1 bg-momo-mint/20 border border-momo-mint/50 text-momo-mint text-xs font-bold rounded mb-4">★ Momo 家庭年费会员 Plus 免费赠送一件</div>' if p["isMemberFree"] else ''
        specs_rows = "".join([f'''
            <div class="flex justify-between py-2 border-b border-neutral-900 text-xs sm:text-sm">
                <span class="text-neutral-500">{k}</span>
                <span class="text-neutral-200 font-mono text-right">{v}</span>
            </div>
        ''' for k, v in p["specs"]])

        html = f'''<!DOCTYPE html>
<html lang="zh-CN" class="dark scroll-smooth">
<head>
    <title>{p["name"]} · Momo 音乐美学商店</title>
    {COMMON_HEAD_DEFS}
</head>
<body class="bg-black text-white antialiased font-sans pt-24 selection:bg-momo-cyan selection:text-black">
    {get_shared_header("store", depth=1)}

    <main class="max-w-7xl mx-auto px-6 md:px-12 py-12">
        <div class="text-xs font-mono text-neutral-500 mb-8 flex items-center gap-2">
            <a href="../index.html" class="hover:text-white">首页</a>
            <span>/</span>
            <a href="./index.html" class="hover:text-white">Momo 音乐美学商店</a>
            <span>/</span>
            <span class="text-neutral-300">{p["name"]}</span>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-start">
            <div class="lg:col-span-7">
                <div class="aspect-square w-full brutalist-border bg-neutral-950 overflow-hidden relative">
                    <img src="{p["img"]}" alt="{p["name"]}" class="w-full h-full object-cover">
                </div>
                <div class="mt-4 text-xs font-mono text-neutral-500 text-center">
                    // HIGH RESOLUTION HARDWARE STILL LIFE · 真实实物摄影
                </div>
            </div>

            <div class="lg:col-span-5 space-y-6">
                <div>
                    <span class="text-xs font-mono text-momo-mint uppercase tracking-widest">{p["category"]}</span>
                    <h1 class="text-3xl sm:text-4xl font-black uppercase text-white mt-2 tracking-tight">
                        {p["name"]}
                    </h1>
                    <div class="text-3xl font-black font-mono text-momo-cyan mt-3">{p["price"]}</div>
                    <p class="text-neutral-400 text-xs font-mono mt-1">{p["tagline"]}</p>
                </div>

                {member_badge}

                <div class="border-t border-neutral-900 pt-5 text-neutral-300 text-xs sm:text-sm leading-relaxed">
                    {p["desc"]}
                </div>

                <div class="bg-[#0f0f0f] brutalist-border p-5 rounded space-y-2">
                    <div class="text-xs font-bold text-white flex items-center gap-2">
                        <span class="w-2 h-2 rounded-full bg-momo-cyan animate-pulse"></span>
                        购买这件周边的真实意义与教育支持
                    </div>
                    <p class="text-xs text-neutral-400 leading-relaxed">
                        {p["meaning"]}
                    </p>
                </div>

                <div class="border-t border-neutral-900 pt-4">
                    <h3 class="text-xs font-mono font-bold uppercase tracking-wider text-neutral-400 mb-3">规格与工艺参数 (SPECIFICATIONS)</h3>
                    <div class="divide-y divide-neutral-900">
                        {specs_rows}
                    </div>
                </div>

                <div class="pt-6 border-t border-neutral-900 space-y-4">
                    <div class="space-y-3 bg-neutral-950 p-6 brutalist-border">
                        <h4 class="text-xs font-bold uppercase text-white tracking-wider">即刻登记订购 / 自提寄送</h4>
                        <div>
                            <label class="text-[11px] font-mono text-neutral-400 block mb-1">您的称呼 / 微信</label>
                            <input type="text" id="order-name" placeholder="如：李先生 / 微信同号" class="w-full bg-neutral-900 border border-neutral-800 px-3 py-2 text-xs text-white focus:outline-none focus:border-momo-cyan">
                        </div>
                        <div>
                            <label class="text-[11px] font-mono text-neutral-400 block mb-1">联系电话 / 顺丰邮寄地址（或到店自提）</label>
                            <input type="text" id="order-address" placeholder="如：成都市武侯区银都花园自提 / 邮寄详细地址" class="w-full bg-neutral-900 border border-neutral-800 px-3 py-2 text-xs text-white focus:outline-none focus:border-momo-cyan">
                        </div>
                        <div>
                            <label class="text-[11px] font-mono text-neutral-400 block mb-1">尺码/备注说明</label>
                            <input type="text" id="order-size" placeholder="如：尺码 L / 会员姓名立享特权" class="w-full bg-neutral-900 border border-neutral-800 px-3 py-2 text-xs text-white focus:outline-none focus:border-momo-cyan">
                        </div>
                        <button type="button" onclick="submitMerchOrder('{p["name"]}')" class="w-full gradient-bg text-black py-3 font-black text-xs uppercase tracking-wider hover:opacity-90">
                            确认提交订单 ({p["price"]}) &rarr;
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </main>

    <script>
        function submitMerchOrder(productName) {{
            const name = document.getElementById('order-name').value.trim();
            const address = document.getElementById('order-address').value.trim();
            if (!name || !address) {{
                alert('请填写称呼与联系方式/地址，我们将尽快为您安排！');
                return;
            }}
            alert('订单已成功提交！【' + productName + '】\\n顾问与主理人团队将尽快通过微信联络您完成确认，感谢您对 Momo 音乐教育与独立文化的大力支持！');
        }}
    </script>

    {get_shared_footer(depth=1)}
</body>
</html>
'''
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print("Generated product page:", path)

# -------------------------------------------------------------
# Study Abroad Page
# -------------------------------------------------------------
def build_study_abroad_page():
    path = os.path.join(WEBSITE_DIR, "study-abroad.html")
    html = f'''<!DOCTYPE html>
<html lang="zh-CN" class="dark scroll-smooth">
<head>
    <title>作品积累与方向规划 | 高信博士与艺术家团队 · 成都Momo约书亚音乐工作坊</title>
    {COMMON_HEAD_DEFS}
</head>
<body class="bg-black text-white antialiased font-sans pt-24 selection:bg-momo-cyan selection:text-black">
    {get_shared_header("study-abroad", depth=0)}

    <main class="max-w-7xl mx-auto px-6 md:px-12 py-12">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center mb-16 pb-16 border-b border-neutral-900">
            <div class="lg:col-span-7 space-y-6">
                <span class="text-xs font-mono font-bold uppercase tracking-widest text-[#D4AF37] block">// WORKS & DIRECTION</span>
                <h1 class="text-3xl sm:text-5xl md:text-6xl font-black uppercase tracking-tight text-white leading-tight">
                    作品积累<br>
                    <span class="text-[#D4AF37]">与方向规划</span>
                </h1>
                <div class="flex items-baseline gap-4 pt-2">
                    <span class="text-3xl sm:text-4xl font-black text-[#D4AF37]">欢迎来访或咨询</span>
                    <span class="text-sm font-mono text-neutral-400">/ 当面聊聊作品与接下来的方向</span>
                </div>
                <p class="text-neutral-300 text-sm sm:text-base leading-relaxed">
                    成都Momo约书亚音乐工作坊陪你把正在做的曲子、合奏和棚内录音慢慢积累成可以反复听的作品，并一起梳理接下来想走的方向。教学方法参考伯克利现代音乐课程里重视听、唱、合奏与写作的做法。具体安排欢迎来访或咨询。
                </p>
                <div class="border-l-2 border-[#D4AF37] pl-5 py-2 space-y-2 bg-neutral-950 p-4">
                    <div class="text-white text-xs sm:text-sm font-bold">
                        ✦ 核心交付阵容：
                    </div>
                    <div class="text-neutral-300 text-xs sm:text-sm leading-relaxed">
                        • <strong>学术领衔</strong>：高信博士（管乐与和声学博士 · 作品与方向顾问）<br>
                        • <strong>交付底盘</strong>：Momo 13 位一线艺术家团队全程配合，完成专业课教学与乐队合奏支撑<br>
                        • <strong>品控跟进</strong>：品牌创始人 Timo 亲自参与并把控录音棚同期声像与最终作品集交付
                    </div>
                </div>
            </div>

            <div class="lg:col-span-5">
                <div class="aspect-[4/3] brutalist-border bg-neutral-950 overflow-hidden relative">
                    <img src="./assets/images/conservatory_mentorship_hero.jpg" alt="Conservatory Prep" class="w-full h-full object-cover">
                </div>
                <div class="text-[11px] font-mono text-neutral-500 mt-3 text-center">
                    // P&amp;R STUDIO 24-TRACK RECORDING FACILITY · 录音棚同期实录作品集
                </div>
            </div>
        </div>

        <div class="mb-20">
            <h2 class="text-2xl sm:text-3xl font-black uppercase text-white mb-10 text-center">作品积累与方向规划，我们一起做的五件事</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                <div class="brutalist-border bg-neutral-950 p-8 space-y-3">
                    <div class="text-xs font-mono text-[#D4AF37] font-bold">MODULE 01</div>
                    <h3 class="text-lg font-bold text-white">听听你现在的声音</h3>
                    <p class="text-xs text-neutral-400 leading-relaxed">
                        高信博士和你一起听视唱、和声、演奏和即兴，看清作品现在的样子，以及下一步可以练什么。
                    </p>
                </div>
                <div class="brutalist-border bg-neutral-950 p-8 space-y-3">
                    <div class="text-xs font-mono text-[#D4AF37] font-bold">MODULE 02</div>
                    <h3 class="text-lg font-bold text-white">方向怎么排</h3>
                    <p class="text-xs text-neutral-400 leading-relaxed">
                        按你正在做的曲子和能投入的时间，一起排接下来几个月的作品和合奏。不列院校名单。具体安排欢迎来访或咨询。
                    </p>
                </div>
                <div class="brutalist-border bg-neutral-950 p-8 space-y-3">
                    <div class="text-xs font-mono text-[#D4AF37] font-bold">MODULE 03</div>
                    <h3 class="text-lg font-bold text-white">需要时向外请教</h3>
                    <p class="text-xs text-neutral-400 leading-relaxed">
                        若你希望听听外面老师怎么说，我们可以协助约一次交流。交流用来改作品。
                    </p>
                </div>
                <div class="brutalist-border bg-neutral-950 p-8 space-y-3">
                    <div class="text-xs font-mono text-[#D4AF37] font-bold">MODULE 04</div>
                    <h3 class="text-lg font-bold text-white">和乐队把作品练出来</h3>
                    <p class="text-xs text-neutral-400 leading-relaxed">
                        依托工作室的真实乐队，几位艺术家老师进排练，把合奏的呼吸和律动放进作品里。
                    </p>
                </div>
                <div class="brutalist-border bg-neutral-950 p-8 space-y-3">
                    <div class="text-xs font-mono text-[#D4AF37] font-bold">MODULE 05</div>
                    <h3 class="text-lg font-bold text-white">进棚把作品录下来</h3>
                    <p class="text-xs text-neutral-400 leading-relaxed">
                        由制作人与创始人 Timo 一起，在录音棚完成多轨现场录音，留下可以反复听、可以继续改的作品。
                    </p>
                </div>
                <div class="brutalist-border bg-neutral-950 p-8 space-y-3 flex flex-col justify-between">
                    <div>
                        <div class="text-xs font-mono text-momo-mint font-bold">GUARANTEE</div>
                        <h3 class="text-lg font-bold text-white">透明合同 · 全程陪伴</h3>
                        <p class="text-xs text-neutral-400 leading-relaxed">
                            过程怎么安排，欢迎来访或咨询，当面把步骤说清楚。
                        </p>
                    </div>
                    <button type="button" onclick="document.getElementById('study-apply').scrollIntoView({{behavior:'smooth'}})" class="w-full gradient-bg text-black py-2.5 font-bold text-xs uppercase tracking-wider">
                        欢迎来访或咨询 &rarr;
                    </button>
                </div>
            </div>
        </div>

        <div id="study-apply" class="max-w-2xl mx-auto brutalist-border bg-[#0d0d0d] p-8 sm:p-12 mb-16">
            <h3 class="text-2xl font-black uppercase text-white text-center mb-2">预约一次作品与方向的面谈</h3>
            <p class="text-xs font-mono text-neutral-400 text-center mb-8">成都Momo约书亚音乐工作坊会安排高信博士与创始人 Timo，和你以及家人当面聊聊正在做的作品</p>
            <form onsubmit="handleStudyForm(event)" class="space-y-4">
                <div>
                    <label class="text-xs font-mono text-neutral-400 block mb-1">你与家人的称呼 *</label>
                    <input type="text" id="study-name" required placeholder="如：张同学与父亲" class="w-full bg-neutral-900 border border-neutral-800 px-4 py-3 text-xs text-white focus:outline-none focus:border-[#D4AF37]">
                </div>
                <div>
                    <label class="text-xs font-mono text-neutral-400 block mb-1">微信号 / 手机号 *</label>
                    <input type="text" id="study-phone" required placeholder="如：13800000000 (微信同号)" class="w-full bg-neutral-900 border border-neutral-800 px-4 py-3 text-xs text-white focus:outline-none focus:border-[#D4AF37]">
                </div>
                <div>
                    <label class="text-xs font-mono text-neutral-400 block mb-1">正在做的作品与想聊的方向</label>
                    <input type="text" id="study-target" placeholder="如：爵士萨克斯 / 想先把三首曲子录下来" class="w-full bg-neutral-900 border border-neutral-800 px-4 py-3 text-xs text-white focus:outline-none focus:border-[#D4AF37]">
                </div>
                <button type="submit" class="w-full bg-[#D4AF37] text-black py-4 font-black text-xs uppercase tracking-wider hover:opacity-90">
                    提交面谈预约 &rarr;
                </button>
            </form>
        </div>
    </main>

    <script>
        function handleStudyForm(e) {{
            e.preventDefault();
            const phone = document.getElementById('study-phone').value;
            alert('面谈预约已收到。高信博士与 Timo 主理人将在 12 小时内亲自联络您（' + phone + '），为您安排专属作品集诊断会议。');
        }}
    </script>

    {get_shared_footer(depth=0)}
</body>
</html>
'''
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Generated study abroad page:", path)

# -------------------------------------------------------------
# Execute All Builds
# -------------------------------------------------------------
if __name__ == "__main__":
    build_store_index()
    build_product_pages()
    build_membership_page()
    build_study_abroad_page()
    build_spaces_page()
    build_ensemble_lab_page()
    print("ALL SECONDARY & DEDICATED PAGES GENERATED SUCCESSFULLY!")
