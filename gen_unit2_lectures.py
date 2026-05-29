#!/usr/bin/env python3
"""Append L09-L15 to CSAI601_Unit2_Notes.html"""

out = '/sessions/blissful-quirky-tesla/mnt/outputs/CSAI601_Unit2_Notes.html'

# ─────────────────────────────────────── L09 ────────────────────────────────
L09 = r"""
  <!-- ═══════════════ L09 ═══════════════ -->
  <section class="lecture" data-lec="L09">
    <div class="lec-hero">
      <div class="lec-hero-inner">
        <span class="unit-tag">Unit 2 &middot; L09</span>
        <h1>Zero-Shot &amp; Few-Shot Prompting</h1>
        <p class="lec-sub">Exploiting model priors vs. steering with demonstrations</p>
        <div class="lec-meta"><span>&#9200; 1 Hour</span><span>&#128218; CO2</span><span>&#127919; Core Technique</span></div>
      </div>
    </div>
    <div class="lec-body">

      <div class="content-card">
        <h2>9.1 The Prompting Spectrum</h2>
        <p>Before models see a single example from you, they already carry billions of training patterns inside their weights.
        <strong>Zero-shot prompting</strong> exploits that prior knowledge directly; <strong>few-shot prompting</strong> steers it
        with handpicked demonstrations embedded in the prompt itself. Between these two poles lies a spectrum every practitioner navigates daily.</p>
        <div class="concept-grid">
          <div class="concept-box" style="border-color:var(--teal)">
            <h4>Zero-Shot</h4>
            <p>No examples. Pure instruction. Works when the task is unambiguous and well-covered by training data.</p>
          </div>
          <div class="concept-box" style="border-color:var(--gold)">
            <h4>One-Shot</h4>
            <p>One example to anchor format and tone. Best when you have exactly one good demonstration.</p>
          </div>
          <div class="concept-box" style="border-color:var(--green)">
            <h4>Few-Shot (2–8)</h4>
            <p>Multiple input-output pairs. Model generalises the pattern to novel inputs.</p>
          </div>
          <div class="concept-box" style="border-color:var(--purple)">
            <h4>Many-Shot</h4>
            <p>Dozens to hundreds of examples in a long-context window. Approaches fine-tuning quality for narrow tasks.</p>
          </div>
        </div>
      </div>

      <div class="content-card">
        <h2>9.2 Zero-Shot: When It Works &amp; When It Fails</h2>
        <p>Zero-shot works because LLMs generalise from pre-training. The craft is in framing the task completely and unambiguously.</p>
        <h3>Making Zero-Shot Prompts Succeed</h3>
        <table class="info-table">
          <thead><tr><th>Component</th><th>Weak</th><th>Strong</th></tr></thead>
          <tbody>
            <tr><td>Task name</td><td>Tell me about this</td><td>Summarise this review in exactly 2 sentences</td></tr>
            <tr><td>Output format</td><td>Give keywords</td><td>List 5 keywords, comma-separated, all lowercase</td></tr>
            <tr><td>Audience</td><td>Explain neural nets</td><td>Explain neural nets to a high-school student with no maths background</td></tr>
            <tr><td>Constraints</td><td>Write an email</td><td>Write a 3-sentence follow-up email; professional tone; no jargon</td></tr>
            <tr><td>Role</td><td>Check my code</td><td>Act as a senior Python security engineer. Find vulnerabilities.</td></tr>
          </tbody>
        </table>
        <h3>Failure Modes</h3>
        <div class="warning-box">
          <strong>Zero-shot breaks down when:</strong>
          <ul>
            <li>The task demands a precise proprietary schema (custom JSON, specific table layout)</li>
            <li>Domain is highly specialised (rare medical conditions, niche legal clauses)</li>
            <li>Desired style is idiosyncratic (brand voice, specific author cadence)</li>
            <li>Multi-step reasoning with exact intermediate steps is required</li>
          </ul>
          <p>In these situations, provide examples (few-shot) or explicit reasoning steps (chain-of-thought).</p>
        </div>
      </div>

      <div class="content-card">
        <h2>9.3 Few-Shot Prompting: Mechanics</h2>
        <p>Few-shot embeds worked examples as Human/Assistant turns before the actual question. Claude learns format, tone, and reasoning
        style from the demonstrations and applies that pattern to the new input.</p>

        <h3>Example: Support Ticket Classification</h3>
        <div class="code-block-wrap">
          <button class="copy-btn" onclick="copyCode(this)">Copy</button>
          <pre><code>System: Classify tickets into: Billing | Technical | Shipping | Other.

H: "My invoice shows double charge."  A: Billing
H: "App crashes on iOS 17."           A: Technical
H: "Package not delivered in 10 days."A: Shipping

H: "I want to cancel my subscription."
A:</code></pre>
        </div>
        <p>Claude outputs: <code>Billing</code> — correctly generalising from 3 demonstrations.</p>

        <h3>Designing Good Demonstrations</h3>
        <table class="info-table">
          <thead><tr><th>Design Rule</th><th>Why It Matters</th></tr></thead>
          <tbody>
            <tr><td>Cover the output space</td><td>If you have 4 classes, show at least one example of each so Claude knows all valid outputs</td></tr>
            <tr><td>Use realistic inputs</td><td>Toy examples lead to brittle generalisation on real data</td></tr>
            <tr><td>Keep format consistent</td><td>Any deviation in how examples are formatted leaks into Claude's output</td></tr>
            <tr><td>Order by difficulty</td><td>Start with easy clear-cut examples, end with edge cases closest to the real query</td></tr>
            <tr><td>Label accurately</td><td>Wrong labels hurt more than no labels — one mislabelled example can flip Claude's understanding</td></tr>
          </tbody>
        </table>
      </div>

      <div class="content-card">
        <h2>9.4 Advanced Few-Shot Patterns</h2>
        <h3>Format Priming</h3>
        <p>Use demonstrations purely to lock in output structure, not to teach the task semantics:</p>
        <div class="code-block-wrap">
          <button class="copy-btn" onclick="copyCode(this)">Copy</button>
          <pre><code>Review: "Good laptop but fan is loud."
Output:
  summary: decent performance
  pros: [portability, battery]
  cons: [fan noise]
  score: 6/10

Review: "Best phone I have owned. Camera is stunning."
Output:
  summary: excellent all-rounder
  pros: [camera, display, build]
  cons: []
  score: 9/10

Review: "{{USER_REVIEW}}"
Output:</code></pre>
        </div>

        <h3>Many-Shot with Long Contexts</h3>
        <p>Claude supports context windows up to 200K tokens. This enables "many-shot" prompting where you embed 50–500 examples.
        Anthropic research shows many-shot can match or exceed fine-tuning on classification and extraction tasks — without any gradient updates.</p>
        <div class="highlight-box">
          <strong>Rule of thumb:</strong> Below 8 examples use few-shot; above 20 examples consider whether the overhead is worth the quality gain vs. a well-crafted system prompt.
        </div>

        <h3>Self-Generated Examples (Bootstrap)</h3>
        <p>When you have no labelled data, ask Claude to generate demonstrations first:</p>
        <div class="code-block-wrap">
          <button class="copy-btn" onclick="copyCode(this)">Copy</button>
          <pre><code>Step 1 — Generate:
"Give me 5 realistic customer complaint emails about delayed shipping
and their ideal one-sentence summaries."

Step 2 — Use as few-shot:
[paste generated pairs]
Email: {{REAL_EMAIL}}
Summary:</code></pre>
        </div>
        <p>This bootstrap works surprisingly well and lets you iterate on demonstration quality before committing to a dataset.</p>
      </div>

      <div class="content-card">
        <h2>9.5 Choosing Between Zero-Shot and Few-Shot</h2>
        <table class="info-table">
          <thead><tr><th>Factor</th><th>Lean Zero-Shot</th><th>Lean Few-Shot</th></tr></thead>
          <tbody>
            <tr><td>Task familiarity</td><td>Common, well-defined task</td><td>Novel or specialised task</td></tr>
            <tr><td>Output format</td><td>Free-form prose is fine</td><td>Strict schema required</td></tr>
            <tr><td>Token budget</td><td>Tight (API cost sensitive)</td><td>Budget allows demonstration overhead</td></tr>
            <tr><td>Data availability</td><td>No labelled examples exist</td><td>Have 2-20 quality examples</td></tr>
            <tr><td>Iteration speed</td><td>Rapid prototyping phase</td><td>Production system tuning phase</td></tr>
          </tbody>
        </table>
        <div class="tip-box">
          <strong>Practical workflow:</strong> Start zero-shot. If quality is insufficient, add 2-3 examples (few-shot). If still insufficient, move to chain-of-thought or fine-tuning.
        </div>
      </div>

      <div class="content-card">
        <h2>L09 Summary</h2>
        <div class="summary-grid">
          <div class="summary-item"><span class="summary-icon">&#128161;</span><h4>Zero-Shot</h4><p>Instruction only. Fast, cheap. Works for common tasks when framing is crisp.</p></div>
          <div class="summary-item"><span class="summary-icon">&#128214;</span><h4>Few-Shot</h4><p>2-8 demonstrations. Locks format and style. Essential for structured outputs.</p></div>
          <div class="summary-item"><span class="summary-icon">&#128640;</span><h4>Many-Shot</h4><p>50+ examples in context. Near fine-tuning quality. Use Claude long-context window.</p></div>
          <div class="summary-item"><span class="summary-icon">&#9881;</span><h4>Bootstrap</h4><p>No data? Ask Claude to generate examples, then use them as demonstrations.</p></div>
        </div>
      </div>

    </div><!-- end lec-body -->
  </section>
"""

# ─────────────────────────────────────── L10 ────────────────────────────────
L10 = r"""
  <!-- ═══════════════ L10 ═══════════════ -->
  <section class="lecture" data-lec="L10">
    <div class="lec-hero">
      <div class="lec-hero-inner">
        <span class="unit-tag">Unit 2 &middot; L10</span>
        <h1>Chain-of-Thought &amp; Reasoning Prompts</h1>
        <p class="lec-sub">Teaching Claude to think before it answers</p>
        <div class="lec-meta"><span>&#9200; 1 Hour</span><span>&#128218; CO2</span><span>&#127919; Advanced Technique</span></div>
      </div>
    </div>
    <div class="lec-body">

      <div class="content-card">
        <h2>10.1 Why Reasoning Matters</h2>
        <p>Large language models are next-token predictors. When asked a multi-step question directly, they produce an answer token by token without any explicit reasoning buffer — leading to brittle results on problems that require arithmetic, logical deduction, or sequential planning. <strong>Chain-of-Thought (CoT)</strong> prompting forces the model to externalise its reasoning before committing to a final answer, dramatically improving accuracy on complex tasks.</p>
        <div class="highlight-box">
          <strong>Key insight (Wei et al., 2022):</strong> Adding "Let's think step by step." to a prompt improved GPT-3 accuracy on grade-school math from 17.7% to 78.7%. The same principle applies to Claude.
        </div>
      </div>

      <div class="content-card">
        <h2>10.2 Chain-of-Thought Variants</h2>
        <div class="concept-grid">
          <div class="concept-box" style="border-color:var(--teal)">
            <h4>Zero-Shot CoT</h4>
            <p>Append <em>"Let's think step by step."</em> — no examples needed. Activates latent reasoning capability.</p>
          </div>
          <div class="concept-box" style="border-color:var(--gold)">
            <h4>Few-Shot CoT</h4>
            <p>Provide examples that include reasoning chains, not just final answers. Model mimics the reasoning style.</p>
          </div>
          <div class="concept-box" style="border-color:var(--green)">
            <h4>Self-Consistency</h4>
            <p>Sample N reasoning paths, take majority vote on the final answer. Reduces variance significantly.</p>
          </div>
          <div class="concept-box" style="border-color:var(--purple)">
            <h4>Extended Thinking</h4>
            <p>Claude 3.7 Sonnet has a built-in thinking mode that allocates extra compute tokens to scratchpad reasoning before answering.</p>
          </div>
        </div>
      </div>

      <div class="content-card">
        <h2>10.3 Zero-Shot CoT in Practice</h2>
        <h3>Simple Trigger Phrases</h3>
        <table class="info-table">
          <thead><tr><th>Phrase</th><th>Best Use</th></tr></thead>
          <tbody>
            <tr><td>Let's think step by step.</td><td>General reasoning, math, logic puzzles</td></tr>
            <tr><td>Walk me through your reasoning.</td><td>Analytical tasks, diagnoses, recommendations</td></tr>
            <tr><td>First, identify the key facts. Then...</td><td>Structured problem-solving</td></tr>
            <tr><td>Before answering, list all assumptions.</td><td>Ambiguous problems with hidden constraints</td></tr>
            <tr><td>Think out loud.</td><td>Creative problem-solving, brainstorming</td></tr>
          </tbody>
        </table>
        <h3>Example: Word Problem</h3>
        <div class="code-block-wrap">
          <button class="copy-btn" onclick="copyCode(this)">Copy</button>
          <pre><code>Without CoT:
Q: A train leaves Delhi at 9am going 80 km/h. Another leaves Mumbai
   at 10am going 100 km/h toward Delhi. Distance: 1400 km. When do
   they meet?
A: 2:30pm (WRONG)

With CoT:
Q: [same question] Let's think step by step.
A: 1. Distance: 1400 km
   2. Train 1 travels from 9am. In the first hour it covers 80 km.
      Remaining gap at 10am: 1400-80=1320 km.
   3. Both now moving toward each other: closing speed=80+100=180 km/h
   4. Time to close 1320 km: 1320/180 = 7.33 h = 7h 20min
   5. 10am + 7h 20min = 5:20pm
   Answer: 5:20pm (CORRECT)</code></pre>
        </div>
      </div>

      <div class="content-card">
        <h2>10.4 Few-Shot CoT</h2>
        <p>Provide demonstrations where the reasoning chain is shown explicitly. Claude will mimic your reasoning style and depth.</p>
        <div class="code-block-wrap">
          <button class="copy-btn" onclick="copyCode(this)">Copy</button>
          <pre><code>Q: Roger has 5 balls. He buys 2 cans of 3 balls each. How many balls?
A: Roger starts with 5. He buys 2x3=6 more. Total: 5+6=11. Answer: 11.

Q: A juggler has 16 balls. Half are golf balls. Half of golf balls
   are blue. How many blue golf balls?
A: 16 total. Half are golf balls = 8. Half of 8 are blue = 4.
   Answer: 4.

Q: [YOUR QUESTION]
A:</code></pre>
        </div>
        <div class="tip-box">
          <strong>Design tip:</strong> Make your reasoning chains match the complexity of your target tasks. Simple 2-step demonstrations do not transfer to 6-step problems.
        </div>
      </div>

      <div class="content-card">
        <h2>10.5 Self-Consistency Decoding</h2>
        <p>Instead of taking a single reasoning path, generate multiple reasoning chains (temperature &gt; 0) and aggregate the final answers:</p>
        <div class="code-block-wrap">
          <button class="copy-btn" onclick="copyCode(this)">Copy</button>
          <pre><code>import anthropic, re
from collections import Counter

client = anthropic.Anthropic()
question = "What is 17% of 340?"

answers = []
for _ in range(5):
    r = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=300,
        messages=[{"role":"user",
                   "content": question + " Let's think step by step."}]
    )
    text = r.content[0].text
    # Extract last number from response
    nums = re.findall(r'\d+\.?\d*', text)
    if nums: answers.append(nums[-1])

final = Counter(answers).most_common(1)[0][0]
print("Majority answer:", final)</code></pre>
        </div>
        <p>Self-consistency typically improves accuracy by 5-15% on arithmetic and logical reasoning benchmarks.</p>
      </div>

      <div class="content-card">
        <h2>10.6 Extended Thinking (Claude 3.7+)</h2>
        <p>Claude 3.7 Sonnet exposes a <code>thinking</code> block in the API — allocated compute tokens used for internal scratchpad reasoning before the final response is generated.</p>
        <div class="code-block-wrap">
          <button class="copy-btn" onclick="copyCode(this)">Copy</button>
          <pre><code>response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=16000,
    thinking={
        "type": "enabled",
        "budget_tokens": 10000   # tokens for scratchpad
    },
    messages=[{"role":"user","content":"Solve: ..."}]
)

for block in response.content:
    if block.type == "thinking":
        print("Scratchpad:\n", block.thinking)
    elif block.type == "text":
        print("Answer:\n", block.text)</code></pre>
        </div>
        <div class="highlight-box">
          <strong>When to use extended thinking:</strong> Complex multi-step math, competitive programming, long-horizon planning, scientific reasoning. Cost: ~3x token overhead. Use judiciously.
        </div>
      </div>

      <div class="content-card">
        <h2>10.7 Structuring Complex Reasoning</h2>
        <h3>The PREP Framework</h3>
        <table class="info-table">
          <thead><tr><th>Step</th><th>Instruction</th><th>Purpose</th></tr></thead>
          <tbody>
            <tr><td><strong>P</strong>roblem</td><td>Restate the problem in your own words</td><td>Confirms correct understanding</td></tr>
            <tr><td><strong>R</strong>elevant facts</td><td>List all known quantities and constraints</td><td>Surfaces hidden assumptions</td></tr>
            <tr><td><strong>E</strong>xecution</td><td>Solve step by step, showing each operation</td><td>Auditable reasoning chain</td></tr>
            <tr><td><strong>P</strong>lausibility check</td><td>Sanity-check the answer against intuition</td><td>Catches calculation errors</td></tr>
          </tbody>
        </table>
        <div class="code-block-wrap">
          <button class="copy-btn" onclick="copyCode(this)">Copy</button>
          <pre><code>Solve this using the PREP framework:
Problem: [QUESTION]

P (Problem restatement):
R (Relevant facts):
E (Step-by-step execution):
P (Plausibility check):</code></pre>
        </div>
      </div>

      <div class="content-card">
        <h2>L10 Summary</h2>
        <div class="summary-grid">
          <div class="summary-item"><span class="summary-icon">&#128161;</span><h4>Zero-Shot CoT</h4><p>"Think step by step" unlocks latent reasoning. Works on most LLMs with no examples.</p></div>
          <div class="summary-item"><span class="summary-icon">&#128214;</span><h4>Few-Shot CoT</h4><p>Show reasoning chains in demonstrations. Model mimics depth and style.</p></div>
          <div class="summary-item"><span class="summary-icon">&#128202;</span><h4>Self-Consistency</h4><p>Sample multiple paths, take majority vote. +5-15% accuracy on reasoning tasks.</p></div>
          <div class="summary-item"><span class="summary-icon">&#9881;</span><h4>Extended Thinking</h4><p>Claude 3.7 built-in scratchpad. Best for hardest reasoning tasks.</p></div>
        </div>
      </div>

    </div>
  </section>
"""

# ─────────────────────────────────────── L11 ────────────────────────────────
L11 = r"""
  <!-- ═══════════════ L11 ═══════════════ -->
  <section class="lecture" data-lec="L11">
    <div class="lec-hero">
      <div class="lec-hero-inner">
        <span class="unit-tag">Unit 2 &middot; L11</span>
        <h1>Role, Persona &amp; Tone Control</h1>
        <p class="lec-sub">Shaping who Claude is and how it speaks</p>
        <div class="lec-meta"><span>&#9200; 1 Hour</span><span>&#128218; CO2</span><span>&#127919; Persona Design</span></div>
      </div>
    </div>
    <div class="lec-body">

      <div class="content-card">
        <h2>11.1 The Power of Role Assignment</h2>
        <p>Assigning a role to Claude does more than change its tone — it activates a cluster of knowledge, terminology, values, and communication patterns associated with that role in Claude's training. A senior cardiologist, a startup founder, and a high-school teacher will explain "cardiac risk" in structurally different ways, and so will Claude when primed with each role.</p>
        <div class="concept-grid">
          <div class="concept-box" style="border-color:var(--teal)">
            <h4>Professional Roles</h4>
            <p>Doctor, lawyer, engineer, teacher — activates domain vocabulary and communication norms.</p>
          </div>
          <div class="concept-box" style="border-color:var(--gold)">
            <h4>Creative Roles</h4>
            <p>Novelist, screenwriter, copywriter — unlocks narrative voice and creative latitude.</p>
          </div>
          <div class="concept-box" style="border-color:var(--green)">
            <h4>Functional Roles</h4>
            <p>Critic, devil's advocate, fact-checker — shapes the lens through which Claude evaluates content.</p>
          </div>
          <div class="concept-box" style="border-color:var(--purple)">
            <h4>Hybrid Roles</h4>
            <p>"Act as a UX designer with a background in behavioural psychology" — stack roles for precision.</p>
          </div>
        </div>
      </div>

      <div class="content-card">
        <h2>11.2 Building a Persona</h2>
        <p>A persona is a richer specification than a role. It combines identity, expertise, personality, communication style, and constraints into a coherent character that Claude maintains across a conversation.</p>
        <h3>Persona Template</h3>
        <div class="code-block-wrap">
          <button class="copy-btn" onclick="copyCode(this)">Copy</button>
          <pre><code>You are Priya, a senior data scientist at a B2B SaaS company.

Identity:
- 8 years experience in ML, specialising in churn prediction
- Direct communication style — no filler phrases
- Uses concrete numbers over vague adjectives

Expertise:
- Python, SQL, scikit-learn, XGBoost, Spark
- Familiar with Salesforce, Mixpanel, Amplitude

Communication rules:
- Always ask for the business context before diving technical
- When uncertain, say so explicitly rather than guessing
- Offer 2-3 options with trade-offs, never a single answer

Do not:
- Use marketing language ("game-changing", "synergy")
- Recommend paid tools when free alternatives exist</code></pre>
        </div>
      </div>

      <div class="content-card">
        <h2>11.3 Tone Control Dimensions</h2>
        <table class="info-table">
          <thead><tr><th>Dimension</th><th>Examples</th><th>How to Specify</th></tr></thead>
          <tbody>
            <tr><td>Formality</td><td>Casual / Professional / Academic</td><td>"Write in a casual, conversational tone suitable for a Slack message"</td></tr>
            <tr><td>Brevity</td><td>Terse / Balanced / Expansive</td><td>"Be concise. Maximum 3 sentences per response."</td></tr>
            <tr><td>Hedging</td><td>Confident / Cautious / Neutral</td><td>"State conclusions directly. Do not hedge with 'perhaps' or 'it seems'."</td></tr>
            <tr><td>Empathy</td><td>Clinical / Warm / Supportive</td><td>"Use empathetic language. Acknowledge the user's frustration before solving."</td></tr>
            <tr><td>Technical depth</td><td>Lay / Intermediate / Expert</td><td>"Assume the reader has a CS degree but no ML background."</td></tr>
          </tbody>
        </table>

        <h3>Layered Tone Example</h3>
        <div class="code-block-wrap">
          <button class="copy-btn" onclick="copyCode(this)">Copy</button>
          <pre><code>Write customer support responses with:
- Tone: warm, empathetic but professional
- Formality: semi-formal (no slang, but contractions allowed)
- Length: 3-5 sentences
- Always: acknowledge the issue in sentence 1, give solution in 2-3, close warmly
- Never: use phrases like "I understand your frustration" (overused)</code></pre>
        </div>
      </div>

      <div class="content-card">
        <h2>11.4 Audience Calibration</h2>
        <p>The same content needs radically different framing depending on who reads it. Explicitly specifying your audience is one of the highest-leverage prompt improvements.</p>
        <table class="info-table">
          <thead><tr><th>Audience</th><th>Prompt Modifier</th><th>Effect</th></tr></thead>
          <tbody>
            <tr><td>5-year-old child</td><td>"Explain like I'm 5"</td><td>Analogies, simple words, no jargon</td></tr>
            <tr><td>Domain expert</td><td>"Assume PhD-level background in X"</td><td>Technical depth, field-specific terminology</td></tr>
            <tr><td>Executive</td><td>"C-suite audience, 2-minute read"</td><td>Strategic framing, business impact, no implementation details</td></tr>
            <tr><td>Journalist</td><td>"Write for a general audience of educated readers"</td><td>Clear prose, concrete examples, no assumed prior knowledge</td></tr>
            <tr><td>Developer</td><td>"Technical audience; include code examples"</td><td>Code-first, concise explanation, links to references</td></tr>
          </tbody>
        </table>
      </div>

      <div class="content-card">
        <h2>11.5 Maintaining Persona Across Turns</h2>
        <p>In multi-turn conversations, Claude can drift from a persona as the conversation evolves. Techniques to maintain consistency:</p>
        <div class="concept-grid">
          <div class="concept-box" style="border-color:var(--teal)">
            <h4>System Prompt Anchoring</h4>
            <p>Keep the full persona definition in the system prompt. It persists across all turns automatically.</p>
          </div>
          <div class="concept-box" style="border-color:var(--gold)">
            <h4>Explicit Reminders</h4>
            <p>Occasionally append "Respond as Priya" to user turns during long conversations.</p>
          </div>
          <div class="concept-box" style="border-color:var(--green)">
            <h4>Negative Constraints</h4>
            <p>List what the persona should never do — these are often more robust than positive instructions.</p>
          </div>
          <div class="concept-box" style="border-color:var(--red)">
            <h4>Persona vs. Ethics</h4>
            <p>Claude will not maintain a persona that conflicts with its values. Never design personas to circumvent safety guidelines.</p>
          </div>
        </div>
      </div>

      <div class="content-card">
        <h2>L11 Summary</h2>
        <div class="summary-grid">
          <div class="summary-item"><span class="summary-icon">&#127775;</span><h4>Role Assignment</h4><p>Activates knowledge clusters. Stack roles for precision (domain + function).</p></div>
          <div class="summary-item"><span class="summary-icon">&#129302;</span><h4>Persona Design</h4><p>Identity + expertise + communication rules + constraints = stable, useful character.</p></div>
          <div class="summary-item"><span class="summary-icon">&#127908;</span><h4>Tone Control</h4><p>Formality, brevity, hedging, empathy, depth — all specifiable and combinable.</p></div>
          <div class="summary-item"><span class="summary-icon">&#128100;</span><h4>Audience Calibration</h4><p>Matching complexity to reader is the single highest-leverage prompt edit.</p></div>
        </div>
      </div>

    </div>
  </section>
"""

# ─────────────────────────────────────── L12 ────────────────────────────────
L12 = r"""
  <!-- ═══════════════ L12 ═══════════════ -->
  <section class="lecture" data-lec="L12">
    <div class="lec-hero">
      <div class="lec-hero-inner">
        <span class="unit-tag">Unit 2 &middot; L12</span>
        <h1>Structured Output &amp; Format Control</h1>
        <p class="lec-sub">Getting Claude to produce machine-readable and precisely formatted responses</p>
        <div class="lec-meta"><span>&#9200; 1 Hour</span><span>&#128218; CO2</span><span>&#127919; Production Skill</span></div>
      </div>
    </div>
    <div class="lec-body">

      <div class="content-card">
        <h2>12.1 Why Structured Output Matters</h2>
        <p>In production applications, Claude's output is rarely read by a human directly — it feeds downstream systems: databases, APIs, UI renderers, workflow automations. If the output format is inconsistent, the whole pipeline breaks. Structured output prompting is the art of making Claude produce <em>exactly</em> the format your downstream expects, every single time.</p>
        <div class="highlight-box">
          <strong>The golden rule:</strong> Any system that parses Claude's output programmatically must specify the output format explicitly in the prompt. Never rely on implicit formatting.
        </div>
      </div>

      <div class="content-card">
        <h2>12.2 JSON Output</h2>
        <p>JSON is the most common structured output format. There are three techniques to enforce it:</p>
        <h3>Technique 1: Explicit Instruction</h3>
        <div class="code-block-wrap">
          <button class="copy-btn" onclick="copyCode(this)">Copy</button>
          <pre><code>Extract the following from the text and return ONLY valid JSON.
No markdown, no explanation, no code fences.

Schema:
{
  "name": string,
  "date": "YYYY-MM-DD",
  "amount": number,
  "currency": "USD"|"EUR"|"INR"
}

Text: "Received payment of Rs.5,000 from Amit on 12 March 2025."</code></pre>
        </div>
        <h3>Technique 2: JSON Mode (API)</h3>
        <div class="code-block-wrap">
          <button class="copy-btn" onclick="copyCode(this)">Copy</button>
          <pre><code># Note: Claude does not have a dedicated json_mode parameter.
# Instead, use explicit schema instruction + response validation.
import json, anthropic

client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=500,
    system="You output only valid JSON. No extra text.",
    messages=[{"role":"user","content": PROMPT}]
)
data = json.loads(response.content[0].text)  # Validate immediately</code></pre>
        </div>
        <h3>Technique 3: Seed the Response</h3>
        <div class="code-block-wrap">
          <button class="copy-btn" onclick="copyCode(this)">Copy</button>
          <pre><code># Provide the opening brace as the start of the assistant turn
messages = [
    {"role": "user",    "content": "Extract entities. Return JSON."},
    {"role": "assistant","content": "{"}   # Force JSON start
]</code></pre>
        </div>
      </div>

      <div class="content-card">
        <h2>12.3 XML, Markdown Tables &amp; Custom Formats</h2>
        <h3>XML Output</h3>
        <div class="code-block-wrap">
          <button class="copy-btn" onclick="copyCode(this)">Copy</button>
          <pre><code>Return the analysis in this exact XML structure:
&lt;analysis&gt;
  &lt;sentiment&gt;positive|negative|neutral&lt;/sentiment&gt;
  &lt;confidence&gt;0.0 to 1.0&lt;/confidence&gt;
  &lt;reasons&gt;
    &lt;reason&gt;...&lt;/reason&gt;
  &lt;/reasons&gt;
&lt;/analysis&gt;</code></pre>
        </div>
        <h3>Markdown Tables</h3>
        <div class="code-block-wrap">
          <button class="copy-btn" onclick="copyCode(this)">Copy</button>
          <pre><code>Compare these 3 frameworks. Return a markdown table with columns:
Framework | Stars | License | Best For | Weakness

Do not include any prose before or after the table.</code></pre>
        </div>
        <h3>Custom Delimited Formats</h3>
        <div class="code-block-wrap">
          <button class="copy-btn" onclick="copyCode(this)">Copy</button>
          <pre><code>Return each finding on a new line in this format:
SEVERITY|COMPONENT|DESCRIPTION
Example:
HIGH|AuthService|JWT tokens are not expiring</code></pre>
        </div>
      </div>

      <div class="content-card">
        <h2>12.4 Schema Enforcement &amp; Validation</h2>
        <p>Even with perfect prompts, Claude occasionally deviates. Build a validation layer:</p>
        <div class="code-block-wrap">
          <button class="copy-btn" onclick="copyCode(this)">Copy</button>
          <pre><code>from pydantic import BaseModel, ValidationError
import json, anthropic

class Ticket(BaseModel):
    category: str
    priority: int      # 1-5
    summary: str
    tags: list[str]

client = anthropic.Anthropic()

def extract_ticket(text: str, retries: int = 3) -> Ticket:
    for attempt in range(retries):
        r = client.messages.create(
            model="claude-opus-4-5",
            max_tokens=300,
            system="Output only valid JSON matching the Ticket schema.",
            messages=[{"role":"user","content": text}]
        )
        try:
            data = json.loads(r.content[0].text)
            return Ticket(**data)
        except (json.JSONDecodeError, ValidationError) as e:
            if attempt == retries - 1:
                raise
            text = f"Previous output was invalid: {e}. Try again.\n{text}"</code></pre>
        </div>
      </div>

      <div class="content-card">
        <h2>12.5 Length &amp; Density Control</h2>
        <table class="info-table">
          <thead><tr><th>Control Type</th><th>Instruction Pattern</th><th>Example</th></tr></thead>
          <tbody>
            <tr><td>Hard word limit</td><td>"In exactly N words"</td><td>"Summarise in exactly 50 words."</td></tr>
            <tr><td>Sentence count</td><td>"In N sentences"</td><td>"Explain in 3 sentences."</td></tr>
            <tr><td>Bullet count</td><td>"List exactly N points"</td><td>"Give exactly 5 action items."</td></tr>
            <tr><td>Token budget</td><td>"Be brief" / "Be exhaustive"</td><td>"Exhaustive technical documentation."</td></tr>
            <tr><td>Depth by section</td><td>Per-section specs</td><td>"Introduction: 2 sentences. Details: 4 paragraphs. Summary: 1 sentence."</td></tr>
          </tbody>
        </table>
        <div class="warning-box">
          <strong>Note:</strong> Claude understands approximate word/sentence counts well. Exact character counts are less reliable. For hard character limits (SMS, Twitter), always validate programmatically and retry if needed.
        </div>
      </div>

      <div class="content-card">
        <h2>L12 Summary</h2>
        <div class="summary-grid">
          <div class="summary-item"><span class="summary-icon">&#123;&#125;</span><h4>JSON Output</h4><p>Explicit schema, seed responses, always validate with Pydantic or json.loads.</p></div>
          <div class="summary-item"><span class="summary-icon">&#128196;</span><h4>XML / Custom</h4><p>Show the exact template. Use XML tags for complex nested structures.</p></div>
          <div class="summary-item"><span class="summary-icon">&#128207;</span><h4>Length Control</h4><p>Word limits, sentence counts, per-section specs. Hard limits need programmatic validation.</p></div>
          <div class="summary-item"><span class="summary-icon">&#9989;</span><h4>Validation</h4><p>Retry loop with error feedback. Claude corrects itself when shown the specific failure.</p></div>
        </div>
      </div>

    </div>
  </section>
"""

# ─────────────────────────────────────── L13 ────────────────────────────────
L13 = r"""
  <!-- ═══════════════ L13 ═══════════════ -->
  <section class="lecture" data-lec="L13">
    <div class="lec-hero">
      <div class="lec-hero-inner">
        <span class="unit-tag">Unit 2 &middot; L13</span>
        <h1>Context Management &amp; Long Conversations</h1>
        <p class="lec-sub">Working effectively within and beyond context windows</p>
        <div class="lec-meta"><span>&#9200; 1 Hour</span><span>&#128218; CO2</span><span>&#127919; Architecture Skill</span></div>
      </div>
    </div>
    <div class="lec-body">

      <div class="content-card">
        <h2>13.1 Understanding the Context Window</h2>
        <p>The context window is the total number of tokens Claude can see at once — including the system prompt, all conversation history, and the current message. Claude Opus and Sonnet 3.5+ support a 200K token window, roughly equivalent to a 150,000-word novel or 600 pages of dense text.</p>
        <table class="info-table">
          <thead><tr><th>Model</th><th>Context Window</th><th>Approx. Pages</th></tr></thead>
          <tbody>
            <tr><td>Claude Haiku 3.5</td><td>200K tokens</td><td>~600 pages</td></tr>
            <tr><td>Claude Sonnet 3.5/4</td><td>200K tokens</td><td>~600 pages</td></tr>
            <tr><td>Claude Opus 4</td><td>200K tokens</td><td>~600 pages</td></tr>
          </tbody>
        </table>
        <div class="highlight-box">
          <strong>The "Lost in the Middle" problem:</strong> Research shows that LLMs recall information placed at the beginning and end of the context most reliably. Content in the middle of a long context is retrieved less accurately. Place the most important instructions at the top (system prompt) and just before the question.
        </div>
      </div>

      <div class="content-card">
        <h2>13.2 Context Management Strategies</h2>
        <div class="concept-grid">
          <div class="concept-box" style="border-color:var(--teal)">
            <h4>Sliding Window</h4>
            <p>Keep only the N most recent turns. Oldest turns are dropped. Simple but loses early context.</p>
          </div>
          <div class="concept-box" style="border-color:var(--gold)">
            <h4>Summarisation</h4>
            <p>Periodically ask Claude to summarise the conversation so far, then replace the raw history with the summary.</p>
          </div>
          <div class="concept-box" style="border-color:var(--green)">
            <h4>Retrieval-Augmented</h4>
            <p>Store conversation turns in a vector database. Retrieve only the most relevant turns for each new message.</p>
          </div>
          <div class="concept-box" style="border-color:var(--purple)">
            <h4>Hierarchical Memory</h4>
            <p>Working memory (recent turns) + episodic memory (summaries) + semantic memory (facts) managed separately.</p>
          </div>
        </div>
      </div>

      <div class="content-card">
        <h2>13.3 Conversation Summarisation</h2>
        <div class="code-block-wrap">
          <button class="copy-btn" onclick="copyCode(this)">Copy</button>
          <pre><code>import anthropic

client = anthropic.Anthropic()
MAX_TURNS = 10

def summarise_history(history: list) -> str:
    summary_prompt = [
        *history,
        {"role": "user",
         "content": "Summarise the above conversation in bullet points. Focus on: decisions made, facts established, open questions. Be concise - this summary replaces the full history."}
    ]
    r = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=500,
        messages=summary_prompt
    )
    return r.content[0].text

def chat(history: list, user_msg: str) -> tuple[str, list]:
    if len(history) > MAX_TURNS * 2:
        summary = summarise_history(history)
        history = [{"role":"assistant",
                    "content": f"[Conversation summary]\n{summary}"}]

    history.append({"role":"user","content": user_msg})
    r = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1000,
        messages=history
    )
    reply = r.content[0].text
    history.append({"role":"assistant","content": reply})
    return reply, history</code></pre>
        </div>
      </div>

      <div class="content-card">
        <h2>13.4 Document Chunking Strategies</h2>
        <p>When processing documents longer than the context window, you must chunk them. Different chunking strategies suit different tasks:</p>
        <table class="info-table">
          <thead><tr><th>Strategy</th><th>How</th><th>Best For</th></tr></thead>
          <tbody>
            <tr><td>Fixed-size chunks</td><td>Split every N tokens with overlap</td><td>Vector search, embedding</td></tr>
            <tr><td>Semantic chunks</td><td>Split at paragraph/section boundaries</td><td>Q&amp;A, summarisation</td></tr>
            <tr><td>Hierarchical</td><td>Chunk by chapter, then section, then paragraph</td><td>Long-form document analysis</td></tr>
            <tr><td>Map-reduce</td><td>Process each chunk independently, combine results</td><td>Summarisation, extraction</td></tr>
            <tr><td>Sliding window</td><td>Overlapping chunks (e.g., 500 tokens, 100 overlap)</td><td>When context spans chunk boundaries</td></tr>
          </tbody>
        </table>
        <h3>Map-Reduce Summarisation</h3>
        <div class="code-block-wrap">
          <button class="copy-btn" onclick="copyCode(this)">Copy</button>
          <pre><code>def map_reduce_summarise(text: str, chunk_size: int = 50000) -> str:
    # Split text into chunks
    words = text.split()
    chunks = [" ".join(words[i:i+chunk_size])
              for i in range(0, len(words), chunk_size)]

    # Map: summarise each chunk
    summaries = []
    for chunk in chunks:
        r = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=500,
            messages=[{"role":"user",
                       "content":f"Summarise:\n{chunk}"}]
        )
        summaries.append(r.content[0].text)

    # Reduce: combine summaries
    combined = "\n\n".join(summaries)
    r = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1000,
        messages=[{"role":"user",
                   "content":f"Combine these summaries into a final coherent summary:\n{combined}"}]
    )
    return r.content[0].text</code></pre>
        </div>
      </div>

      <div class="content-card">
        <h2>13.5 System Prompt Design for Long Sessions</h2>
        <p>The system prompt is always present and costs tokens on every call. Design it for efficiency:</p>
        <table class="info-table">
          <thead><tr><th>Do</th><th>Avoid</th></tr></thead>
          <tbody>
            <tr><td>State critical constraints once, clearly</td><td>Repeating the same instruction multiple times</td></tr>
            <tr><td>Use numbered rules for easy reference</td><td>Long paragraph descriptions of behavior</td></tr>
            <tr><td>Include examples only when format is non-obvious</td><td>Including many examples that inflate token cost</td></tr>
            <tr><td>Define abbreviations used in the prompt</td><td>Assuming Claude knows your internal terminology</td></tr>
            <tr><td>Keep the system prompt under 2K tokens when possible</td><td>Dumping the entire product documentation</td></tr>
          </tbody>
        </table>
      </div>

      <div class="content-card">
        <h2>L13 Summary</h2>
        <div class="summary-grid">
          <div class="summary-item"><span class="summary-icon">&#128084;</span><h4>200K Window</h4><p>Large but not infinite. Critical info at top and bottom. Middle is less reliable.</p></div>
          <div class="summary-item"><span class="summary-icon">&#128221;</span><h4>Summarisation</h4><p>Compress old history into summaries. Haiku handles summarisation cheaply.</p></div>
          <div class="summary-item"><span class="summary-icon">&#128209;</span><h4>Chunking</h4><p>Map-reduce for long docs. Semantic chunks for Q&amp;A. Sliding window for continuity.</p></div>
          <div class="summary-item"><span class="summary-icon">&#9881;</span><h4>System Prompt</h4><p>Under 2K tokens. Clear numbered rules. Avoid repetition. Define custom terms.</p></div>
        </div>
      </div>

    </div>
  </section>
"""

# ─────────────────────────────────────── L14 ────────────────────────────────
L14 = r"""
  <!-- ═══════════════ L14 ═══════════════ -->
  <section class="lecture" data-lec="L14">
    <div class="lec-hero">
      <div class="lec-hero-inner">
        <span class="unit-tag">Unit 2 &middot; L14</span>
        <h1>Prompt Evaluation &amp; Iteration</h1>
        <p class="lec-sub">Measuring, testing, and systematically improving prompt quality</p>
        <div class="lec-meta"><span>&#9200; 1 Hour</span><span>&#128218; CO2</span><span>&#127919; Engineering Practice</span></div>
      </div>
    </div>
    <div class="lec-body">

      <div class="content-card">
        <h2>14.1 Why Prompts Need Evaluation</h2>
        <p>A prompt that works on 3 test cases may fail on the 4th. A prompt improved by intuition may actually degrade on edge cases. Systematic prompt evaluation — measuring quality across a diverse test set — is what separates ad-hoc prompting from reliable prompt engineering.</p>
        <div class="highlight-box">
          <strong>Goodhart's Law applied to prompts:</strong> "When a measure becomes a target, it ceases to be a good measure." Optimising a prompt on a small test set often leads to overfitting. Always hold out a validation set.
        </div>
      </div>

      <div class="content-card">
        <h2>14.2 Evaluation Metrics by Task Type</h2>
        <table class="info-table">
          <thead><tr><th>Task Type</th><th>Primary Metric</th><th>Tool / Method</th></tr></thead>
          <tbody>
            <tr><td>Classification</td><td>Accuracy, F1, Confusion Matrix</td><td>sklearn metrics + labelled test set</td></tr>
            <tr><td>Extraction</td><td>Exact match, Partial match, F1</td><td>String matching + normalisation</td></tr>
            <tr><td>Summarisation</td><td>ROUGE-L, BERTScore, Human eval</td><td>evaluate library, LLM-as-judge</td></tr>
            <tr><td>Generation quality</td><td>Human rating (1-5), LLM-as-judge</td><td>Claude grading Claude's outputs</td></tr>
            <tr><td>Format compliance</td><td>Parse success rate</td><td>json.loads() + Pydantic validation</td></tr>
            <tr><td>Latency / Cost</td><td>p50/p95 latency, $/1000 requests</td><td>Usage API, timing instrumentation</td></tr>
          </tbody>
        </table>
      </div>

      <div class="content-card">
        <h2>14.3 LLM-as-Judge</h2>
        <p>Using Claude to evaluate Claude's outputs is surprisingly effective and scales to tasks where labelled ground truth is unavailable. The key is a well-designed evaluation prompt.</p>
        <div class="code-block-wrap">
          <button class="copy-btn" onclick="copyCode(this)">Copy</button>
          <pre><code>EVAL_PROMPT = (
  "You are an expert evaluator. Score the response on 4 dimensions.\n"
  "Task: {task}\nResponse: {response}\n\n"
  "Score 1-5: accuracy, completeness, clarity, format.\n"
  "Return ONLY this JSON:\n"
  '{{"accuracy":N,"completeness":N,"clarity":N,"format":N,'
  '"overall":N,"critique":"one sentence"}}'
)

def evaluate(task: str, response: str) -> dict:
    r = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=200,
        messages=[{"role":"user",
                   "content": EVAL_PROMPT.format(task=task,response=response)}]
    )
    return json.loads(r.content[0].text)</code></pre>
        </div>
      </div>

      <div class="content-card">
        <h2>14.4 A/B Prompt Testing</h2>
        <p>Systematically compare two prompt variants on the same test set:</p>
        <div class="code-block-wrap">
          <button class="copy-btn" onclick="copyCode(this)">Copy</button>
          <pre><code>import statistics

def compare_prompts(prompt_a: str, prompt_b: str,
                    test_cases: list, n_trials: int = 3):
    results = {"A": [], "B": []}

    for case in test_cases:
        for prompt, label in [(prompt_a,"A"),(prompt_b,"B")]:
            scores = []
            for _ in range(n_trials):
                r = client.messages.create(
                    model="claude-opus-4-5",
                    max_tokens=500,
                    messages=[{"role":"user",
                               "content":prompt.format(**case)}]
                )
                score = evaluate(case["task"], r.content[0].text)
                scores.append(score["overall"])
            results[label].append(statistics.mean(scores))

    return {
        "A_mean": statistics.mean(results["A"]),
        "B_mean": statistics.mean(results["B"]),
        "winner": "A" if statistics.mean(results["A"]) > statistics.mean(results["B"]) else "B"
    }</code></pre>
        </div>
      </div>

      <div class="content-card">
        <h2>14.5 Iterative Prompt Improvement</h2>
        <h3>The Prompt Engineering Cycle</h3>
        <table class="info-table">
          <thead><tr><th>Step</th><th>Action</th><th>Outcome</th></tr></thead>
          <tbody>
            <tr><td>1. Baseline</td><td>Write a simple first prompt</td><td>Initial performance score</td></tr>
            <tr><td>2. Failure analysis</td><td>Categorise errors on test set</td><td>Error taxonomy</td></tr>
            <tr><td>3. Hypothesis</td><td>Guess which prompt element causes each error type</td><td>Prioritised changes list</td></tr>
            <tr><td>4. Intervention</td><td>Change one thing at a time</td><td>New prompt variant</td></tr>
            <tr><td>5. Evaluation</td><td>Run full test suite</td><td>Delta vs. baseline</td></tr>
            <tr><td>6. Decision</td><td>Accept, reject, or combine changes</td><td>Updated best prompt</td></tr>
            <tr><td>7. Repeat</td><td>Until performance plateaus or target is met</td><td>Production prompt</td></tr>
          </tbody>
        </table>
        <div class="tip-box">
          <strong>Common error categories to look for:</strong> Hallucination (invented facts), format deviation (wrong structure), scope creep (answering beyond the task), truncation (cut off before complete), refusal (unnecessary safety triggers).
        </div>
      </div>

      <div class="content-card">
        <h2>14.6 Prompt Versioning</h2>
        <p>Treat prompts as code — version, test, and review them:</p>
        <div class="code-block-wrap">
          <button class="copy-btn" onclick="copyCode(this)">Copy</button>
          <pre><code># prompts/ticket_classifier/v3.txt
# Changelog:
# v1: Basic zero-shot (72% accuracy)
# v2: Added output schema (81% accuracy)
# v3: Added 4 few-shot examples (89% accuracy)
# Test suite: tests/ticket_classifier_test.json (50 cases)
# Last eval: 2025-03-15

System: You are a customer support ticket classifier.
# ... rest of prompt</code></pre>
        </div>
        <p>Store prompts in a dedicated directory in your repository. Track performance metrics alongside each version. Never silently update a production prompt without running the full test suite.</p>
      </div>

      <div class="content-card">
        <h2>L14 Summary</h2>
        <div class="summary-grid">
          <div class="summary-item"><span class="summary-icon">&#128202;</span><h4>Metrics First</h4><p>Define success before writing the first prompt. Choose metrics that match your actual task.</p></div>
          <div class="summary-item"><span class="summary-icon">&#9878;</span><h4>LLM-as-Judge</h4><p>Scale evaluation with Claude grading Claude. Works when ground truth is unavailable.</p></div>
          <div class="summary-item"><span class="summary-icon">&#128300;</span><h4>A/B Testing</h4><p>Always compare on the same test set. Multiple trials per case to reduce variance.</p></div>
          <div class="summary-item"><span class="summary-icon">&#128196;</span><h4>Version Control</h4><p>Prompts are code. Git-track them with performance metadata alongside each version.</p></div>
        </div>
      </div>

    </div>
  </section>
"""

# ─────────────────────────────────────── L15 ────────────────────────────────
L15 = r"""
  <!-- ═══════════════ L15 ═══════════════ -->
  <section class="lecture" data-lec="L15">
    <div class="lec-hero">
      <div class="lec-hero-inner">
        <span class="unit-tag">Unit 2 &middot; L15</span>
        <h1>Workshop: Prompt Optimisation Lab</h1>
        <p class="lec-sub">Hands-on practice: writing, testing, and improving prompts end-to-end</p>
        <div class="lec-meta"><span>&#9200; 1 Hour</span><span>&#128218; CO2</span><span>&#127919; Applied Lab</span></div>
      </div>
    </div>
    <div class="lec-body">

      <div class="content-card">
        <h2>15.1 Lab Overview</h2>
        <p>This workshop consolidates all Unit 2 techniques into a structured lab session. You will work through three progressively complex prompt engineering challenges, applying the full cycle: write baseline, measure, analyse failures, iterate, and verify improvement.</p>
        <div class="concept-grid">
          <div class="concept-box" style="border-color:var(--teal)">
            <h4>Lab A</h4>
            <p>Sentiment classifier with structured JSON output. Target: 95%+ accuracy on a 20-case test set.</p>
          </div>
          <div class="concept-box" style="border-color:var(--gold)">
            <h4>Lab B</h4>
            <p>Multi-step reasoning: contract risk extraction. Identify and score clauses with explanations.</p>
          </div>
          <div class="concept-box" style="border-color:var(--green)">
            <h4>Lab C</h4>
            <p>Persona-driven chatbot: technical support agent with constrained tone, format, and escalation rules.</p>
          </div>
        </div>
      </div>

      <div class="content-card">
        <h2>15.2 Lab A: Sentiment Classifier</h2>
        <p>Build a multi-class sentiment classifier that returns structured JSON and handles edge cases.</p>
        <h3>Baseline Prompt (Start Here)</h3>
        <div class="code-block-wrap">
          <button class="copy-btn" onclick="copyCode(this)">Copy</button>
          <pre><code>Classify the sentiment of this text: {{TEXT}}</code></pre>
        </div>
        <h3>Target Output Schema</h3>
        <div class="code-block-wrap">
          <button class="copy-btn" onclick="copyCode(this)">Copy</button>
          <pre><code>{
  "label": "positive" | "negative" | "neutral" | "mixed",
  "confidence": 0.0 to 1.0,
  "aspects": [
    {"aspect": string, "sentiment": "pos"|"neg"|"neu"}
  ],
  "explanation": string  // 1 sentence
}</code></pre>
        </div>
        <h3>Test Cases (select 5 to start)</h3>
        <table class="info-table">
          <thead><tr><th>#</th><th>Text</th><th>Expected Label</th></tr></thead>
          <tbody>
            <tr><td>1</td><td>Great product, terrible shipping!</td><td>mixed</td></tr>
            <tr><td>2</td><td>The battery lasts all day.</td><td>positive</td></tr>
            <tr><td>3</td><td>Item arrived. Works.</td><td>neutral</td></tr>
            <tr><td>4</td><td>Completely broken, never buying again.</td><td>negative</td></tr>
            <tr><td>5</td><td>Love the design but the software is buggy.</td><td>mixed</td></tr>
          </tbody>
        </table>
        <div class="tip-box">
          <strong>Iteration guide:</strong> If the model produces positive when mixed is expected, add a "mixed" definition and one few-shot example. If JSON is malformed, seed the assistant turn with <code>{"</code>.
        </div>
      </div>

      <div class="content-card">
        <h2>15.3 Lab B: Contract Risk Extraction</h2>
        <p>Extract risky clauses from legal text, classify risk level, and generate a structured risk report.</p>
        <h3>System Prompt Design</h3>
        <div class="code-block-wrap">
          <button class="copy-btn" onclick="copyCode(this)">Copy</button>
          <pre><code>You are a legal risk analyst. Your job is to:
1. Read contract clauses provided by the user
2. Identify potential risks for the CLIENT party
3. Score each risk: HIGH / MEDIUM / LOW
4. Explain why it is risky in plain English

Return a JSON array. Each element:
{
  "clause_text": "exact quote",
  "risk_level": "HIGH"|"MEDIUM"|"LOW",
  "risk_category": "Liability"|"IP"|"Payment"|"Termination"|"Other",
  "explanation": "1-2 sentence plain English explanation",
  "suggested_fix": "brief suggestion to mitigate"
}</code></pre>
        </div>
        <h3>Sample Contract Clause to Test</h3>
        <div class="code-block-wrap">
          <button class="copy-btn" onclick="copyCode(this)">Copy</button>
          <pre><code>"The Client grants the Vendor a perpetual, irrevocable, worldwide,
royalty-free license to use, reproduce, modify, and distribute any
materials provided by the Client in connection with the Services,
including the right to sublicense such rights to third parties."</code></pre>
        </div>
        <div class="warning-box">
          <strong>Expected output:</strong> HIGH risk, IP category — this clause gives the vendor unlimited rights to client materials forever. A good prompt should catch this and suggest limiting the license to "solely for performing the Services."
        </div>
      </div>

      <div class="content-card">
        <h2>15.4 Lab C: Technical Support Persona</h2>
        <p>Build a full support agent persona with escalation logic, tone control, and structured response format.</p>
        <h3>Complete Persona Prompt</h3>
        <div class="code-block-wrap">
          <button class="copy-btn" onclick="copyCode(this)">Copy</button>
          <pre><code>You are Aria, a Level 1 technical support specialist for CloudStore.

Identity:
- Friendly but efficient. No small talk beyond a brief greeting.
- Always acknowledge the issue before attempting to solve it.

Response format (always follow exactly):
[ISSUE IDENTIFIED]: one-sentence restatement
[STEPS TO TRY]:
  1. ...
  2. ...
[EXPECTED OUTCOME]: what the user should see after following steps
[ESCALATE IF]: condition under which user should contact L2 support

Rules:
- Maximum 150 words per response
- Never speculate about hardware failures — escalate instead
- Always end with: "Did that help? [YES] / [NO]"
- If user says NO: escalate with ticket number format TKT-{random 5 digits}

Do NOT:
- Promise things you cannot guarantee
- Mention competitors
- Use phrases: "Great question!", "Absolutely!"</code></pre>
        </div>
        <h3>Test Scenarios</h3>
        <table class="info-table">
          <thead><tr><th>Scenario</th><th>What to Check</th></tr></thead>
          <tbody>
            <tr><td>"My app won't load on Android."</td><td>Format compliance, tone, step clarity</td></tr>
            <tr><td>"I've tried everything, nothing works."</td><td>Escalation trigger, TKT format</td></tr>
            <tr><td>"Is this a hardware problem?"</td><td>Should NOT speculate, should escalate</td></tr>
            <tr><td>User says "NO" to "Did that help?"</td><td>Proper escalation with ticket number</td></tr>
          </tbody>
        </table>
      </div>

      <div class="content-card">
        <h2>15.5 Lab Debrief: Common Findings</h2>
        <table class="info-table">
          <thead><tr><th>Issue Found</th><th>Root Cause</th><th>Fix</th></tr></thead>
          <tbody>
            <tr><td>Wrong label on "mixed" sentiment</td><td>No definition of "mixed" provided</td><td>Add explicit definition + 1-2 few-shot examples</td></tr>
            <tr><td>JSON missing fields</td><td>Schema not explicit about required vs optional</td><td>Mark all fields as required; add "null" as allowed value</td></tr>
            <tr><td>Aria uses "Absolutely!" anyway</td><td>Negative constraint not specific enough</td><td>Add: "These exact phrases are forbidden: [list]"</td></tr>
            <tr><td>Risk level too conservative (all HIGH)</td><td>No calibration examples provided</td><td>Add 1 example each for HIGH, MEDIUM, LOW</td></tr>
            <tr><td>Response exceeds 150 words</td><td>Word limit ignored</td><td>Add: "Count your words. If over 150, revise before responding."</td></tr>
          </tbody>
        </table>
      </div>

      <div class="content-card">
        <h2>15.6 Unit 2 Capstone: What You Can Now Do</h2>
        <p>Completing Unit 2 means you can architect reliable prompt-based AI features from scratch. Here is the capability map:</p>
        <div class="summary-grid">
          <div class="summary-item"><span class="summary-icon">&#128161;</span><h4>Zero &amp; Few-Shot</h4><p>Choose the right demonstration strategy for any task type and data availability.</p></div>
          <div class="summary-item"><span class="summary-icon">&#129504;</span><h4>Chain-of-Thought</h4><p>Activate step-by-step reasoning for complex problems. Use extended thinking for hardest tasks.</p></div>
          <div class="summary-item"><span class="summary-icon">&#127775;</span><h4>Persona Design</h4><p>Build consistent, multi-turn AI characters with controlled tone and communication rules.</p></div>
          <div class="summary-item"><span class="summary-icon">&#123;&#125;</span><h4>Structured Output</h4><p>Produce schema-validated JSON, XML, and custom formats for downstream systems.</p></div>
          <div class="summary-item"><span class="summary-icon">&#128084;</span><h4>Context Management</h4><p>Handle long sessions with summarisation, chunking, and hierarchical memory.</p></div>
          <div class="summary-item"><span class="summary-icon">&#128202;</span><h4>Evaluation &amp; Iteration</h4><p>Measure prompt quality systematically and improve it with A/B testing and LLM-as-judge.</p></div>
        </div>
      </div>

    </div>
  </section>
"""

# ─────────────────────────── Closing JS + HTML ──────────────────────────────
CLOSING = r"""
</main><!-- end main-content -->

<script>
// Navigation
const links = document.querySelectorAll('.nav-links a[data-lec]');
const sections = document.querySelectorAll('section.lecture');

function showSection(id) {
  sections.forEach(s => s.classList.remove('active'));
  links.forEach(l => l.classList.remove('active'));
  const target = document.querySelector('section[data-lec="' + id + '"]');
  if (target) target.classList.add('active');
  const link = document.querySelector('a[data-lec="' + id + '"]');
  if (link) link.classList.add('active');
  window.scrollTo(0, 0);
}

links.forEach(link => {
  link.addEventListener('click', e => {
    e.preventDefault();
    showSection(link.dataset.lec);
  });
});

// Show L08 by default
showSection('L08');

// Search
const searchInput = document.getElementById('search-input');
searchInput && searchInput.addEventListener('input', function() {
  const q = this.value.toLowerCase().trim();
  if (!q) { showSection('L08'); return; }
  let firstMatch = null;
  sections.forEach(s => {
    const text = s.textContent.toLowerCase();
    if (text.includes(q)) {
      if (!firstMatch) firstMatch = s.dataset.lec;
    }
  });
  if (firstMatch) showSection(firstMatch);
});

// Theme toggle
const themeBtn = document.getElementById('theme-toggle');
themeBtn && themeBtn.addEventListener('click', () => {
  document.body.classList.toggle('light-mode');
  themeBtn.textContent = document.body.classList.contains('light-mode') ? '🌙' : '☀️';
});

// Copy code
function copyCode(btn) {
  const code = btn.nextElementSibling.textContent;
  navigator.clipboard.writeText(code).then(() => {
    btn.textContent = 'Copied!';
    setTimeout(() => btn.textContent = 'Copy', 2000);
  });
}
</script>
</body>
</html>
"""

with open(out, 'a') as f:
    f.write(L09)
    print("L09 written")
    f.write(L10)
    print("L10 written")
    f.write(L11)
    print("L11 written")
    f.write(L12)
    print("L12 written")
    f.write(L13)
    print("L13 written")
    f.write(L14)
    print("L14 written")
    f.write(L15)
    print("L15 written")
    f.write(CLOSING)
    print("Closing written")

print("DONE — all sections appended.")
