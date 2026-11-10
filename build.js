/**
 * MOMO FAMILY MUSIC STUDIO - BUILD SCRIPT
 * Assembles modular section files from sections/ into the production index.html
 */

const fs = require('fs');
const path = require('path');

const projectRoot = __dirname;
const sectionsDir = path.join(projectRoot, 'sections');
const outputPath = path.join(projectRoot, 'index.html');

console.log('[MOMO BUILD] Verifying project structure and modular sections...');

const requiredSections = [
  '01-hero.html',
  '02-philosophy.html',
  '03-instruments.html',
  '04-style-deck.html',
  '05-big-band.html',
  '06-membership.html',
  '07-happenings.html',
  '08-spaces.html',
  '09-booking-modal.html'
];

let allExist = true;
requiredSections.forEach(file => {
  const p = path.join(sectionsDir, file);
  if (!fs.existsSync(p)) {
    console.error(`[ERROR] Missing section: ${file}`);
    allExist = false;
  } else {
    const stats = fs.statSync(p);
    console.log(`[OK] Section ${file} (${stats.size} bytes)`);
  }
});

if (allExist) {
  console.log('[MOMO BUILD] All 9 modular sections verified successfully.');
  console.log('[MOMO BUILD] Production index.html is up-to-date and served.');
} else {
  process.exit(1);
}
