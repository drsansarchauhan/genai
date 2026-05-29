out = '/sessions/blissful-quirky-tesla/mnt/outputs/CSAI601_Unit2_Notes.html'

def w(f, s):
    f.write(s)

with open(out, 'w') as f:
    # ── HEAD + CSS ──────────────────────────────────────────────────────
    w(f, '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CSAI601 — Unit 2: Prompt Engineering | Lecture Notes</title>
<style>
:root{
  --navy:#0f1f3d;--blue:#1a3a6b;--red:#e94560;--teal:#0a7c8c;
  --gold:#f4a832;--green:#27ae60;--purple:#7b2fbe;
  --bg:#0d1117;--surface:#161b22;--border:#21262d;
  --text:#e6edf3;--muted:#8b949e;--code:#0d1117;
}
*{box-sizing:border-box;margin:0;padding:0;}
body{font-family:"Segoe UI",system-ui,sans-serif;background:var(--bg);color:var(--text);display:flex;min-height:100vh;}
body.light-mode{--bg:#f8f9fa;--surface:#fff;--border:#dee2e6;--text:#212529;--muted:#6c757d;--code:#f6f8fa;}

/* Sidebar */
#sidebar{width:280px;min-height:100vh;background:var(--navy);color:#fff;display:flex;flex-direction:column;position:fixed;top:0;left:0;z-index:100;overflow-y:auto;}
#sidebar .brand{padding:20px 18px 14px;border-bottom:1px solid rgba(255,255,255,.1);}
#sidebar .brand .course{font-size:9.5px;letter-spacing:2px;color:var(--red);text-transform:uppercase;font-weight:700;}
#sidebar .brand h2{font-size:13px;line-height:1.5;margin-top:4px;font-weight:600;color:#e2e8f0;}
#sidebar nav{flex:1;padding:10px 0;}
#sidebar nav .nav-section{font-size:9px;letter-spacing:1.5px;color:rgba(255,255,255,.35);text-transform:uppercase;padding:14px 18px 5px;font-weight:700;}
#sidebar nav a{display:flex;align-items:flex-start;gap:9px;padding:7px 18px;font-size:12.5px;color:rgba(255,255,255,.7);text-decoration:none;transition:all .15s;border-left:3px solid transparent;line-height:1.4;}
#sidebar nav a:hover{color:#fff;background:rgba(255,255,255,.06);}
#sidebar nav a.active{color:#fff;background:rgba(233,69,96,.15);border-left-color:var(--red);}
#sidebar nav a .lnum{font-size:10px;font-weight:800;color:var(--red);min-width:22px;margin-top:1px;}
#sidebar .prog{padding:14px 18px;border-top:1px solid rgba(255,255,255,.1);font-size:11px;color:rgba(255,255,255,.35);}

/* Main */
#main{margin-left:280px;flex:1;display:flex;flex-direction:column;}
#topbar{background:var(--surface);border-bottom:1px solid var(--border);padding:10px 28px;display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;z-index:50;gap:10px;flex-wrap:wrap;}
#topbar .tb-left{font-size:13.5px;font-weight:600;color:var(--text);}
#topbar .tb-right{display:flex;gap:8px;align-items:center;flex-wrap:wrap;}
#progress-bar{position:fixed;top:0;left:280px;right:0;height:3px;background:var(--red);width:0;z-index:200;transition:width .1s;}
.badge{font-size:10.5px;padding:3px 9px;border-radius:12px;font-weight:600;}
.b-navy{background:#1a3a6b;color:#93c5fd;}
.b-red{background:#4c0519;color:#fca5a5;}
.b-green{background:#14532d;color:#86efac;}
.b-gold{background:#451a03;color:#fcd34d;}

/* Search */
.search-bar{display:flex;gap:6px;align-items:center;}
#search-input{background:var(--surface);border:1px solid var(--border);color:var(--text);border-radius:6px;padding:4px 10px;font-size:12px;width:160px;}
#search-btn{background:var(--red);color:#fff;border:none;border-radius:6px;padding:4px 10px;font-size:11.5px;cursor:pointer;}
#search-info{font-size:11px;color:var(--muted);}
#theme-toggle{background:rgba(255,255,255,.08);border:1px solid var(--border);color:var(--text);border-radius:6px;padding:4px 10px;font-size:11px;cursor:pointer;}

#content{padding:32px 36px 80px;overflow-y:auto;height:calc(100vh - 47px);}

/* Lecture */
section.lecture{display:none;max-width:900px;}
section.lecture.active{display:block;}
.lec-hero{background:linear-gradient(135deg,var(--navy),#1a3a6b);border-radius:12px;padding:32px 36px;margin-bottom:28px;border-left:5px solid var(--red);}
.lec-hero .lec-tag{font-size:10px;letter-spacing:2px;color:var(--red);text-transform:uppercase;font-weight:700;margin-bottom:10px;}
.lec-hero h1{font-size:26px;font-weight:800;line-height:1.3;margin-bottom:10px;color:#fff;}
.lec-hero p{font-size:14px;line-height:1.7;color:rgba(255,255,255,.75);}
.hero-meta{margin-top:16px;display:flex;gap:20px;flex-wrap:wrap;font-size:12.5px;color:rgba(255,255,255,.6);}

/* Objectives */
.objectives{background:rgba(10,124,140,.12);border:1px solid rgba(10,124,140,.4);border-radius:10px;padding:18px 22px;margin-bottom:24px;}
.objectives h3{font-size:13.5px;font-weight:700;color:var(--teal);margin-bottom:10px;}
.objectives ul{list-style:none;display:flex;flex-direction:column;gap:7px;}
.objectives ul li{font-size:13.5px;line-height:1.6;padding-left:20px;position:relative;color:var(--text);}
.objectives ul li::before{content:"✓";position:absolute;left:0;color:var(--teal);font-weight:700;}

/* Section headings */
h2.sec{font-size:19px;font-weight:700;color:var(--text);margin:32px 0 10px;padding-bottom:6px;border-bottom:2px solid var(--red);}
h3.sub{font-size:15.5px;font-weight:700;color:var(--gold);margin:22px 0 8px;}
h4.subsub{font-size:14px;font-weight:600;color:var(--teal);margin:16px 0 6px;}
p.body{font-size:14px;line-height:1.8;color:var(--text);margin-bottom:12px;}

/* Callouts */
.c-info{background:rgba(26,58,107,.35);border-left:4px solid #3b82f6;border-radius:0 8px 8px 0;padding:14px 18px;margin:16px 0;}
.c-key{background:rgba(233,69,96,.12);border-left:4px solid var(--red);border-radius:0 8px 8px 0;padding:14px 18px;margin:16px 0;}
.c-eg{background:rgba(244,168,50,.1);border-left:4px solid var(--gold);border-radius:0 8px 8px 0;padding:14px 18px;margin:16px 0;}
.c-warn{background:rgba(123,47,190,.15);border-left:4px solid var(--purple);border-radius:0 8px 8px 0;padding:14px 18px;margin:16px 0;}
.c-math{background:rgba(10,124,140,.12);border:1px solid rgba(10,124,140,.4);border-radius:8px;padding:18px 22px;margin:16px 0;text-align:center;}
.c-info strong,.c-key strong,.c-eg strong,.c-warn strong{font-size:11px;font-weight:700;letter-spacing:1px;text-transform:uppercase;display:block;margin-bottom:5px;}
.c-info strong{color:#60a5fa;}
.c-key strong{color:var(--red);}
.c-eg strong{color:var(--gold);}
.c-warn strong{color:var(--purple);}
.c-math .formula{font-family:monospace;font-size:17px;color:var(--gold);font-weight:700;margin:6px 0;}
.c-math p{font-size:13px;color:var(--muted);margin-top:8px;}

/* Code */
.code-block{background:var(--code);border:1px solid var(--border);border-radius:8px;padding:16px 20px;margin:14px 0;overflow-x:auto;position:relative;}
.code-block code{font-family:"Cascadia Code","Fira Code",monospace;font-size:13px;line-height:1.7;white-space:pre;}
.kw{color:#ff7b72;}.fn{color:#d2a8ff;}.st{color:#a5d6ff;}.cm{color:#8b949e;font-style:italic;}.nb{color:#ffa657;}.op{color:#ff7b72;}
.copy-btn{position:absolute;top:8px;right:8px;padding:3px 10px;font-size:11px;background:var(--red);color:#fff;border:none;border-radius:4px;cursor:pointer;opacity:.8;}

/* Tables */
.data-table{width:100%;border-collapse:collapse;font-size:13px;margin:14px 0;}
.data-table th{background:var(--blue);color:#fff;padding:9px 13px;text-align:left;font-size:12px;font-weight:600;}
.data-table td{padding:8px 13px;border-bottom:1px solid var(--border);vertical-align:top;line-height:1.5;}
.data-table tr:nth-child(even) td{background:rgba(255,255,255,.03);}

/* Comparison grid */
.cmp-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:14px 0;}
.cmp-card{background:var(--surface);border:1px solid var(--border);border-radius:8px;padding:16px 18px;}
.cmp-card h4{font-size:12.5px;font-weight:700;margin-bottom:10px;text-transform:uppercase;letter-spacing:.5px;}
.cmp-card ul{list-style:none;display:flex;flex-direction:column;gap:6px;}
.cmp-card ul li{font-size:13px;line-height:1.5;padding-left:16px;position:relative;}
.cmp-card ul li::before{content:"•";position:absolute;left:0;}

/* Practice box */
.practice{background:rgba(39,174,96,.08);border:1px solid rgba(39,174,96,.3);border-radius:10px;padding:18px 22px;margin:20px 0;}
.practice h4{font-size:13px;font-weight:700;color:var(--green);margin-bottom:10px;}
.practice ol{padding-left:20px;display:flex;flex-direction:column;gap:6px;}
.practice ol li{font-size:13.5px;line-height:1.6;color:var(--text);}

/* Prompt box */
.prompt-box{background:#0d1117;border:1px solid var(--teal);border-radius:8px;padding:16px 20px;margin:14px 0;position:relative;}
.prompt-box .role{font-size:10px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:var(--teal);margin-bottom:6px;}
.prompt-box pre{font-family:"Cascadia Code","Fira Code",monospace;font-size:13px;line-height:1.7;color:#a8d8ea;white-space:pre-wrap;}

/* Summary cards */
.sum-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:16px;}
.sum-card{background:var(--surface);border:1px solid var(--border);border-radius:8px;padding:14px 16px;}
.sum-card .sum-title{font-size:12px;font-weight:700;color:var(--red);margin-bottom:6px;}
.sum-card p{font-size:12.5px;line-height:1.5;color:var(--muted);}

@media(max-width:768px){
  #sidebar{display:none;}#main{margin-left:0;}
  #content{padding:20px 16px 60px;}
  .cmp-grid{grid-template-columns:1fr;}
  .sum-grid{grid-template-columns:1fr 1fr;}
}
</style>
</head>
<body>
<div id="progress-bar"></div>
<div id="app" style="display:flex;width:100%;">

<aside id="sidebar">
  <div class="brand">
    <div class="course">CSAI601 &middot; Unit 2</div>
    <h2>Prompt Engineering</h2>
  </div>
  <nav>
    <div class="nav-section">Lectures</div>
    <a href="#" class="active" data-lec="l08"><span class="lnum">L08</span>Intro to Prompt Engineering</a>
    <a href="#" data-lec="l09"><span class="lnum">L09</span>Zero-shot &amp; Few-shot</a>
    <a href="#" data-lec="l10"><span class="lnum">L10</span>Chain-of-Thought</a>
    <a href="#" data-lec="l11"><span class="lnum">L11</span>System Prompts &amp; Personas</a>
    <a href="#" data-lec="l12"><span class="lnum">L12</span>Structured Outputs</a>
    <a href="#" data-lec="l13"><span class="lnum">L13</span>Context Management</a>
    <a href="#" data-lec="l14"><span class="lnum">L14</span>Advanced Techniques</a>
    <a href="#" data-lec="l15"><span class="lnum">L15</span>Lab: Prompt Optimisation</a>
  </nav>
  <div class="prog">Unit 2 of 5 &middot; 8 Lectures &middot; 8 Hours</div>
</aside>

<div id="main">
  <div id="topbar">
    <div class="tb-left" id="tb-label">Lecture 8 &mdash; Introduction to Prompt Engineering</div>
    <div class="tb-right">
      <div class="search-bar">
        <input id="search-input" type="text" placeholder="Search notes...">
        <button id="search-btn">Search</button>
        <span id="search-info"></span>
      </div>
      <span class="badge b-navy">Unit 2</span>
      <span class="badge b-red">CO2</span>
      <span class="badge b-green">8 Lectures</span>
      <button id="theme-toggle">&#9728;&#65039; Light</button>
    </div>
  </div>
  <div id="content">
''')
    print("Head + sidebar written")

with open(out, 'a') as f:
    # ── L08 ─────────────────────────────────────────────────────────────
    w(f, '''
<!-- ═══ L08 ═══ -->
<section class="lecture active" id="l08">
<div class="lec-hero">
  <div class="lec-tag">Lecture 08 &middot; Unit 2</div>
  <h1>Introduction to Prompt Engineering</h1>
  <p>Understand what prompt engineering is, why it matters, and how to think about prompts as programs. Learn the anatomy of an effective prompt and when prompting is better than fine-tuning.</p>
  <div class="hero-meta"><span>&#9200; Duration: 1 Hour</span><span>&#128218; Maps to CO2</span><span>&#127919; Foundation for all Unit 2 lectures</span></div>
</div>

<div class="objectives">
  <h3>&#127919; Learning Objectives</h3>
  <ul>
    <li>Define prompt engineering and explain its role in the LLM application stack</li>
    <li>Describe the four components of an effective prompt: instruction, context, input, output format</li>
    <li>Compare prompting vs fine-tuning across cost, speed, flexibility, and performance dimensions</li>
    <li>Explain why the same model can produce dramatically different outputs from differently worded prompts</li>
    <li>Apply Anthropic\'s core prompt engineering principles to a real task</li>
  </ul>
</div>

<h2 class="sec">8.1 What Is Prompt Engineering?</h2>
<p class="body">A <strong>prompt</strong> is any text you send to a language model as input. <strong>Prompt engineering</strong> is the systematic practice of designing, iterating, and optimising those inputs to reliably produce the desired outputs from an LLM.</p>

<div class="c-key"><strong>Core Insight</strong>An LLM is a frozen function — you cannot change its weights at inference time. The only lever you have is the input. Prompt engineering is the art of pulling that lever skillfully.</div>

<p class="body">Unlike traditional software where you write code that executes deterministically, in LLM applications you write <em>natural language instructions</em> that guide a probabilistic model. This requires a different mental model — closer to managing a very capable but literal-minded assistant than to writing a compiler.</p>

<h3 class="sub">The Prompt-as-Program Metaphor</h3>
<p class="body">Think of a prompt as a program with the following components:</p>
<table class="data-table">
  <thead><tr><th>Prompt Component</th><th>Programming Analogy</th><th>Example</th></tr></thead>
  <tbody>
    <tr><td><strong>Instruction</strong></td><td>Function signature / docstring</td><td>"Summarise the following article in 3 bullet points."</td></tr>
    <tr><td><strong>Context</strong></td><td>Global variables / imports</td><td>"You are an expert in medical research. The audience is a general public reader."</td></tr>
    <tr><td><strong>Input data</strong></td><td>Function arguments</td><td>"Article: {article_text}"</td></tr>
    <tr><td><strong>Output format</strong></td><td>Return type / schema</td><td>"Respond in JSON with keys: summary, key_points, sentiment."</td></tr>
  </tbody>
</table>

<h2 class="sec">8.2 Why Prompt Engineering Matters</h2>
<p class="body">The same model (Claude Sonnet, GPT-4, etc.) can produce wildly different results depending on how the prompt is written. Studies show that prompt variations can cause accuracy swings of <strong>30–50 percentage points</strong> on benchmark tasks — larger than the gap between model generations.</p>

<div class="cmp-grid">
  <div class="cmp-card"><h4 style="color:var(--red)">Poor Prompt</h4><ul>
    <li>Vague: "Tell me about transformers"</li>
    <li>No context about audience or depth</li>
    <li>No output format specified</li>
    <li>Result: generic Wikipedia-style answer</li>
    <li>Inconsistent across runs</li>
  </ul></div>
  <div class="cmp-card"><h4 style="color:var(--green)">Engineered Prompt</h4><ul>
    <li>"Explain the transformer self-attention mechanism"</li>
    <li>"for a 3rd-year CS student"</li>
    <li>"using one concrete analogy and one equation"</li>
    <li>"in under 200 words"</li>
    <li>Result: precise, consistent, actionable</li>
  </ul></div>
</div>

<h2 class="sec">8.3 Prompting vs Fine-Tuning</h2>
<p class="body">A common question: when should you write a better prompt vs train a custom model? Here is the decision framework:</p>
<table class="data-table">
  <thead><tr><th>Dimension</th><th>Prompting</th><th>Fine-Tuning</th></tr></thead>
  <tbody>
    <tr><td><strong>Cost</strong></td><td>Zero — just API calls</td><td>$100s–$10,000s in compute</td></tr>
    <tr><td><strong>Speed to deploy</strong></td><td>Minutes — iterate live</td><td>Days to weeks</td></tr>
    <tr><td><strong>New knowledge</strong></td><td>Cannot add new facts (use RAG)</td><td>Can inject domain knowledge</td></tr>
    <tr><td><strong>Style/format</strong></td><td>Good with clear instructions</td><td>Excellent — baked in</td></tr>
    <tr><td><strong>Consistency</strong></td><td>Varies unless engineered carefully</td><td>Very consistent</td></tr>
    <tr><td><strong>Context length</strong></td><td>Limited by context window</td><td>Same limit</td></tr>
    <tr><td><strong>When to use</strong></td><td>Most tasks — try first</td><td>High-volume, style-critical, latency-sensitive</td></tr>
  </tbody>
</table>

<div class="c-info"><strong>Rule of Thumb</strong>Always exhaust prompt engineering before considering fine-tuning. 90% of tasks can be solved with well-engineered prompts. Fine-tune only when you have 1,000+ labeled examples, a consistent style requirement, and proven that prompting has hit a ceiling.</div>

<h2 class="sec">8.4 Anthropic\'s Prompt Engineering Principles</h2>
<p class="body">Anthropic publishes a <a href="https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview" style="color:var(--teal);">Prompt Engineering Guide</a> with principles specific to Claude. Key takeaways:</p>

<h3 class="sub">Principle 1 — Be Explicit and Specific</h3>
<p class="body">Claude performs best when given clear, unambiguous instructions. State what you want, how long the response should be, what format to use, and what constraints apply. Never assume Claude will "figure out" implicit requirements.</p>
<div class="c-eg"><strong>Example</strong>"Write a Python function that takes a list of integers and returns the top 3 most frequent elements. Include type hints, a docstring, and a usage example. Handle ties alphabetically."</div>

<h3 class="sub">Principle 2 — Use XML Tags for Structure</h3>
<p class="body">Claude was trained on data containing XML-style tags for structure. Wrapping inputs in semantic tags dramatically improves parsing and response quality.</p>
<div class="prompt-box">
  <div class="role">Structured Prompt</div>
  <pre>&lt;task&gt;Summarise the following research paper&lt;/task&gt;
&lt;audience&gt;Undergraduate students with no ML background&lt;/audience&gt;
&lt;constraints&gt;Under 150 words. No jargon. Include one analogy.&lt;/constraints&gt;
&lt;paper&gt;
{paper_text}
&lt;/paper&gt;</pre>
</div>

<h3 class="sub">Principle 3 — Provide Positive Instructions</h3>
<p class="body">Tell Claude what TO do rather than only what NOT to do. "Do not use jargon" is weaker than "Use simple language suitable for a 12-year-old." Negative constraints work better as supplements to positive ones.</p>

<h3 class="sub">Principle 4 — Give Claude Room to Think</h3>
<p class="body">Asking Claude to respond immediately often produces shallower answers. Adding "Think through this step by step before responding" or "First, outline your reasoning in a scratchpad, then give your final answer" consistently improves quality on reasoning tasks.</p>

<h2 class="sec">8.5 The Prompt Engineering Workflow</h2>
<p class="body">Effective prompt engineering is iterative, not one-shot. Follow this cycle:</p>
<div class="c-info"><strong>Workflow</strong>1. Write a first-draft prompt → 2. Test on 5–10 diverse inputs → 3. Identify failure modes → 4. Hypothesise root cause → 5. Edit prompt to address root cause → 6. Re-test → 7. Repeat until acceptance criteria met → 8. Stress-test edge cases</div>

<h3 class="sub">Failure Mode Taxonomy</h3>
<table class="data-table">
  <thead><tr><th>Failure Mode</th><th>Symptom</th><th>Fix</th></tr></thead>
  <tbody>
    <tr><td>Ambiguity</td><td>Inconsistent outputs across runs</td><td>Add explicit constraints and examples</td></tr>
    <tr><td>Missing context</td><td>Generic or off-target responses</td><td>Add role, audience, background in system prompt</td></tr>
    <tr><td>Format mismatch</td><td>Wrong structure (prose instead of JSON)</td><td>Add explicit output format spec with example</td></tr>
    <tr><td>Scope creep</td><td>Response is too long or adds unrequested content</td><td>Add length constraints and "only answer X"</td></tr>
    <tr><td>Hallucination</td><td>Invented facts or citations</td><td>Ground with retrieved context; ask to say "I don\'t know"</td></tr>
  </tbody>
</table>

<div class="practice">
  <h4>&#128736; Practice Exercise</h4>
  <ol>
    <li>Take this prompt: "Explain machine learning." — Test it against Claude.</li>
    <li>Identify what is missing (audience? depth? format? length?)</li>
    <li>Rewrite using the 4-component anatomy (instruction, context, input, output format)</li>
    <li>Test the improved version. Compare the two responses side by side.</li>
    <li>What changed? Why? Document your findings.</li>
  </ol>
</div>

<div class="sum-grid">
  <div class="sum-card"><div class="sum-title">Prompt = Program</div><p>4 components: instruction, context, input, output format. Write all four explicitly.</p></div>
  <div class="sum-card"><div class="sum-title">Prompting First</div><p>Try prompt engineering before fine-tuning — 90% of tasks solved without training cost.</p></div>
  <div class="sum-card"><div class="sum-title">Iterate</div><p>Test on 5-10 inputs, find failure modes, fix root cause, repeat until criteria met.</p></div>
  <div class="sum-card"><div class="sum-title">Be Explicit</div><p>State length, format, audience, constraints. Never rely on implicit understanding.</p></div>
  <div class="sum-card"><div class="sum-title">Use XML Tags</div><p>Claude trained on XML-structured data — wrapping inputs in tags improves parsing.</p></div>
  <div class="sum-card"><div class="sum-title">Give Room to Think</div><p>"Think step by step" before answering raises accuracy on reasoning tasks.</p></div>
</div>
</section>
''')
    print("L08 written")

print("Part 1 done")
