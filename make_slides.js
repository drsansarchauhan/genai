const pptxgen = require('/usr/local/lib/node_modules_global/lib/node_modules/pptxgenjs');

const pres = new pptxgen();
pres.layout = 'LAYOUT_16x9';
pres.title = 'CSAI601 – Generative AI with Claude';

// ─── Palette ───────────────────────────────────────────────
const BG_DARK  = '1a1a2e';
const BG_MID   = '16213e';
const BG_LIGHT = 'f8f9fa';
const ACCENT   = 'e94560';
const ACCENT2  = '0f3460';
const WHITE    = 'FFFFFF';
const MUTED    = '94a3b8';
const BODY_TXT = '334155';

const makeShadow = () => ({ type: 'outer', blur: 8, offset: 3, angle: 135, color: '000000', opacity: 0.18 });

// ─── Helper: dark section divider slide ─────────────────────
function sectionSlide(title, sub) {
  const s = pres.addSlide();
  s.background = { color: BG_DARK };
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 0.06, h: 5.625, fill: { color: ACCENT } });
  s.addText(title, { x: 0.4, y: 1.9, w: 9.2, h: 1.0, fontSize: 36, bold: true, color: WHITE, fontFace: 'Calibri', align: 'left' });
  s.addText(sub, { x: 0.4, y: 3.0, w: 9.2, h: 0.5, fontSize: 16, color: MUTED, fontFace: 'Calibri', align: 'left' });
  return s;
}

// ─── Helper: content slide with title ───────────────────────
function contentSlide(title, unit) {
  const s = pres.addSlide();
  s.background = { color: BG_LIGHT };
  // top accent bar
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.08, fill: { color: ACCENT } });
  // unit label
  s.addText(unit, { x: 0.4, y: 0.14, w: 2.5, h: 0.28, fontSize: 10, color: ACCENT, bold: true, fontFace: 'Calibri' });
  // title
  s.addText(title, { x: 0.4, y: 0.45, w: 9.2, h: 0.65, fontSize: 24, bold: true, color: BG_DARK, fontFace: 'Calibri', align: 'left' });
  // divider
  s.addShape(pres.shapes.LINE, { x: 0.4, y: 1.15, w: 9.2, h: 0, line: { color: 'dee2e6', width: 1 } });
  return s;
}

// ─── Helper: bullet block ───────────────────────────────────
function addBullets(slide, items, x, y, w, h, opts={}) {
  const arr = items.map((t, i) => ({
    text: t,
    options: { bullet: true, breakLine: i < items.length - 1, fontSize: opts.fontSize || 14, color: opts.color || BODY_TXT, fontFace: 'Calibri', paraSpaceAfter: 6 }
  }));
  slide.addText(arr, { x, y, w, h });
}

// ─── Helper: two-column layout ──────────────────────────────
function twoCol(slide, leftTitle, leftItems, rightTitle, rightItems, yStart) {
  yStart = yStart || 1.25;
  slide.addText(leftTitle, { x: 0.4, y: yStart, w: 4.4, h: 0.35, fontSize: 13, bold: true, color: ACCENT2, fontFace: 'Calibri' });
  addBullets(slide, leftItems, 0.4, yStart + 0.38, 4.4, 3.5, { fontSize: 13 });
  slide.addText(rightTitle, { x: 5.2, y: yStart, w: 4.4, h: 0.35, fontSize: 13, bold: true, color: ACCENT2, fontFace: 'Calibri' });
  addBullets(slide, rightItems, 5.2, yStart + 0.38, 4.4, 3.5, { fontSize: 13 });
}

// ─── Helper: card row (3 cards) ────────────────────────────
function threeCards(slide, cards, y) {
  y = y || 1.3;
  const w = 2.9, gap = 0.25;
  cards.forEach((c, i) => {
    const x = 0.4 + i * (w + gap);
    slide.addShape(pres.shapes.RECTANGLE, { x, y, w, h: 2.8, fill: { color: WHITE }, shadow: makeShadow() });
    slide.addShape(pres.shapes.RECTANGLE, { x, y, w, h: 0.08, fill: { color: ACCENT } });
    slide.addText(c.title, { x: x + 0.15, y: y + 0.18, w: w - 0.3, h: 0.45, fontSize: 13, bold: true, color: BG_DARK, fontFace: 'Calibri' });
    addBullets(slide, c.items, x + 0.15, y + 0.7, w - 0.3, 1.95, { fontSize: 12 });
  });
}

// ══════════════════════════════════════════════════════════════
//  SLIDE 1 — TITLE SLIDE
// ══════════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = { color: BG_DARK };
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 0.06, h: 5.625, fill: { color: ACCENT } });
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 4.9, w: 10, h: 0.725, fill: { color: BG_MID } });
  s.addText('CSAI601', { x: 0.4, y: 0.6, w: 9, h: 0.45, fontSize: 14, color: ACCENT, bold: true, fontFace: 'Calibri', charSpacing: 4 });
  s.addText('Generative AI with Claude', { x: 0.4, y: 1.1, w: 9, h: 1.1, fontSize: 42, bold: true, color: WHITE, fontFace: 'Calibri' });
  s.addText('Principles · Prompt Engineering · Application Development', { x: 0.4, y: 2.25, w: 9, h: 0.5, fontSize: 16, color: MUTED, fontFace: 'Calibri', italic: true });
  s.addText([
    { text: '3 Credits  |  ', options: { color: MUTED, fontSize: 13 } },
    { text: '36 Hours  |  ', options: { color: MUTED, fontSize: 13 } },
    { text: 'B.Tech CS/IT — 3rd Year Elective', options: { color: MUTED, fontSize: 13 } }
  ], { x: 0.4, y: 2.9, w: 9, h: 0.4 });
  s.addText('Professor, Department of Computer Science', { x: 0.4, y: 4.92, w: 9, h: 0.35, fontSize: 13, color: MUTED, fontFace: 'Calibri' });
}

// ══════════════════════════════════════════════════════════════
//  SLIDE 2 — COURSE OVERVIEW
// ══════════════════════════════════════════════════════════════
{
  const s = contentSlide('Course Overview', 'CSAI601');
  threeCards(s, [
    { title: 'What You Will Learn', items: ['LLM architecture & Claude internals', 'Prompt engineering strategies', 'Build apps with Claude API', 'Responsible AI & ethics', 'Agentic & multi-modal systems'] },
    { title: 'Prerequisites', items: ['Basic Python programming', 'Introductory ML concepts', 'Neural networks fundamentals', 'Data structures knowledge'] },
    { title: 'Assessments', items: ['5 Assignments (20 marks)', '5 Unit Quizzes (10 marks)', 'Mid-semester exam (30 marks)', 'End-semester exam (40 marks)', 'Capstone project (bonus 10)'] }
  ]);
}

// ══════════════════════════════════════════════════════════════
//  SLIDE 3 — COURSE OUTCOMES
// ══════════════════════════════════════════════════════════════
{
  const s = contentSlide('Course Outcomes (COs)', 'CSAI601');
  const rows = [
    ['CO1', "Understand the evolution of NLP, transformer architecture, and Constitutional AI principles.", "L1/L2"],
    ['CO2', "Apply systematic prompt engineering strategies to design effective LLM interactions.", "L3"],
    ['CO3', "Develop functional applications using the Claude API, chatbots, tool-use agents, RAG.", "L3/L4"],
    ['CO4', "Evaluate AI systems for bias, hallucinations, safety risks, and ethical implications.", "L4/L5"],
    ['CO5', "Design and implement end-to-end intelligent solutions with advanced Claude features.", "L5/L6"],
  ];
  s.addTable(
    [
      [{ text: 'CO', options: { bold: true, color: WHITE, fill: { color: ACCENT2 }, align: 'center', fontSize: 13 } },
       { text: 'Outcome Statement', options: { bold: true, color: WHITE, fill: { color: ACCENT2 }, fontSize: 13 } },
       { text: "Bloom's", options: { bold: true, color: WHITE, fill: { color: ACCENT2 }, align: 'center', fontSize: 13 } }],
      ...rows.map(r => [
        { text: r[0], options: { bold: true, color: ACCENT, align: 'center', fontSize: 13 } },
        { text: r[1], options: { fontSize: 12, color: BODY_TXT } },
        { text: r[2], options: { fontSize: 12, color: BODY_TXT, align: 'center' } }
      ])
    ],
    { x: 0.4, y: 1.25, w: 9.2, h: 3.8, colW: [0.7, 7.2, 1.3], border: { pt: 0.5, color: 'dee2e6' }, fontFace: 'Calibri' }
  );
}

// ══════════════════════════════════════════════════════════════
//  SECTION: UNIT 1
// ══════════════════════════════════════════════════════════════
sectionSlide('Unit 1: Foundations of Large Language Models', '7 Lecture Hours  ·  Maps to CO1');

// SLIDE — History of NLP
{
  const s = contentSlide('History of AI & NLP', 'Unit 1 — L01');
  s.addText('From Rules to Neural Networks', { x: 0.4, y: 1.25, w: 9.2, h: 0.38, fontSize: 15, bold: true, color: ACCENT2, fontFace: 'Calibri' });
  const timeline = [
    { year: '1960s', event: 'ELIZA — rule-based chatbot' },
    { year: '1990s', event: 'Statistical NLP (HMMs, n-grams)' },
    { year: '2013', event: 'Word2Vec — dense word embeddings' },
    { year: '2015', event: 'Attention mechanism (Bahdanau et al.)' },
    { year: '2017', event: '"Attention is All You Need" — Transformers' },
    { year: '2018', event: 'BERT & GPT-1 — pre-trained language models' },
    { year: '2020', event: 'GPT-3 — 175B parameter few-shot learner' },
    { year: '2022+', event: 'Claude, ChatGPT — instruction-tuned assistants' },
  ];
  timeline.forEach((t, i) => {
    const col = i < 4 ? 0 : 1;
    const row = i % 4;
    const x = col === 0 ? 0.4 : 5.1;
    const y = 1.75 + row * 0.78;
    s.addShape(pres.shapes.RECTANGLE, { x, y, w: 0.9, h: 0.35, fill: { color: ACCENT }, shadow: makeShadow() });
    s.addText(t.year, { x, y, w: 0.9, h: 0.35, fontSize: 11, bold: true, color: WHITE, fontFace: 'Calibri', align: 'center', valign: 'middle', margin: 0 });
    s.addText(t.event, { x: x + 1.0, y, w: 3.5, h: 0.35, fontSize: 12.5, color: BODY_TXT, fontFace: 'Calibri', valign: 'middle' });
  });
}

// SLIDE — Transformer Architecture
{
  const s = contentSlide('Transformer Architecture', 'Unit 1 — L02');
  twoCol(s,
    'Key Components',
    ['Multi-Head Self-Attention', 'Positional Encoding', 'Layer Normalisation', 'Feed-Forward Sub-layer', 'Residual Connections'],
    'Self-Attention Formula',
    ['Q, K, V = linear projections of input', 'Attention(Q,K,V) = softmax(QKᵀ/√dk)·V', 'Scaling by √dk prevents vanishing gradients', 'Multi-head: run h attention heads in parallel', 'Concatenate heads → linear projection']
  );
}

// SLIDE — Constitutional AI
{
  const s = contentSlide('Constitutional AI & How Claude is Trained', 'Unit 1 — L04');
  twoCol(s,
    'RLHF Pipeline',
    ['1. Supervised fine-tuning on demonstrations', '2. Train reward model on human preferences', '3. Optimise policy with PPO', '4. Iterate with human labellers', 'Limitation: expensive, human inconsistency'],
    'Constitutional AI (CAI)',
    ['Define a set of written principles', 'Model critiques its own harmful outputs', 'AI feedback replaces costly human labels', 'RLAIF: Reinforcement Learning from AI Feedback', 'Result: scalable, more consistent alignment']
  );
}

// ══════════════════════════════════════════════════════════════
//  SECTION: UNIT 2
// ══════════════════════════════════════════════════════════════
sectionSlide('Unit 2: Prompt Engineering', '8 Lecture Hours  ·  Maps to CO2');

// SLIDE — Prompting Techniques Overview
{
  const s = contentSlide('Prompting Techniques — Overview', 'Unit 2 — L08-L14');
  threeCards(s, [
    { title: 'Zero / Few-Shot', items: ['Zero-shot: instruction only', 'Few-shot: 3–5 examples in prompt', 'Example quality > quantity', 'Label formatting matters', 'Brown et al. (GPT-3, 2020)'] },
    { title: 'Chain-of-Thought', items: ['"Let\'s think step by step"', 'Zero-shot CoT triggers reasoning', 'Self-consistency: majority vote', 'Program-of-Thought (code)', 'Wei et al. (2022)'] },
    { title: 'Advanced', items: ['ReAct: Reasoning + Acting', 'Tree of Thoughts (ToT)', 'Self-critique / reflection', 'Negative prompting', 'Meta-prompting'] }
  ]);
}

// SLIDE — System Prompts
{
  const s = contentSlide('System Prompts & Structured Output', 'Unit 2 — L11-L12');
  s.addText('System Prompt Best Practices', { x: 0.4, y: 1.25, w: 9.2, h: 0.38, fontSize: 15, bold: true, color: ACCENT2, fontFace: 'Calibri' });
  addBullets(s,
    ['Define role & persona clearly: "You are a senior Python code reviewer..."',
     'State output format upfront: JSON, Markdown, XML',
     'Specify constraints: length, tone, language, prohibited topics',
     'Provide context and examples in the system prompt',
     'Use XML tags to delimit sections in long prompts: <context>, <instructions>'],
    0.4, 1.7, 9.2, 2.5, { fontSize: 13.5 });
  s.addText('Requesting Structured JSON Output', { x: 0.4, y: 4.0, w: 9.2, h: 0.35, fontSize: 14, bold: true, color: ACCENT2, fontFace: 'Calibri' });
  s.addText('Say: "Return ONLY valid JSON with keys: title (str), sentiment (pos/neg/neutral), score (0-1)"', {
    x: 0.4, y: 4.4, w: 9.2, h: 0.7, fontSize: 13, color: BODY_TXT, fontFace: 'Courier New', fill: { color: 'f1f5f9' }, valign: 'middle'
  });
}

// ══════════════════════════════════════════════════════════════
//  SECTION: UNIT 3
// ══════════════════════════════════════════════════════════════
sectionSlide('Unit 3: Building Applications with Claude API', '8 Lecture Hours  ·  Maps to CO3');

// SLIDE — API Deep Dive
{
  const s = contentSlide('Claude API — Key Concepts', 'Unit 3 — L16-L17');
  twoCol(s,
    'API Parameters',
    ['model: claude-3-5-sonnet-20241022', 'max_tokens: max output length', 'temperature: 0 (det.) to 1 (creative)', 'system: developer instructions', 'messages: conversation history array', 'stream: True for streaming output'],
    'Python SDK Quick Start',
    ['pip install anthropic', 'client = anthropic.Anthropic()', 'Env var: ANTHROPIC_API_KEY', 'client.messages.create(model, max_tokens, messages)', 'response.content[0].text = output text', 'response.usage = {input_tokens, output_tokens}']
  );
}

// SLIDE — RAG Architecture
{
  const s = contentSlide('Retrieval-Augmented Generation (RAG)', 'Unit 3 — L20');
  const steps = [
    { num: '1', title: 'Ingest', desc: 'Load documents, chunk into ~500 token pieces' },
    { num: '2', title: 'Embed', desc: 'Convert chunks to vectors using embedding model' },
    { num: '3', title: 'Store', desc: 'Save vectors in ChromaDB / FAISS / Pinecone' },
    { num: '4', title: 'Retrieve', desc: 'User query → embed → cosine similarity search' },
    { num: '5', title: 'Generate', desc: 'Pass top-k chunks + query to Claude for answer' },
  ];
  steps.forEach((step, i) => {
    const x = 0.3 + i * 1.88;
    s.addShape(pres.shapes.RECTANGLE, { x, y: 1.3, w: 1.6, h: 1.2, fill: { color: ACCENT2 }, shadow: makeShadow() });
    s.addText(step.num, { x, y: 1.3, w: 1.6, h: 0.45, fontSize: 22, bold: true, color: WHITE, fontFace: 'Calibri', align: 'center', valign: 'bottom', margin: 0 });
    s.addText(step.title, { x, y: 1.72, w: 1.6, h: 0.38, fontSize: 13, bold: true, color: WHITE, fontFace: 'Calibri', align: 'center', valign: 'middle', margin: 0 });
    if (i < 4) s.addShape(pres.shapes.LINE, { x: x + 1.6, y: 1.9, w: 0.28, h: 0, line: { color: ACCENT, width: 2 } });
    s.addText(step.desc, { x: x - 0.1, y: 2.7, w: 1.8, h: 1.0, fontSize: 11.5, color: BODY_TXT, fontFace: 'Calibri', align: 'center' });
  });
  s.addText('Why RAG? → Reduces hallucinations · Keeps knowledge current · Source-attributable answers', {
    x: 0.4, y: 4.5, w: 9.2, h: 0.5, fontSize: 13.5, color: ACCENT2, bold: true, fontFace: 'Calibri', align: 'center'
  });
}

// ══════════════════════════════════════════════════════════════
//  SECTION: UNIT 4
// ══════════════════════════════════════════════════════════════
sectionSlide('Unit 4: Responsible AI, Safety & Ethics', '6 Lecture Hours  ·  Maps to CO4');

// SLIDE — Hallucinations
{
  const s = contentSlide('Hallucinations — Causes & Mitigation', 'Unit 4 — L25');
  twoCol(s,
    'Why LLMs Hallucinate',
    ['Training objective: predict next token', 'No internal truth/falsity signal', 'Over-confidence from RLHF', 'Out-of-distribution queries', 'Conflicting training data'],
    'Mitigation Strategies',
    ['RAG: ground answers in retrieved docs', 'Chain-of-Verification (CoVe)', 'Self-consistency checking', 'Source citation enforcement', 'Human-in-the-loop for high-stakes tasks', 'Structured output + validation']
  );
}

// SLIDE — Ethics Frameworks
{
  const s = contentSlide('AI Ethics Frameworks', 'Unit 4 — L26-L28');
  threeCards(s, [
    { title: "Anthropic's HHH", items: ['Helpful: assist users effectively', 'Harmless: avoid causing harm', 'Honest: truthful, calibrated', 'Constitutional AI principles', 'RLAIF training for alignment'] },
    { title: 'EU AI Act', items: ['Unacceptable risk: banned uses', 'High risk: healthcare, hiring', 'Limited risk: transparency req.', 'Minimal risk: most AI apps', 'Effective 2024–2026 rollout'] },
    { title: 'NIST AI RMF', items: ['Govern: culture & policies', 'Map: context & risk categories', 'Measure: quantify risk', 'Manage: mitigate & monitor', 'Iterative, not one-time'] }
  ]);
}

// ══════════════════════════════════════════════════════════════
//  SECTION: UNIT 5
// ══════════════════════════════════════════════════════════════
sectionSlide('Unit 5: Advanced Topics & Capstone', '7 Lecture Hours  ·  Maps to CO3, CO5');

// SLIDE — Agentic AI
{
  const s = contentSlide('Agentic AI — Agent Architecture', 'Unit 5 — L30-L31');
  twoCol(s,
    'Agent Loop Components',
    ['Perceive: receive user goal + context', 'Plan: decompose into sub-tasks (Claude)', 'Act: call tools (web, DB, code)', 'Observe: read tool results', 'Reflect: evaluate progress', 'Respond: return final answer'],
    'Memory Types',
    ['In-context: recent conversation turns', 'External (vector DB): long-term knowledge', 'Episodic: past interaction summaries', 'Procedural: in-system-prompt knowledge', 'Working: scratchpad in extended thinking']
  );
}

// SLIDE — MCP
{
  const s = contentSlide('Model Context Protocol (MCP)', 'Unit 5 — L32');
  s.addText('What is MCP?', { x: 0.4, y: 1.25, w: 9.2, h: 0.38, fontSize: 15, bold: true, color: ACCENT2, fontFace: 'Calibri' });
  addBullets(s, [
    'Open protocol by Anthropic for connecting Claude to external tools & data sources',
    'MCP Host (e.g., Claude Desktop / IDE) ↔ MCP Client ↔ MCP Server',
    'MCP Server exposes: Tools (actions), Resources (read-only data), Prompts (templates)',
    'Examples: File system server, PostgreSQL server, GitHub server, Slack server',
    'Developer builds MCP servers using Python or TypeScript SDK',
    'Enables a rich ecosystem: Claude connects to ANY tool through standardised protocol'
  ], 0.4, 1.7, 9.2, 3.3, { fontSize: 13.5 });
}

// SLIDE — Capstone Project
{
  const s = contentSlide('Capstone Project', 'Unit 5 — L36');
  s.addText('Design & Build a Real AI Application Powered by Claude', {
    x: 0.4, y: 1.25, w: 9.2, h: 0.5, fontSize: 16, bold: false, italic: true, color: ACCENT2, fontFace: 'Calibri'
  });
  const ideas = [
    ['📚 Education', 'Personalised doubt solver for CS students'],
    ['🏥 Healthcare', 'Medical literature summariser with citations'],
    ['⚖️ Legal', 'Contract clause extractor & risk analyser'],
    ['💼 Productivity', 'AI meeting assistant with action items'],
    ['♿ Accessibility', 'Image description tool for visually impaired'],
    ['💻 Dev Tools', 'Multi-agent code review & test generator'],
  ];
  ideas.forEach((idea, i) => {
    const col = i % 2;
    const row = Math.floor(i / 2);
    const x = col === 0 ? 0.4 : 5.2;
    const y = 1.9 + row * 0.9;
    s.addShape(pres.shapes.RECTANGLE, { x, y, w: 4.5, h: 0.7, fill: { color: i % 2 === 0 ? 'f0f4ff' : 'fff0f3' }, shadow: makeShadow() });
    s.addText(idea[0], { x: x + 0.15, y, w: 1.1, h: 0.7, fontSize: 20, valign: 'middle', margin: 0 });
    s.addText(idea[1], { x: x + 1.2, y, w: 3.1, h: 0.7, fontSize: 12.5, color: BODY_TXT, fontFace: 'Calibri', valign: 'middle' });
  });
}

// ══════════════════════════════════════════════════════════════
//  SLIDE — THANK YOU
// ══════════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = { color: BG_DARK };
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 0.06, h: 5.625, fill: { color: ACCENT } });
  s.addText('Start Learning', { x: 0.4, y: 1.5, w: 9, h: 0.5, fontSize: 16, color: ACCENT, bold: true, fontFace: 'Calibri' });
  s.addText('docs.anthropic.com', { x: 0.4, y: 2.1, w: 9, h: 0.8, fontSize: 36, bold: true, color: WHITE, fontFace: 'Calibri' });
  s.addText([
    { text: 'Questions?  ', options: { color: MUTED, fontSize: 16 } },
    { text: 'claude.ai/chat', options: { color: ACCENT, fontSize: 16, bold: true } }
  ], { x: 0.4, y: 3.1, w: 9, h: 0.5 });
  s.addText('CSAI601  ·  Generative AI with Claude  ·  B.Tech CS/IT', {
    x: 0.4, y: 4.8, w: 9, h: 0.4, fontSize: 12, color: MUTED, fontFace: 'Calibri'
  });
}

// ══════════════════════════════════════════════════════════════
pres.writeFile({ fileName: '/sessions/blissful-quirky-tesla/mnt/outputs/CSAI601_Lecture_Slides.pptx' })
  .then(() => console.log('PPTX written OK'))
  .catch(e => { console.error('PPTX error:', e.message); process.exit(1); });
