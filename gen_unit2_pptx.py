#!/usr/bin/env python3
"""Generate make_unit2_slides.js for pptxgenjs — 100 slides Unit 2 Prompt Engineering"""

js_path = '/sessions/blissful-quirky-tesla/mnt/outputs/make_unit2_slides.js'

lines = []
a = lines.append

# ─── preamble ───────────────────────────────────────────────────────────────
a("""'use strict';
const pptxgen = require('/usr/local/lib/node_modules_global/lib/node_modules/pptxgenjs');
const prs = new pptxgen();
prs.layout = 'LAYOUT_WIDE';
prs.title = 'CSAI601 Unit 2 - Prompt Engineering';

// ── Palette ────────────────────────────────────────────────────────────────
const C = {
  navy:   '0f1f3d',
  blue:   '1a3a6b',
  red:    'e94560',
  teal:   '0a7c8c',
  gold:   'f4a832',
  green:  '27ae60',
  purple: '7b2fbe',
  white:  'FFFFFF',
  light:  'e6edf3',
  muted:  '8b949e',
  dark:   '0d1117',
};

// ── Helpers ────────────────────────────────────────────────────────────────
function bg(sld, color) {
  sld.background = { color: color || C.dark };
}
function rect(sld, x, y, w, h, color, opts) {
  sld.addShape(prs.ShapeType.rect, Object.assign({ x, y, w, h, fill: { color } }, opts || {}));
}
function txt(sld, text, x, y, w, h, opts) {
  sld.addText(text, Object.assign({ x, y, w, h }, opts || {}));
}
function titleBar(sld, label) {
  rect(sld, 0, 0, 13.33, 0.55, C.navy);
  txt(sld, 'CSAI601 | Unit 2: Prompt Engineering', 0.15, 0.08, 9, 0.38,
      { fontSize: 11, color: C.muted, bold: false });
  txt(sld, label, 9.5, 0.08, 3.5, 0.38,
      { fontSize: 11, color: C.gold, bold: true, align: 'right' });
}
function bottomBar(sld, left, right) {
  rect(sld, 0, 7.05, 13.33, 0.45, C.navy);
  txt(sld, left || 'CSAI601 | B.Tech CS/IT 3rd Year', 0.15, 7.1, 7, 0.3,
      { fontSize: 10, color: C.muted });
  txt(sld, right || 'CO2', 10, 7.1, 3, 0.3,
      { fontSize: 10, color: C.gold, align: 'right' });
}
function heroSlide(title, subtitle, tag, slide_no) {
  const sld = prs.addSlide();
  bg(sld, C.dark);
  rect(sld, 0, 0, 13.33, 7.5, C.dark);
  rect(sld, 0, 0, 0.08, 7.5, C.red);
  rect(sld, 0, 3.2, 13.33, 0.04, C.blue);
  txt(sld, tag || 'CSAI601 | Unit 2', 0.5, 0.8, 12, 0.5,
      { fontSize: 14, color: C.teal, bold: true });
  txt(sld, title, 0.5, 1.5, 12.3, 2.2,
      { fontSize: 36, color: C.white, bold: true, breakLine: false });
  txt(sld, subtitle || '', 0.5, 3.5, 12, 0.9,
      { fontSize: 18, color: C.light });
  txt(sld, 'Prompt Engineering', 0.5, 6.5, 8, 0.5,
      { fontSize: 13, color: C.muted });
  txt(sld, String(slide_no || ''), 12.5, 6.5, 0.7, 0.5,
      { fontSize: 13, color: C.muted, align: 'right' });
  return sld;
}
function bulletSlide(title, bullets, tag, slide_no) {
  const sld = prs.addSlide();
  bg(sld, C.dark);
  titleBar(sld, tag || '');
  bottomBar(sld, null, 'CO2');
  txt(sld, title, 0.4, 0.7, 12.5, 0.7,
      { fontSize: 24, color: C.gold, bold: true });
  rect(sld, 0.4, 1.45, 2.5, 0.04, C.red);
  const items = bullets.map(b => ({
    text: b, options: { fontSize: 17, color: C.light, bullet: { type: 'bullet', color: C.teal },
    paraSpaceBefore: 8 }
  }));
  sld.addText(items, { x: 0.4, y: 1.6, w: 12.5, h: 5.2 });
  txt(sld, String(slide_no || ''), 12.5, 6.5, 0.7, 0.3,
      { fontSize: 11, color: C.muted, align: 'right' });
  return sld;
}
function twoColSlide(title, leftH, leftB, rightH, rightB, tag, slide_no) {
  const sld = prs.addSlide();
  bg(sld, C.dark);
  titleBar(sld, tag || '');
  bottomBar(sld);
  txt(sld, title, 0.4, 0.7, 12.5, 0.6, { fontSize: 22, color: C.gold, bold: true });
  rect(sld, 0.4, 1.38, 12.5, 0.04, C.red);
  rect(sld, 0.4, 1.5, 6.0, 5.4, '111827', { line: { color: C.blue, width: 1 } });
  rect(sld, 6.93, 1.5, 6.0, 5.4, '111827', { line: { color: C.teal, width: 1 } });
  txt(sld, leftH, 0.6, 1.6, 5.6, 0.5, { fontSize: 15, color: C.red, bold: true });
  txt(sld, leftB, 0.6, 2.15, 5.6, 4.5, { fontSize: 14, color: C.light, valign: 'top' });
  txt(sld, rightH, 7.13, 1.6, 5.6, 0.5, { fontSize: 15, color: C.teal, bold: true });
  txt(sld, rightB, 7.13, 2.15, 5.6, 4.5, { fontSize: 14, color: C.light, valign: 'top' });
  txt(sld, String(slide_no || ''), 12.5, 6.5, 0.7, 0.3,
      { fontSize: 11, color: C.muted, align: 'right' });
  return sld;
}
function codeSlide(title, codeText, note, tag, slide_no) {
  const sld = prs.addSlide();
  bg(sld, C.dark);
  titleBar(sld, tag || '');
  bottomBar(sld);
  txt(sld, title, 0.4, 0.7, 12.5, 0.6, { fontSize: 22, color: C.gold, bold: true });
  rect(sld, 0.4, 1.45, 12.5, 5.0, '0d1117', { line: { color: C.blue, width: 1 } });
  txt(sld, codeText, 0.6, 1.6, 12.0, 4.7,
      { fontSize: 13, color: C.green, fontFace: 'Courier New', valign: 'top' });
  if (note) {
    txt(sld, note, 0.4, 6.6, 12.5, 0.35, { fontSize: 12, color: C.muted });
  }
  txt(sld, String(slide_no || ''), 12.5, 6.5, 0.7, 0.3,
      { fontSize: 11, color: C.muted, align: 'right' });
  return sld;
}
function tableSlide(title, headers, rows, tag, slide_no) {
  const sld = prs.addSlide();
  bg(sld, C.dark);
  titleBar(sld, tag || '');
  bottomBar(sld);
  txt(sld, title, 0.4, 0.7, 12.5, 0.6, { fontSize: 22, color: C.gold, bold: true });
  const colW = 12.5 / headers.length;
  const tableRows = [
    headers.map(h => ({ text: h, options: { bold: true, color: C.white, fill: C.blue, fontSize: 13 }})),
    ...rows.map((row, ri) => row.map(cell => ({
      text: cell,
      options: { color: C.light, fill: ri % 2 === 0 ? '1a2535' : '111827', fontSize: 12 }
    })))
  ];
  sld.addTable(tableRows, {
    x: 0.4, y: 1.5, w: 12.5, colW: headers.map(() => colW),
    border: { color: C.blue, pt: 0.5 }
  });
  txt(sld, String(slide_no || ''), 12.5, 6.5, 0.7, 0.3,
      { fontSize: 11, color: C.muted, align: 'right' });
  return sld;
}
function summarySlide(title, items, tag, slide_no) {
  const sld = prs.addSlide();
  bg(sld, C.dark);
  titleBar(sld, tag || '');
  bottomBar(sld);
  txt(sld, title, 0.4, 0.7, 12.5, 0.6, { fontSize: 22, color: C.gold, bold: true });
  const cols = items.length <= 3 ? items.length : 2;
  const rows2 = Math.ceil(items.length / cols);
  const bw = 12.5 / cols - 0.15;
  const bh = 4.8 / rows2 - 0.15;
  items.forEach((item, i) => {
    const col = i % cols;
    const row = Math.floor(i / cols);
    const x = 0.4 + col * (bw + 0.15);
    const y = 1.5 + row * (bh + 0.15);
    rect(sld, x, y, bw, bh, '111827', { line: { color: C.teal, width: 1 } });
    txt(sld, item.icon || '', x + 0.15, y + 0.1, bw - 0.3, 0.5,
        { fontSize: 22 });
    txt(sld, item.title, x + 0.15, y + 0.55, bw - 0.3, 0.45,
        { fontSize: 14, color: C.gold, bold: true });
    txt(sld, item.body, x + 0.15, y + 1.0, bw - 0.3, bh - 1.1,
        { fontSize: 12, color: C.light, valign: 'top' });
  });
  txt(sld, String(slide_no || ''), 12.5, 6.5, 0.7, 0.3,
      { fontSize: 11, color: C.muted, align: 'right' });
  return sld;
}
""")

# ─── Slide 1: Course Title ──────────────────────────────────────────────────
a("""
// ═══ SLIDE 1: Course Title ═══
{
  const sld = prs.addSlide();
  bg(sld, C.dark);
  rect(sld, 0, 0, 0.1, 7.5, C.red);
  rect(sld, 0, 3.5, 13.33, 0.05, C.blue);
  txt(sld, 'CSAI601', 0.4, 0.5, 12, 1.0, { fontSize: 52, color: C.red, bold: true });
  txt(sld, 'Generative AI with Claude', 0.4, 1.55, 12, 0.7,
      { fontSize: 28, color: C.light });
  txt(sld, 'UNIT 2: PROMPT ENGINEERING', 0.4, 2.45, 12, 0.6,
      { fontSize: 20, color: C.teal, bold: true });
  txt(sld, '8 Lectures  |  8 Hours  |  CO2  |  B.Tech CS/IT 3rd Year', 0.4, 3.2, 12, 0.4,
      { fontSize: 14, color: C.muted });
  rect(sld, 0.4, 3.75, 12, 0.04, C.blue);
  const topics = ['L08: Intro to Prompt Engineering', 'L09: Zero-Shot & Few-Shot',
    'L10: Chain-of-Thought', 'L11: Role, Persona & Tone',
    'L12: Structured Output', 'L13: Context Management',
    'L14: Evaluation & Iteration', 'L15: Prompt Lab Workshop'];
  topics.forEach((t, i) => {
    const col = i < 4 ? 0 : 1;
    const row = i < 4 ? i : i - 4;
    txt(sld, t, 0.4 + col * 6.5, 4.0 + row * 0.55, 6.2, 0.5,
        { fontSize: 14, color: C.light, bullet: { type: 'bullet', color: C.teal } });
  });
  txt(sld, 'Dept. of CS/IT  |  CO-PO Mapping: CO2-PO1,PO2,PO3', 0.4, 6.9, 12, 0.35,
      { fontSize: 11, color: C.muted });
}
""")

# ─── Slide 2: Unit Overview ─────────────────────────────────────────────────
a("""
// ═══ SLIDE 2: Unit Overview ═══
{
  const sld = prs.addSlide();
  bg(sld, C.dark);
  titleBar(sld, 'Unit Overview');
  bottomBar(sld);
  txt(sld, 'Unit 2 — Prompt Engineering', 0.4, 0.7, 12.5, 0.6,
      { fontSize: 26, color: C.gold, bold: true });
  const cards = [
    { label: 'What is it?', body: 'The art and science of crafting inputs to steer LLM behavior without changing model weights', color: C.teal },
    { label: 'Why it matters', body: 'Solve 90% of LLM application requirements through prompt design alone — no GPU, no fine-tuning', color: C.red },
    { label: 'CO mapped', body: 'CO2: Design prompts for diverse NLP tasks; evaluate quality and apply chain-of-thought reasoning', color: C.gold },
    { label: 'Key outcome', body: 'Build production-ready prompts: structured output, persona, reasoning, long-context, with evaluation loop', color: C.green },
  ];
  cards.forEach((c, i) => {
    const x = 0.4 + (i % 2) * 6.5;
    const y = 1.6 + Math.floor(i / 2) * 2.5;
    rect(sld, x, y, 6.2, 2.2, '111827', { line: { color: c.color, width: 2 } });
    txt(sld, c.label, x + 0.2, y + 0.15, 5.8, 0.45,
        { fontSize: 15, color: c.color, bold: true });
    txt(sld, c.body, x + 0.2, y + 0.65, 5.8, 1.4,
        { fontSize: 13, color: C.light, valign: 'top' });
  });
}
""")

# ─── L08 slides (3–14) = 12 slides ─────────────────────────────────────────
a("""
// ══════════════════════════════════════════════════
// L08 — Introduction to Prompt Engineering (12 slides)
// ══════════════════════════════════════════════════

heroSlide('L08: Introduction to\\nPrompt Engineering',
  'Anatomy of a prompt · When to prompt vs fine-tune · Anthropic principles',
  'L08 of 8', 3);

bulletSlide('What Is Prompt Engineering?', [
  'Prompt engineering = crafting inputs to LLMs to elicit desired outputs — without modifying weights',
  'Operates entirely at inference time: no training, no GPU, no labelled data required',
  'Spans four concerns: correctness, format, tone, and safety',
  'Analogy: writing a detailed job description vs. hoping someone guesses the role',
  'Scale: a 10-word change in a system prompt can shift output quality by 40%+',
], 'L08 | Intro', 4);

bulletSlide('The LLM Application Stack', [
  'Layer 1 — Foundation Model: Pre-trained weights (Claude, GPT, Gemini) — fixed at inference',
  'Layer 2 — System Prompt: Persona, rules, format constraints — set per deployment',
  'Layer 3 — Conversation History: Prior turns in the context window',
  'Layer 4 — User Prompt: Real-time input from the end user',
  'Prompt engineering operates on Layers 2–4 to shape Layer 1 behavior',
  'Fine-tuning modifies Layer 1 — expensive, needs data, rarely necessary',
], 'L08 | Stack', 5);

bulletSlide('Anatomy of an Effective Prompt', [
  'Component 1 — INSTRUCTION: What task should Claude perform? Be explicit (classify, summarise, translate)',
  'Component 2 — CONTEXT: Background info, domain, constraints, prior decisions',
  'Component 3 — INPUT DATA: The text, code, or data to operate on (use XML tags to delimit)',
  'Component 4 — OUTPUT FORMAT: Exact schema, length, tone, language',
  'Missing any one component degrades output — the model guesses what you left implicit',
  'Rule: Write all four components even when one seems obvious',
], 'L08 | Anatomy', 6);

codeSlide('4-Component Prompt Template',
`System:
You are a senior technical writer. [ROLE]
Audience: software engineers with 2+ years Python experience. [CONTEXT]

User:
<task>
Write a 200-word explanation of the GIL (Global Interpreter Lock).
Include: what it is, why Python has it, one real-world impact on threading.
Respond in 3 numbered paragraphs.
</task>               [FORMAT specified]

<input_data>
Target: Python developers unfamiliar with CPython internals.
</input_data>         [INPUT delimited with XML]`,
'Note: XML-tagged inputs improve Claudes parsing accuracy significantly',
'L08 | Template', 7);

tableSlide('Prompting vs Fine-Tuning: When to Use What',
  ['Factor', 'Prompt Engineering', 'Fine-Tuning'],
  [
    ['Data required', 'Zero — no examples needed', '100s–10,000s labelled pairs'],
    ['Cost', 'API call only (~$0.001)', '$100–$10,000 depending on model size'],
    ['Time to deploy', 'Minutes', 'Days to weeks'],
    ['Style adaptation', 'Good with examples', 'Excellent — learns custom voice'],
    ['Format enforcement', 'Good (schema in prompt)', 'Excellent (baked in)'],
    ['Novel reasoning', 'Excellent (CoT)', 'No improvement over base model'],
    ['Use first when', 'Starting any new task', 'Prompt engineering plateaued'],
  ],
  'L08 | PE vs FT', 8);

bulletSlide('Anthropic Prompting Principles', [
  'Principle 1 — Be specific: Claude performs better with precise, unambiguous instructions',
  'Principle 2 — Use XML tags: Claude trained on XML-structured data — tags improve parsing',
  'Principle 3 — Give reasoning room: "Think step by step" before final answer improves accuracy',
  'Principle 4 — Show examples: 2-3 demonstrations outperform long textual explanations',
  'Principle 5 — Assign a role: Role priming activates relevant knowledge clusters',
  'Principle 6 — Iterate systematically: Test on 10+ inputs, categorise failures, fix root cause',
], 'L08 | Principles', 9);

twoColSlide('Prompt Failure Modes',
  'Vague Instructions',
  'Tell me about Python\\n\\nSummarise this\\n\\nMake it better\\n\\nDescribe the situation\\n\\nHelp me with this code',
  'Specific Instructions',
  'Explain Pythons GIL to a junior developer in 3 bullet points\\n\\nSummarise this product review in 2 sentences highlighting pros and cons\\n\\nRewrite for a C-suite audience in under 100 words\\n\\nDescribe the 2008 financial crisis: cause, peak impact, resolution\\n\\nIdentify the bug in this Python code and explain the fix',
  'L08 | Failures', 10);

bulletSlide('Common Prompt Anti-Patterns', [
  'Anti-pattern 1 — Implicit format: "Give me a list" without specifying count or structure',
  'Anti-pattern 2 — Overloaded task: Asking for 5 different outputs in one prompt',
  'Anti-pattern 3 — No audience spec: Claude defaults to generic; misses expert or layperson register',
  'Anti-pattern 4 — Ignoring safety: Prompts that push against Claudes guidelines will be refused',
  'Anti-pattern 5 — No iteration: Treating a first-draft prompt as production-ready',
  'Anti-pattern 6 — Context dump: Pasting 10,000 tokens of background without prioritising key facts',
], 'L08 | Anti-Patterns', 11);

bulletSlide('The Prompt Engineering Workflow', [
  'Step 1 — Define success: What does a perfect response look like? Write 3 ideal examples first',
  'Step 2 — Write baseline: Simplest possible prompt (usually just the task instruction)',
  'Step 3 — Test on 10 diverse inputs: Include easy cases, edge cases, and adversarial inputs',
  'Step 4 — Categorise failures: Hallucination / wrong format / wrong scope / wrong tone',
  'Step 5 — Fix root cause: Add role, examples, format spec, or constraint — one change at a time',
  'Step 6 — Re-test full suite: Ensure improvement does not cause regressions',
  'Step 7 — Repeat until target quality or diminishing returns — then consider fine-tuning',
], 'L08 | Workflow', 12);

codeSlide('Working with XML Tags (Anthropic Best Practice)',
`<!-- Wrap distinct input sections in semantic XML tags -->

<task>
Classify the following email as: Billing | Technical | Shipping | Other
</task>

<examples>
  <example>
    <email>My invoice is wrong this month.</email>
    <label>Billing</label>
  </example>
  <example>
    <email>App crashes when I try to upload.</email>
    <label>Technical</label>
  </example>
</examples>

<email>
  My package was supposed to arrive 3 days ago.
</email>`,
'Tip: XML tags tell Claude exactly where each component starts and ends',
'L08 | XML Tags', 13);

summarySlide('L08 — Key Takeaways', [
  { icon: '📝', title: 'Prompt = Program', body: '4 components: instruction, context, input, output format. Write all four.' },
  { icon: '🚀', title: 'Prompt First', body: 'Try prompt engineering before fine-tuning. 90% of tasks solved at inference time.' },
  { icon: '🏷', title: 'Use XML Tags', body: 'Anthropic recommends XML-delimited inputs. Improves parsing and reduces errors.' },
  { icon: '🔁', title: 'Iterate', body: 'Test 10+ inputs. Categorise failures. Fix root cause. One change at a time.' },
], 'L08 | Summary', 14);
""")

# ─── L09 slides (15–26) = 12 slides ────────────────────────────────────────
a("""
// ══════════════════════════════════════════════════
// L09 — Zero-Shot & Few-Shot Prompting (12 slides)
// ══════════════════════════════════════════════════

heroSlide('L09: Zero-Shot & Few-Shot\\nPrompting',
  'Exploiting model priors · Steering with demonstrations · Many-shot with long context',
  'L09 of 8', 15);

bulletSlide('The Prompting Spectrum', [
  'Zero-shot: No examples in the prompt — pure instruction. Relies on pre-training knowledge.',
  'One-shot: A single demonstration to anchor output format or style.',
  'Few-shot (2–8): Multiple input-output pairs. Model generalises the pattern to new inputs.',
  'Many-shot (20–500+): Long-context window packed with examples. Near fine-tuning quality.',
  'Key insight: More examples reduce ambiguity but increase token cost and latency.',
  'Practical starting point: Always try zero-shot first; add examples only if quality is insufficient.',
], 'L09 | Spectrum', 16);

bulletSlide('Making Zero-Shot Prompts Succeed', [
  'Name the task explicitly: "Classify" / "Summarise" / "Extract" — not "tell me about"',
  'Specify the output format: "Return a JSON object with fields: name, score, reason"',
  'Define the audience: "Explain to a high-school student with no statistics background"',
  'Set hard constraints: "Maximum 3 sentences. No jargon. Active voice."',
  'Assign a role: "Act as a senior Python security engineer — identify vulnerabilities"',
  'All five together = a zero-shot prompt that leaves little room for misinterpretation',
], 'L09 | Zero-Shot', 17);

tableSlide('When Zero-Shot Fails → Add Examples',
  ['Failure Pattern', 'Root Cause', 'Fix'],
  [
    ['Wrong output structure', 'Format not specified precisely', 'Show exact format in 1-2 examples'],
    ['Wrong classification label', 'Label set ambiguous or overlapping', 'Define each label + 1 example per class'],
    ['Wrong tone/register', 'Audience not specified or hard to infer', '1 demonstration in target tone'],
    ['Domain errors', 'Domain under-represented in training data', '3-5 domain-specific demonstrations'],
    ['Inconsistent depth', 'Desired depth not quantified', 'Show target depth in 1 example'],
  ],
  'L09 | Failures', 18);

codeSlide('Few-Shot: Ticket Classification',
`System: Classify support tickets into: Billing | Technical | Shipping | Other.