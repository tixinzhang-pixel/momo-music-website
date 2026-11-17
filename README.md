# Momo Family Music Studio 官方展示网站工程

> **品牌理念**：KIND · TRUTH · PASSION  
> **视觉设计规范**：前卫画报粗野主义（Avant-Garde Editorial Neo-Brutalism）与现代瑞士平面设计（Swiss Modern Graphic Design），参考 The New School (纽约新学院) 极简大版面冲击力排版。

---

## 一、 项目工程结构

本项目采用模块化前端工程架构，拒绝单文件拥挤，完全解耦各层级逻辑与静态资产：

```text
MomoMusicWebsite/
├── index.html               # 生产主骨架入口页面（语义化 HTML5）
├── package.json             # 项目元信息与启动脚本配置
├── build.js                 # 模块化组件校验与装配脚本
├── README.md                # 完整工程文档与技术说明
├── css/
│   └── style.css            # 粗野主义与瑞士排版设计系统、颜色变量、响应式断点
├── js/
│   └── main.js              # 核心交互引擎（毛玻璃导航、抽卡机、Web Audio、FAQ手风琴、预约弹窗）
├── sections/                # 9 大核心业务板块的独立模块化 HTML 组件
│   ├── 01-hero.html         # 首屏海报区与滚动指标
│   ├── 02-philosophy.html   # 去功利化教育生态与生命安全场
│   ├── 03-instruments.html  # 全系专业乐器矩阵（低音、吉他音色、小提琴、键盘）
│   ├── 04-style-deck.html   # 音乐风格长河抽卡机与联动声波均衡器
│   ├── 05-big-band.html     # 青少年现代爵士大乐队企划（林肯中心标准）
│   ├── 06-membership.html   # 家庭音乐年费会员 Plus (真理普惠理念) 与 FAQ 手风琴
│   ├── 07-happenings.html   # 成都月度现场排期（开放麦、合奏研习日、先锋社团）
│   ├── 08-spaces.html       # 桐梓林空间 & 麓湖水岸实验室
│   └── 09-booking-modal.html # 全功能预约探访弹窗与轻量 Toast 提示系统
└── assets/
    ├── images/              # 本地高清插图库（免翻墙同服直出）
    │   ├── double_bass.png   # 原声立式低音提琴 Double Bass 实录特写
    │   ├── pedalboard.jpg    # 专业电吉他效果器踏板矩阵
    │   ├── modern_violin.jpg # 现代小提琴先锋演奏特写
    │   └── keyboard_synth.jpg# 经典红色舞台合成器录音室特写
    └── audio/               # 6 大经典风格本地音轨试听库
        ├── swing_demo.wav    # Swing 大乐队（摇摆乐、跳跃 Walking Bass）
        ├── bebop_demo.wav    # Bebop 先锋爵士（疾风和声与延伸音）
        ├── blues_demo.wav    # 根源 Blues（十二小节与推弦微音程）
        ├── rock_demo.wav     # Classic & Modern Rock（电子管过载与后拍军鼓）
        ├── bossa_demo.wav    # Bossa Nova（桑巴微醺切分与冷峻和声）
        └── funk_demo.wav     # Pop / Funk Groove（16分音符律动 Pocket）
```

---

## 二、 本地快速启动与预览

### 方式 1：使用内置服务（推荐）
当前已启动本地静态服务，直接在浏览器中打开：
* **本地服务地址**：[http://localhost:8080/](http://localhost:8080/)

### 方式 2：使用 NPM 脚本
```bash
npm start
# 或使用现代静态伺服器
npm run serve
```

### 方式 3：直接浏览器打开本地文件
直接在 Chrome 或 Safari 中打开本地文件协议即可，所有素材均已绑定为标准本地相对路径：
`file:///Users/timomo/Documents/MomoMusicWebsite/index.html`

---

## 三、 9 大核心业务板块全景

1. **顶部导航栏 (Global Header)**：
   - 采用 SVG 矢量重构的 Momo 盾牌 Logo（内置 `Kind Truth Passion` 标语与经典 M 字标）。
   - 滚动监听平滑毛玻璃透明度渐变，内置移动端汉堡折叠菜单与**顶部环境声波（Ambient Sonic A432Hz）一键开关**。
2. **首屏海报区 (Hero Section)**：
   - 标语：“FIND YOUR OWN SOUND. / 从锦江河畔到曼哈顿西村”。
   - 纯黑炭黑背景与电光青绿渐变交相辉映，配备双空间胶囊标签与平滑跑马灯（Ticker）。
   - 实时滚动呈现四大硬核指标（100%一线艺术家执教、365天一户一群、12+年度舞台、双物理空间）。
3. **教育生态与生命安全场 (Sanctuary Philosophy)**：
   - **01 广义家庭概念**：单身成人本身即是完整精神家庭。
   - **02 特别感知力温柔安全场 (去功利化)**：拥抱 ADHD、高敏感（HSP）与休学青少年，**坚决不打鸡血、不许诺速成与功利名校**，提供安然躺平与温暖看护。
   - **03 反向资源配置**：破除“启蒙找新手、大师只带艺考”陋习，通识启蒙第一课直面顶尖世界艺术家。
4. **全系专业乐器矩阵 (Comprehensive Matrix)**：
   - 呈现原声立式大贝斯 Double Bass（Pizzicato / Arco）、电贝斯（Funk Slap）、单块效果器捏制、非古典现代提琴、红色舞台合成器、现代流行鼓组、真实乐队主唱与海外名校棚录制作。
5. **音乐风格长河与声波抽卡机 (Style Deck & Audio Engine)**：
   - 涵盖 Swing、Bebop、Blues、Rock、Bossa Nova、Pop/Funk 6 大经典风格卡片。
   - 支持前后平滑滑动聚焦，内置双轨播放引擎（真实本地音轨 + Web Audio 实时声学合成保底），联动跳动声波均衡器（Equalizer Wave Bars）。
6. **Momo 青少年现代爵士大乐队企划 (Youth Big Band)**：
   - 对标纽约林肯中心爵士乐团标准，全编制铜管与节奏组深度合练，配备原创总谱与城市剧场演出季。
7. **Momo 家庭音乐年费会员 Plus (Membership & Philosophy)**：
   - 定价 欢迎来访或咨询），真理普惠无歧视。
   - 涵盖 12 次 1对1 专属定制指导、3 次家庭成长深度诊断、**365天一户一群多师协同智库**、4 次全球审美实践、**原创作品录制发表计划（仅需1次课时消耗，导师现场乐队伴奏并实录，杜绝高额棚费）**、7天冷静期全额退款保障与 FAQ 手风琴面板。
8. **成都月度现场排期 (Monthly Happenings)**：
   - 每月第四周六：`Free Frequency` 自由声波社群开放麦。
   - 每月倒数第三周六（下午）：`The Groove Session` 会员乐队合奏研习日。
   - 每月倒数第三周六（日场）：`Next-Gen Sonic Club` 青少年先锋社团选拔。
9. **全功能预约弹窗与轻量 Toast 提示系统**：
   - 点击任意板块预约按钮自动呼起弹窗，并自动根据按钮来源预选意向科目（如大乐队、年费会员或指定乐器）。
   - 禁用原生浏览器 alert，采用沉浸式浮动 Toast 弹窗反馈，并自动将数据持久化备份至浏览器 localStorage。
10. **实体双空间落地 (Dual Spaces)**：
    - **桐梓林空间**：成都市武侯区银都花园14栋2单元101（林荫国际社区沙龙与声学黑胶大排练场）。
    - **麓湖空间**：成都市天府新区麓坊中心A座1栋811（麓湖水岸先锋实验室与现代流行青年矩阵）。

---

## 四、 国内用户访问保障
所有图片（`.png`、`.jpg`）与音频文件（`.wav`）均采用与网站源码同服部署的本地相对路径引用（`./assets/...`），**国内访问不依赖任何外部海外云盘或翻墙网络**，秒开加载，不裂图、不断流。
