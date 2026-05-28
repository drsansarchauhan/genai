from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY

BRAND   = colors.HexColor('#1a3a6b')
ACCENT  = colors.HexColor('#c0392b')
LIGHT   = colors.HexColor('#dce8f7')
LIGHT2  = colors.HexColor('#f0f4fa')
GREEN   = colors.HexColor('#166534')
BGGREEN = colors.HexColor('#dcfce7')
MUTED   = colors.HexColor('#6c757d')
WHITE   = colors.white

def build_styles():
    s = getSampleStyleSheet()
    def add(name, **kw):
        s.add(ParagraphStyle(name=name, **kw))
    add('CourseHeader', fontName='Helvetica-Bold', fontSize=10, textColor=BRAND, alignment=TA_CENTER)
    add('DocTitle',     fontName='Helvetica-Bold', fontSize=18, textColor=BRAND, spaceAfter=4, alignment=TA_CENTER)
    add('DocSubtitle',  fontName='Helvetica',      fontSize=13, textColor=ACCENT, spaceAfter=16, alignment=TA_CENTER)
    add('SectionHead',  fontName='Helvetica-Bold', fontSize=13, textColor=BRAND, spaceBefore=14, spaceAfter=6,
        borderPad=4, borderColor=BRAND, borderWidth=0)
    add('QHead',        fontName='Helvetica-Bold', fontSize=11.5, textColor=BRAND, spaceBefore=10, spaceAfter=4)
    add('Body',         fontName='Helvetica',      fontSize=10.5, leading=15, textColor=colors.HexColor('#1a1a2e'), spaceAfter=4)
    add('BodyItalic',   fontName='Helvetica-Oblique', fontSize=10.5, leading=15, textColor=colors.HexColor('#444444'), spaceAfter=4)
    add('BulletItem',   fontName='Helvetica',      fontSize=10.5, leading=15, leftIndent=16, firstLineIndent=-10, spaceAfter=3)
    add('SmallNote',    fontName='Helvetica-Oblique', fontSize=9.5, textColor=MUTED, spaceBefore=6)
    add('AnswerKey',    fontName='Helvetica',      fontSize=10, textColor=GREEN, leading=14, leftIndent=12,
        backColor=BGGREEN, borderPad=4)
    add('MCQ_Correct',  fontName='Helvetica-Bold', fontSize=10.5, textColor=GREEN, leading=15, leftIndent=16, firstLineIndent=-10)
    add('MCQ_Option',   fontName='Helvetica',      fontSize=10.5, leading=15, leftIndent=16, firstLineIndent=-10)
    return s

styles = build_styles()

def header_block(title, sub, code, marks, co, page_story):
    """Add standard header to a page_story list."""
    page_story.append(Paragraph('CSAI601 — Generative AI with Claude  |  B.Tech CS/IT', styles['CourseHeader']))
    page_story.append(HRFlowable(width='100%', thickness=1.5, color=BRAND, spaceAfter=8))
    page_story.append(Paragraph(title, styles['DocTitle']))
    page_story.append(Paragraph(sub, styles['DocSubtitle']))
    info = [
        ['Course Code: CSAI601', f'Assessment: {code}', f'Total Marks: {marks}', f'CO Mapped: {co}']
    ]
    t = Table(info, colWidths=[1.8*inch, 1.9*inch, 1.8*inch, 2.0*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0),(-1,-1), LIGHT),
        ('TEXTCOLOR',  (0,0),(-1,-1), BRAND),
        ('FONT',       (0,0),(-1,-1), 'Helvetica-Bold', 9.5),
        ('ALIGN',      (0,0),(-1,-1), 'CENTER'),
        ('BOX',        (0,0),(-1,-1), 0.5, BRAND),
        ('INNERGRID',  (0,0),(-1,-1), 0.5, BRAND),
        ('ROWBACKGROUNDS', (0,0),(-1,-1), [LIGHT]),
        ('TOPPADDING',  (0,0),(-1,-1), 5),
        ('BOTTOMPADDING',(0,0),(-1,-1), 5),
    ]))
    page_story.append(t)
    page_story.append(Spacer(1, 12))

def q(num, text):
    return Paragraph(f'<b>Q{num}.</b> {text}', styles['QHead'])

def body(text):
    return Paragraph(text, styles['Body'])

def note(text):
    return Paragraph(text, styles['SmallNote'])

def option(letter, text, correct=False):
    style = styles['MCQ_Correct'] if correct else styles['MCQ_Option']
    mark = ' ✓' if correct else ''
    return Paragraph(f'{letter})  {text}{mark}', style)

def answer(text):
    return Paragraph(f'Model Answer: {text}', styles['AnswerKey'])

def sp(h=8):
    return Spacer(1, h)

def hr():
    return HRFlowable(width='100%', thickness=0.5, color=colors.HexColor('#dee2e6'), spaceBefore=8, spaceAfter=8)

# ══════════════════════════════════════════════════════════════
#  ASSIGNMENTS PDF
# ══════════════════════════════════════════════════════════════
story_a = []

# ── Assignment 1 ──
header_block('Assignment 1', 'LLM Architecture Analysis', 'Assignment 1/5', '4 Marks', 'CO1', story_a)
story_a.append(body('<b>Objective:</b> Demonstrate understanding of transformer architecture and Constitutional AI.'))
story_a.append(body('<b>Submission:</b> PDF report (max 6 pages) + Python script (.py file) via LMS. <b>Due:</b> End of Week 2.'))
story_a.append(hr())

story_a.append(q(1, '[1 Mark] Draw a detailed diagram of the Transformer Encoder block and label: multi-head attention, feed-forward network, residual connections, and layer normalisation. Explain the role of each component in 3–4 lines each.'))
story_a.append(sp())
story_a.append(q(2, '[1 Mark] Explain the self-attention mechanism mathematically. Given Query (Q), Key (K), and Value (V) matrices, derive the attention output. Why is the scaling factor 1/√d<sub>k</sub> necessary? What happens without it?'))
story_a.append(sp())
story_a.append(q(3, '[1 Mark] Compare RLHF and Constitutional AI (RLAIF) using a structured table with the following columns: (a) Training pipeline steps, (b) Data requirements, (c) Scalability, (d) Key limitation. After the table, write a 100-word paragraph arguing which approach is better and why.'))
story_a.append(sp())
story_a.append(q(4, '[1 Mark] Write a Python script that: (i) authenticates with the Anthropic API using an environment variable, (ii) sends a 5-message conversation history to Claude, (iii) prints the text response, (iv) prints input and output token counts, (v) handles rate limit errors with a 10-second retry. Submit the script and a screenshot of successful output.'))
story_a.append(note('Evaluation Rubric: Accuracy of diagram/explanation (35%), Mathematical correctness (25%), Depth of comparison (25%), Code functionality (15%)'))

story_a.append(PageBreak())

# ── Assignment 2 ──
header_block('Assignment 2', 'Prompt Engineering Portfolio', 'Assignment 2/5', '4 Marks', 'CO2', story_a)
story_a.append(body('<b>Objective:</b> Apply and compare different prompting strategies on real tasks.'))
story_a.append(body('<b>Submission:</b> Jupyter Notebook (.ipynb) + PDF report. <b>Due:</b> End of Week 4.'))
story_a.append(hr())

story_a.append(q(1, '[1 Mark] Choose any text classification task (sentiment analysis, topic classification, spam detection). Implement three versions: (a) zero-shot, (b) 3-shot, (c) 5-shot. Test each on 20 labelled samples. Report accuracy in a table. Analyse: does adding more examples always improve performance?'))
story_a.append(sp())
story_a.append(q(2, '[1 Mark] Design a Chain-of-Thought prompt for the following problem: "A train travels 120 km in 2 hours, stops for 30 minutes, then travels 80 km at 60 km/h. What is the total journey time?" Show: (a) the complete prompt, (b) Claude\'s full CoT response, (c) apply Self-Consistency (3 independent runs) and report the majority answer.'))
story_a.append(sp())
story_a.append(q(3, '[1 Mark] Write a system prompt that creates a "Senior Python Code Reviewer" persona. The persona should: identify bugs, suggest PEP 8 improvements, and rate code quality 1–10. Test on 3 code snippets of varying quality. Create a rubric to evaluate the persona\'s output quality.'))
story_a.append(sp())
story_a.append(q(4, '[1 Mark] Implement the ReAct framework manually (no agent loop code). Write a prompt that instructs Claude to interleave "Thought: ...", "Action: ...", "Observation: ..." steps to answer: "What is the population of the capital city of the country that won the 2022 FIFA World Cup?" Provide 3 fully worked examples.'))
story_a.append(note('Note: Use claude-3-haiku-20240307 to manage costs. Include token counts for each experiment.'))

story_a.append(PageBreak())

# ── Assignment 3 ──
header_block('Assignment 3', 'Build a Claude-Powered Application', 'Assignment 3/5', '4 Marks', 'CO3', story_a)
story_a.append(body('<b>Objective:</b> Develop a working application using the Claude API. Individual submission.'))
story_a.append(body('<b>Submission:</b> GitHub repo link + 2-page write-up. <b>Due:</b> End of Week 6.'))
story_a.append(hr())

story_a.append(body('<b>Choose ONE track:</b>'))
story_a.append(sp(4))
story_a.append(q(1, '[4 Marks — Track A: RAG Document Assistant] Build a system that: (i) ingests a PDF (min 20 pages), (ii) chunks it using a strategy you choose and justify, (iii) embeds chunks using any embedding model, (iv) stores vectors in ChromaDB or FAISS, (v) answers user questions using Claude with the top-3 retrieved chunks injected. Evaluate on 10 questions with and without RAG — measure answer quality.'))
story_a.append(sp())
story_a.append(q(1, '[4 Marks — Track B: Tool-Use Agent] Build a Claude agent with at least 3 tools (e.g., web search, calculator, weather API, Wikipedia). Implement the tool loop manually using the Anthropic SDK (no LangChain). Demonstrate 5 multi-step queries where Claude uses multiple tools in sequence.'))
story_a.append(sp())
story_a.append(q(1, '[4 Marks — Track C: Vision Application] Build an app that accepts image input and answers questions. Implement batch processing for 10 images. Add a Streamlit or Gradio web UI. Demonstrate at least 3 use cases (e.g., chart reading, document OCR, scene description).'))
story_a.append(sp(4))
story_a.append(body('<b>All tracks must include:</b> (a) Clean Python code with docstrings, (b) README with setup and run instructions, (c) Cost estimation for 100 API calls, (d) Error handling for at least 3 failure modes.'))

story_a.append(PageBreak())

# ── Assignment 4 ──
header_block('Assignment 4', 'AI Ethics Case Study Report', 'Assignment 4/5', '4 Marks', 'CO4', story_a)
story_a.append(body('<b>Objective:</b> Critically analyse a real-world AI ethics incident.'))
story_a.append(body('<b>Submission:</b> PDF report, max 8 pages. <b>Due:</b> End of Week 8.'))
story_a.append(hr())

story_a.append(q(1, '[1 Mark] Select a documented AI ethics incident (not discussed in class). Write a 500-word case description covering: what happened, who was affected, what the technical root cause was, and what the company\'s response was. Include references.'))
story_a.append(sp())
story_a.append(q(2, '[1 Mark] Analyse the incident using TWO frameworks: (a) Anthropic\'s HHH (Helpful, Harmless, Honest) — rate the system on all three dimensions, and (b) EU AI Act risk categories — classify the system and justify. Does this system qualify as "high risk"? Why or why not?'))
story_a.append(sp())
story_a.append(q(3, '[1 Mark] Identify 3 specific technical changes that could have prevented the incident. For each change: describe the implementation, explain the trade-off it introduces, and rate its feasibility (Easy/Medium/Hard).'))
story_a.append(sp())
story_a.append(q(4, '[1 Mark] Design a Responsible AI Checklist (minimum 12 items, max 20) for a developer building a healthcare AI assistant powered by Claude. Organise by category: Data Governance, Model Behaviour, Deployment, Ongoing Monitoring. Each item must be actionable (yes/no checkable).'))

story_a.append(PageBreak())

# ── Assignment 5 ──
header_block('Assignment 5', 'Capstone Project Proposal & Architecture', 'Assignment 5/5', '4 Marks', 'CO5', story_a)
story_a.append(body('<b>Objective:</b> Plan the Capstone Project to be demonstrated in Week 15. Groups of 2–3 students.'))
story_a.append(body('<b>Submission:</b> PDF document + architecture diagram image. <b>Due:</b> End of Week 10.'))
story_a.append(hr())

story_a.append(q(1, '[1 Mark] Problem Statement: (a) Identify a real-world problem solvable with Claude. (b) Justify why an LLM is the appropriate solution vs a rule-based system, traditional ML, or manual approach. (c) Define 3 measurable success criteria (e.g., "answers 80% of test questions correctly").'))
story_a.append(sp())
story_a.append(q(2, '[1 Mark] System Architecture: Draw a complete architecture diagram showing: User Interface, Claude API, all tools/databases/external APIs, caching layer, deployment environment. Label all data flows with arrows. Describe each component in 2–3 lines.'))
story_a.append(sp())
story_a.append(q(3, '[1 Mark] Prompt Design: Write the complete system prompt for your application. Write 2 example user messages with Claude\'s expected ideal response. Justify your prompting strategy (which technique and why).'))
story_a.append(sp())
story_a.append(q(4, '[1 Mark] Ethics & Risk Analysis: (a) Identify 3 ethical risks of your application. For each: describe the risk, rate severity (Low/Medium/High), and specify a technical mitigation. (b) Calculate estimated Claude API cost for 1,000 daily active users, each sending 5 queries of average 500 input tokens and 200 output tokens. State which model you\'ll use and why.'))

# write assignments PDF
doc_a = SimpleDocTemplate('/sessions/blissful-quirky-tesla/mnt/outputs/CSAI601_Assignments.pdf',
                           pagesize=letter, leftMargin=0.75*inch, rightMargin=0.75*inch,
                           topMargin=0.75*inch, bottomMargin=0.75*inch)
doc_a.build(story_a)
print('Assignments PDF written OK')

# ══════════════════════════════════════════════════════════════
#  QUIZZES PDF (Instructor Version with Answer Keys)
# ══════════════════════════════════════════════════════════════
story_q = []

def quiz_header(num, unit, co):
    story_q.append(Paragraph('CSAI601 — Generative AI with Claude  |  B.Tech CS/IT', styles['CourseHeader']))
    story_q.append(HRFlowable(width='100%', thickness=1.5, color=BRAND, spaceAfter=8))
    story_q.append(Paragraph(f'Quiz {num}: {unit}', styles['DocTitle']))
    story_q.append(Paragraph(f'{co}  ·  2 Marks  ·  15 Minutes  ·  In-Class', styles['DocSubtitle']))
    info_data = [['Name:', '________________________________', 'Roll No.:', '_______________', 'Date:', '___________']]
    t = Table(info_data, colWidths=[0.55*inch, 2.1*inch, 0.7*inch, 1.3*inch, 0.5*inch, 1.1*inch])
    t.setStyle(TableStyle([
        ('FONT', (0,0), (-1,-1), 'Helvetica', 10),
        ('FONT', (0,0), (0,-1), 'Helvetica-Bold', 10),
        ('FONT', (2,0), (2,-1), 'Helvetica-Bold', 10),
        ('FONT', (4,0), (4,-1), 'Helvetica-Bold', 10),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story_q.append(t)
    story_q.append(HRFlowable(width='100%', thickness=0.5, color=MUTED, spaceBefore=8, spaceAfter=8))
    story_q.append(body('<i>Instructions: Circle the letter of the best answer. Q5 requires a written answer (3–5 lines).</i>'))
    story_q.append(note('★ INSTRUCTOR COPY — Answer key shown in green. Remove for student distribution.'))
    story_q.append(sp(8))

# ── Quiz 1 ──
quiz_header(1, 'Foundations of Large Language Models', 'CO1')
story_q.append(q(1, 'In the self-attention mechanism, the scaling factor 1/√d<sub>k</sub> is used to:'))
story_q.append(option('A', 'Prevent gradient explosion during backpropagation'))
story_q.append(option('B', 'Prevent vanishingly small gradients when dot products grow large', correct=True))
story_q.append(option('C', 'Reduce overfitting to training examples'))
story_q.append(option('D', 'Decrease memory usage at inference time'))
story_q.append(hr())
story_q.append(q(2, 'Constitutional AI (CAI) differs from RLHF primarily because:'))
story_q.append(option('A', 'CAI requires more human labellers'))
story_q.append(option('B', 'CAI does not use reinforcement learning at all'))
story_q.append(option('C', 'CAI uses AI-generated feedback based on written principles instead of human preference labels', correct=True))
story_q.append(option('D', 'CAI only works with smaller models under 7B parameters'))
story_q.append(hr())
story_q.append(q(3, 'Which tokenisation method does Claude primarily use?'))
story_q.append(option('A', 'Character-level tokenisation'))
story_q.append(option('B', 'Word-level tokenisation'))
story_q.append(option('C', 'Byte-Pair Encoding (BPE)', correct=True))
story_q.append(option('D', 'Unigram language model tokenisation'))
story_q.append(hr())
story_q.append(q(4, 'Setting temperature = 0.0 in Claude\'s API produces:'))
story_q.append(option('A', 'Deterministic / greedy output — always the highest probability token', correct=True))
story_q.append(option('B', 'Uniform random sampling across the full vocabulary'))
story_q.append(option('C', 'Top-p = 0 sampling, blocking all output'))
story_q.append(option('D', 'The model refuses to generate any response'))
story_q.append(hr())
story_q.append(q(5, '[Short Answer — 3–5 lines] What is the HHH framework and why is it central to Claude?'))
story_q.append(answer('HHH stands for Helpful, Harmless, Honest — Anthropic\'s three core training objectives for Claude. Helpful: Claude must maximally assist users in completing their goals. Harmless: Claude must avoid producing outputs that cause physical, psychological, or societal harm. Honest: Claude must be truthful, calibrated in its uncertainty, and non-deceptive. Together these three properties operationalise Anthropic\'s mission of building safe and beneficial AI, and are directly encoded into the Constitutional AI training process.'))

story_q.append(PageBreak())

# ── Quiz 2 ──
quiz_header(2, 'Prompt Engineering', 'CO2')
story_q.append(q(1, '"Let\'s think step by step" is the trigger phrase for which prompting technique?'))
story_q.append(option('A', 'Few-shot prompting'))
story_q.append(option('B', 'Zero-shot Chain-of-Thought (CoT)', correct=True))
story_q.append(option('C', 'Self-consistency prompting'))
story_q.append(option('D', 'ReAct prompting'))
story_q.append(hr())
story_q.append(q(2, 'Self-consistency improves accuracy by:'))
story_q.append(option('A', 'Using a larger model for each query'))
story_q.append(option('B', 'Sampling multiple diverse reasoning chains and selecting the majority answer', correct=True))
story_q.append(option('C', 'Having the model critique its own output once'))
story_q.append(option('D', 'Adding more in-context examples'))
story_q.append(hr())
story_q.append(q(3, 'In the ReAct framework, the "Action" step refers to:'))
story_q.append(option('A', 'The model\'s final answer to the user'))
story_q.append(option('B', 'Human feedback on the model\'s output'))
story_q.append(option('C', 'A tool call or external operation triggered by the model', correct=True))
story_q.append(option('D', 'Rewriting the original prompt'))
story_q.append(hr())
story_q.append(q(4, 'Which of the following is NOT a direct benefit of structured output prompting?'))
story_q.append(option('A', 'Easier downstream parsing of model responses'))
story_q.append(option('B', 'Consistent, predictable response format'))
story_q.append(option('C', 'Better integration with APIs expecting JSON'))
story_q.append(option('D', 'Guaranteed elimination of hallucinations', correct=True))
story_q.append(hr())
story_q.append(q(5, '[Short Answer] Explain the difference between a system prompt and a user prompt in Claude.'))
story_q.append(answer('A system prompt is injected by the developer/operator before the conversation begins. It defines Claude\'s persona, task scope, constraints, tone, and output format. It is not visible to the end-user and frames how Claude should interpret all subsequent messages. A user prompt is the message sent by the end-user during the conversation. System prompts take precedence and act as persistent instructions. Example: a system prompt might say "You are a tax assistant. Only answer tax-related questions." while user prompts contain the actual questions.'))

story_q.append(PageBreak())

# ── Quiz 3 ──
quiz_header(3, 'Claude API & Applications', 'CO3')
story_q.append(q(1, 'In a RAG pipeline, the vector database is used to:'))
story_q.append(option('A', 'Store the LLM model weights'))
story_q.append(option('B', 'Store and retrieve document embeddings using similarity search', correct=True))
story_q.append(option('C', 'Cache API responses to reduce cost'))
story_q.append(option('D', 'Store multi-turn conversation history'))
story_q.append(hr())
story_q.append(q(2, 'When Claude\'s API returns stop_reason = "tool_use", the developer must:'))
story_q.append(option('A', 'Retry the API call with a higher temperature'))
story_q.append(option('B', 'Execute the requested tool and return its result as the next message', correct=True))
story_q.append(option('C', 'Increase the max_tokens parameter'))
story_q.append(option('D', 'Switch to a different Claude model'))
story_q.append(hr())
story_q.append(q(3, 'To pass an image to Claude\'s Vision API, it must be:'))
story_q.append(option('A', 'Encoded as UTF-8 text'))
story_q.append(option('B', 'Encoded as hexadecimal'))
story_q.append(option('C', 'Encoded as base64, or provided as a publicly accessible URL', correct=True))
story_q.append(option('D', 'Encoded as raw binary data'))
story_q.append(hr())
story_q.append(q(4, 'Claude\'s prompt caching feature primarily reduces:'))
story_q.append(option('A', 'Cost and latency for large, repeated context prefixes', correct=True))
story_q.append(option('B', 'Hallucination rate in model responses'))
story_q.append(option('C', 'The need for system prompts'))
story_q.append(option('D', 'Model size at inference time'))
story_q.append(hr())
story_q.append(q(5, '[Short Answer] What is wrong with this API call: messages=[{"role":"user","content":"Hi"},{"role":"user","content":"What can you do?"}]?'))
story_q.append(answer('The Claude API requires strictly alternating user/assistant turns. Two consecutive messages with role="user" are invalid and will result in an API error (400 Bad Request). The correct pattern is user → assistant → user → assistant. After the first user message "Hi", the developer must include the model\'s response (role="assistant") before sending the next user message. Fix: insert {"role": "assistant", "content": "Hello! How can I help you?"} between the two user messages.'))

story_q.append(PageBreak())

# ── Quiz 4 ──
quiz_header(4, 'Responsible AI & Ethics', 'CO4')
story_q.append(q(1, '"Extrinsic hallucination" in LLMs refers to:'))
story_q.append(option('A', 'Internal contradictions within a single model response'))
story_q.append(option('B', 'Generated content that cannot be verified from or contradicts the source document', correct=True))
story_q.append(option('C', 'Errors caused by low temperature sampling'))
story_q.append(option('D', 'Hallucinations in multilingual settings only'))
story_q.append(hr())
story_q.append(q(2, 'Under the EU AI Act, AI systems used in employment screening are classified as:'))
story_q.append(option('A', 'Minimal risk'))
story_q.append(option('B', 'Limited risk'))
story_q.append(option('C', 'High risk', correct=True))
story_q.append(option('D', 'Unacceptable risk'))
story_q.append(hr())
story_q.append(q(3, 'Which strategy is most effective at grounding Claude\'s answers to a specific document?'))
story_q.append(option('A', 'Increasing temperature to 1.5'))
story_q.append(option('B', 'Using the word "accurate" in the system prompt'))
story_q.append(option('C', 'RAG — injecting retrieved document chunks into the context', correct=True))
story_q.append(option('D', 'Using Claude-3-Opus instead of Haiku'))
story_q.append(hr())
story_q.append(q(4, 'A prompt injection attack aims to:'))
story_q.append(option('A', 'Overload the API server with too many requests'))
story_q.append(option('B', 'Override the developer\'s system prompt by embedding adversarial instructions in user input', correct=True))
story_q.append(option('C', 'Steal API keys embedded in API responses'))
story_q.append(option('D', 'Reduce the model\'s effective context window'))
story_q.append(hr())
story_q.append(q(5, '[Short Answer] What is the WinoBias benchmark and what does it measure?'))
story_q.append(answer('WinoBias is a benchmark dataset used to evaluate gender bias in NLP systems, specifically in coreference resolution. It contains sentence pairs testing both stereotypical associations (e.g., "the nurse... she") and anti-stereotypical associations (e.g., "the nurse... he"). A system that performs significantly better on stereotypical examples than anti-stereotypical ones exhibits gender bias. High disparity scores indicate the model relies on gender stereotypes rather than genuine linguistic cues.'))

story_q.append(PageBreak())

# ── Quiz 5 ──
quiz_header(5, 'Advanced Topics', 'CO5')
story_q.append(q(1, 'In the Model Context Protocol (MCP) architecture, an "MCP Server" is responsible for:'))
story_q.append(option('A', 'Running the Claude model weights locally on the user\'s machine'))
story_q.append(option('B', 'Exposing tools, resources, and capabilities (e.g., file system, database) to the LLM host', correct=True))
story_q.append(option('C', 'Managing user authentication and session tokens'))
story_q.append(option('D', 'Compressing and batching API requests for efficiency'))
story_q.append(hr())
story_q.append(q(2, 'In a multi-agent "orchestrator-worker" pattern, the orchestrator\'s primary role is:'))
story_q.append(option('A', 'Directly executing all tool calls'))
story_q.append(option('B', 'Planning tasks, delegating to worker agents, and aggregating results', correct=True))
story_q.append(option('C', 'Providing the user-facing UI layer'))
story_q.append(option('D', 'Monitoring API costs and triggering alerts'))
story_q.append(hr())
story_q.append(q(3, 'RAG is preferred over fine-tuning when:'))
story_q.append(option('A', 'The knowledge domain is very narrow and completely static'))
story_q.append(option('B', 'The knowledge base changes frequently and needs real-time updates', correct=True))
story_q.append(option('C', 'Inference latency is not a concern'))
story_q.append(option('D', 'Embedding models are not available'))
story_q.append(hr())
story_q.append(q(4, 'Claude\'s "extended thinking" mode is designed to improve performance on:'))
story_q.append(option('A', 'Short creative writing tasks'))
story_q.append(option('B', 'Image generation'))
story_q.append(option('C', 'Complex multi-step reasoning and mathematics problems', correct=True))
story_q.append(option('D', 'Real-time streaming applications'))
story_q.append(hr())
story_q.append(q(5, '[Short Answer] Name THREE strategies to reduce Claude API costs in a production application.'))
story_q.append(answer('(1) Prompt caching: Cache large, repeated system prompt prefixes so they are only processed once, reducing input token costs on subsequent calls. (2) Model tiering: Route simple queries to claude-3-haiku (cheapest) and reserve claude-3-5-sonnet or Opus for complex tasks that actually require it. (3) Output length control: Set max_tokens appropriately and use concise prompts to avoid unnecessarily long responses. Bonus strategies: Use the Batch API for non-real-time workloads (50% discount); compress or summarise conversation history to reduce context length.'))

# write quiz PDF
doc_q = SimpleDocTemplate('/sessions/blissful-quirky-tesla/mnt/outputs/CSAI601_Quizzes_InstructorKey.pdf',
                           pagesize=letter, leftMargin=0.75*inch, rightMargin=0.75*inch,
                           topMargin=0.75*inch, bottomMargin=0.75*inch)
doc_q.build(story_q)
print('Quizzes PDF written OK')
