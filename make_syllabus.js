const docx = require('/usr/local/lib/node_modules_global/lib/node_modules/docx');
const fs = require('fs');

const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Header, Footer, AlignmentType, HeadingLevel, BorderStyle, WidthType,
  ShadingType, VerticalAlign, PageNumber, PageBreak, LevelFormat,
  TableOfContents
} = docx;

const BRAND   = '1a3a6b';
const ACCENT  = 'c0392b';
const LIGHT   = 'dce8f7';
const BORDER_COLOR = 'aac4e0';

const border = { style: BorderStyle.SINGLE, size: 4, color: BORDER_COLOR };
const allBorders = { top: border, bottom: border, left: border, right: border };

const hdrBorder = { style: BorderStyle.SINGLE, size: 4, color: BRAND };
const allHdrBorders = { top: hdrBorder, bottom: hdrBorder, left: hdrBorder, right: hdrBorder };

function headBg(text) {
  return new TableCell({
    borders: allHdrBorders,
    shading: { fill: BRAND, type: ShadingType.CLEAR },
    margins: { top: 80, bottom: 80, left: 140, right: 140 },
    children: [new Paragraph({ children: [new TextRun({ text, bold: true, color: 'FFFFFF', size: 22, font: 'Arial' })] })]
  });
}
function cell(text, { shade = false, bold = false, center = false } = {}) {
  return new TableCell({
    borders: allBorders,
    shading: shade ? { fill: 'f0f4fa', type: ShadingType.CLEAR } : undefined,
    margins: { top: 60, bottom: 60, left: 120, right: 120 },
    children: [new Paragraph({
      alignment: center ? AlignmentType.CENTER : AlignmentType.LEFT,
      children: [new TextRun({ text, bold, size: 20, font: 'Arial', color: '1a1a2e' })]
    })]
  });
}

function h1(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    spacing: { before: 280, after: 120 },
    border: { bottom: { style: BorderStyle.THICK, size: 6, color: BRAND, space: 4 } },
    children: [new TextRun({ text, bold: true, size: 28, color: BRAND, font: 'Arial' })]
  });
}
function h2(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    spacing: { before: 180, after: 80 },
    children: [new TextRun({ text, bold: true, size: 24, color: ACCENT, font: 'Arial' })]
  });
}
function p(text, opts = {}) {
  return new Paragraph({
    spacing: { before: 60, after: 60 },
    children: [new TextRun({ text, size: 20, font: 'Arial', color: '1a1a2e', ...opts })]
  });
}
function bullet(text) {
  return new Paragraph({
    numbering: { reference: 'bullets', level: 0 },
    spacing: { before: 40, after: 40 },
    children: [new TextRun({ text, size: 20, font: 'Arial', color: '1a1a2e' })]
  });
}
function spacer(before = 80) {
  return new Paragraph({ spacing: { before, after: 0 }, children: [] });
}

const doc = new Document({
  numbering: {
    config: [
      {
        reference: 'bullets',
        levels: [{
          level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 560, hanging: 280 } } }
        }]
      }
    ]
  },
  styles: {
    default: {
      document: { run: { font: 'Arial', size: 20 } }
    },
    paragraphStyles: [
      { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true,
        run: { size: 28, bold: true, font: 'Arial', color: BRAND },
        paragraph: { spacing: { before: 280, after: 120 }, outlineLevel: 0 }
      },
      { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true,
        run: { size: 24, bold: true, font: 'Arial', color: ACCENT },
        paragraph: { spacing: { before: 180, after: 80 }, outlineLevel: 1 }
      }
    ]
  },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 },
        margin: { top: 1080, right: 1080, bottom: 1080, left: 1080 }
      }
    },
    headers: {
      default: new Header({
        children: [new Paragraph({
          alignment: AlignmentType.RIGHT,
          border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: BRAND, space: 1 } },
          children: [
            new TextRun({ text: 'CSAI601 — Generative AI with Claude  |  Course Syllabus', size: 18, color: BRAND, font: 'Arial' })
          ]
        })]
      })
    },
    footers: {
      default: new Footer({
        children: [new Paragraph({
          alignment: AlignmentType.CENTER,
          border: { top: { style: BorderStyle.SINGLE, size: 4, color: BORDER_COLOR, space: 1 } },
          children: [
            new TextRun({ text: 'B.Tech CS/IT · 3rd Year Elective · Page ', size: 18, color: '6c757d', font: 'Arial' }),
            new TextRun({ children: [PageNumber.CURRENT], size: 18, color: '6c757d', font: 'Arial' }),
            new TextRun({ text: ' of ', size: 18, color: '6c757d', font: 'Arial' }),
            new TextRun({ children: [PageNumber.TOTAL_PAGES], size: 18, color: '6c757d', font: 'Arial' }),
          ]
        })]
      })
    },
    children: [
      // ─── TITLE BLOCK ───────────────────────────────────────────────
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 120, after: 60 },
        children: [new TextRun({ text: 'COURSE SYLLABUS', bold: true, size: 36, color: BRAND, font: 'Arial' })] }),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 0, after: 0 },
        border: { bottom: { style: BorderStyle.THICK, size: 8, color: ACCENT, space: 4 } },
        children: [new TextRun({ text: 'CSAI601: Generative AI with Claude', size: 30, bold: true, color: ACCENT, font: 'Arial' })] }),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 100, after: 160 },
        children: [new TextRun({ text: 'Principles, Prompt Engineering & Application Development', size: 22, italics: true, color: '444444', font: 'Arial' })] }),

      // ─── COURSE INFO TABLE ─────────────────────────────────────────
      new Table({
        width: { size: 10080, type: WidthType.DXA },
        columnWidths: [2520, 2520, 2520, 2520],
        rows: [
          new TableRow({ children: [headBg('Course Code'), headBg('Credits'), headBg('L-T-P'), headBg('Semester')] }),
          new TableRow({ children: [cell('CSAI601'), cell('3'), cell('3-0-0'), cell('VI / VII')] }),
          new TableRow({ children: [headBg('Department'), headBg('Program'), headBg('Year'), headBg('Total Hours')] }),
          new TableRow({ children: [cell('Computer Science & IT'), cell('B.Tech CS / IT'), cell('3rd Year'), cell('36')] }),
        ]
      }),

      spacer(200),

      // ─── COURSE DESCRIPTION ────────────────────────────────────────
      h1('1. Course Description'),
      p('This course introduces 3rd-year B.Tech CS/IT students to Generative AI through the lens of Claude, Anthropic\'s large language model. Students gain theoretical understanding of transformer architecture and Constitutional AI, develop practical prompt engineering skills, build real applications using the Claude API, and critically evaluate AI systems for safety and ethics. The course is designed to make students industry-ready in the rapidly evolving Generative AI domain.'),

      spacer(),
      // ─── PREREQUISITES ─────────────────────────────────────────────
      h1('2. Prerequisites'),
      bullet('Basic Python programming (loops, functions, classes, file I/O)'),
      bullet('Introductory Machine Learning concepts (regression, classification)'),
      bullet('Fundamentals of neural networks (forward pass, backpropagation)'),
      bullet('Data Structures and Algorithms (arrays, dictionaries, graphs)'),
      bullet('Recommended: DBMS basics for Unit 3 (RAG with vector databases)'),

      spacer(),
      // ─── COURSE OUTCOMES ──────────────────────────────────────────
      h1('3. Course Outcomes (COs)'),
      p('On successful completion of this course, students will be able to:'),
      spacer(80),
      new Table({
        width: { size: 10080, type: WidthType.DXA },
        columnWidths: [700, 7180, 2200],
        rows: [
          new TableRow({ children: [headBg('CO'), headBg('Outcome Statement'), headBg("Bloom's Level")] }),
          new TableRow({ children: [
            cell('CO1', { shade: false, bold: true }),
            cell('Understand the evolution of NLP, transformer architecture, and how Claude is built upon Constitutional AI principles.'),
            cell('L1 – Remember / L2 – Understand', { center: true })
          ]}),
          new TableRow({ children: [
            cell('CO2', { shade: true, bold: true }),
            cell('Apply systematic prompt engineering strategies—zero-shot, few-shot, CoT, role-play—to design effective LLM interactions.', { shade: true }),
            cell('L3 – Apply', { shade: true, center: true })
          ]}),
          new TableRow({ children: [
            cell('CO3', { bold: true }),
            cell('Develop functional applications using the Claude API, including chatbots, tool-use agents, and RAG pipelines.'),
            cell('L3 – Apply / L4 – Analyze', { center: true })
          ]}),
          new TableRow({ children: [
            cell('CO4', { shade: true, bold: true }),
            cell('Evaluate AI systems for bias, hallucinations, safety risks, and ethical implications using established frameworks.', { shade: true }),
            cell('L4 – Analyze / L5 – Evaluate', { shade: true, center: true })
          ]}),
          new TableRow({ children: [
            cell('CO5', { bold: true }),
            cell('Design and implement end-to-end intelligent solutions integrating advanced Claude capabilities such as multi-modal input and agentic workflows.'),
            cell('L5 – Evaluate / L6 – Create', { center: true })
          ]}),
        ]
      }),

      spacer(),
      // ─── CO-PO MAPPING ─────────────────────────────────────────────
      h1('4. CO–PO Mapping'),
      p('Correlation Level: 3 = High, 2 = Medium, 1 = Low, blank = No significant correlation'),
      spacer(80),
      new Table({
        width: { size: 10080, type: WidthType.DXA },
        columnWidths: [700, 560, 560, 560, 560, 560, 560, 560, 560, 560, 560, 560, 560, 840, 840],
        rows: [
          new TableRow({ children: [
            headBg('CO\\PO'), headBg('PO1'), headBg('PO2'), headBg('PO3'), headBg('PO4'),
            headBg('PO5'), headBg('PO6'), headBg('PO7'), headBg('PO8'), headBg('PO9'),
            headBg('PO10'), headBg('PO11'), headBg('PO12'), headBg('PSO1'), headBg('PSO2')
          ]}),
          new TableRow({ children: [cell('CO1',{bold:true}), cell('3',{center:true}), cell('2',{center:true}), cell('',{center:true}), cell('1',{center:true}), cell('2',{center:true}), cell('',{center:true}), cell('',{center:true}), cell('',{center:true}), cell('',{center:true}), cell('1',{center:true}), cell('',{center:true}), cell('3',{center:true}), cell('2',{center:true}), cell('3',{center:true})] }),
          new TableRow({ children: [cell('CO2',{bold:true,shade:true}), cell('2',{center:true,shade:true}), cell('3',{center:true,shade:true}), cell('3',{center:true,shade:true}), cell('2',{center:true,shade:true}), cell('3',{center:true,shade:true}), cell('',{center:true,shade:true}), cell('',{center:true,shade:true}), cell('',{center:true,shade:true}), cell('1',{center:true,shade:true}), cell('2',{center:true,shade:true}), cell('',{center:true,shade:true}), cell('2',{center:true,shade:true}), cell('3',{center:true,shade:true}), cell('2',{center:true,shade:true})] }),
          new TableRow({ children: [cell('CO3',{bold:true}), cell('2',{center:true}), cell('2',{center:true}), cell('3',{center:true}), cell('2',{center:true}), cell('3',{center:true}), cell('1',{center:true}), cell('',{center:true}), cell('',{center:true}), cell('2',{center:true}), cell('2',{center:true}), cell('2',{center:true}), cell('2',{center:true}), cell('3',{center:true}), cell('3',{center:true})] }),
          new TableRow({ children: [cell('CO4',{bold:true,shade:true}), cell('1',{center:true,shade:true}), cell('2',{center:true,shade:true}), cell('1',{center:true,shade:true}), cell('3',{center:true,shade:true}), cell('1',{center:true,shade:true}), cell('3',{center:true,shade:true}), cell('2',{center:true,shade:true}), cell('3',{center:true,shade:true}), cell('1',{center:true,shade:true}), cell('2',{center:true,shade:true}), cell('',{center:true,shade:true}), cell('2',{center:true,shade:true}), cell('1',{center:true,shade:true}), cell('1',{center:true,shade:true})] }),
          new TableRow({ children: [cell('CO5',{bold:true}), cell('2',{center:true}), cell('3',{center:true}), cell('3',{center:true}), cell('2',{center:true}), cell('3',{center:true}), cell('2',{center:true}), cell('1',{center:true}), cell('1',{center:true}), cell('3',{center:true}), cell('2',{center:true}), cell('2',{center:true}), cell('3',{center:true}), cell('3',{center:true}), cell('3',{center:true})] }),
        ]
      }),
      spacer(80),
      p('PO1: Engineering Knowledge · PO2: Problem Analysis · PO3: Design/Development · PO4: Investigation · PO5: Modern Tools · PO6: Engineer & Society · PO7: Environment · PO8: Ethics · PO9: Team Work · PO10: Communication · PO11: Project Management · PO12: Lifelong Learning · PSO1: Software Development · PSO2: Computation', { italics: true, color: '6c757d' }),

      spacer(),
      new Paragraph({ children: [new PageBreak()] }),

      // ─── UNIT-WISE SYLLABUS ────────────────────────────────────────
      h1('5. Unit-wise Syllabus'),
      spacer(60),
      h2('Unit 1: Foundations of Large Language Models (7 Hours)'),
      p('History of AI and NLP: rule-based systems to statistical to neural approaches. Word embeddings (Word2Vec, GloVe). Attention mechanism. Transformer architecture: encoder-decoder structure, multi-head self-attention, positional encoding, residual connections, layer normalisation, feed-forward sub-layers. BERT vs GPT paradigms. Introduction to Claude: Anthropic\'s mission and the Claude 3 family (Haiku, Sonnet, Opus). Constitutional AI (CAI): training pipeline, RLHF vs RLAIF, HHH framework. Claude\'s capabilities: 200K token context, vision, code generation, tool use, multilingual. Tokenisation: Byte-Pair Encoding (BPE). Temperature, top-p, top-k sampling parameters. Lab: Python Anthropic SDK, first API call, exploring the playground.'),
      spacer(60),
      h2('Unit 2: Prompt Engineering (8 Hours)'),
      p('Introduction to prompt engineering: anatomy of a prompt (instruction, context, input, output format). Zero-shot prompting. Few-shot prompting: selecting and ordering examples. Chain-of-Thought (CoT) prompting: Wei et al. (2022), "Let\'s think step by step." Zero-shot CoT. Self-consistency: majority voting over multiple reasoning chains. System prompts and role-playing personas. Structured output: JSON, XML, Markdown formatting. Context management: token limits, sliding window, summarisation. Advanced techniques: ReAct (Reasoning + Acting), Tree of Thoughts (ToT), meta-prompting, negative prompting. Workshop: iterative prompt optimisation, A/B testing, failure mode analysis.'),
      spacer(60),
      h2('Unit 3: Building Applications with Claude API (8 Hours)'),
      p('Claude API architecture: authentication, model selection, rate limits, pricing. Python Anthropic SDK: messages API, streaming, async usage. Building multi-turn chatbots: conversation history, stateless vs stateful design. Tool use / function calling: schema definition, tool_use content blocks, result passing, error handling. Retrieval-Augmented Generation (RAG): document ingestion, chunking, embeddings (Sentence Transformers), vector databases (Chroma, FAISS), cosine similarity retrieval, context injection. Vision API: base64 image encoding, multimodal prompts, document parsing. Production considerations: prompt caching, batch API, cost optimisation, latency, monitoring. Lab: end-to-end application build (RAG system, tool-use agent, or vision app).'),
      spacer(60),
      h2('Unit 4: Responsible AI, Safety & Ethics (6 Hours)'),
      p('Bias in LLMs: training data bias, social biases, amplification through RLHF, evaluation benchmarks (WinoBias, BBQ, TruthfulQA), mitigation strategies. Hallucinations: intrinsic vs extrinsic, causes, detection (self-consistency, Chain-of-Verification), grounding strategies. Constitutional AI deep dive: 58-principle constitution, RLAIF training loop, comparison with OpenAI RLHF. Privacy and data security: PII risks, prompt injection attacks, membership inference, GDPR implications. Responsible Use Guidelines: Anthropic\'s Acceptable Use Policy, prohibited uses, content moderation. AI governance: EU AI Act (risk categories), UNESCO AI Ethics framework, NIST AI Risk Management Framework. Case studies: AI misuse incidents, ethical discussion seminar.'),
      spacer(60),
      h2('Unit 5: Advanced Topics & Capstone (7 Hours)'),
      p('Agentic AI: Perceive-Plan-Act loop, ReAct agent implementation, memory types (in-context, vector DB, episodic). Multi-agent systems: orchestrator-worker pattern, critic-generator, agent communication. Model Context Protocol (MCP): host-client-server architecture, MCP servers (file system, DB, APIs), building a custom server. Claude in production: deployment patterns, load balancing, observability, cost optimisation. Fine-tuning vs prompt engineering vs RAG trade-offs. Industry applications: healthcare, legal, education, software engineering. Extended thinking mode. Future of LLMs: multimodality, reasoning, alignment. Guest lecture. Capstone project presentations and peer review.'),

      spacer(),
      // ─── EVALUATION SCHEME ─────────────────────────────────────────
      h1('6. Evaluation Scheme'),
      spacer(80),
      new Table({
        width: { size: 10080, type: WidthType.DXA },
        columnWidths: [2800, 2000, 1400, 3880],
        rows: [
          new TableRow({ children: [headBg('Component'), headBg('Frequency'), headBg('Marks'), headBg('COs Assessed')] }),
          new TableRow({ children: [cell('Unit Assignments'), cell('5 (one per unit)'), cell('20', {center:true}), cell('CO1, CO2, CO3, CO4, CO5')] }),
          new TableRow({ children: [cell('Unit Quizzes', {shade:true}), cell('5 (in-class, 15 min)', {shade:true}), cell('10', {center:true,shade:true}), cell('CO1, CO2, CO3, CO4, CO5', {shade:true})] }),
          new TableRow({ children: [cell('Mid-Semester Exam'), cell('1 (after Unit 2)'), cell('30', {center:true}), cell('CO1, CO2')] }),
          new TableRow({ children: [cell('End-Semester Exam', {shade:true}), cell('1', {shade:true}), cell('40', {center:true,shade:true}), cell('CO1, CO2, CO3, CO4, CO5', {shade:true})] }),
          new TableRow({ children: [cell('Capstone Project', {bold:true}), cell('Group (2–3 students)'), cell('Bonus 10', {center:true}), cell('CO3, CO5')] }),
          new TableRow({ children: [cell('TOTAL', {bold:true}), cell(''), cell('100', {center:true, bold:true}), cell('')] }),
        ]
      }),

      spacer(),
      // ─── BOOKS ─────────────────────────────────────────────────────
      h1('7. Books & Reference Materials'),
      spacer(60),
      h2('Textbooks'),
      bullet('T1: John Berryman & Albert Ziegler, Prompt Engineering for LLMs, O\'Reilly Media, 2024.'),
      bullet('T2: Lewis Tunstall, Leandro von Werra & Thomas Wolf, Natural Language Processing with Transformers, O\'Reilly Media, 2022.'),
      bullet('T3: Valentina Alto, Building LLM Powered Applications, Packt Publishing, 2023.'),
      spacer(80),
      h2('Reference Books & Papers'),
      bullet('R1: Vaswani et al., "Attention Is All You Need," NeurIPS 2017. arXiv:1706.03762'),
      bullet('R2: Anthropic Team, "Constitutional AI: Harmlessness from AI Feedback," 2022.'),
      bullet('R3: Anthropic, Claude API Documentation. docs.anthropic.com'),
      bullet('R4: Mark Coeckelbergh, AI Ethics, MIT Press Essential Knowledge, 2020.'),
      bullet('R5: Aston Zhang et al., Dive into Deep Learning. d2l.ai (free online).'),
      bullet('R6: Wei et al., "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models," NeurIPS 2022.'),
      bullet('R7: Yao et al., "ReAct: Synergizing Reasoning and Acting in Language Models," ICLR 2023.'),
      spacer(80),
      h2('Online Resources'),
      bullet('Anthropic Documentation: https://docs.anthropic.com'),
      bullet('Anthropic Prompt Engineering Guide: docs.anthropic.com/en/docs/build-with-claude/prompt-engineering'),
      bullet('Stanford CS224N — NLP with Deep Learning (YouTube)'),
      bullet('DeepLearning.AI Short Courses: Prompt Engineering for Developers'),
      bullet('ChromaDB Documentation: https://docs.trychroma.com'),

      spacer(),
      // ─── WEEKLY PLAN ──────────────────────────────────────────────
      h1('8. Weekly Lecture Plan'),
      spacer(80),
      new Table({
        width: { size: 10080, type: WidthType.DXA },
        columnWidths: [700, 1800, 5180, 2400],
        rows: [
          new TableRow({ children: [headBg('Week'), headBg('Lecture(s)'), headBg('Topic'), headBg('Assessment')] }),
          new TableRow({ children: [cell('1'), cell('L01–L02'), cell('History of NLP; Transformer Architecture'), cell('')] }),
          new TableRow({ children: [cell('2', {shade:true}), cell('L03–L04', {shade:true}), cell('LLM Landscape; Constitutional AI', {shade:true}), cell('Assignment 1 issued', {shade:true})] }),
          new TableRow({ children: [cell('3'), cell('L05–L07'), cell('Claude Capabilities; Tokenisation; API Lab'), cell('Quiz 1')] }),
          new TableRow({ children: [cell('4', {shade:true}), cell('L08–L10', {shade:true}), cell('Intro to Prompting; Zero/Few-shot; CoT', {shade:true}), cell('A1 due; A2 issued', {shade:true})] }),
          new TableRow({ children: [cell('5'), cell('L11–L12'), cell('System Prompts; Structured Output'), cell('Quiz 2')] }),
          new TableRow({ children: [cell('6', {shade:true}), cell('L13–L15', {shade:true}), cell('Context Management; Advanced Techniques; Workshop', {shade:true}), cell('A2 due; A3 issued', {shade:true})] }),
          new TableRow({ children: [cell('7'), cell('Mid-Sem'), cell('Mid-Semester Examination (Units 1 & 2)'), cell('Mid-Semester Exam')] }),
          new TableRow({ children: [cell('8', {shade:true}), cell('L16–L18', {shade:true}), cell('Claude API; Python SDK; Multi-turn Chatbot', {shade:true}), cell('', {shade:true})] }),
          new TableRow({ children: [cell('9'), cell('L19–L21'), cell('Tool Use; RAG; Vision API'), cell('Quiz 3')] }),
          new TableRow({ children: [cell('10', {shade:true}), cell('L22–L23', {shade:true}), cell('Production Patterns; Application Lab', {shade:true}), cell('A3 due; A4 issued; A5 issued', {shade:true})] }),
          new TableRow({ children: [cell('11'), cell('L24–L25'), cell('Bias in LLMs; Hallucinations'), cell('')] }),
          new TableRow({ children: [cell('12', {shade:true}), cell('L26–L29', {shade:true}), cell('Constitutional AI; Privacy; Ethics Case Studies', {shade:true}), cell('Quiz 4; A4 due', {shade:true})] }),
          new TableRow({ children: [cell('13'), cell('L30–L32'), cell('Agentic AI; Multi-agent; MCP'), cell('')] }),
          new TableRow({ children: [cell('14', {shade:true}), cell('L33–L35', {shade:true}), cell('Production Deployment; Industry Apps; Guest Lecture', {shade:true}), cell('Quiz 5; A5 due', {shade:true})] }),
          new TableRow({ children: [cell('15'), cell('L36'), cell('Capstone Project Presentations'), cell('Project Demo')] }),
        ]
      }),

      spacer(200),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 200 },
        border: { top: { style: BorderStyle.SINGLE, size: 4, color: BORDER_COLOR, space: 4 } },
        children: [
          new TextRun({ text: 'End of Course Syllabus  |  CSAI601 — Generative AI with Claude  |  B.Tech CS/IT', size: 18, color: '6c757d', italics: true, font: 'Arial' })
        ]
      })
    ]
  }]
});

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync('/sessions/blissful-quirky-tesla/mnt/outputs/CSAI601_Syllabus.docx', buffer);
  console.log('DOCX written OK');
}).catch(e => { console.error('DOCX error:', e.message); process.exit(1); });
