/**
 * Browser checks for the isolated C-signal hero preview.
 * Usage: node check.mjs [screenshotDir]
 * Needs Google Chrome. No network and no extra packages.
 */
import { spawn } from 'node:child_process';
import { mkdtempSync, createReadStream, existsSync, statSync, mkdirSync, writeFileSync, readFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, dirname, extname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { createHash } from 'node:crypto';
import http from 'node:http';
import net from 'node:net';

const root = dirname(fileURLToPath(import.meta.url));
const shotDir = process.argv[2] || join(tmpdir(), 'hero-shots');
mkdirSync(shotDir, { recursive: true });

const LOCKED = {
  'app.js': '0a90ebd504b106ffefdff5ee353236c9008cfcd198c01ea53aeacee44a5d62e3',
  'hero_revise.css': 'c9dc34403e627947e1c05682d0a2949b84b3a5de877cc329e01600b0eaa01d06',
  'style.css': 'ccd7ceedcd937ec2b21e7880d47dc11e838dcc48b1724635fd3428549bbdd872',
  'tokens_C.css': '0f39c459425987e0a33b06f4cefa90d97121058c5db79406ae677c386becf9fc',
  'assets/mascots/amp_default.svg': '413595094d71e4cdcf15f790c95d2ee7b5f57043e4ff2e87eccda9ebbd71d5d9',
  'assets/mascots/amp_happy.svg': '387347ae00b81cfaecccd7e65df17c356377a418aeb4ecfecaf5e7fe5f2cfe22',
  'assets/mascots/amp_surprised.svg': '87a2a5a542a5ba201afff62c2cfb309ccf83d0132ed908c3f16a625c6b63c710',
  'assets/mascots/drum_default.svg': 'd65603ec441edd43f6c72bc9f4c26e699c0e7e32611fb620519d9193e2d101a3',
  'assets/mascots/drum_happy.svg': 'af80b1cfcec53174715d25a8585ce351b6bfca4f76492fb94f0c641a9588de95',
  'assets/mascots/drum_surprised.svg': '7001c05e01af28a1b2bc82cd6e6ebbb048f4e906f7b54aab7aa3c05e10fd1780',
  'assets/mascots/guitar_default.svg': '46ecbd13b1edd2e949ce5d41dc9577e443f0ac2adb7af4d1d9a58632653f46d3',
  'assets/mascots/guitar_happy.svg': 'e5f9d1845f46b579fbb63f1455d876fece3f087e832a4f056cc4a998732bc2a8',
  'assets/mascots/guitar_surprised.svg': '22277965844db46234c6b21466b0ab5bc16db860689614916735bbfa35a8c25b',
  'assets/mascots/mic_default.svg': '6fcd00d7ec23adfb56afcaf996a2c2270ce0b65be0b75ec177c0abd698910b49',
  'assets/mascots/mic_happy.svg': 'fd4930856b38be4a0d20b6dc5b2dfd05724597b23f4a3e31b06f56494b050c18',
  'assets/mascots/mic_surprised.svg': 'e34de16c0f3823c985bf698408c323b5a81769d43b4e0f04c280ab0fdcd1d10c',
  'assets/mascots/note_default.svg': 'd702c2d4515b740f905113161f7f026cfdcc555724b872052c6724adfdf24b9b',
  'assets/mascots/note_happy.svg': '4f94acd8ccbba04a390ab2f3059a022017299b80a922d1d71051baeffa819568',
  'assets/mascots/note_surprised.svg': 'b320b4510b25de34d0dfe35c570adb5f6b270e0a5e8d32e4ea54210af295f8e2',
  'assets/mascots/pick_default.svg': 'fc604f1f7b47138f4be1fd65ff65ebdea5c2f7edd893201fc88826fab69b0c6c',
  'assets/mascots/pick_happy.svg': '6ad483ea9620ebfebdd71b791097b289f920c4b1fdd8c2eb17db21f9c4f86610',
  'assets/mascots/pick_surprised.svg': 'fc3803da7a1a3cc196ed187dcbe7875e60351fb31dc7afbd3600a5d26af9f3f8',
};

function sha256(file) {
  return createHash('sha256').update(readFileSync(join(root, file))).digest('hex');
}

function eyeMap() {
  const I = { a: 1, b: 0, c: 0, d: 1, e: 0, f: 0 };
  const mul = (m1, m2) => ({
    a: m1.a * m2.a + m1.c * m2.b, b: m1.b * m2.a + m1.d * m2.b,
    c: m1.a * m2.c + m1.c * m2.d, d: m1.b * m2.c + m1.d * m2.d,
    e: m1.a * m2.e + m1.c * m2.f + m1.e, f: m1.b * m2.e + m1.d * m2.f + m1.f,
  });
  const apply = (m, x, y) => [m.a * x + m.c * y + m.e, m.b * x + m.d * y + m.f];
  function fromList(str) {
    const parts = [...str.matchAll(/([a-zA-Z]+)\(([^)]*)\)/g)];
    let m = I;
    for (let i = parts.length - 1; i >= 0; i--) {
      const name = parts[i][1];
      const n = parts[i][2].trim().split(/[\s,]+/).filter(Boolean).map(Number);
      let t = I;
      if (name === 'translate') t = { a: 1, b: 0, c: 0, d: 1, e: n[0], f: n[1] || 0 };
      else if (name === 'scale') t = { a: n[0], b: 0, c: 0, d: n.length > 1 ? n[1] : n[0], e: 0, f: 0 };
      else if (name === 'rotate') {
        const ang = n[0] * Math.PI / 180, cos = Math.cos(ang), sin = Math.sin(ang);
        let r = { a: cos, b: sin, c: -sin, d: cos, e: 0, f: 0 };
        if (n.length >= 3) {
          r = mul({ a: 1, b: 0, c: 0, d: 1, e: n[1], f: n[2] }, mul(r, { a: 1, b: 0, c: 0, d: 1, e: -n[1], f: -n[2] }));
        }
        t = r;
      }
      m = mul(t, m);
    }
    return m;
  }
  const out = {};
  for (const role of ['note', 'drum', 'guitar', 'mic', 'amp', 'pick']) {
    const svg = readFileSync(join(root, 'assets/mascots', `${role}_default.svg`), 'utf8');
    const [vx, vy, vw, vh] = svg.match(/viewBox="([^"]+)"/)[1].split(/\s+/).map(Number);
    const tags = [...svg.matchAll(/<(\/?)(svg|g|ellipse|circle)\b([^>]*)>/g)];
    let stack = [I];
    const eyes = [];
    for (const tag of tags) {
      const close = tag[1] === '/', name = tag[2], attrs = tag[3] || '';
      if (close) { if (name !== 'svg') stack.pop(); continue; }
      if (name === 'svg') continue;
      const self = /\/>$/.test(tag[0]);
      let m = stack.at(-1);
      const tr = attrs.match(/transform="([^"]+)"/);
      if (tr) m = mul(m, fromList(tr[1]));
      if (name === 'ellipse' && /fill="#000"/.test(attrs)) {
        const cx = +attrs.match(/\bcx="([^"]+)"/)[1];
        const cy = +attrs.match(/\bcy="([^"]+)"/)[1];
        const rx = +attrs.match(/\brx="([^"]+)"/)[1];
        const ry = +attrs.match(/\bry="([^"]+)"/)[1];
        const [x, y] = apply(m, cx, cy);
        const [x2, y2] = apply(m, cx + rx, cy);
        const [x3, y3] = apply(m, cx, cy + ry);
        eyes.push({
          x: (x - vx) / vw, y: (y - vy) / vh,
          rx: Math.hypot(x2 - x, y2 - y) / vw, ry: Math.hypot(x3 - x, y3 - y) / vh,
        });
      }
      if (!self && name === 'g') stack.push(m);
    }
    if (eyes.length !== 2) throw new Error(`expected 2 eyes for ${role}, got ${eyes.length}`);
    out[role] = eyes;
  }
  return out;
}

const EYES = eyeMap();

function freePort() {
  return new Promise((resolve) => {
    const server = net.createServer();
    server.listen(0, '127.0.0.1', () => {
      const { port } = server.address();
      server.close(() => resolve(port));
    });
  });
}

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.mjs': 'text/javascript; charset=utf-8',
  '.svg': 'image/svg+xml',
  '.woff2': 'font/woff2',
  '.json': 'application/json',
};

function startServer() {
  const server = http.createServer((req, res) => {
    let pathname = decodeURIComponent(new URL(req.url, 'http://127.0.0.1').pathname);
    if (pathname.endsWith('/')) pathname += 'index.html';
    const file = join(root, pathname);
    if (!file.startsWith(root) || !existsSync(file) || statSync(file).isDirectory()) {
      res.writeHead(404); res.end('missing'); return;
    }
    res.writeHead(200, { 'content-type': MIME[extname(file)] || 'application/octet-stream', 'cache-control': 'no-store' });
    createReadStream(file).pipe(res);
  });
  return new Promise((resolve) => server.listen(0, '127.0.0.1', () => resolve(server)));
}

async function connectChrome(port) {
  const ver = await (await fetch(`http://127.0.0.1:${port}/json/version`)).json();
  const ws = new WebSocket(ver.webSocketDebuggerUrl);
  await new Promise((resolve, reject) => {
    ws.addEventListener('open', resolve);
    ws.addEventListener('error', reject);
  });
  let seq = 0;
  const pending = new Map();
  ws.addEventListener('message', (ev) => {
    const msg = JSON.parse(ev.data);
    if (msg.id && pending.has(msg.id)) {
      pending.get(msg.id)(msg);
      pending.delete(msg.id);
    }
  });
  const send = (method, params = {}, sessionId) => new Promise((resolve, reject) => {
    const id = ++seq;
    pending.set(id, (msg) => {
      if (msg.error) reject(new Error(`${method} ${JSON.stringify(msg.error)}`));
      else resolve(msg.result);
    });
    const packet = { id, method, params };
    if (sessionId) packet.sessionId = sessionId;
    ws.send(JSON.stringify(packet));
  });
  const created = await send('Target.createTarget', { url: 'about:blank' });
  const attached = await send('Target.attachToTarget', { targetId: created.targetId, flatten: true });
  const sessionId = attached.sessionId;
  const s = (method, params = {}) => send(method, params, sessionId);
  return { ws, s };
}

const PAGE_FN = function pageMeasure(eyes) {
  const fails = [];
  const findings = [];
  const seen = new Set();
  const fail = (msg) => { if (!seen.has(msg)) { seen.add(msg); fails.push(msg); } };
  const note = (msg) => { if (!seen.has(msg)) { seen.add(msg); findings.push(msg); } };
  if (window.__timers) window.__timers.forEach((id) => clearTimeout(id));
  const stage = document.querySelector('.mascot-stage');
  const stageRect = () => stage.getBoundingClientRect();
  const all = [...stage.querySelectorAll(':scope > button.mascot')];
  const visible = () => all.filter((m) => getComputedStyle(m).display !== 'none');
  const num = (el, name) => parseFloat(getComputedStyle(el).getPropertyValue(name));
  const faceRect = (m) => {
    const r = m.querySelector('.face-default').getBoundingClientRect();
    return { left: r.left, top: r.top, right: r.right, bottom: r.bottom, width: r.width, height: r.height };
  };
  const clearMotion = (m) => {
    m.classList.remove('is-active', 'is-hopping');
    delete m.dataset.expression;
    for (const el of m.querySelectorAll('.m-pop,.m-spot,.m-float,.m-breath,.m-hop')) {
      el.style.animation = 'none';
      el.style.transition = 'none';
      el.style.transform = 'none';
    }
  };
  const applyLayers = (m, pose) => {
    const pop = m.querySelector('.m-pop');
    const spot = m.querySelector('.m-spot');
    const float = m.querySelector('.m-float');
    const breath = m.querySelector('.m-breath');
    const hop = m.querySelector('.m-hop');
    for (const el of [pop, spot, float, breath, hop]) {
      el.style.animation = 'none';
      el.style.transition = 'none';
    }
    pop.style.transform = pose.pop || 'none';
    spot.style.transform = pose.spot || 'none';
    float.style.transform = pose.float || 'none';
    breath.style.transform = pose.breath || 'none';
    hop.style.transform = pose.hop || 'none';
  };
  function glyphBoxes(el) {
    const range = document.createRange();
    range.selectNodeContents(el);
    return [...range.getClientRects()].filter((r) => r.width > 0.5 && r.height > 0.5)
      .map((r) => ({ left: r.left, top: r.top, right: r.right, bottom: r.bottom }));
  }
  function overlapArea(a, b) {
    const w = Math.min(a.right, b.right) - Math.max(a.left, b.left);
    const h = Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top);
    return w > 0 && h > 0 ? w * h : 0;
  }
  function animNamed(el, name) {
    const found = el.getAnimations().find((a) => a.animationName === name);
    if (!found) {
      const names = el.getAnimations().map((a) => `${a.animationName || a.transitionProperty || a.constructor.name}:${a.playState}`);
      throw new Error(`missing animation ${name} on .${el.className}; have ${names.join(',') || 'none'}`);
    }
    return found;
  }
  function restart(el) {
    el.style.animation = 'none';
    el.style.transform = '';
    el.style.transition = '';
    void el.offsetWidth;
    el.style.animation = '';
    void el.offsetWidth;
  }

  const textTargets = [
    ['label', inkBoxes(document.querySelector('.hero-copy .label'))],
    ['title', inkBoxes(document.querySelector('#home-title'))],
    ['sub', inkBoxes(document.querySelector('.hero-copy .sub'))],
    ...[...document.querySelectorAll('.hero-copy .actions a')].map((a, i) => [`button${i}`, inkBoxes(a)]),
  ];
  for (const [name, boxes] of textTargets) if (!boxes.length) fail(`no glyph ink for ${name}`);
  const art = new Map();
  function artwork(m) {
    const role = m.dataset.role;
    if (art.has(role)) return art.get(role);
    const img = m.querySelector('.face-default');
    const hop = m.querySelector('.m-hop');
    const w = Math.max(2, Math.round(hop.offsetWidth));
    const h = Math.max(2, Math.round(hop.offsetHeight));
    const canvas = document.createElement('canvas');
    canvas.width = w; canvas.height = h;
    const ctx = canvas.getContext('2d', { willReadFrequently: true });
    ctx.drawImage(img, 0, 0, w, h);
    const info = { data: ctx.getImageData(0, 0, w, h).data, w, h };
    let opaque = 0;
    for (let i = 3; i < info.data.length; i += 4) if (info.data[i] > 20) opaque++;
    if (!opaque) throw new Error(`no opaque pixels for ${role}`);
    art.set(role, info);
    return info;
  }
  function cornersOf(m) {
    const hop = m.querySelector('.m-hop');
    const probe = hop.querySelector('i.probe') || hop.appendChild(Object.assign(document.createElement('i'), { className: 'probe' }));
    probe.style.cssText = 'position:absolute;width:0;height:0;padding:0;border:0;pointer-events:none';
    const pts = [];
    for (const [x, y] of [[0, 0], [100, 0], [0, 100]]) {
      probe.style.left = x + '%';
      probe.style.top = y + '%';
      const r = probe.getBoundingClientRect();
      pts.push([r.left, r.top]);
    }
    return pts;
  }
  function alphaAt(info, corners, x, y) {
    const [tl, tr, bl] = corners;
    const ux = tr[0] - tl[0], uy = tr[1] - tl[1];
    const vx = bl[0] - tl[0], vy = bl[1] - tl[1];
    const det = ux * vy - uy * vx;
    if (Math.abs(det) < 1e-6) return 0;
    const px = x - tl[0], py = y - tl[1];
    const u = (px * vy - py * vx) / det;
    const v = (ux * py - uy * px) / det;
    if (u < -0.02 || v < -0.02 || u > 1.02 || v > 1.02) return 0;
    const ix = Math.max(0, Math.min(info.w - 1, Math.round(u * (info.w - 1))));
    const iy = Math.max(0, Math.min(info.h - 1, Math.round(v * (info.h - 1))));
    return info.data[(iy * info.w + ix) * 4 + 3];
  }
  function opaqueHits(m, box, rect) {
    const left = Math.max(rect.left, box.left);
    const right = Math.min(rect.right, box.right);
    const top = Math.max(rect.top, box.top);
    const bottom = Math.min(rect.bottom, box.bottom);
    if (right - left < 0.5 || bottom - top < 0.5) return 0;
    const info = artwork(m);
    const corners = cornersOf(m);
    let hits = 0;
    for (let y = top + 0.5; y <= bottom; y += 1) {
      for (let x = left + 0.5; x <= right; x += 1) {
        if (alphaAt(info, corners, x, y) > 20) hits++;
      }
    }
    return hits;
  }
  function inkBoxes(el) {
    const cs = getComputedStyle(el);
    const ctx = document.createElement('canvas').getContext('2d');
    ctx.font = `${cs.fontStyle} ${cs.fontWeight} ${cs.fontSize} ${cs.fontFamily}`;
    const boxes = [];
    const walk = (node) => {
      for (const child of node.childNodes) {
        if (child.nodeType === 3 && child.textContent.trim()) {
          const mark = document.createElement('span');
          mark.style.cssText = 'display:inline-block;width:0;height:0;vertical-align:baseline;pointer-events:none';
          child.parentNode.insertBefore(mark, child);
          const baseline = mark.getBoundingClientRect().top;
          mark.remove();
          const text = child.textContent;
          for (let i = 0; i < text.length; i++) {
            const ch = text[i];
            if (!ch.trim()) continue;
            const range = document.createRange();
            range.setStart(child, i);
            range.setEnd(child, i + 1);
            const rect = range.getBoundingClientRect();
            if (rect.width < 0.2) continue;
            const metrics = ctx.measureText(ch);
            const left = rect.left - (metrics.actualBoundingBoxLeft || 0);
            const right = rect.left + (metrics.actualBoundingBoxRight || 0);
            const top = baseline - (metrics.actualBoundingBoxAscent || 0);
            const bottom = baseline + (metrics.actualBoundingBoxDescent || 0);
            if (right - left < 0.3 || bottom - top < 0.3) continue;
            boxes.push({ left, right, top, bottom, ch });
          }
        } else if (child.nodeType === 1 && child.tagName !== 'BR') walk(child);
      }
    };
    walk(el);
    return boxes;
  }
  function boxGap(a, b) {
    const dx = a.right < b.left ? b.left - a.right : b.right < a.left ? a.left - b.right : 0;
    const dy = a.bottom < b.top ? b.top - a.bottom : b.bottom < a.top ? a.top - b.bottom : 0;
    return dx === 0 && dy === 0 ? 0 : Math.hypot(dx, dy);
  }
  function inkGap(m, box, pad = 28) {
    const rect = faceRect(m);
    if (opaqueHits(m, box, rect) > 0) return -1;
    const info = artwork(m);
    const corners = cornersOf(m);
    let best = Infinity;
    const left = Math.max(rect.left, box.left - pad);
    const right = Math.min(rect.right, box.right + pad);
    const top = Math.max(rect.top, box.top - pad);
    const bottom = Math.min(rect.bottom, box.bottom + pad);
    for (let y = top; y <= bottom; y += 1) {
      for (let x = left; x <= right; x += 1) {
        if (alphaAt(info, corners, x, y) <= 20) continue;
        const dx = x < box.left ? box.left - x : x > box.right ? x - box.right : 0;
        const dy = y < box.top ? box.top - y : y > box.bottom ? y - box.bottom : 0;
        const dist = Math.hypot(dx, dy);
        if (dist < best) best = dist;
      }
    }
    return best;
  }
  const bars = document.querySelector('.hero-levels').getBoundingClientRect();

  const clientW = document.documentElement.clientWidth;
  const expectedH = clientW <= 374 ? 680 : clientW <= 1023 ? 720 : clientW <= 1199 ? 860 : 960;
  const heroH = document.querySelector('.hero').getBoundingClientRect().height;
  const stageH = stageRect().height;
  if (Math.abs(heroH - expectedH) > 0.6) fail(`hero height ${heroH} expected ${expectedH}`);
  if (Math.abs(stageH - expectedH) > 0.6) fail(`stage height ${stageH} expected ${expectedH}`);
  const h1 = getComputedStyle(document.querySelector('#home-title')).fontSize;
  if (clientW <= 374 && h1 !== '30px') fail(`title size ${h1} expected 30px`);
  if (clientW > 374 && h1 === '30px') fail('30px title leaked past 374');

  const copyLeft = document.querySelector('.hero-copy').getBoundingClientRect().left;
  const headerLeft = document.querySelector('.header').getBoundingClientRect().left;
  if (Math.abs(copyLeft - headerLeft) > 1) fail(`copy left ${copyLeft} != header left ${headerLeft}`);

  const glow = getComputedStyle(document.querySelector('.hero-glow')).backgroundImage;
  const bodyBg = getComputedStyle(document.body).backgroundImage;
  if (bodyBg !== 'none') fail(`body still paints a glow: ${bodyBg.slice(0, 140)}`);
  const large = [];
  for (const el of document.querySelectorAll('body *')) {
    const bg = getComputedStyle(el).backgroundImage;
    if (bg && bg !== 'none' && bg.includes('radial-gradient') && !/1px/.test(bg)) large.push(el.className + ' ' + bg.slice(0, 80));
  }
  if (large.length !== 1 || !large[0].startsWith('hero-glow')) fail(`page lights ${JSON.stringify(large)}`);
  if (clientW >= 1024) {
    if (!/720px/.test(glow) || !/540px/.test(glow) || !/56%/.test(glow)) fail(`desktop glow ${glow.slice(0, 180)}`);
  } else if (!/420px/.test(glow) || !/360px/.test(glow) || !/72%/.test(glow)) fail(`mobile glow ${glow.slice(0, 180)}`);

  for (const m of visible()) {
    const img = m.querySelector('img');
    const cs = getComputedStyle(img);
    if (cs.filter !== 'none') fail(`${m.dataset.role} filter ${cs.filter}`);
    if (cs.boxShadow !== 'none') fail(`${m.dataset.role} shadow ${cs.boxShadow}`);
  }
  const stageCs = getComputedStyle(stage);
  const heroCs = getComputedStyle(document.querySelector('.hero'));
  if (stageCs.overflow === 'hidden' || heroCs.overflow === 'hidden') fail('stage or hero overflow hidden');

  const roles = {};
  const motions = new Map();
  let worstPose = null;
  function scaleOf(transform) {
    if (!transform || transform === 'none') return 1;
    const matrix = new DOMMatrix(transform);
    return Math.max(Math.abs(matrix.a), Math.abs(matrix.d));
  }
  for (const m of visible()) {
    const role = m.dataset.role;
    const k = num(m, '--k');
    const fx = num(m, '--fx');
    const fy = num(m, '--fy');
    clearMotion(m);
    const pop = m.querySelector('.m-pop');
    const spot = m.querySelector('.m-spot');
    const hop = m.querySelector('.m-hop');
    const floatEl = m.querySelector('.m-float');
    const breathEl = m.querySelector('.m-breath');
    pop.style.animation = 'none';
    restart(hop);
    m.classList.add('is-hopping');
    void hop.offsetWidth;
    const hopName = getComputedStyle(hop).animationName;
    if (role === 'note' && hopName !== 'hop-note') fail(`${role} hop animation is ${hopName}`);
    if (role !== 'note' && hopName !== 'hop') fail(`${role} hop animation is ${hopName}`);
    const hopAnim = animNamed(hop, hopName);
    const hopTiming = hopAnim.effect.getComputedTiming();
    const hopDur = hopTiming.activeDuration;
    const hopSamples = [];
    const hopKeyframes = [];
    for (let t = 0; t <= hopDur + 0.01; t += 16) {
      hopAnim.currentTime = (hopTiming.delay || 0) + Math.min(t, hopDur);
      hopSamples.push(getComputedStyle(hop).transform);
    }
    for (const f of [0, 0.18, 0.45, 0.7, 0.85, 1]) {
      hopAnim.currentTime = (hopTiming.delay || 0) + hopDur * f;
      hopKeyframes.push(getComputedStyle(hop).transform);
    }
    m.classList.remove('is-hopping');
    hop.style.animation = 'none';
    hop.style.transform = 'none';

    spot.style.animation = 'none';
    spot.style.transition = '';
    spot.style.transform = '';
    m.classList.remove('is-active');
    void spot.offsetWidth;
    m.classList.add('is-active');
    void spot.offsetWidth;
    const transition = spot.getAnimations().find((a) => a.transitionProperty === 'transform');
    if (!transition) throw new Error(`focus transition was not created for ${role}; transform ${getComputedStyle(spot).transform}`);
    const focusTiming = transition.effect.getComputedTiming();
    const focusDur = focusTiming.activeDuration || 700;
    let peak = 1;
    let peakTransform = 'none';
    for (let t = 0; t <= focusDur + 0.01; t += 4) {
      transition.currentTime = (focusTiming.delay || 0) + Math.min(t, focusDur);
      const transform = getComputedStyle(spot).transform;
      const s = scaleOf(transform);
      if (s > peak) { peak = s; peakTransform = transform; }
    }
    transition.currentTime = (focusTiming.delay || 0) + focusDur;
    const settled = getComputedStyle(spot).transform;
    m.classList.remove('is-active');
    spot.style.transition = 'none';
    spot.style.transform = 'none';
    const peakCap = clientW <= 1023 ? 1.08 : 1.10;
    if (role === 'note' && peak > peakCap + 0.0005) fail(`${role} focus peak ${peak.toFixed(4)} > ${peakCap}`);
    if (role !== 'note' && peak < 1.14) fail(`${role} focus peak ${peak.toFixed(4)} dropped below the locked 1.15 curve`);

    const floats = ['translate(0px, 0px)', `translate(${fx}px, ${fy}px)`];
    const breaths = ['scale(1, 1)', `scale(${1 - 0.018 * k}, ${1 + 0.022 * k})`];
    const sr = stageRect();
    let worst = { clearance: Infinity };
    let worstEntry = { clearance: Infinity };
    let restOverlap = 0;
    let motionOverlap = 0;
    let entryOverlap = 0;
    let minTextGap = Infinity;
    let minTextPose = 'none';
    const consider = (rect, pose, bucket) => {
      const top = rect.top - sr.top;
      const left = rect.left - sr.left;
      const right = sr.right - rect.right;
      const bottom = sr.bottom - rect.bottom;
      const clearance = Math.min(top, left, right, bottom);
      const record = { clearance, top, left, right, bottom, pose };
      if (clearance < bucket.clearance) Object.assign(bucket, record);
      if (!worstPose || clearance < worstPose.clearance) worstPose = { role, ...record };
      let hits = 0;
      const aabbHits = textTargets.some(([, boxes]) => boxes.some((box) => overlapArea(rect, box) > 0.5));
      if (aabbHits) {
        for (const [, boxes] of textTargets) for (const box of boxes) hits += opaqueHits(m, box, rect);
      }
      if (pose === 'rest') restOverlap = Math.max(restOverlap, hits);
      else if (String(pose).startsWith('entry')) entryOverlap = Math.max(entryOverlap, hits);
      else motionOverlap = Math.max(motionOverlap, hits);
      if (clientW <= 374) {
        for (const [, boxes] of textTargets) {
          for (const box of boxes) {
            const separated = boxGap(rect, box);
            let gap = separated;
            if (separated < 16) {
              const measured = inkGap(m, box, 40);
              gap = measured < 0 ? -1 : (Number.isFinite(measured) ? measured : 40);
            }
            if (gap < minTextGap) { minTextGap = gap; minTextPose = pose; }
          }
        }
      }
      const de = document.documentElement;
      if (de.scrollWidth > de.clientWidth + 0.5) fail(`${role} ${pose} horizontal scroll ${de.scrollWidth}>${de.clientWidth}`);
    };
    applyLayers(m, {});
    consider(faceRect(m), 'rest', worst);

    restart(pop);
    const popAnim = animNamed(pop, 'pop');
    const popTiming = popAnim.effect.getComputedTiming();
    const popDur = popTiming.activeDuration;
    spot.style.animation = 'none';
    spot.style.transform = 'none';
    hop.style.animation = 'none';
    hop.style.transform = 'none';
    for (let t = 0; t <= popDur + 0.01; t += 8) {
      popAnim.currentTime = (popTiming.delay || 0) + Math.min(t, popDur);
      for (const fl of floats) for (const br of breaths) {
        floatEl.style.animation = 'none';
        breathEl.style.animation = 'none';
        floatEl.style.transform = fl;
        breathEl.style.transform = br;
        consider(faceRect(m), `entry@${Math.round(t)}`, worstEntry);
      }
    }
    pop.style.animation = 'none';
    pop.style.transform = 'none';

    const focusExtremes = ['none', settled, peakTransform];
    motions.set(role, { peakTransform, settled, hopKeyframes, fx, fy, k });
    for (const hopT of hopSamples) {
      for (const fl of floats) for (const br of breaths) {
        applyLayers(m, { spot: peakTransform, hop: hopT, float: fl, breath: br });
        consider(faceRect(m), 'combo-peak', worst);
      }
    }
    for (const spotT of focusExtremes) {
      for (const hopT of hopKeyframes) {
        for (const fl of floats) for (const br of breaths) {
          applyLayers(m, { spot: spotT, hop: hopT, float: fl, breath: br });
          consider(faceRect(m), 'combo-key', worst);
        }
      }
    }
    if (worst.clearance < 16) fail(`${role} combo clearance ${worst.clearance.toFixed(2)} < 16 (${worst.pose} t${worst.top.toFixed(1)} l${worst.left.toFixed(1)} r${worst.right.toFixed(1)} b${worst.bottom.toFixed(1)})`);
    if (worstEntry.clearance < 16) fail(`${role} entry clearance ${worstEntry.clearance.toFixed(2)} < 16`);
    if (restOverlap > 0) fail(`${role} rest ink intrusion ${restOverlap}`);
    if (entryOverlap > 0) fail(`${role} entry ink intrusion ${entryOverlap}`);
    if (motionOverlap > 0) fail(`${role} motion ink intrusion ${motionOverlap}`);
    if (clientW <= 374 && minTextGap < 16) fail(`${role} text ink clearance ${Number.isFinite(minTextGap) ? minTextGap.toFixed(2) : minTextGap}px < 16 (${minTextPose})`);
    let restGap = null;
    if (role === 'note' && clientW <= 374) {
      clearMotion(m);
      applyLayers(m, {});
      const gaps = textTargets.flatMap(([, boxes]) => boxes.map((box) => inkGap(m, box, 160))).filter((g) => Number.isFinite(g) && g >= 0);
      restGap = gaps.length ? Math.min(...gaps) : null;
    }
    if (role === 'note' && clientW <= 1023 && Math.abs(fx) > 0.01) fail(`mobile note --fx is ${fx}, expected 0`);
    if (role === 'note' && clientW >= 1024 && Math.abs(fx - 8) > 0.01) fail(`desktop note --fx is ${fx}, expected 8`);
    clearMotion(m);
    roles[role] = {
      combo: +worst.clearance.toFixed(2),
      entry: +worstEntry.clearance.toFixed(2),
      restOverlap,
      entryOverlap,
      motionOverlap,
      restGap: restGap == null ? null : +restGap.toFixed(2),
      textGap: Number.isFinite(minTextGap) ? +minTextGap.toFixed(2) : null,
      textPose: Number.isFinite(minTextGap) ? minTextPose : null,
      peakScale: +peak.toFixed(4),
      hop: hopName,
      top: +worst.top.toFixed(2),
      left: +worst.left.toFixed(2),
      right: +worst.right.toFixed(2),
      bottom: +worst.bottom.toFixed(2),
      w: +faceRect(m).width.toFixed(2),
      fx,
      fy,
    };
  }

  function eyePoints(m) {
    const hop = m.querySelector('.m-hop');
    const probe = hop.querySelector('i.eye') || hop.appendChild(Object.assign(document.createElement('i'), { className: 'eye' }));
    probe.style.cssText = 'position:absolute;width:0;height:0;padding:0;border:0;pointer-events:none';
    const pts = [];
    for (const eye of eyes[m.dataset.role]) {
      for (const [dx, dy] of [[0, 0], [eye.rx, 0], [-eye.rx, 0], [0, eye.ry], [0, -eye.ry]]) {
        probe.style.left = ((eye.x + dx) * 100) + '%';
        probe.style.top = ((eye.y + dy) * 100) + '%';
        const r = probe.getBoundingClientRect();
        pts.push([r.left, r.top]);
      }
    }
    return pts;
  }
  const shown = visible();
  function faceCovered(label) {
    const points = shown.map((m) => ({ role: m.dataset.role, m, pts: eyePoints(m) }));
    for (const eye of points) {
      for (const other of points) {
        if (eye.role === other.role) continue;
        const info = artwork(other.m);
        const corners = cornersOf(other.m);
        for (const [x, y] of eye.pts) {
          if (alphaAt(info, corners, x, y) > 20) fail(`${eye.role} eye covered by ${other.role} at ${label}`);
        }
      }
    }
  }
  for (const m of shown) clearMotion(m);
  faceCovered('rest');
  for (const active of shown) {
    const motion = motions.get(active.dataset.role);
    const breathOn = `scale(${1 - 0.018 * motion.k}, ${1 + 0.022 * motion.k})`;
    const poses = [];
    for (const hopT of motion.hopKeyframes) {
      for (const fl of [`translate(0px, 0px)`, `translate(${motion.fx}px, ${motion.fy}px)`]) {
        for (const br of ['scale(1, 1)', breathOn]) poses.push({ spot: motion.peakTransform, hop: hopT, float: fl, breath: br });
      }
    }
    for (const otherFloat of [0, 1]) {
      for (const pose of poses) {
        for (const m of shown) clearMotion(m);
        applyLayers(active, pose);
        for (const other of shown) {
          if (other === active) continue;
          const om = motions.get(other.dataset.role);
          applyLayers(other, otherFloat
            ? { float: `translate(${om.fx}px, ${om.fy}px)`, breath: `scale(${1 - 0.018 * om.k}, ${1 + 0.022 * om.k})` }
            : {});
        }
        faceCovered(`${active.dataset.role}-focus`);
      }
    }
    const pop = active.querySelector('.m-pop');
    restart(pop);
    const popAnim = animNamed(pop, 'pop');
    const popTiming = popAnim.effect.getComputedTiming();
    const popDur = popTiming.activeDuration;
    const entrySamples = [];
    for (const frac of [0, 0.42, 0.5, 0.58, 0.74, 0.88, 1]) {
      popAnim.currentTime = (popTiming.delay || 0) + popDur * frac;
      entrySamples.push(getComputedStyle(pop).transform);
    }
    pop.style.animation = 'none';
    for (const popT of entrySamples) {
      for (const otherFloat of [0, 1]) {
        for (const m of shown) clearMotion(m);
        applyLayers(active, {
          pop: popT,
          float: `translate(${motion.fx}px, ${motion.fy}px)`,
          breath: breathOn,
        });
        for (const other of shown) {
          if (other === active) continue;
          const om = motions.get(other.dataset.role);
          applyLayers(other, otherFloat
            ? { float: `translate(${om.fx}px, ${om.fy}px)`, breath: `scale(${1 - 0.018 * om.k}, ${1 + 0.022 * om.k})` }
            : {});
        }
        faceCovered(`${active.dataset.role}-entry`);
      }
    }
  }
  for (const m of shown) clearMotion(m);

  for (const [, boxes] of textTargets) {
    for (const box of boxes) {
      if (overlapArea(box, bars) > 0.5) fail('level bars overlap copy');
    }
  }

  const de = document.documentElement;
  const links = [...document.querySelectorAll('a')].map((a) => a.getAttribute('href'));
  if (links.some((href) => href && /about\.html|weixin|wechat/i.test(href))) fail('unexpected link ' + links.join(','));
  const boundary = document.querySelector('#preview-boundary');
  if (!boundary || !boundary.textContent.includes('当前仅首屏演示')) fail('boundary note missing');
  const hiddenNow = all.filter((m) => getComputedStyle(m).display === 'none').map((m) => m.dataset.role).sort();
  const expectHidden = de.clientWidth <= 1023 ? ['amp', 'guitar', 'pick'] : [];
  if (hiddenNow.join() !== expectHidden.join()) fail(`hidden ${hiddenNow.join()} expected ${expectHidden.join()}`);
  const subEl = document.querySelector('.sub');
  const intact = [...subEl.childNodes].some((node) => node.nodeType === 3 && node.textContent.includes('家庭音乐俱乐部'));
  if (!intact) fail('家庭音乐俱乐部 is not one text run');
  const xsDisplay = getComputedStyle(document.querySelector('.sub-break-xs')).display;
  const subDisplay = getComputedStyle(document.querySelector('.sub-break')).display;
  if (de.clientWidth <= 374 && xsDisplay !== 'block') fail(`sub-break-xs is ${xsDisplay} at <=374`);
  if (de.clientWidth > 374 && xsDisplay !== 'none') fail(`sub-break-xs is ${xsDisplay} above 374`);
  if (de.clientWidth <= 1023 && subDisplay !== 'block') fail(`sub-break is ${subDisplay} at <=1023`);
  if (de.clientWidth >= 1024 && subDisplay !== 'none') fail(`sub-break is ${subDisplay} at >=1024`);

  return {
    fails,
    findings,
    clientWidth: de.clientWidth,
    scrollWidth: de.scrollWidth,
    clientHeight: de.clientHeight,
    scrollHeight: de.scrollHeight,
    stage: { w: +stageRect().width.toFixed(2), h: +stageRect().height.toFixed(2) },
    heroTop: +document.querySelector('.hero').getBoundingClientRect().top.toFixed(2),
    stageBottom: +stageRect().bottom.toFixed(2),
    viewportBottom: de.clientHeight,
    title: h1,
    copyLeft: +copyLeft.toFixed(2),
    headerLeft: +headerLeft.toFixed(2),
    glow: glow.slice(0, 160),
    roles,
    links,
    subBreak: subDisplay,
    subBreakXs: xsDisplay,
  };
};

async function evaluate(s, expression, awaitPromise = false) {
  const result = await s('Runtime.evaluate', { expression, returnByValue: true, awaitPromise });
  if (result.exceptionDetails) {
    const text = result.exceptionDetails.exception?.description || result.exceptionDetails.text;
    throw new Error(text);
  }
  return result.result.value;
}

async function main() {
  const hashFails = [];
  for (const [file, expect] of Object.entries(LOCKED)) {
    const got = sha256(file);
    if (got !== expect) hashFails.push(`${file} ${got}`);
  }
  if (hashFails.length) {
    console.error('LOCKED BYTE MISMATCH');
    hashFails.forEach((line) => console.error(line));
    process.exit(1);
  }
  console.log('locked bytes ok', Object.keys(LOCKED).length);

  const server = await startServer();
  const httpPort = server.address().port;
  const debugPort = await freePort();
  const userDir = mkdtempSync(join(tmpdir(), 'hero-chrome-'));
  const chrome = spawn('/usr/bin/google-chrome', [
    '--headless=new', '--disable-gpu', '--no-first-run', '--no-default-browser-check',
    '--disable-background-networking', '--disable-sync', '--hide-scrollbars',
    `--remote-debugging-port=${debugPort}`, `--user-data-dir=${userDir}`, 'about:blank',
  ], { stdio: ['ignore', 'ignore', 'pipe'] });
  let chromeLog = '';
  chrome.stderr.on('data', (buf) => { chromeLog += buf.toString(); });
  try {
    for (let i = 0; i < 80; i++) {
      try {
        const res = await fetch(`http://127.0.0.1:${debugPort}/json/version`);
        if (res.ok) break;
      } catch { /* retry */ }
      if (i === 79) throw new Error('chrome did not start\n' + chromeLog.slice(-500));
      await new Promise((r) => setTimeout(r, 100));
    }
    const { ws, s } = await connectChrome(debugPort);
    const consoleErrors = [];
    const cdp = s;
    await cdp('Page.enable');
    await cdp('Runtime.enable');
    await cdp('Network.enable');
    await cdp('Log.enable');
    await cdp('Page.addScriptToEvaluateOnNewDocument', {
      source: `(() => {
        window.__timers = [];
        const orig = window.setTimeout;
        window.setTimeout = function(fn, delay, ...args) {
          const id = orig(fn, delay, ...args);
          window.__timers.push(id);
          return id;
        };
      })();`,
    });
    const network = [];
    const raw = ws;
    // Network events arrive on the browser socket with sessionId. Listen before navigate.
    const pendingEvents = [];
    raw.addEventListener('message', (ev) => {
      const msg = JSON.parse(ev.data);
      if (!msg.method) return;
      if (msg.method === 'Network.responseReceived') network.push(msg.params.response);
      if (msg.method === 'Network.loadingFailed') network.push({ url: msg.params.url || msg.params.requestId, status: 0, error: msg.params.errorText });
      if (msg.method === 'Runtime.exceptionThrown') consoleErrors.push(msg.params.exceptionDetails.exception?.description || msg.params.exceptionDetails.text);
      if (msg.method === 'Runtime.consoleAPICalled' && msg.params.type === 'error') {
        consoleErrors.push(msg.params.args.map((a) => a.value || a.description).join(' '));
      }
      if (msg.method === 'Log.entryAdded' && msg.params.entry.level === 'error') consoleErrors.push(msg.params.entry.text);
      pendingEvents.push(msg.method);
    });

    const widths = [320, 374, 375, 390, 860, 1023, 1024, 1100, 1199, 1200, 1280, 1440];
    const report = { geometry: [], overflow: [], interaction: null, reduced: null, resources: null, consoleErrors };

    async function open(width, height, reduced = false) {
      await cdp('Emulation.setDeviceMetricsOverride', { width, height, deviceScaleFactor: 1, mobile: false });
      await cdp('Emulation.setEmulatedMedia', {
        features: [{ name: 'prefers-reduced-motion', value: reduced ? 'reduce' : 'no-preference' }],
      });
      network.length = 0;
      consoleErrors.length = 0;
      await cdp('Page.navigate', { url: `http://127.0.0.1:${httpPort}/index.html` });
      for (let i = 0; i < 50; i++) {
        const state = await evaluate(cdp, 'document.readyState');
        const imgs = await evaluate(cdp, '[...document.images].every(img => img.complete && img.naturalWidth > 0)');
        if (state === 'complete' && imgs) break;
        await new Promise((r) => setTimeout(r, 40));
        if (i === 49) throw new Error(`page not ready at ${width}x${height}`);
      }
      await evaluate(cdp, 'document.fonts.ready', true);
    }

    for (const width of widths) {
      await open(width, 1800, false);
      const measured = await evaluate(cdp, `(${PAGE_FN})(${JSON.stringify(EYES)})`);
      measured.requestedWidth = width;
      measured.height = 1800;
      report.geometry.push(measured);
      const flag = measured.fails.length ? 'FAIL' : 'ok';
      const tight = Object.entries(measured.roles).map(([role, v]) => `${role}:${v.combo}/${v.entry}${v.textGap == null ? '' : `/g${v.textGap}@${v.textPose}`}`).join(' ');
      console.log(`${flag} ${width} scroll ${measured.scrollWidth}/${measured.clientWidth} stage ${measured.stage.w}x${measured.stage.h} title ${measured.title} ${tight}`);
      measured.fails.forEach((item) => console.log('  FAIL', item));
      measured.findings.forEach((item) => console.log('  note', item));
    }

    const shortHeights = [640, 800, 900, 1080];
    for (const width of [320, 374, 390, 860, 1100, 1280, 1440]) {
      for (const height of shortHeights) {
        await open(width, height, false);
        const box = await evaluate(cdp, `(() => {
          const de = document.documentElement;
          const stage = document.querySelector('.mascot-stage').getBoundingClientRect();
          const hero = document.querySelector('.hero').getBoundingClientRect();
          return {
            scrollWidth: de.scrollWidth, clientWidth: de.clientWidth,
            scrollHeight: de.scrollHeight, clientHeight: de.clientHeight,
            stageH: +stage.height.toFixed(2), stageBottom: +stage.bottom.toFixed(2),
            heroH: +hero.height.toFixed(2), viewport: de.clientHeight,
          };
        })()`);
        const overflow = box.scrollWidth > box.clientWidth + 0.5;
        report.overflow.push({ width, height, ...box, overflow });
        if (overflow) console.log('OVERFLOW', width, height, box.scrollWidth, box.clientWidth);
      }
    }

    await open(1440, 1800, false);
    const resources = await evaluate(cdp, `performance.getEntriesByType('resource').map(r => ({name:r.name.split('/').slice(-2).join('/'), status:r.responseStatus, type:r.initiatorType}))`);
    report.resources = resources;
    const badRes = resources.filter((r) => r.status && r.status !== 200);
    console.log('resources', resources.length, 'non-200', badRes.length);
    badRes.forEach((r) => console.log('  ', r.status, r.name));

    async function press(key, code, vk, text) {
      const down = { type: 'keyDown', key, code, windowsVirtualKeyCode: vk, nativeVirtualKeyCode: vk };
      const up = { type: 'keyUp', key, code, windowsVirtualKeyCode: vk, nativeVirtualKeyCode: vk };
      if (text) { down.text = text; down.unmodifiedText = text; up.text = text; }
      await cdp('Input.dispatchKeyEvent', down);
      await cdp('Input.dispatchKeyEvent', up);
    }
    async function activeInfo() {
      return evaluate(cdp, `(() => {
        const el = document.activeElement;
        if (!el) return null;
        return { tag: el.tagName, role: el.dataset ? el.dataset.role || '' : '', label: el.getAttribute('aria-label') || el.textContent.slice(0, 24), expr: el.dataset ? el.dataset.expression || '' : '', active: el.classList.contains('is-active'), hop: el.classList.contains('is-hopping') };
      })()`);
    }
    await open(1440, 900, false);
    const tabPath = [];
    const reached = new Set();
    let noteFocused = false;
    for (let i = 0; i < 12 && !noteFocused; i++) {
      await press('Tab', 'Tab', 9);
      const info = await activeInfo();
      tabPath.push(info);
      if (info && info.role) reached.add(info.role);
      if (info && info.role === 'note') noteFocused = true;
    }
    const beforeSpace = await activeInfo();
    await press(' ', 'Space', 32, ' ');
    const afterSpace = await activeInfo();
    await press('Tab', 'Tab', 9);
    const beforeEnter = await activeInfo();
    if (beforeEnter && beforeEnter.role) reached.add(beforeEnter.role);
    await press('Enter', 'Enter', 13, '\r');
    const afterEnter = await activeInfo();
    for (let i = 0; i < 8; i++) {
      await press('Tab', 'Tab', 9);
      const info = await activeInfo();
      tabPath.push(info);
      if (info && info.role) reached.add(info.role);
    }
    report.interaction = { tabPath, reached: [...reached], beforeSpace, afterSpace, beforeEnter, afterEnter };

    await open(390, 844, false);
    await cdp('Emulation.setTouchEmulationEnabled', { enabled: true, maxTouchPoints: 1 });
    const point = await evaluate(cdp, `(() => { const r = document.querySelector('.m-note').getBoundingClientRect(); return {x: r.left + r.width/2, y: r.top + r.height/2}; })()`);
    await cdp('Input.dispatchTouchEvent', { type: 'touchStart', touchPoints: [{ x: point.x, y: point.y, id: 0, radiusX: 4, radiusY: 4 }] });
    await cdp('Input.dispatchTouchEvent', { type: 'touchEnd', touchPoints: [] });
    await new Promise((r) => setTimeout(r, 100));
    let touched = await evaluate(cdp, `(() => { const m = document.querySelector('.m-note'); const r = m.getBoundingClientRect(); const hit = document.elementFromPoint(r.left + r.width/2, r.top + r.height/2); return {expr: m.dataset.expression || '', hop: m.classList.contains('is-hopping'), via:'touch', hit: hit ? hit.tagName + '.' + (hit.dataset.role || hit.className) : 'none'}; })()`);
    if (!touched.expr) {
      await cdp('Input.dispatchMouseEvent', { type: 'mousePressed', x: point.x, y: point.y, button: 'left', clickCount: 1, pointerType: 'touch' });
      await cdp('Input.dispatchMouseEvent', { type: 'mouseReleased', x: point.x, y: point.y, button: 'left', clickCount: 1, pointerType: 'touch' });
      await new Promise((r) => setTimeout(r, 80));
      touched = await evaluate(cdp, `(() => { const m = document.querySelector('.m-note'); return {expr: m.dataset.expression || '', hop: m.classList.contains('is-hopping'), via:'pointer'}; })()`);
    }
    report.interaction.touch390 = touched;
    await cdp('Emulation.setTouchEmulationEnabled', { enabled: false });

    await open(1440, 900, true);
    const reducedBefore = await evaluate(cdp, `(() => { const m = document.querySelector('.m-note'); const r = m.querySelector('.face-default').getBoundingClientRect(); return {w:r.width,h:r.height,top:r.top,left:r.left, animations: document.getAnimations().length}; })()`);
    await new Promise((r) => setTimeout(r, 400));
    const reducedMid = await evaluate(cdp, `(() => { const m = document.querySelector('.m-note'); const r = m.querySelector('.face-default').getBoundingClientRect(); return {w:r.width,h:r.height,top:r.top,left:r.left, animations: document.getAnimations().length, hop:m.classList.contains('is-hopping')}; })()`);
    const noteCenter = await evaluate(cdp, `(() => { const r = document.querySelector('.m-note').getBoundingClientRect(); return {x:r.left+r.width/2,y:r.top+r.height/2}; })()`);
    await cdp('Input.dispatchMouseEvent', { type: 'mousePressed', x: noteCenter.x, y: noteCenter.y, button: 'left', clickCount: 1 });
    await cdp('Input.dispatchMouseEvent', { type: 'mouseReleased', x: noteCenter.x, y: noteCenter.y, button: 'left', clickCount: 1 });
    await new Promise((r) => setTimeout(r, 50));
    const reducedAfter = await evaluate(cdp, `(() => { const m = document.querySelector('.m-note'); const r = m.querySelector('.face-default').getBoundingClientRect(); return {expr:m.dataset.expression||'', hop:m.classList.contains('is-hopping'), active:m.classList.contains('is-active'), w:r.width, top:r.top, left:r.left}; })()`);
    report.reduced = { reducedBefore, reducedMid, reducedAfter };

    async function shot(name, width, height) {
      await open(width, height, false);
      await evaluate(cdp, `document.documentElement.dataset.shot='static'; document.querySelectorAll('.mascot').forEach(m => { m.classList.remove('is-active','is-hopping'); delete m.dataset.expression; });`);
      const frame = await evaluate(cdp, `(() => { const top = 0; const bottom = document.querySelector('.hero').getBoundingClientRect().bottom + window.scrollY; return {w: document.documentElement.clientWidth, h: Math.ceil(bottom)}; })()`);
      await cdp('Emulation.setDeviceMetricsOverride', { width, height: Math.max(height, frame.h), deviceScaleFactor: 1, mobile: false });
      const png = await cdp('Page.captureScreenshot', {
        format: 'png',
        clip: { x: 0, y: 0, width: frame.w, height: frame.h, scale: 1 },
        captureBeyondViewport: true,
      });
      const file = join(shotDir, name);
      writeFileSync(file, Buffer.from(png.data, 'base64'));
      console.log('shot', file, frame.w, frame.h);
    }
    await shot('hero_1440.png', 1440, 1100);
    await shot('hero_390.png', 390, 900);
    await shot('hero_374.png', 374, 800);
    await shot('hero_320.png', 320, 800);

    writeFileSync(join(shotDir, 'report.json'), JSON.stringify(report, null, 2));
    const geoFail = report.geometry.some((g) => g.fails.length);
    const overflowFail = report.overflow.some((o) => o.overflow);
    const resourceFail = (report.resources || []).some((r) => r.status && r.status !== 200);
    const touchFail = !report.interaction.touch390.expr;
    const keyFail = report.interaction.afterSpace.expr !== 'surprised' || report.interaction.afterEnter.expr !== 'surprised';
    const reducedFail = report.reduced.reducedAfter.hop || report.reduced.reducedAfter.active || report.reduced.reducedMoved || report.reduced.reducedAfter.expr !== 'surprised';
    console.log(JSON.stringify({
      geoFail, overflowFail, resourceFail, touchFail, keyFail, reducedFail,
      consoleErrors: report.consoleErrors,
      reached: report.interaction.reached,
      afterSpace: report.interaction.afterSpace,
      afterEnter: report.interaction.afterEnter,
      touch390: report.interaction.touch390,
      reducedAfter: report.reduced.reducedAfter,
      reducedMoved: report.reduced.reducedBefore.top !== report.reduced.reducedMid.top,
    }, null, 2));
    ws.close();
    const failed = geoFail || overflowFail || resourceFail || touchFail || keyFail || reducedFail || report.consoleErrors.length;
    process.exitCode = failed ? 1 : 0;
  } finally {
    chrome.kill('SIGKILL');
    server.close();
  }
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
