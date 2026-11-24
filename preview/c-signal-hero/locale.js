/* Preview language switch. Strings are the reviewed copy, written as text. */
(() => {
  const KEY = 'momo-preview-locale';
  const messages = {
    'zh-CN': {
      'document.title': '让音乐自然长进每个家庭｜成都Momo约书亚音乐工作坊',
      skipLink: '跳到正文',
      brand: '成都Momo约书亚音乐工作坊',
      'nav.ariaLabel': '主导航',
      'nav.play': '一起玩',
      'nav.about': '关于我们',
      'hero.kicker': 'MUSIC · FAMILY · PLAY',
      'hero.title': '让音乐自然\n长进每个家庭',
      'hero.subtitle': '流行与爵士的\n家庭音乐俱乐部 ·\n孩子和大人一起玩',
      'cta.explore': '一起探索',
      'cta.growth': '看看音乐成长线',
      'stage.ariaLabel': '和音乐伙伴打个招呼',
      'mascot.note.ariaLabel': '和音符仔打个招呼',
      'mascot.drum.ariaLabel': '和小军鼓打个招呼',
      'mascot.guitar.ariaLabel': '和吉他仔打个招呼',
      'mascot.mic.ariaLabel': '和话筒仔打个招呼',
      'mascot.amp.ariaLabel': '和音箱仔打个招呼',
      'mascot.pick.ariaLabel': '和拨片仔打个招呼',
      'preview.kicker': 'THIS SCREEN ONLY',
      'preview.title': '当前仅首屏演示',
      'preview.body': '这次页面只演示首页首屏。关于我们、音乐成长线还没有放进来。',
      'language.label': '语言切换',
      'language.zhLabel': '中文',
      'language.enLabel': 'EN',
      'language.switchToChinese': '切换为中文',
      'language.switchToEnglish': '切换为英文',
    },
    en: {
      'document.title': 'Let music grow in every home | Momo · Chengdu',
      skipLink: 'Skip to main content',
      brand: 'Momo · Chengdu',
      'nav.ariaLabel': 'Main navigation',
      'nav.play': 'Play together',
      'nav.about': 'About us',
      'hero.kicker': 'MUSIC · FAMILY · PLAY',
      'hero.title': 'Let music grow in every home',
      'hero.subtitle': 'A pop & jazz family music club · Kids and grown-ups play together.',
      'cta.explore': 'Explore together',
      'cta.growth': 'Explore the music journey',
      'stage.ariaLabel': 'Meet our music friends',
      'mascot.note.ariaLabel': 'Say hello to the music note',
      'mascot.drum.ariaLabel': 'Say hello to the snare drum',
      'mascot.guitar.ariaLabel': 'Say hello to the guitar',
      'mascot.mic.ariaLabel': 'Say hello to the microphone',
      'mascot.amp.ariaLabel': 'Say hello to the amplifier',
      'mascot.pick.ariaLabel': 'Say hello to the guitar pick',
      'preview.kicker': 'THIS SCREEN ONLY',
      'preview.title': 'Homepage intro preview',
      'preview.body': 'This preview shows only the top of the homepage. About us and the music journey are not included yet.',
      'language.label': 'Language',
      'language.zhLabel': '中文',
      'language.enLabel': 'EN',
      'language.switchToChinese': 'Switch to Chinese',
      'language.switchToEnglish': 'Switch to English',
    },
  };

  function readStored() {
    try {
      const value = localStorage.getItem(KEY);
      return value === 'en' || value === 'zh-CN' ? value : null;
    } catch (error) {
      return null;
    }
  }

  function writeStored(locale) {
    try {
      localStorage.setItem(KEY, locale);
    } catch (error) {
      /* The current page still switches when storage is unavailable. */
    }
  }

  function text(locale, key) {
    return messages[locale][key];
  }

  function setLabel(el, value) {
    if (!el) return;
    const arrow = el.querySelector('[aria-hidden="true"]');
    if (!arrow) {
      el.textContent = value;
      return;
    }
    arrow.remove();
    el.textContent = value;
    el.append(' ', arrow);
  }

  function fillTitle(locale) {
    const h1 = document.getElementById('home-title');
    h1.replaceChildren();
    if (locale === 'en') {
      h1.append(text(locale, 'hero.title'));
      return;
    }
    const [first, second] = text(locale, 'hero.title').split('\n');
    h1.append(first, document.createElement('br'), second);
  }

  function fillSubtitle(locale) {
    const sub = document.querySelector('.hero-copy .sub');
    sub.replaceChildren();
    if (locale === 'en') {
      sub.append(text(locale, 'hero.subtitle'));
      return;
    }
    const [lead, club, kids] = text(locale, 'hero.subtitle').split('\n');
    const narrow = document.createElement('br');
    narrow.className = 'sub-break-xs';
    const wide = document.createElement('br');
    wide.className = 'sub-break';
    sub.append(lead, narrow, club, wide, kids);
  }

  function apply(locale) {
    const pack = messages[locale] ? locale : 'zh-CN';
    document.documentElement.lang = pack === 'en' ? 'en' : 'zh-CN';
    document.title = text(pack, 'document.title');
    setLabel(document.querySelector('.skip'), text(pack, 'skipLink'));
    setLabel(document.querySelector('.wordmark'), text(pack, 'brand'));
    const nav = document.querySelector('.header nav');
    if (nav) {
      nav.setAttribute('aria-label', text(pack, 'nav.ariaLabel'));
      const links = [...nav.querySelectorAll(':scope > a')];
      setLabel(links[0], text(pack, 'nav.play'));
      setLabel(links[1], text(pack, 'nav.about'));
    }
    setLabel(document.querySelector('.hero-copy > .label'), text(pack, 'hero.kicker'));
    fillTitle(pack);
    fillSubtitle(pack);
    const actions = [...document.querySelectorAll('.hero-copy .actions > a')];
    setLabel(actions[0], text(pack, 'cta.explore'));
    setLabel(actions[1], text(pack, 'cta.growth'));
    const stage = document.querySelector('.mascot-stage');
    if (stage) stage.setAttribute('aria-label', text(pack, 'stage.ariaLabel'));
    for (const role of ['note', 'drum', 'guitar', 'mic', 'amp', 'pick']) {
      const button = document.querySelector(`.mascot-stage > button[data-role="${role}"]`);
      if (button) button.setAttribute('aria-label', text(pack, `mascot.${role}.ariaLabel`));
    }
    document.querySelectorAll('.mascot img').forEach((img) => { img.alt = ''; });
    setLabel(document.querySelector('#preview-boundary .label'), text(pack, 'preview.kicker'));
    setLabel(document.getElementById('boundary-title'), text(pack, 'preview.title'));
    setLabel(document.querySelector('#preview-boundary p:not(.label)'), text(pack, 'preview.body'));
    const group = document.querySelector('.lang-switch');
    if (group) group.setAttribute('aria-label', text(pack, 'language.label'));
    const zh = document.querySelector('.lang-switch [data-locale="zh-CN"]');
    const en = document.querySelector('.lang-switch [data-locale="en"]');
    if (zh && en) {
      // Keep the short labels as authored. Rewriting the active button mid-click
      // was tearing down the document in headless Chrome.
      zh.setAttribute('aria-label', text(pack, 'language.switchToChinese'));
      en.setAttribute('aria-label', text(pack, 'language.switchToEnglish'));
      zh.setAttribute('aria-pressed', pack === 'zh-CN' ? 'true' : 'false');
      en.setAttribute('aria-pressed', pack === 'en' ? 'true' : 'false');
    }
    document.documentElement.dataset.currentLocale = pack;
  }

  const saved = readStored();
  apply(saved === 'en' ? 'en' : 'zh-CN');
  document.querySelectorAll('.lang-switch [data-locale]').forEach((button) => {
    button.addEventListener('click', () => {
      const next = button.dataset.locale === 'en' ? 'en' : 'zh-CN';
      apply(next);
      writeStored(next);
    });
  });
})();
