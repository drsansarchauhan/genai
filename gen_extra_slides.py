# Generates extra slides and appends writeFile to the base working script

import shutil

# Copy the original working 74-slide script as our base
shutil.copy(
    '/sessions/blissful-quirky-tesla/mnt/outputs/make_unit1_slides.js',
    '/sessions/blissful-quirky-tesla/mnt/outputs/make_unit1_full.js'
)

# Remove the last 5 lines (the writeFile block) so we can add slides before it
with open('/sessions/blissful-quirky-tesla/mnt/outputs/make_unit1_full.js', 'r') as f:
    lines = f.readlines()

# Strip the writeFile block from the end
cutoff = len(lines)
for i in range(len(lines)-1, max(len(lines)-15, 0), -1):
    if 'pres.writeFile' in lines[i]:
        cutoff = i
        break

base = lines[:cutoff]

# ── Extra slide generators (plain JS, no heredoc issues) ─────────────

def b(items, col='C.light'):
    """Generate rich text array for bullet list"""
    parts = []
    for i, it in enumerate(items):
        last = i == len(items)-1
        parts.append(
            '  { text: ' + repr(it) + ', options: { bullet:true, fontSize:13.5, '
            'color:' + col + ', fontFace:"Calibri", breakLine:' + ('false' if last else 'true') + ' } }'
        )
    return '[\n' + ',\n'.join(parts) + '\n]'

extra = []
extra.append('\n// ═══════ EXTRA SLIDES — expanding each lecture to 14+ ═══════\n')

# ─── L01 extra ────────────────────────────────────────────────────────
extra.append("""
bulletSlide(n++, 'L01 · History of AI & NLP', 'GloVe & FastText — Beyond Word2Vec', [
  'GloVe (Stanford, 2014): Global Vectors — factorises global word co-occurrence matrix, not local windows',
  'GloVe loss: Σᵢⱼ f(Xᵢⱼ)(wᵢᵀw̃ⱼ + bᵢ + b̃ⱼ − log Xᵢⱼ)² — directly fits co-occurrence statistics',
  'FastText (Facebook, 2016): word = sum of character n-gram embeddings (tri-grams to hex-grams)',
  'FastText example: "playing" → <pla + lay + ayi + yin + ing> — sub-words are averaged into one vector',
  'Out-of-vocabulary words: FastText can produce embedding for "unbelievableness" via n-gram composition',
  'Static embedding limitation: polysemy — "bank" near "river" gets same vector as "bank" near "loan"',
], C.red);
""")

extra.append("""
bulletSlide(n++, 'L01 · History of AI & NLP', 'ELMo — Contextual Embeddings (2018)', [
  'ELMo = Embeddings from Language Models (AllenNLP, Peters et al. 2018)',
  'Architecture: 2-layer bidirectional LSTM trained as language model on 1 billion words',
  'Key innovation: word representation = weighted combination of all LSTM layer outputs (not just final)',
  'Layer 0 (embedding): morphological information — "playing" vs "plays"',
  'Layer 1 (LSTM-1): syntactic information — part-of-speech, dependency structure',
  'Layer 2 (LSTM-2): semantic information — word sense disambiguation, coreference',
  '"Bank" near "river" → different ELMo vector than "bank" near "loan" — context-dependent!',
  'Result: SoTA on 6/7 NLP benchmarks in 2018 — final proof that contextual embeddings work',
], C.red);
""")

extra.append("""
bulletSlide(n++, 'L01 · History of AI & NLP', 'Timeline: 70 Years of NLP at a Glance', [
  '1950 — Turing Test proposed. Language as the benchmark for machine intelligence',
  '1966 — ELIZA: pattern-matching chatbot. Zero understanding, but convincing enough to fool users',
  '1990 — IBM statistical MT & Hidden Markov Models for speech recognition',
  '2003 — Bengio neural language model: first dense word embeddings (slow, not widely adopted yet)',
  '2013 — Word2Vec: efficient training, viral adoption. Semantic arithmetic demonstrated',
  '2014 — Seq2Seq + Attention: MT quality surges; attention mechanism born',
  '2017 — "Attention Is All You Need": Transformer. RNNs become obsolete for NLP',
  '2018 — BERT + GPT: pre-train on huge data, fine-tune on tasks. Modern NLP era begins',
], C.red);
""")

# ─── L02 extra ────────────────────────────────────────────────────────
extra.append("""
bulletSlide(n++, 'L02 · Transformer Architecture', 'Transformer vs RNN: Head-to-Head', [
  'Sequential steps: RNN=O(n) sequential — cannot parallelise across sequence. Transformer=O(1) sequential',
  'Path length between positions: RNN=O(n) hops. Transformer=O(1) — direct attention in one step',
  'Training speed: Transformer ~10× faster than LSTM on same hardware due to full parallelism',
  'Memory cost: Transformer=O(n²·d) per layer. RNN=O(n·d). Quadratic attention is the price for O(1) paths',
  'Long-range learning: RNN forgets early tokens via vanishing gradient. Transformer attends to any position',
  'Inductive bias: RNN assumes sequential structure. Transformer has no structural assumption (PE adds it back)',
], C.teal);
""")

extra.append("""
twoColSlide(n++, 'L02 · Transformer Architecture', 'Encoder-Only vs Decoder-Only vs Encoder-Decoder',
  'Model Architectures',
  [
    'Encoder-only: BERT, RoBERTa, ELECTRA, DeBERTa',
    'Decoder-only: GPT family, Claude, LLaMA, Mistral',
    'Encoder-Decoder: T5, BART, mT5, original Transformer',
    'MoE hybrid: Mixtral 8×7B, Switch Transformer',
    'State-space alt: Mamba (linear in sequence length!)',
  ],
  'Best Use Cases',
  [
    'Encoder: classification, NER, QA, embeddings, retrieval',
    'Decoder: generation, dialogue, code, autocomplete',
    'Enc-Dec: translation, summarisation, seq2seq tasks',
    'MoE: high capacity at lower active compute cost',
    'SSM: very long sequences where O(n²) is prohibitive',
  ], C.teal
);
""")

extra.append("""
formulaSlide(n++, 'L02 · Transformer Architecture', 'Complexity: Attention vs RNN vs Convolution',
  'Self-Attn: O(n²·d)    RNN: O(n·d²)    Conv: O(k·n·d²)',
  [
    'n=sequence length, d=model dimension, k=kernel size',
    'Self-attention: quadratic in n — but O(1) sequential steps (fully parallel)',
    'RNN: linear in n — but O(n) sequential steps (cannot parallelise)',
    'Flash Attention (Dao et al., 2022): same O(n²) FLOPs, 3× faster via IO-aware tiling on GPU memory hierarchy',
    'Flash Attention 2 (2023): 2× faster still — used in Claude 3, GPT-4, LLaMA 2/3',
    'Practical limit: on A100 GPU, 100K tokens per layer requires ~40GB VRAM — why 200K ctx is expensive',
  ], C.teal
);
""")

# ─── L03 extra ────────────────────────────────────────────────────────
extra.append("""
bulletSlide(n++, 'L03 · LLM Landscape', 'Open-Source LLM Ecosystem', [
  'LLaMA (Meta, Feb 2023): 7B–65B params. Weights leaked → sparked open-source LLM revolution',
  'LLaMA 2 (Jul 2023): official open release (research + commercial). Chat-tuned variants via RLHF',
  'Mistral 7B (Sep 2023): beats LLaMA 2 13B on most benchmarks. Uses sliding window attention + GQA',
  'Mixtral 8×7B: Mixture of Experts — 8 expert FFNs per layer, 2 active per token. 47B params, 12.9B active',
  'LLaMA 3 (2024): 8B + 70B + 405B. Strong multilingual, 128K context, instruction-tuned variants',
  'Run locally: 7B model at 4-bit quantisation ≈ 4GB VRAM — fits on a gaming GPU or M2 MacBook',
], C.gold);
""")

extra.append("""
bulletSlide(n++, 'L03 · LLM Landscape', 'Fine-Tuning Strategies: LoRA & QLoRA', [
  'Full fine-tuning: update all N parameters. Best quality but requires same GPU memory as pre-training',
  'LoRA (Hu et al. 2021): freeze pretrained weights W₀; add ΔW = A·B where A∈ℝᵈˣʳ, B∈ℝʳˣᵏ, rank r≪d',
  'LoRA math: W_new = W₀ + α·(A·B) — only A and B trained. r=8: 10,000× fewer trainable params than full FT',
  'QLoRA (Dettmers et al. 2023): quantise base model to 4-bit NF4, add 16-bit LoRA adapters on top',
  'QLoRA result: fine-tune 65B LLaMA on single 48GB GPU — previously needed 8×80GB A100s',
  'Instruction tuning: fine-tune on (instruction, output) pairs from FLAN, Alpaca, Dolly datasets',
], C.gold);
""")

extra.append("""
bulletSlide(n++, 'L03 · LLM Landscape', 'Retrieval-Augmented Generation (RAG)', [
  'Problem: LLMs have knowledge cutoffs and no access to your private documents or recent events',
  'RAG pipeline: embed query → vector similarity search → retrieve top-k chunks → include in prompt → generate',
  'Vector stores: FAISS (Facebook), Pinecone, Weaviate, ChromaDB — store and search over embeddings',
  'Embedding model: converts text to dense vector. E.g., text-embedding-3-small produces 1536-dim vectors',
  'Augmented prompt: "Using the following documents: {chunks}\\nAnswer: {question}"',
  'RAG vs fine-tuning: RAG = dynamic retrieval, no retraining needed; FT = baked-in knowledge, no retrieval cost',
], C.gold);
""")

extra.append("""
bulletSlide(n++, 'L03 · LLM Landscape', 'LLM Evaluation Benchmarks', [
  'MMLU: 14,000 questions across 57 subjects (math, law, medicine, history). Tests breadth of world knowledge',
  'HumanEval: 164 Python programming problems. Tests code generation. Pass@k metric (k attempts)',
  'GSM8K: 8,500 grade-school math word problems requiring multi-step reasoning. Tests arithmetic reasoning',
  'TruthfulQA: 817 questions humans answer falsely due to misconceptions. Tests calibration vs. sycophancy',
  'BIG-Bench: 204 tasks spanning beyond typical NLP — musical notation, logic puzzles, social reasoning',
  'MT-Bench: 80 multi-turn questions judged by GPT-4. Best proxy for chatbot user experience quality',
], C.gold);
""")

# ─── L04 extra ────────────────────────────────────────────────────────
extra.append("""
bulletSlide(n++, 'L04 · Constitutional AI', 'AI Safety — Threat Models', [
  'Misuse: malicious actors using capable AI to automate cyberattacks, disinformation, or CBRN research',
  'Accidents: well-intentioned system pursues proxy objective in harmful ways (reward hacking)',
  'Specification gaming: agent achieves reward by violating spirit of objective — "pausing video game to not lose"',
  'Sycophancy: model flatters and agrees with user even when user is factually wrong',
  'Deceptive alignment (hypothetical): model appears aligned in training, behaves differently in deployment',
  'CAI directly addresses misuse (explicit refusal principles) and sycophancy (honesty principles in constitution)',
], C.purple);
""")

extra.append("""
twoColSlide(n++, 'L04 · Constitutional AI', 'HHH — Operationalising Claude Values',
  'Helpful',
  [
    'Give substantive value, not watered-down answers',
    'Complete tasks fully — no unnecessary hedging',
    'Adjust technicality to the user level',
    'Ask clarification only when truly ambiguous',
    'Proactively add relevant info user didn\'t ask for',
  ],
  'Harmless & Honest',
  [
    'Refuse requests enabling real-world harm',
    'Give reasoned refusals, not blunt blocks',
    'Calibrated uncertainty: "I\'m not certain..."',
    'Don\'t claim to be human (if sincerely asked)',
    'Don\'t shift position under social pressure alone',
  ], C.purple
);
""")

extra.append("""
bulletSlide(n++, 'L04 · Constitutional AI', 'Red-Teaming and Ongoing Safety Work', [
  'Red team: group that tries to elicit harmful, unethical, or policy-violating responses from the model',
  'Manual red-teaming: humans craft creative jailbreaks — role-play bypass, indirect requests, code obfuscation',
  'Automated red-teaming: a separate LLM generates adversarial prompts at scale (100K+ attempts)',
  'Anthropic finding: more capable models are both harder to jailbreak AND more dangerous if successfully jailbreaked',
  'CAI improvement: Claude models reject harmful prompts more consistently AND provide more nuanced reasoning',
  'Red-teaming is continuous — new attack vectors discovered as models, users, and deployment contexts evolve',
], C.purple);
""")

# ─── L05 extra ────────────────────────────────────────────────────────
extra.append("""
bulletSlide(n++, "L05 · Claude's Capabilities", 'Agentic Claude — Tool Loops and Automation', [
  'Agent loop: Claude generates action → tool executes → result returned → Claude decides next action',
  'Coding agent: write code → run tests → read output → debug → iterate without human in loop',
  'Research agent: search web → read pages → synthesise → cite sources → write report',
  'Computer use (Claude 3.5): control mouse/keyboard, browse web, interact with desktop GUIs',
  'Multi-agent: orchestrator Claude delegates sub-tasks to specialist Claude instances via tool calls',
  'Safety in agents: mistakes in long chains are hard to reverse — Claude applies extra caution in agentic settings',
], C.green);
""")

extra.append("""
bulletSlide(n++, "L05 · Claude's Capabilities", 'Prompt Engineering — Best Practices', [
  'Be specific: "Write a 200-word explanation of transformers for a 3rd-year CS student" beats "explain transformers"',
  'Use XML tags: <document>{text}</document><question>{q}</question> — Claude was trained on XML-structured data',
  'System prompt: set role, tone, constraints, output format once — applies to entire conversation',
  'Chain-of-thought: "Think step by step before answering" → forces intermediate reasoning → higher accuracy on hard tasks',
  'Negative constraints: "Do not use bullet points. Do not include code." — Claude follows these reliably',
  'Few-shot: 2–3 input/output examples in prompt for consistent format compliance (JSON, tables, specific styles)',
], C.green);
""")

extra.append("""
twoColSlide(n++, "L05 · Claude's Capabilities", 'Claude vs GPT-4 — Practical Comparison',
  'Claude (Anthropic)',
  [
    'Constitutional AI — explicit principles',
    '200K context window (Sonnet & Opus)',
    'Strong long-document reasoning',
    'More thorough explanations by default',
    'Excellent nuanced ethical reasoning',
    'Strong coding + analysis capabilities',
  ],
  'GPT-4 (OpenAI)',
  [
    'RLHF alignment',
    '128K context (GPT-4 Turbo)',
    'Code Interpreter (data analysis in-chat)',
    'Fine-tuning available via API',
    'Larger ChatGPT plugin ecosystem',
    'More widely benchmarked publicly',
  ], C.green
);
""")

# ─── L06 extra ────────────────────────────────────────────────────────
extra.append("""
bulletSlide(n++, 'L06 · Tokenisation & Sampling', 'Tokenisation Quirks That Trip Up Developers', [
  'Case sensitivity: "hello" and "Hello" and "HELLO" may each be different tokens',
  'Leading space: " hello" (space before) is often a different token from "hello" — affects prompt formatting',
  'Numbers split unpredictably: "2024" = 1 token, but "20240528" may split as ["2024", "05", "28"] = 3 tokens',
  'Non-English efficiency: Chinese/Japanese ~1 char per token; same meaning costs 3–4× more tokens than English',
  'Counting accurately: use anthropic SDK count_tokens() method — never guess from character count',
  'Injection risk: adversarial strings crafted to manipulate tokenisation boundaries or escape instruction following',
], C.teal);
""")

extra.append("""
bulletSlide(n++, 'L06 · Tokenisation & Sampling', 'Decoding Strategies Compared', [
  'Greedy (T=0): always pick highest-probability token. Deterministic. Repetitive for open-ended generation',
  'Beam search (B=4): maintain 4 partial sequences, expand all, prune to best 4. More globally optimal than greedy',
  'Beam search weakness: tends to generic output; repetition at high B; slow (B× compute)',
  'Ancestral sampling (T=1): pure random draw from full distribution. Diverse but potentially incoherent',
  'Top-k + temperature: most practical combination. Filter candidates, control randomness level',
  'Top-p + temperature: more adaptive than top-k — nucleus size adjusts to model confidence automatically',
], C.teal);
""")

extra.append("""
twoColSlide(n++, 'L06 · Tokenisation & Sampling', 'API Cost Optimisation Strategies',
  'Expensive Patterns',
  [
    'Resending full document every conversation turn',
    'Very long system prompts for simple tasks',
    'Requesting verbose CoT on easy questions',
    'Using Opus for tasks Haiku handles well',
    'No max_tokens cap — runaway long outputs',
    'Sending high-res images when thumbnail works',
  ],
  'Cost-Reduction Strategies',
  [
    'Prompt caching for repeated large contexts (90% off)',
    'Route by complexity: Haiku for simple, Opus for hard',
    'Summarise conversation history periodically',
    'Set max_tokens tightly for each use case',
    'Batch requests with async calls',
    'Extract only needed data before LLM call',
  ], C.teal
);
""")

# ─── L07 extra ────────────────────────────────────────────────────────
extra.append(r"""
codeSlide(n++, 'L07 · Lab — API Call', 'Async API Calls for Production',
`import asyncio
import anthropic

async def generate_batch(prompts):
    """Send multiple prompts concurrently — much faster than sequential."""
    client = anthropic.AsyncAnthropic()

    async def one_call(prompt):
        msg = await client.messages.create(
            model="claude-haiku-4-5",
            max_tokens=512,
            messages=[{"role": "user", "content": prompt}]
        )
        return msg.content[0].text

    # asyncio.gather runs all calls concurrently
    results = await asyncio.gather(*[one_call(p) for p in prompts])
    return results

prompts = ["Explain RLHF", "What is RAG?", "Summarise transformers"]
results = asyncio.run(generate_batch(prompts))
# 3 API calls in ~2s instead of ~6s sequential`,
  'AsyncAnthropic client required for async calls. asyncio.gather() is the key to concurrent requests.', C.green
);
""")

extra.append("""
bulletSlide(n++, 'L07 · Lab — API Call', 'Prompt Caching — Slash Costs on Repeated Context', [
  'What it is: Anthropic caches frequently reused prompt prefixes server-side for 5 minutes',
  'When to use: same large system prompt or document across many requests (RAG, document Q&A)',
  'How to enable: add cache_control: {type: "ephemeral"} to the content block to be cached',
  'Cost: cached tokens = 10% of normal input price → 90% savings on the repeated portion',
  'Example: 100K-token legal document + 1000 questions → pay full price once, cached price 999 times',
  'Cache key: exact byte-match required — even one character difference = full cache miss',
], C.green);
""")

extra.append("""
bulletSlide(n++, 'L07 · Lab — API Call', 'Production Checklist for Claude Integration', [
  'API key: always from environment variable — NEVER hard-code. Never commit to git. Use .env + dotenv',
  'Error handling: catch RateLimitError (exponential backoff), APIStatusError 5xx (retry), 4xx (raise)',
  'max_tokens: always set — prevents unexpected long outputs and runaway costs',
  'stop_reason check: handle "max_tokens" (truncated) differently from "end_turn" (complete)',
  'Usage logging: log input_tokens + output_tokens per request for cost monitoring and anomaly detection',
  'Input validation: reject obviously invalid inputs before spending tokens — empty string, too-long input',
], C.green);
""")

# ─── Assemble final file ────────────────────────────────────────────
write_file_block = """
// ─── Write file ──────────────────────────────────────────────────────
pres.writeFile({ fileName: '/sessions/blissful-quirky-tesla/mnt/outputs/CSAI601_Unit1_Slides.pptx' })
  .then(() => {
    console.log('DONE — CSAI601_Unit1_Slides.pptx written');
    console.log('Total slides (n-1):', n - 1);
  })
  .catch(e => { console.error('ERROR:', e); process.exit(1); });
"""

with open('/sessions/blissful-quirky-tesla/mnt/outputs/make_unit1_full.js', 'w') as f:
    f.writelines(base)
    for block in extra:
        f.write(block)
    f.write(write_file_block)

print('Done — make_unit1_full.js written')

# Syntax check
import subprocess
r = subprocess.run(['node', '--check', '/sessions/blissful-quirky-tesla/mnt/outputs/make_unit1_full.js'],
                   capture_output=True, text=True)
print('Syntax check:', r.returncode, r.stderr[:200] if r.stderr else 'OK')
