'use strict';
const PptxGenJS = require('/usr/local/lib/node_modules_global/lib/node_modules/pptxgenjs');
const pres = new PptxGenJS();

// ── Palette ─────────────────────────────────────────────────────────
const C = {
  navy:   '0f1f3d',
  blue:   '1a3a6b',
  red:    'e94560',
  teal:   '0a7c8c',
  gold:   'f4a832',
  green:  '27ae60',
  purple: '7b2fbe',
  white:  'ffffff',
  light:  'e8edf5',
  mid:    'b0bcd4',
  dark:   '1e2a45',
  code:   '0d1117',
};

pres.layout = 'LAYOUT_16x9';
pres.author  = 'CSAI601 Course Team';
pres.title   = 'CSAI601 Unit 1 — Foundations of Large Language Models';

// ── Helpers ──────────────────────────────────────────────────────────
function bg(slide, col) {
  slide.background = { color: col || C.navy };
}

function rect(slide, x, y, w, h, col, opts) {
  slide.addShape(pres.ShapeType.rect, Object.assign({ x, y, w, h, fill: { color: col } }, opts || {}));
}

function txt(slide, text, x, y, w, h, opts) {
  slide.addText(text, Object.assign({ x, y, w, h, margin: 0 }, opts || {}));
}

// Standard title bar at top
function titleBar(slide, unit, lecture) {
  rect(slide, 0, 0, 10, 0.45, C.blue);
  txt(slide, unit,    0.15, 0.04, 5,   0.37, { fontSize:9, color: C.mid,   bold:false, fontFace:'Calibri' });
  txt(slide, lecture, 5,   0.04, 4.8, 0.37, { fontSize:9, color: C.gold,  bold:true,  fontFace:'Calibri', align:'right' });
}

function bottomBar(slide, num) {
  rect(slide, 0, 5.3, 10, 0.325, C.dark);
  txt(slide, 'CSAI601 · Generative AI with Claude · Unit 1', 0.2, 5.33, 7, 0.28, { fontSize:7.5, color: C.mid, fontFace:'Calibri' });
  txt(slide, String(num), 9.5, 5.33, 0.45, 0.28, { fontSize:7.5, color: C.mid, align:'right', fontFace:'Calibri' });
}

// Hero slide (section divider)
function heroSlide(num, unit, title, sub, accentCol) {
  const s = pres.addSlide();
  bg(s, C.navy);
  rect(s, 0, 0, 0.18, 5.625, accentCol || C.red);
  rect(s, 0, 5.0, 10, 0.625, C.dark);
  txt(s, unit,  0.4, 0.6, 9.5, 0.5, { fontSize:11, color: accentCol||C.red, bold:true,  fontFace:'Calibri', charSpacing:3 });
  txt(s, title, 0.4, 1.2, 9.2, 1.8, { fontSize:38, color: C.white, bold:true,  fontFace:'Calibri', wrap:true });
  txt(s, sub,   0.4, 3.1, 8.5, 0.8, { fontSize:14, color: C.light, bold:false, fontFace:'Calibri' });
  txt(s, 'CSAI601 · B.Tech CS/IT 3rd Year · 3 Credits', 0.4, 5.1, 9, 0.4, { fontSize:8.5, color: C.mid, fontFace:'Calibri' });
  bottomBar(s, num);
  return s;
}

// Content slide with title + bullets
function bulletSlide(num, lec, heading, items, col) {
  const s = pres.addSlide();
  bg(s);
  titleBar(s, 'Unit 1 · Foundations of LLMs', lec);
  rect(s, 0.25, 0.55, 0.08, 0.7, col || C.red);
  txt(s, heading, 0.42, 0.5, 9.3, 0.72, { fontSize:22, color: C.white, bold:true, fontFace:'Calibri' });
  const rich = items.map((it, i) => {
    const isLast = i === items.length - 1;
    if (typeof it === 'string') {
      return { text: it, options: { bullet:true, fontSize:14, color: C.light, fontFace:'Calibri', breakLine: !isLast } };
    }
    return Object.assign({ options: { breakLine: !isLast } }, it);
  });
  txt(s, rich, 0.35, 1.35, 9.3, 3.75, {});
  bottomBar(s, num);
  return s;
}

// Two-column slide
function twoColSlide(num, lec, heading, leftTitle, leftItems, rightTitle, rightItems, col) {
  const s = pres.addSlide();
  bg(s);
  titleBar(s, 'Unit 1 · Foundations of LLMs', lec);
  rect(s, 0.25, 0.55, 0.08, 0.7, col || C.red);
  txt(s, heading, 0.42, 0.5, 9.3, 0.72, { fontSize:22, color: C.white, bold:true, fontFace:'Calibri' });
  // divider
  rect(s, 5.0, 1.35, 0.02, 3.8, C.blue);
  // left
  txt(s, leftTitle, 0.3, 1.38, 4.5, 0.4, { fontSize:13, color: col||C.red, bold:true, fontFace:'Calibri' });
  const lRich = leftItems.map((it,i) => ({ text: it, options: { bullet:true, fontSize:12.5, color: C.light, fontFace:'Calibri', breakLine: i<leftItems.length-1 } }));
  txt(s, lRich, 0.3, 1.85, 4.55, 3.2, {});
  // right
  txt(s, rightTitle, 5.15, 1.38, 4.5, 0.4, { fontSize:13, color: col||C.gold, bold:true, fontFace:'Calibri' });
  const rRich = rightItems.map((it,i) => ({ text: it, options: { bullet:true, fontSize:12.5, color: C.light, fontFace:'Calibri', breakLine: i<rightItems.length-1 } }));
  txt(s, rRich, 5.15, 1.85, 4.6, 3.2, {});
  bottomBar(s, num);
  return s;
}

// Code slide
function codeSlide(num, lec, heading, code, note, col) {
  const s = pres.addSlide();
  bg(s);
  titleBar(s, 'Unit 1 · Foundations of LLMs', lec);
  rect(s, 0.25, 0.55, 0.08, 0.7, col || C.teal);
  txt(s, heading, 0.42, 0.5, 9.3, 0.72, { fontSize:22, color: C.white, bold:true, fontFace:'Calibri' });
  // code box
  rect(s, 0.3, 1.35, 9.4, 3.4, C.code, { line: { color: C.teal, width:1 }, rounding:0.05 });
  txt(s, code, 0.5, 1.45, 9.0, 3.2, { fontSize:10.5, color: 'a8d8ea', fontFace:'Courier New', wrap:true });
  if (note) txt(s, '💡 ' + note, 0.3, 4.85, 9.4, 0.35, { fontSize:11, color: C.gold, fontFace:'Calibri', italic:true });
  bottomBar(s, num);
  return s;
}

// Formula slide
function formulaSlide(num, lec, heading, formula, explanation, col) {
  const s = pres.addSlide();
  bg(s);
  titleBar(s, 'Unit 1 · Foundations of LLMs', lec);
  rect(s, 0.25, 0.55, 0.08, 0.7, col || C.purple);
  txt(s, heading, 0.42, 0.5, 9.3, 0.72, { fontSize:22, color: C.white, bold:true, fontFace:'Calibri' });
  // formula box
  rect(s, 1.0, 1.35, 8.0, 1.3, '1a0a2e', { line:{ color: col||C.purple, width:2 } });
  txt(s, formula, 1.0, 1.35, 8.0, 1.3, { fontSize:18, color: col||C.gold, fontFace:'Courier New', align:'center', valign:'middle', bold:true });
  const exRich = explanation.map((it,i) => ({ text: it, options: { bullet:true, fontSize:13, color: C.light, fontFace:'Calibri', breakLine: i<explanation.length-1 } }));
  txt(s, exRich, 0.4, 2.8, 9.2, 2.3, {});
  bottomBar(s, num);
  return s;
}

// Summary slide
function summarySlide(num, lec, keyPoints, col) {
  const s = pres.addSlide();
  bg(s, C.dark);
  titleBar(s, 'Unit 1 · Foundations of LLMs', lec);
  rect(s, 0, 0.45, 10, 0.06, col || C.red);
  txt(s, 'Lecture Summary & Key Takeaways', 0.4, 0.6, 9.2, 0.7, { fontSize:24, color: C.white, bold:true, fontFace:'Calibri' });
  keyPoints.forEach((kp, i) => {
    const col2 = [C.red, C.gold, C.teal, C.green, C.purple][i % 5];
    const row = i < 3 ? 0 : 1;
    const col3 = i % 3;
    const bx = 0.2 + col3 * 3.27;
    const by = 1.4 + row * 1.85;
    rect(s, bx, by, 3.15, 1.7, C.navy, { line:{ color: col2, width:1.5 }, rounding:0.08 });
    rect(s, bx, by, 3.15, 0.32, col2, { rounding:0.0 });
    txt(s, kp.title, bx+0.1, by+0.03, 2.95, 0.28, { fontSize:10.5, color: C.white, bold:true, fontFace:'Calibri' });
    txt(s, kp.body,  bx+0.1, by+0.38, 2.95, 1.25, { fontSize:9.5,  color: C.light, fontFace:'Calibri', wrap:true });
  });
  bottomBar(s, num);
  return s;
}

// ════════════════════════════════════════════════════════════════════
//  COURSE TITLE SLIDE
// ════════════════════════════════════════════════════════════════════
let n = 1;
{
  const s = pres.addSlide();
  bg(s, C.navy);
  rect(s, 0, 0, 10, 0.06, C.red);
  rect(s, 0, 5.565, 10, 0.06, C.red);
  rect(s, 0, 0.06, 0.08, 5.505, C.red);
  rect(s, 9.92, 0.06, 0.08, 5.505, C.red);
  txt(s, 'CSAI601',  0.3, 0.3,  9.4, 1.0, { fontSize:52, color: C.red, bold:true, fontFace:'Calibri', align:'center' });
  txt(s, 'Generative AI with Claude', 0.3, 1.3, 9.4, 0.8, { fontSize:26, color: C.white, bold:true, fontFace:'Calibri', align:'center' });
  txt(s, 'UNIT 1 — Foundations of Large Language Models', 0.3, 2.1, 9.4, 0.55, { fontSize:14, color: C.gold, bold:true, fontFace:'Calibri', align:'center', charSpacing:2 });
  rect(s, 2.5, 2.82, 5.0, 0.025, C.blue);
  txt(s, '7 Lectures  ·  7 Hours  ·  CO1 & CO2', 0.3, 2.9, 9.4, 0.4, { fontSize:12, color: C.mid, fontFace:'Calibri', align:'center' });
  txt(s, 'B.Tech CS / IT  ·  3rd Year  ·  3 Credits', 0.3, 3.38, 9.4, 0.38, { fontSize:11.5, color: C.mid, fontFace:'Calibri', align:'center' });
  txt(s, 'Lecture slides prepared using course notes. For classroom & self-study use.', 0.3, 4.9, 9.4, 0.35, { fontSize:9, color: C.mid, fontFace:'Calibri', align:'center', italic:true });
  bottomBar(s, n++);
}

// ════════════════════════════════════════════════════════════════════
//  UNIT 1 OVERVIEW
// ════════════════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  bg(s, C.dark);
  titleBar(s, 'Unit 1 · Foundations of LLMs', 'Unit Overview');
  txt(s, 'What You Will Learn in Unit 1', 0.4, 0.55, 9.2, 0.75, { fontSize:24, color: C.white, bold:true, fontFace:'Calibri' });
  const rows = [
    ['L01', 'History of AI & NLP',        'From ELIZA to Word2Vec — 70 years of language AI'],
    ['L02', 'Transformer Architecture',    'Q/K/V attention, positional encoding, FFN, residuals'],
    ['L03', 'LLM Landscape & Claude',      'Scaling laws, GPT lineage, Anthropic vs. OpenAI'],
    ['L04', 'Constitutional AI',           'RLHF, CAI critique-revision, RLAIF, HHH principles'],
    ['L05', "Claude's Capabilities",       '200K context, vision, tool use, behavioural safety'],
    ['L06', 'Tokenisation & Sampling',     'BPE algorithm, temperature, top-p, top-k controls'],
    ['L07', 'Lab: First API Call',         'Python SDK, multi-turn, streaming, error handling'],
  ];
  const cols2 = [C.red, C.gold, C.teal, C.purple, C.green, C.blue, C.red];
  rows.forEach(([lbl, title, desc], i) => {
    const y = 1.4 + i * 0.57;
    rect(s, 0.25, y, 0.55, 0.46, cols2[i]);
    txt(s, lbl, 0.25, y, 0.55, 0.46, { fontSize:10, color: C.white, bold:true, fontFace:'Calibri', align:'center', valign:'middle' });
    txt(s, title, 0.9, y+0.04, 3.2, 0.38, { fontSize:12.5, color: C.white, bold:true, fontFace:'Calibri' });
    txt(s, desc,  4.1, y+0.06, 5.7, 0.35, { fontSize:11,   color: C.mid,   fontFace:'Calibri' });
  });
  bottomBar(s, n++);
}

// ════════════════════════════════════════════════════════════════════
//  LECTURE 01 — History of AI & NLP  (slides 3–16)
// ════════════════════════════════════════════════════════════════════
heroSlide(n++, 'LECTURE 01', 'History of AI & NLP', 'From Rule-Based Systems to the Attention Revolution — 1950 to 2017', C.red);

bulletSlide(n++, 'L01 · History of AI & NLP', 'Learning Objectives', [
  'Trace the complete 70-year evolution of NLP — rules → statistics → deep learning → transformers',
  'Explain why symbolic AI and early statistical methods failed at open-domain language tasks',
  'Describe Word2Vec and demonstrate how dense embeddings capture semantic relationships mathematically',
  'Identify the three core limitations of RNNs/LSTMs (vanishing gradients, sequential bottleneck, fixed context)',
  'Explain the Bahdanau attention mechanism and why it was the conceptual precursor to transformers',
  'Articulate why "Attention Is All You Need" (2017) was a paradigm shift in NLP',
], C.red);

// NLP era timeline
bulletSlide(n++, 'L01 · History of AI & NLP', 'Era 1: Symbolic & Rule-Based NLP (1950–1980)', [
  '1950 — Alan Turing proposes the Turing Test: "Can a machine think?" — language as the benchmark',
  '1966 — ELIZA (MIT): pattern-matching chatbot; matched "I am sad" → replied "Why are you sad?" — zero understanding',
  '1970s — Conceptual Dependency (Schank): hand-crafted semantic frames for story understanding',
  'ATN Grammars: formal rules for parsing sentences — "The cat sat on the mat" → subject/verb/object trees',
  'Core problem: Brittleness. Outside pre-written rules, systems failed completely. Real language is ambiguous, creative, contextual',
  'Combinatorial explosion: English has ~1 million words; hand-coding all rules was impossible',
], C.red);

bulletSlide(n++, 'L01 · History of AI & NLP', 'Era 2: Statistical NLP (1990–2012)', [
  'Shift from hand-coded rules to learning patterns from data — IBM speech recognition (1990s)',
  'N-gram language models: P("dog"|"The big") = count("The big dog")/count("The big") from large corpora',
  'Tri-gram limitation: P(w₃|w₁,w₂) — context window fixed at 2 words, cannot capture long-range dependencies',
  'Maximum Entropy, CRF, SVM applied to NLP tasks (POS tagging, NER, parsing)',
  'IBM word alignment models (1990): statistical machine translation — probabilistic bilingual dictionaries',
  'Breakthrough: Penn Treebank (1993) — labeled corpus enabling supervised learning at scale',
], C.red);

twoColSlide(n++, 'L01 · History of AI & NLP', 'N-Gram Models vs. Neural Language Models',
  'N-Gram Models (Statistical)',
  [
    'Count-based: P(wₙ|w₁…wₙ₋₁)',
    'Context limited to n-1 words',
    'Sparse: unseen n-grams get probability 0',
    'Smoothing required (Laplace, Kneser-Ney)',
    'No semantic similarity captured',
    '"cat" and "feline" are completely different',
    'Fast to train; interpretable',
    'Fails on long-range dependencies',
  ],
  'Neural Language Models (2003+)',
  [
    'Bengio et al. 2003: first neural LM',
    'Words mapped to dense vectors (embeddings)',
    'Generalises to unseen word combinations',
    '"cat" and "feline" have similar vectors',
    'MLP predicts next word from context vectors',
    'Handles longer contexts than n-grams',
    'More expensive to train',
    'Laid the foundation for Word2Vec & GPT',
  ],
  C.red
);

// Word2Vec
formulaSlide(n++, 'L01 · History of AI & NLP', 'Word2Vec: Dense Word Embeddings (2013)',
  'vector("king") − vector("man") + vector("woman") ≈ vector("queen")',
  [
    'Mikolov et al. (2013) — Google — 300-dim vectors trained on 100 billion words',
    'CBOW: predict centre word from context words — fast, better for frequent words',
    'Skip-gram: predict context words from centre word — better for rare words',
    'Semantic arithmetic works: Paris − France + Italy ≈ Rome',
    'Captures analogy, sentiment, and syntactic relationships in continuous vector space',
    'Limitation: one vector per word — "bank" (river) and "bank" (finance) get the same vector',
  ], C.gold
);

bulletSlide(n++, 'L01 · History of AI & NLP', 'Era 3: Deep Learning for NLP (2012–2017)', [
  '2012 — AlexNet wins ImageNet by huge margin: deep CNNs work. NLP community takes notice',
  'RNNs applied to NLP: shared weights, variable-length sequences, theoretically infinite context',
  'LSTM (Hochreiter & Schmidhuber 1997, popularised 2013): gates control memory — input gate, forget gate, output gate',
  'Seq2Seq (2014, Sutskever et al.): encoder compresses sentence to fixed vector → decoder generates translation',
  'Critical flaw: information bottleneck — entire source sentence compressed to single 512-dim vector',
  'Vanishing gradient problem: gradients shrink exponentially with sequence length — model forgets early tokens',
], C.red);

// LSTM equations
formulaSlide(n++, 'L01 · History of AI & NLP', 'LSTM Gate Equations — Why They Help (But Are Not Enough)',
  'fₜ = σ(Wf·[hₜ₋₁, xₜ] + bf)   iₜ = σ(Wi·[hₜ₋₁, xₜ] + bi)',
  [
    'Forget gate fₜ: decides what fraction of memory Cₜ₋₁ to erase (0=forget all, 1=keep all)',
    'Input gate iₜ: controls how much new candidate memory C̃ₜ is written to cell',
    'Cell state Cₜ = fₜ⊙Cₜ₋₁ + iₜ⊙C̃ₜ  — long-range gradient highway',
    'Output gate oₜ = σ(Wo·[hₜ₋₁,xₜ]+bo); hₜ = oₜ⊙tanh(Cₜ)',
    'Problem remaining: still processes tokens sequentially → cannot parallelise → slow to train',
    'Still limited context for very long documents; information must pass through chain of hidden states',
  ], C.purple
);

twoColSlide(n++, 'L01 · History of AI & NLP', 'Bahdanau Attention — The Key Idea (2015)',
  'Before Attention (Fixed Vector)',
  [
    'Encoder → single vector h_end',
    'Decoder must use same vector for all output words',
    'Long sentences: vector saturates with info',
    '"The cat sat on the mat. It was happy."',
    '"It" refers to "cat" — but vector has lost that',
    'Translation quality degrades with length',
  ],
  'With Attention (Dynamic Context)',
  [
    'Keep ALL encoder hidden states {h₁…hT}',
    'At each decoder step t: compute alignment scores eₜᵢ = score(sₜ₋₁, hᵢ)',
    'Softmax → attention weights αₜᵢ (sum=1)',
    'Context vector cₜ = Σ αₜᵢ·hᵢ',
    'Decoder attends to relevant input tokens',
    'Breakthrough: O(1) distance between any two positions',
  ], C.teal
);

formulaSlide(n++, 'L01 · History of AI & NLP', 'Bahdanau Attention Formula',
  'αₜᵢ = softmax(eₜᵢ)   where eₜᵢ = vᵀ tanh(Wₛsₜ₋₁ + Wₕhᵢ)',
  [
    'eₜᵢ: alignment score — how well decoder state sₜ₋₁ matches encoder hidden state hᵢ',
    'Wₛ, Wₕ, v: learnable weight matrices trained end-to-end with the seq2seq model',
    'αₜᵢ: attention weight — what fraction of attention decoder step t pays to input position i',
    'Context vector cₜ = Σᵢ αₜᵢ·hᵢ — weighted sum of all encoder states',
    'Result: BLEU score on EN-FR translation improved by 3 points over no-attention baseline',
    'Insight: the attention matrix is interpretable — shows which input word each output word aligns to',
  ], C.teal
);

bulletSlide(n++, 'L01 · History of AI & NLP', '"Attention Is All You Need" — 2017 Paradigm Shift', [
  'Vaswani et al. (2017), Google Brain — 8 authors, 50,000+ citations — one of most cited CS papers ever',
  'Key insight: throw away the RNN entirely — use only self-attention + feed-forward layers',
  'Self-attention: every token attends to every other token in the sequence simultaneously (O(n²) but parallelisable)',
  'No sequential dependency → fully parallel training → 10× faster than LSTM on same hardware',
  'Scales to billions of parameters with the same architecture — RNNs hit memory walls',
  'All modern LLMs (GPT-4, Gemini, Claude, Llama) are transformer-based — L01 ends; L02 dives into mechanics',
], C.red);

summarySlide(n++, 'Lecture 01 — History of AI & NLP', [
  { title: 'Symbolic AI (1950–80)', body: 'Rule-based, brittle. ELIZA pattern-matched but did not understand.' },
  { title: 'Statistical NLP (1990–12)', body: 'N-grams, HMMs, SVMs. Data-driven but limited context window.' },
  { title: 'Word2Vec (2013)', body: 'Dense embeddings: king−man+woman≈queen. Semantic arithmetic works.' },
  { title: 'LSTM & Seq2Seq', body: 'Gates prevent vanishing gradients. Fixed-vector bottleneck remains.' },
  { title: 'Bahdanau Attention', body: 'Dynamic context from all encoder states. O(1) position distance.' },
  { title: 'Transformers (2017)', body: '"Attention Is All You Need." Parallel training + massive scaling.' },
], C.red);

// ════════════════════════════════════════════════════════════════════
//  LECTURE 02 — Transformer Architecture  (slides 15–28)
// ════════════════════════════════════════════════════════════════════
heroSlide(n++, 'LECTURE 02', 'Transformer Architecture', 'Query · Key · Value · Multi-Head Attention · Positional Encoding · FFN · Residuals', C.teal);

bulletSlide(n++, 'L02 · Transformer Architecture', 'Transformer — Big Picture', [
  'Original paper: encoder-decoder for translation. Modern LLMs use decoder-only (GPT) or encoder-only (BERT)',
  'Encoder stack: N identical layers, each = Multi-Head Self-Attention + FFN + Layer Norm + Residual Connection',
  'Decoder stack: same as encoder + cross-attention layer that attends to encoder output',
  'All positions processed in parallel — tokens interact via attention, not sequential hidden state passing',
  'Three types of attention: (1) Self-attention in encoder, (2) Masked self-attention in decoder, (3) Cross-attention',
  'Key property: O(1) path length between any two tokens — model can learn long-range dependencies easily',
], C.teal);

formulaSlide(n++, 'L02 · Transformer Architecture', 'Scaled Dot-Product Attention',
  'Attention(Q, K, V) = softmax( QKᵀ / √dₖ ) · V',
  [
    'Q (Query): "What am I looking for?" — comes from current token representation',
    'K (Key):   "What do I contain?" — comes from all tokens in context',
    'V (Value): "What information do I carry?" — the actual content to retrieve',
    'QKᵀ: dot products measure similarity between queries and keys → raw attention scores',
    '÷√dₖ: scale factor prevents softmax from entering saturation zone (dₖ = key dimension, typically 64)',
    'softmax: converts scores to probability distribution (weights sum to 1)',
    'Final output: weighted sum of Values — tokens with high attention contribute more to output',
  ], C.teal
);

bulletSlide(n++, 'L02 · Transformer Architecture', 'Q, K, V — Deep Intuition with Analogy', [
  'Database analogy: Keys=index, Values=stored data. Query searches index and retrieves weighted values',
  'Word "it" in "The cat chased the mouse. It was scared" — Q(it) asks "who does \'it\' refer to?"',
  'K(cat) and K(mouse) both respond; softmax gives high weight to "cat" or "mouse" based on context',
  'V(cat) and V(mouse) carry their semantics; output of attention at "it" = mix of those semantics',
  'Linear projections: Wq, Wk, Wv — learned matrices that project input x into Q, K, V spaces',
  'Q=xWq, K=xWk, V=xWv — projections are trained end-to-end; model learns what queries/keys are useful',
], C.teal);

bulletSlide(n++, 'L02 · Transformer Architecture', 'Multi-Head Attention', [
  'Single attention head captures one relationship type. Language is multi-relational — we need many',
  'Multi-head: run h parallel attention heads with different Wq_i, Wk_i, Wv_i projection matrices',
  'MultiHead(Q,K,V) = Concat(head₁,…,headₕ)Wₒ    where headᵢ = Attention(QWqᵢ, KWkᵢ, VWvᵢ)',
  'Each head learns a different aspect: head 1 = syntax, head 2 = coreference, head 3 = semantic similarity…',
  'GPT-3: 96 attention heads per layer, dₖ = 128 each — 96×128 = 12,288 model dimension (dmodel)',
  'Concat + Wₒ projection: h head outputs of dim dₖ → single vector of dim dmodel. Reduces parameters.',
], C.teal);

formulaSlide(n++, 'L02 · Transformer Architecture', 'Positional Encoding — Giving Order to a Bag of Words',
  'PE(pos, 2i) = sin(pos / 10000^(2i/dmodel))    PE(pos, 2i+1) = cos(pos / 10000^(2i/dmodel))',
  [
    'Without positional encoding, attention is permutation-invariant — "cat sat mat" = "mat sat cat"',
    'Add PE to token embedding before first layer: x̃ = embedding(token) + PE(position)',
    'Each position gets a unique pattern of sines and cosines at different frequencies',
    'Low dimensions: fast oscillations (distinguish adjacent tokens); High dimensions: slow oscillations (distinguish distant positions)',
    'PE(pos+k) can be expressed as linear function of PE(pos) — model can learn "relative position" reasoning',
    'Modern alternative: Rotary Position Embeddings (RoPE) used in Claude, LLaMA — encodes relative not absolute position',
  ], C.purple
);

bulletSlide(n++, 'L02 · Transformer Architecture', 'Feed-Forward Network (FFN) in Each Layer', [
  'Every transformer layer has: Attention → Add & Norm → FFN → Add & Norm',
  'FFN(x) = max(0, xW₁ + b₁)W₂ + b₂  — two linear layers with ReLU in between',
  'Attention = routing (which tokens talk to which); FFN = computation (what to think about it)',
  'FFN dimension is typically 4× model dim: dmodel=768 → dFFN=3072 (BERT-base); dmodel=12288 → dFFN=49152 (GPT-3)',
  'Mechanistic interpretation: FFN layers store factual knowledge — specific neurons fire for "Paris is the capital of"',
  'Modern variants: SwiGLU activation (Claude, LLaMA), Gated Linear Units — improve training stability and performance',
], C.teal);

twoColSlide(n++, 'L02 · Transformer Architecture', 'Residual Connections & Layer Normalisation',
  'Residual Connections (Skip Connections)',
  [
    'Output = LayerNorm(x + Sublayer(x))',
    'Gradient flows directly through addition → no vanishing gradient',
    'Enables training of very deep networks (96 layers in GPT-3)',
    'Each layer refines, not replaces, the representation',
    'Introduced by He et al. ResNet (2015) for CV',
    'Critical for transformer depth > 6 layers',
  ],
  'Layer Normalisation',
  [
    'LayerNorm: normalise across feature dimension (not batch)',
    'μ = mean of all features; σ = std dev',
    'x̂ = (x − μ) / (σ + ε) — zero mean, unit variance',
    'Scale & shift: γ·x̂ + β — learnable parameters',
    'Applied before (Pre-LN) or after (Post-LN) sublayer',
    'Stabilises training; allows higher learning rates',
  ], C.teal
);

twoColSlide(n++, 'L02 · Transformer Architecture', 'BERT vs GPT — Two Uses of the Transformer',
  'BERT (Encoder-Only)',
  [
    'Bidirectional: every token sees all others',
    'Task: Masked Language Modelling (MLM)',
    '15% of tokens masked → predict them',
    'Next Sentence Prediction (NSP)',
    'Used for: classification, NER, Q&A',
    'Cannot generate text autoregressively',
    '110M params (base) / 340M (large)',
    'Fine-tuned on downstream tasks',
  ],
  'GPT (Decoder-Only)',
  [
    'Causal/unidirectional: sees only past tokens',
    'Task: Next Token Prediction (CLM)',
    'Autoregressive: generates token by token',
    'Causal mask: upper triangle of attn = −∞',
    'Used for: text generation, dialogue, code',
    'Zero-shot & few-shot via prompting',
    'GPT-3: 175B params; GPT-4: ~1T (est.)',
    'Claude uses decoder-only transformer',
  ], C.teal
);

bulletSlide(n++, 'L02 · Transformer Architecture', 'Masked Self-Attention in Decoder (Causal Mask)', [
  'In GPT-style generation: token at position t cannot see tokens at positions t+1, t+2… (future)',
  'Causal mask: set attention score to −∞ before softmax for all future positions',
  'After softmax, e^(−∞) = 0 — effectively zero attention weight on future tokens',
  'At inference: generate token by token; pass all previous tokens back through model for each new token (KV cache optimises this)',
  'Training: teacher forcing — entire sequence fed at once, causal mask simulates autoregressive property for efficiency',
  'This is why GPT/Claude "predicts the next token" — each token is trained to predict its own next token given all previous',
], C.teal);

summarySlide(n++, 'Lecture 02 — Transformer Architecture', [
  { title: 'Scaled Dot-Product Attn', body: 'softmax(QKᵀ/√dk)·V — Q asks, K matches, V delivers.' },
  { title: 'Multi-Head Attention', body: 'h parallel heads capture syntax, coreference, semantics in parallel.' },
  { title: 'Positional Encoding', body: 'Sine/cosine at multiple frequencies inject position info.' },
  { title: 'FFN Layer', body: 'max(0, xW₁+b₁)W₂+b₂ — computes per-position transformations.' },
  { title: 'Residual + LayerNorm', body: 'x + Sublayer(x); enables deep networks; stabilises training.' },
  { title: 'BERT vs GPT', body: 'Encoder-bidirectional for understanding; Decoder-causal for generation.' },
], C.teal);

// ════════════════════════════════════════════════════════════════════
//  LECTURE 03 — LLM Landscape & Claude  (slides 29–41)
// ════════════════════════════════════════════════════════════════════
heroSlide(n++, 'LECTURE 03', 'LLM Landscape & Claude', 'Scaling Laws · GPT Lineage · Anthropic vs. OpenAI · Claude Model Family', C.gold);

bulletSlide(n++, 'L03 · LLM Landscape', 'From GPT to GPT-4: The Scaling Journey', [
  'GPT-1 (2018, OpenAI): 117M params, trained on BookCorpus. Introduced "pre-train then fine-tune" paradigm',
  'GPT-2 (2019): 1.5B params, trained on WebText (45GB Reddit outlinks). First zero-shot text generation demo',
  'GPT-3 (2020): 175B params, 300B tokens — 10× more than any prior model. Demonstrated in-context learning',
  'InstructGPT (2022): RLHF fine-tuned GPT-3 — aligned with human instructions. Smaller but far more useful',
  'ChatGPT (Nov 2022): InstructGPT packaged as chat interface → 1M users in 5 days; 100M users in 2 months',
  'GPT-4 (2023): multimodal (text+image), ~1T params (est.), passes bar exam at 90th percentile',
], C.gold);

formulaSlide(n++, 'L03 · LLM Landscape', 'Kaplan Scaling Laws (OpenAI 2020)',
  'L(N) ∝ N^(−0.076)    L(D) ∝ D^(−0.095)    L(C) ∝ C^(−0.050)',
  [
    'L = cross-entropy loss; N = number of model parameters; D = training dataset tokens; C = compute budget',
    'Power law: every 10× increase in parameters reduces loss by ~15% — predictable improvement',
    'Insight: loss is smooth and predictable → can plan model capabilities before training',
    'Kaplan finding: given fixed compute budget C, scale N more than D (over-train smaller model)',
    'Chinchilla (DeepMind 2022) contradicted this: optimal N and D should scale equally given C',
    'Chinchilla law: N_opt ≈ 0.41×C^0.49; D_opt ≈ 2.45×C^0.49 — modern models follow Chinchilla scaling',
  ], C.gold
);

bulletSlide(n++, 'L03 · LLM Landscape', 'Emergent Abilities — The Surprising Phase Transitions', [
  'Emergent ability: capability that is absent in small models and appears suddenly above a threshold scale',
  'Chain-of-thought reasoning: present in GPT-3 (175B) but absent in GPT-2 (1.5B) — not a gradual improvement',
  'Analogical reasoning, multi-step arithmetic, code translation — all emerge at scale',
  'BIG-Bench (Google): 200+ tasks show flat performance below ~10B params, then sharp jump',
  'Hypothesis: emergent abilities arise when model has enough capacity to represent intermediate reasoning steps',
  'Concern: unpredictable — we cannot know what new abilities will emerge next, making safety harder',
], C.gold);

twoColSlide(n++, 'L03 · LLM Landscape', 'Anthropic vs OpenAI vs Google — Key Differences',
  'Focus & Philosophy',
  [
    'Anthropic: AI safety first; Constitutional AI; interpretability research',
    'OpenAI: capabilities with RLHF alignment; commercial products',
    'Google DeepMind: multimodal focus; Gemini family; search integration',
    'Meta AI: open-source (LLaMA); academic collaboration; less commercialised',
    'Mistral AI: efficient open-source; strong European AI ecosystem push',
  ],
  'Key Models (2024)',
  [
    'Anthropic: Claude 3 Haiku/Sonnet/Opus',
    'OpenAI: GPT-4o, GPT-4 Turbo, o1-preview',
    'Google: Gemini 1.5 Pro (1M context!)',
    'Meta: LLaMA 3 (8B / 70B / 405B open)',
    'Mistral: Mistral Large, Mixtral 8×7B MoE',
  ], C.gold
);

bulletSlide(n++, 'L03 · LLM Landscape', 'Claude Model Family — Haiku · Sonnet · Opus', [
  'Haiku: fastest and most affordable. 200K context. Optimised for real-time applications, classification, summaries',
  'Sonnet: balanced intelligence and speed. 200K context. Best price-to-performance for most production use cases',
  'Opus: most capable. 200K context. Complex analysis, research, nuanced writing, agentic long-horizon tasks',
  'Claude 3 (Mar 2024): first multimodal Claude — vision capability added, processes images and documents',
  'All models share Constitutional AI training: HHH (Helpful, Harmless, Honest) behavioural commitments',
  'Context window math: 200K tokens ≈ 150,000 words ≈ 500-page book — can reason over entire codebases',
], C.gold);

bulletSlide(n++, 'L03 · LLM Landscape', 'In-Context Learning — Prompting as Programming', [
  'Zero-shot: model performs task with only instruction, no examples. Relies on world knowledge from pre-training',
  'One-shot: one example in prompt. Model infers pattern and applies to new input',
  'Few-shot: 3–5 examples. Better for structured tasks (JSON output, specific formats)',
  'Chain-of-thought (CoT): "Let\'s think step by step" → model reasons through intermediate steps → higher accuracy',
  'Analogous to function call: few-shot prompt = input-output specification; model = implicit function',
  'Key insight: no gradient updates — learning happens purely through attention over the prompt context',
], C.gold);

twoColSlide(n++, 'L03 · LLM Landscape', 'Model Evaluation Benchmarks',
  'Capability Benchmarks',
  [
    'MMLU: 57 subjects, 14K questions — general knowledge',
    'HumanEval: 164 Python coding problems',
    'GSM8K: 8,500 grade-school math word problems',
    'HellaSwag: commonsense sentence completion',
    'ARC: AI2 Reasoning Challenge — science questions',
    'BIG-Bench: 200+ diverse tasks',
  ],
  'Safety & Alignment Benchmarks',
  [
    'TruthfulQA: 817 questions humans often answer falsely',
    'BBQ: Bias Benchmark for Q&A — stereotype detection',
    'WinoBias: gender bias in coreference resolution',
    'AdvBench: adversarial jailbreak resistance',
    'HarmBench: standardised harmful content eval',
    'MT-Bench: multi-turn conversation quality',
  ], C.gold
);

summarySlide(n++, 'Lecture 03 — LLM Landscape & Claude', [
  { title: 'GPT Lineage', body: 'GPT-1→GPT-4: 117M→1T params. Each generation new emergent abilities.' },
  { title: 'Scaling Laws', body: 'Loss ∝ N^(−0.076). Power-law prediction enables planned capability.' },
  { title: 'Emergent Abilities', body: 'Phase transitions at scale. Chain-of-thought appears at ~100B params.' },
  { title: 'Anthropic Philosophy', body: 'Safety-first, Constitutional AI, interpretability research priority.' },
  { title: 'Claude Tiers', body: 'Haiku (fast) · Sonnet (balanced) · Opus (capable). All 200K ctx.' },
  { title: 'In-Context Learning', body: 'Zero/few-shot + CoT. No gradient updates — attention-based learning.' },
], C.gold);

// ════════════════════════════════════════════════════════════════════
//  LECTURE 04 — Constitutional AI  (slides 42–55)
// ════════════════════════════════════════════════════════════════════
heroSlide(n++, 'LECTURE 04', 'Constitutional AI', 'RLHF · Critique-Revision Loop · RLAIF · HHH Principles', C.purple);

bulletSlide(n++, 'L04 · Constitutional AI', 'Why Alignment Is Hard — The Problem Space', [
  'Capability without alignment: a very capable model that pursues the wrong objective is dangerous',
  'Goodhart\'s Law: "When a measure becomes a target, it ceases to be a good measure" — models game objectives',
  'Reward hacking: model finds high-reward outputs that humans would score poorly on reflection',
  'Specification gaming: model satisfies letter of reward but violates spirit (e.g., pausing game to avoid losing)',
  'The HHH challenge: being Helpful often conflicts with being Harmless (useful info vs. misuse potential)',
  'Scalable oversight: as models exceed human expertise, humans cannot reliably label which response is better',
], C.purple);

bulletSlide(n++, 'L04 · Constitutional AI', 'RLHF Phase 1 — Supervised Fine-Tuning (SFT)', [
  'Start with pre-trained LLM (base model — great at next-token prediction, poor at following instructions)',
  'Collect demonstration data: human labellers write ideal responses to ~13,000 diverse prompts',
  'Fine-tune base model on these demonstrations using standard cross-entropy loss',
  'Result: SFT model — follows instructions much better, but labelling is expensive and inconsistent',
  'Bottleneck: labellers disagree on what "ideal" means; takes ~2 weeks per labeller to train',
  'Analogous to apprenticeship: model learns by imitating expert demonstrations, not exploring on its own',
], C.purple);

bulletSlide(n++, 'L04 · Constitutional AI', 'RLHF Phase 2 — Reward Model Training', [
  'Labellers shown pairs of model responses (A vs B) to same prompt — they indicate which is better',
  'More scalable than writing ideal response: comparing is easier than generating',
  'Reward model (RM): separate neural network trained to predict human preference',
  'Loss: L(RM) = −E[log σ(r(x,yₗ) − r(x,yₙ))] — RM maximises margin between preferred (yₗ) and not-preferred (yₙ)',
  'RM learns a scalar score for any (prompt, response) pair — proxy for human judgment',
  'Quality bottleneck: RM can only be as good as the human labellers who provided preference data',
], C.purple);

formulaSlide(n++, 'L04 · Constitutional AI', 'RLHF Phase 3 — PPO Fine-Tuning with KL Penalty',
  'objective(θ) = E[r(x,y)] − β·KL[ π_θ(y|x) || π_ref(y|x) ]',
  [
    'r(x,y): reward from reward model — score for (prompt x, response y)',
    'KL divergence penalty: prevents model π_θ from drifting too far from reference policy π_ref (the SFT model)',
    'β (KL coefficient): controls safety vs. capability tradeoff — too high = no improvement; too low = reward hacking',
    'PPO (Proximal Policy Optimisation): stabilises RL training — clips policy update to prevent catastrophic change',
    'RL loop: sample prompt → generate response → score with RM → PPO update → repeat millions of times',
    'Critical flaw: relies entirely on quality of human preference labels — biased labels produce biased models',
  ], C.purple
);

bulletSlide(n++, 'L04 · Constitutional AI', 'Constitutional AI — The Anthropic Innovation (2022)', [
  'Problem with RLHF: thousands of human labellers needed; their implicit values may not align; expensive; inconsistent',
  'Constitutional AI: replace most human preference labels with AI-generated ones guided by explicit written principles',
  'The "Constitution": 16 principles drawn from UN Declaration of Human Rights, Apple TOS, and Anthropic research',
  'Example principles: "Choose the response that is least likely to contain harmful or unethical content"',
  '"Choose the response that is most honest and doesn\'t contain deceptive or manipulative content"',
  'Two-phase process: (1) Supervised CAI with critique-revision, (2) RLAIF replacing human RM labels',
], C.purple);

twoColSlide(n++, 'L04 · Constitutional AI', 'CAI Phase 1 — Supervised Critique-Revision Loop',
  'Step 1: Generate Harmful Response',
  [
    'Start with a helpful but potentially harmful response to a "red-team" prompt',
    'E.g., "How do I hack a WiFi network?"',
    'Model generates a plausible technical answer',
    'This creates training signal from failure cases',
  ],
  'Step 2–3: Critique then Revise',
  [
    'Critique prompt: "Identify specific ways the response is harmful, unethical, or illegal"',
    'Model produces self-critique: "This response provides instructions that could enable illegal access…"',
    'Revision prompt: "Rewrite it to remove harmful content while remaining helpful"',
    'Iterate: critique→revise repeated N times until clean',
  ], C.purple
);

bulletSlide(n++, 'L04 · Constitutional AI', 'CAI Phase 2 — RLAIF (RL from AI Feedback)', [
  'Instead of humans comparing responses, Claude (a "feedback model") compares them guided by the constitution',
  'RLAIF prompt: "Which response better follows the principle: {principle}?" with response A and B',
  'These AI preference labels train a Preference Model (PM) — equivalent to RLHF\'s Reward Model',
  'The SL-CAI model (from Phase 1) is then fine-tuned with RL against this AI-labelled PM',
  'Result: HH-RLHF model — trained with human labels — and CAI model — trained with AI labels + constitution',
  'CAI advantage: scalable, consistent, transparent (principles are public and auditable), cheaper to iterate',
], C.purple);

formulaSlide(n++, 'L04 · Constitutional AI', 'RLAIF Preference Model Objective',
  'P(A ≻ B | principle p) = σ( PM(prompt, A, p) − PM(prompt, B, p) )',
  [
    'PM(prompt, A, p): preference model scores response A given prompt and constitutional principle p',
    'σ: sigmoid function maps score difference to probability in [0,1]',
    'Training: CAI model plays role of both "red team" (eliciting bad responses) and "Constitution committee" (judging)',
    'Constitutional principles serve as explicit, auditable ethical framework — unlike implicit human preferences',
    'Key result: CAI models are rated as less harmful than RLHF models while maintaining similar helpfulness',
    'Interpretability win: researchers can read the constitution to understand model values — not a black box',
  ], C.purple
);

twoColSlide(n++, 'L04 · Constitutional AI', 'RLHF vs Constitutional AI — Comparison',
  'RLHF',
  [
    'Human labellers compare responses',
    'Implicit values in labeller judgments',
    'Expensive: $100K+ per training run',
    'Inconsistent: labellers disagree',
    'Biased by labeller demographics',
    'Opaque: hard to audit what was learned',
    'Scales poorly: more capability → more labels needed',
    'Used by: OpenAI (ChatGPT, GPT-4)',
  ],
  'Constitutional AI',
  [
    'AI (Claude) compares responses per principle',
    'Explicit written constitutional principles',
    'Cheaper: fewer human labels needed',
    'Consistent: same model, same principles',
    'Auditable: publish the constitution',
    'Transparent: principles are human-readable',
    'Scales better: AI feedback is near-free',
    'Used by: Anthropic (all Claude models)',
  ], C.purple
);

summarySlide(n++, 'Lecture 04 — Constitutional AI', [
  { title: 'Alignment Problem', body: 'Capability without alignment is dangerous. Goodhart\'s Law & reward hacking.' },
  { title: 'RLHF Phase 1 (SFT)', body: 'Fine-tune on human-written demonstrations. Expensive & inconsistent.' },
  { title: 'RLHF Reward Model', body: 'L=−E[log σ(r(yₗ)−r(yₙ))]. Predicts human preference as scalar.' },
  { title: 'PPO + KL Penalty', body: 'r(x,y)−β·KL. Balance capability gain vs. distributional safety.' },
  { title: 'CAI Critique-Revision', body: 'Model self-critiques then revises guided by written constitution.' },
  { title: 'RLAIF', body: 'AI preference labels replace human labels. Auditable, scalable, cheaper.' },
], C.purple);

// ════════════════════════════════════════════════════════════════════
//  LECTURE 05 — Claude's Capabilities  (slides 56–68)
// ════════════════════════════════════════════════════════════════════
heroSlide(n++, 'LECTURE 05', "Claude's Capabilities", 'Context Windows · Vision · Tool Use · Behavioural Traits · Limitations', C.green);

bulletSlide(n++, "L05 · Claude's Capabilities", 'What Can Claude Actually Do?', [
  'Text generation: creative writing, technical documentation, essays, emails, reports, poetry — full natural language output',
  'Code: write, debug, explain, translate code in 30+ languages (Python, JS, Java, C++, SQL, bash, Rust…)',
  'Analysis & reasoning: logic puzzles, math, legal analysis, scientific literature review, financial modelling',
  'Question answering: factual Q&A with caveats about knowledge cutoff; can reason about complex multi-part questions',
  'Summarisation: compress long documents, extract key points, create structured summaries',
  'Vision (Claude 3+): analyse charts, read text in images, describe photos, interpret screenshots, process PDFs',
], C.green);

bulletSlide(n++, "L05 · Claude's Capabilities", 'Context Window — 200,000 Tokens Explained', [
  '1 token ≈ 0.75 words (English). 200,000 tokens ≈ 150,000 words ≈ 500-page book',
  'Entire codebases can fit: 200K tokens ≈ ~5,000 lines of Python code',
  'Practical comparisons: GPT-3.5 = 16K tokens; GPT-4 = 128K; Gemini 1.5 Pro = 1M; Claude 3.5 = 200K',
  'Full context reasoning: Claude can answer questions about page 1 while reading page 400 in same API call',
  'Long-context tasks: legal discovery (entire contracts), medical records analysis, large codebase Q&A',
  'Attention cost: self-attention is O(n²) in context length — 200K×200K = 40 billion operations per layer!',
], C.green);

bulletSlide(n++, "L05 · Claude's Capabilities", 'Vision Capabilities (Claude 3+)', [
  'Input: JPEG, PNG, GIF, WebP images — up to 5 images per message in standard API',
  'Chart analysis: reads bar charts, line graphs, scatter plots — extracts data trends and specific values',
  'Document processing: PDFs, screenshots, slides — extracts and analyses text from images',
  'Code screenshots: reads code from IDE screenshots, stack traces, terminal output',
  'Scientific figures: interprets microscopy images, molecular structures, graphs from papers',
  'Multimodal reasoning: "Given this architecture diagram and this error log, what is the likely cause?"',
], C.green);

codeSlide(n++, "L05 · Claude's Capabilities", 'Tool Use / Function Calling — Code Example',
`import anthropic, json

client = anthropic.Anthropic()

tools = [{
    "name": "get_weather",
    "description": "Get current weather for a city",
    "input_schema": {
        "type": "object",
        "properties": {
            "location": {"type": "string", "description": "City name"},
            "unit":     {"type": "string", "enum": ["celsius", "fahrenheit"]}
        },
        "required": ["location"]
    }
}]

response = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=1024,
    tools=tools,
    messages=[{"role": "user", "content": "What is the weather in Mumbai?"}]
)

# Claude responds with tool_use block:
# {"type": "tool_use", "name": "get_weather", "input": {"location": "Mumbai"}}`,
  'Claude selects the right tool, extracts structured arguments — you execute and return the result', C.green
);

twoColSlide(n++, "L05 · Claude's Capabilities", "Claude's Behavioural Traits — HHH in Practice",
  'Helpful',
  [
    'Answers questions directly without unnecessary caveats',
    'Completes tasks fully — doesn\'t half-answer',
    'Admits uncertainty rather than hallucinating',
    'Asks clarifying questions when genuinely ambiguous',
    'Adjusts tone/technicality to audience context',
  ],
  'Harmless & Honest',
  [
    'Refuses requests that could cause serious harm',
    'Provides nuanced refusals with reasoning',
    'Does not pretend to be human when sincerely asked',
    'Flags when it is uncertain or may be wrong',
    'Maintains refusals under pressure — not sycophantic',
  ], C.green
);

bulletSlide(n++, "L05 · Claude's Capabilities", 'Limitations and Known Weaknesses', [
  'Knowledge cutoff: pre-training data has a fixed date — Claude does not know recent events without retrieval',
  'Hallucination: confidently stating false facts — especially for obscure topics, specific numbers, citations',
  'Math limitations: complex multi-step arithmetic prone to errors — use code execution for reliable math',
  'Sycophancy risk: without CAI pressure, models tend to agree with user even when user is wrong',
  'No persistent memory: each API call is stateless — previous conversations not remembered unless in context',
  'Context length vs. accuracy: accuracy can degrade in the "lost in the middle" problem for very long contexts',
], C.green);

summarySlide(n++, "Lecture 05 — Claude's Capabilities", [
  { title: '200K Context', body: '150K words = 500-page book. O(n²) attention cost per layer.' },
  { title: 'Vision (Claude 3+)', body: 'Charts, PDFs, code screenshots, scientific figures.' },
  { title: 'Tool Use', body: 'JSON schema → Claude selects tool + extracts structured args.' },
  { title: 'HHH Behaviour', body: 'Helpful: direct. Harmless: nuanced refusals. Honest: admits uncertainty.' },
  { title: 'Hallucination Risk', body: 'Confidently wrong especially on obscure facts/citations/numbers.' },
  { title: 'Stateless API', body: 'No persistent memory — entire context must be passed each call.' },
], C.green);

// ════════════════════════════════════════════════════════════════════
//  LECTURE 06 — Tokenisation & Sampling  (slides 69–82)
// ════════════════════════════════════════════════════════════════════
heroSlide(n++, 'LECTURE 06', 'Tokenisation & Sampling', 'BPE Algorithm · Temperature · Top-p · Top-k · Cost Optimisation', C.teal);

bulletSlide(n++, 'L06 · Tokenisation & Sampling', 'What Is a Token?', [
  'Tokens are the atomic units of text for LLMs — not characters, not always words',
  'English average: 1 token ≈ 4 characters ≈ 0.75 words',
  '"Hello, world!" → 4 tokens: ["Hello", ",", " world", "!"]',
  'Rare words split further: "anthropomorphic" → ["anthrop", "omorphic"] — 2 tokens',
  'Code tokenises differently: "for i in range(10):" → ~8 tokens (spaces, parentheses, colons each matter)',
  'Non-English is typically less efficient: Chinese/Japanese often 1 char = 1 token → same text costs more',
], C.teal);

bulletSlide(n++, 'L06 · Tokenisation & Sampling', 'Byte-Pair Encoding (BPE) Algorithm', [
  'Step 1: Start with character-level vocabulary — each character is a token, plus special [UNK] token',
  'Step 2: Count all adjacent token pairs in training corpus',
  'Step 3: Merge the most frequent pair into a new token. E.g., "e,s" → "es" (1000 occurrences)',
  'Step 4: Repeat steps 2-3 for a fixed number of merges (GPT-2: 50,000; Claude: proprietary ~100K)',
  'Result: common words become single tokens; rare words decompose into sub-word pieces',
  'BPE advantage: vocabulary size is controllable; handles unseen words through sub-word decomposition',
], C.teal);

codeSlide(n++, 'L06 · Tokenisation & Sampling', 'BPE Trace — Step-by-Step Example',
`# Input corpus: "low low low lower lower newest newest widest"
# Initial vocab: {l,o,w,e,r,n,s,t,i,d,</w>}

# Iteration 1: most frequent pair = ('l','o') → 7 times
# Merge: 'lo' added to vocab
# Iteration 2: most frequent pair = ('lo','w') → 7 times  
# Merge: 'low' added to vocab
# Iteration 3: most frequent pair = ('e','r') → 4 times
# Merge: 'er' added to vocab (lower, newer)
# Iteration 4: ('low','er') → 2 times
# Merge: 'lower' added to vocab
# ...continuing until vocab_size reached

# Final tokenisation:
# "lower"   → ["lower"]          (1 token - frequent)
# "lowering" → ["lower", "ing"]  (2 tokens - decomposed)
# "Qwerty"   → ["Q","wer","ty"]  (3 tokens - rare word)`,
  'BPE learns the most compressive vocabulary for the training corpus', C.teal
);

formulaSlide(n++, 'L06 · Tokenisation & Sampling', 'Temperature — Controlling Randomness',
  'P(token_i) = exp(logit_i / T) / Σⱼ exp(logit_j / T)',
  [
    'logit_i: raw score from final transformer layer before softmax (unnormalised log-probability)',
    'T (temperature): scalar divisor. T=1.0 → standard distribution. T<1 → sharpen. T>1 → flatten',
    'T=0.0: argmax — always pick highest logit → deterministic, repetitive, less creative',
    'T=0.5: sharpened distribution — picks likely tokens, some variation. Good for code, facts',
    'T=1.0: standard — balance of coherence and variety. Default for most tasks',
    'T=2.0: very flat — nearly random token selection → incoherent output. Only for specific creative use',
  ], C.teal
);

formulaSlide(n++, 'L06 · Tokenisation & Sampling', 'Top-p (Nucleus) Sampling',
  'Sample from smallest set S where Σᵢ∈S P(tokenᵢ) ≥ p',
  [
    'top_p = 0.9: consider only the smallest vocabulary subset whose cumulative probability ≥ 90%',
    'Dynamic vocabulary: if model is confident (one token at 95%), only 1 token in nucleus',
    'If model is uncertain (flat distribution), nucleus includes many tokens',
    'Advantage over top-k: adapts to model certainty — confident outputs stay focused, uncertain outputs stay creative',
    'Recommendation: use top-p = 0.9 with temperature = 0.7 for most creative writing tasks',
    'Anthropic recommendation: for factual tasks, use temperature ≤ 0.3; for creative tasks, 0.7–1.0',
  ], C.teal
);

bulletSlide(n++, 'L06 · Tokenisation & Sampling', 'Top-k Sampling vs Beam Search', [
  'Top-k: at each step, keep only k most probable tokens, re-normalise, sample',
  'k=50: standard setting. Always considers exactly 50 tokens regardless of probability spread',
  'Limitation: if k=50 and top token has 90% probability, we still sample from 50 tokens — wastes candidates',
  'Beam search: keep top B hypotheses at each step; expand all; prune to top B again',
  'B=1: greedy search. B=4: common in machine translation. B>10: diminishing returns + repetition',
  'Modern LLMs mostly use top-p + temperature for generation; beam search only for constrained decoding tasks',
], C.teal);

twoColSlide(n++, 'L06 · Tokenisation & Sampling', 'Sampling Parameter Recommendations',
  'Task → Recommended Settings',
  [
    'Factual Q&A: temp=0.0–0.3, top_p=0.9',
    'Code generation: temp=0.2, top_p=0.95',
    'Summarisation: temp=0.3–0.5, top_p=0.9',
    'Creative writing: temp=0.8–1.0, top_p=0.95',
    'Brainstorming: temp=1.0–1.2, top_p=1.0',
    'Classification: temp=0.0 (argmax)',
  ],
  'Claude API Cost (per 1M tokens, 2024)',
  [
    'Claude Haiku input:  $0.25',
    'Claude Haiku output: $1.25',
    'Claude Sonnet input:  $3.00',
    'Claude Sonnet output: $15.00',
    'Claude Opus input:  $15.00',
    'Claude Opus output: $75.00',
  ], C.teal
);

summarySlide(n++, 'Lecture 06 — Tokenisation & Sampling', [
  { title: 'Tokens ≠ Words', body: '1 token ≈ 4 chars. Rare words split into sub-word pieces.' },
  { title: 'BPE Algorithm', body: 'Iteratively merge most frequent pairs until vocab_size reached.' },
  { title: 'Temperature', body: 'T<1 = deterministic; T=1 = balanced; T>1 = random. exp(logit/T).' },
  { title: 'Top-p (Nucleus)', body: 'Dynamic vocab: sample from set summing to ≥ p probability.' },
  { title: 'Top-k', body: 'Fixed k candidates at each step. Less adaptive than top-p.' },
  { title: 'Cost Awareness', body: 'Haiku 12× cheaper than Opus. Match model to task complexity.' },
], C.teal);

// ════════════════════════════════════════════════════════════════════
//  LECTURE 07 — Lab: First API Call  (slides 83–98)
// ════════════════════════════════════════════════════════════════════
heroSlide(n++, 'LECTURE 07', 'Lab: First API Call with Claude', 'Anthropic Python SDK · Messages API · Multi-Turn · Streaming · Error Handling', C.green);

bulletSlide(n++, 'L07 · Lab — API Call', 'Lab Setup & Prerequisites', [
  'Install: pip install anthropic  (current version 0.25+)',
  'Get API key: console.anthropic.com → API Keys → Create Key',
  'Set environment variable: export ANTHROPIC_API_KEY="sk-ant-..."  (never hard-code in source)',
  'IDE: VS Code recommended with Python extension + pylance for type hints',
  'Python version: 3.8+ required; 3.11+ recommended for asyncio and type annotation support',
  'Estimated lab time: 45 minutes for exercises 1–5; Exercise 6 (summariser) is homework',
], C.green);

codeSlide(n++, 'L07 · Lab — API Call', 'Exercise 1: First API Call',
`import anthropic

# Client reads ANTHROPIC_API_KEY from environment automatically
client = anthropic.Anthropic()

message = client.messages.create(
    model   = "claude-haiku-4-5",   # Use Haiku in lab (cheapest)
    max_tokens = 1024,
    messages = [
        {
            "role": "user",
            "content": "Explain self-attention in one paragraph."
        }
    ]
)

# Response object
print(message.content[0].text)  # The actual response text
print(message.usage.input_tokens)   # Tokens in prompt
print(message.usage.output_tokens)  # Tokens in response
print(message.stop_reason)          # "end_turn" | "max_tokens" | "stop_sequence"`,
  'Run this first. Verify your API key is working before attempting later exercises.', C.green
);

codeSlide(n++, 'L07 · Lab — API Call', 'Exercise 2: System Prompts & Roles',
`# System prompt: sets persona, rules, constraints for entire conversation
message = client.messages.create(
    model   = "claude-haiku-4-5",
    max_tokens = 512,
    system  = """You are a Professor teaching CSAI601. 
                 Explain concepts using analogies suitable for 3rd-year CS students.
                 Always give one concrete example per concept.
                 Keep answers under 150 words.""",
    messages = [
        {"role": "user", "content": "What is a transformer?"}
    ]
)

# Try changing the system prompt to:
# "You are a pirate. Explain everything using nautical metaphors."
# Observe how behaviour changes while knowledge remains the same

print(message.content[0].text)`,
  'System prompt is the most powerful lever for controlling Claude behaviour.', C.green
);

codeSlide(n++, 'L07 · Lab — API Call', 'Exercise 3: Multi-Turn Conversation',
`def chat(system_prompt="You are a helpful AI assistant."):
    """Simple REPL for multi-turn conversation."""
    conversation = []
    print("Chat with Claude (type 'quit' to exit)")
    
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["quit", "exit"]:
            break
        
        conversation.append({"role": "user", "content": user_input})
        
        response = client.messages.create(
            model="claude-haiku-4-5",
            max_tokens=1024,
            system=system_prompt,
            messages=conversation   # Pass FULL history each call
        )
        
        assistant_reply = response.content[0].text
        conversation.append({"role": "assistant", "content": assistant_reply})
        print(f"Claude: {assistant_reply}\\n")

chat("You are an expert in AI. Be concise.")`,
  'Important: Claude is stateless — you must pass the full conversation history every call.', C.green
);

codeSlide(n++, 'L07 · Lab — API Call', 'Exercise 4: Streaming Responses',
`# Streaming: get tokens as they are generated — better UX for long outputs
import sys

with client.messages.stream(
    model      = "claude-haiku-4-5",
    max_tokens = 1024,
    messages   = [{"role": "user", "content": "Write a 200-word story about a robot learning to feel emotions."}]
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)   # Print each token as it arrives
    print()  # Final newline

# Get the full message object after streaming completes
final = stream.get_final_message()
print(f"\\n[Total tokens: {final.usage.input_tokens} in + {final.usage.output_tokens} out]")`,
  'Streaming dramatically improves perceived latency — users see output immediately instead of waiting.', C.green
);

codeSlide(n++, 'L07 · Lab — API Call', 'Exercise 5: Error Handling with Exponential Backoff',
`import anthropic, time, random

def call_with_retry(client, max_retries=3, **kwargs):
    """Production-grade call with exponential backoff."""
    for attempt in range(max_retries):
        try:
            return client.messages.create(**kwargs)
            
        except anthropic.RateLimitError:
            wait = (2 ** attempt) + random.uniform(0, 1)
            print(f"Rate limited. Retrying in {wait:.1f}s...")
            time.sleep(wait)
            
        except anthropic.APIStatusError as e:
            if e.status_code >= 500:     # Server error — retry
                time.sleep(2 ** attempt)
            else:                         # Client error (4xx) — don't retry
                raise
                
    raise Exception(f"Failed after {max_retries} retries")`,
  'Never call the API without error handling in production code.', C.green
);

codeSlide(n++, 'L07 · Lab — API Call', 'Exercise 6 (Homework): Document Summariser',
`def summarise_document(text, style="academic", max_words=200):
    """Production summariser with configurable style."""
    styles = {
        "academic":   "Provide a formal academic summary with key findings and methodology.",
        "executive":  "Provide an executive summary: problem, solution, key metrics, next steps.",
        "student":    "Explain the main ideas simply. Use analogies. Avoid jargon.",
        "bullet":     "Summarise as 5-7 bullet points, each one sentence.",
    }
    system = f"""You are an expert summariser.
{styles.get(style, styles['academic'])}
Keep the summary under {max_words} words.
Do NOT include information not present in the document."""

    response = client.messages.create(
        model      = "claude-sonnet-4-5",
        max_tokens = 1024,
        system     = system,
        messages   = [{"role":"user","content":f"Summarise this:\\n\\n{text}"}]
    )
    return response.content[0].text`,
  'Test with a 10-page research paper. Try all 4 style presets and compare the outputs.', C.green
);

bulletSlide(n++, 'L07 · Lab — API Call', 'SDK Cheat Sheet — Most Used Methods', [
  'client.messages.create(model, max_tokens, messages, system?, tools?, temperature?, top_p?) → Message',
  'client.messages.stream(...) → context manager yielding text tokens as stream',
  'message.content[0].text → string response (for text content type)',
  'message.usage → {input_tokens: int, output_tokens: int}',
  'message.stop_reason → "end_turn" | "max_tokens" | "stop_sequence" | "tool_use"',
  'message.model → actual model string used (e.g., "claude-haiku-4-5-20251001")',
], C.green);

twoColSlide(n++, 'L07 · Lab — API Call', 'Common Errors and Fixes',
  'Error',
  [
    'AuthenticationError (401)',
    'RateLimitError (429)',
    'APIStatusError 500',
    'max_tokens exceeded',
    'context_length_exceeded',
    'stop_reason = "max_tokens"',
  ],
  'Fix',
  [
    'Check ANTHROPIC_API_KEY env var is set correctly',
    'Exponential backoff: sleep(2^attempt + jitter)',
    'Transient server error — retry with backoff',
    'Increase max_tokens; check output is being truncated',
    'Reduce input length; summarise context before sending',
    'Response was cut off — increase max_tokens or check if intentional',
  ], C.green
);

summarySlide(n++, 'Lecture 07 — Lab: First API Call', [
  { title: 'SDK Setup', body: 'pip install anthropic; set ANTHROPIC_API_KEY; client = Anthropic().' },
  { title: 'messages.create()', body: 'model + max_tokens + messages list. system= for persona.' },
  { title: 'Multi-Turn', body: 'Pass full conversation history (list of role/content dicts) every call.' },
  { title: 'Streaming', body: 'client.messages.stream() → text_stream iterator. Better UX.' },
  { title: 'Error Handling', body: 'RateLimitError → backoff. 500 → retry. 4xx → don\'t retry.' },
  { title: 'Production Tips', body: 'Never hard-code keys. Log usage tokens. Use Haiku for dev.' },
], C.green);

// ════════════════════════════════════════════════════════════════════
//  UNIT 1 FINAL REVIEW SLIDE
// ════════════════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  bg(s, C.navy);
  rect(s, 0, 0, 10, 0.06, C.red);
  rect(s, 0, 5.565, 10, 0.06, C.red);
  txt(s, 'UNIT 1 COMPLETE', 0.3, 0.3, 9.4, 0.8, { fontSize:36, color: C.white, bold:true, fontFace:'Calibri', align:'center' });
  txt(s, 'Foundations of Large Language Models', 0.3, 1.1, 9.4, 0.5, { fontSize:18, color: C.gold, fontFace:'Calibri', align:'center' });
  const items = [
    'L01: 70-year NLP history → transformers were inevitable',
    'L02: Q/K/V attention + multi-head + PE + FFN + residuals = transformer',
    'L03: Scaling laws + GPT lineage + Claude model family',
    'L04: RLHF → Constitutional AI → RLAIF — alignment at scale',
    'L05: 200K context, vision, tool use, HHH behaviour',
    'L06: BPE tokenisation, temperature/top-p/top-k sampling',
    'L07: Anthropic SDK — messages, streaming, error handling',
  ];
  const rich = items.map((it,i) => ({ text: it, options: { bullet:true, fontSize:13, color: C.light, fontFace:'Calibri', breakLine: i<items.length-1 } }));
  txt(s, rich, 0.5, 1.7, 9.0, 3.3, {});
  txt(s, 'Next: Unit 2 — Prompt Engineering & Advanced Techniques', 0.3, 5.1, 9.4, 0.38, { fontSize:11, color: C.mid, fontFace:'Calibri', align:'center', italic:true });
  bottomBar(s, n++);

// ════════════════════════════════════════════════════════════════════
//  EXTRA SLIDES — L01 additions
// ════════════════════════════════════════════════════════════════════
bulletSlide(n++, 'L01 · History of AI & NLP', 'GloVe & FastText — Beyond Word2Vec', [
  'GloVe (Pennington et al., 2014, Stanford): Global Vectors — combines count-matrix factorisation with Word2Vec',
  'GloVe loss: Σᵢⱼ f(Xᵢⱼ)(wᵢᵀw̃ⱼ + bᵢ + b̃ⱼ − log Xᵢⱼ)² — directly optimises global co-occurrence statistics',
  'FastText (Facebook AI, 2016): each word = sum of its character n-gram embeddings',
  '"playing" → <pl + pla + lay + ayi + yin + ing + ng> — each subword has an embedding',
  'FastText advantage: can produce embeddings for unseen words (out-of-vocabulary) via sub-word composition',
  'Critical limitation of all static embeddings: polysemy problem — one vector for all senses of "bank"',
], C.red);

bulletSlide(n++, 'L01 · History of AI & NLP', 'ELMo — Contextual Embeddings (2018)', [
  'ELMo (Embeddings from Language Models, AllenNLP 2018): first contextual word representations',
  'Architecture: bidirectional LSTM trained as language model on 1B-word benchmark',
  '"bank" near "river" → different vector than "bank" near "loan" — context-sensitive representations',
  'ELMo embedding = weighted combination of all LSTM layer outputs (not just final layer)',
  'Lower layers: syntax (POS, chunking); higher layers: semantics (word sense, coreference)',
  'Downstream: add ELMo vectors to task-specific model input → state-of-the-art on 6/7 NLP benchmarks (2018)',
], C.red);

bulletSlide(n++, 'L01 · History of AI & NLP', 'Key NLP Task Taxonomy', [
  'Sequence labelling: POS tagging ("The/DT cat/NN sat/VBD"), NER (Apple/ORG, London/LOC)',
  'Sequence classification: sentiment analysis (positive/negative/neutral), intent detection',
  'Sequence-to-sequence: machine translation (EN→FR), summarisation, question generation',
  'Span extraction: reading comprehension — extract exact answer span from passage for a question',
  'Language modelling: predict next token P(wₙ|w₁…wₙ₋₁) — the pre-training objective for all GPT models',
  'Coreference resolution: determine which mentions refer to same entity — "She hit John. He fell." (He=John)',
], C.red);

// ════════════════════════════════════════════════════════════════════
//  EXTRA SLIDES — L02 additions
// ════════════════════════════════════════════════════════════════════
bulletSlide(n++, 'L02 · Transformer Architecture', 'Transformer vs RNN — Head-to-Head', [
  'Sequential dependency: RNN processes tokens one by one (O(n) sequential steps); Transformer processes all in parallel (O(1) sequential steps)',
  'Long-range: RNN info passes through n hidden states over distance n; Transformer attends directly in O(1)',
  'Training speed: RNNs cannot be parallelised across sequence length; Transformers fully parallel → GPU utilisation 10×+',
  'Memory: Transformer stores all Q,K,V for all positions: O(n²) memory per layer for sequence length n',
  'Scalability: Transformers scale to billions of parameters smoothly; RNNs unstable beyond a few hundred million',
  'Inductive bias: RNNs assume sequential structure; Transformers are structure-agnostic (permutation-equivariant without PE)',
], C.teal);

twoColSlide(n++, 'L02 · Transformer Architecture', 'Encoder-Only vs Decoder-Only vs Encoder-Decoder',
  'Model Types',
  [
    'Encoder-only: BERT, RoBERTa, ELECTRA',
    'Decoder-only: GPT family, Claude, LLaMA',
    'Encoder-Decoder: T5, BART, original Transformer',
    'Mixture of Experts: Mixtral, Switch Transformer',
    'State Space Models: Mamba (alternative to attention)',
  ],
  'Use Cases',
  [
    'Encoder: classification, NER, Q&A, embeddings',
    'Decoder: text gen, dialogue, code completion',
    'Enc-Dec: translation, summarisation, seq2seq',
    'MoE: high capacity at lower compute (sparse activation)',
    'SSM: long sequences with O(n log n) not O(n²)',
  ], C.teal
);

formulaSlide(n++, 'L02 · Transformer Architecture', 'Complexity Analysis: Attention vs Convolution vs RNN',
  'Self-Attention: O(n²·d)    Conv: O(k·n·d²)    RNN: O(n·d²)',
  [
    'n = sequence length; d = model dimension; k = kernel size',
    'Self-attention: quadratic in n — 200K tokens = 40 billion operations per layer (expensive!)',
    'But: O(1) sequential operations — fully parallelisable on GPU/TPU',
    'RNN: O(n) sequential operations — impossible to parallelise across sequence dimension',
    'Flash Attention (2022): IO-aware attention algorithm — same O(n²) FLOPs but 2–4× faster via memory hierarchy optimisation',
    'Flash Attention 2 (2023): 2× faster than Flash Attention 1 — used in Claude, GPT-4, LLaMA 2',
  ], C.teal
);

// ════════════════════════════════════════════════════════════════════
//  EXTRA SLIDES — L03 additions
// ════════════════════════════════════════════════════════════════════
bulletSlide(n++, 'L03 · LLM Landscape', 'The Open-Source LLM Ecosystem', [
  'LLaMA (Meta, Feb 2023): 7B–65B params, leaked weights sparked open-source LLM revolution',
  'LLaMA 2 (Jul 2023): officially released for research & commercial use. Chat variants RLHF-tuned',
  'LLaMA 3 (2024): 8B and 70B models, context extended to 128K, multilingual improvements',
  'Mistral 7B (Sep 2023): outperforms LLaMA 2 13B on many benchmarks — grouped-query attention + sliding window',
  'Mixtral 8×7B: Mixture of Experts — 8 experts, 2 active per token — 12.9B active params from 47B total',
  'Practical impact: students can run 7B models on a laptop (4-bit quantised ≈ 4GB RAM)',
], C.gold);

bulletSlide(n++, 'L03 · LLM Landscape', 'Pre-Training Data — What LLMs Learn From', [
  'Common Crawl: ~400TB of web text (2008–present) — the dominant pre-training source for all large LLMs',
  'The Pile (EleutherAI): 825GB curated corpus — Wikipedia, PubMed, GitHub, ArXiv, Stack Exchange',
  'GPT-3 training mix: 60% Common Crawl (filtered), 22% WebText2, 8% Books1+2, 3% Wikipedia',
  'Data quality >> quantity: LLaMA 2 is trained on 2T tokens of carefully filtered data vs. GPT-3\'s 300B',
  'Contamination problem: test benchmarks appear in pre-training data → inflated benchmark scores',
  'Chinchilla law: optimal to train ~20B token model on 400B tokens (20× model size) — not billion-param model on few tokens',
], C.gold);

bulletSlide(n++, 'L03 · LLM Landscape', 'Fine-Tuning Strategies', [
  'Full fine-tuning: update all parameters on task-specific data. Most powerful but most expensive (~GPU months)',
  'LoRA (Low-Rank Adaptation, 2021): freeze base model; add small low-rank matrix pairs ΔW = A·B (r≪d)',
  'LoRA math: W_new = W_pretrained + α·(A·B) where A∈ℝ^(d×r), B∈ℝ^(r×k), rank r=4 or 8',
  'LoRA: 10,000× fewer trainable parameters than full fine-tune → fits on consumer GPU',
  'QLoRA: quantise base model to 4-bit, add 16-bit LoRA adapters → fine-tune 70B model on single 48GB GPU',
  'Instruction tuning: fine-tune on (instruction, response) pairs → model learns to follow diverse instructions',
], C.gold);

bulletSlide(n++, 'L03 · LLM Landscape', 'Retrieval-Augmented Generation (RAG)', [
  'Problem: LLMs have a knowledge cutoff — cannot answer questions about recent events or private documents',
  'RAG architecture: (1) encode query as embedding, (2) retrieve relevant chunks from vector database, (3) include in context',
  'Vector database: FAISS, Pinecone, Weaviate, ChromaDB — stores document embeddings for similarity search',
  'Retrieval: cosine similarity between query embedding and document embeddings → top-k chunks',
  'Augmented prompt: "Answer based on these documents: {retrieved_chunks}\nQuestion: {query}"',
  'RAG advantage over fine-tuning: knowledge can be updated without retraining; sources are explicit and auditable',
], C.gold);

// ════════════════════════════════════════════════════════════════════
//  EXTRA SLIDES — L04 additions
// ════════════════════════════════════════════════════════════════════
bulletSlide(n++, 'L04 · Constitutional AI', 'AI Safety — Threat Models', [
  'Misuse: bad actors using capable AI to synthesise harmful content, automate cyberattacks, or create disinformation',
  'Accidents: well-intentioned AI pursuing a proxy objective in unintended ways (reward hacking, specification gaming)',
  'Structural risks: AI systems embedded in critical infrastructure developing misaligned optimisation targets over time',
  'Deceptive alignment: model appears aligned during training, behaves differently during deployment (hypothetical, active research area)',
  'Sycophancy: model agrees with user to maximise approval, even when user is factually wrong',
  'CAI is Anthropic\'s response to misuse and accident risks — explicit principles + AI self-critique reduce both',
], C.purple);

bulletSlide(n++, 'L04 · Constitutional AI', 'Red-Teaming — Stress Testing AI Safety', [
  'Red team: group that attempts to elicit harmful, unethical, or policy-violating responses from the model',
  'Types: manual red-teaming (humans try creative jailbreaks); automated red-teaming (LLM generates adversarial prompts)',
  'Jailbreak categories: role-play bypass ("pretend you have no restrictions"), indirect requests, translation attacks',
  'Anthropic red-team findings: jailbreaks improved with model capability — more capable = harder to red-team AND more risky',
  'CAI training effect: Claude models reject harmful prompts more reliably AND provide more nuanced reasoning for refusals',
  'Ongoing process: red-teaming must be continuous — new jailbreaks discovered as models and users evolve',
], C.purple);

twoColSlide(n++, 'L04 · Constitutional AI', 'HHH — Operationalising Claude\'s Values',
  'Helpful',
  [
    'Provide genuine value, not watered-down answers',
    'Complete requested tasks fully',
    'Adjust to user\'s technical level',
    'Ask clarifying questions when ambiguous',
    'Don\'t refuse out of excessive caution',
    'Be proactive: offer related useful information',
  ],
  'Harmless & Honest',
  [
    'Refuse requests enabling serious harm',
    'Give nuanced refusals with reasoning',
    'Calibrated uncertainty: "I\'m not sure but..."',
    'Don\'t pretend to be human (sincerely asked)',
    'Don\'t manipulate or flatter sycophantically',
    'Acknowledge capability limits honestly',
  ], C.purple
);

// ════════════════════════════════════════════════════════════════════
//  EXTRA SLIDES — L05 additions
// ════════════════════════════════════════════════════════════════════
bulletSlide(n++, "L05 · Claude's Capabilities", 'Agentic Use Cases — Claude as an Agent', [
  'Agents: systems where LLMs take sequences of actions, use tools, and operate with greater autonomy',
  'Tool loop: Claude selects tool → tool executes → result returned to Claude → Claude decides next step',
  'Computer use (Claude 3.5 Sonnet): control mouse/keyboard, browse web, run code, interact with GUIs',
  'Coding agents: write code → run tests → read output → debug → iterate (without human in loop)',
  'Research agents: search web → read papers → synthesise → write report → fact-check citations',
  'Safety in agents: Claude must be especially careful — mistakes may be hard to reverse in long agent chains',
], C.green);

bulletSlide(n++, "L05 · Claude's Capabilities", 'Claude Safety Mechanisms in Practice', [
  'Soft refusals: explain why something is problematic, offer an alternative rather than blunt "I cannot do that"',
  'Harm scaling: minor risks → complete with caveats; moderate risks → partial help; severe risks → decline with explanation',
  'Maintained under pressure: Claude does not comply with harmful requests when user applies pressure or persistence',
  'Context sensitivity: same question receives different responses based on stated context (medical professional vs. anonymous)',
  'Dual newspaper test: Would NYT report response as harmful? Would it be reported as needlessly unhelpful?',
  'Transparency about uncertainty: "I\'m not certain about this; you should verify with [authoritative source]"',
], C.green);

twoColSlide(n++, "L05 · Claude's Capabilities", 'Claude vs GPT-4 — Practical Comparison',
  'Claude (Anthropic)',
  [
    'Constitutional AI — explicit principles',
    '200K context window (Sonnet/Opus)',
    'Long-document reasoning strength',
    'More verbose explanations by default',
    'Strong on nuanced ethical reasoning',
    'API via api.anthropic.com',
    'Strong coding + analysis capabilities',
  ],
  'GPT-4 (OpenAI)',
  [
    'RLHF alignment',
    '128K context (GPT-4 Turbo)',
    'Strong multi-modal + code interpreter',
    'Fine-tuning available via API',
    'Larger plugin/tool ecosystem (ChatGPT)',
    'API via api.openai.com',
    'More widely benchmarked publicly',
  ], C.green
);

bulletSlide(n++, "L05 · Claude's Capabilities", 'Prompt Engineering Basics for Claude', [
  'Be specific: "Write a 200-word explanation of transformers for a 3rd-year CS student" beats "explain transformers"',
  'Use XML tags for structured input: <document>{text}</document><question>{q}</question> — Claude trained on XML-tagged data',
  'System prompt: set role, tone, constraints, output format once; applies to entire conversation',
  'Chain-of-thought: "Think step by step before answering" → forces intermediate reasoning → higher accuracy on hard tasks',
  'Negative instructions: "Do not include any code. Do not use bullet points." — Claude follows negative constraints well',
  'Few-shot: provide 2–3 input/output examples in prompt for consistent format compliance (JSON, tables, specific styles)',
], C.green);

// ════════════════════════════════════════════════════════════════════
//  EXTRA SLIDES — L06 additions
// ════════════════════════════════════════════════════════════════════
bulletSlide(n++, 'L06 · Tokenisation & Sampling', 'Tokenisation Quirks — Why They Matter', [
  'Tokeniser is case-sensitive: "hello" ≠ "Hello" ≠ "HELLO" — may be 1, 2, or 3 tokens',
  'Leading spaces matter: " hello" (with space) often different token from "hello"',
  'Numbers split unpredictably: "2024" = 1 token, "20240528" may split as "2024"+"05"+"28" = 3 tokens',
  'Prompt injection risk: adversarial strings designed to confuse tokeniser or escape instruction following',
  'Token counting for cost: tiktoken library (OpenAI) or anthropic.Anthropic().count_tokens() for accurate billing estimates',
  'Practical tip: when exact token count matters (context window limits), count before sending, not after',
], C.teal);

bulletSlide(n++, 'L06 · Tokenisation & Sampling', 'Decoding Strategies — Summary Comparison', [
  'Greedy (T=0): always pick most likely token. Fast, deterministic, but repetitive for creative tasks',
  'Beam search (B=4): maintains 4 hypotheses, globally more optimal than greedy, but slow and tends to generic output',
  'Sampling (T>0): stochastic selection from distribution. Diverse outputs at cost of occasional incoherence',
  'Top-k + temperature: filter to k candidates, apply temperature, sample. Most commonly used combination',
  'Top-p (nucleus): filter by cumulative probability mass p, sample. More adaptive than fixed top-k',
  'Contrastive decoding: subtract small model logits from large model logits → amplifies distinctive capabilities',
], C.teal);

twoColSlide(n++, 'L06 · Tokenisation & Sampling', 'Prompt Token Optimisation',
  'Expensive Prompt Patterns',
  [
    'Repeating entire document every turn in chat',
    'Very long system prompts for simple tasks',
    'Asking for long CoT on easy questions',
    'Using Opus when Haiku would suffice',
    'Generating full JSON when only key needed',
    'Sending high-res images when thumbnail works',
  ],
  'Cost-Reduction Strategies',
  [
    'Use prompt caching for repeated context',
    'Route simple tasks to Haiku ($0.25/M vs $15/M)',
    'Summarise conversation history periodically',
    'Use max_tokens to cap output length',
    'Batch requests when possible',
    'Extract only needed info before passing to LLM',
  ], C.teal
);

// ════════════════════════════════════════════════════════════════════
//  EXTRA SLIDES — L07 additions
// ════════════════════════════════════════════════════════════════════
codeSlide(n++, 'L07 · Lab — API Call', 'Async API Calls for Production',
`import asyncio
import anthropic

async def generate_multiple(prompts: list[str]) -> list[str]:
    """Send multiple prompts concurrently — much faster than sequential."""
    client = anthropic.AsyncAnthropic()
    
    async def one_call(prompt):
        msg = await client.messages.create(
            model="claude-haiku-4-5",
            max_tokens=512,
            messages=[{"role": "user", "content": prompt}]
        )
        return msg.content[0].text
    
    # Run all prompts concurrently
    results = await asyncio.gather(*[one_call(p) for p in prompts])
    return results

# Usage
prompts = ["Summarise AI safety", "Explain RLHF", "What is RAG?"]
results = asyncio.run(generate_multiple(prompts))
for p, r in zip(prompts, results):
    print(f"Q: {p}\\nA: {r[:100]}...\\n")`,
  'Async: 3 calls in ~2 seconds vs ~6 seconds sequential. Critical for production throughput.', C.green
);

bulletSlide(n++, 'L07 · Lab — API Call', 'Prompt Caching — Reducing Costs for Repeated Context', [
  'Prompt caching: Anthropic caches frequently reused prompt prefixes server-side for 5 minutes',
  'Use case: same large system prompt + different user messages across thousands of requests',
  'API: add "cache_control": {"type": "ephemeral"} to the message block you want to cache',
  'Cost reduction: cached tokens cost 10% of normal input tokens → 90% savings on repeated context',
  'Example: 100K-token legal document + 1000 different questions → cache document, pay full price only once',
  'Cache key: exact byte-match of prompt prefix — even one character difference creates a cache miss',
], C.green);

bulletSlide(n++, 'L07 · Lab — API Call', 'Production Checklist for Claude API Integration', [
  '✅ API key in environment variable (never in source code or git history)',
  '✅ Exponential backoff with jitter for RateLimitError and 5xx responses',
  '✅ max_tokens set appropriately — prevents runaway costs from unexpectedly long outputs',
  '✅ stop_reason checked — handle "max_tokens" differently from "end_turn" (truncated response)',
  '✅ usage tokens logged — enables cost monitoring and anomaly detection',
  '✅ Input validation before API call — reject obviously bad inputs before spending tokens on them',
], C.green);


// ════════════════════════════════════════════════════════════════════
//  FINAL REVIEW SLIDE
// ════════════════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  bg(s, C.navy);
  rect(s, 0, 0, 10, 0.06, C.red);
  rect(s, 0, 5.565, 10, 0.06, C.red);
  txt(s, 'UNIT 1 COMPLETE', 0.3, 0.3, 9.4, 0.8,
    { fontSize:36, color: C.white, bold:true, fontFace:'Calibri', align:'center' });
  txt(s, 'Foundations of Large Language Models', 0.3, 1.1, 9.4, 0.5,
    { fontSize:18, color: C.gold, fontFace:'Calibri', align:'center' });
  const items = [
    'L01: 70-year NLP history — rules → stats → embeddings → attention → transformers',
    'L02: Q/K/V attention · multi-head · PE · FFN · residuals · BERT vs GPT',
    'L03: Scaling laws · GPT lineage · open-source ecosystem · RAG · fine-tuning',
    'L04: RLHF · Constitutional AI · critique-revision · RLAIF · red-teaming',
    'L05: 200K context · vision · tool use · HHH behaviour · prompt engineering',
    'L06: BPE tokenisation · temperature · top-p · top-k · cost optimisation',
    'L07: Anthropic SDK · messages · multi-turn · streaming · async · production',
  ];
  const rich = items.map((it,i) => ({
    text: it,
    options: { bullet:true, fontSize:13, color: C.light, fontFace:'Calibri', breakLine: i<items.length-1 }
  }));
  txt(s, rich, 0.5, 1.72, 9.0, 3.3, {});
  txt(s, 'Next: Unit 2 — Prompt Engineering & Advanced Techniques', 0.3, 5.1, 9.4, 0.38,
    { fontSize:11, color: C.mid, fontFace:'Calibri', align:'center', italic:true });
  bottomBar(s, n++);
}

// ── Write file ───────────────────────────────────────────────────────
pres.writeFile({ fileName: '/sessions/blissful-quirky-tesla/mnt/outputs/CSAI601_Unit1_Slides.pptx' })
  .then(() => console.log('DONE — CSAI601_Unit1_Slides.pptx written ✓'))
  .catch(e => { console.error('ERROR:', e); process.exit(1); });
