# -*- coding: utf-8 -*-
"""
fix_style_deck_audio.py
Fixes null-pointer crashes in updateStyleDeckUI() and nativeAudio event listeners
caused by compact Style Deck HTML on index.html, and improves card centering/sliding.
"""

import os

WEBSITE_DIR = "/Users/timomo/Documents/Momo音乐工作坊总文件/MomoMusicWebsite"
COMPILE_SCRIPT = os.path.join(WEBSITE_DIR, "compile_complete_website.py")

with open(COMPILE_SCRIPT, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Replace the nativeAudio listeners and Style Deck JS block safely
old_start_marker = "// 音频播放状态监听"
old_end_marker = "// 4. FAQ 手风琴展开与收起"

pos_start = code.find(old_start_marker)
pos_end = code.find(old_end_marker)

if pos_start == -1 or pos_end == -1:
    raise Exception(f"Markers not found: start={pos_start}, end={pos_end}")

new_audio_and_deck_js = '''// 音频播放状态监听 (全量空值保护，兼容首页精简卡片机与课程专页)
        if (nativeAudio) {
            nativeAudio.addEventListener('play', () => {
                if (waveBox) waveBox.classList.add('sound-wave-active');
                if (btnPlayText) btnPlayText.textContent = "暂停音轨";
                if (playIconSvg) playIconSvg.innerHTML = '<path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"/>';
                if (audioStatusTag) {
                    audioStatusTag.textContent = "🔊 正在真实播放【" + styleData[currentStyleIndex].name + "】原声音频";
                    audioStatusTag.className = "text-momo-mint font-bold truncate pr-2";
                }
                const activeCard = document.querySelectorAll('.style-card')[currentStyleIndex];
                if (activeCard) {
                    const vid = activeCard.querySelector('video');
                    if (vid) vid.play().catch(() => {});
                }
            });

            nativeAudio.addEventListener('pause', () => {
                if (waveBox) waveBox.classList.remove('sound-wave-active');
                if (btnPlayText) btnPlayText.textContent = "试听音轨";
                if (playIconSvg) playIconSvg.innerHTML = '<path d="M8 5v14l11-7z"/>';
                if (audioStatusTag) {
                    audioStatusTag.textContent = "● 已暂停 · 点击即可随时重播";
                    audioStatusTag.className = "text-neutral-400 truncate pr-2";
                }
                document.querySelectorAll('.style-card video').forEach(v => v.pause());
            });

            nativeAudio.addEventListener('ended', () => {
                if (waveBox) waveBox.classList.remove('sound-wave-active');
                if (btnPlayText) btnPlayText.textContent = "再次试听";
                if (playIconSvg) playIconSvg.innerHTML = '<path d="M8 5v14l11-7z"/>';
                if (audioStatusTag) {
                    audioStatusTag.textContent = "● 试听已完毕 · 可左右切换探索下一风格";
                    audioStatusTag.className = "text-neutral-400 truncate pr-2";
                }
                if (audioSeekBar) audioSeekBar.value = 0;
                if (audioCurrentTime) audioCurrentTime.textContent = '0:00';
                document.querySelectorAll('.style-card video').forEach(v => v.pause());
            });

            nativeAudio.addEventListener('error', () => {
                if (waveBox) waveBox.classList.remove('sound-wave-active');
                if (audioStatusTag) {
                    audioStatusTag.textContent = "● 音轨就绪 · 点击即可播放";
                    audioStatusTag.className = "text-neutral-400 truncate pr-2";
                }
            });

            nativeAudio.addEventListener('timeupdate', () => {
                if (!nativeAudio.duration) return;
                const current = nativeAudio.currentTime;
                const duration = nativeAudio.duration;
                if (audioCurrentTime) audioCurrentTime.textContent = formatAudioTime(current);
                if (audioSeekBar && !audioSeekBar.dataset.dragging) {
                    audioSeekBar.value = (current / duration) * 100;
                }
            });

            nativeAudio.addEventListener('loadedmetadata', () => {
                if (audioDurationTime && nativeAudio.duration) {
                    audioDurationTime.textContent = formatAudioTime(nativeAudio.duration);
                }
            });
        }

        if (audioSeekBar && nativeAudio) {
            audioSeekBar.addEventListener('input', () => {
                audioSeekBar.dataset.dragging = 'true';
                if (nativeAudio.duration) {
                    const targetSec = (audioSeekBar.value / 100) * nativeAudio.duration;
                    if (audioCurrentTime) audioCurrentTime.textContent = formatAudioTime(targetSec);
                }
            });

            audioSeekBar.addEventListener('change', () => {
                if (nativeAudio.duration) {
                    nativeAudio.currentTime = (audioSeekBar.value / 100) * nativeAudio.duration;
                }
                delete audioSeekBar.dataset.dragging;
            });
        }

        function toggleAudioPlayback() {
            if (!nativeAudio) return;
            if (nativeAudio.paused) {
                const playPromise = nativeAudio.play();
                if (playPromise !== undefined) {
                    playPromise.catch(error => {
                        console.log("Audio play intercepted:", error);
                    });
                }
            } else {
                nativeAudio.pause();
            }
        }

        // 风格药丸标签高亮同步
        function updateStylePillsUI(activeIdx) {
            const pills = document.querySelectorAll('.style-tab-pill');
            pills.forEach((p, idx) => {
                if (idx === activeIdx) {
                    p.className = 'style-tab-pill active px-3.5 py-1.5 rounded-full text-xs font-mono-code font-bold transition-all bg-white text-black shadow shrink-0';
                } else {
                    p.className = 'style-tab-pill px-3.5 py-1.5 rounded-full text-xs font-mono-code font-bold transition-all bg-neutral-900 text-neutral-300 hover:text-white border border-neutral-800 shrink-0';
                }
            });
        }

        // 切换卡片并同步更新 MP4 原生音频源与专辑左右滑动
        function updateStyleDeckUI(autoPlay = false) {
            const data = styleData[currentStyleIndex];
            const elTitle = document.getElementById('card-title');
            const elPeriod = document.getElementById('card-period');
            const elRegion = document.getElementById('card-region');
            const elDesc = document.getElementById('card-desc');
            const elArtists = document.getElementById('card-artists');
            const elInstruments = document.getElementById('card-instruments');
            const elIndicator = document.getElementById('deck-indicator');
            const elAudioNote = document.getElementById('audio-track-note');

            if (elTitle) elTitle.innerHTML = data.title;
            if (elPeriod) elPeriod.textContent = data.period;
            if (elRegion) elRegion.textContent = data.region;
            if (elDesc) elDesc.textContent = data.desc;
            if (elArtists) elArtists.textContent = data.artists;
            if (elInstruments) elInstruments.textContent = data.instruments;
            if (elIndicator) elIndicator.textContent = '0' + (currentStyleIndex + 1) + ' / 06';
            if (elAudioNote) elAudioNote.textContent = data.audioTitle;

            updateStylePillsUI(currentStyleIndex);

            // 兼容课程专页的映射面板
            const momoPlayEl = document.getElementById('card-momo-play');
            const momoProductEl = document.getElementById('card-momo-product');
            const actionBtn = document.getElementById('card-action-btn');
            if (momoPlayEl && data.momoPlay) momoPlayEl.textContent = data.momoPlay;
            if (momoProductEl && data.momoProduct) momoProductEl.textContent = data.momoProduct;
            if (actionBtn && data.momoIntent) {
                actionBtn.setAttribute('onclick', `openBookingModal('${data.momoIntent}')`);
            }

            // 切换音频 URL 并重载播放器
            if (nativeAudio) {
                const wasPlaying = !nativeAudio.paused;
                nativeAudio.pause();
                nativeAudio.src = data.audioUrl;
                if (nativeSource) nativeSource.src = data.audioUrl;
                nativeAudio.load();
                if (audioSeekBar) audioSeekBar.value = 0;
                if (audioCurrentTime) audioCurrentTime.textContent = '0:00';
                if (audioDurationTime) audioDurationTime.textContent = '0:00';

                if (autoPlay || wasPlaying) {
                    nativeAudio.play().catch(e => console.log("Audio play deferred:", e));
                } else {
                    if (waveBox) waveBox.classList.remove('sound-wave-active');
                    if (btnPlayText) btnPlayText.textContent = "试听音轨";
                    if (playIconSvg) playIconSvg.innerHTML = '<path d="M8 5v14l11-7z"/>';
                    if (audioStatusTag) {
                        audioStatusTag.textContent = "● 点击即可试听，支持进度条拖动与后台播放";
                        audioStatusTag.className = "text-neutral-400";
                    }
                }
            }

            // 高亮当前专辑卡片 & 柔化非当前卡片
            const cards = document.querySelectorAll('.style-card');
            cards.forEach(function(card, idx) {
                if (idx === currentStyleIndex) {
                    card.classList.add('active-card', 'border-cyan-400', 'opacity-100', 'shadow-lg');
                    card.classList.remove('opacity-60', 'border-neutral-800');
                } else {
                    card.classList.remove('active-card', 'border-cyan-400', 'opacity-100', 'shadow-lg');
                    card.classList.add('opacity-60', 'border-neutral-800');
                }
            });

            // 平滑居中滑动当前专辑
            const track = document.getElementById('cards-track');
            const activeCardEl = cards[currentStyleIndex];
            if (track && activeCardEl && track.parentElement) {
                const containerWidth = track.parentElement.clientWidth;
                const maxScroll = Math.max(0, track.scrollWidth - containerWidth);
                const targetX = Math.max(0, Math.min(maxScroll, activeCardEl.offsetLeft - (containerWidth - activeCardEl.offsetWidth) / 2));
                track.style.transform = 'translateX(-' + targetX + 'px)';
            }
        }

        function nextStyleCard() {
            currentStyleIndex = (currentStyleIndex + 1) % styleData.length;
            updateStyleDeckUI(false);
        }

        function prevStyleCard() {
            currentStyleIndex = (currentStyleIndex - 1 + styleData.length) % styleData.length;
            updateStyleDeckUI(false);
        }

        function selectStyleCard(idx) {
            currentStyleIndex = idx;
            updateStyleDeckUI(true);
        }

        '''

code = code[:pos_start] + new_audio_and_deck_js + code[pos_end:]

# 2. Also ensure style-tab-pill buttons have shrink-0 on initial render
code = code.replace(
    'class="style-tab-pill active px-3.5 py-1.5 rounded-full text-xs font-mono-code font-bold transition-all bg-white text-black shadow"',
    'class="style-tab-pill active px-3.5 py-1.5 rounded-full text-xs font-mono-code font-bold transition-all bg-white text-black shadow shrink-0"'
)
code = code.replace(
    'class="style-tab-pill px-3.5 py-1.5 rounded-full text-xs font-mono-code font-bold transition-all bg-neutral-900 text-neutral-300 hover:text-white border border-neutral-800"',
    'class="style-tab-pill px-3.5 py-1.5 rounded-full text-xs font-mono-code font-bold transition-all bg-neutral-900 text-neutral-300 hover:text-white border border-neutral-800 shrink-0"'
)

with open(COMPILE_SCRIPT, "w", encoding="utf-8") as f:
    f.write(code)

print("Successfully patched compile_complete_website.py!")
