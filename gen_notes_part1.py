# Part 1: HTML head + CSS + sidebar + L01 full content
out = open('/sessions/blissful-quirky-tesla/mnt/outputs/CSAI601_Unit1_Notes.html', 'w')

HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CSAI601 Unit 1 — Foundations of Large Language Models | Lecture Notes</title>
<style>
:root{
  --navy:#1a1a2e;--blue:#0f3460;--red:#e94560;--teal:#00b4d8;
  --bg:#f4f6fb;--card:#ffffff;--border:#dce3f0;--muted:#64748b;
  --text:#1e293b;--code-bg:#1e293b;--code-text:#e2e8f0;
  --info-bg:#eff6ff;--info-border:#3b82f6;
  --key-bg:#fdf4ff;--key-border:#a855f7;
  --eg-bg:#f0fdf4;--eg-border:#22c55e;
  --warn-bg:#fff7ed;--warn-border:#f97316;
  --math-bg:#f8f0ff;--math-border:#8b5cf6;
  --sidebar-w:280px;
}
*{box-sizing:border-box;margin:0;padding:0;}
body{font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--text);display:flex;min-height:100vh;font-size:15px;line-height:1.75;}

/* ── Sidebar ── */
#sidebar{
  width:var(--sidebar-w);min-height:100vh;background:var(--navy);color:#fff;
  position:fixed;top:0;left:0;overflow-y:auto;z-index:200;display:flex;flex-direction:column;
}
#sidebar .brand{padding:22px 20px 16px;border-bottom:1px solid rgba(255,255,255,.1);}
#sidebar .brand .course{font-size:10px;letter-spacing:2px;color:var(--red);text-transform:uppercase;font-weight:700;}
#sidebar .brand h2{font-size:13px;line-height:1.5;margin-top:5px;font-weight:600;color:#e2e8f0;}
#sidebar nav{flex:1;padding:10px 0;}
#sidebar nav .nav-section{font-size:9.5px;letter-spacing:1.5px;color:rgba(255,255,255,.35);text-transform:uppercase;padding:14px 18px 5px;font-weight:700;}
#sidebar nav a{display:flex;align-items:flex-start;gap:9px;padding:7px 18px;font-size:12.5px;color:rgba(255,255,255,.7);text-decoration:none;transition:all .15s;border-left:3px solid transparent;line-height:1.4;}
#sidebar nav a:hover{color:#fff;background:rgba(255,255,255,.06);}
#sidebar nav a.active{color:#fff;background:rgba(233,69,96,.15);border-left-color:var(--red);}
#sidebar nav a .lnum{font-size:10px;font-weight:800;color:var(--red);min-width:22px;margin-top:1px;}
#sidebar .progress{padding:14px 18px;border-top:1px solid rgba(255,255,255,.1);font-size:11px;color:rgba(255,255,255,.35);}

/* ── Main ── */
#main{margin-left:var(--sidebar-w);flex:1;display:flex;flex-direction:column;}
#topbar{background:#fff;border-bottom:1px solid var(--border);padding:12px 40px;position:sticky;top:0;z-index:100;display:flex;align-items:center;justify-content:space-between;}
#topbar .tb-left{font-size:13px;color:var(--muted);}
#topbar .tb-right{display:flex;gap:8px;}
.badge{font-size:11px;padding:3px 10px;border-radius:20px;font-weight:700;}
.b-navy{background:#e8edf7;color:var(--navy);}
.b-red{background:#fee2e2;color:#991b1b;}
.b-green{background:#dcfce7;color:#166534;}

#content{padding:44px 52px 80px;max-width:940px;}

/* ── Lecture sections ── */
.lecture{display:none;}
.lecture.active{display:block;}
.lec-hero{background:linear-gradient(135deg,var(--navy),var(--blue));border-radius:14px;padding:36px 40px;margin-bottom:32px;color:#fff;}
.lec-hero .lec-tag{font-size:10px;letter-spacing:2px;font-weight:800;color:var(--red);text-transform:uppercase;background:rgba(233,69,96,.15);padding:4px 12px;border-radius:20px;display:inline-block;margin-bottom:12px;}
.lec-hero h1{font-size:26px;font-weight:800;line-height:1.3;margin-bottom:10px;}
.lec-hero p{font-size:14px;opacity:.85;line-height:1.7;max-width:680px;}
.lec-hero .hero-meta{display:flex;gap:20px;margin-top:18px;flex-wrap:wrap;}
.lec-hero .hero-meta span{font-size:12.5px;opacity:.8;}

.objectives{background:var(--eg-bg);border:1px solid var(--eg-border);border-radius:10px;padding:20px 24px;margin-bottom:28px;}
.objectives h3{font-size:13px;font-weight:800;color:#166534;margin-bottom:10px;display:flex;align-items:center;gap:7px;}
.objectives ul{list-style:none;padding:0;}
.objectives ul li{font-size:13.5px;color:#14532d;padding:3px 0 3px 22px;position:relative;line-height:1.6;}
.objectives ul li::before{content:"✓";position:absolute;left:0;color:#22c55e;font-weight:800;}

/* ── Content headings ── */
h2.sec{font-size:20px;font-weight:800;color:var(--navy);margin:36px 0 14px;padding-bottom:8px;border-bottom:2px solid var(--border);display:flex;align-items:center;gap:10px;}
h2.sec .sec-num{background:var(--red);color:#fff;border-radius:6px;padding:2px 9px;font-size:13px;font-weight:800;}
h3.sub{font-size:16px;font-weight:700;color:var(--blue);margin:24px 0 10px;}
h4.sub2{font-size:14.5px;font-weight:700;color:var(--navy);margin:18px 0 8px;}
p.body{font-size:14.5px;line-height:1.8;color:#334155;margin-bottom:14px;}
p.body b{color:var(--navy);}
ul.body-ul,ol.body-ol{padding-left:22px;margin-bottom:14px;}
ul.body-ul li,ol.body-ol li{font-size:14.5px;line-height:1.8;color:#334155;margin-bottom:5px;}
ul.body-ul li b,ol.body-ol li b{color:var(--navy);}

/* ── Callout boxes ── */
.callout{border-radius:10px;padding:18px 22px;margin:20px 0;border-left:4px solid;}
.callout h4{font-size:12.5px;font-weight:800;text-transform:uppercase;letter-spacing:.8px;margin-bottom:8px;}
.callout p,.callout ul{font-size:14px;line-height:1.75;margin-bottom:0;}
.callout ul{padding-left:18px;}
.callout ul li{margin-bottom:4px;}
.c-info{background:var(--info-bg);border-color:var(--info-border);}
.c-info h4{color:#1e40af;}
.c-key{background:var(--key-bg);border-color:var(--key-border);}
.c-key h4{color:#7e22ce;}
.c-eg{background:var(--eg-bg);border-color:var(--eg-border);}
.c-eg h4{color:#166534;}
.c-warn{background:var(--warn-bg);border-color:var(--warn-border);}
.c-warn h4{color:#c2410c;}
.c-math{background:var(--math-bg);border-color:var(--math-border);}
.c-math h4{color:#6d28d9;}
.c-math .formula{font-family:'Courier New',monospace;font-size:14.5px;color:#4c1d95;background:#ede9fe;border-radius:6px;padding:10px 14px;margin-top:8px;display:block;line-height:1.9;}

/* ── Code blocks ── */
.code-block{background:var(--code-bg);border-radius:10px;overflow:hidden;margin:18px 0;box-shadow:0 4px 16px rgba(0,0,0,.18);}
.code-header{background:#0f1929;padding:8px 16px;display:flex;align-items:center;justify-content:space-between;}
.code-header .lang{font-size:11px;font-weight:700;color:#94a3b8;text-transform:uppercase;letter-spacing:1px;}
.code-header .dots{display:flex;gap:5px;}
.code-header .dots span{width:10px;height:10px;border-radius:50%;}
.code-header .dots .d1{background:#ff5f57;}
.code-header .dots .d2{background:#ffbd2e;}
.code-header .dots .d3{background:#28c840;}
pre{padding:18px 20px;overflow-x:auto;font-family:'Courier New',monospace;font-size:13.5px;line-height:1.7;color:var(--code-text);}
pre .kw{color:#c792ea;}      /* keywords */
pre .fn{color:#82aaff;}      /* functions */
pre .st{color:#c3e88d;}      /* strings */
pre .cm{color:#546e7a;font-style:italic;} /* comments */
pre .nb{color:#f78c6c;}      /* numbers */
pre .cl{color:#ffcb6b;}      /* class names */
pre .op{color:#89ddff;}      /* operators */

/* ── Tables ── */
.data-table{width:100%;border-collapse:collapse;margin:16px 0;font-size:13.5px;}
.data-table th{background:var(--navy);color:#fff;padding:10px 14px;text-align:left;font-size:12px;font-weight:700;letter-spacing:.4px;}
.data-table td{padding:9px 14px;border-bottom:1px solid var(--border);vertical-align:top;line-height:1.6;}
.data-table tr:nth-child(even) td{background:#f8faff;}
.data-table tr:last-child td{border-bottom:none;}

/* ── Diagram (CSS) ── */
.diagram{background:#fff;border:1px solid var(--border);border-radius:12px;padding:28px;margin:20px 0;overflow-x:auto;}
.diagram h4{font-size:12px;font-weight:700;text-align:center;color:var(--muted);margin-bottom:20px;letter-spacing:1px;text-transform:uppercase;}
.flow{display:flex;align-items:center;justify-content:center;gap:0;flex-wrap:wrap;}
.flow-box{background:var(--blue);color:#fff;border-radius:8px;padding:10px 16px;font-size:12.5px;font-weight:700;text-align:center;min-width:90px;}
.flow-box.red{background:var(--red);}
.flow-box.teal{background:#0d9488;}
.flow-box.purple{background:#7c3aed;}
.flow-box.green{background:#16a34a;}
.flow-box.gray{background:#64748b;}
.flow-arr{color:var(--muted);font-size:20px;padding:0 6px;}
.flow-col{display:flex;flex-direction:column;align-items:center;gap:8px;}
.flow-col .flow-arr{transform:rotate(90deg);}

/* ── Summary box ── */
.summary-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:20px 0;}
.sum-card{background:#fff;border:1px solid var(--border);border-radius:10px;padding:16px 18px;border-top:3px solid var(--red);}
.sum-card h4{font-size:13px;font-weight:800;color:var(--navy);margin-bottom:8px;}
.sum-card p{font-size:13px;color:#475569;line-height:1.6;}

/* ── Quiz / practice ── */
.practice{background:#fffbf0;border:1px solid #fbbf24;border-radius:10px;padding:20px 24px;margin:24px 0;}
.practice h4{font-size:13px;font-weight:800;color:#92400e;margin-bottom:12px;}
.practice ol{padding-left:20px;font-size:14px;color:#44403c;line-height:1.8;}
.practice ol li{margin-bottom:6px;}

/* ── Timeline ── */
.timeline{list-style:none;padding:0;position:relative;margin:20px 0;}
.timeline::before{content:'';position:absolute;left:16px;top:0;bottom:0;width:2px;background:var(--border);}
.timeline li{display:flex;gap:20px;margin-bottom:22px;padding-left:44px;position:relative;}
.timeline li::before{content:'';position:absolute;left:8px;top:6px;width:16px;height:16px;border-radius:50%;background:var(--red);border:2px solid #fff;box-shadow:0 0 0 2px var(--red);}
.timeline .tl-year{font-size:12px;font-weight:800;color:var(--red);min-width:50px;margin-top:2px;}
.timeline .tl-content h5{font-size:14px;font-weight:700;color:var(--navy);margin-bottom:3px;}
.timeline .tl-content p{font-size:13.5px;color:#475569;line-height:1.6;}

/* ── Comparison ── */
.compare{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin:16px 0;}
.compare-card{background:#fff;border:1px solid var(--border);border-radius:10px;overflow:hidden;}
.compare-card .cc-head{padding:10px 16px;font-size:13px;font-weight:800;color:#fff;}
.compare-card .cc-head.blue{background:var(--blue);}
.compare-card .cc-head.red{background:var(--red);}
.compare-card .cc-body{padding:14px 16px;}
.compare-card .cc-body ul{list-style:disc;padding-left:18px;}
.compare-card .cc-body ul li{font-size:13.5px;color:#334155;margin-bottom:5px;line-height:1.6;}

/* scroll */
html{scroll-behavior:smooth;}
.lecture{scroll-margin-top:60px;}

@media(max-width:800px){
  #sidebar{display:none;}#main{margin-left:0;}#content{padding:24px 20px 60px;}
  .summary-grid,.compare{grid-template-columns:1fr;}
}
</style>
</head>
<body>
'''

out.write(HEAD)
