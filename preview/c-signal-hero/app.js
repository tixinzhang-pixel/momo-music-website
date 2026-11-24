/* No dependencies, no network, no inline SVG. Fixed identity colors live in asset files. */
(()=>{
const reduce=matchMedia('(prefers-reduced-motion: reduce)');
const stage=document.querySelector('.mascot-stage');
if(stage){
 const all=[...stage.querySelectorAll('button.mascot')];
 const order=['note','amp','guitar','drum','pick','mic'];
 const expressions=['happy','surprised','happy','happy','surprised'];
 let cycle=null,reset=null,resume=null,tap=null,turn=0,round=0,visible=true,held=null;
 const sizeTiming=()=>all.forEach(m=>m.style.setProperty('--ts',(.8+.0013*m.offsetWidth).toFixed(3)));
 sizeTiming();
 const shown=()=>order.map(id=>all.find(m=>m.dataset.role===id)).filter(m=>m&&getComputedStyle(m).display!=='none');
 function clear(){all.forEach(m=>{m.classList.remove('is-active','is-hopping');delete m.dataset.expression;});}
 function cancel(){clearTimeout(cycle);clearTimeout(reset);cycle=null;}
 function focus(m,expression='happy',jump=true){
   clear();m.dataset.expression=expression;
   if(!reduce.matches){m.classList.add('is-active');if(jump){void m.offsetWidth;m.classList.add('is-hopping');}}
 }
 function schedule(delay=2400){
   cancel();if(reduce.matches||document.hidden||!visible||held)return;
   cycle=setTimeout(()=>{const ms=shown();if(!ms.length)return;const m=ms[turn++%ms.length];focus(m,expressions[round++%expressions.length]);reset=setTimeout(clear,2100);scheduleNext();},delay);
 }
 function scheduleNext(){if(reduce.matches||document.hidden||!visible||held)return;cycle=setTimeout(()=>{const ms=shown();const m=ms[turn++%ms.length];focus(m,expressions[round++%expressions.length]);reset=setTimeout(clear,2100);scheduleNext();},2400);}
 function enter(m){clearTimeout(resume);clearTimeout(tap);held=m;cancel();focus(m);}
 function leave(){held=null;clear();clearTimeout(tap);clearTimeout(resume);resume=setTimeout(()=>schedule(),1200);}
 for(const m of all){
   m.addEventListener('pointerenter',e=>{if(e.pointerType==='mouse')enter(m);});
   m.addEventListener('pointerleave',e=>{if(e.pointerType==='mouse')leave();});
   m.addEventListener('focus',()=>enter(m));
   m.addEventListener('blur',leave);
   m.addEventListener('click',()=>{cancel();clearTimeout(tap);focus(m,'surprised');tap=setTimeout(()=>{if(held===m){focus(m,'happy',false);}else{clear();schedule();}},900);});
 }
 const obs=new IntersectionObserver(([e])=>{visible=e.isIntersecting;stage.classList.toggle('is-paused',!visible);if(visible)schedule();else{cancel();clear();}},{threshold:.1});obs.observe(stage);
 document.addEventListener('visibilitychange',()=>{stage.classList.toggle('is-paused',document.hidden||!visible);if(document.hidden){cancel();clear();}else schedule();});
 reduce.addEventListener('change',()=>{cancel();clear();schedule();});
 window.addEventListener('resize',()=>{sizeTiming();clear();schedule();});
}
const stations=[...document.querySelectorAll('[data-station]')];
if(stations.length){
 const links=[...document.querySelectorAll('[data-station-link]')];
 let seen=new Set();
 const obs=new IntersectionObserver(entries=>entries.forEach(entry=>{
   if(!entry.isIntersecting)return;
   links.forEach(link=>{if(link.dataset.stationLink===entry.target.dataset.station)link.setAttribute('aria-current','step');else link.removeAttribute('aria-current');});
   if(!seen.has(entry.target)&&!reduce.matches){entry.target.classList.add('reveal-in');seen.add(entry.target);}
 }),{rootMargin:'-10% 0px -30% 0px',threshold:.05});stations.forEach(s=>obs.observe(s));
 const bar=document.querySelector('.reading-progress span');let ticking=false;
 function update(){ticking=false;if(!reduce.matches){const total=document.documentElement.scrollHeight-innerHeight;bar.style.transform=`scaleX(${Math.max(0,Math.min(1,scrollY/(total||1)))})`;}}
 addEventListener('scroll',()=>{if(!ticking){ticking=true;requestAnimationFrame(update);}},{passive:true});update();
}
})();
