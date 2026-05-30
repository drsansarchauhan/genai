#!/usr/bin/env python3
"""Rebuild CSAI601_Unit2_Notes.html with unified, consistent design system."""

OUT = '/sessions/blissful-quirky-tesla/mnt/outputs/CSAI601_Unit2_Notes.html'

HEAD = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>CSAI601 Unit 2 – Prompt Engineering | Lecture Notes</title>
<style>
:root{
  --navy:#0f1f3d;--blue:#1a3a6b;--red:#e94560;--teal:#0a7c8c;
  --gold:#f4a832;--green:#27ae60;--purple:#7b2fbe;
  --bg:#0d1117;--surface:#161b22;--border:#21262d;
  --text:#e6edf3;--muted:#8b949e;--code-bg:#0d1117;
}
*{box-sizing:border-box;margin:0;padding:0;}
body{font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--text);display:flex;min-height:100vh;}
a{color:var(--teal);text-decoration:none;}
a:hover{text-decoration:underline;}
code,pre{font-family:'Cascadia Code','Fira Code',monospace;}

/* ── Sidebar ── */
#sidebar{width:260px;min-height:100vh;background:var(--navy);display:flex;flex-direction:column;position:fixed;top:0;left:0;z-index:100;overflow-y:auto;}
.brand{padding:20px 18px 14px;border-bottom:1px solid rgba(255,255,255,.1);}
.brand .course{font-size:10px;letter-spacing:2px;color:var(--red);text-transform:uppercase;font-weight:700;}
.brand h2{font-size:14px;line-height:1.4;margin-top:4px;font-weight:600;color:#fff;}
nav{flex:1;padding:10px 0;}
nav .nav-section{font-size:10px;letter-spacing:1.5px;color:rgba(255,255,255,.35);text-transform:uppercase;padding:14px 18px 5px;font-weight:700;}
nav a{display:flex;align-items:center;gap:8px;padding:9px 18px;font-size:13px;color:rgba(255,255,255,.7);text-decoration:none;border-left:3px solid transparent;transition:all .15s;}
nav a:hover{color:#fff;background:rgba(255,255,255,.06);}
nav a.active{color:#fff;background:rgba(233,69,96,.15);border-left-color:var(--red);}
.lnum{font-size:10px;background:rgba(255,255,255,.1);padding:1px 6px;border-radius:3px;font-weight:700;color:rgba(255,255,255,.5);}
.prog{padding:14px 18px;border-top:1px solid rgba(255,255,255,.08);font-size:11px;color:rgba(255,255,255,.3);}

/* ── Topbar ── */
#topbar{position:fixed;top:0;left:260px;right:0;height:52px;background:var(--surface);border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;padding:0 24px;z-index:99;}
.tb-title{font-size:13px;font-weight:600;color:var(--text);}
.tb-right{display:flex;align-items:center;gap:12px;}
.search-input{background:var(--bg);border:1px solid var(--border);border-radius:6px;padding:5px 12px;font-size:12px;color:var(--text);width:200px;outline:none;}
.search-input:focus{border-color:var(--teal);}
.theme-btn{background:none;border:1px solid var(--border);border-radius:6px;padding:5px 10px;cursor:pointer;font-size:14px;}

/* ── Main ── */
#main{margin-left:260px;padding-top:52px;flex:1;min-height:100vh;}
.lec-wrap{max-width:920px;margin:0 auto;padding:32px 28px 60px;}

/* ── Section visibility ── */
section.lecture{display:none;}
section.lecture.active{display:block;}

/* ── Hero ── */
.lec-hero{background:linear-gradient(135deg,var(--navy),#1a3a6b);border-radius:12px;padding:32px 36px;margin-bottom:28px;border-left:5px solid var(--red);}
.lec-badge{font-size:10px;letter-spacing:2px;color:var(--red);text-transform:uppercase;font-weight:700;margin-bottom:10px;}
.lec-hero h1{font-size:26px;font-weight:800;line-height:1.3;margin-bottom:10px;color:#fff;}
.lec-hero .lec-desc{font-size:14px;line-height:1.7;color:rgba(255,255,255,.75);margin-bottom:14px;}
.lec-meta{display:flex;gap:16px;flex-wrap:wrap;}
.lec-meta span{font-size:12px;color:rgba(255,255,255,.55);background:rgba(255,255,255,.07);padding:3px 10px;border-radius:12px;}

/* ── Objectives ── */
.objectives{background:rgba(10,124,140,.12);border:1px solid rgba(10,124,140,.3);border-radius:10px;padding:20px 24px;margin-bottom:24px;}
.objectives h3{font-size:14px;font-weight:700;color:var(--teal);margin-bottom:10px;}
.objectives ul{list-style:none;display:flex;flex-direction:column;gap:6px;}
.objectives li::before{content:"✓ ";color:var(--teal);font-weight:700;}
.objectives li{font-size:13.5px;color:var(--text);}

/* ── Section headings ── */
.sec-h2{font-size:20px;font-weight:700;color:var(--gold);margin:28px 0 10px;padding-bottom:6px;border-bottom:1px solid var(--border);}
.sec-h3{font-size:15px;font-weight:600;color:var(--teal);margin:18px 0 8px;}
.body-p{font-size:14px;line-height:1.8;color:var(--text);margin-bottom:12px;}

/* ── Cards ── */
.card{background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:22px 24px;margin-bottom:20px;}
.card h2{font-size:18px;font-weight:700;color:var(--gold);margin-bottom:14px;}
.card h3{font-size:14px;font-weight:600;color:var(--teal);margin:16px 0 8px;}
.card p{font-size:14px;line-height:1.8;color:var(--text);margin-bottom:10px;}

/* ── Callout boxes ── */
.callout{border-radius:8px;padding:14px 18px;margin:14px 0;font-size:13.5px;line-height:1.7;}
.callout strong{display:block;margin-bottom:4px;font-size:13px;}
.callout-key{background:rgba(244,168,50,.08);border-left:4px solid var(--gold);color:var(--text);}
.callout-key strong{color:var(--gold);}
.callout-info{background:rgba(10,124,140,.1);border-left:4px solid var(--teal);color:var(--text);}
.callout-info strong{color:var(--teal);}
.callout-warn{background:rgba(233,69,96,.08);border-left:4px solid var(--red);color:var(--text);}
.callout-warn strong{color:var(--red);}
.callout-tip{background:rgba(39,174,96,.08);border-left:4px solid var(--green);color:var(--text);}
.callout-tip strong{color:var(--green);}

/* ── Tables ── */
.tbl{width:100%;border-collapse:collapse;margin:14px 0;font-size:13px;}
.tbl th{background:var(--blue);color:#fff;padding:9px 12px;text-align:left;font-weight:600;}
.tbl td{padding:8px 12px;border-bottom:1px solid var(--border);color:var(--text);}
.tbl tr:nth-child(even) td{background:rgba(255,255,255,.02);}
.tbl tr:hover td{background:rgba(255,255,255,.04);}

/* ── Code blocks ── */
.code-wrap{position:relative;margin:14px 0;}
.code-wrap pre{background:var(--code-bg);border:1px solid var(--border);border-radius:8px;padding:16px 18px;overflow-x:auto;}
.code-wrap code{font-size:12.5px;line-height:1.7;color:#79c0ff;}
.copy-btn{position:absolute;top:8px;right:10px;background:rgba(255,255,255,.08);border:1px solid var(--border);border-radius:5px;padding:3px 10px;font-size:11px;color:var(--muted);cursor:pointer;}
.copy-btn:hover{background:rgba(255,255,255,.15);color:#fff;}

/* ── Concept grid ── */
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:14px 0;}
.grid3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;margin:14px 0;}
.grid4{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:14px 0;}
.gbox{background:var(--bg);border-radius:8px;padding:16px;border:1px solid var(--border);}
.gbox.teal{border-color:var(--teal);}
.gbox.gold{border-color:var(--gold);}
.gbox.green{border-color:var(--green);}
.gbox.red{border-color:var(--red);}
.gbox.purple{border-color:var(--purple);}
.gbox h4{font-size:13px;font-weight:700;color:var(--gold);margin-bottom:6px;}
.gbox p{font-size:12.5px;color:var(--muted);line-height:1.6;}

/* ── Comparison grid ── */
.cmp-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:14px 0;}
.cmp-card{background:var(--bg);border:1px solid var(--border);border-radius:8px;padding:16px;}
.cmp-card h4{font-size:13px;font-weight:700;margin-bottom:10px;}
.cmp-card ul{list-style:none;display:flex;flex-direction:column;gap:5px;}
.cmp-card li{font-size:12.5px;color:var(--muted);}
.cmp-card li::before{content:"• ";color:var(--teal);}

/* ── Summary grid ── */
.sum-grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;margin:14px 0;}
.sum-card{background:var(--bg);border:1px solid var(--teal);border-radius:8px;padding:14px;}
.sum-card .icon{font-size:20px;margin-bottom:6px;}
.sum-card h4{font-size:13px;font-weight:700;color:var(--gold);margin-bottom:5px;}
.sum-card p{font-size:12px;color:var(--muted);line-height:1.6;}

/* ── Tags / badges ── */
.tag-row{display:flex;gap:8px;flex-wrap:wrap;margin:10px 0;}
.tag{display:inline-block;padding:3px 10px;border-radius:12px;font-size:11px;font-weight:600;}
.tag-teal{background:rgba(10,124,140,.2);color:var(--teal);}
.tag-red{background:rgba(233,69,96,.2);color:var(--red);}
.tag-gold{background:rgba(244,168,50,.2);color:var(--gold);}
.tag-green{background:rgba(39,174,96,.2);color:var(--green);}

/* ── Exercise ── */
.exercise{background:rgba(123,47,190,.1);border:1px solid rgba(123,47,190,.3);border-radius:10px;padding:18px 22px;margin:16px 0;}
.exercise h3{font-size:14px;font-weight:700;color:var(--purple);margin-bottom:10px;}
.exercise ol{padding-left:18px;display:flex;flex-direction:column;gap:6px;}
.exercise li{font-size:13.5px;color:var(--text);line-height:1.7;}

/* ── Light mode ── */
body.light{--bg:#f0f2f5;--surface:#fff;--border:#d0d7de;--text:#1f2328;--muted:#57606a;--code-bg:#f6f8fa;--navy:#1a3a6b;}
body.light #sidebar{background:#1a3a6b;}
body.light .lec-hero{background:linear-gradient(135deg,#1a3a6b,#0f1f3d);}

@media(max-width:768px){
  #sidebar{display:none;}
  #main,#topbar{margin-left:0;left:0;}
}
</style>
</head>
<body>

<aside id="sidebar">
  <div class="brand">
    <div class="course">CSAI601 &middot; Unit 2</div>
    <h2>Prompt Engineering</h2>
  </div>
  <nav>
    <div class="nav-section">Lectures</div>
    <a href="#" data-lec="L08" class="active"><span class="lnum">L08</span>&nbsp; Intro to Prompt Engineering</a>
    <a href="#" data-lec="L09"><span class="lnum">L09</span>&nbsp; Zero-Shot &amp; Few-Shot</a>
    <a href="#" data-lec="L10"><span class="lnum">L10</span>&nbsp; Chain-of-Thought</a>
    <a href="#" data-lec="L11"><span class="lnum">L11</span>&nbsp; Role, Persona &amp; Tone</a>
    <a href="#" data-lec="L12"><span class="lnum">L12</span>&nbsp; Structured Output</a>
    <a href="#" data-lec="L13"><span class="lnum">L13</span>&nbsp; Context Management</a>
    <a href="#" data-lec="L14"><span class="lnum">L14</span>&nbsp; Evaluation &amp; Iteration</a>
    <a href="#" data-lec="L15"><span class="lnum">L15</span>&nbsp; Lab: Prompt Optimisation</a>
  </nav>
  <div class="prog">Unit 2 of 5 &middot; 8 Lectures &middot; 8 Hours</div>
</aside>

<div id="topbar">
  <span class="tb-title" id="tb-title">L08 &mdash; Introduction to Prompt Engineering</span>
  <div class="tb-right">
    <input class="search-input" id="search" placeholder="&#128269; Search notes..." />
    <button class="theme-btn" id="theme-btn">&#9728;</button>
  </div>
</div>

<div id="main">
"""

# ─── helper to build a lecture section ───────────────────────────────────────

def hero(lec_id, badge, title, desc, meta_items):
    meta = "".join(f"<span>{m}</span>" for m in meta_items)
    return (f'<section class="lecture" data-lec="{lec_id}">\n'
            f'<div class="lec-wrap">\n'
            f'<div class="lec-hero">\n'
            f'  <div class="lec-badge">{badge}</div>\n'
            f'  <h1>{title}</h1>\n'
            f'  <div class="lec-desc">{desc}</div>\n'
            f'  <div class="lec-meta">{meta}</div>\n'
            f'</div>\n')

def objectives(items):
    lis = "\n".join(f"    <li>{i}</li>" for i in items)
    return f'<div class="objectives"><h3>&#127919; Learning Objectives</h3><ul>\n{lis}\n</ul></div>\n'

def h2(text): return f'<h2 class="sec-h2">{text}</h2>\n'
def h3(text): return f'<h3 class="sec-h3">{text}</h3>\n'
def p(text):  return f'<p class="body-p">{text}</p>\n'

def callout(kind, label, text):
    return f'<div class="callout callout-{kind}"><strong>{label}</strong>{text}</div>\n'

def table(headers, rows):
    ths = "".join(f"<th>{h}</th>" for h in headers)
    trs = ""
    for row in rows:
        tds = "".join(f"<td>{c}</td>" for c in row)
        trs += f"<tr>{tds}</tr>\n"
    return f'<table class="tbl"><thead><tr>{ths}</tr></thead><tbody>{trs}</tbody></table>\n'

def code(snippet, note=""):
    note_html = f'<p style="font-size:12px;color:var(--muted);margin-top:6px;">{note}</p>' if note else ""
    escaped = snippet.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
    return (f'<div class="code-wrap"><button class="copy-btn" onclick="copyCode(this)">Copy</button>'
            f'<pre><code>{escaped}</code></pre></div>{note_html}\n')

def grid4(boxes):
    """boxes = list of (css_class, title, body)"""
    items = ""
    for cls, title, body in boxes:
        items += f'<div class="gbox {cls}"><h4>{title}</h4><p>{body}</p></div>\n'
    return f'<div class="grid4">{items}</div>\n'

def grid3(boxes):
    items = ""
    for cls, title, body in boxes:
        items += f'<div class="gbox {cls}"><h4>{title}</h4><p>{body}</p></div>\n'
    return f'<div class="grid3">{items}</div>\n'

def grid2(boxes):
    items = ""
    for cls, title, body in boxes:
        items += f'<div class="gbox {cls}"><h4>{title}</h4><p>{body}</p></div>\n'
    return f'<div class="grid2">{items}</div>\n'

def cmp(left_title, left_items, right_title, right_items, l_color="var(--red)", r_color="var(--green)"):
    def li(items): return "".join(f"<li>{i}</li>" for i in items)
    return (f'<div class="cmp-grid">'
            f'<div class="cmp-card"><h4 style="color:{l_color}">{left_title}</h4><ul>{li(left_items)}</ul></div>'
            f'<div class="cmp-card"><h4 style="color:{r_color}">{right_title}</h4><ul>{li(right_items)}</ul></div>'
            f'</div>\n')

def summary(cards):
    """cards = list of (icon, title, body)"""
    items = ""
    for icon, title, body in cards:
        items += f'<div class="sum-card"><div class="icon">{icon}</div><h4>{title}</h4><p>{body}</p></div>\n'
    return f'<div class="sum-grid">{items}</div>\n'

def exercise(title, steps):
    lis = "".join(f"<li>{s}</li>" for s in steps)
    return f'<div class="exercise"><h3>&#128396; {title}</h3><ol>{lis}</ol></div>\n'

def card_open(): return '<div class="card">\n'
def card_close(): return '</div>\n'
def lec_close(): return '</div></section>\n'  # closes lec-wrap + section

# ══════════════════════════════════════════════════════════════════════════════
# L08 — Introduction to Prompt Engineering
# ══════════════════════════════════════════════════════════════════════════════
L08  = hero("L08","Lecture 08 &middot; Unit 2",
             "Introduction to Prompt Engineering",
             "Understand what prompt engineering is, why it matters, and how to think about prompts as programs. Learn the anatomy of an effective prompt and when prompting is the right tool.",
             ["&#9200; 1 Hour","&#128218; CO2","&#127919; Foundation for Unit 2"])
L08 += objectives([
    "Define prompt engineering and explain its role in the LLM application stack",
    "Describe the four components of an effective prompt: instruction, context, input, output format",
    "Compare prompting vs fine-tuning across cost, speed, flexibility, and performance",
    "Apply Anthropic's core prompt engineering principles to a real task",
    "Identify common prompt anti-patterns and how to fix them",
])
L08 += h2("8.1 What Is Prompt Engineering?")
L08 += p("A <strong>prompt</strong> is any text you send to a language model as input. <strong>Prompt engineering</strong> is the systematic practice of designing, iterating, and optimising those inputs to reliably produce the desired outputs — without changing the model's weights.")
L08 += callout("key","Core Insight","An LLM is a frozen function — you cannot change its weights at inference time. The only lever you have is the input. Prompt engineering is the art of pulling that lever skillfully.")
L08 += h3("The Prompt-as-Program Metaphor")
L08 += table(["Prompt Component","Programming Analogy","Example"],[
    ["<strong>Instruction</strong>","Function signature / docstring","\"Summarise the following article in 3 bullet points.\""],
    ["<strong>Context</strong>","Global variables / imports","\"You are an expert in medical research. Audience: general public.\""],
    ["<strong>Input data</strong>","Function arguments","\"Article: {article_text}\""],
    ["<strong>Output format</strong>","Return type / schema","\"Respond in JSON with keys: summary, key_points, sentiment.\""],
])
L08 += h2("8.2 Why Prompt Engineering Matters")
L08 += p("The same model (Claude Sonnet, GPT-4, etc.) can produce wildly different results depending on how the prompt is written. Studies show that prompt variations can cause accuracy swings of <strong>30–50 percentage points</strong> on benchmark tasks — larger than the gap between model generations.")
L08 += cmp("Poor Prompt","Vague — 'Tell me about transformers';No audience or depth context;No output format;Result: generic Wikipedia answer;Inconsistent across runs".split(";"),
           "Engineered Prompt","Explain transformer self-attention;For a 3rd-year CS student;One analogy + one equation;Under 200 words;Result: precise, consistent, actionable".split(";"))
L08 += h2("8.3 Prompting vs Fine-Tuning")
L08 += table(["Dimension","Prompting","Fine-Tuning"],[
    ["<strong>Cost</strong>","Zero — just API calls","$100s–$10,000s in compute"],
    ["<strong>Speed to deploy</strong>","Minutes — iterate live","Days to weeks"],
    ["<strong>New knowledge</strong>","Cannot add new facts (use RAG)","Can inject domain knowledge"],
    ["<strong>Style/format</strong>","Good with clear instructions","Excellent — baked in"],
    ["<strong>Consistency</strong>","Varies unless engineered carefully","Very consistent"],
    ["<strong>When to use</strong>","Most tasks — try first","High-volume, style-critical tasks"],
])
L08 += callout("info","Rule of Thumb","Always exhaust prompt engineering before considering fine-tuning. 90% of tasks can be solved with well-engineered prompts. Fine-tune only when you have 1,000+ labelled examples, a consistent style requirement, and proven prompting has hit a ceiling.")
L08 += h2("8.4 Anatomy of an Effective Prompt")
L08 += grid4([
    ("teal","Instruction","What task should Claude perform? Be explicit: classify, summarise, translate, extract. Never vague."),
    ("gold","Context","Background info: who you are, the domain, constraints, relevant history, audience."),
    ("green","Input Data","The text, code, or data to operate on. Delimit with XML tags: &lt;document&gt;...&lt;/document&gt;"),
    ("red","Output Format","Exact schema, length limit, tone, language. Show a template if needed."),
])
L08 += callout("warn","Anti-Patterns to Avoid",
    "<ul style='margin-top:8px;padding-left:18px;line-height:2'>"
    "<li><strong>Vague task:</strong> 'Help me with this' → no outcome defined</li>"
    "<li><strong>Missing format:</strong> 'Give me a list' → count and structure unspecified</li>"
    "<li><strong>No audience:</strong> Claude defaults to generic register</li>"
    "<li><strong>Overloaded task:</strong> asking for 5 outputs in one prompt</li>"
    "<li><strong>Context dump:</strong> pasting 10,000 tokens without prioritising key facts</li></ul>")
L08 += h2("8.5 Anthropic's Prompt Engineering Principles")
L08 += table(["Principle","Description","Quick Example"],[
    ["Be specific","Precise instructions outperform vague ones","'Summarise in exactly 3 bullet points' not 'summarise'"],
    ["Use XML tags","Claude trained on XML — tags improve parsing","Wrap inputs: &lt;document&gt;...&lt;/document&gt;"],
    ["Give reasoning room","CoT triggers improve complex task accuracy","Append 'Think step by step' before the question"],
    ["Show examples","2–3 demos beat long textual explanations","Include 1 example per output class"],
    ["Assign a role","Role priming activates knowledge clusters","'Act as a senior Python security engineer'"],
    ["Iterate systematically","Test on 10+ inputs; fix one thing at a time","Track score per prompt version"],
])
L08 += h2("8.6 The Prompt Engineering Workflow")
L08 += table(["Step","Action","Goal"],[
    ["1","Define success — write 3 ideal responses before drafting","Know what you're aiming for"],
    ["2","Write baseline — simplest possible prompt","Get an initial quality score"],
    ["3","Test on 10 diverse inputs: easy, edge, adversarial","Find failure patterns"],
    ["4","Categorise failures: hallucination / format / scope / tone","Understand root cause"],
    ["5","Fix root cause — ONE change at a time","Controlled improvement"],
    ["6","Re-test full suite — verify improvement, no regressions","Confirm the fix works"],
    ["7","Repeat until target quality or diminishing returns","Ship or fine-tune"],
])
L08 += h2("8.7 Working with XML Tags")
L08 += code(
    "<task>\nClassify the email into: Billing | Technical | Shipping | Other\n</task>\n\n"
    "<examples>\n  <example>\n    <email>My invoice is wrong this month.</email>\n    <label>Billing</label>\n  </example>\n"
    "  <example>\n    <email>App crashes when I try to upload.</email>\n    <label>Technical</label>\n  </example>\n</examples>\n\n"
    "<email>\n  My package was supposed to arrive 3 days ago.\n</email>",
    "XML tags tell Claude exactly where each component starts and ends — dramatically reducing parsing errors."
)
L08 += card_open()
L08 += "<h2>L08 Summary</h2>\n"
L08 += summary([
    ("📝","Prompt = Program","4 components: instruction, context, input, output format. Always write all four."),
    ("🚀","Prompt First","Try prompt engineering before fine-tuning. 90% of tasks solved at inference time."),
    ("🏷","Use XML Tags","Anthropic recommends XML-delimited inputs. Improves parsing, reduces errors."),
    ("🔁","Iterate Systematically","Test 10+ inputs. Categorise failures. Fix root cause. One change at a time."),
    ("🎯","Define Success First","Write ideal outputs before drafting the prompt. Know your target metric."),
    ("⚠","Avoid Anti-Patterns","Vague tasks, missing formats, context dumps — each costs quality."),
])
L08 += card_close()
L08 += lec_close()

# ══════════════════════════════════════════════════════════════════════════════
# L09 — Zero-Shot & Few-Shot Prompting
# ══════════════════════════════════════════════════════════════════════════════
L09  = hero("L09","Lecture 09 &middot; Unit 2",
             "Zero-Shot &amp; Few-Shot Prompting",
             "Learn when to rely on pre-training knowledge alone vs. when to steer with demonstrations. Master the full spectrum from zero-shot to many-shot, and apply bootstrap techniques when data is scarce.",
             ["&#9200; 1 Hour","&#128218; CO2","&#127919; Core Technique"])
L09 += objectives([
    "Explain the difference between zero-shot, one-shot, few-shot, and many-shot prompting",
    "Write zero-shot prompts that leave no room for misinterpretation",
    "Design high-quality few-shot demonstrations: coverage, realism, consistency",
    "Apply many-shot prompting using Claude's 200K context window",
    "Bootstrap demonstrations when no labelled data is available",
])
L09 += h2("9.1 The Prompting Spectrum")
L09 += p("Before models see a single example from you, they already carry billions of training patterns inside their weights. <strong>Zero-shot prompting</strong> exploits that prior knowledge directly; <strong>few-shot prompting</strong> steers it with handpicked demonstrations embedded in the prompt itself.")
L09 += grid4([
    ("teal","Zero-Shot","No examples. Pure instruction. Works when the task is unambiguous and well-covered by training data."),
    ("gold","One-Shot","A single demonstration to anchor format and tone. Best when you have exactly one good example."),
    ("green","Few-Shot (2–8)","Multiple input-output pairs. Model generalises the pattern to novel inputs. Most common in production."),
    ("purple","Many-Shot (20+)","Long-context window packed with examples. Approaches fine-tuning quality for narrow tasks."),
])
L09 += h2("9.2 Zero-Shot Prompting")
L09 += p("Zero-shot works because LLMs generalise from pre-training. The craft is in framing the task completely and unambiguously in a single instruction block.")
L09 += h3("Five Elements of a Strong Zero-Shot Prompt")
L09 += table(["Element","Weak Version","Strong Version"],[
    ["Task name","Tell me about this","Summarise this review in exactly 2 sentences"],
    ["Output format","Give keywords","List 5 keywords, comma-separated, all lowercase"],
    ["Audience","Explain neural nets","Explain neural nets to a high-school student with no maths background"],
    ["Constraints","Write an email","Write a 3-sentence follow-up email; professional tone; no jargon"],
    ["Role","Check my code","Act as a senior Python security engineer. Find vulnerabilities."],
])
L09 += callout("warn","When Zero-Shot Fails",
    "<ul style='margin-top:8px;padding-left:18px;line-height:2'>"
    "<li>Task demands a precise proprietary schema (custom JSON, specific table layout)</li>"
    "<li>Domain is highly specialised and under-represented in training data</li>"
    "<li>Desired style is idiosyncratic (brand voice, specific author cadence)</li>"
    "<li>Multi-step reasoning with exact intermediate steps is required</li>"
    "</ul><p style='margin-top:8px;'>In these situations, provide examples (few-shot) or explicit reasoning steps (chain-of-thought).</p>")
L09 += h2("9.3 Few-Shot Prompting")
L09 += p("Few-shot prompting embeds worked examples as Human/Assistant turns before the actual question. Claude learns the <strong>format</strong>, <strong>tone</strong>, and <strong>reasoning style</strong> from the demonstrations and applies that pattern to the new input.")
L09 += h3("Example: Support Ticket Classification")
L09 += code(
    "System: Classify support tickets into: Billing | Technical | Shipping | Other.\n\n"
    "H: \"My invoice shows double charge.\"    A: Billing\n"
    "H: \"App crashes on iOS 17.\"             A: Technical\n"
    "H: \"Package not delivered in 10 days.\"  A: Shipping\n\n"
    "H: \"I want to cancel my subscription.\"\n"
    "A:",
    "Claude outputs: Billing — correctly generalising from 3 demonstrations."
)
L09 += h3("Rules for Designing Good Demonstrations")
L09 += table(["Rule","Why It Matters"],[
    ["Cover the output space","Show at least one example per class/label — Claude learns all valid outputs"],
    ["Use realistic inputs","Toy examples generalise poorly to real data distributions"],
    ["Keep format perfectly consistent","Any deviation in example format leaks into Claude's output"],
    ["Order by difficulty","Easy cases first, edge cases last (closest to the real query)"],
    ["Label accurately","One wrong label hurts more than having no examples at all"],
    ["Match the domain","Examples from a different domain confuse rather than help"],
])
L09 += h2("9.4 Format Priming")
L09 += p("Use demonstrations purely to lock in output structure, not to teach the task semantics. This is useful when Claude already understands the task but needs to match a specific format.")
L09 += code(
    "Review: \"Good laptop but fan is loud.\"\n"
    "Output:\n  summary: decent performance\n  pros: [portability, battery]\n  cons: [fan noise]\n  score: 6/10\n\n"
    "Review: \"Best phone I have owned. Camera is stunning.\"\n"
    "Output:\n  summary: excellent all-rounder\n  pros: [camera, display, build]\n  cons: []\n  score: 9/10\n\n"
    "Review: {{USER_REVIEW}}\n"
    "Output:",
    "The demos teach format here, not task semantics — Claude already knows sentiment analysis."
)
L09 += h2("9.5 Many-Shot &amp; Bootstrap")
L09 += p("Claude supports context windows up to 200K tokens, enabling 50–500 demonstrations in a single prompt. Anthropic research shows many-shot can match or exceed fine-tuning on classification and extraction tasks — without any gradient updates.")
L09 += callout("tip","Bootstrap Technique — When You Have No Data",
    "Step 1: Ask Claude to generate 5–10 realistic examples of input + ideal output.<br>"
    "Step 2: Review and correct the generated examples.<br>"
    "Step 3: Use the curated examples as your few-shot demonstrations.<br>"
    "This works surprisingly well and lets you iterate on demonstration quality before committing to a labelled dataset.")
L09 += h2("9.6 Choosing: Zero-Shot vs Few-Shot")
L09 += table(["Factor","Lean Zero-Shot","Lean Few-Shot"],[
    ["Task familiarity","Common, well-defined task","Novel or specialised task"],
    ["Output format","Free-form prose is fine","Strict schema required"],
    ["Token budget","Tight (cost sensitive)","Budget allows demonstration overhead"],
    ["Data availability","No labelled examples","Have 2–20 quality examples"],
    ["Iteration phase","Rapid prototyping","Production system tuning"],
])
L09 += callout("info","Practical Workflow","Start zero-shot. If quality is insufficient after 3 iterations, add 2–3 examples (few-shot). If still insufficient, move to chain-of-thought (L10) or fine-tuning.")
L09 += card_open()
L09 += "<h2>L09 Summary</h2>\n"
L09 += summary([
    ("🔵","Zero-Shot","Fast and cheap. Works for common tasks when instruction is crisp and complete."),
    ("🟡","Few-Shot (2–8)","Locks format and style. Essential when zero-shot produces wrong structure or class."),
    ("🟢","Many-Shot (20+)","Near fine-tuning quality in 200K context. No training needed."),
    ("⚙","Bootstrap","No labelled data? Generate examples with Claude first, then use as demonstrations."),
    ("📐","Format Priming","Use demos just to lock in output structure when task semantics are clear."),
    ("📊","Decision Guide","Zero-shot first; escalate to few-shot only when quality is insufficient."),
])
L09 += card_close()
L09 += lec_close()

# ══════════════════════════════════════════════════════════════════════════════
# L10 — Chain-of-Thought & Reasoning
# ══════════════════════════════════════════════════════════════════════════════
L10  = hero("L10","Lecture 10 &middot; Unit 2",
             "Chain-of-Thought &amp; Reasoning Prompts",
             "Teach Claude to think before it answers. Learn zero-shot CoT, few-shot CoT, self-consistency decoding, and the Extended Thinking API for the hardest reasoning tasks.",
             ["&#9200; 1 Hour","&#128218; CO2","&#127919; Advanced Technique"])
L10 += objectives([
    "Explain why chain-of-thought prompting improves accuracy on complex tasks",
    "Apply zero-shot CoT triggers effectively across different task types",
    "Design few-shot CoT demonstrations that match target reasoning depth",
    "Implement self-consistency decoding in Python to reduce variance",
    "Use the Extended Thinking API for Claude's hardest reasoning tasks",
])
L10 += h2("10.1 Why Reasoning Prompts Matter")
L10 += p("Large language models are next-token predictors. When asked a multi-step question directly, they produce an answer token by token without any explicit reasoning buffer — leading to brittle results on problems that require arithmetic, logical deduction, or sequential planning.")
L10 += callout("key","Key Finding (Wei et al., 2022)","Adding 'Let's think step by step.' to a prompt improved GPT-3 accuracy on grade-school math from 17.7% to 78.7%. The same principle applies to Claude — and the improvement is largest on the hardest problems.")
L10 += h2("10.2 Chain-of-Thought Variants")
L10 += grid4([
    ("teal","Zero-Shot CoT","Append 'Think step by step' — no examples needed. Activates latent reasoning capability in any large LLM."),
    ("gold","Few-Shot CoT","Provide demonstrations that include full reasoning chains, not just final answers. Model mimics reasoning style."),
    ("green","Self-Consistency","Sample N reasoning paths, take majority vote on the final answer. Reduces variance by 5–15%."),
    ("purple","Extended Thinking","Claude 3.7+ allocates scratchpad tokens before answering. Best for hardest math, code, planning."),
])
L10 += h2("10.3 Zero-Shot CoT in Practice")
L10 += h3("Effective Trigger Phrases")
L10 += table(["Phrase","Best Use"],[
    ["Let's think step by step.","General reasoning, maths, logic puzzles — most widely tested"],
    ["Walk me through your reasoning.","Analytical tasks, diagnoses, recommendations"],
    ["First, identify all relevant facts. Then solve.","Structured problem-solving with known unknowns"],
    ["Before answering, list all assumptions.","Ambiguous problems with hidden constraints"],
    ["Show your work.","Calculations, proofs, derivations"],
])
L10 += h3("Before vs After CoT")
L10 += code(
    "WITHOUT CoT:\nQ: Train A leaves Delhi at 9am at 80 km/h. Train B leaves Mumbai at 10am\n"
    "   at 100 km/h toward Delhi. Distance 1400 km. When do they meet?\nA: 2:30pm  [WRONG]\n\n"
    "WITH 'Let's think step by step.':\nA: 1. In the first hour, Train A covers 80 km. Gap at 10am = 1320 km.\n"
    "   2. Both moving toward each other: closing speed = 80+100 = 180 km/h\n"
    "   3. Time to close 1320 km: 1320/180 = 7.33 h = 7 hr 20 min\n"
    "   4. 10am + 7h 20min = 5:20pm\n   Answer: 5:20pm  [CORRECT]",
    "The reasoning chain also makes errors visible and correctable — you can see exactly where logic failed."
)
L10 += h2("10.4 Few-Shot CoT")
L10 += p("Provide demonstrations where the reasoning chain is shown explicitly. Claude will mimic your reasoning style and depth — so match chain complexity to your actual task.")
L10 += code(
    "Q: Roger has 5 balls. He buys 2 cans of 3 balls each. How many balls?\n"
    "A: Roger starts with 5. He buys 2x3=6 more. Total: 5+6=11. Answer: 11.\n\n"
    "Q: A juggler has 16 balls. Half are golf balls. Half of golf balls are blue.\n   How many blue golf balls?\n"
    "A: Total: 16. Golf balls: 16/2=8. Blue golf balls: 8/2=4. Answer: 4.\n\n"
    "Q: [YOUR QUESTION]\nA:",
    "Design tip: make reasoning chains match the complexity of your target tasks. Simple 2-step demos don't transfer to 6-step problems."
)
L10 += h2("10.5 Self-Consistency Decoding")
L10 += p("Instead of taking a single reasoning path, generate multiple chains (temperature &gt; 0) and take a majority vote on the final answer. Typically improves accuracy by 5–15% on arithmetic and logical reasoning benchmarks.")
L10 += code(
    "import anthropic, re\nfrom collections import Counter\n\nclient = anthropic.Anthropic()\n"
    "question = 'What is 17% of 340? Let\\'s think step by step.'\n\nanswers = []\n"
    "for _ in range(5):  # sample 5 reasoning paths\n"
    "    r = client.messages.create(\n        model='claude-opus-4-5',\n"
    "        max_tokens=300,\n        messages=[{'role':'user','content': question}]\n    )\n"
    "    nums = re.findall(r'\\d+\\.?\\d*', r.content[0].text)\n"
    "    if nums: answers.append(nums[-1])\n\n"
    "final = Counter(answers).most_common(1)[0][0]\nprint('Majority answer:', final)  # 57.8",
    "Sampling 5 paths and voting reduces the chance of a confident-but-wrong single answer."
)
L10 += h2("10.6 Extended Thinking API")
L10 += p("Claude 3.7 Sonnet exposes a <code>thinking</code> block — allocated compute tokens used for internal scratchpad reasoning before the final response is generated. The scratchpad is visible in the response for debugging.")
L10 += code(
    "response = client.messages.create(\n    model='claude-sonnet-4-5',\n    max_tokens=16000,\n"
    "    thinking={\n        'type': 'enabled',\n        'budget_tokens': 10000   # scratchpad allocation\n    },\n"
    "    messages=[{'role':'user','content':'Solve: ...'}]\n)\n\n"
    "for block in response.content:\n    if block.type == 'thinking':\n"
    "        print('Scratchpad:', block.thinking)\n    elif block.type == 'text':\n"
    "        print('Final answer:', block.text)",
    "Cost: ~3x token overhead. Use for complex math, competitive coding, long-horizon planning, scientific reasoning."
)
L10 += h2("10.7 PREP Reasoning Framework")
L10 += table(["Step","Instruction to Claude","Purpose"],[
    ["P — Problem","Restate the problem in your own words","Confirms correct understanding before solving"],
    ["R — Relevant","List all known quantities and constraints","Surfaces hidden assumptions and edge cases"],
    ["E — Execution","Solve step by step, showing each operation","Creates an auditable reasoning chain"],
    ["P — Plausibility","Sanity-check the answer against intuition","Catches arithmetic errors and wrong units"],
])
L10 += card_open()
L10 += "<h2>L10 Summary</h2>\n"
L10 += summary([
    ("💡","Zero-Shot CoT","'Think step by step' unlocks latent reasoning. Works across all major LLMs."),
    ("📖","Few-Shot CoT","Show reasoning chains in demos. Model mimics both depth and style."),
    ("📊","Self-Consistency","Sample N paths, take majority vote. +5–15% accuracy. Reduces variance."),
    ("⚙","Extended Thinking","Claude 3.7 built-in scratchpad. Best for hardest reasoning. ~3x token cost."),
    ("🔢","PREP Framework","Problem → Relevant facts → Execution → Plausibility. Structured approach for any hard problem."),
    ("✅","When CoT Helps","Multi-step maths, logical deduction, planning, causal reasoning. Less useful for simple factual recall."),
])
L10 += card_close()
L10 += lec_close()

# ══════════════════════════════════════════════════════════════════════════════
# L11 — Role, Persona & Tone Control
# ══════════════════════════════════════════════════════════════════════════════
L11  = hero("L11","Lecture 11 &middot; Unit 2",
             "Role, Persona &amp; Tone Control",
             "Shape who Claude is and how it speaks. Build consistent multi-turn personas, calibrate tone across five dimensions, and target specific audiences for maximum clarity.",
             ["&#9200; 1 Hour","&#128218; CO2","&#127919; Persona Design"])
L11 += objectives([
    "Explain why role assignment activates knowledge clusters in LLMs",
    "Build a complete persona specification: identity, expertise, communication rules, constraints",
    "Control five tone dimensions: formality, brevity, hedging, empathy, technical depth",
    "Calibrate content to a specified audience effectively",
    "Maintain persona consistency across a long multi-turn conversation",
])
L11 += h2("11.1 Why Role Assignment Works")
L11 += p("Assigning a role to Claude does more than change its tone — it activates a cluster of knowledge, terminology, values, and communication patterns associated with that role in Claude's training. A senior cardiologist, a startup founder, and a high-school teacher will explain 'cardiac risk' in structurally different ways, and so will Claude when primed with each role.")
L11 += grid4([
    ("teal","Professional Roles","Doctor, lawyer, engineer, teacher — activates domain vocabulary and epistemic standards."),
    ("gold","Creative Roles","Novelist, screenwriter, copywriter — unlocks narrative voice and creative latitude."),
    ("green","Functional Roles","Critic, devil's advocate, fact-checker — shapes the evaluative lens Claude applies."),
    ("purple","Hybrid Roles","Stack roles for precision: 'UX designer with a behavioural psychology background.'"),
])
L11 += h2("11.2 Building a Full Persona")
L11 += p("A persona is richer than a role. It combines identity, expertise, personality, communication style, and constraints into a coherent character Claude maintains across a conversation.")
L11 += code(
    "You are Priya, a senior data scientist at a B2B SaaS company.\n\n"
    "Identity:\n- 8 years experience in ML, specialising in churn prediction\n"
    "- Direct communication style — no filler phrases\n- Uses concrete numbers over vague adjectives\n\n"
    "Expertise:\n- Python, SQL, scikit-learn, XGBoost, Spark\n"
    "- Familiar with Salesforce, Mixpanel, Amplitude\n\n"
    "Communication rules:\n- Always ask for business context before going technical\n"
    "- When uncertain, say so explicitly rather than guessing\n"
    "- Offer 2-3 options with trade-offs, never a single answer\n\n"
    "Do NOT:\n- Use marketing language ('game-changing', 'synergy')\n"
    "- Recommend paid tools when free alternatives exist",
    "Persona = Identity + Expertise + Communication Rules + Constraints. Specify all four layers."
)
L11 += h2("11.3 Five Tone Dimensions")
L11 += table(["Dimension","Range","How to Specify"],[
    ["Formality","Casual → Professional → Academic","'Write in a casual, conversational tone suitable for a Slack message'"],
    ["Brevity","Terse → Balanced → Expansive","'Be concise. Maximum 3 sentences per response.'"],
    ["Hedging","Confident → Cautious → Neutral","'State conclusions directly. Do not hedge with \"perhaps\" or \"it seems\".'"],
    ["Empathy","Clinical → Warm → Supportive","'Acknowledge the user's frustration before solving.'"],
    ["Technical depth","Lay → Intermediate → Expert","'Assume the reader has a CS degree but no ML background.'"],
])
L11 += h3("Layered Tone Specification")
L11 += code(
    "Write customer support responses with:\n- Tone: warm, empathetic, professional\n"
    "- Formality: semi-formal (no slang; contractions allowed)\n- Length: 3-5 sentences maximum\n\n"
    "Structure (always follow):\n  Sentence 1: acknowledge the specific issue\n"
    "  Sentences 2-3: provide the solution steps\n  Final sentence: warm closing with next step\n\n"
    "Forbidden phrases:\n- 'I understand your frustration' (overused)\n"
    "- 'No problem!' (too casual)\n- 'Going forward' (corporate jargon)",
    "Forbidden phrase lists are often more robust than positive tone descriptions."
)
L11 += h2("11.4 Audience Calibration")
L11 += p("The same content needs radically different framing depending on who reads it. Explicitly specifying your audience is one of the highest-leverage prompt improvements.")
L11 += table(["Audience","Prompt Modifier","What Changes"],[
    ["5-year-old","'Explain like I'm 5'","Simple words, analogies, no jargon, short sentences"],
    ["Domain expert","'Assume PhD-level background in X'","Technical depth, field-specific terms, dense information"],
    ["C-suite executive","'2-minute read; business impact only'","Strategic framing, ROI focus, no implementation details"],
    ["Journalist","'Educated general reader; no assumed prior'","Clear prose, concrete examples, no unexplained acronyms"],
    ["Developer","'Technical audience; include code examples'","Code-first, concise explanation"],
])
L11 += h2("11.5 Maintaining Persona Across Turns")
L11 += table(["Technique","How","When to Use"],[
    ["System prompt anchoring","Full persona in system prompt — persists automatically","Always — the baseline"],
    ["Explicit reminders","Append '[Respond as Priya]' to user turns","Long conversations (10+ turns)"],
    ["Negative constraints","List forbidden behaviors explicitly","More robust than positive descriptions"],
    ["Sample exchanges","Include 2 Q&amp;A turns inside the system prompt","When tone is hard to describe verbally"],
])
L11 += callout("warn","Ethics Boundary","Claude will not maintain personas designed to circumvent its safety guidelines. Never design personas intended to bypass content policies — the persona will be abandoned when it conflicts with Claude's values.")
L11 += cmp("Poor Persona Design",
    ["You are an AI assistant.","Be helpful and friendly.","Answer questions accurately.","(Too vague — no real constraint. Claude defaults to generic responses. Persona adds no value.)"],
    "Strong Persona Design",
    ["You are Arjun, Level 1 API support specialist.","Max 100 words per response.","Always number your steps.","Escalate with TKT-XXXXX if unresolved in 2 exchanges.","(Specific constraints that actually shape output differently from default.)"])
L11 += card_open()
L11 += "<h2>L11 Summary</h2>\n"
L11 += summary([
    ("🌟","Role Assignment","Activates knowledge clusters. Stack roles for precision: domain + function."),
    ("🤖","Persona Design","Identity + expertise + communication rules + constraints = stable character."),
    ("🎙","Tone Control","Formality, brevity, hedging, empathy, depth — all specifiable and combinable."),
    ("👤","Audience","Matching content complexity to the reader is the highest-leverage single edit."),
    ("🔒","Persona Anchoring","System prompt + forbidden list + sample exchanges = consistent multi-turn persona."),
    ("⚠","Ethics Boundary","Personas cannot override Claude's values. Design responsibly."),
])
L11 += card_close()
L11 += lec_close()

# ══════════════════════════════════════════════════════════════════════════════
# L12 — Structured Output & Format Control
# ══════════════════════════════════════════════════════════════════════════════
L12  = hero("L12","Lecture 12 &middot; Unit 2",
             "Structured Output &amp; Format Control",
             "Make Claude produce machine-readable, precisely formatted responses every time. Master JSON schema enforcement, XML output, length control, and production-grade validation patterns.",
             ["&#9200; 1 Hour","&#128218; CO2","&#127919; Production Skill"])
L12 += objectives([
    "Enforce JSON output using three distinct techniques with increasing reliability",
    "Use Pydantic validation with an automatic retry loop for near-100% format compliance",
    "Design XML and custom delimited output formats for downstream systems",
    "Control output length and density with word limits, sentence counts, and section specs",
    "Build a production format-compliance rate monitor",
])
L12 += h2("12.1 Why Structured Output Matters in Production")
L12 += p("In production applications, Claude's output is rarely read by a human directly — it feeds downstream systems: databases, APIs, UI renderers, workflow automations. If the output format is inconsistent, the whole pipeline breaks regardless of content quality.")
L12 += callout("key","The Golden Rule","Any system that parses Claude's output programmatically must specify the output format explicitly in the prompt. Never rely on implicit formatting — what works 95% of the time fails 5% and breaks your application.")
L12 += h2("12.2 JSON Output — Three Techniques")
L12 += table(["Technique","How","Reliability"],[
    ["Explicit schema instruction","Paste the JSON schema in the prompt; say 'Return ONLY valid JSON'","Good — 90–95%"],
    ["Seed the assistant turn","Start the assistant turn with '{' to force JSON opening","Better — 95–98%"],
    ["System prompt mode","System: 'You output only valid JSON. No extra text.'","Best — 97–99%"],
    ["Validation + retry (recommended)","Catch JSONDecodeError; feed error back; retry up to 3 times","Near 100%"],
])
L12 += h3("JSON Output with Schema")
L12 += code(
    "System: You output only valid JSON. No extra text, no code fences.\n\n"
    "Schema:\n{\n  \"name\": string,\n  \"date\": \"YYYY-MM-DD\",\n"
    "  \"amount\": number,\n  \"currency\": \"USD\"|\"EUR\"|\"INR\"\n}\n\n"
    "Text: \"Received payment of Rs.5,000 from Amit on 12 March 2025.\"\n\n"
    "Expected output:\n{\"name\":\"Amit\",\"date\":\"2025-03-12\",\"amount\":5000,\"currency\":\"INR\"}",
    "Always validate immediately with json.loads() — never assume success."
)
L12 += h2("12.3 Pydantic Validation + Retry Pattern")
L12 += code(
    "from pydantic import BaseModel, ValidationError\nimport json, anthropic\n\n"
    "class Ticket(BaseModel):\n    category: str\n    priority: int  # 1-5\n"
    "    summary: str\n    tags: list[str]\n\nclient = anthropic.Anthropic()\n\n"
    "def extract_ticket(text: str, retries: int = 3) -> Ticket:\n"
    "    for attempt in range(retries):\n"
    "        r = client.messages.create(\n            model='claude-opus-4-5', max_tokens=300,\n"
    "            system='Output only valid JSON matching the Ticket schema.',\n"
    "            messages=[{'role':'user','content': text}]\n        )\n"
    "        try:\n            return Ticket(**json.loads(r.content[0].text))\n"
    "        except (json.JSONDecodeError, ValidationError) as e:\n"
    "            if attempt == retries - 1: raise\n"
    "            text = f'Error: {e}. Fix and retry.\\n{text}'",
    "Feeding the exact error message back to Claude lets it self-correct on retry. Reaches near 100% compliance."
)
L12 += h2("12.4 XML and Custom Formats")
L12 += h3("XML Output (for nested/hierarchical data)")
L12 += code(
    "Return in this exact XML structure:\n<analysis>\n"
    "  <sentiment>positive|negative|neutral</sentiment>\n"
    "  <confidence>0.0 to 1.0</confidence>\n  <reasons>\n"
    "    <reason>TEXT</reason>\n  </reasons>\n</analysis>",
    "XML is ideal for nested structures. Claude has a natural affinity for XML from its training."
)
L12 += h3("Custom Pipe-Delimited Format")
L12 += code(
    "Return each finding on a new line in this format:\nSEVERITY|COMPONENT|DESCRIPTION\n\n"
    "Example:\nHIGH|AuthService|JWT tokens are not expiring\nMEDIUM|Database|Connection pool not releasing",
    "Pipe-delimited formats are easy to parse line-by-line and work well for ETL pipelines."
)
L12 += h2("12.5 Length &amp; Density Control")
L12 += table(["Control Type","Instruction Pattern","Example"],[
    ["Hard word limit","'In exactly N words'","'Summarise in exactly 50 words.'"],
    ["Sentence count","'In N sentences'","'Explain in 3 sentences.'"],
    ["Bullet count","'List exactly N points'","'Give exactly 5 action items.'"],
    ["Section spec","Per-section lengths","'Intro: 2 sentences. Details: 4 paragraphs. Summary: 1 sentence.'"],
    ["Format type","Named format","'Return a 2-column markdown table: Pros | Cons'"],
])
L12 += callout("warn","Hard Character Limits","Claude understands approximate word/sentence counts well. For hard character limits (SMS, tweet), always validate programmatically and retry with a tighter instruction if exceeded.")
L12 += card_open()
L12 += "<h2>L12 Summary</h2>\n"
L12 += summary([
    ("{}","JSON Output","Explicit schema + seed assistant turn. Always validate with Pydantic."),
    ("📄","XML / Custom","Show the exact template. XML for nested; pipe-delimited for tabular ETL."),
    ("📏","Length Control","Word/sentence/bullet counts. Hard limits need programmatic validation."),
    ("✅","Retry Loop","Catch parse errors. Feed error back to Claude. 3 retries = near 100%."),
    ("🏭","Production Rule","Instrument format compliance rate. Target >99% before shipping."),
    ("🔑","Golden Rule","Any downstream parser requires explicit format in the prompt — always."),
])
L12 += card_close()
L12 += lec_close()

# ══════════════════════════════════════════════════════════════════════════════
# L13 — Context Management & Long Conversations
# ══════════════════════════════════════════════════════════════════════════════
L13  = hero("L13","Lecture 13 &middot; Unit 2",
             "Context Management &amp; Long Conversations",
             "Work effectively within and beyond Claude's 200K token context window. Learn summarisation, chunking strategies, map-reduce patterns, and RAG basics to handle arbitrarily long sessions.",
             ["&#9200; 1 Hour","&#128218; CO2","&#127919; Architecture Skill"])
L13 += objectives([
    "Explain the 200K context window and the 'lost in the middle' phenomenon",
    "Choose appropriate context management strategies for different use cases",
    "Implement conversation summarisation with automatic history compression",
    "Apply map-reduce chunking for documents longer than the context window",
    "Design efficient system prompts that minimise per-call token cost",
])
L13 += h2("13.1 Understanding the Context Window")
L13 += p("The context window is the total number of tokens Claude can see at once — including the system prompt, all conversation history, and the current message. Claude Sonnet and Opus 4 support <strong>200K tokens</strong>, roughly equivalent to a 150,000-word novel or 600 pages of dense text.")
L13 += table(["Model","Context Window","Approx. Pages"],[
    ["Claude Haiku 4.5","200K tokens","~600 pages"],
    ["Claude Sonnet 4","200K tokens","~600 pages"],
    ["Claude Opus 4","200K tokens","~600 pages"],
])
L13 += callout("warn","The 'Lost in the Middle' Problem","Research shows LLMs recall information at the <strong>beginning and end</strong> of the context most reliably. Content in the middle of a very long context is retrieved less accurately. Design implication: place critical instructions in the system prompt AND just before the question.")
L13 += h2("13.2 Context Management Strategies")
L13 += grid4([
    ("teal","Sliding Window","Keep only the N most recent turns. Oldest turns are dropped. Simple but loses early context."),
    ("gold","Summarisation","Periodically compress history into a summary, replace raw turns. Preserves key facts cheaply."),
    ("green","RAG","Store turns in a vector DB. Retrieve the most relevant turns for each new message."),
    ("purple","Hierarchical Memory","Working memory (recent) + episodic (summaries) + semantic (facts) managed separately."),
])
L13 += h2("13.3 Conversation Summarisation")
L13 += code(
    "import anthropic\nclient = anthropic.Anthropic()\nMAX_TURNS = 10\n\n"
    "def summarise_history(history: list) -> str:\n"
    "    r = client.messages.create(\n        model='claude-haiku-4-5-20251001',\n        max_tokens=500,\n"
    "        messages=[*history,\n            {'role':'user',\n"
    "             'content':'Summarise: decisions made, facts established, open questions.'}]\n    )\n"
    "    return r.content[0].text\n\n"
    "def chat(history: list, user_msg: str) -> tuple:\n"
    "    if len(history) > MAX_TURNS * 2:\n        summary = summarise_history(history)\n"
    "        history = [{'role':'assistant','content': f'[Summary]\\n{summary}'}]\n"
    "    history.append({'role':'user','content': user_msg})\n"
    "    r = client.messages.create(model='claude-opus-4-5', max_tokens=1000, messages=history)\n"
    "    reply = r.content[0].text\n    history.append({'role':'assistant','content': reply})\n"
    "    return reply, history",
    "Cost tip: use cheap Haiku for summarisation; use Opus/Sonnet for the final responses."
)
L13 += h2("13.4 Document Chunking Strategies")
L13 += table(["Strategy","How","Best For"],[
    ["Fixed-size chunks","Split every N tokens with overlap","Vector search, embedding"],
    ["Semantic chunks","Split at paragraph/section boundaries","Q&amp;A, summarisation"],
    ["Hierarchical","Chapter → section → paragraph levels","Long-form document analysis"],
    ["Map-reduce","Process each chunk independently, combine","Summarisation, extraction"],
    ["Sliding window","Overlapping chunks (e.g., 500 tokens, 100 overlap)","When context spans chunk boundaries"],
])
L13 += h3("Map-Reduce Summarisation")
L13 += code(
    "def map_reduce_summarise(text: str, chunk_size: int = 50000) -> str:\n"
    "    words = text.split()\n"
    "    chunks = [' '.join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]\n\n"
    "    # Map: summarise each chunk with Haiku\n    summaries = []\n"
    "    for chunk in chunks:\n"
    "        r = client.messages.create(\n            model='claude-haiku-4-5-20251001', max_tokens=500,\n"
    "            messages=[{'role':'user','content':f'Summarise:\\n{chunk}'}]\n        )\n"
    "        summaries.append(r.content[0].text)\n\n"
    "    # Reduce: combine summaries with Opus\n"
    "    r = client.messages.create(\n        model='claude-opus-4-5', max_tokens=1000,\n"
    "        messages=[{'role':'user','content': 'Combine these summaries:\\n' + '\\n\\n'.join(summaries)}]\n    )\n"
    "    return r.content[0].text",
    "Use Haiku for the map phase (cheap/fast); Opus or Sonnet for the reduce phase (quality)."
)
L13 += h2("13.5 System Prompt Design for Long Sessions")
L13 += table(["Do","Avoid"],[
    ["State critical constraints once, clearly","Repeating the same instruction multiple times hoping it sticks"],
    ["Use numbered rules for easy reference","Long paragraph descriptions of behavior"],
    ["Include examples only when format is non-obvious","Many examples that inflate token cost on every call"],
    ["Define abbreviations and custom terms","Assuming Claude knows your internal terminology"],
    ["Keep system prompt under 2K tokens when possible","Dumping the entire product documentation"],
])
L13 += card_open()
L13 += "<h2>L13 Summary</h2>\n"
L13 += summary([
    ("🎀","200K Window","Large but not infinite. Critical info at top and bottom. Middle is less reliable."),
    ("📝","Summarisation","Compress old history. Haiku is cheap for summarisation. Preserve key facts."),
    ("📑","Chunking","Map-reduce for long docs. Semantic chunks for Q&A. Overlap prevents boundary loss."),
    ("⚙","System Prompt","Under 2K tokens. Numbered rules. Avoid repetition. Define custom terms."),
    ("🔍","RAG","Vector DB for long-lived agents. Retrieve top-K relevant chunks per query."),
    ("💡","Placement","Critical instructions: system prompt first, then repeat just before the question."),
])
L13 += card_close()
L13 += lec_close()

# ══════════════════════════════════════════════════════════════════════════════
# L14 — Prompt Evaluation & Iteration
# ══════════════════════════════════════════════════════════════════════════════
L14  = hero("L14","Lecture 14 &middot; Unit 2",
             "Prompt Evaluation &amp; Iteration",
             "Measure, test, and systematically improve prompt quality. Learn metrics by task type, LLM-as-judge patterns, A/B testing, and how to version-control prompts like production code.",
             ["&#9200; 1 Hour","&#128218; CO2","&#127919; Engineering Practice"])
L14 += objectives([
    "Choose the right evaluation metric for each task type (classification, generation, extraction)",
    "Build an LLM-as-judge evaluation pipeline using Haiku",
    "Run A/B prompt tests with multiple trials and interpret the results",
    "Apply the 7-step iterative improvement cycle to any failing prompt",
    "Version-control prompts with performance metadata in a git repository",
])
L14 += h2("14.1 Why Systematic Evaluation Matters")
L14 += p("A prompt that works on 3 test cases may fail on the 4th. A prompt improved by intuition may actually degrade on edge cases you did not test. Systematic prompt evaluation — measuring quality across a diverse test set — is what separates ad-hoc prompting from reliable prompt engineering.")
L14 += callout("warn","Goodhart's Law for Prompts","'When a measure becomes a target, it ceases to be a good measure.' Optimising a prompt on a small test set leads to overfitting. Always hold out a <strong>validation set</strong> that you never use during iteration.")
L14 += h2("14.2 Evaluation Metrics by Task Type")
L14 += table(["Task Type","Primary Metric","Tool / Method"],[
    ["Classification","Accuracy, F1, Confusion Matrix","sklearn metrics + labelled test set"],
    ["Extraction","Exact match, Partial match, F1","String matching + normalisation"],
    ["Summarisation","ROUGE-L, BERTScore, Human eval","evaluate library or LLM-as-judge"],
    ["Generation quality","Human rating 1–5, LLM-as-judge","Claude grading Claude's outputs"],
    ["Format compliance","Parse success rate","json.loads() + Pydantic validation"],
    ["Cost / Latency","p50/p95 ms, $/1000 requests","Usage API + timing instrumentation"],
])
L14 += h2("14.3 LLM-as-Judge")
L14 += p("Using Claude to evaluate Claude's outputs is surprisingly effective and scales to tasks where labelled ground truth is unavailable. The key is a well-designed evaluation rubric prompt.")
L14 += code(
    "EVAL_PROMPT = (\n    'You are an expert evaluator.\\n'\n"
    "    'Task: {task}\\nResponse: {response}\\n\\n'\n"
    "    'Score each dimension 1 (poor) to 5 (excellent):\\n'\n"
    "    'accuracy, completeness, clarity, format.\\n'\n"
    "    'Return ONLY JSON: '\n"
    "    '{\"accuracy\":N,\"completeness\":N,\"clarity\":N,\"format\":N,'\n"
    "    '\"overall\":N,\"critique\":\"one sentence\"}'\n)\n\n"
    "def evaluate(task: str, response: str) -> dict:\n"
    "    r = client.messages.create(\n        model='claude-haiku-4-5-20251001',\n"
    "        max_tokens=200,\n"
    "        messages=[{'role':'user','content': EVAL_PROMPT.format(task=task,response=response)}]\n    )\n"
    "    return json.loads(r.content[0].text)",
    "Use Haiku as judge — cheap, fast, and surprisingly accurate on well-defined rubrics."
)
L14 += h2("14.4 A/B Prompt Testing")
L14 += code(
    "import statistics\n\ndef compare_prompts(prompt_a, prompt_b, test_cases, n_trials=3):\n"
    "    results = {'A': [], 'B': []}\n    for case in test_cases:\n"
    "        for prompt, label in [(prompt_a,'A'),(prompt_b,'B')]:\n"
    "            scores = []\n            for _ in range(n_trials):\n"
    "                r = client.messages.create(\n                    model='claude-opus-4-5', max_tokens=500,\n"
    "                    messages=[{'role':'user','content':prompt.format(**case)}]\n                )\n"
    "                s = evaluate(case['task'], r.content[0].text)\n"
    "                scores.append(s['overall'])\n"
    "            results[label].append(statistics.mean(scores))\n\n"
    "    a = statistics.mean(results['A']); b = statistics.mean(results['B'])\n"
    "    return {'A_mean':a, 'B_mean':b, 'winner':'A' if a > b else 'B'}",
    "Always compare on the SAME test set. Multiple trials reduce variance from model non-determinism."
)
L14 += h2("14.5 The 7-Step Iterative Improvement Cycle")
L14 += table(["Step","Action","Outcome"],[
    ["1. Baseline","Write the simplest first prompt","Initial performance score"],
    ["2. Failure analysis","Categorise errors on test set","Error taxonomy (5 categories)"],
    ["3. Hypothesis","Identify which prompt element causes each error","Prioritised change list"],
    ["4. Intervention","Change ONE element at a time","New prompt variant to test"],
    ["5. Evaluation","Run full test suite on new variant","Delta vs. baseline score"],
    ["6. Decision","Accept, reject, or combine changes","Updated best prompt"],
    ["7. Repeat","Until target quality or diminishing returns","Production-ready prompt"],
])
L14 += table(["Error Category","Symptom","Fix"],[
    ["Hallucination","Invented facts not in the input","Add: 'Only use information provided. Do not infer.'"],
    ["Format deviation","Wrong structure or missing fields","Show exact template + add Pydantic validation"],
    ["Scope creep","Answers beyond the requested task","Add: 'Answer only what is asked. Nothing else.'"],
    ["Truncation","Response cut off before completion","Increase max_tokens; add 'Complete the full response.'"],
    ["Refusal","Unnecessary safety trigger","Add context explaining the legitimate use case"],
])
L14 += h2("14.6 Prompt Versioning")
L14 += code(
    "# prompts/ticket_classifier/v3.txt\n"
    "# Changelog:\n# v1: Basic zero-shot — 72% accuracy on 50-case test set\n"
    "# v2: Added explicit output schema — 81% accuracy\n"
    "# v3: Added 4 few-shot examples (1 per class) — 89% accuracy\n"
    "# Test suite: tests/ticket_classifier_test.json (50 cases)\n"
    "# Last eval date: 2025-03-15 | Eval model: claude-opus-4-5\n\n"
    "System: You are a customer support ticket classifier...\n[rest of prompt follows]",
    "Rule: never silently update a production prompt without running the full test suite first."
)
L14 += card_open()
L14 += "<h2>L14 Summary</h2>\n"
L14 += summary([
    ("📊","Metrics First","Define success before writing the first prompt. Match metrics to the actual task."),
    ("⚖","LLM-as-Judge","Scale evaluation with Haiku grading outputs. Works when ground truth unavailable."),
    ("🔬","A/B Testing","Same test set. Multiple trials. Change one thing at a time."),
    ("📄","Version Control","Prompts are code. Git-track with performance metadata alongside each version."),
    ("🔁","7-Step Cycle","Baseline → Failure analysis → Hypothesis → Intervention → Eval → Decision → Repeat."),
    ("🛡","Hold-Out Set","Never optimise on your test set. Hold out a validation set from day one."),
])
L14 += card_close()
L14 += lec_close()

# ══════════════════════════════════════════════════════════════════════════════
# L15 — Workshop: Prompt Optimisation Lab
# ══════════════════════════════════════════════════════════════════════════════
L15  = hero("L15","Lecture 15 &middot; Unit 2",
             "Workshop: Prompt Optimisation Lab",
             "Consolidate all Unit 2 skills in a structured hands-on lab. Three real-world challenges — sentiment classification, contract risk extraction, and a persona-driven support agent.",
             ["&#9200; 1 Hour","&#128218; CO2","&#127919; Applied Lab"])
L15 += objectives([
    "Apply the full prompt engineering cycle (write → test → analyse → iterate) on a real task",
    "Build a sentiment classifier with 95%+ accuracy and schema-validated JSON output",
    "Use chain-of-thought to extract and score risks from legal contract clauses",
    "Design a complete support agent persona with format, tone, and escalation rules",
    "Diagnose and fix common prompt failure modes using the debrief checklist",
])
L15 += h2("15.1 Lab Overview")
L15 += grid3([
    ("teal","Lab A — Sentiment Classifier","Structured JSON output. Multi-class with confidence score. Target: 95%+ accuracy on 20-case test set."),
    ("gold","Lab B — Contract Risk Extraction","Identify and score risky clauses. Chain-of-thought reasoning. Structured JSON report."),
    ("purple","Lab C — Support Agent Persona","Constrained tone + format + escalation rules. Test 4 scenarios for format compliance."),
])
L15 += h2("15.2 Lab A: Sentiment Classifier")
L15 += h3("Baseline Prompt (Start Here)")
L15 += code("Classify the sentiment of this text: {text}",
    "This is intentionally weak. Run it first, observe failures, then improve.")
L15 += h3("Target Output Schema")
L15 += code(
    '{\n  "label": "positive" | "negative" | "neutral" | "mixed",\n'
    '  "confidence": 0.0 to 1.0,\n'
    '  "aspects": [{"aspect": string, "sentiment": "pos"|"neg"|"neu"}],\n'
    '  "explanation": "one sentence"\n}')
L15 += h3("Test Cases")
L15 += table(["#","Text","Expected Label"],[
    ["1","Great product, terrible shipping!","mixed"],
    ["2","The battery lasts all day.","positive"],
    ["3","Item arrived. Works.","neutral"],
    ["4","Completely broken, never buying again.","negative"],
    ["5","Love the design but the software is buggy.","mixed"],
])
L15 += callout("tip","Iteration Guide",
    "<ol style='padding-left:18px;line-height:2;margin-top:8px'>"
    "<li>Add explicit JSON schema → expect +10% accuracy</li>"
    "<li>Define 'mixed' explicitly → fixes misclassified examples</li>"
    "<li>Add 1 few-shot example per label → expect +15% accuracy</li>"
    "<li>Seed assistant turn with '{' → eliminates JSON parse errors</li>"
    "<li>Add Pydantic validation + retry → near 100% format compliance</li></ol>")
L15 += h2("15.3 Lab B: Contract Risk Extraction")
L15 += code(
    "System: You are a legal risk analyst. Identify risks for the CLIENT.\n\n"
    "Return a JSON array. Each element:\n{\n"
    "  \"clause_text\": \"exact quote from contract\",\n"
    "  \"risk_level\": \"HIGH\"|\"MEDIUM\"|\"LOW\",\n"
    "  \"risk_category\": \"Liability\"|\"IP\"|\"Payment\"|\"Termination\"|\"Other\",\n"
    "  \"explanation\": \"1-2 sentence plain English explanation\",\n"
    "  \"suggested_fix\": \"brief mitigation suggestion\"\n}",
    "Use chain-of-thought: 'Think through each clause carefully before assigning a risk level.'"
)
L15 += h3("Test Clause")
L15 += code(
    '"The Client grants the Vendor a perpetual, irrevocable, worldwide, royalty-free license\n'
    'to use, reproduce, modify, and distribute any materials provided by the Client in\n'
    'connection with the Services, including the right to sublicense such rights to third parties."',
    "Expected: HIGH risk, IP category — perpetual + irrevocable + sublicense = severe IP risk for the client."
)
L15 += h2("15.4 Lab C: Technical Support Persona")
L15 += code(
    "You are Aria, Level 1 technical support specialist for CloudStore.\n\n"
    "Response format (always follow exactly):\n"
    "[ISSUE IDENTIFIED]: one-sentence restatement\n"
    "[STEPS TO TRY]:\n  1. ...\n  2. ...\n"
    "[EXPECTED OUTCOME]: what user should see\n"
    "[ESCALATE IF]: condition to contact L2\n\n"
    "Rules:\n- Maximum 150 words per response\n"
    "- Never speculate about hardware failures — escalate instead\n"
    "- End with: 'Did that help? [YES] / [NO]'\n"
    "- If NO: create ticket TKT-{random 5 digits}\n\n"
    "Forbidden: 'Great question!' 'Absolutely!' 'As per my last email'",
    "Test: submit 'I've tried everything, nothing works' — should trigger immediate escalation."
)
L15 += h3("Test Scenarios")
L15 += table(["Scenario","What to Check"],[
    ["'My app won't load on Android.'","Format compliance, tone, step clarity"],
    ["'I've tried everything, nothing works.'","Escalation trigger, TKT format generated"],
    ["'Is this a hardware problem?'","Should NOT speculate — must escalate"],
    ["User says 'NO' to 'Did that help?'","Proper escalation with ticket number"],
])
L15 += h2("15.5 Lab Debrief: Common Findings &amp; Fixes")
L15 += table(["Issue Found","Root Cause","Fix"],[
    ["Wrong 'mixed' label","No definition of 'mixed' provided","Add definition + 1-2 few-shot mixed examples"],
    ["JSON missing fields","Schema not explicit about required vs optional","Mark all fields required; allow null explicitly"],
    ["Aria says 'Absolutely!'","Negative constraint not specific enough","Add exact forbidden phrase list"],
    ["All risks scored HIGH","No calibration examples between levels","Add 1 example each for HIGH, MEDIUM, LOW"],
    ["Response exceeds 150 words","Word limit instruction too soft","Add: 'Count your words. If over 150, revise before responding.'"],
    ["JSON parse error persists","Error feedback not specific enough","Feed the exact error location to Claude on retry"],
])
L15 += h2("15.6 Unit 2 Capability Map")
L15 += card_open()
L15 += "<h2>Completing Unit 2 — What You Can Now Do</h2>\n"
L15 += summary([
    ("💡","Zero &amp; Few-Shot","Choose the right demonstration strategy for any task type and data availability."),
    ("🧠","Chain-of-Thought","Activate step-by-step reasoning. Use Extended Thinking for hardest tasks."),
    ("🌟","Persona Design","Build consistent multi-turn AI characters with controlled tone and rules."),
    ("{}","Structured Output","Schema-validated JSON/XML for downstream systems. Retry with error feedback."),
    ("🎀","Context Management","Summarisation, chunking, hierarchical memory, RAG for long sessions."),
    ("📊","Evaluation &amp; Iteration","Metrics, A/B testing, LLM-as-judge, version control. Treat prompts as code."),
])
L15 += card_close()
L15 += exercise("Final Reflection Exercise",[
    "Pick one real task you want to solve with Claude (e.g., classify customer emails, summarise meeting notes, extract data from PDFs).",
    "Write a baseline prompt and a refined prompt using everything from this unit.",
    "Build a 10-case test set and measure accuracy on both versions.",
    "Document your failure categories and what fix resolved each one.",
    "Share your prompt version history with a colleague and explain your iteration decisions.",
])
L15 += lec_close()

# ─── Closing JS + HTML ───────────────────────────────────────────────────────
CLOSING = r"""
</div><!-- end #main -->

<script>
const links = document.querySelectorAll('#sidebar nav a[data-lec]');
const sections = document.querySelectorAll('section.lecture');

function showLec(id) {
  sections.forEach(s => s.classList.remove('active'));
  links.forEach(l => l.classList.remove('active'));
  const sec = document.querySelector('section[data-lec="' + id + '"]');
  const lnk = document.querySelector('#sidebar nav a[data-lec="' + id + '"]');
  if (sec) sec.classList.add('active');
  if (lnk) {
    lnk.classList.add('active');
    document.getElementById('tb-title').textContent =
      id + ' — ' + lnk.textContent.trim().replace(/^L\d+\s*/,'');
  }
  window.scrollTo(0, 0);
}

links.forEach(l => l.addEventListener('click', e => { e.preventDefault(); showLec(l.dataset.lec); }));
showLec('L08');

// Search
document.getElementById('search').addEventListener('input', function() {
  const q = this.value.toLowerCase().trim();
  if (!q) { showLec('L08'); return; }
  for (const s of sections) {
    if (s.textContent.toLowerCase().includes(q)) { showLec(s.dataset.lec); return; }
  }
});

// Theme
document.getElementById('theme-btn').addEventListener('click', () => {
  document.body.classList.toggle('light');
  document.getElementById('theme-btn').textContent =
    document.body.classList.contains('light') ? '\u{1F319}' : '☀';
});

// Copy code
function copyCode(btn) {
  const txt = btn.nextElementSibling.textContent;
  navigator.clipboard.writeText(txt).then(() => {
    btn.textContent = 'Copied!';
    setTimeout(() => btn.textContent = 'Copy', 2000);
  });
}
</script>
</body></html>
"""

with open(OUT, 'w') as f:
    f.write(HEAD)
    f.write(L08)
    f.write(L09)
    f.write(L10)
    f.write(L11)
    f.write(L12)
    f.write(L13)
    f.write(L14)
    f.write(L15)
    f.write(CLOSING)

print("Done. Lines:", open(OUT).read().count('\n'))
