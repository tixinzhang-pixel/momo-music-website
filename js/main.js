/**
 * MOMO FAMILY MUSIC STUDIO - MAIN INTERACTIVE ENGINE
 * Features:
 * - Smart Glassmorphic Sticky Header
 * - Style Deck Carousel & Web Audio Engine with Pulse Waveform
 * - Ambient Sonic Generator (Web Audio API)
 * - FAQ Smooth Accordion
 * - Dynamic Booking Modal with Auto-Preset Category
 * - Lightweight Non-blocking Toast Feedback System
 */

document.addEventListener('DOMContentLoaded', () => {
  initHeader();
  initStyleDeck();
  initAmbientSonic();
  initFAQ();
  initBookingModal();
});

/* ==========================================================================
   1. 顶部导航栏滚动监听与移动端抽屉菜单
   ========================================================================== */
function initHeader() {
  const navbar = document.getElementById('navbar');
  const mobileToggle = document.getElementById('mobileMenuToggle');
  const navLinks = document.getElementById('navLinks');

  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  }, { passive: true });

  if (mobileToggle && navLinks) {
    mobileToggle.addEventListener('click', () => {
      navLinks.classList.toggle('mobile-open');
    });

    // 点击链接后自动收起菜单
    navLinks.querySelectorAll('.nav-item').forEach(link => {
      link.addEventListener('click', () => {
        navLinks.classList.remove('mobile-open');
      });
    });
  }
}

/* ==========================================================================
   2. 风格长河抽卡机与双轨音频引擎 (HTML5 Audio + Web Audio API 降级保证)
   ========================================================================== */
function initStyleDeck() {
  const cards = Array.from(document.querySelectorAll('.style-card'));
  const carousel = document.getElementById('deckCarousel');
  const prevBtn = document.getElementById('prevCardBtn');
  const nextBtn = document.getElementById('nextCardBtn');
  const counter = document.getElementById('deckCounter');
  const stopBtn = document.getElementById('masterAudioStopBtn');
  const visualizer = document.getElementById('equalizerVisualizer');
  const statusIndicator = document.querySelector('.status-dot');
  const playingTitle = document.getElementById('currentPlayingTitle');
  const playingMeta = document.getElementById('currentPlayingMeta');

  if (!cards.length) return;

  let currentIndex = 0;
  let currentAudio = null;
  let webAudioCtx = null;
  let synthOscillators = [];
  let visualizerTimer = null;

  function updateActiveCard(index) {
    currentIndex = (index + cards.length) % cards.length;
    cards.forEach((card, idx) => {
      if (idx === currentIndex) {
        card.classList.add('active');
        card.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
      } else {
        card.classList.remove('active');
      }
    });

    if (counter) {
      counter.textContent = `0${currentIndex + 1} / 0${cards.length}`;
    }
  }

  if (prevBtn) {
    prevBtn.addEventListener('click', () => {
      updateActiveCard(currentIndex - 1);
    });
  }

  if (nextBtn) {
    nextBtn.addEventListener('click', () => {
      updateActiveCard(currentIndex + 1);
    });
  }

  // 风格音频播放引擎
  function stopCurrentAudio() {
    if (currentAudio) {
      currentAudio.pause();
      currentAudio.currentTime = 0;
      currentAudio = null;
    }

    // 停止 Web Audio 模拟合成音
    synthOscillators.forEach(osc => {
      try { osc.stop(); osc.disconnect(); } catch (e) {}
    });
    synthOscillators = [];

    // 重置所有卡片播放按钮状态
    document.querySelectorAll('.card-play-trigger').forEach(btn => {
      btn.querySelector('.play-state-icon').innerHTML = '&#9658;';
      btn.querySelector('.play-state-text').textContent = '试听风格音轨 & 启动声波';
    });

    if (visualizer) visualizer.classList.remove('animating');
    if (statusIndicator) statusIndicator.classList.remove('playing');
    if (playingTitle) playingTitle.textContent = 'STANDBY / 点击卡片试听';
    if (playingMeta) playingMeta.textContent = 'HTML5 Web Audio 实时渲染引擎已就绪';

    if (visualizerTimer) {
      clearInterval(visualizerTimer);
      visualizerTimer = null;
    }

    // 复位均衡条高度
    if (visualizer) {
      visualizer.querySelectorAll('.bar').forEach(b => b.style.height = '4px');
    }
  }

  function startVisualizerAnimation() {
    if (visualizer) {
      visualizer.classList.add('animating');
      const bars = visualizer.querySelectorAll('.bar');
      if (visualizerTimer) clearInterval(visualizerTimer);

      visualizerTimer = setInterval(() => {
        bars.forEach(bar => {
          const randH = Math.floor(Math.random() * 32) + 6;
          bar.style.height = `${randH}px`;
        });
      }, 100);
    }
  }

  // Web Audio 纯代码合成和声律动（防止本地文件协议或特定浏览器策略阻断）
  function playSyntheticStyleChord(bpm, rootFreq = 220) {
    try {
      const AudioContext = window.AudioContext || window.webkitAudioContext;
      if (!AudioContext) return;
      if (!webAudioCtx) webAudioCtx = new AudioContext();
      if (webAudioCtx.state === 'suspended') webAudioCtx.resume();

      const chords = [rootFreq, rootFreq * 1.25, rootFreq * 1.5, rootFreq * 1.875];
      const masterGain = webAudioCtx.createGain();
      masterGain.gain.setValueAtTime(0.12, webAudioCtx.currentTime);
      masterGain.connect(webAudioCtx.destination);

      chords.forEach((freq, i) => {
        const osc = webAudioCtx.createOscillator();
        const gain = webAudioCtx.createGain();

        osc.type = i === 0 ? 'triangle' : 'sine';
        osc.frequency.setValueAtTime(freq, webAudioCtx.currentTime);

        // 柔和琶音脉冲
        gain.gain.setValueAtTime(0, webAudioCtx.currentTime);
        gain.gain.linearRampToValueAtTime(0.2, webAudioCtx.currentTime + 0.1);
        gain.gain.exponentialRampToValueAtTime(0.01, webAudioCtx.currentTime + 3.0);

        osc.connect(gain);
        gain.connect(masterGain);
        osc.start();
        osc.stop(webAudioCtx.currentTime + 3.2);

        synthOscillators.push(osc);
      });
    } catch (e) {
      console.warn('Web Audio synthesis fallback:', e);
    }
  }

  function playCardAudio(card) {
    const isAlreadyPlaying = card.classList.contains('playing-now');
    stopCurrentAudio();

    if (isAlreadyPlaying) {
      card.classList.remove('playing-now');
      return;
    }

    card.classList.add('playing-now');
    const audioSrc = card.dataset.audio;
    const styleName = card.querySelector('.style-name').textContent;
    const bpm = card.dataset.bpm || '120';
    const key = card.dataset.key || 'C';
    const era = card.dataset.era || '';

    // 更新界面信息
    if (statusIndicator) statusIndicator.classList.add('playing');
    if (playingTitle) playingTitle.textContent = `NOW PLAYING: ${styleName}`;
    if (playingMeta) playingMeta.textContent = `BPM ${bpm} · KEY: ${key} · [${era}]`;

    const playBtn = card.querySelector('.card-play-trigger');
    if (playBtn) {
      playBtn.querySelector('.play-state-icon').innerHTML = '&#9646;&#9646;';
      playBtn.querySelector('.play-state-text').textContent = '正在播放 · 点击停止';
    }

    startVisualizerAnimation();

    // 优先加载本地真实音频文件
    currentAudio = new Audio(audioSrc);
    currentAudio.play().then(() => {
      currentAudio.onended = () => {
        stopCurrentAudio();
      };
    }).catch(err => {
      // 本地无源或策略阻止时，自动切换至 Web Audio 实时声学合成
      console.log('Audio file play diverted to Web Audio synthesizer:', err.message);
      const rootNote = 180 + (parseInt(card.dataset.index) * 25);
      playSyntheticStyleChord(parseInt(bpm), rootNote);

      setTimeout(() => {
        if (card.classList.contains('playing-now')) {
          stopCurrentAudio();
        }
      }, 3500);
    });
  }

  cards.forEach((card, index) => {
    card.addEventListener('click', (e) => {
      updateActiveCard(index);
      // 如果点击的是卡片本身（非专门点试听按钮），触发聚焦并试听
      if (!e.target.closest('.card-play-trigger')) {
        playCardAudio(card);
      }
    });

    const triggerBtn = card.querySelector('.card-play-trigger');
    if (triggerBtn) {
      triggerBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        updateActiveCard(index);
        playCardAudio(card);
      });
    }
  });

  if (stopBtn) {
    stopBtn.addEventListener('click', stopCurrentAudio);
  }
}

/* ==========================================================================
   3. 顶部环境背景声波发生器 (Ambient Sonic Generator)
   ========================================================================== */
function initAmbientSonic() {
  const toggleBtn = document.getElementById('headerAudioToggle');
  if (!toggleBtn) return;

  const statusText = toggleBtn.querySelector('.audio-status-text');
  const icon = toggleBtn.querySelector('.audio-wave-icon');
  let isAmbientOn = false;
  let ambientAudioCtx = null;
  let droneGain = null;
  let droneOscs = [];

  toggleBtn.addEventListener('click', () => {
    isAmbientOn = !isAmbientOn;

    if (isAmbientOn) {
      try {
        const AudioCtx = window.AudioContext || window.webkitAudioContext;
        if (!ambientAudioCtx) ambientAudioCtx = new AudioCtx();
        if (ambientAudioCtx.state === 'suspended') ambientAudioCtx.resume();

        // 温暖的深层模拟合成器环境音脉冲（基于低音提琴空弦基频 55Hz A1 & 110Hz A2）
        droneGain = ambientAudioCtx.createGain();
        droneGain.gain.setValueAtTime(0.04, ambientAudioCtx.currentTime);
        droneGain.connect(ambientAudioCtx.destination);

        const freqs = [55, 110, 164.81, 220];
        droneOscs = freqs.map((f, i) => {
          const osc = ambientAudioCtx.createOscillator();
          osc.type = i % 2 === 0 ? 'triangle' : 'sine';
          osc.frequency.setValueAtTime(f, ambientAudioCtx.currentTime);
          osc.connect(droneGain);
          osc.start();
          return osc;
        });

        icon.classList.add('audio-wave-active');
        statusText.textContent = 'SONIC: ON';
        showToast('环境空间声波已开启 (A432Hz 温暖背景微频)', 'success');
      } catch (e) {
        showToast('浏览器限制自动音频播放，请先与页面交互', 'error');
        isAmbientOn = false;
      }
    } else {
      droneOscs.forEach(o => {
        try { o.stop(); o.disconnect(); } catch (e) {}
      });
      droneOscs = [];
      icon.classList.remove('audio-wave-active');
      statusText.textContent = 'SONIC: OFF';
      showToast('环境空间声波已关闭', 'info');
    }
  });
}

/* ==========================================================================
   4. FAQ 平滑手风琴组件
   ========================================================================== */
function initFAQ() {
  const faqItems = document.querySelectorAll('.faq-item');

  faqItems.forEach(item => {
    const questionBtn = item.querySelector('.faq-question');
    const answer = item.querySelector('.faq-answer');

    if (!questionBtn || !answer) return;

    questionBtn.addEventListener('click', () => {
      const isActive = item.classList.contains('active');

      // 互斥折叠：关闭其他展开项
      faqItems.forEach(other => {
        if (other !== item && other.classList.contains('active')) {
          other.classList.remove('active');
          other.querySelector('.faq-question').setAttribute('aria-expanded', 'false');
          other.querySelector('.faq-answer').style.maxHeight = '0px';
        }
      });

      // 切换当前项
      if (isActive) {
        item.classList.remove('active');
        questionBtn.setAttribute('aria-expanded', 'false');
        answer.style.maxHeight = '0px';
      } else {
        item.classList.add('active');
        questionBtn.setAttribute('aria-expanded', 'true');
        answer.style.maxHeight = `${answer.scrollHeight}px`;
      }
    });
  });
}

/* ==========================================================================
   5. 全功能预约探访弹窗与分类自动预选
   ========================================================================== */
function initBookingModal() {
  const modal = document.getElementById('bookingModal');
  const closeBtn = document.getElementById('modalCloseBtn');
  const bookingForm = document.getElementById('bookingForm');
  const categorySelect = document.getElementById('formCategory');
  const openButtons = document.querySelectorAll('.open-booking-btn');

  if (!modal || !bookingForm) return;

  function openModal(presetCategory = '') {
    modal.classList.add('active');
    modal.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';

    // 自动匹配预设项
    if (presetCategory && categorySelect) {
      let matched = false;
      Array.from(categorySelect.options).forEach(opt => {
        if (opt.value.includes(presetCategory) || presetCategory.includes(opt.value)) {
          categorySelect.value = opt.value;
          matched = true;
        }
      });
      if (!matched && presetCategory.includes('大乐队')) {
        categorySelect.value = '青少年现代爵士大乐队考核';
      } else if (!matched && presetCategory.includes('年费会员')) {
        categorySelect.value = 'Momo 家庭年费会员 Plus';
      }
    }

    const firstInput = bookingForm.querySelector('input');
    if (firstInput) setTimeout(() => firstInput.focus(), 150);
  }

  function closeModal() {
    modal.classList.remove('active');
    modal.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
  }

  openButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const preset = btn.dataset.preset || '';
      openModal(preset);
    });
  });

  if (closeBtn) {
    closeBtn.addEventListener('click', closeModal);
  }

  modal.addEventListener('click', (e) => {
    if (e.target === modal) {
      closeModal();
    }
  });

  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal.classList.contains('active')) {
      closeModal();
    }
  });

  // 表单提交处理
  bookingForm.addEventListener('submit', (e) => {
    e.preventDefault();

    const name = document.getElementById('formName').value.trim();
    const phone = document.getElementById('formPhone').value.trim();
    const category = document.getElementById('formCategory').value;
    const location = document.getElementById('formLocation').value;
    const notes = document.getElementById('formNotes').value.trim();

    if (!name || !phone) {
      showToast('请完整填写您的姓名与联系方式', 'error');
      return;
    }

    // 禁用提交按钮防止重复发送
    const submitBtn = document.getElementById('formSubmitBtn');
    submitBtn.disabled = true;
    submitBtn.innerHTML = '<span>正在安排专属音乐顾问...</span>';

    setTimeout(() => {
      showToast(`预约成功！我们已为 [${name}] 记录 [${category}] 探访需求，音乐管家将通过电话/微信与您建立看护群。`, 'success');

      // 本地存储备份
      try {
        const bookings = JSON.parse(localStorage.getItem('momo_bookings') || '[]');
        bookings.push({ name, phone, category, location, notes, timestamp: new Date().toISOString() });
        localStorage.setItem('momo_bookings', JSON.stringify(bookings));
      } catch (err) {}

      bookingForm.reset();
      submitBtn.disabled = false;
      submitBtn.innerHTML = `
        <span>确认提交 · 开启真实声学生态</span>
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
      `;

      closeModal();
    }, 800);
  });
}

/* ==========================================================================
   6. 轻量优雅 Toast 提示层 (拒绝原生 alert)
   ========================================================================== */
function showToast(message, type = 'info') {
  let hub = document.getElementById('toastHub');
  if (!hub) {
    hub = document.createElement('div');
    hub.id = 'toastHub';
    hub.className = 'toast-hub';
    document.body.appendChild(hub);
  }

  const toast = document.createElement('div');
  toast.className = `toast-message ${type}`;

  const iconSymbol = type === 'success' ? '✦' : (type === 'error' ? '!' : 'ℹ');
  toast.innerHTML = `
    <span style="color: ${type === 'success' ? '#50FA7B' : (type === 'error' ? '#FF5555' : '#00F0FF')}; font-weight: 700; font-family: monospace;">[${iconSymbol}]</span>
    <span>${message}</span>
  `;

  hub.appendChild(toast);

  // 触发显示动画
  requestAnimationFrame(() => {
    toast.classList.add('show');
  });

  // 4 秒后自动淡出销毁
  setTimeout(() => {
    toast.classList.remove('show');
    setTimeout(() => {
      toast.remove();
    }, 400);
  }, 3800);
}
