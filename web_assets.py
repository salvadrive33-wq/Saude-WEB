"""Páginas e estilos do sistema, em formato Python. Redesign moderno estilo telemedicina."""

FILES = {}

FILES['theme.css'] = """/* Tema Saude Moderna (Telemedicina & Low-Code) */
:root {
  --bg: #EDF7F5;
  --card: #FFFFFF;
  --ink: #143430;
  --mut: #6A8B86;
  --pri: #00BFA5;
  --pri-dark: #008E7B;
  --pri-light: #E0F7F4;
  --onpri: #FFFFFF;
  --soft: #E6F8F5;
  --acc: #00E5FF;
  --coral: #FF6E6E;
  --line: #D5ECE7;
  --bad: #FF5252;
  --ok: #00C853;
  color-scheme: light;
  box-sizing: border-box;
}
* { box-sizing: border-box; }
html { font-size: 16px; background: var(--bg); }
body {
  margin: 0;
  background: var(--bg);
  color: var(--ink);
  font: 500 1rem/1.5 "Plus Jakarta Sans", system-ui, -apple-system, sans-serif;
  -webkit-tap-highlight-color: transparent;
  min-height: 100vh;
}
button, input, select, textarea { font: inherit; color: inherit; }
input, select, textarea {
  width: 100%;
  min-height: 48px;
  padding: .75rem 1.1rem;
  border: 1.5px solid var(--line);
  border-radius: 16px;
  background: #FFFFFF;
  color: var(--ink);
  transition: all .2s ease;
  box-shadow: 0 2px 6px rgba(0,0,0,.02);
}
input:focus, select:focus, textarea:focus {
  outline: none;
  border-color: var(--pri);
  box-shadow: 0 0 0 3px rgba(0,191,165,.15);
}
input[type=checkbox] {
  width: 1.3rem;
  min-height: 0;
  height: 1.3rem;
  margin: 0 .6rem 0 0;
  vertical-align: middle;
  accent-color: var(--pri);
}
label {
  display: block;
  font-weight: 700;
  margin: 1rem 0 0;
  color: var(--ink);
  font-size: .92rem;
}
label > input, label > select, label > textarea {
  margin-top: .4rem;
  font-weight: 400;
}
label.ck { font-weight: 500; }
:focus-visible { outline: 3px solid var(--pri); outline-offset: 2px; }
h1, h2, h3 {
  line-height: 1.25;
  margin: .3rem 0 .7rem;
  font-weight: 800;
  color: var(--ink);
  letter-spacing: -.02em;
}
h2 { font-size: 1.35rem; }
h3 { font-size: 1.1rem; }
.btn {
  display: block;
  width: 100%;
  min-height: 48px;
  text-align: center;
  text-decoration: none;
  background: var(--pri);
  color: #FFFFFF;
  border: none;
  border-radius: 999px;
  padding: .75rem 1.4rem;
  font-weight: 800;
  font-size: .95rem;
  cursor: pointer;
  margin-top: 1rem;
  box-shadow: 0 6px 20px rgba(0,191,165,.32);
  transition: all .2s ease;
}
.btn:hover {
  background: var(--pri-dark);
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0,191,165,.4);
}
.btn:active { transform: translateY(0); }
.btn.s {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: auto;
  margin: .4rem .4rem 0 0;
  padding: .45rem 1.1rem;
  background: var(--soft);
  color: var(--pri-dark);
  border: none;
  border-radius: 999px;
  font-weight: 700;
  font-size: .84rem;
  min-height: 36px;
  box-shadow: none;
}
.btn.s:hover {
  background: var(--pri);
  color: #FFFFFF;
  box-shadow: 0 4px 12px rgba(0,191,165,.25);
}
.btn:disabled { opacity: .5; cursor: not-allowed; transform: none; box-shadow: none; }
.card {
  background: #FFFFFF;
  border: 1.5px solid var(--line);
  border-radius: 22px;
  padding: 1.2rem;
  margin: 1rem 0;
  box-shadow: 0 6px 20px rgba(0,191,165,.06);
  transition: transform .2s ease, box-shadow .2s ease;
}
.card:hover { box-shadow: 0 8px 24px rgba(0,191,165,.12); }
.card.err { border-color: var(--bad); background: #FFF5F5; }
.mut { color: var(--mut); }
.small { font-size: .84rem; }
.bad { color: var(--bad); font-weight: 700; }
.chip {
  display: inline-flex;
  align-items: center;
  padding: .25rem .8rem;
  border-radius: 999px;
  background: var(--soft);
  border: 1px solid var(--line);
  font-size: .76rem;
  font-weight: 700;
  margin: .25rem .35rem 0 0;
  color: var(--pri-dark);
}
.chip.no { opacity: .65; background: #f1f5f9; border-color: #e2e8f0; color: #64748b; }
.chip.ok { border-color: rgba(0,200,83,.3); color: #008f39; background: rgba(0,200,83,.1); font-weight: 800; }
.load { text-align: center; color: var(--mut); padding: 3rem 0; font-weight: 600; }
table { border-collapse: collapse; width: 100%; font-size: .88rem; }
th, td { text-align: left; padding: .7rem .6rem; border-bottom: 1px solid var(--line); vertical-align: middle; }
th { color: var(--mut); font-weight: 700; text-transform: uppercase; font-size: .74rem; letter-spacing: .04em; }
#toast {
  position: fixed;
  left: 50%;
  bottom: 5.5rem;
  transform: translateX(-50%);
  background: #143430;
  color: #FFFFFF;
  padding: .75rem 1.6rem;
  border-radius: 999px;
  font-weight: 700;
  z-index: 99;
  max-width: 90vw;
  box-shadow: 0 10px 30px rgba(0,0,0,.25);
  font-size: .9rem;
}
#toast[hidden] { display: none; }
"""

FILES['public.css'] = """/* Public layout */
.top-nav {
  max-width: 440px;
  margin: 0 auto;
  padding: 1.1rem 1.3rem .4rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.greet-row {
  display: flex;
  align-items: center;
  gap: 8px;
}
.greeting h2 {
  margin: 0;
  font-size: 1.35rem;
  font-weight: 800;
  color: #143430;
  letter-spacing: -.02em;
  cursor: pointer;
}
.greeting h2:hover {
  color: var(--pri-dark);
}
.btn-edit-name {
  background: rgba(0, 191, 165, 0.12);
  border: none;
  border-radius: 50%;
  width: 30px;
  height: 30px;
  min-width: 30px;
  display: grid;
  place-items: center;
  cursor: pointer;
  font-size: .82rem;
  color: var(--pri-dark);
  transition: all .2s ease;
}
.btn-edit-name:hover {
  background: var(--pri);
  transform: scale(1.1);
}
.greeting p {
  margin: 2px 0 0;
  font-size: .86rem;
  color: var(--mut);
  font-weight: 600;
}
.user-avatar {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  border: 2px solid var(--pri);
  object-fit: cover;
  box-shadow: 0 4px 12px rgba(0,191,165,.25);
  cursor: pointer;
  transition: transform .2s ease;
}
.user-avatar:hover {
  transform: scale(1.05);
}
.sub-top {
  background: linear-gradient(135deg, #00BFA5 0%, #009688 100%);
  color: #FFFFFF;
  text-align: center;
  font-weight: 800;
  font-size: 1.15rem;
  padding: 1.1rem 1rem 1.2rem;
  max-width: 440px;
  margin: 0 auto;
  box-shadow: 0 8px 24px rgba(0,191,165,.2);
  position: relative;
  letter-spacing: -.01em;
}
.sub-top[hidden] { display: none; }
.bk {
  position: absolute;
  left: 1.1rem;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(255,255,255,.22);
  border: 0;
  font-size: 1.5rem;
  line-height: 1;
  color: #FFFFFF;
  width: 38px;
  height: 38px;
  min-width: 38px;
  min-height: 38px;
  border-radius: 50%;
  cursor: pointer;
  display: grid;
  place-items: center;
  transition: all .2s ease;
  backdrop-filter: blur(4px);
}
.bk:hover { background: rgba(255,255,255,.4); }
.hero-illu-wrap {
  max-width: 440px;
  margin: 0 auto;
  padding: .4rem 1.2rem 1.6rem;
  text-align: center;
  position: relative;
}
.hero-illu-wrap[hidden] { display: none; }
.hero-svg {
  width: 100%;
  max-width: 310px;
  height: 135px;
  margin: 0 auto;
  display: block;
}
.shell {
  max-width: 440px;
  margin: -16px auto 0;
  background: #FFFFFF;
  min-height: 85vh;
  padding: 1rem 1.3rem 6.5rem;
  box-shadow: 0 -10px 40px rgba(0,191,165,.08);
  position: relative;
  border-radius: 36px 36px 0 0;
  z-index: 2;
}
.shell.plain {
  margin-top: 0;
  border-radius: 0;
  box-shadow: none;
}
.handle {
  width: 40px;
  height: 5px;
  background: #DCE8E5;
  border-radius: 999px;
  margin: 0 auto 1.1rem;
}
.search-pill {
  position: relative;
  margin-bottom: 1.2rem;
}
.search-pill input {
  width: 100%;
  min-height: 48px;
  padding: .75rem 1.2rem .75rem 2.8rem;
  background: #F4FAF8;
  border: 1.5px solid var(--line);
  border-radius: 999px;
  font-size: .92rem;
  font-weight: 600;
  color: var(--ink);
  box-shadow: 0 4px 16px rgba(0,191,165,.05);
  transition: all .2s ease;
}
.search-pill input:focus {
  outline: none;
  background: #FFFFFF;
  border-color: var(--pri);
  box-shadow: 0 6px 20px rgba(0,191,165,.18);
}
.search-pill svg {
  position: absolute;
  left: 1rem;
  top: 50%;
  transform: translateY(-50%);
  width: 19px;
  height: 19px;
  stroke: var(--pri);
  stroke-width: 2.2;
  fill: none;
}
.tele-alert {
  background: linear-gradient(135deg, #00CBA9 0%, #009688 100%);
  color: #FFFFFF;
  border-radius: 20px;
  padding: 1rem 1.1rem;
  margin-bottom: 1.1rem;
  display: flex;
  align-items: center;
  gap: .85rem;
  box-shadow: 0 8px 24px rgba(0,191,165,.22);
  cursor: pointer;
  transition: transform .2s ease;
}
.tele-alert:hover {
  transform: translateY(-2px);
}
.tele-icon {
  width: 42px;
  height: 42px;
  border-radius: 50%;
  background: rgba(255,255,255,.25);
  display: grid;
  place-items: center;
  flex-shrink: 0;
}
.tele-icon svg {
  width: 22px;
  height: 22px;
  stroke: #FFFFFF;
  stroke-width: 2.2;
  fill: none;
}
.tele-text b { font-size: .94rem; display: block; }
.tele-text p { margin: 2px 0 0; font-size: .8rem; opacity: .92; }
.routine-title {
  text-align: center;
  font-size: 1.18rem;
  font-weight: 800;
  color: var(--ink);
  margin: .2rem 0 .9rem;
  line-height: 1.35;
}
.grid-routine {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: .8rem;
  margin-bottom: 1.2rem;
}
.rt-card {
  position: relative;
  background: #FFFFFF;
  border: 1.5px solid var(--line);
  border-radius: 20px;
  padding: .95rem .95rem .85rem;
  cursor: pointer;
  box-shadow: 0 4px 16px rgba(0,191,165,.05);
  transition: all .2s ease;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  min-height: 105px;
  text-align: left;
}
.rt-card:hover {
  transform: translateY(-3px);
  border-color: var(--pri);
  box-shadow: 0 8px 24px rgba(0,191,165,.14);
}
.rt-btn {
  position: absolute;
  top: .8rem;
  right: .8rem;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: #EEF5FD;
  color: #4A7AFF;
  display: grid;
  place-items: center;
  font-weight: 800;
  font-size: .92rem;
  line-height: 1;
  pointer-events: none;
}
.rt-card b {
  font-size: .95rem;
  color: var(--ink);
  font-weight: 800;
  display: block;
}
.rt-card span.meta {
  font-size: .74rem;
  color: var(--mut);
  display: block;
  margin-top: 2px;
}
.rt-card span.val {
  font-size: .84rem;
  color: #4A7AFF;
  font-weight: 700;
  margin-top: .35rem;
  display: block;
}
.rt-card.highlight {
  background: linear-gradient(135deg, #FF7B7B 0%, #FF5252 100%);
  border-color: transparent;
  color: #FFFFFF;
  box-shadow: 0 8px 24px rgba(255,110,110,.35);
}
.rt-card.highlight b { color: #FFFFFF; }
.rt-card.highlight span.meta { color: rgba(255,255,255,.85); }
.rt-card.highlight span.val { color: #FFFFFF; }
.rt-card.highlight .rt-btn {
  background: rgba(255,255,255,.28);
  color: #FFFFFF;
  font-size: .9rem;
}
.sec-head {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin: 1.3rem 0 .75rem;
}
.sec-head h3 {
  margin: 0;
  font-size: 1.12rem;
  font-weight: 800;
  color: var(--ink);
  letter-spacing: -.01em;
}
.sec-head a, .sec-head span {
  font-size: .8rem;
  font-weight: 700;
  color: var(--pri);
  cursor: pointer;
}
.cat-scroll {
  display: flex;
  gap: .8rem;
  overflow-x: auto;
  scrollbar-width: none;
  padding: .2rem .2rem .5rem;
  margin: 0 -.2rem;
}
.cat-scroll::-webkit-scrollbar { display: none; }
.cat-item {
  flex: 0 0 138px;
  height: 105px;
  border-radius: 18px;
  position: relative;
  overflow: hidden;
  cursor: pointer;
  box-shadow: 0 6px 18px rgba(0,0,0,.08);
  transition: transform .2s ease, box-shadow .2s ease;
}
.cat-item:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 24px rgba(0,0,0,.15);
}
.cat-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform .3s ease;
}
.cat-item:hover img { transform: scale(1.05); }
.cat-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, rgba(20,52,48,.15) 0%, rgba(20,52,48,.75) 100%);
  display: flex;
  align-items: flex-end;
  padding: .7rem .8rem;
}
.cat-overlay span {
  color: #FFFFFF;
  font-weight: 800;
  font-size: .88rem;
  text-shadow: 0 2px 4px rgba(0,0,0,.4);
}
.doc-card {
  background: #FFFFFF;
  border: 1.5px solid var(--line);
  border-radius: 20px;
  padding: .95rem 1.05rem;
  margin-bottom: .8rem;
  display: flex;
  align-items: center;
  gap: .95rem;
  box-shadow: 0 4px 16px rgba(0,191,165,.06);
  cursor: pointer;
  transition: all .2s ease;
}
.doc-card:hover {
  transform: translateY(-2px);
  border-color: var(--pri);
  box-shadow: 0 8px 24px rgba(0,191,165,.14);
}
.doc-pic {
  width: 54px;
  height: 54px;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid #E0F7F4;
  flex-shrink: 0;
}
.doc-info { flex: 1; min-width: 0; }
.doc-info b {
  font-size: .98rem;
  color: var(--ink);
  font-weight: 800;
  display: block;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.doc-info span.spec {
  display: inline-block;
  font-size: .76rem;
  font-weight: 700;
  color: var(--pri-dark);
  background: var(--soft);
  padding: 2px 8px;
  border-radius: 999px;
  margin-top: 3px;
}
.doc-info .rating {
  font-size: .76rem;
  color: var(--mut);
  margin-top: 3px;
  font-weight: 600;
}
.doc-info .rating b { display: inline; color: #FFB300; }
.doc-btn {
  background: var(--pri);
  color: #FFFFFF;
  border: 0;
  border-radius: 999px;
  padding: .45rem .95rem;
  font-weight: 800;
  font-size: .8rem;
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(0,191,165,.3);
  transition: all .2s ease;
  white-space: nowrap;
}
.doc-btn:hover {
  background: var(--pri-dark);
  transform: translateY(-1px);
}
.net {
  background: #FFE082;
  color: #6A4B00;
  text-align: center;
  font-weight: 800;
  padding: .6rem;
  font-size: .85rem;
  border-radius: 14px;
  max-width: 440px;
  margin: .8rem auto 0;
}
.tabs {
  position: fixed;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 100%;
  max-width: 440px;
  z-index: 50;
  display: flex;
  justify-content: space-around;
  background: rgba(255,255,255,.98);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-top: 1.5px solid var(--line);
  padding: .55rem .8rem calc(env(safe-area-inset-bottom,0px) + .4rem);
  box-shadow: 0 -8px 30px rgba(0,191,165,.1);
}
.tabs button {
  flex: 1;
  background: none;
  border: 0;
  color: #9DBEB8;
  padding: .35rem .2rem;
  font-size: .74rem;
  font-weight: 700;
  cursor: pointer;
  min-height: 52px;
  transition: all .2s ease;
  position: relative;
}
.tabs svg {
  display: block;
  margin: 0 auto 3px;
  width: 23px;
  height: 23px;
  fill: none;
  stroke: currentColor;
  stroke-width: 2.2;
}
.tabs .on { color: var(--pri); font-weight: 800; }
.tabs .on svg { stroke: var(--pri); transform: translateY(-2px); }
.tabs .on::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 5px;
  height: 5px;
  background: var(--pri);
  border-radius: 50%;
}
.slots { display: flex; flex-wrap: wrap; gap: .6rem; margin-top: .7rem; }
.slot {
  min-width: 82px;
  min-height: 44px;
  border: 1.5px solid var(--line);
  background: #FFFFFF;
  color: var(--ink);
  border-radius: 999px;
  font-weight: 700;
  font-size: .9rem;
  cursor: pointer;
  transition: all .2s ease;
}
.slot:hover { border-color: var(--pri); color: var(--pri-dark); background: var(--soft); }
.slot.on { background: var(--pri); border-color: var(--pri); color: #fff; box-shadow: 0 4px 14px rgba(0,191,165,.35); font-weight: 800; }
#map {
  height: 50vh;
  min-height: 300px;
  border-radius: 22px;
  border: 1.5px solid var(--line);
  margin-top: .8rem;
  background: var(--soft);
  box-shadow: 0 4px 14px rgba(0,191,165,.08);
  overflow: hidden;
}
.pin {
  background: var(--pri);
  color: #fff;
  border: 3px solid #fff;
  border-radius: 50%;
  font-weight: 800;
  display: grid;
  place-items: center;
  width: 32px!important;
  height: 32px!important;
  box-shadow: 0 4px 12px rgba(0,0,0,.2);
}
.ok-big { font-size: 3.5rem; color: var(--ok); text-align: center; }
.code {
  font-size: 2.2rem;
  font-weight: 800;
  letter-spacing: .25em;
  text-align: center;
  background: var(--soft);
  color: var(--pri-dark);
  border-radius: 18px;
  padding: .8rem;
  margin: .6rem 0;
  border: 1.5px dashed var(--pri);
}
.demo {
  background: var(--soft);
  border: 1.5px solid var(--line);
  color: var(--pri-dark);
  border-radius: 18px;
  padding: .85rem 1.1rem;
  font-weight: 700;
  text-align: center;
  margin: .6rem 0;
  font-size: .86rem;
}
.cols { display: grid; gap: 1rem; }
"""

FILES['public.html'] = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Saúde Ibiassucê</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/static/theme.css">
<link rel="stylesheet" href="/static/public.css">
</head>
<body>

<header class="top-nav" id="top-nav">
  <div class="greeting">
    <div class="greet-row">
      <h2 id="greet-name" title="Clique para editar seu nome">Olá, Denis H! 👋</h2>
      <button id="btn-edit-name" class="btn-edit-name" title="Editar seu nome" aria-label="Editar seu nome">✏️</button>
    </div>
    <p>Saúde Ibiassucê · Telemedicina</p>
  </div>
  <img id="user-avatar" src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=120&q=80" alt="Avatar" class="user-avatar" title="Seu perfil">
</header>

<header class="sub-top" id="sub-top" hidden>
  <button id="back" class="bk" data-act="back" aria-label="Voltar">&#8249;</button>
  <span id="title">Home</span>
</header>

<div class="hero-illu-wrap" id="hero-wrap">
  <svg class="hero-svg" viewBox="0 0 320 145" fill="none" xmlns="http://www.w3.org/2000/svg">
    <circle cx="160" cy="72" r="65" fill="#FFE5E5" opacity="0.65"/>
    <circle cx="70" cy="45" r="22" fill="#E8F8F5" opacity="0.8"/>
    <circle cx="260" cy="110" r="28" fill="#E0F7F4" opacity="0.7"/>
    <!-- Ampulheta -->
    <g transform="translate(30, 48)">
      <rect x="2" y="0" width="32" height="5" rx="2.5" fill="#FFA3A3"/>
      <rect x="2" y="55" width="32" height="5" rx="2.5" fill="#FFA3A3"/>
      <path d="M6 5 L18 30 L6 55 M30 5 L18 30 L30 55" stroke="#FFA3A3" stroke-width="2.5" stroke-linecap="round"/>
      <path d="M12 42 L24 42 L18 32 Z" fill="#FF8080"/>
      <path d="M14 18 L22 18 L18 24 Z" fill="#FF8080"/>
    </g>
    <!-- Calendario -->
    <g transform="translate(85, 32)">
      <rect x="0" y="0" width="105" height="85" rx="16" fill="#FFFFFF" stroke="#FFA8A8" stroke-width="2.5"/>
      <rect x="0" y="0" width="105" height="24" rx="16" fill="#FF7B7B"/>
      <circle cx="20" cy="12" r="3.5" fill="#FFFFFF"/><circle cx="42" cy="12" r="3.5" fill="#FFFFFF"/><circle cx="64" cy="12" r="3.5" fill="#FFFFFF"/><circle cx="86" cy="12" r="3.5" fill="#FFFFFF"/>
      <circle cx="20" cy="40" r="4" fill="#FFE0E0"/><circle cx="42" cy="40" r="4" fill="#FFE0E0"/><circle cx="64" cy="40" r="4" fill="#FFE0E0"/><circle cx="86" cy="40" r="4" fill="#FFE0E0"/>
      <circle cx="20" cy="58" r="4" fill="#FFE0E0"/><rect x="34" y="50" width="16" height="16" rx="5" fill="#00BFA5"/><circle cx="64" cy="58" r="4" fill="#FFE0E0"/><circle cx="86" cy="58" r="4" fill="#FFE0E0"/>
      <circle cx="20" cy="74" r="4" fill="#FFE0E0"/><circle cx="42" cy="74" r="4" fill="#FFE0E0"/><circle cx="64" cy="74" r="4" fill="#FF8080"/><circle cx="86" cy="74" r="4" fill="#FFE0E0"/>
    </g>
    <!-- Relogio com ponteiros -->
    <g transform="translate(200, 36)">
      <path d="M18 10 C18 4, 30 4, 30 10 Z" fill="#00BFA5"/>
      <circle cx="42" cy="52" r="42" fill="#FFFFFF" stroke="#FF5252" stroke-width="4"/>
      <line x1="22" y1="90" x2="14" y2="102" stroke="#143430" stroke-width="3.5" stroke-linecap="round"/>
      <line x1="62" y1="90" x2="70" y2="102" stroke="#143430" stroke-width="3.5" stroke-linecap="round"/>
      <circle cx="42" cy="52" r="4" fill="#FF5252"/>
      <line x1="42" y1="52" x2="42" y2="26" stroke="#143430" stroke-width="3.5" stroke-linecap="round"/>
      <line x1="42" y1="52" x2="62" y2="58" stroke="#143430" stroke-width="3.5" stroke-linecap="round"/>
      <path d="M42 0 C40 10, 48 18, 56 12 C60 10, 60 5, 52 0 Z" fill="#FFF0F0"/>
    </g>
  </svg>
</div>

<div id="net" class="net" role="status" hidden>Conectando ao servidor… na primeira vez pode levar até 1 minuto.</div>
<main id="main" class="shell"></main>
<nav id="tabs" class="tabs" aria-label="Navegação"></nav>
<div id="toast" role="status" hidden></div>
<script src="/static/public.js"></script>
</body>
</html>
"""

FILES['public.js'] = """/* Interface pública moderna estilo telemedicina. Conectada com a API Flask. */
const $ = s => document.querySelector(s);
const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const DIAS = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom'];

const DOC_AVATARS = [
  'https://images.unsplash.com/photo-1559839734-2b71ea197ec2?auto=format&fit=crop&w=200&q=80',
  'https://images.unsplash.com/photo-1622253692010-333f2da6031d?auto=format&fit=crop&w=200&q=80',
  'https://images.unsplash.com/photo-1594824813504-7b70bc9bb3a6?auto=format&fit=crop&w=200&q=80',
  'https://images.unsplash.com/photo-1537368910025-700350fe46c7?auto=format&fit=crop&w=200&q=80',
  'https://images.unsplash.com/photo-1582750433449-648ed127bb54?auto=format&fit=crop&w=200&q=80'
];
const docPic = id => DOC_AVATARS[(id || 0) % DOC_AVATARS.length];

const CATS = [
  { name: 'Odontologia', img: 'https://images.unsplash.com/photo-1588776814546-1ffcf47267a5?auto=format&fit=crop&w=300&q=80' },
  { name: 'Clínica Geral', img: 'https://images.unsplash.com/photo-1579684385127-1ef15d508118?auto=format&fit=crop&w=300&q=80' },
  { name: 'Pediatria', img: 'https://images.unsplash.com/photo-1631815589968-fdb09a223b1e?auto=format&fit=crop&w=300&q=80' },
  { name: 'Dermatologia', img: 'https://images.unsplash.com/photo-1666214280557-f1b5022eb634?auto=format&fit=crop&w=300&q=80' }
];

const IC = {
  home: '<path d="M4 11l8-6 8 6v9H4z"/><path d="M12 17s-3-2-3-4a1.7 1.7 0 013-.5 1.7 1.7 0 013 .5c0 2-3 4-3 4z"/>',
  servicos: [6, 12, 18].flatMap(y => [6, 12, 18].map(x => `<circle cx="${x}" cy="${y}" r="1.6"/>`)).join(''),
  avisos: '<path d="M6 17v-6a6 6 0 0112 0v6l1.5 2h-15z"/><path d="M10 21h4"/>',
  ajustes: '<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/>',
  pin: '<path d="M12 21s-6-5.5-6-11a6 6 0 0112 0c0 5.5-6 11-6 11z"/><circle cx="12" cy="10" r="2"/>',
  cal: '<rect x="4" y="5" width="16" height="15" rx="2"/><path d="M4 10h16M9 3v4M15 3v4"/>',
  doc: '<circle cx="12" cy="7" r="3.5"/><path d="M5 21c0-4 3-6 7-6s7 2 7 6M10 15v3M14 15v3"/>',
  map: '<path d="M3 6l6-2 6 2 6-2v14l-6 2-6-2-6 2z"/><path d="M9 4v14M15 6v14"/>',
  acc: '<circle cx="12" cy="5" r="2"/><path d="M5 9h14M12 9v6l-3 6M12 15l3 6"/>',
};
const ico = k => `<svg viewBox="0 0 24 24" aria-hidden="true">${IC[k]}</svg>`;
const TABS = [['home', 'Home'], ['servicos', 'Serviços'], ['avisos', 'Avisos'], ['ajustes', 'Ajustes']];
const cache = {}, st = { book: {}, filter: {}, prefs: { hc: false, fs: 16, userName: 'Denis H' } };

async function api(path, opt = {}) {
  const slow = setTimeout(() => { $('#net').hidden = false; }, 4000);
  const ctl = new AbortController(), to = setTimeout(() => ctl.abort(), 70000);
  try {
    const r = await fetch(path, { signal: ctl.signal, headers: { 'Content-Type': 'application/json' }, ...opt });
    const j = await r.json().catch(() => ({}));
    if (!r.ok) throw new Error(j.error || 'Erro inesperado.');
    return j;
  } catch (e) {
    if (e.name === 'AbortError') throw new Error('O servidor demorou demais. Tente novamente.');
    if (e instanceof TypeError) throw new Error('Sem conexão com o servidor.');
    throw e;
  } finally { clearTimeout(slow); clearTimeout(to); $('#net').hidden = true; }
}
const get = async k => cache[k] || (cache[k] = await api('/api/' + k));
const say = t => { try { speechSynthesis.cancel(); const u = new SpeechSynthesisUtterance(t); u.lang = 'pt-BR'; speechSynthesis.speak(u); } catch (e) { } };
function toast(t) { const e = $('#toast'); e.textContent = t; e.hidden = false; clearTimeout(toast.t); toast.t = setTimeout(() => e.hidden = true, 3500); }
const fd = d => d.split('-').reverse().join('/');
const today = () => new Date(Date.now() - new Date().getTimezoneOffset() * 6e4).toISOString().slice(0, 10);
const setMain = h => { $('#main').innerHTML = h; };

function loadPrefs() {
  try {
    Object.assign(st.prefs, JSON.parse(localStorage.getItem('prefs') || '{}'));
    const savedName = localStorage.getItem('userName');
    if (savedName) st.prefs.userName = savedName;
  } catch (e) { }
  applyPrefs();
}

function applyPrefs() {
  document.documentElement.classList.toggle('hc', !!st.prefs.hc);
  document.documentElement.style.fontSize = (st.prefs.fs || 16) + 'px';
  const gn = $('#greet-name');
  if (gn) gn.textContent = `Olá, ${st.prefs.userName || 'Visitante'}! 👋`;
  try {
    localStorage.setItem('prefs', JSON.stringify({ hc: st.prefs.hc, fs: st.prefs.fs }));
    localStorage.setItem('userName', st.prefs.userName || 'Denis H');
  } catch (e) { }
}

function setUserName(name) {
  const n = (name || '').trim();
  if (!n) return;
  st.prefs.userName = n;
  applyPrefs();
  toast(`Nome atualizado para "${n}"!`);
}

function promptEditName() {
  const current = st.prefs.userName || 'Denis H';
  const n = prompt('Como você gostaria de ser chamado no aplicativo?', current);
  if (n && n.trim() && n.trim() !== current) {
    setUserName(n.trim());
  }
}

const accChips = u => [['ramp', 'Rampa'], ['wc', 'Banheiro adaptado'], ['libras', 'Intérprete de Libras']]
  .map(([k, l]) => `<span class="chip ${u[k] ? '' : 'no'}">${u[k] ? '' : 'Sem '}${l}</span>`).join('');

const availText = u => {
  const by = {}; (u.availabilities || []).forEach(a => (by[a.weekday] = by[a.weekday] || []).push(`${a.starts}–${a.ends}`));
  return Object.keys(by).map(w => `${DIAS[w]} ${by[w].join(', ')}`).join(' · ') || 'Sem horários cadastrados';
};

const unitCard = u => `<article class="card">
  <div style="display:flex;justify-content:space-between;align-items:start">
    <div>
      <h3 style="margin:0 0 .2rem">${esc(u.name)}</h3>
      <span class="chip">${esc(u.type)}</span>
    </div>
  </div>
  <p style="margin:.6rem 0 .4rem">${esc(u.address)}<br><span class="mut small">${esc(u.hours || '')}</span></p>
  <p class="small">${esc(u.services || '')}</p>
  ${accChips(u)}<br>
  ${u.lat != null ? `<a class="btn s" target="_blank" rel="noopener" href="https://www.google.com/maps/search/?api=1&query=${u.lat},${u.lng}">Como chegar</a>` : ''}
  <button class="btn s" data-act="units-doctors" data-unit="${u.id}">Médicos</button>
  <button class="btn s" data-act="book-unit" data-unit="${u.id}">Agendar</button>
  <button class="btn s" data-act="say" data-t="${esc(`${u.name}. ${u.type}. Endereço: ${u.address}.`)}">Ouvir</button>
</article>`;

const docCard = (d, i) => {
  const uId = (d.units && d.units[0]) ? d.units[0].unit_id : '';
  const uName = (d.units && d.units[0]) ? d.units[0].unit_name : 'Ibiassucê';
  return `
  <div class="doc-card" data-act="book-doc" data-doc="${d.id}" data-unit="${uId}">
    <img src="${docPic(d.id || i)}" alt="${esc(d.name)}" class="doc-pic">
    <div class="doc-info">
      <b>${esc(d.name)}</b>
      <span class="spec">${esc(d.specialty)}</span>
      <div class="rating"><b>★ 4.9</b> · ${esc(uName)}</div>
    </div>
    <button class="doc-btn" data-act="book-doc" data-doc="${d.id}" data-unit="${uId}">Agendar</button>
  </div>`;
};

/* ---------- TELAS ---------- */
async function vHome() {
  const [camps, units, docs] = await Promise.all([get('campaigns'), get('units'), get('doctors')]);
  const uCount = units.filter(u => u.active !== 0).length || 3;
  const dCount = docs.filter(d => d.active !== 0).length || 4;

  const html = `
  <div class="handle"></div>

  <!-- Barra de Busca Flutuante -->
  <div class="search-pill">
    <svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><line x1="16.5" y1="16.5" x2="21" y2="21"/></svg>
    <input id="home-q" type="search" placeholder="Buscar médico, especialidade ou posto...">
  </div>

  <!-- Próximo Atendimento / Telemedicina -->
  <div class="tele-alert" data-go="agendar">
    <div class="tele-icon">
      <svg viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 16.92z"/></svg>
    </div>
    <div class="tele-text">
      <b>Como está sua saúde hoje?</b>
      <p>Agende sua consulta ou confira a presença médica em Ibiassucê</p>
    </div>
  </div>

  <!-- Titulo de Rotina e Atividades -->
  <div class="routine-title">Acompanhe seus horários<br>e atendimentos de saúde</div>

  <!-- Grid 2x2 com + e card Coral com ✓ -->
  <div class="grid-routine">
    <div class="rt-card" data-go="unidades">
      <div class="rt-btn">+</div>
      <div>
        <b>Unidades</b>
        <span class="meta">Postos & UBS</span>
      </div>
      <span class="val">${uCount} ativas hoje</span>
    </div>

    <div class="rt-card" data-go="medicos">
      <div class="rt-btn">+</div>
      <div>
        <b>Médicos</b>
        <span class="meta">Especialistas</span>
      </div>
      <span class="val">${dCount} disponíveis</span>
    </div>

    <div class="rt-card" data-go="avisos">
      <div class="rt-btn">+</div>
      <div>
        <b>Campanhas</b>
        <span class="meta">Vacinação</span>
      </div>
      <span class="val">Gripe & Dengue</span>
    </div>

    <div class="rt-card highlight" data-go="agendar">
      <div class="rt-btn">✓</div>
      <div>
        <b>Agendamento</b>
        <span class="meta">Demonstração</span>
      </div>
      <span class="val">Marcar agora</span>
    </div>
  </div>

  <!-- Seção Categorias com Fotos -->
  <div class="sec-head">
    <h3>Categorias</h3>
    <span data-go="medicos">Ver todas</span>
  </div>
  <div class="cat-scroll">
    ${CATS.map(c => `
      <div class="cat-item" data-cat="${esc(c.name)}">
        <img src="${c.img}" alt="${esc(c.name)}">
        <div class="cat-overlay"><span>${esc(c.name)}</span></div>
      </div>
    `).join('')}
  </div>

  <!-- Seção Médicos em Destaque -->
  <div class="sec-head">
    <h3>Médicos em Destaque</h3>
    <span data-go="medicos">Filtrar</span>
  </div>
  <div id="home-docs">
    ${docs.slice(0, 4).map(docCard).join('') || '<p style="text-align:center;padding:1rem;color:var(--mut)">Carregando médicos...</p>'}
  </div>

  <div style="background:#F0FAF8;border:1.5px dashed var(--pri);border-radius:20px;padding:1rem 1.1rem;margin-top:1.2rem;text-align:center;">
    <b style="color:var(--pri-dark);font-size:.92rem">🔬 Demonstração Feira de Ciências</b>
    <p style="margin:4px 0 0;font-size:.82rem;color:var(--mut)">Sistema de autoatendimento e telemedicina para postos de saúde de Ibiassucê.</p>
  </div>
  `;

  setMain(html);

  $('#home-q').oninput = e => {
    const q = e.target.value.toLowerCase().trim();
    if (!q) {
      $('#home-docs').innerHTML = docs.slice(0, 4).map(docCard).join('');
      return;
    }
    const matchedDocs = docs.filter(d => (d.name + ' ' + d.specialty).toLowerCase().includes(q));
    const matchedUnits = units.filter(u => (u.name + ' ' + u.address + ' ' + u.type + ' ' + (u.services || '')).toLowerCase().includes(q));
    
    let res = '';
    if (matchedDocs.length) {
      res += matchedDocs.map(docCard).join('');
    }
    if (matchedUnits.length) {
      res += '<div style="margin-top:1rem"><b>Unidades encontradas:</b></div>' + matchedUnits.map(unitCard).join('');
    }
    if (!matchedDocs.length && !matchedUnits.length) {
      res = '<p style="text-align:center;color:var(--mut);padding:1.5rem">Nenhum médico ou posto encontrado com essa busca.</p>';
    }
    $('#home-docs').innerHTML = res;
  };
}

async function vServ() {
  const camps = await get('campaigns');
  setMain(`
  <div class="routine-title">Serviços & Atendimentos</div>
  <div class="grid-routine">
    <div class="rt-card" data-go="unidades">
      <div class="rt-btn">+</div>
      <div><b>Unidades de saúde</b><span class="meta">Postos e horários</span></div>
      <span class="val">Ver lista</span>
    </div>
    <div class="rt-card" data-go="medicos">
      <div class="rt-btn">+</div>
      <div><b>Médicos e escalas</b><span class="meta">Presença e plantão</span></div>
      <span class="val">Ver médicos</span>
    </div>
    <div class="rt-card" data-go="mapa">
      <div class="rt-btn">+</div>
      <div><b>Mapa das unidades</b><span class="meta">Localização e rotas</span></div>
      <span class="val">Abrir mapa</span>
    </div>
    <div class="rt-card highlight" data-go="agendar">
      <div class="rt-btn">✓</div>
      <div><b>Agendar consulta</b><span class="meta">Fila interativa</span></div>
      <span class="val">Agendar</span>
    </div>
    <div class="rt-card" data-go="avisos">
      <div class="rt-btn">+</div>
      <div><b>Campanhas</b><span class="meta">Vacinação e avisos</span></div>
      <span class="val">Ver avisos</span>
    </div>
    <div class="rt-card" data-go="ajustes">
      <div class="rt-btn">+</div>
      <div><b>Acessibilidade</b><span class="meta">Voz e perfil</span></div>
      <span class="val">Configurar</span>
    </div>
  </div>`);
}

async function vUnits() {
  const units = await get('units');
  const list = q => units.filter(u => (u.name + u.address + (u.services || '') + u.type).toLowerCase().includes(q.toLowerCase()));
  setMain(`<div class="search-pill"><svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><line x1="16.5" y1="16.5" x2="21" y2="21"/></svg><input id="q" type="search" placeholder="Buscar por posto, endereço ou serviço"></div><div id="ul" class="cols" style="margin-top:.8rem">${units.map(unitCard).join('') || '<p>Nenhuma unidade cadastrada.</p>'}</div>`);
  $('#q').oninput = e => { const l = list(e.target.value); $('#ul').innerHTML = l.map(unitCard).join('') || '<p>Nenhuma unidade encontrada.</p>'; };
}

const CDN = 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/';
const loadLeaflet = () => new Promise((ok, no) => {
  if (window.L) return ok();
  const l = document.createElement('link'); l.rel = 'stylesheet'; l.href = CDN + 'leaflet.css'; document.head.appendChild(l);
  const s = document.createElement('script'); s.src = CDN + 'leaflet.js'; s.onload = ok; s.onerror = () => no(new Error('Não foi possível carregar o mapa. Verifique a internet; a lista continua disponível.')); document.head.appendChild(s);
});

async function vMap() {
  const units = (await get('units')).filter(u => u.lat != null && u.lng != null);
  setMain(`<div id="map" role="application" aria-label="Mapa das unidades"></div><div id="ml" style="margin-top:.8rem">${units.map((u, i) => `<button class="btn s" data-act="fly" data-i="${i}">${i + 1}. ${esc(u.name)}</button>`).join('')}</div>`);
  if (!units.length) { $('#map').innerHTML = '<p class="load">Nenhuma unidade com localização cadastrada.</p>'; return; }
  try {
    await loadLeaflet();
    const m = L.map('map'); st.map = m; st.mapUnits = units;
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', { maxZoom: 19, attribution: '&copy; OpenStreetMap' }).addTo(m);
    units.forEach((u, i) => L.marker([u.lat, u.lng], { icon: L.divIcon({ className: '', html: `<div class="pin">${i + 1}</div>`, iconSize: [30, 30] }) })
      .addTo(m).bindPopup(`<b>${esc(u.name)}</b><br>${esc(u.address)}`));
    m.fitBounds(units.map(u => [u.lat, u.lng]), { padding: [40, 40], maxZoom: 16 });
  } catch (e) { $('#map').innerHTML = `<p class="load bad">${esc(e.message)}</p>`; }
}

async function vDocs() {
  const [docs, units, specs] = await Promise.all([get('doctors'), get('units'), get('specialties')]);
  const f = st.filter || (st.filter = {});
  const shown = docs.filter(d => (!f.unit || d.units.some(u => u.unit_id == f.unit)) && (!f.spec || d.specialty_id == f.spec));

  setMain(`
  <div class="cols">
    <label>Unidade<select data-f="unit"><option value="">Todas as unidades</option>${units.map(u => `<option value="${u.id}" ${f.unit == u.id ? 'selected' : ''}>${esc(u.name)}</option>`).join('')}</select></label>
    <label>Especialidade<select data-f="spec"><option value="">Todas as especialidades</option>${specs.map(s => `<option value="${s.id}" ${f.spec == s.id ? 'selected' : ''}>${esc(s.name)}</option>`).join('')}</select></label>
  </div>
  <div class="cols" style="margin-top:.9rem">
    ${shown.map((d, i) => `
      <article class="card">
        <div style="display:flex;align-items:center;gap:.9rem;margin-bottom:.8rem">
          <img src="${docPic(d.id || i)}" alt="${esc(d.name)}" class="doc-pic">
          <div class="doc-info">
            <h3 style="margin:0">${esc(d.name)}</h3>
            <span class="spec">${esc(d.specialty)}</span>
            <div class="rating"><b>★ 4.9</b> · Atendimento SUS</div>
          </div>
        </div>
        ${d.units.map(u => `
          <div style="background:var(--soft);border-radius:14px;padding:.7rem;margin-top:.5rem">
            <b>${esc(u.unit_name)}</b><br>
            <span class="small">${availText(u)}</span><br>
            ${u.presence_today ? '<span class="chip ok" style="margin:.3rem 0">✓ Presença confirmada hoje</span>' : '<span class="chip no" style="margin:.3rem 0">Horário cadastrado</span>'}<br>
            <button class="btn s" data-act="book-doc" data-unit="${u.unit_id}" data-doc="${d.id}">Agendar com este médico</button>
          </div>
        `).join('') || '<p class="mut">Sem unidade vinculada.</p>'}
      </article>
    `).join('') || '<p style="text-align:center;padding:2rem;color:var(--mut)">Nenhum médico encontrado com esse filtro.<br><button class="btn s" data-act="clear-filter" style="margin-top:.8rem">Limpar filtros</button></p>'}
  </div>`);
}

async function vBook() {
  const [units, docs] = await Promise.all([get('units'), get('doctors')]);
  const b = st.book;
  
  if (b.doc && !b.unit) {
    const docObj = docs.find(d => d.id == b.doc);
    if (docObj && docObj.units && docObj.units.length) {
      b.unit = String(docObj.units[0].unit_id);
    }
  }

  const dl = docs.filter(d => !b.unit || d.units.some(u => u.unit_id == b.unit));
  const doc = docs.find(d => d.id == b.doc);
  
  let slots = null, msg = '';
  if (doc && b.unit && b.day) {
    slots = await api(`/api/slots?doctor_id=${b.doc}&unit_id=${b.unit}&day=${b.day}`);
    if (!slots.length) {
      const uAvail = doc.units.find(u => u.unit_id == b.unit);
      msg = `Sem horários livres neste dia. Atendimento: ${availText(uAvail || doc.units[0] || {})}.`;
    }
  }
  
  const opt = (a, sel, fn) => a.map(x => `<option value="${x.id}" ${x.id == sel ? 'selected' : ''}>${esc(fn(x))}</option>`).join('');

  setMain(`
  <div class="demo">🔬 Agendamento de demonstração da Feira de Ciências</div>
  <label>1. Unidade de Saúde<select data-b="unit"><option value="">Escolha a unidade</option>${opt(units, b.unit, u => u.name)}</select></label>
  ${b.unit ? `<label>2. Médico Especialista<select data-b="doc"><option value="">Escolha o médico</option>${opt(dl, b.doc, d => `${d.specialty} — ${d.name}`)}</select></label>${dl.length ? '' : '<p class="mut">Nenhum médico disponível nesta unidade.</p>'}` : ''}
  ${doc && b.unit ? `<label>3. Data da consulta<input type="date" data-b="day" min="${today()}" value="${b.day || ''}"></label>` : ''}
  ${msg ? `<p class="bad" role="alert" style="margin-top:.6rem">${esc(msg)}</p>` : ''}
  ${slots && slots.length ? `
    <label>4. Horário disponível</label>
    <div class="slots">${slots.map(s => `<button class="slot ${s === b.slot ? 'on' : ''}" data-act="slot" data-v="${s}">${s}</button>`).join('')}</div>
    <label>5. Seu nome<input id="pn" maxlength="80" autocomplete="off" value="${esc(b.name || st.prefs.userName || 'Denis H')}"></label>
    <button class="btn" data-act="confirm">Confirmar agendamento</button>` : ''}
  `);
}

async function vDone() {
  const r = st.done; if (!r) { location.hash = '#/agendar'; return; }
  setMain(`<div class="card"><div class="ok-big" aria-hidden="true">&#10003;</div><h2 style="text-align:center">Agendamento confirmado</h2><div class="code" aria-label="Código">${esc(r.code)}</div>
  <p style="text-align:center"><b>${fd(r.day)} às ${esc(r.slot)}</b><br>${esc(r.specialty)} com ${esc(r.doctor)}<br><span class="mut">${esc(r.unit)}</span></p>
  <p style="text-align:center;font-size:.9rem;color:var(--pri-dark)">Paciente: <b>${esc(r.patient_name || st.prefs.userName || 'Denis H')}</b></p>
  <div class="demo">Demonstração da Feira: consulta fictícia interativa.</div>
  <button class="btn" data-act="new-book">Fazer outro agendamento</button></div>`);
}

async function vNews() {
  const c = await get('campaigns');
  setMain(c.map(x => `<article class="card"><h3>${esc(x.title)}</h3>${x.day ? `<span class="mut small">${fd(x.day)}</span>` : ''}<p>${esc(x.body)}</p>
  <button class="btn s" data-act="say" data-t="${esc(x.title + '. ' + x.body)}">Ouvir</button></article>`).join('') || '<p class="load">Nenhum aviso por enquanto.</p>');
}

async function vSet() {
  setMain(`
  <h2>Perfil & Personalização</h2>
  <div class="card">
    <label>Como prefere ser chamado?
      <input id="pref_username" maxlength="50" value="${esc(st.prefs.userName || 'Denis H')}" placeholder="Digite seu nome">
    </label>
    <button class="btn s" data-act="save-pref-name" style="margin-top:.8rem">Salvar nome</button>
  </div>

  <h2>Acessibilidade</h2>
  <div class="card">
    <label class="ck"><input type="checkbox" data-p="hc" ${st.prefs.hc ? 'checked' : ''}>Modo de alto contraste</label>
    <p style="margin:.8rem 0 .4rem"><b>Tamanho do texto</b></p>
    <button class="btn s" data-act="fs-" aria-label="Diminuir texto">A−</button>
    <button class="btn s" data-act="fs+" aria-label="Aumentar texto">A+</button>
    <br><br>
    <button class="btn s" data-act="say-screen">Ouvir esta tela</button>
    <button class="btn s" data-act="stop">Parar leitura</button>
  </div>

  <h2>Conexão</h2>
  <div class="card">
    <p class="mut">Verifique se o servidor e o banco de dados estão respondendo em tempo real.</p>
    <button class="btn s" data-act="health">Testar conexão</button>
    <p id="hs" role="status" style="margin-top:.6rem"></p>
  </div>`);
}

/* ---------- AÇÕES ---------- */
async function confirmBook() {
  const b = st.book, name = ($('#pn').value || '').trim(); b.name = name;
  if (name.length < 2) { toast('Digite um nome com pelo menos 2 letras.'); return; }
  if (!b.slot) { toast('Escolha um horário.'); return; }
  const btn = $('[data-act=confirm]'); btn.disabled = true; btn.textContent = 'Agendando…';
  try {
    st.done = await api('/api/appointments', { method: 'POST', body: JSON.stringify({ doctor_id: +b.doc, unit_id: +b.unit, day: b.day, slot: b.slot, patient_name: name }) });
    st.done.patient_name = name;
    st.book = {}; location.hash = '#/confirmacao';
  } catch (e) { toast(e.message); b.slot = ''; await vBook(); }
}

const ACT = {
  back: () => history.length > 1 ? history.back() : (location.hash = '#/home'),
  retry: () => route(),
  say: el => say(el.dataset.t),
  'say-screen': () => say($('#main').innerText),
  stop: () => speechSynthesis.cancel(),
  'units-doctors': el => { st.filter = { unit: el.dataset.unit }; location.hash = '#/medicos'; },
  'book-unit': el => { st.book = { unit: el.dataset.unit }; location.hash = '#/agendar'; },
  'book-doc': el => { st.book = { unit: el.dataset.unit || '', doc: el.dataset.doc }; location.hash = '#/agendar'; },
  'new-book': () => { st.done = null; st.book = {}; location.hash = '#/agendar'; },
  'clear-filter': () => { st.filter = {}; vDocs().catch(showErr); },
  'save-pref-name': () => { const inp = $('#pref_username'); if (inp) setUserName(inp.value); },
  slot: el => { st.book.slot = el.dataset.v; document.querySelectorAll('.slot').forEach(b => b.classList.toggle('on', b === el)); },
  confirm: confirmBook,
  fly: el => { const u = st.mapUnits[+el.dataset.i]; st.map && st.map.flyTo([u.lat, u.lng], 17); },
  'fs-': () => { st.prefs.fs = Math.max(14, (st.prefs.fs || 16) - 2); applyPrefs(); },
  'fs+': () => { st.prefs.fs = Math.min(28, (st.prefs.fs || 16) + 2); applyPrefs(); },
  health: async () => {
    const o = $('#hs'); o.textContent = 'Testando…'; const t = Date.now();
    try { await api('/api/health'); o.innerHTML = `<span class="chip ok">Servidor e banco OK (${Date.now() - t} ms)</span>`; } catch (e) { o.innerHTML = `<span class="bad">Falha: ${esc(e.message)}</span>`; }
  },
};

document.addEventListener('click', async e => {
  const editBtn = e.target.closest('#btn-edit-name, #greet-name');
  if (editBtn) {
    promptEditName();
    return;
  }
  const avatarClick = e.target.closest('#user-avatar');
  if (avatarClick) {
    promptEditName();
    return;
  }

  const el = e.target.closest('[data-go],[data-act],[data-cat]');
  if (!el) return;

  if (el.dataset.cat) {
    const cat = el.dataset.cat.toLowerCase().trim();
    try {
      const specs = await get('specialties');
      const found = specs.find(s => {
        const sName = s.name.toLowerCase();
        return sName.includes(cat.split(' ')[0]) || cat.includes(sName.split(' ')[0]);
      });
      st.filter = { spec: found ? found.id : '' };
    } catch (err) {
      st.filter = {};
    }
    location.hash = '#/medicos';
    return;
  }

  if (el.dataset.go) {
    location.hash = '#/' + el.dataset.go;
  } else if (el.dataset.act) {
    ACT[el.dataset.act]?.(el);
  }
});

document.addEventListener('change', async e => {
  const t = e.target;
  if (t.dataset.p) { st.prefs[t.dataset.p] = t.checked; applyPrefs(); }
  if (t.dataset.f) { (st.filter = st.filter || {})[t.dataset.f] = t.value; vDocs().catch(showErr); }
  if (t.dataset.b) {
    const k = t.dataset.b, b = st.book; b[k] = t.value;
    if (k === 'unit') { b.doc = ''; b.day = ''; b.slot = ''; }
    if (k === 'doc') { b.day = ''; b.slot = ''; }
    if (k === 'day') b.slot = '';
    const pn = $('#pn'); if (pn) b.name = pn.value;
    vBook().catch(showErr);
  }
});

/* ---------- ROTEADOR ---------- */
const ROUTES = {
  home: [vHome, 'Home'],
  servicos: [vServ, 'Serviços'],
  unidades: [vUnits, 'Unidades de saúde'],
  mapa: [vMap, 'Mapa das unidades'],
  medicos: [vDocs, 'Médicos e horários'],
  agendar: [vBook, 'Agendar consulta'],
  confirmacao: [vDone, 'Confirmação'],
  avisos: [vNews, 'Avisos e Campanhas'],
  ajustes: [vSet, 'Ajustes']
};

const showErr = e => setMain(`<div class="card err" role="alert"><b>Não foi possível carregar.</b><p>${esc(e.message)}</p><button class="btn" data-act="retry">Tentar de novo</button></div>`);

async function route() {
  const name = (location.hash.slice(2) || 'home').split('/')[0], r = ROUTES[name] || ROUTES.home, key = ROUTES[name] ? name : 'home';
  Object.keys(cache).forEach(k => delete cache[k]);
  if (st.map) { st.map.remove(); st.map = null; }
  
  const isHome = (key === 'home');
  const topNav = $('#top-nav');
  const heroWrap = $('#hero-wrap');
  const subTop = $('#sub-top');
  
  if (topNav) topNav.hidden = !isHome;
  if (heroWrap) heroWrap.hidden = !isHome;
  if (subTop) subTop.hidden = isHome;
  
  $('#title').textContent = r[1];
  $('#main').classList.toggle('plain', !isHome);

  $('#tabs').innerHTML = TABS.map(([k, l]) => `<button class="${k === key ? 'on' : ''}" data-go="${k}">${ico(k)}${l}</button>`).join('');
  setMain('<p class="load">Carregando…</p>');
  try { await r[0](); } catch (e) { showErr(e); }
  scrollTo(0, 0);
}

addEventListener('hashchange', route);
loadPrefs(); route();
"""

FILES['admin.css'] = """html{font-size:16px}
.auth{min-height:100dvh;display:grid;place-items:center;padding:1.2rem;background:var(--bg)}
.box{width:100%;max-width:420px;background:var(--card);border:1.5px solid var(--line);border-radius:26px;padding:2rem;box-shadow:0 12px 36px rgba(0,191,166,.12)}
.adm{display:grid;grid-template-columns:250px 1fr;min-height:100dvh}
.adm aside{background:var(--card);border-right:1.5px solid var(--line);padding:1.4rem;position:sticky;top:0;height:100dvh;display:flex;flex-direction:column;gap:.4rem;box-shadow:4px 0 20px rgba(0,191,166,.04)}
.adm aside h1{font-size:1.2rem;margin:0;color:var(--pri-dark);font-weight:800}
.adm nav{margin:1.2rem 0;flex:1}
.adm nav button{display:flex;align-items:center;gap:.7rem;width:100%;min-height:48px;text-align:left;background:none;border:0;border-radius:14px;padding:.6rem 1rem;font-weight:700;color:var(--mut);cursor:pointer;transition:all .2s ease}
.adm nav button:hover{background:var(--soft);color:var(--pri-dark)}
.adm nav .on{background:var(--soft);color:var(--pri-dark);font-weight:800}
.adm main{padding:1.8rem 2.2rem;min-width:0}
.split{display:grid;grid-template-columns:minmax(300px,380px) 1fr;gap:1.4rem;align-items:start}.split .card{margin:0}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:1.2rem}
.stats .card{margin:0;background:var(--card);border:1.5px solid var(--line);border-radius:20px}
.stats b{font-size:2.5rem;display:block;color:var(--pri);font-weight:800;letter-spacing:-.02em}
.tw{overflow-x:auto}.row{display:flex;flex-wrap:wrap;gap:.9rem}.row>*{flex:1;min-width:150px}
.st-agendada{background:#FFF9E6;color:#8F6B00;border-radius:999px;padding:.2rem .75rem;font-weight:700}.st-confirmada{background:#E0F7FA;color:#006064;border-radius:999px;padding:.2rem .75rem;font-weight:700}.st-concluida{background:#E8F5E9;color:#1B5E20;border-radius:999px;padding:.2rem .75rem;font-weight:700}.st-cancelada{background:#FFEBEE;color:#B71C1C;border-radius:999px;padding:.2rem .75rem;font-weight:700}
.on-off{font-weight:700}.off{opacity:.55}
td .btn.s{margin:.15rem .35rem .15rem 0;min-height:38px;padding:.35rem .9rem;font-size:.85rem}
.btn.danger{color:var(--bad);border-color:var(--bad);background:transparent;box-shadow:none}
.btn.danger:hover{background:var(--bad);color:#fff}
#map{height:60vh;min-height:340px;border-radius:22px;border:1.5px solid var(--line);margin:.8rem 0}
.pin{background:var(--pri);color:var(--onpri);border:2px solid #fff;border-radius:50%;font-weight:700;display:grid;place-items:center;width:30px!important;height:30px!important}
@media(max-width:900px){.adm{grid-template-columns:1fr}.adm aside{position:static;height:auto}.adm nav{display:flex;overflow-x:auto;margin:.5rem 0}.adm nav button{width:auto;white-space:nowrap}.split{grid-template-columns:1fr}.adm main{padding:1.2rem}}
#toast{bottom:1.5rem}
"""

FILES['admin.js'] = """/* Painel administrativo. Toda a autorização é validada no servidor; aqui ficam só as telas. */
const $ = s => document.querySelector(s);
const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const DIAS = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo'];
const STAT = { agendada: 'Agendada', confirmada: 'Confirmada', concluida: 'Concluída', cancelada: 'Cancelada' };
const NAV = [['painel', 'Painel'], ['unidades', 'Unidades'], ['medicos', 'Médicos'], ['horarios', 'Horários e presença'], ['agendamentos', 'Agendamentos'], ['mapa', 'Mapa'], ['campanhas', 'Campanhas']];
const V = { sec: 'painel', ed: null, del: null, f: {}, av: {} };
let ME = null;

async function call(path, method = 'GET', body) {
  let r;
  try { r = await fetch(path, { method, credentials: 'same-origin', headers: { 'Content-Type': 'application/json', 'X-Requested-With': 'fetch' }, body: body ? JSON.stringify(body) : undefined }); }
  catch (e) { throw new Error('Sem conexão com o servidor.'); }
  const j = await r.json().catch(() => ({}));
  if (r.status === 401 && !path.endsWith('/login') && !path.endsWith('/me')) { ME = null; login('Sessão expirada. Entre novamente.'); throw new Error('AUTH'); }
  if (!r.ok) throw new Error(j.error || 'Erro inesperado.');
  return j;
}
function toast(t) { const e = $('#toast'); e.textContent = t; e.hidden = false; clearTimeout(toast.t); toast.t = setTimeout(() => e.hidden = true, 3500); }
const run = async fn => { try { await fn(); } catch (e) { if (e.message !== 'AUTH') toast(e.message); } };
const val = id => $('#' + id).value.trim(), chk = id => $('#' + id).checked;
const fld = (l, id, v, type = 'text', x = '') => `<label>${l}<input id="${id}" type="${type}" value="${esc(v)}" ${x}></label>`;
const ck = (l, id, v) => `<label class="ck"><input type="checkbox" id="${id}" ${v ? 'checked' : ''}>${l}</label>`;
const opts = (a, sel, fn) => a.map(x => `<option value="${x.id}" ${x.id == sel ? 'selected' : ''}>${esc(fn(x))}</option>`).join('');
const fd = d => d ? d.split('-').reverse().join('/') : '';
const today = () => new Date(Date.now() - new Date().getTimezoneOffset() * 6e4).toISOString().slice(0, 10);
const delBtn = (k, id) => `<button class="btn s danger" data-act="del-${k}" data-id="${id}">${V.del === k + id ? 'Confirmar remoção' : 'Remover'}</button>`;
const statusChip = s => `<span class="chip st-${s}">${STAT[s] || s}</span>`;
const mins = h => +h.slice(0, 2) * 60 + +h.slice(3);

/* ---------- login e estrutura ---------- */
function login(msg = '') {
  $('#root').innerHTML = `<main class="auth"><form class="box" id="lf"><h1>Administração</h1><p class="mut">Saúde Ibiassucê · acesso restrito</p>
  <label>E-mail<input id="le" type="email" autocomplete="username" required></label><label>Senha<input id="lp" type="password" autocomplete="current-password" required></label>
  <p class="bad" role="alert" id="lm">${esc(msg)}</p><button class="btn">Entrar</button></form></main>`;
  $('#lf').onsubmit = e => { e.preventDefault(); run(async () => { try { ME = await call('/api/admin/login', 'POST', { email: val('le'), password: $('#lp').value }); shell(); } catch (er) { if (er.message !== 'AUTH') $('#lm').textContent = er.message; } }); };
}
function shell() {
  $('#root').innerHTML = `<div class="adm"><aside><h1>Saúde Ibiassucê</h1><span class="mut small">${esc(ME.email)}</span><nav id="nav" aria-label="Seções"></nav><button class="btn s" data-act="logout">Sair</button></aside><main id="c"></main></div>`;
  route();
}
async function route() {
  if (!ME) return;
  const s = location.hash.slice(2) || 'painel'; V.sec = SEC[s] ? s : 'painel';
  $('#nav').innerHTML = NAV.map(([k, l]) => `<button class="${k === V.sec ? 'on' : ''}" data-go="${k}">${l}</button>`).join('');
  await section();
}
function section() {
  return V.chain = (V.chain || Promise.resolve()).then(async () => {
    try { await SEC[V.sec](); } catch (e) { if (e.message !== 'AUTH') $('#c').innerHTML = `<div class="card err"><b>Não foi possível carregar.</b><p>${esc(e.message)}</p><button class="btn s" data-act="reload">Tentar de novo</button></div>`; }
  });
}
const reload = async (keep = true) => { const y = scrollY; await section(); if (keep) scrollTo(0, y); };

/* ---------- painel ---------- */
const SEC = {};
SEC.painel = async () => {
  const s = await call('/api/admin/stats');
  $('#c').innerHTML = `<h2>Painel</h2><div class="stats">${[['Unidades ativas', s.units], ['Médicos ativos', s.doctors], ['Agendamentos', s.appointments], ['Consultas hoje', s.today]].map(([l, n]) => `<div class="card"><b>${n}</b>${l}</div>`).join('')}</div>
  <div class="card"><h3>Situação dos agendamentos</h3>${Object.keys(STAT).map(k => `<span class="chip st-${k}">${STAT[k]}: ${s.by_status[k] || 0}</span>`).join('')}</div>
  <div class="card"><h3>Atalhos</h3><button class="btn s" data-go="unidades">Cadastrar unidade</button><button class="btn s" data-go="medicos">Cadastrar médico</button><button class="btn s" data-go="horarios">Definir horários</button><button class="btn s" data-go="agendamentos">Ver agendamentos</button></div>
  <div class="card tw"><h3>Agendamentos recentes</h3><table><thead><tr><th>Código</th><th>Paciente</th><th>Médico</th><th>Unidade</th><th>Data</th><th>Situação</th></tr></thead><tbody>${s.recent.map(a => `<tr><td>${esc(a.code)}</td><td>${esc(a.patient_name)}</td><td>${esc(a.doctor)}</td><td>${esc(a.unit)}</td><td>${fd(a.day)} ${a.slot}</td><td>${statusChip(a.status)}</td></tr>`).join('') || '<tr><td colspan="6">Nenhum agendamento ainda.</td></tr>'}</tbody></table></div>`;
};

/* ---------- unidades ---------- */
SEC.unidades = async () => {
  const us = await call('/api/admin/units'), e = us.find(u => u.id == V.ed) || {};
  $('#c').innerHTML = `<h2>Unidades</h2><div class="split"><div class="card"><h3>${V.ed ? 'Editar unidade' : 'Nova unidade'}</h3>${fld('Nome', 'u_name', e.name)}
  <label>Tipo<select id="u_type">${['UBS', 'Hospital', 'Posto', 'Vacinação'].map(t => `<option ${e.type === t ? 'selected' : ''}>${t}</option>`).join('')}</select></label>
  ${fld('Endereço', 'u_address', e.address)}${fld('Telefone', 'u_phone', e.phone)}${fld('Horário de funcionamento', 'u_hours', e.hours)}${fld('Serviços (separe por vírgula)', 'u_services', e.services)}${fld('Documentos necessários', 'u_docs', e.docs)}
  <div class="row">${fld('Latitude', 'u_lat', e.lat, 'number', 'step="any"')}${fld('Longitude', 'u_lng', e.lng, 'number', 'step="any"')}</div>
  <p class="mut small">Dica: no Google Maps, clique com o botão direito no local e copie as coordenadas.</p>
  ${ck('Rampa de acesso', 'u_ramp', e.ramp)}<br>${ck('Banheiro adaptado', 'u_wc', e.wc)}<br>${ck('Intérprete de Libras', 'u_libras', e.libras)}
  <button class="btn" data-act="save-unit">Salvar</button>${V.ed ? '<button class="btn s" data-act="cancel-edit">Cancelar edição</button>' : ''}</div>
  <div class="card tw"><input data-filter placeholder="Pesquisar unidade" aria-label="Pesquisar"><table style="margin-top:.6rem"><thead><tr><th>Nome</th><th>Tipo</th><th>Endereço</th><th>Situação</th><th></th></tr></thead><tbody>
  ${us.map(u => `<tr data-s="${esc((u.name + u.address + u.type).toLowerCase())}" class="${u.active ? '' : 'off'}"><td><b>${esc(u.name)}</b><br><span class="mut small">${esc(u.hours || '')}</span></td><td>${esc(u.type)}</td><td>${esc(u.address)}</td><td>${u.active ? 'Ativa' : 'Desativada'}</td>
  <td><button class="btn s" data-act="edit" data-id="${u.id}">Editar</button><button class="btn s" data-act="toggle-unit" data-id="${u.id}" data-to="${u.active ? 0 : 1}">${u.active ? 'Desativar' : 'Ativar'}</button>${delBtn('unit', u.id)}</td></tr>`).join('') || '<tr><td colspan="5">Nenhuma unidade.</td></tr>'}</tbody></table></div></div>`;
};
const saveUnit = () => run(async () => {
  const b = { name: val('u_name'), type: val('u_type'), address: val('u_address'), phone: val('u_phone'), hours: val('u_hours'), services: val('u_services'), docs: val('u_docs'), lat: val('u_lat'), lng: val('u_lng'), ramp: chk('u_ramp'), wc: chk('u_wc'), libras: chk('u_libras') };
  V.ed ? await call('/api/admin/units/' + V.ed, 'PUT', b) : await call('/api/admin/units', 'POST', b);
  V.ed = null; toast('Unidade salva.'); await reload(false);
});

/* ---------- médicos ---------- */
SEC.medicos = async () => {
  const [docs, us, sp] = await Promise.all([call('/api/doctors?public=0'), call('/api/admin/units'), call('/api/specialties')]);
  const e = docs.find(d => d.id == V.ed) || {}, mine = (e.units || []).map(u => u.unit_id);
  $('#c').innerHTML = `<h2>Médicos</h2><div class="split"><div class="card"><h3>${V.ed ? 'Editar médico' : 'Novo médico'}</h3>${fld('Nome', 'd_name', e.name)}
  <label>Especialidade<select id="d_spec">${opts(sp, e.specialty_id, s => s.name)}</select></label>${fld('Ou criar nova especialidade', 'd_newspec', '', 'text', 'placeholder="Deixe vazio para usar a lista"')}
  <p><b>Atende nas unidades</b></p>${us.map(u => `<label class="ck"><input type="checkbox" class="d_unit" value="${u.id}" ${mine.includes(u.id) ? 'checked' : ''}>${esc(u.name)}${u.active ? '' : ' (desativada)'}</label>`).join('') || '<p class="mut">Cadastre uma unidade primeiro.</p>'}
  <button class="btn" data-act="save-doc">Salvar</button>${V.ed ? '<button class="btn s" data-act="cancel-edit">Cancelar edição</button>' : ''}</div>
  <div class="card tw"><input data-filter placeholder="Pesquisar médico" aria-label="Pesquisar"><table style="margin-top:.6rem"><thead><tr><th>Nome</th><th>Especialidade</th><th>Unidades</th><th>Situação</th><th></th></tr></thead><tbody>
  ${docs.map(d => `<tr data-s="${esc((d.name + d.specialty).toLowerCase())}" class="${d.active ? '' : 'off'}"><td><b>${esc(d.name)}</b></td><td>${esc(d.specialty)}</td><td>${d.units.map(u => esc(u.unit_name)).join('<br>') || '<span class="mut">nenhuma</span>'}</td><td>${d.active ? 'Ativo' : 'Desativado'}</td>
  <td><button class="btn s" data-act="edit" data-id="${d.id}">Editar</button><button class="btn s" data-act="toggle-doc" data-id="${d.id}" data-to="${d.active ? 0 : 1}">${d.active ? 'Desativar' : 'Ativar'}</button>${delBtn('doc', d.id)}</td></tr>`).join('') || '<tr><td colspan="5">Nenhum médico.</td></tr>'}</tbody></table></div></div>`;
  $('#c').dataset.specs = JSON.stringify(sp);
};
const saveDoc = () => run(async () => {
  let spec = +val('d_spec'); const ns = val('d_newspec');
  if (ns) { const known = JSON.parse($('#c').dataset.specs).find(s => s.name.toLowerCase() === ns.toLowerCase()); spec = known ? known.id : (await call('/api/admin/specialties', 'POST', { name: ns })).id; }
  if (!spec) throw new Error('Escolha ou crie uma especialidade.');
  const body = { name: val('d_name'), specialty_id: spec };
  const id = V.ed ? (await call('/api/admin/doctors/' + V.ed, 'PUT', body), V.ed) : (await call('/api/admin/doctors', 'POST', body)).id;
  await call(`/api/admin/doctors/${id}/units`, 'PUT', { unit_ids: [...document.querySelectorAll('.d_unit:checked')].map(c => +c.value) });
  V.ed = null; toast('Médico salvo.'); await reload(false);
});

/* ---------- horários e presença ---------- */
SEC.horarios = async () => {
  const [docs, av] = await Promise.all([call('/api/doctors?public=0'), call('/api/admin/availabilities')]);
  const a = V.av, doc = docs.find(d => d.id == a.doctor) || docs[0] || { units: [] }; a.doctor = doc.id;
  if (!doc.units.some(u => u.unit_id == a.unit)) a.unit = doc.units[0]?.unit_id;
  const edit = !!V.avEd, t = today(), wd = (new Date(t + 'T12:00').getDay() + 6) % 7;
  const rows = [];
  for (const d of docs) for (const u of d.units) {
    const list = u.availabilities.filter(x => x.weekday === wd); if (!list.length) continue;
    const total = list.reduce((n, x) => n + Math.floor((mins(x.ends) - mins(x.starts)) / x.slot_minutes), 0);
    const free = (await call(`/api/slots?doctor_id=${d.id}&unit_id=${u.unit_id}&day=${t}`)).length;
    rows.push({ d, u, total, free });
  }
  $('#c').innerHTML = `<h2>Horários e presença</h2><div class="split"><div class="card"><h3>${edit ? 'Editar horário' : 'Novo horário de atendimento'}</h3>
  <label>Médico<select data-av="doctor" ${edit ? 'disabled' : ''}>${opts(docs, a.doctor, d => `${d.name} (${d.specialty})`)}</select></label>
  <label>Unidade<select data-av="unit" ${edit ? 'disabled' : ''}>${opts(doc.units.map(u => ({ id: u.unit_id, n: u.unit_name })), a.unit, u => u.n)}</select></label>
  ${doc.units.length ? '' : '<p class="bad">Associe este médico a uma unidade na tela Médicos.</p>'}
  <label>Dia da semana<select id="a_wd">${DIAS.map((n, i) => `<option value="${i}" ${(a.weekday ?? 0) == i ? 'selected' : ''}>${n}</option>`).join('')}</select></label>
  <div class="row">${fld('Início', 'a_st', a.starts || '08:00', 'time')}${fld('Fim', 'a_en', a.ends || '12:00', 'time')}</div>${fld('Duração de cada consulta (minutos)', 'a_sl', a.slot_minutes || 30, 'number', 'min="10" max="120"')}
  <button class="btn" data-act="save-av">Salvar horário</button>${edit ? '<button class="btn s" data-act="cancel-av">Cancelar edição</button>' : ''}</div>
  <div><div class="card tw" style="margin-top:0"><h3>Hoje (${fd(t)}, ${DIAS[wd]}): cadastrado, disponível e presença</h3><table><thead><tr><th>Médico</th><th>Unidade</th><th>Cadastrados</th><th>Disponíveis agora</th><th>Presença</th></tr></thead><tbody>
  ${rows.map(r => `<tr><td>${esc(r.d.name)}</td><td>${esc(r.u.unit_name)}</td><td>${r.total}</td><td>${r.free}</td><td>${r.u.presence_today ? '<span class="chip ok">Confirmada</span>' : '<span class="chip no">Não confirmada</span>'}
  <button class="btn s" data-act="pres" data-d="${r.d.id}" data-u="${r.u.unit_id}" data-on="${r.u.presence_today ? 0 : 1}">${r.u.presence_today ? 'Desmarcar' : 'Confirmar presença'}</button></td></tr>`).join('') || '<tr><td colspan="5">Nenhum médico com horário cadastrado para hoje.</td></tr>'}</tbody></table></div>
  <div class="card tw"><h3>Horários cadastrados</h3><table><thead><tr><th>Médico</th><th>Unidade</th><th>Dia</th><th>Horário</th><th>Duração</th><th></th></tr></thead><tbody>
  ${av.map(x => `<tr><td>${esc(x.doctor)}</td><td>${esc(x.unit)}</td><td>${DIAS[x.weekday]}</td><td>${x.starts}–${x.ends}</td><td>${x.slot_minutes} min</td><td><button class="btn s" data-act="edit-av" data-id="${x.id}">Editar</button><button class="btn s danger" data-act="del-av" data-id="${x.id}">${V.del === 'av' + x.id ? 'Confirmar remoção' : 'Remover'}</button></td></tr>`).join('') || '<tr><td colspan="6">Nenhum horário cadastrado.</td></tr>'}</tbody></table></div></div></div>`;
  V.avRows = av;
};
const saveAv = () => run(async () => {
  const a = V.av, b = { weekday: +val('a_wd'), starts: val('a_st'), ends: val('a_en'), slot_minutes: +val('a_sl') };
  V.avEd ? await call('/api/admin/availabilities/' + V.avEd, 'PUT', b) : await call('/api/admin/availabilities', 'POST', { doctor_id: a.doctor, unit_id: a.unit, ...b });
  V.av = V.avEd ? { doctor: a.doctor, unit: a.unit } : { ...a, ...b }; V.avEd = null; toast('Horário salvo.'); await reload();
});

/* ---------- agendamentos ---------- */
SEC.agendamentos = async () => {
  const f = V.f, qs = Object.entries(f).filter(([, v]) => v).map(([k, v]) => `${k}=${encodeURIComponent(v)}`).join('&');
  const [ap, us, docs] = await Promise.all([call('/api/admin/appointments?' + qs), call('/api/admin/units'), call('/api/doctors?public=0')]);
  $('#c').innerHTML = `<h2>Agendamentos</h2><div class="card"><div class="row"><label>Unidade<select data-fl="unit_id"><option value="">Todas</option>${opts(us, f.unit_id, u => u.name)}</select></label>
  <label>Médico<select data-fl="doctor_id"><option value="">Todos</option>${opts(docs, f.doctor_id, d => d.name)}</select></label><label>Data<input type="date" data-fl="day" value="${f.day || ''}"></label>
  <label>Situação<select data-fl="status"><option value="">Todas</option>${Object.entries(STAT).map(([k, l]) => `<option value="${k}" ${f.status === k ? 'selected' : ''}>${l}</option>`).join('')}</select></label></div></div>
  <div class="card tw"><table><thead><tr><th>Código</th><th>Paciente (demo)</th><th>Data</th><th>Médico</th><th>Unidade</th><th>Situação</th><th></th></tr></thead><tbody>
  ${ap.map(a => `<tr><td>${esc(a.code)}</td><td>${esc(a.patient_name)}</td><td>${fd(a.day)} ${a.slot}</td><td>${esc(a.doctor)}<br><span class="mut small">${esc(a.specialty)}</span></td><td>${esc(a.unit)}</td><td>${statusChip(a.status)}</td><td>
  ${a.status === 'agendada' ? `<button class="btn s" data-act="appt" data-id="${a.id}" data-st="confirmada">Confirmar</button>` : ''}${a.status === 'confirmada' ? `<button class="btn s" data-act="appt" data-id="${a.id}" data-st="concluida">Concluir</button>` : ''}
  ${a.status === 'cancelada' ? `<button class="btn s" data-act="appt" data-id="${a.id}" data-st="agendada">Reativar</button>` : (a.status !== 'concluida' ? `<button class="btn s danger" data-act="appt" data-id="${a.id}" data-st="cancelada">Cancelar</button>` : '')}</td></tr>`).join('') || '<tr><td colspan="7">Nenhum agendamento encontrado.</td></tr>'}</tbody></table></div>`;
};

/* ---------- mapa ---------- */
const CDN = 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/';
const loadLeaflet = () => new Promise((ok, no) => {
  if (window.L) return ok();
  const l = document.createElement('link'); l.rel = 'stylesheet'; l.href = CDN + 'leaflet.css'; document.head.appendChild(l);
  const s = document.createElement('script'); s.src = CDN + 'leaflet.js'; s.onload = ok; s.onerror = () => no(new Error('Não foi possível carregar o mapa. Verifique a internet.')); document.head.appendChild(s);
});
let MAP = null, MU = [];
SEC.mapa = async () => {
  if (MAP) { MAP.remove(); MAP = null; }
  MU = (await call('/api/admin/units')).filter(u => u.lat != null && u.lng != null);
  $('#c').innerHTML = `<h2>Mapa das unidades</h2><div id="map" role="application" aria-label="Mapa"></div><div>${MU.map((u, i) => `<button class="btn s ${u.active ? '' : 'off'}" data-act="fly" data-i="${i}">${i + 1}. ${esc(u.name)}${u.active ? '' : ' (desativada)'}</button>`).join('')}</div>
  ${MU.length ? '' : '<p class="mut">Nenhuma unidade com latitude e longitude. Cadastre as coordenadas na tela Unidades.</p>'}`;
  if (!MU.length) return;
  try {
    await loadLeaflet(); MAP = L.map('map');
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', { maxZoom: 19, attribution: '&copy; OpenStreetMap' }).addTo(MAP);
    MU.forEach((u, i) => L.marker([u.lat, u.lng], { icon: L.divIcon({ className: '', html: `<div class="pin">${i + 1}</div>`, iconSize: [30, 30] }) }).addTo(MAP).bindPopup(`<b>${esc(u.name)}</b><br>${esc(u.address)}`));
    MAP.fitBounds(MU.map(u => [u.lat, u.lng]), { padding: [40, 40], maxZoom: 16 });
  } catch (e) { $('#map').innerHTML = `<p class="load bad" style="padding:2rem">${esc(e.message)}</p>`; }
};

/* ---------- campanhas ---------- */
SEC.campanhas = async () => {
  const cs = await call('/api/admin/campaigns'), e = cs.find(c => c.id == V.ed) || {};
  $('#c').innerHTML = `<h2>Campanhas e avisos</h2><div class="split"><div class="card"><h3>${V.ed ? 'Editar campanha' : 'Nova campanha'}</h3>${fld('Título', 'c_title', e.title)}
  <label>Mensagem<textarea id="c_body" rows="4" maxlength="600">${esc(e.body)}</textarea></label>${fld('Data (opcional)', 'c_day', e.day, 'date')}
  <button class="btn" data-act="save-camp">Publicar</button>${V.ed ? '<button class="btn s" data-act="cancel-edit">Cancelar edição</button>' : ''}</div>
  <div class="card tw"><table><thead><tr><th>Título</th><th>Data</th><th>Mensagem</th><th></th></tr></thead><tbody>${cs.map(c => `<tr><td><b>${esc(c.title)}</b></td><td>${fd(c.day)}</td><td>${esc(c.body)}</td>
  <td><button class="btn s" data-act="edit" data-id="${c.id}">Editar</button>${delBtn('camp', c.id)}</td></tr>`).join('') || '<tr><td colspan="4">Nenhuma campanha.</td></tr>'}</tbody></table></div></div>`;
};
const saveCamp = () => run(async () => {
  const b = { title: val('c_title'), body: val('c_body'), day: val('c_day') };
  V.ed ? await call('/api/admin/campaigns/' + V.ed, 'PUT', b) : await call('/api/admin/campaigns', 'POST', b);
  V.ed = null; toast('Campanha publicada.'); await reload(false);
});

/* ---------- eventos ---------- */
const DEL = { unit: 'units', doc: 'doctors', camp: 'campaigns', av: 'availabilities' };
const ACT = {
  logout: () => run(async () => { await call('/api/admin/logout', 'POST'); ME = null; login(); }),
  reload: () => section(),
  edit: el => { V.ed = +el.dataset.id; section(); scrollTo(0, 0); },
  'cancel-edit': () => { V.ed = null; section(); },
  'save-unit': saveUnit, 'save-doc': saveDoc, 'save-camp': saveCamp, 'save-av': saveAv,
  'toggle-unit': el => run(async () => { await call('/api/admin/units/' + el.dataset.id, 'PUT', { active: +el.dataset.to }); await reload(); }),
  'toggle-doc': el => run(async () => { await call('/api/admin/doctors/' + el.dataset.id, 'PUT', { active: +el.dataset.to }); await reload(); }),
  'edit-av': el => { const x = V.avRows.find(r => r.id == el.dataset.id); V.avEd = x.id; V.av = { doctor: x.doctor_id, unit: x.unit_id, weekday: x.weekday, starts: x.starts, ends: x.ends, slot_minutes: x.slot_minutes }; section(); scrollTo(0, 0); },
  'cancel-av': () => { V.avEd = null; V.av = {}; section(); },
  pres: el => run(async () => { await call('/api/admin/presence', 'POST', { doctor_id: +el.dataset.d, unit_id: +el.dataset.u, day: today(), confirmed: el.dataset.on === '1' }); await reload(); }),
  appt: el => run(async () => { await call('/api/admin/appointments/' + el.dataset.id, 'PUT', { status: el.dataset.st }); await reload(); }),
  fly: el => { const u = MU[+el.dataset.i]; MAP && MAP.flyTo([u.lat, u.lng], 17); },
};
document.addEventListener('click', e => {
  const el = e.target.closest('[data-go],[data-act]'); if (!el) return;
  if (el.dataset.go) { V.ed = null; V.del = null; location.hash = '#/' + el.dataset.go; return; }
  const m = el.dataset.act.match(/^del-(unit|doc|camp|av)$/);
  if (m) {
    const key = m[1] + el.dataset.id;
    if (V.del !== key) { V.del = key; reload(); return; }
    V.del = null; run(async () => { await call(`/api/admin/${DEL[m[1]]}/${el.dataset.id}`, 'DELETE'); toast('Removido.'); await reload(); }); return;
  }
  ACT[el.dataset.act]?.(el);
});
document.addEventListener('change', e => {
  const t = e.target;
  if (t.dataset.fl) { V.f[t.dataset.fl] = t.value; section(); }
  if (t.dataset.av) { V.av[t.dataset.av] = +t.value; if (t.dataset.av === 'doctor') V.av.unit = null; for (const [k, id] of [['weekday', 'a_wd'], ['starts', 'a_st'], ['ends', 'a_en'], ['slot_minutes', 'a_sl']]) V.av[k] = $('#' + id).value; reload(); }
});
document.addEventListener('input', e => {
  if (!e.target.matches('[data-filter]')) return; const q = e.target.value.toLowerCase();
  document.querySelectorAll('tr[data-s]').forEach(r => r.hidden = !r.dataset.s.includes(q));
});
addEventListener('hashchange', route);
call('/api/admin/me').then(u => { ME = u; shell(); }).catch(e => { if (e.message !== 'AUTH') login(); });
"""

FILES['admin.html'] = """<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex"><title>Administração — Saúde Ibiassucê</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/static/theme.css"><link rel="stylesheet" href="/static/admin.css">
</head><body><div id="root"></div><div id="toast" role="status" hidden></div><script src="/static/admin.js"></script></body></html>
"""
