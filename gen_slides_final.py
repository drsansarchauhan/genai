import shutil, subprocess

shutil.copy(
    '/sessions/blissful-quirky-tesla/mnt/outputs/make_unit1_slides.js',
    '/sessions/blissful-quirky-tesla/mnt/outputs/make_unit1_full.js'
)

with open('/sessions/blissful-quirky-tesla/mnt/outputs/make_unit1_full.js', 'r') as f:
    lines = f.readlines()

# Remove the writeFile block (last ~5 lines containing pres.writeFile)
cutoff = len(lines)
for i in range(len(lines)-1, max(len(lines)-15, 0), -1):
    if 'pres.writeFile' in lines[i]:
        cutoff = i
        break
base = lines[:cutoff]

# Build extra slides as a list of JS strings
extras = []

extras.append("""
// ═════ EXTRA SLIDES — L01 additions ═════
bulletSlide(n++, 'L01 · History of AI & NLP', 'GloVe & FastText — Beyond Word2Vec', [
  'GloVe (Stanford, 2014): factorises global co-occurrence matrix X where Xij = times word j in context of i',
  'GloVe loss trains word vectors so wTi wj + bi + bj approximates log(Xij)',
  'FastText (Facebook 2016): word = sum of character n-gram embeddings (subword model)',
  'FastText example: "playing" splits into <pla, lay, ayi, yin, ing, ng> each with own embedding',
  'FastText advantage: produces embedding for unseen words via subword composition',
  'Limitation of all static embeddings: one vector per word regardless of context (polysemy problem)',
], C.red);
""")

extras.append("""
bulletSlide(n++, 'L01 · History of AI & NLP', 'ELMo — Contextual Embeddings (2018)', [
  'ELMo = Embeddings from Language Models (AllenNLP, Peters et al. 2018)',
  'Architecture: 2-layer bidirectional LSTM trained as language model on 1 billion words',
  'Key innovation: representation = weighted sum of ALL LSTM layers, not just the last',
  'Lower LSTM layers capture syntax (POS, chunks); upper layers capture semantics (word sense)',
  '"bank" near "river" gets a different ELMo vector than "bank" near "loan" - context-sensitive!',
  'Result: state-of-the-art on 6 out of 7 NLP benchmarks in 2018; proved contextual reps work',
], C.red);
""")

extras.append("""
bulletSlide(n++, 'L01 · History of AI & NLP', 'NLP Task Taxonomy', [
  'Token classification: POS tagging (The/DT cat/NN), Named Entity Recognition (Apple/ORG London/LOC)',
  'Sequence classification: sentiment analysis (positive/negative), intent detection, topic classification',
  'Sequence-to-sequence: machine translation, abstractive summarisation, question generation',
  'Span extraction: reading comprehension — extract exact answer span from passage given a question',
  'Language modelling: P(wn|w1...wn-1) — the universal pre-training objective for GPT-style models',
  'Coreference resolution: "She hit John. He fell." — determine He refers to John',
], C.red);
""")

extras.append("""
// ═════ EXTRA SLIDES — L02 additions ═════
bulletSlide(n++, 'L02 · Transformer Architecture', 'Transformer vs RNN: Head-to-Head Comparison', [
  'Sequential steps: RNN = O(n) sequential (cannot parallelise). Transformer = O(1) sequential (fully parallel)',
  'Path length between positions: RNN = O(n) hops through hidden states. Transformer = O(1) direct attention',
  'Training speed: Transformer approximately 10x faster than LSTM on same hardware due to full parallelism',
  'Memory cost: Transformer O(n squared x d) per layer. RNN O(n x d). Quadratic is the price for O(1) paths',
  'Long-range dependencies: RNN gradient vanishes over n steps. Transformer attends to any position directly',
  'Scaling: Transformer scales smoothly to billions of params; RNNs become numerically unstable above ~500M',
], C.teal);
""")

extras.append("""
twoColSlide(n++, 'L02 · Transformer Architecture', 'Encoder-Only vs Decoder-Only vs Encoder-Decoder',
  'Architecture Types',
  [
    'Encoder-only: BERT, RoBERTa, ELECTRA, DeBERTa',
    'Decoder-only: GPT series, Claude, LLaMA, Mistral',
    'Encoder-Decoder: T5, BART, original Transformer',
    'Mixture-of-Experts: Mixtral 8x7B, Switch Transformer',
    'State Space Models: Mamba (linear sequence length)',
  ],
  'Best Use Cases',
  [
    'Encoder: classification, NER, Q&A, semantic search',
    'Decoder: text generation, dialogue, code completion',
    'Enc-Dec: translation, summarisation, seq2seq tasks',
    'MoE: large capacity at lower active compute cost',
    'SSM: very long sequences where O(n^2) is too slow',
  ], C.teal
);
""")

extras.append("""
formulaSlide(n++, 'L02 · Transformer Architecture', 'Flash Attention — Making O(n squared) Practical',
  'Standard Attn: O(n squared x d) memory    Flash Attn: O(n x d) memory, same FLOPs',
  [
    'Problem: standard attention materialises the full n x n attention matrix in GPU HBM (slow memory)',
    'Flash Attention (Dao et al. 2022): tile the computation to fit in SRAM (fast memory) without writing nxn matrix',
    'Result: same mathematical output, same O(n squared) FLOPs, but 3x faster and 10x less memory',
    'Flash Attention 2 (2023): further 2x speedup via better GPU thread parallelism and fewer non-matmul FLOPs',
    'Flash Attention 3 (2024): exploits H100 hardware features (FP8, asynchronous pipelines)',
    'Used by: Claude 3, GPT-4, LLaMA 2/3, Mistral, Gemini — essentially every modern LLM training run',
  ], C.teal
);
""")

extras.append("""
// ═════ EXTRA SLIDES — L03 additions ═════
bulletSlide(n++, 'L03 · LLM Landscape', 'Open-Source LLM Ecosystem (2023-2024)', [
  'LLaMA (Meta, Feb 2023): 7B-65B params. Weights leaked, igniting the open-source LLM revolution',
  'LLaMA 2 (Jul 2023): officially released for research and commercial use. RLHF-tuned chat variants included',
  'Mistral 7B (Sep 2023): outperforms LLaMA 2 13B on most benchmarks. Grouped-query attention + sliding window',
  'Mixtral 8x7B: MoE architecture, 8 experts per layer, 2 active per token. 47B total, 12.9B active params',
  'LLaMA 3 (2024): 8B + 70B + 405B variants. Strong multilingual support. 128K context window',
  'Run locally: 7B model at 4-bit quantisation fits in 4GB VRAM. Can run on a MacBook M2 or gaming GPU',
], C.gold);
""")

extras.append("""
bulletSlide(n++, 'L03 · LLM Landscape', 'Fine-Tuning: LoRA and QLoRA', [
  'Full fine-tuning: update all N parameters. Best quality but same GPU cost as pre-training',
  'LoRA (Hu et al. 2021): freeze W0, add delta-W = A times B where rank r is much less than d',
  'LoRA example: r=8 on GPT-3 (175B) means only 4.7M trainable params instead of 175B. 37,000x fewer!',
  'LoRA formula: W_new = W0 + alpha times (A times B) where A and B are the only trained matrices',
  'QLoRA (2023): quantise base model to 4-bit NF4 format, add 16-bit LoRA adapters',
  'QLoRA result: fine-tune 65B LLaMA on a single 48GB GPU, previously needed 8x80GB A100s',
], C.gold);
""")

extras.append("""
bulletSlide(n++, 'L03 · LLM Landscape', 'Retrieval-Augmented Generation (RAG)', [
  'Core problem: LLMs have a fixed knowledge cutoff and no access to private or recent documents',
  'RAG pipeline: (1) embed query, (2) retrieve top-k similar chunks from vector store, (3) include in prompt',
  'Vector store options: FAISS (Meta), Pinecone, Weaviate, ChromaDB — store and search over embeddings',
  'Embedding model: text-embedding-3-small (OpenAI) or voyage-2 (Anthropic) produce dense float vectors',
  'Augmented prompt structure: system=RAG instructions, user=retrieved chunks + original question',
  'RAG vs fine-tuning: RAG = real-time retrieval, auditable sources; fine-tuning = baked-in knowledge, no retrieval cost',
], C.gold);
""")

extras.append("""
bulletSlide(n++, 'L03 · LLM Landscape', 'LLM Evaluation Benchmarks', [
  'MMLU: 14,000 multiple-choice questions across 57 subjects. Measures breadth of world knowledge',
  'HumanEval: 164 Python programming problems. Measures code generation. Pass@k metric',
  'GSM8K: 8,500 grade-school math word problems requiring multi-step arithmetic reasoning',
  'TruthfulQA: 817 questions that humans often answer wrongly due to misconceptions. Measures calibration',
  'BIG-Bench: 204 diverse tasks beyond standard NLP. Reveals emergent vs non-emergent abilities',
  'MT-Bench: 80 multi-turn conversation questions judged by GPT-4. Best proxy for chat UX quality',
], C.gold);
""")

extras.append("""
// ═════ EXTRA SLIDES — L04 additions ═════
bulletSlide(n++, 'L04 · Constitutional AI', 'AI Safety: Key Threat Models', [
  'Misuse: bad actors using capable AI to automate cyberattacks, generate disinformation, or assist CBRN research',
  'Accidents: well-intentioned AI pursues proxy objective harmfully (reward hacking, specification gaming)',
  'Sycophancy: model prioritises user approval over truth, agreeing with wrong statements to seem helpful',
  'Structural risk: AI embedded in critical systems developing misaligned optimisation targets over time',
  'Deceptive alignment (hypothetical): appears aligned in training, behaves differently in deployment',
  'CAI directly targets misuse (refusal principles), sycophancy (honesty principles), and accidents (critique-revision)',
], C.purple);
""")

extras.append("""
twoColSlide(n++, 'L04 · Constitutional AI', 'HHH: Operationalising Claude Values',
  'Helpful',
  [
    'Provide substantive value, not watered-down answers',
    'Complete tasks fully without unnecessary hedging',
    'Match technical level to the user context',
    'Ask for clarification only when genuinely ambiguous',
    'Proactively mention relevant info not explicitly asked',
  ],
  'Harmless + Honest',
  [
    'Decline requests that enable real-world harm',
    'Give reasoned refusals with offered alternatives',
    'Express calibrated uncertainty honestly',
    'Never claim to be human if sincerely asked',
    'Maintain position under social pressure alone',
  ], C.purple
);
""")

extras.append("""
bulletSlide(n++, 'L04 · Constitutional AI', 'Red-Teaming: Stress Testing Safety', [
  'Red team: dedicated group attempting to elicit harmful or policy-violating responses from the model',
  'Manual red-teaming: humans craft creative jailbreaks — roleplay bypass, indirect requests, multilingual tricks',
  'Automated red-teaming: a separate LLM generates thousands of adversarial prompts per hour',
  'Key finding: more capable models are harder to jailbreak AND more dangerous if successfully jailbreaked',
  'CAI effect: Claude models reject harmful prompts more consistently with more nuanced reasoning',
  'Red-teaming must be continuous — new attack vectors emerge as models, users, and use cases evolve',
], C.purple);
""")

extras.append("""
// ═════ EXTRA SLIDES — L05 additions ═════
bulletSlide(n++, "L05 · Claude's Capabilities", 'Agentic Use Cases: Claude as an Autonomous Agent', [
  'Agent loop: Claude selects action, tool executes, result returned, Claude decides next step, repeat',
  'Coding agent: write code, run tests, read error output, debug, iterate — without human in the loop',
  'Research agent: search web, read pages, synthesise findings, generate citations, write final report',
  'Computer use (Claude 3.5): control mouse and keyboard, browse web, interact with desktop GUIs',
  'Multi-agent systems: orchestrator Claude delegates sub-tasks to specialist Claude instances via tool calls',
  'Safety caveat: agentic mistakes can be hard to reverse — Claude applies extra caution in long agent chains',
], C.green);
""")

extras.append("""
bulletSlide(n++, "L05 · Claude's Capabilities", 'Prompt Engineering Best Practices for Claude', [
  'Be specific: "Write 200-word explanation of transformers for 3rd-year CS student" beats "explain transformers"',
  'Use XML tags: wrap context in <document> tags, questions in <question> tags — Claude was trained on XML',
  'System prompt: set persona, constraints, and output format once for the entire conversation',
  'Chain-of-thought: adding "Think step by step" before the answer forces intermediate reasoning steps',
  'Negative constraints work well: "Do not use bullet points. Do not include code." Claude follows these reliably',
  'Few-shot examples: 2-3 input/output pairs in prompt produces consistent format compliance (JSON, tables)',
], C.green);
""")

extras.append("""
twoColSlide(n++, "L05 · Claude's Capabilities", 'Claude vs GPT-4: Practical Comparison',
  'Claude (Anthropic)',
  [
    'Constitutional AI with explicit principles',
    '200K context window on Sonnet and Opus',
    'Strong long-document reasoning performance',
    'More thorough explanations by default',
    'Excellent nuanced ethical reasoning',
    'Strong coding and technical analysis',
  ],
  'GPT-4 (OpenAI)',
  [
    'RLHF-based alignment',
    '128K context window (GPT-4 Turbo)',
    'Code Interpreter (Python sandbox in chat)',
    'Fine-tuning available via API',
    'Larger ChatGPT plugin ecosystem',
    'Most widely benchmarked model publicly',
  ], C.green
);
""")

extras.append("""
// ═════ EXTRA SLIDES — L06 additions ═════
bulletSlide(n++, 'L06 · Tokenisation & Sampling', 'Tokenisation Quirks Developers Must Know', [
  'Case sensitivity: "hello" and "Hello" and "HELLO" may each be different tokens — matters for prompts',
  'Leading spaces: " hello" with a leading space is often a different token from "hello" without it',
  'Numbers split unpredictably: "2024" = 1 token, but "20240528" may tokenise as three separate tokens',
  'Non-English penalty: Chinese or Japanese roughly 1 character per token vs 4 chars per token in English',
  'Count accurately: use anthropic SDK count_tokens() or tiktoken library, never estimate from character count',
  'Prompt injection risk: crafted strings can manipulate tokenisation to confuse instruction following',
], C.teal);
""")

extras.append("""
bulletSlide(n++, 'L06 · Tokenisation & Sampling', 'Decoding Strategies Compared', [
  'Greedy (T=0): always pick the top token. Deterministic. Fast. Repetitive for open-ended tasks',
  'Beam search (B=4): maintain 4 partial sequences, expand all, keep best 4. More optimal but slower',
  'Beam search weakness: generic output at high B values; repetition loops; B times compute cost',
  'Ancestral sampling (T=1.0): pure random draw from the distribution. Diverse but potentially incoherent',
  'Top-k with temperature: practical default. Filter to k candidates, then sample with temperature T',
  'Top-p (nucleus) with temperature: more adaptive than top-k — nucleus size adjusts to model confidence',
], C.teal);
""")

extras.append("""
twoColSlide(n++, 'L06 · Tokenisation & Sampling', 'API Cost Optimisation',
  'Expensive Patterns to Avoid',
  [
    'Re-sending full document every turn in chat',
    'Very long system prompts for simple tasks',
    'Requesting verbose CoT reasoning unnecessarily',
    'Using Opus model when Haiku would suffice',
    'No max_tokens cap allowing runaway outputs',
    'High-resolution images when thumbnail works',
  ],
  'Cost-Reduction Strategies',
  [
    'Prompt caching for repeated context (90% savings)',
    'Route by task complexity: Haiku vs Sonnet vs Opus',
    'Summarise conversation history every N turns',
    'Set tight max_tokens per use-case type',
    'Batch concurrent requests with async client',
    'Extract only needed data before LLM call',
  ], C.teal
);
""")

extras.append("""
// ═════ EXTRA SLIDES — L07 additions ═════
bulletSlide(n++, 'L07 · Lab', 'Async API Calls for Production Throughput', [
  'Problem: sequential API calls waste time — 3 calls at 2s each = 6s total sequentially',
  'Solution: AsyncAnthropic client with asyncio.gather() runs all calls concurrently',
  'Result: same 3 calls take approximately 2s total — limited by the slowest single call',
  'Code pattern: create AsyncAnthropic() client, define async def one_call(prompt), gather all coroutines',
  'Use case: batch processing — summarise 100 documents in parallel vs 100 sequential calls',
  'Rate limit note: concurrent calls still count against your tokens-per-minute limit — add semaphore if needed',
], C.green);
""")

extras.append("""
bulletSlide(n++, 'L07 · Lab', 'Prompt Caching: 90% Cost Reduction on Repeated Context', [
  'What it is: Anthropic caches frequently used prompt prefixes server-side for up to 5 minutes',
  'Ideal use case: same large system prompt or document sent with many different user questions',
  'How to enable: add cache_control: {type: "ephemeral"} to the content block to be cached',
  'Cost structure: first call at full price, subsequent calls within 5 min at 10% of input token price',
  'Real example: 100K-token legal contract + 1000 different queries = full price once, 10% price 999 times',
  'Cache invalidation: any single character difference in the prefix creates a complete cache miss',
], C.green);
""")

extras.append("""
bulletSlide(n++, 'L07 · Lab', 'Production Integration Checklist', [
  'Security: API key always from environment variable. Never hardcode. Use .env file plus python-dotenv',
  'Resilience: catch RateLimitError with exponential backoff, catch 5xx with retry, raise on 4xx',
  'Budget control: set max_tokens on every call. Log input and output token counts for billing tracking',
  'Response validation: always check stop_reason. Handle max_tokens (truncated) vs end_turn (complete)',
  'Observability: log model, latency, token counts, stop_reason per request for monitoring and debugging',
  'Input sanitisation: validate and truncate inputs before sending. Reject empty strings and oversized inputs',
], C.green);
""")

# ─── Final slide ───────────────────────────────────────────────────
extras.append("""
// ═════ UNIT 1 FINAL REVIEW ═════
{
  const s = pres.addSlide();
  bg(s, C.navy);
  rect(s, 0, 0, 10, 0.06, C.red);
  rect(s, 0, 5.565, 10, 0.06, C.red);
  txt(s, 'UNIT 1 COMPLETE', 0.3, 0.3, 9.4, 0.8,
    { fontSize:36, color: C.white, bold:true, fontFace:'Calibri', align:'center' });
  txt(s, 'Foundations of Large Language Models', 0.3, 1.1, 9.4, 0.5,
    { fontSize:18, color: C.gold, fontFace:'Calibri', align:'center' });
  const recap = [
    'L01: 70 years of NLP history — rules, statistics, embeddings, attention, transformers',
    'L02: Q/K/V attention, multi-head, positional encoding, FFN, residuals, Flash Attention',
    'L03: Scaling laws, GPT lineage, open-source ecosystem, LoRA, RAG, benchmarks',
    'L04: RLHF, Constitutional AI, critique-revision loop, RLAIF, red-teaming',
    'L05: 200K context, vision, tool use, agentic loops, HHH behaviour, prompt engineering',
    'L06: BPE tokenisation, temperature, top-p, top-k, decoding strategies, cost optimisation',
    'L07: Anthropic SDK, messages API, multi-turn, streaming, async, production checklist',
  ];
  const rich = recap.map((it,i) => ({
    text: it,
    options: { bullet:true, fontSize:12.5, color: C.light, fontFace:'Calibri', breakLine: i<recap.length-1 }
  }));
  txt(s, rich, 0.5, 1.72, 9.0, 3.3, {});
  txt(s, 'Next: Unit 2 — Prompt Engineering & Advanced Techniques', 0.3, 5.1, 9.4, 0.38,
    { fontSize:11, color: C.mid, fontFace:'Calibri', align:'center', italic:true });
  bottomBar(s, n++);
}
""")

write_block = """
pres.writeFile({ fileName: '/sessions/blissful-quirky-tesla/mnt/outputs/CSAI601_Unit1_Slides.pptx' })
  .then(() => { console.log('DONE'); console.log('Slides:', n - 1); })
  .catch(e => { console.error('ERROR:', e); process.exit(1); });
"""

with open('/sessions/blissful-quirky-tesla/mnt/outputs/make_unit1_full.js', 'w') as f:
    f.writelines(base)
    for block in extras:
        f.write(block)
    f.write(write_block)

print('Script written')
r = subprocess.run(['node', '--check',
                    '/sessions/blissful-quirky-tesla/mnt/outputs/make_unit1_full.js'],
                   capture_output=True, text=True)
print('Syntax:', 'OK' if r.returncode == 0 else r.stderr[:300])
