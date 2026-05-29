import sys

out = '/sessions/blissful-quirky-tesla/mnt/outputs/CSAI601_Unit2_Notes.html'

content = """
  <!-- L09 -->
  <section class="lecture" data-lec="L09">
    <div class="lec-hero">
      <div class="lec-hero-inner">
        <span class="unit-tag">Unit 2 &middot; L09</span>
        <h1>Zero-Shot &amp; Few-Shot Prompting</h1>
        <p class="lec-sub">Learning to guide Claude without examples and with them</p>
        <div class="lec-meta">
          <span>60 min</span><span>CO2</span><span>Core Technique</span>
        </div>
      </div>
    </div>
    <div class="lec-body">

      <div class="content-card">
        <h2>9.1 The Prompting Spectrum</h2>
        <p>Before models see a single example from you, they already carry billions of training examples inside their weights. <strong>Zero-shot prompting</strong> exploits that prior knowledge directly; <strong>few-shot prompting</strong> steers it with handpicked demonstrations embedded in the prompt itself. Between these two poles lies a spectrum that every practitioner navigates daily.</p>
        <div class="concept-grid">
          <div class="concept-box" style="border-color:var(--teal)">
            <h4>Zero-Shot</h4>
            <p>No examples in the prompt. Pure instruction. Works when the task is unambiguous and well-represented in training data.</p>
          </div>
          <div class="concept-box" style="border-color:var(--gold)">
            <h4>One-Shot</h4>
            <p>One example to anchor format and style. Best when you need a specific output layout but only have one good demonstration.</p>
          </div>
          <div class="concept-box" style="border-color:var(--green)">
            <h4>Few-Shot (2-8)</h4>
            <p>Several demonstrations showing input-to-output pairs. Model generalises the pattern to new inputs.</p>
          </div>
          <div class="concept-box" style="border-color:var(--purple)">
            <h4>Many-Shot</h4>
            <p>Dozens to hundreds of examples in a long-context window. Approaches fine-tuning quality for well-scoped tasks.</p>
          </div>
        </div>
      </div>

      <div class="content-card">
        <h2>9.2 Zero-Shot Prompting in Practice</h2>
        <p>Zero-shot works because modern LLMs generalise from pre-training. The key is framing the task completely and unambiguously in a single instruction block.</p>
        <h3>Anatomy of a Strong Zero-Shot Prompt</h3>
        <table class="info-table">
          <thead><tr><th>Component</th><th>Weak Version</th><th>Strong Version</th></tr></thead>
          <tbody>
            <tr><td>Task name</td><td>Tell me about this</td><td>Summarise this product review in 2 sentences</td></tr>
            <tr><td>Output format</td><td>Give me keywords</td><td>List 5 keywords, comma-separated, lowercase</td></tr>
            <tr><td>Audience</td><td>Explain neural nets</td><td>Explain neural nets to a high-school student with no maths background</td></tr>
            <tr><td>Constraints</td><td>Write an email</td><td>Write a 3-sentence follow-up email, professional tone, no jargon</td></tr>
            <tr><td>Role</td><td>Check my code</td><td>Act as a senior Python engineer. Review this code for security vulnerabilities</td></tr>
          </tbody>
        </table>
        <h3>When Zero-Shot Fails</h3>
        <div class="warning-box">
          <strong>Zero-shot breaks down when:</strong>
          <ul>
            <li>The task requires a very specific format (JSON schemas, proprietary templates)</li>
            <li>The domain is highly specialised and under-represented in training data</li>
            <li>Desired style is idiosyncratic (your company voice, a particular author style)</li>
            <li>The task involves multi-step reasoning with precise intermediate steps</li>
          </ul>
          <p>In these cases, move to few-shot or chain-of-thought prompting.</p>
        </div>
      </div>

      <div class="content-card">
        <h2>9.3 Few-Shot Prompting: Mechanics</h2>
        <p>Few-shot prompting embeds worked examples before the actual task. Claude learns the format, tone, and reasoning style from these demonstrations.</p>
        <h3>Example: Ticket Classification</h3>
        <pre><code>System: Classify customer support tickets into: Billing, Technical, Shipping, Other.
