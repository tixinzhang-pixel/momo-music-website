# -*- coding: utf-8 -*-
"""
build_berklee_momo_website.py
Implement full Berklee-inspired visual aesthetic, style deck audio engine,
uncrowded membership, signature camps recruitment, faculty correction & infinite marquee,
MI-style admission form, and complete removal of coffee and shangri-la.
"""

import os
import re

WEBSITE_DIR = "/Users/timomo/Documents/Momo音乐工作坊总文件/MomoMusicWebsite"
COMPILE_SCRIPT = os.path.join(WEBSITE_DIR, "compile_complete_website.py")

with open(COMPILE_SCRIPT, "r", encoding="utf-8") as f:
    compile_code = f.read()

# 1. Update footer coffee link
compile_code = compile_code.replace(
    '<span>预约来空间喝杯咖啡</span><span>&rsaquo;</span>',
    '<span>预约来空间探访 / 试奏交流</span><span>&rsaquo;</span>'
)

# 2. Update upgrade_existing_subpage coffee link
compile_code = compile_code.replace(
    "openBookingModal('预约来空间喝杯咖啡 / 现场体验沟通')",
    "openBookingModal('预约来空间探访 / 现场体验沟通')"
)

# 3. Define the new Berklee-styled Membership + Signature Camps + Corrected Faculty + MI Admission sections
# Locate Section 02 start and Section 05 Bento start in compile_code
pos_sec02 = compile_code.find('<!-- ==================== 02. 2026 PLUS 会员旗舰')
pos_bento = compile_code.find('<!-- ==================== 05. 6 大专页 Bento 瓷砖')

if pos_sec02 == -1 or pos_bento == -1:
    raise Exception(f"Failed to find markers: pos_sec02={pos_sec02}, pos_bento={pos_bento}")

print(f"Found markers: sec02={pos_sec02}, bento={pos_bento}")

# Extract the existing style-deck and marquee tracks from compile_code
pos_style_deck = compile_code.find('<section id="style-deck"', pos_sec02)
pos_faculty = compile_code.find('<!-- ==================== 04. 导师长廊', pos_style_deck)
pos_marquee_wrapper = compile_code.find('<div class="marquee-wrapper', pos_faculty)
pos_faculty_end = compile_code.find('</section>', pos_marquee_wrapper) + len('</section>')

style_deck_block = compile_code[pos_style_deck:pos_faculty].strip()
marquee_wrapper_block = compile_code[pos_marquee_wrapper:pos_faculty_end].strip()

# Build Section 02: 2026 PLUS 会员旗舰 (通透白底 · 对标 Berklee 学院现代质感 · 大留白 · 突出实体黑金卡)
section_02_membership = '''
        <!-- ==================== 02. 2026 PLUS 会员旗舰：通透白底 · 突出黑金会员卡 · 舒展不打挤 ==================== -->
        <section id="membership" class="space-y-6 pt-6">
            <div class="rounded-3xl p-8 sm:p-14 lg:p-16 bg-white text-black border border-neutral-200/90 shadow-[0_25px_70px_-15px_rgba(0,0,0,0.08)] relative overflow-hidden">
                <!-- 顶部眉标与主题声明 -->
                <div class="flex flex-col sm:flex-row sm:items-baseline justify-between pb-8 border-b border-neutral-200/80 gap-3">
                    <div>
                        <span class="text-[11px] font-mono-code uppercase tracking-[0.25em] text-neutral-500 font-bold">
                            // BECOME A MEMBER · 2026 PLUS PASS
                        </span>
                        <h2 class="text-3xl sm:text-4xl lg:text-[42px] font-black tracking-tight text-black mt-2 leading-[1.15]">
                            邀请你和家人，成为 MOMO 家庭音乐会员
                        </h2>
                    </div>
                    <span class="text-xs font-mono-code text-neutral-500 bg-neutral-100 px-3.5 py-1.5 rounded-full w-fit">
                        ONE PASS · WHOLE FAMILY
                    </span>
                </div>

                <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-14 items-center pt-8">
                    <!-- 左侧 5 列：高亮突出实体黑金会员卡 (3D 浮动立体感 + 标价清晰) -->
                    <div class="lg:col-span-5 flex flex-col items-center">
                        <div class="tilt-card-container w-full max-w-sm">
                            <div class="tilt-card relative w-full rounded-3xl p-3 bg-gradient-to-br from-neutral-900 via-black to-neutral-800 shadow-[0_20px_50px_rgba(0,0,0,0.35)] border border-neutral-700/60 group cursor-pointer transition-transform duration-500 hover:-translate-y-1">
                                <div class="rounded-2xl overflow-hidden bg-black relative">
                                    <img
                                        src="./assets/images/momo_platinum_card.jpg"
                                        alt="MOMO 2026 Plus 尊享黑金实体会员卡"
                                        class="w-full aspect-[1.58/1] object-cover group-hover:scale-105 transition-transform duration-700"
                                    >
                                    <div class="absolute inset-0 bg-gradient-to-t from-black/75 via-transparent to-transparent"></div>
                                    <div class="absolute bottom-3 left-4 right-4 flex items-center justify-between text-xs font-mono-code">
                                        <span class="text-white font-bold tracking-wider">2026 PLUS PASS</span>
                                        <span class="text-amber-300 font-bold">MOMO FAMILY</span>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- 卡片下方价格与保障标签 (清楚明了) -->
                        <div class="mt-8 text-center space-y-2.5">
                            <div class="flex items-baseline justify-center gap-2">
                                <span class="text-3xl sm:text-4xl font-black text-black tracking-tight">欢迎来访或咨询</span>
                                <span class="text-xs sm:text-sm text-neutral-500 font-mono-code">当面了解会员</span>
                            </div>
                            <div class="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full bg-emerald-50 border border-emerald-300/60 text-xs text-emerald-800 font-semibold">
                                <span>★</span>
                                <span>7 天无理由全额退款保障 · 赠定制文化衫</span>
                            </div>
                        </div>
                    </div>

                    <!-- 右侧 7 列：权益清楚明了 · 留白舒适 · 绝不打挤 -->
                    <div class="lg:col-span-7 space-y-6">
                        <div>
                            <span class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-neutral-100 text-xs font-mono-code text-neutral-700 font-bold border border-neutral-200">
                                一人入会 · 全家共享
                            </span>
                            <h3 class="text-2xl sm:text-3xl font-extrabold text-black mt-3 tracking-tight leading-snug">
                                为全家构建 365 天真实音乐生活底座
                            </h3>
                            <p class="text-xs sm:text-sm text-neutral-600 mt-2 leading-relaxed font-normal">
                                拒绝传统培训机构按次消课的焦虑与机械打卡。MOMO 年费会员让音乐真正成为家庭的日常生活底色：父母与孩子随时走进录音棚与声学排练室，与一线爵士乐导师同台合奏。
                            </p>
                        </div>

                        <!-- 4 大核心权益 (大行距，舒展大气，不打挤) -->
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-1">
                            <div class="p-4 rounded-2xl bg-neutral-50/90 border border-neutral-200/80 hover:border-black/30 transition-all">
                                <div class="text-black font-mono-code text-xs font-bold">01 / 专属指导</div>
                                <h4 class="text-sm font-bold text-black mt-1">12 次 1对1 深度定制课</h4>
                                <p class="text-[11px] text-neutral-600 mt-1.5 leading-relaxed">全系乐器、声乐与即兴自由选修，支持家庭成员跨乐器流转。</p>
                            </div>
                            <div class="p-4 rounded-2xl bg-neutral-50/90 border border-neutral-200/80 hover:border-black/30 transition-all">
                                <div class="text-black font-mono-code text-xs font-bold">02 / 真实合奏</div>
                                <h4 class="text-sm font-bold text-black mt-1">4师1生 真实乐队合奏</h4>
                                <p class="text-[11px] text-neutral-600 mt-1.5 leading-relaxed">拒绝罐头伴奏带！4位真正音乐家围着你合奏，声场临场感极强。</p>
                            </div>
                            <div class="p-4 rounded-2xl bg-neutral-50/90 border border-neutral-200/80 hover:border-black/30 transition-all">
                                <div class="text-black font-mono-code text-xs font-bold">03 / 棚录单曲</div>
                                <h4 class="text-sm font-bold text-black mt-1">P&R Studio 录音棚单曲实录</h4>
                                <p class="text-[11px] text-neutral-600 mt-1.5 leading-relaxed">24轨真棚同期多麦实录 + 混音，发表属于全家的年度纪念唱片。</p>
                            </div>
                            <div class="p-4 rounded-2xl bg-neutral-50/90 border border-neutral-200/80 hover:border-black/30 transition-all">
                                <div class="text-black font-mono-code text-xs font-bold">04 / 全家共享</div>
                                <h4 class="text-sm font-bold text-black mt-1">家庭专属档案与空间通行</h4>
                                <p class="text-[11px] text-neutral-600 mt-1.5 leading-relaxed">桐梓林与麓湖双空间畅通，全家三代共享艺术沙龙与排练场。</p>
                            </div>
                        </div>

                        <!-- 操作按钮组 -->
                        <div class="pt-3 flex flex-wrap items-center gap-4">
                            <a
                                href="#admission"
                                class="px-8 py-3.5 rounded-full bg-black hover:bg-neutral-800 text-white font-extrabold text-xs sm:text-sm transition-all shadow-xl shadow-black/10 flex items-center gap-2 cursor-pointer"
                            >
                                <span>立即递接入会申请 · 预约评估</span>
                                <span>&rarr;</span>
                            </a>
                            <a
                                href="./membership.html"
                                class="px-6 py-3.5 rounded-full bg-neutral-100 hover:bg-neutral-200 border border-neutral-300 text-neutral-800 font-semibold text-xs sm:text-sm transition-all flex items-center gap-1.5"
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

# Build Section 03: 【新增独立重磅板块】MOMO 国际音乐主题营会招募专区 (暖米白/浅砂底 · 三大真实 IP)
section_03_camps = '''
        <!-- ==================== 03. MOMO 国际音乐主题营会招募专区：暖砂米白底 · 三大经典 IP ==================== -->
        <section id="camps" class="space-y-6 pt-4">
            <div class="rounded-3xl p-8 sm:p-14 lg:p-16 bg-[#F4F3EF] text-black border border-neutral-300/80 shadow-[0_20px_50px_-15px_rgba(0,0,0,0.06)] relative overflow-hidden">
                <!-- 标题头 -->
                <div class="flex flex-col sm:flex-row sm:items-baseline justify-between pb-8 border-b border-neutral-300/80 gap-3">
                    <div>
                        <span class="text-[11px] font-mono-code uppercase tracking-[0.25em] text-neutral-600 font-bold">
                            // SIGNATURE CAMPS · 国际音乐营会招募
                        </span>
                        <h2 class="text-3xl sm:text-4xl lg:text-[40px] font-black tracking-tight text-black mt-2 leading-[1.15]">
                            在真实的声场与山野里，让热爱爆发
                        </h2>
                        <p class="text-xs sm:text-sm text-neutral-600 mt-2 max-w-2xl leading-relaxed">
                            告别枯燥考级应试，在沉浸式全日制合奏中突破音乐极限。MOMO 三大经典营会 IP 现已开放近期席位预约与简章咨询：
                        </p>
                    </div>
                    <span class="text-xs font-mono-code text-neutral-600 bg-white/80 px-3.5 py-1.5 rounded-full border border-neutral-200 w-fit">
                        WINTER &amp; SUMMER IMMERSION
                    </span>
                </div>

                <!-- 3 大营会 IP 卡片矩阵 -->
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6 pt-8">
                    
                    <!-- 营会 1: 冬季共鸣音乐营 -->
                    <div class="rounded-2xl bg-white p-7 border border-neutral-200/80 shadow-md flex flex-col justify-between hover:shadow-xl hover:-translate-y-1 transition-all duration-300">
                        <div class="space-y-4">
                            <div class="flex items-center justify-between">
                                <span class="px-2.5 py-1 rounded-full bg-cyan-50 text-cyan-800 text-[10px] font-mono-code font-bold border border-cyan-200">
                                    寒假档期 · 5天4晚 · 招募16席
                                </span>
                                <span class="text-xs font-mono-code text-neutral-400">CAMP 01</span>
                            </div>
                            <div>
                                <h3 class="text-xl font-black text-black">Momo 冬季共鸣音乐营</h3>
                                <p class="text-xs font-serif italic text-neutral-500 mt-0.5">“让共鸣，自然发生”</p>
                            </div>
                            <p class="text-xs text-neutral-600 leading-relaxed">
                                面向 6–16 岁青少年乐手与音乐家庭。零门槛走进现代流行音乐通识，跨乐器破冰合奏，建立真正耳朵灵敏度。
                            </p>
                            <ul class="text-[11px] text-neutral-600 space-y-1.5 border-t border-neutral-100 pt-3">
                                <li class="flex items-center gap-1.5"><span class="text-emerald-600 font-bold">✓</span> 现代音乐全方位通识与概念认知</li>
                                <li class="flex items-center gap-1.5"><span class="text-emerald-600 font-bold">✓</span> 乐队多声部合奏与跨声部互动</li>
                                <li class="flex items-center gap-1.5"><span class="text-emerald-600 font-bold">✓</span> 家庭结营展演汇报音乐会实录</li>
                            </ul>
                        </div>
                        <div class="pt-6">
                            <button
                                type="button"
                                onclick="openBookingModal('咨询【Momo 冬季共鸣音乐营】简章与席位')"
                                class="w-full py-2.5 rounded-xl bg-black hover:bg-neutral-800 text-white font-bold text-xs transition-all shadow text-center"
                            >
                                咨询冬季营简章 &amp; 预约席位 &rarr;
                            </button>
                        </div>
                    </div>

                    <!-- 营会 2: 夏季即兴音乐营会 -->
                    <div class="rounded-2xl bg-white p-7 border border-neutral-200/80 shadow-md flex flex-col justify-between hover:shadow-xl hover:-translate-y-1 transition-all duration-300">
                        <div class="space-y-4">
                            <div class="flex items-center justify-between">
                                <span class="px-2.5 py-1 rounded-full bg-amber-50 text-amber-800 text-[10px] font-mono-code font-bold border border-amber-200">
                                    暑假档期 · 7天6晚 · 进阶集训
                                </span>
                                <span class="text-xs font-mono-code text-neutral-400">CAMP 02</span>
                            </div>
                            <div>
                                <h3 class="text-xl font-black text-black">Momo 夏季即兴音乐营会</h3>
                                <p class="text-xs font-serif italic text-neutral-500 mt-0.5">“听见即弹奏，在律动中自由呼吸”</p>
                            </div>
                            <p class="text-xs text-neutral-600 leading-relaxed">
                                面向有乐器或声乐基础的进阶学员。告别视谱依赖，攻克五度圈与即兴和声思维，享受草坪夏日真乐队合奏。
                            </p>
                            <ul class="text-[11px] text-neutral-600 space-y-1.5 border-t border-neutral-100 pt-3">
                                <li class="flex items-center gap-1.5"><span class="text-amber-600 font-bold">✓</span> 每日 1对1 资深名师私教精修课</li>
                                <li class="flex items-center gap-1.5"><span class="text-amber-600 font-bold">✓</span> Gospel 现代合唱团实战排练</li>
                                <li class="flex items-center gap-1.5"><span class="text-amber-600 font-bold">✓</span> 夏日露天草坪即兴 Jam 狂欢夜</li>
                            </ul>
                        </div>
                        <div class="pt-6">
                            <button
                                type="button"
                                onclick="openBookingModal('咨询【Momo 夏季即兴音乐营会】简章与席位')"
                                class="w-full py-2.5 rounded-xl bg-black hover:bg-neutral-800 text-white font-bold text-xs transition-all shadow text-center"
                            >
                                咨询夏季营简章 &amp; 预约席位 &rarr;
                            </button>
                        </div>
                    </div>

                    <!-- 营会 3: 102·Momo 国际爵士音乐夏令营 -->
                    <div class="rounded-2xl bg-neutral-900 text-white p-7 border border-neutral-800 shadow-xl flex flex-col justify-between hover:-translate-y-1 transition-all duration-300">
                        <div class="space-y-4">
                            <div class="flex items-center justify-between">
                                <span class="px-2.5 py-1 rounded-full bg-white/10 text-amber-300 text-[10px] font-mono-code font-bold border border-white/20">
                                    欢迎来预约了解
                                </span>
                                <span class="text-xs font-mono-code text-neutral-500">CAMP 03</span>
                            </div>
                            <div>
                                <h3 class="text-xl font-black text-white">102 · Momo 国际爵士音乐夏令营</h3>
                                <p class="text-xs font-mono text-cyan-300 mt-0.5">“Conquered Donna Lee At 360BPM”</p>
                            </div>
                            <p class="text-xs text-neutral-300 leading-relaxed">
                                国际高规格爵士集训，全外籍与海归名师同行同住。挑战快速波普爵士标准曲，大乐队声部精修与顶级录音棚实测。
                            </p>
                            <ul class="text-[11px] text-neutral-300 space-y-1.5 border-t border-neutral-800 pt-3">
                                <li class="flex items-center gap-1.5"><span class="text-cyan-400 font-bold">✓</span> 全外籍与海归一线爵士乐导师同住同行</li>
                                <li class="flex items-center gap-1.5"><span class="text-cyan-400 font-bold">✓</span> 国际标准 Big Band 爵士大乐队总谱排练</li>
                                <li class="flex items-center gap-1.5"><span class="text-cyan-400 font-bold">✓</span> 成都地标专业大剧院/音乐厅结营公演</li>
                            </ul>
                        </div>
                        <div class="pt-6">
                            <button
                                type="button"
                                onclick="openBookingModal('申请【102·Momo 国际爵士夏令营】Audition 考核')"
                                class="w-full py-2.5 rounded-xl bg-gradient-to-r from-amber-400 to-amber-200 text-black font-extrabold text-xs transition-all shadow text-center hover:opacity-90"
                            >
                                申请专业考核 Audition &rarr;
                            </button>
                        </div>
                    </div>

                </div>

                <!-- 底部联合办营声明条 -->
                <div class="mt-8 pt-6 border-t border-neutral-300/80 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-neutral-600">
                    <div class="flex items-center gap-2">
                        <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
                        <span>营会面向全国招生，支持家庭陪同参营。成都桐梓林与麓湖双空间提供专程声学保障。</span>
                    </div>
                    <button type="button" onclick="openTimoModal()" class="text-black font-bold hover:underline inline-flex items-center gap-1">
                        <span>如有学校/机构大乐队集训合作需求，致信主理人 Timo</span>
                        <span>&rarr;</span>
                    </button>
                </div>
            </div>
        </section>
'''

# Build Section 05: 导师长廊 (认知纠偏标题与导言 + 双向无限流动跑马灯)
section_05_faculty = f'''
        <!-- ==================== 05. 真实常驻师资长廊：标题与认知纠偏 · 双向无缝横向流动 · 触碰悬停定格 ==================== -->
        <section class="space-y-6">
            <div class="flex flex-col sm:flex-row sm:items-end justify-between border-b border-white/[0.08] pb-4 gap-3">
                <div>
                    <span class="text-[10px] font-mono-code uppercase tracking-[0.25em] text-cyan-400 font-bold">
                        // FACULTY &amp; RESIDENT ARTISTS · 真实常驻师资团队
                    </span>
                    <h2 class="text-2xl sm:text-3xl font-extrabold tracking-tight text-white mt-1">
                        他们不仅是舞台上的艺术家，更是你每一节课的真实导师
                    </h2>
                    <p class="text-xs sm:text-sm text-neutral-300 max-w-3xl leading-relaxed mt-2 font-light">
                        拒绝名师挂名噱头！以下 35 位国内外一线爵士演奏家、管乐博士与音乐制作人，均为 MOMO 真实常驻的一线教学团队。只要成为 MOMO 会员，你与家人便可以在线下桐梓林/麓湖双空间或线上，直接预约他们的 1对1 课程与 4师1生真乐队合奏指导。
                    </p>
                </div>
                <a href="./faculty.html" class="text-xs text-neutral-400 hover:text-white font-mono-code flex items-center gap-1 transition-colors shrink-0">
                    <span>查阅全部 35 位导师档案</span>
                    <span>&rarr;</span>
                </a>
            </div>

            {marquee_wrapper_block}
'''

# Build Section 06: 【整版 MI 风格】MOMO 入会申请与专业评估 Application for Admission
section_06_admission = '''
        <!-- ==================== 06. MI 学院风格整版入会申请大版面 (APPLICATION FOR ADMISSION) ==================== -->
        <section id="admission" class="space-y-6 pt-6">
            <div class="max-w-4xl mx-auto rounded-3xl bg-white text-black p-8 sm:p-14 lg:p-16 border border-neutral-300 shadow-2xl relative overflow-hidden">
                <!-- 顶标 MI 风格徽章与标题 -->
                <div class="text-center space-y-2 pb-8 border-b border-neutral-200">
                    <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-red-600 text-white text-[11px] font-mono-code font-bold uppercase tracking-wider">
                        <span>★ APPLICATION FOR ADMISSION</span>
                    </div>
                    <h3 class="text-3xl sm:text-4xl font-black text-black tracking-tight mt-2">
                        提交入会申请与专业评估预约
                    </h3>
                    <p class="text-xs sm:text-sm text-neutral-600 max-w-xl mx-auto leading-relaxed">
                        迈向真正家庭音乐生活的第一步！请选择您的学习方向与目标，主理人 Timo 与教务组将在 24 小时内与您联络并安排排期。
                    </p>
                </div>

                <!-- 交互申请表单 -->
                <form id="admission-form" onsubmit="return handleAdmissionSubmit(event)" class="space-y-5 pt-8">
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
                        <div>
                            <label class="block text-xs font-bold text-neutral-800 mb-1.5">
                                学员 / 申请人姓名 <span class="text-red-600">*</span>
                            </label>
                            <input
                                type="text"
                                id="admission-name"
                                required
                                placeholder="例如：张同舟 / 小舟同学"
                                class="w-full px-4 py-3 rounded-xl border border-neutral-300 bg-neutral-50/80 text-sm focus:outline-none focus:ring-2 focus:ring-black text-neutral-900"
                            >
                        </div>
                        <div>
                            <label class="block text-xs font-bold text-neutral-800 mb-1.5">
                                联系电话 / 微信号 <span class="text-red-600">*</span>
                            </label>
                            <input
                                type="tel"
                                id="admission-phone"
                                required
                                placeholder="用于接收主理人预约确认"
                                class="w-full px-4 py-3 rounded-xl border border-neutral-300 bg-neutral-50/80 text-sm focus:outline-none focus:ring-2 focus:ring-black text-neutral-900"
                            >
                        </div>
                    </div>

                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
                        <div>
                            <label class="block text-xs font-bold text-neutral-800 mb-1.5">
                                学员身份与年龄阶段 <span class="text-red-600">*</span>
                            </label>
                            <select
                                id="admission-age"
                                class="w-full px-4 py-3 rounded-xl border border-neutral-300 bg-neutral-50/80 text-sm focus:outline-none focus:ring-2 focus:ring-black text-neutral-900"
                            >
                                <option>3–7 岁 少儿音乐通识与亲子互动</option>
                                <option>8–16 岁 青少年乐手与爵士大乐队</option>
                                <option selected>成人流行 / 爵士爱好者与乐队合奏</option>
                                <option>作品积累与方向规划（教学方法参考伯克利）</option>
                                <option>家庭多成员共同研习 (全家参与)</option>
                            </select>
                        </div>
                        <div>
                            <label class="block text-xs font-bold text-neutral-800 mb-1.5">
                                意向申请项目 / 乐器方向 <span class="text-red-600">*</span>
                            </label>
                            <select
                                id="admission-program"
                                class="w-full px-4 py-3 rounded-xl border border-neutral-300 bg-neutral-50/80 text-sm focus:outline-none focus:ring-2 focus:ring-black text-neutral-900"
                            >
                                <option selected>MOMO 2026 Plus 家庭会员（欢迎来访或咨询）</option>
                                <option>Momo 冬季共鸣音乐营 (寒假 · 5天4晚)</option>
                                <option>Momo 夏季即兴音乐营会 (暑期 · 7天6晚)</option>
                                <option>Momo 国际爵士音乐夏令营（欢迎来预约了解）</option>
                                <option>电吉他 / 贝斯 / 现代打击乐 1对1 课程</option>
                                <option>流行声乐与乐队主唱 / 萨克斯管乐 1对1</option>
                                <option>P&R Studio 录音工程与音乐制作专修</option>
                            </select>
                        </div>
                    </div>

                    <div>
                        <label class="block text-xs font-bold text-neutral-800 mb-2">
                            意向到访空间 (严格全预约制) <span class="text-red-600">*</span>
                        </label>
                        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs">
                            <label class="p-3.5 rounded-xl border border-neutral-200 bg-neutral-50 flex items-center gap-2.5 cursor-pointer hover:border-black transition-colors">
                                <input type="radio" name="admission_space" value="桐梓林花园私密声场" checked class="text-black">
                                <span class="font-bold">桐梓林花园私密声场</span>
                            </label>
                            <label class="p-3.5 rounded-xl border border-neutral-200 bg-neutral-50 flex items-center gap-2.5 cursor-pointer hover:border-black transition-colors">
                                <input type="radio" name="admission_space" value="麓湖湖畔水岸声场" class="text-black">
                                <span class="font-bold">麓湖湖畔水岸声场</span>
                            </label>
                            <label class="p-3.5 rounded-xl border border-neutral-200 bg-neutral-50 flex items-center gap-2.5 cursor-pointer hover:border-black transition-colors">
                                <input type="radio" name="admission_space" value="线上远程评估" class="text-black">
                                <span class="font-bold">线上远程评估与咨询</span>
                            </label>
                        </div>
                    </div>

                    <div>
                        <label class="block text-xs font-bold text-neutral-800 mb-1.5">
                            现有音乐基础与学习期待 (选填)
                        </label>
                        <textarea
                            id="admission-notes"
                            rows="2"
                            placeholder="例如：有2年吉他自学基础，想加入乐队玩即兴；或者零基础，想给孩子最好的节奏启蒙..."
                            class="w-full px-4 py-2.5 rounded-xl border border-neutral-300 bg-neutral-50/80 text-sm focus:outline-none focus:ring-2 focus:ring-black text-neutral-900"
                        ></textarea>
                    </div>

                    <div class="pt-2">
                        <button
                            type="submit"
                            class="w-full py-4 rounded-xl bg-black hover:bg-neutral-800 text-white font-black text-sm transition-all shadow-xl shadow-black/20 flex items-center justify-center gap-2 cursor-pointer"
                        >
                            <span>递接入会意向申请 · 预约专业评估</span>
                            <span>&rarr;</span>
                        </button>
                    </div>
                    <p class="text-[11px] text-center text-neutral-500 font-mono-code">
                        ✦ 递交后主理人团队将在 24 小时内致电或微信联系确认排期
                    </p>
                </form>

                <!-- 提交成功后展示的卡片 (默认隐藏) -->
                <div id="admission-success-card" class="hidden text-center py-10 space-y-6">
                    <div class="w-16 h-16 rounded-full bg-emerald-100 text-emerald-600 text-3xl font-black flex items-center justify-center mx-auto shadow-inner">
                        ✓
                    </div>
                    <div class="space-y-2">
                        <h4 class="text-2xl font-black text-black">入会意向已成功递交！</h4>
                        <p id="admission-success-summary" class="text-xs text-neutral-600 font-mono-code"></p>
                        <p class="text-xs text-neutral-500 max-w-md mx-auto leading-relaxed">
                            感谢您对真实音乐生活的向往。为确保排期时效，欢迎立即添加主理人 Timo 微信（MO 酱~），直接沟通您的到访排期与评估细节。
                        </p>
                    </div>
                    <!-- 二维码立牌 -->
                    <div class="inline-block p-4 bg-neutral-50 rounded-2xl border border-neutral-200 shadow-md">
                        <img src="./assets/images/contact/timo_wechat_qr.png" alt="Timo 微信" class="w-36 h-36 mx-auto object-contain rounded-lg">
                        <div class="mt-2 text-xs font-bold text-black">Timo 创始人微信：tixinzhang</div>
                        <div class="text-[10px] text-neutral-500">扫码或长按识别</div>
                    </div>
                </div>
            </div>
        </section>
'''

# Assemble the whole middle sequence
new_middle_sequence = "\n\n".join([
    section_02_membership,
    section_03_camps,
    style_deck_block,
    section_05_faculty,
    section_06_admission
])

# Replace in compile_code
compile_code = compile_code[:pos_sec02] + new_middle_sequence + "\n\n        " + compile_code[pos_bento:]

# Inject handleAdmissionSubmit into the extra scripts
admission_script = '''
    // MI Admission 表单提交处理
    function handleAdmissionSubmit(e) {
        e.preventDefault();
        const form = document.getElementById('admission-form');
        const successCard = document.getElementById('admission-success-card');
        const name = (document.getElementById('admission-name') || {}).value || '申请人';
        const phone = (document.getElementById('admission-phone') || {}).value || '';
        const program = (document.getElementById('admission-program') || {}).value || 'MOMO 会员/营会';
        
        if (form && successCard) {
            form.classList.add('hidden');
            successCard.classList.remove('hidden');
            const summary = document.getElementById('admission-success-summary');
            if (summary) {
                summary.textContent = `申请人：${name} (${phone}) · 意向项目：${program}`;
            }
        }
        return false;
    }
'''

pos_extra_js = compile_code.find('extra_js = """')
if pos_extra_js != -1:
    compile_code = compile_code[:pos_extra_js + len('extra_js = """')] + admission_script + compile_code[pos_extra_js + len('extra_js = """'):]

with open(COMPILE_SCRIPT, "w", encoding="utf-8") as f:
    f.write(compile_code)

print("compile_complete_website.py successfully updated!")
