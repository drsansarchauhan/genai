#!/usr/bin/env python3
"""Write complete make_unit2_slides.js for pptxgenjs — 100 slides"""

js_path = '/sessions/blissful-quirky-tesla/mnt/outputs/make_unit2_slides.js'

# Read the preamble + L08 content from gen_unit2_pptx.py output
# Since that file was incomplete, rebuild entirely here
lines = []
a = lines.append

# ─── preamble ────────────────────────────────────────────────────────────────
a(r"""'use strict';
const pptxgen = require('/usr/local/lib/node_modules_global/lib/node_modules/pptxgenjs');
const prs = new pptxgen();
prs.layout = 'LAYOUT_WIDE';
prs.title = 'CSAI601 Unit 2 - Prompt Engineering';

const C = {
  navy:'0f1f3d', blue:'1a3a6b', red:'e94560', teal:'0a7c8c',
  gold:'f4a832', green:'27ae60', purple:'7b2fbe',
  white:'FFFFFF', light:'e6edf3', muted:'8b949e', dark:'0d1117',
};

function bg(sld,c){sld.background={color:c||C.dark};}
function rect(sld,x,y,w,h,c,o){sld.addShape(prs.ShapeType.rect,Object.assign({x,y,w,h,fill:{color:c}},o||{}));}
function txt(sld,t,x,y,w,h,o){sld.addText(t,Object.assign({x,y,w,h},o||{}));}
function titleBar(sld,label){
  rect(sld,0,0,13.33,0.55,C.navy);
  txt(sld,'CSAI601 | Unit 2: Prompt Engineering',0.15,0.08,9,0.38,{fontSize:11,color:C.muted});
  txt(sld,label,9.5,0.08,3.5,0.38,{fontSize:11,color:C.gold,bold:true,align:'right'});
}
function bottomBar(sld,l,r){
  rect(sld,0,7.05,13.33,0.45,C.navy);
  txt(sld,l||'CSAI601 | B.Tech CS/IT 3rd Year',0.15,7.1,7,0.3,{fontSize:10,color:C.muted});
  txt(sld,r||'CO2',10,7.1,3,0.3,{fontSize:10,color:C.gold,align:'right'});
}
function heroSlide(title,sub,tag,n){
  const sld=prs.addSlide(); bg(sld,C.dark);
  rect(sld,0,0,0.08,7.5,C.red);
  rect(sld,0,3.2,13.33,0.04,C.blue);
  txt(sld,tag||'CSAI601',0.5,0.8,12,0.5,{fontSize:14,color:C.teal,bold:true});
  txt(sld,title,0.5,1.5,12.3,2.2,{fontSize:34,color:C.white,bold:true});
  txt(sld,sub||'',0.5,3.5,12,0.9,{fontSize:17,color:C.light});
  txt(sld,String(n||''),12.5,6.5,0.7,0.5,{fontSize:13,color:C.muted,align:'right'});
}
function bulletSlide(title,bullets,tag,n){
  const sld=prs.addSlide(); bg(sld,C.dark);
  titleBar(sld,tag||''); bottomBar(sld);
  txt(sld,title,0.4,0.7,12.5,0.7,{fontSize:23,color:C.gold,bold:true});
  rect(sld,0.4,1.45,2.5,0.04,C.red);
  const items=bullets.map(b=>({text:b,options:{fontSize:16,color:C.light,bullet:{type:'bullet',color:C.teal},paraSpaceBefore:7}}));
  sld.addText(items,{x:0.4,y:1.6,w:12.5,h:5.2});
  txt(sld,String(n||''),12.5,6.5,0.7,0.3,{fontSize:11,color:C.muted,align:'right'});
}
function twoColSlide(title,lh,lb,rh,rb,tag,n){
  const sld=prs.addSlide(); bg(sld,C.dark);
  titleBar(sld,tag||''); bottomBar(sld);
  txt(sld,title,0.4,0.7,12.5,0.6,{fontSize:21,color:C.gold,bold:true});
  rect(sld,0.4,1.38,12.5,0.04,C.red);
  rect(sld,0.4,1.5,6.0,5.4,'111827',{line:{color:C.blue,width:1}});
  rect(sld,6.93,1.5,6.0,5.4,'111827',{line:{color:C.teal,width:1}});
  txt(sld,lh,0.6,1.6,5.6,0.5,{fontSize:14,color:C.red,bold:true});
  txt(sld,lb,0.6,2.15,5.6,4.5,{fontSize:13,color:C.light,valign:'top'});
  txt(sld,rh,7.13,1.6,5.6,0.5,{fontSize:14,color:C.teal,bold:true});
  txt(sld,rb,7.13,2.15,5.6,4.5,{fontSize:13,color:C.light,valign:'top'});
  txt(sld,String(n||''),12.5,6.5,0.7,0.3,{fontSize:11,color:C.muted,align:'right'});
}
function codeSlide(title,code,note,tag,n){
  const sld=prs.addSlide(); bg(sld,C.dark);
  titleBar(sld,tag||''); bottomBar(sld);
  txt(sld,title,0.4,0.7,12.5,0.6,{fontSize:21,color:C.gold,bold:true});
  rect(sld,0.4,1.45,12.5,5.0,'0d1117',{line:{color:C.blue,width:1}});
  txt(sld,code,0.6,1.6,12.0,4.7,{fontSize:12,color:C.green,fontFace:'Courier New',valign:'top'});
  if(note) txt(sld,note,0.4,6.6,12.5,0.35,{fontSize:11,color:C.muted});
  txt(sld,String(n||''),12.5,6.5,0.7,0.3,{fontSize:11,color:C.muted,align:'right'});
}
function tableSlide(title,headers,rows,tag,n){
  const sld=prs.addSlide(); bg(sld,C.dark);
  titleBar(sld,tag||''); bottomBar(sld);
  txt(sld,title,0.4,0.7,12.5,0.6,{fontSize:21,color:C.gold,bold:true});
  const cw=12.5/headers.length;
  const trows=[
    headers.map(h=>({text:h,options:{bold:true,color:C.white,fill:C.blue,fontSize:12}})),
    ...rows.map((row,ri)=>row.map(cell=>({text:cell,options:{color:C.light,fill:ri%2===0?'1a2535':'111827',fontSize:11}})))
  ];
  sld.addTable(trows,{x:0.4,y:1.5,w:12.5,colW:headers.map(()=>cw),border:{color:C.blue,pt:0.5}});
  txt(sld,String(n||''),12.5,6.5,0.7,0.3,{fontSize:11,color:C.muted,align:'right'});
}
function summarySlide(title,items,tag,n){
  const sld=prs.addSlide(); bg(sld,C.dark);
  titleBar(sld,tag||''); bottomBar(sld);
  txt(sld,title,0.4,0.7,12.5,0.6,{fontSize:21,color:C.gold,bold:true});
  const cols=items.length<=3?items.length:Math.min(items.length,3);
  const rows2=Math.ceil(items.length/cols);
  const bw=12.5/cols-0.15, bh=4.8/rows2-0.15;
  items.forEach((item,i)=>{
    const col=i%cols, row=Math.floor(i/cols);
    const x=0.4+col*(bw+0.15), y=1.5+row*(bh+0.15);
    rect(sld,x,y,bw,bh,'111827',{line:{color:C.teal,width:1}});
    txt(sld,item.icon||'',x+0.15,y+0.1,bw-0.3,0.45,{fontSize:20});
    txt(sld,item.title,x+0.15,y+0.55,bw-0.3,0.4,{fontSize:13,color:C.gold,bold:true});
    txt(sld,item.body,x+0.15,y+1.0,bw-0.3,bh-1.1,{fontSize:12,color:C.light,valign:'top'});
  });
  txt(sld,String(n||''),12.5,6.5,0.7,0.3,{fontSize:11,color:C.muted,align:'right'});
}
""")

# ─── Slide 1: Title ──────────────────────────────────────────────────────────
a(r"""
// SLIDE 1
{const sld=prs.addSlide(); bg(sld,C.dark);
rect(sld,0,0,0.1,7.5,C.red); rect(sld,0,3.5,13.33,0.05,C.blue);
txt(sld,'CSAI601',0.4,0.5,12,1.0,{fontSize:52,color:C.red,bold:true});
txt(sld,'Generative AI with Claude',0.4,1.55,12,0.7,{fontSize:28,color:C.light});
txt(sld,'UNIT 2: PROMPT ENGINEERING',0.4,2.45,12,0.6,{fontSize:20,color:C.teal,bold:true});
txt(sld,'8 Lectures | 8 Hours | CO2 | B.Tech CS/IT 3rd Year',0.4,3.2,12,0.4,{fontSize:14,color:C.muted});
rect(sld,0.4,3.75,12,0.04,C.blue);
const t1=['L08: Intro to Prompt Engineering','L09: Zero-Shot & Few-Shot',
  'L10: Chain-of-Thought','L11: Role, Persona & Tone',
  'L12: Structured Output','L13: Context Management',
  'L14: Evaluation & Iteration','L15: Prompt Lab Workshop'];
t1.forEach((t,i)=>{const col=i<4?0:1,row=i<4?i:i-4;
  txt(sld,t,0.4+col*6.5,4.0+row*0.55,6.2,0.5,{fontSize:13,color:C.light,bullet:{type:'bullet',color:C.teal}});
});
txt(sld,'Dept. of CS/IT | CO-PO Mapping: CO2-PO1,PO2,PO3',0.4,6.9,12,0.35,{fontSize:11,color:C.muted});}
""")

# ─── Slide 2: Overview ────────────────────────────────────────────────────────
a(r"""
// SLIDE 2
{const sld=prs.addSlide(); bg(sld,C.dark);
titleBar(sld,'Unit Overview'); bottomBar(sld);
txt(sld,'Unit 2 - Prompt Engineering',0.4,0.7,12.5,0.6,{fontSize:24,color:C.gold,bold:true});
const cards=[
  {l:'What is it?',b:'Crafting inputs to steer LLM behavior without changing model weights',c:C.teal},
  {l:'Why it matters',b:'Solve 90% of LLM tasks through prompt design alone — no GPU, no fine-tuning',c:C.red},
  {l:'CO mapped',b:'CO2: Design prompts for NLP tasks; evaluate quality; apply chain-of-thought',c:C.gold},
  {l:'Key outcome',b:'Build production-ready prompts: structured output, persona, reasoning, eval loop',c:C.green},
];
cards.forEach((c,i)=>{const x=0.4+(i%2)*6.5,y=1.6+Math.floor(i/2)*2.5;
  rect(sld,x,y,6.2,2.2,'111827',{line:{color:c.c,width:2}});
  txt(sld,c.l,x+0.2,y+0.15,5.8,0.45,{fontSize:14,color:c.c,bold:true});
  txt(sld,c.b,x+0.2,y+0.65,5.8,1.4,{fontSize:13,color:C.light,valign:'top'});
});}
""")



# L08 slides (3-14)
a(r"""
heroSlide('L08: Introduction to\nPrompt Engineering','Anatomy - When to prompt vs fine-tune - Principles','L08 of 8',3);
bulletSlide('What Is Prompt Engineering?',[
  'Prompt engineering = crafting inputs to LLMs to elicit desired outputs without modifying weights',
  'Operates entirely at inference time: no training, no GPU, no labelled data required',
  'Spans four concerns: correctness, format, tone, and safety',
  'Scale: a 10-word change in a system prompt can shift output quality by 40% or more',
],'L08 | Intro',4);
bulletSlide('Anatomy of an Effective Prompt',[
  'Component 1 INSTRUCTION: What task? Be explicit: classify, summarise, extract',
  'Component 2 CONTEXT: Background info, domain, constraints, prior decisions',
  'Component 3 INPUT DATA: The text or data to operate on - use XML tags to delimit it',
  'Component 4 OUTPUT FORMAT: Exact schema, length, tone, language',
  'Missing any component degrades output - the model guesses what was left implicit',
],'L08 | Anatomy',5);
tableSlide('Prompting vs Fine-Tuning',['Factor','Prompt Engineering','Fine-Tuning'],[
  ['Data required','Zero examples needed','100s-10000s labelled pairs'],
  ['Cost','API call only (~$0.001)','$100-$10000 depending on model'],
  ['Time to deploy','Minutes','Days to weeks'],
  ['Novel reasoning','Excellent via CoT','No improvement over base model'],
  ['When to use','Start every task here','After prompt engineering plateaus'],
],'L08 | PE vs FT',6);
bulletSlide('Anthropic Prompting Principles',[
  'Be specific: Claude performs better with precise, unambiguous instructions',
  'Use XML tags: Claude trained on XML-structured data — tags improve parsing accuracy',
  'Give reasoning room: Think step by step before final answer improves accuracy',
  'Show examples: 2-3 demonstrations outperform long textual explanations every time',
  'Assign a role: Role priming activates relevant knowledge clusters',
  'Iterate systematically: Test on 10+ inputs, categorise failures, fix root cause',
],'L08 | Principles',7);
codeSlide('4-Component Prompt Example',
'System: You are a senior technical writer. [ROLE]\nAudience: engineers, 2+ yr Python. [CONTEXT]\n\nUser:\n<task>\nWrite a 200-word explanation of the GIL.\nInclude: what it is, why Python has it, one threading impact.\nRespond in 3 numbered paragraphs.\n</task>\n\n<input_data>\nTarget: Python devs, no CPython internals background.\n</input_data>',
'XML-tagged inputs improve Claudes parsing accuracy significantly','L08 | Template',8);
twoColSlide('Prompt Failure Modes','Vague Instructions',
  'Tell me about Python\nSummarise this\nMake it better\nHelp with my code',
  'Specific Instructions',
  'Explain Pythons GIL to a junior dev in 3 bullets\nSummarise this review in 2 sentences: pros + cons\nRewrite for C-suite in under 100 words\nFind the bug, explain the fix',
  'L08 | Failures',9);
bulletSlide('Prompt Engineering Workflow',[
  'Step 1: Define success — write 3 ideal responses before drafting the prompt',
  'Step 2: Write baseline — simplest possible prompt',
  'Step 3: Test on 10 diverse inputs — easy, edge cases, adversarial inputs',
  'Step 4: Categorise failures — hallucination / wrong format / wrong scope / wrong tone',
  'Step 5: Fix root cause — add role, examples, format spec — ONE change at a time',
  'Step 6: Re-test full suite — confirm improvement, no regressions',
],'L08 | Workflow',10);
summarySlide('L08 Key Takeaways',[
  {icon:'',title:'Prompt = Program',body:'4 components: instruction, context, input, output format. Write all four.'},
  {icon:'',title:'Prompt First',body:'Try prompt engineering before fine-tuning. 90% solved at inference time.'},
  {icon:'',title:'Use XML Tags',body:'Anthropic recommends XML-delimited inputs. Improves parsing, reduces errors.'},
  {icon:'',title:'Iterate',body:'Test 10+ inputs. Categorise failures. Fix root cause. One change at a time.'},
],'L08 | Summary',14);
""")

# L09 first 4 slides (15-18)
a(r"""
heroSlide('L09: Zero-Shot &\nFew-Shot Prompting','Exploiting model priors - Steering with demonstrations - Many-shot','L09 of 8',15);
bulletSlide('The Prompting Spectrum',[
  'Zero-shot: No examples — pure instruction. Relies entirely on pre-training knowledge.',
  'One-shot: A single demonstration to anchor output format or style.',
  'Few-shot (2-8): Multiple input-output pairs. Model generalises pattern to new inputs.',
  'Many-shot (20-500+): Long-context window packed with examples. Near fine-tuning quality.',
  'Practical rule: Always try zero-shot first; add examples only if quality insufficient.',
],'L09 | Spectrum',16);
bulletSlide('Making Zero-Shot Prompts Succeed',[
  'Name the task explicitly: Classify / Summarise / Extract',
  'Specify output format: Return a JSON object with fields: name, score, reason',
  'Define the audience: Explain to a high-school student with no statistics background',
  'Set hard constraints: Maximum 3 sentences. No jargon. Active voice.',
  'Assign a role: Act as a senior Python security engineer - identify vulnerabilities',
],'L09 | Zero-Shot',17);
tableSlide('When Zero-Shot Fails',[
  'Failure Pattern','Root Cause','Fix'],[
  ['Wrong output structure','Format not specified precisely','Show exact format in 1-2 examples'],
  ['Wrong class label','Label set ambiguous','Define each label + 1 example per class'],
  ['Wrong tone','Audience not specified','1 demonstration in target tone'],
  ['Domain errors','Under-represented in training','3-5 domain-specific demonstrations'],
],'L09 | Failures',18);
""")

a(r"""
codeSlide('Few-Shot: Ticket Classification',
'System: Classify support tickets into: Billing | Technical | Shipping | Other.\n\n' +
'H: "My invoice shows double charge."   A: Billing\n' +
'H: "App crashes on iOS 17."            A: Technical\n' +
'H: "Package not delivered in 10 days." A: Shipping\n\n' +
'H: "I want to cancel my subscription."\n' +
'A: Billing\n\n' +
'Result: Claude correctly generalises from 3 demonstrations.\n' +
'Notice: All 4 classes should appear at least once in demonstrations.',
'Tip: If you have 4 output classes, show at least one example of each',
'L09 | Code', 19);
""")

a(r"""
bulletSlide('Designing Good Demonstrations', [
  'Rule 1 — Cover the output space: Show at least one example per class/label/format',
  'Rule 2 — Use realistic inputs: Toy examples generalise poorly to real data distributions',
  'Rule 3 — Keep format perfectly consistent: Any deviation leaks into Claudes output',
  'Rule 4 — Order by difficulty: Easy cases first, edge cases last (closest to real query)',
  'Rule 5 — Label accurately: One wrong label hurts more than having no examples at all',
  'Rule 6 — Match domain: Examples from a different domain confuse rather than help',
], 'L09 | Design', 20);
""")

a(r"""
twoColSlide('Zero-Shot vs Few-Shot Decision Matrix',
  'Lean Zero-Shot',
  'Common, well-defined task\nFree-form prose output is fine\nTight token budget (cost sensitive)\nNo labelled examples available\nRapid prototyping phase\nTask already in training distribution',
  'Lean Few-Shot',
  'Novel or specialised task\nStrict schema or format required\nBudget allows demonstration overhead\nHave 2-20 quality labelled examples\nProduction system tuning phase\nDomain under-represented in training',
  'L09 | Decision', 21);
""")

a(r"""
codeSlide('Format Priming with Demonstrations',
'# Use demos purely to lock in output structure\n\n' +
'Review: "Good laptop but fan is loud."\n' +
'Output:\n' +
'  summary: decent performance\n' +
'  pros: [portability, battery]\n' +
'  cons: [fan noise]\n' +
'  score: 6/10\n\n' +
'Review: "Best phone I have owned. Camera is stunning."\n' +
'Output:\n' +
'  summary: excellent all-rounder\n' +
'  pros: [camera, display, build]\n' +
'  cons: []\n' +
'  score: 9/10\n\n' +
'Review: {{USER_REVIEW}}\n' +
'Output:',
'Note: Demos teach format here, not task semantics — model already knows sentiment analysis',
'L09 | Format Priming', 22);
""")

a(r"""
bulletSlide('Many-Shot Prompting with Long Context', [
  'Claude supports 200K token context — enabling 50–500 demonstrations in a single prompt',
  'Anthropic research: Many-shot can match fine-tuning on classification and extraction tasks',
  'No gradient updates needed — quality comes from pattern generalisation in context',
  'Cost trade-off: 200 demos add ~40K tokens per call — significant at scale',
  'Rule of thumb: Under 8 examples = few-shot; above 20 = evaluate if overhead is justified',
  'Bootstrap technique: No data? Ask Claude to generate 10 examples, then use them as demos',
], 'L09 | Many-Shot', 23);
""")

a(r"""
summarySlide('L09 — Key Takeaways', [
  { icon: '🔵', title: 'Zero-Shot', body: 'Fast and cheap. Works for common tasks when instruction is crisp and complete.' },
  { icon: '🟡', title: 'Few-Shot (2-8)', body: 'Locks format and style. Essential when zero-shot produces wrong structure or class.' },
  { icon: '🟢', title: 'Many-Shot (20+)', body: 'Near fine-tuning quality in 200K context. No training needed.' },
  { icon: '⚙', title: 'Bootstrap', body: 'No labelled data? Generate examples with Claude first, then use as demonstrations.' },
], 'L09 | Summary', 26);
""")

# ─── L10 slides (27–38) ──────────────────────────────────────────────────────
a(r"""
// ══════════════════════════════════════════════════
// L10 — Chain-of-Thought & Reasoning (12 slides)
// ══════════════════════════════════════════════════

heroSlide('L10: Chain-of-Thought &\nReasoning Prompts',
  'Zero-shot CoT · Few-shot CoT · Self-consistency · Extended Thinking API',
  'L10 of 8', 27);

bulletSlide('Why Reasoning Prompts Matter', [
  'LLMs are next-token predictors — direct answers skip over multi-step reasoning',
  'Without a reasoning buffer, complex problems produce brittle, often wrong answers',
  'Chain-of-Thought (CoT) forces externalised reasoning before committing to a final answer',
  'Wei et al. (2022): Adding "Let us think step by step" boosted GPT-3 math accuracy 17% -> 78%',
  'The reasoning chain itself is auditable — you can spot exactly where logic fails',
  'CoT works on Claude, GPT, Gemini and virtually all large transformer-based models',
], 'L10 | Why CoT', 28);

tableSlide('Chain-of-Thought Variants',
  ['Variant', 'How It Works', 'Best Use Case'],
  [
    ['Zero-shot CoT', 'Append "Let us think step by step" — no examples needed', 'Quick improvement on any reasoning task'],
    ['Few-shot CoT', 'Demonstrations include full reasoning chains not just answers', 'Complex reasoning requiring specific style'],
    ['Self-consistency', 'Sample N reasoning paths; majority vote on final answer', 'High-stakes decisions; reduce variance'],
    ['Extended Thinking', 'Claude 3.7+ allocates scratchpad tokens before answering', 'Hardest reasoning: math, code, planning'],
    ['Tree-of-Thought', 'Explore multiple reasoning branches; prune dead ends', 'Search problems, strategy games'],
  ],
  'L10 | Variants', 29);

codeSlide('Zero-Shot CoT: Before vs After',
'WITHOUT CoT:\n' +
'Q: Train A leaves Delhi at 9am at 80 km/h. Train B leaves Mumbai\n' +
'   at 10am at 100 km/h. Distance: 1400 km. When do they meet?\n' +
'A: 2:30pm  [WRONG]\n\n' +
'WITH "Let us think step by step":\n' +
'A: 1. In the first hour, Train A covers 80 km. Gap at 10am = 1320 km.\n' +
'   2. Both moving toward each other: closing speed = 80+100 = 180 km/h\n' +
'   3. Time to close 1320 km: 1320/180 = 7.33 h = 7h 20min\n' +
'   4. 10am + 7h 20min = 5:20pm\n' +
'   Answer: 5:20pm  [CORRECT]',
'The reasoning chain makes errors visible and correctable',
'L10 | Before/After', 30);

bulletSlide('Effective Zero-Shot CoT Trigger Phrases', [
  '"Let us think step by step." — General reasoning, maths, logic; most widely tested trigger',
  '"Walk me through your reasoning." — Analytical tasks, diagnoses, recommendations',
  '"First, identify all relevant facts. Then solve." — Structured problem-solving',
  '"Before answering, list all assumptions and constraints." — Ambiguous problems',
  '"Think out loud." — Creative problem-solving, brainstorming, strategy',
  '"Show your work." — Calculations, proofs, derivations',
], 'L10 | Triggers', 31);

codeSlide('Few-Shot CoT: Full Example',
'Q: Roger has 5 balls. He buys 2 cans of 3 balls each. Total?\n' +
'A: Roger starts with 5. Buys 2x3=6 more. Total: 5+6=11. Answer: 11.\n\n' +
'Q: A juggler has 16 balls. Half are golf balls. Half of those are blue.\n' +
'   How many blue golf balls?\n' +
'A: Total: 16. Golf balls: 16/2=8. Blue golf balls: 8/2=4. Answer: 4.\n\n' +
'Q: Farmer has 17 sheep. All but 9 die. How many remain?\n' +
'A: "All but 9" means 9 survive. Reasoning step: 17 - (17-9) = 9.\n' +
'   Answer: 9.\n\n' +
'Q: [YOUR QUESTION]\n' +
'A:',
'Design tip: Match chain depth to your target task complexity',
'L10 | Few-shot CoT', 32);

codeSlide('Self-Consistency in Python',
'import anthropic, re\n' +
'from collections import Counter\n\n' +
'client = anthropic.Anthropic()\n' +
'question = "What is 17% of 340? Let us think step by step."\n\n' +
'answers = []\n' +
'for _ in range(5):  # sample 5 reasoning paths\n' +
'    r = client.messages.create(\n' +
'        model="claude-opus-4-5",\n' +
'        max_tokens=300,\n' +
'        messages=[{"role":"user","content": question}]\n' +
'    )\n' +
'    nums = re.findall(r"\\d+\\.?\\d*", r.content[0].text)\n' +
'    if nums: answers.append(nums[-1])\n\n' +
'final = Counter(answers).most_common(1)[0][0]\n' +
'print("Majority answer:", final)  # 57.8',
'Self-consistency improves accuracy 5-15% on arithmetic/logic benchmarks',
'L10 | Self-Consistency', 33);

codeSlide('Extended Thinking API (Claude 3.7+)',
'response = client.messages.create(\n' +
'    model="claude-sonnet-4-5",\n' +
'    max_tokens=16000,\n' +
'    thinking={\n' +
'        "type": "enabled",\n' +
'        "budget_tokens": 10000   # scratchpad allocation\n' +
'    },\n' +
'    messages=[{"role":"user","content":"Solve this..."}]\n' +
')\n\n' +
'for block in response.content:\n' +
'    if block.type == "thinking":\n' +
'        print("Scratchpad:", block.thinking)\n' +
'    elif block.type == "text":\n' +
'        print("Final answer:", block.text)',
'Use for: hard math, competitive coding, long-horizon planning, scientific reasoning',
'L10 | Extended Thinking', 34);

tableSlide('The PREP Reasoning Framework',
  ['Step', 'Instruction to Claude', 'Purpose'],
  [
    ['P — Problem', 'Restate the problem in your own words', 'Confirms correct understanding before solving'],
    ['R — Relevant', 'List all known quantities and constraints', 'Surfaces hidden assumptions and edge cases'],
    ['E — Execution', 'Solve step by step, showing each operation', 'Creates auditable reasoning chain'],
    ['P — Plausibility', 'Sanity-check the answer against intuition', 'Catches arithmetic errors and wrong units'],
  ],
  'L10 | PREP', 35);

bulletSlide('When CoT Helps Most vs. Least', [
  'CoT helps most: Multi-step arithmetic, logical deduction, planning, causal reasoning',
  'CoT helps most: Code generation with complex requirements, scientific problem-solving',
  'CoT helps less: Simple factual recall ("What is the capital of France?")',
  'CoT helps less: Creative writing tasks where reasoning chain disrupts narrative flow',
  'CoT can hurt: If the reasoning chain leads the model down a wrong path confidently',
  'Mitigation: Self-consistency (sample 5+ paths) reduces confident-wrong-answer risk',
], 'L10 | When CoT', 36);

summarySlide('L10 — Key Takeaways', [
  { icon: '💡', title: 'Zero-Shot CoT', body: '"Think step by step" unlocks latent reasoning. Works across all major LLMs.' },
  { icon: '📖', title: 'Few-Shot CoT', body: 'Show reasoning chains in demos. Model mimics both depth and style.' },
  { icon: '📊', title: 'Self-Consistency', body: 'Sample N paths, take majority vote. +5-15% accuracy. Reduces variance.' },
  { icon: '⚙', title: 'Extended Thinking', body: 'Claude 3.7 built-in scratchpad. Best for hardest reasoning. ~3x token cost.' },
], 'L10 | Summary', 38);
""")

# ─── L11 slides (39–50) ──────────────────────────────────────────────────────
a(r"""
// ══════════════════════════════════════════════════
// L11 — Role, Persona & Tone Control (12 slides)
// ══════════════════════════════════════════════════

heroSlide('L11: Role, Persona &\nTone Control',
  'Shaping identity · Calibrating tone · Audience targeting · Multi-turn consistency',
  'L11 of 8', 39);

bulletSlide('Why Role Assignment Works', [
  'Assigning a role activates a cluster of knowledge, vocabulary, and communication norms',
  'A senior cardiologist and a high-school teacher explain "cardiac risk" structurally differently',
  'Role priming shifts default register, vocabulary, hedging, and emphasis automatically',
  'More specific roles outperform generic ones: "senior Python security engineer" > "programmer"',
  'Stack roles for precision: "UX designer with behavioural psychology background"',
  'Limit: Claude will not maintain roles that conflict with its values and safety guidelines',
], 'L11 | Roles', 40);

tableSlide('Role Categories & Effects',
  ['Category', 'Example Roles', 'Effect on Output'],
  [
    ['Professional', 'Doctor, lawyer, data scientist, teacher', 'Domain vocabulary, communication norms, epistemic standards'],
    ['Creative', 'Novelist, screenwriter, copywriter, poet', 'Narrative voice, stylistic choices, creative latitude'],
    ['Functional', 'Devil\'s advocate, fact-checker, critic', 'Evaluation lens, adversarial or corrective framing'],
    ['Audience-based', '"Explain as if to a 5-year-old"', 'Simplification, analogy-heavy, no assumed prior knowledge'],
    ['Hybrid', '"Security engineer + technical writer"', 'Precise technical content in accessible prose'],
  ],
  'L11 | Categories', 41);

codeSlide('Building a Full Persona',
'You are Priya, a senior data scientist at a B2B SaaS company.\n\n' +
'Identity:\n' +
'- 8 years experience in ML, specialising in churn prediction\n' +
'- Direct communication — no filler phrases\n' +
'- Uses concrete numbers over vague adjectives\n\n' +
'Expertise: Python, SQL, scikit-learn, XGBoost, Spark, Salesforce\n\n' +
'Communication rules:\n' +
'- Ask for business context before going technical\n' +
'- When uncertain, say so explicitly\n' +
'- Offer 2-3 options with trade-offs, never a single answer\n\n' +
'Do NOT:\n' +
'- Use marketing language ("game-changing", "synergy")\n' +
'- Recommend paid tools when free alternatives exist',
'Persona = Identity + Expertise + Communication Rules + Constraints',
'L11 | Persona', 42);

tableSlide('Tone Dimensions You Can Control',
  ['Dimension', 'Range', 'How to Specify'],
  [
    ['Formality', 'Casual -> Professional -> Academic', '"Write in a casual Slack-message tone"'],
    ['Brevity', 'Terse -> Balanced -> Expansive', '"Be concise. Max 3 sentences per response."'],
    ['Hedging', 'Confident -> Cautious -> Neutral', '"State conclusions directly. No hedging."'],
    ['Empathy', 'Clinical -> Warm -> Supportive', '"Acknowledge frustration before solving."'],
    ['Technical depth', 'Lay -> Intermediate -> Expert', '"Assume CS degree, no ML background."'],
  ],
  'L11 | Tone', 43);

codeSlide('Layered Tone Specification',
'Write customer support responses with:\n\n' +
'Tone:      warm, empathetic, professional\n' +
'Formality: semi-formal (no slang; contractions allowed)\n' +
'Length:    3-5 sentences maximum\n\n' +
'Structure (always follow):\n' +
'  Sentence 1: acknowledge the specific issue\n' +
'  Sentences 2-3: provide the solution steps\n' +
'  Final sentence: warm closing with next step\n\n' +
'Forbidden phrases:\n' +
'- "I understand your frustration" (overused)\n' +
'- "No problem!" (too casual)\n' +
'- "As per my last email" (passive-aggressive)\n' +
'- "Going forward" (corporate jargon)',
'Forbidden phrase lists are often more robust than positive tone descriptions',
'L11 | Layered Tone', 44);

tableSlide('Audience Calibration Guide',
  ['Audience', 'Prompt Modifier', 'What Changes'],
  [
    ['5-year-old', '"Explain like I am 5"', 'Simple words, analogies, no jargon, short sentences'],
    ['Domain expert', '"Assume PhD-level background in X"', 'Technical depth, field-specific terms, dense information'],
    ['C-suite executive', '"2-minute read; business impact only"', 'Strategic framing, ROI focus, no implementation details'],
    ['Journalist', '"Educated general reader; no assumed prior"', 'Clear prose, concrete examples, no unexplained acronyms'],
    ['Developer', '"Technical audience; include code examples"', 'Code-first, concise explanation, links to documentation'],
  ],
  'L11 | Audience', 45);

bulletSlide('Maintaining Persona Across Turns', [
  'Technique 1 — System prompt anchoring: Full persona definition persists across all turns automatically',
  'Technique 2 — Explicit reminders: Append "Respond as Priya" to user turns in long conversations',
  'Technique 3 — Negative constraints: "Do not break character" + list of forbidden behaviors',
  'Technique 4 — Example exchanges: Include 2 sample Q&A turns inside the system prompt',
  'Watch for: Persona drift after 10+ turns — restate key constraints in the user message',
  'Ethics boundary: Claude will not maintain personas designed to circumvent safety guidelines',
], 'L11 | Multi-turn', 46);

twoColSlide('Good vs. Poor Persona Design',
  'Poor Persona Design',
  'You are an AI assistant.\nBe helpful and friendly.\nAnswer questions accurately.\n\n[Too vague — no real constraint. Claude defaults to generic responses. Persona adds no value.]',
  'Strong Persona Design',
  'You are Arjun, a Level 1 API support specialist.\n- Max 100 words per response\n- Always number your steps\n- Never guess at root cause; ask one clarifying question if uncertain\n- Escalate with ticket TKT-XXXXX if unresolved in 2 exchanges\n\n[Specific constraints that actually shape output differently from default]',
  'L11 | Good vs Poor', 47);

summarySlide('L11 — Key Takeaways', [
  { icon: '🌟', title: 'Role Assignment', body: 'Activates knowledge clusters. Stack roles for precision (domain + function).' },
  { icon: '🤖', title: 'Persona Design', body: 'Identity + expertise + communication rules + constraints = stable character.' },
  { icon: '🎙', title: 'Tone Control', body: 'Formality, brevity, hedging, empathy, depth — all specifiable and combinable.' },
  { icon: '👤', title: 'Audience', body: 'Matching content complexity to the reader is the highest-leverage single edit.' },
], 'L11 | Summary', 50);
""")

# ─── L12 slides (51–62) ──────────────────────────────────────────────────────
a(r"""
// ══════════════════════════════════════════════════
// L12 — Structured Output & Format Control (12 slides)
// ══════════════════════════════════════════════════

heroSlide('L12: Structured Output &\nFormat Control',
  'JSON · XML · Schema enforcement · Length control · Production pipelines',
  'L12 of 8', 51);

bulletSlide('Why Format Matters in Production', [
  'In production, Claude output rarely goes to a human directly — it feeds downstream systems',
  'Databases, APIs, UI renderers, workflow automations all need consistent, parseable output',
  'If format is inconsistent, the whole pipeline breaks regardless of content quality',
  'Structured output prompting = making Claude produce exactly what your downstream expects',
  'The golden rule: Any system that parses Claudes output programmatically must specify format explicitly',
  'Never rely on implicit formatting — what works 95% of the time fails 5% and breaks your app',
], 'L12 | Why Format', 52);

tableSlide('Three Techniques to Enforce JSON Output',
  ['Technique', 'How', 'Reliability'],
  [
    ['Explicit schema instruction', 'Paste the JSON schema in the prompt; say "Return ONLY valid JSON"', 'Good — 90-95%'],
    ['Seed the assistant turn', 'Start the assistant turn with "{" to force JSON opening', 'Better — 95-98%'],
    ['System prompt mode', 'System: "You output only valid JSON. No extra text."', 'Best — 97-99%'],
    ['Validation + retry', 'Catch json.JSONDecodeError; feed error back; retry up to 3 times', 'Near 100%'],
  ],
  'L12 | JSON Techniques', 53);

codeSlide('JSON Output with Schema',
'System: You output only valid JSON. No extra text, no code fences.\n\n' +
'Schema:\n' +
'{\n' +
'  "name": string,\n' +
'  "date": "YYYY-MM-DD",\n' +
'  "amount": number,\n' +
'  "currency": "USD"|"EUR"|"INR"\n' +
'}\n\n' +
'Text: "Received payment of Rs.5000 from Amit on 12 March 2025."\n\n' +
'Expected output:\n' +
'{"name":"Amit","date":"2025-03-12","amount":5000,"currency":"INR"}',
'Always validate immediately with json.loads() — do not assume success',
'L12 | JSON Schema', 54);

codeSlide('Pydantic Validation + Retry Pattern',
'from pydantic import BaseModel, ValidationError\n' +
'import json, anthropic\n\n' +
'class Ticket(BaseModel):\n' +
'    category: str\n' +
'    priority: int          # 1-5\n' +
'    summary: str\n' +
'    tags: list[str]\n\n' +
'client = anthropic.Anthropic()\n\n' +
'def extract_ticket(text: str, retries: int = 3) -> Ticket:\n' +
'    for attempt in range(retries):\n' +
'        r = client.messages.create(\n' +
'            model="claude-opus-4-5", max_tokens=300,\n' +
'            system="Output only valid JSON matching the Ticket schema.",\n' +
'            messages=[{"role":"user","content": text}]\n' +
'        )\n' +
'        try:\n' +
'            return Ticket(**json.loads(r.content[0].text))\n' +
'        except (json.JSONDecodeError, ValidationError) as e:\n' +
'            if attempt == retries - 1: raise\n' +
'            text = f"Error: {e}. Retry.\\n{text}"',
'Feeding the error message back to Claude lets it self-correct on retry',
'L12 | Pydantic', 55);

codeSlide('XML and Custom Delimited Formats',
'# XML structure for nested output:\n' +
'Return in this exact XML:\n' +
'<analysis>\n' +
'  <sentiment>positive|negative|neutral</sentiment>\n' +
'  <confidence>0.0 to 1.0</confidence>\n' +
'  <reasons>\n' +
'    <reason>TEXT</reason>\n' +
'  </reasons>\n' +
'</analysis>\n\n' +
'# Custom pipe-delimited for ETL:\n' +
'Return each finding on a new line:\n' +
'SEVERITY|COMPONENT|DESCRIPTION\n\n' +
'Example:\n' +
'HIGH|AuthService|JWT tokens are not expiring',
'XML suits nested/hierarchical data; pipe-delimited suits tabular ETL pipelines',
'L12 | XML/Custom', 56);

tableSlide('Length & Density Control Techniques',
  ['Control Type', 'Instruction Pattern', 'Example'],
  [
    ['Hard word limit', '"In exactly N words"', '"Summarise in exactly 50 words."'],
    ['Sentence count', '"In N sentences"', '"Explain in 3 sentences."'],
    ['Bullet count', '"List exactly N points"', '"Give exactly 5 action items."'],
    ['Section spec', 'Per-section length', '"Intro: 2 sentences. Body: 4 paragraphs. Summary: 1 sentence."'],
    ['Format type', 'Named format', '"Return a 2-column markdown table with headers: Pros | Cons"'],
  ],
  'L12 | Length', 57);

bulletSlide('Output Format Design Principles', [
  'Principle 1: The simpler the format, the more reliably Claude produces it',
  'Principle 2: Show the exact template — do not just describe it in words',
  'Principle 3: Add "Do not include any text before or after the [FORMAT]" to suppress preamble',
  'Principle 4: For hard character limits (SMS, tweet) always validate programmatically and retry',
  'Principle 5: Seeding the assistant turn (prefilling) is the single most reliable format lock',
  'Principle 6: Use Pydantic or jsonschema to validate — never trust Claude 100% in production',
], 'L12 | Principles', 58);

summarySlide('L12 — Key Takeaways', [
  { icon: '{}', title: 'JSON Output', body: 'Explicit schema + seed assistant turn. Always validate with Pydantic.' },
  { icon: '📄', title: 'XML / Custom', body: 'Show the exact template. XML for nested; delimited for tabular.' },
  { icon: '📏', title: 'Length Control', body: 'Word/sentence/bullet counts. Hard limits need programmatic validation.' },
  { icon: '✅', title: 'Retry Loop', body: 'Catch parse errors. Feed error back to Claude. 3 retries = near 100%.' },
], 'L12 | Summary', 62);
""")

# ─── L13 slides (63–74) ──────────────────────────────────────────────────────
a(r"""
// ══════════════════════════════════════════════════
// L13 — Context Management & Long Conversations (12 slides)
// ══════════════════════════════════════════════════

heroSlide('L13: Context Management &\nLong Conversations',
  '200K token window · Lost in the middle · Summarisation · Map-reduce chunking',
  'L13 of 8', 63);

bulletSlide('Understanding the Context Window', [
  'Context window = total tokens Claude sees at once: system prompt + history + current message',
  'Claude Sonnet/Opus 4 supports 200K tokens — roughly 600 pages or a 150,000-word novel',
  'Tokens are consumed by: system prompt, conversation history, documents, and current query',
  'Output tokens are separate — each response adds to input cost on the next call',
  'The "Lost in the Middle" problem: LLMs recall start and end of context most reliably',
  'Design implication: Place critical instructions in system prompt AND immediately before the question',
], 'L13 | Window', 64);

tableSlide('Context Management Strategies',
  ['Strategy', 'How It Works', 'Best For'],
  [
    ['Sliding window', 'Keep only the N most recent turns; drop oldest', 'Simple chat; OK to lose early context'],
    ['Summarisation', 'Periodically compress history into a summary; replace raw turns', 'Long conversations where key facts matter'],
    ['RAG (retrieval)', 'Store turns in vector DB; retrieve top-K relevant turns per query', 'Knowledge-intensive, long-lived agents'],
    ['Hierarchical memory', 'Working memory + episodic (summaries) + semantic (facts)', 'Full AI assistant with persistent state'],
    ['Map-reduce', 'Process each chunk independently; combine results', 'Long document analysis and summarisation'],
  ],
  'L13 | Strategies', 65);

codeSlide('Sliding Window + Auto-Summarisation',
'import anthropic\n' +
'client = anthropic.Anthropic()\n' +
'MAX_TURNS = 10\n\n' +
'def summarise(history):\n' +
'    r = client.messages.create(\n' +
'        model="claude-haiku-4-5-20251001", max_tokens=500,\n' +
'        messages=[*history,\n' +
'            {"role":"user","content": "Summarise: decisions made, facts, open questions."}]\n' +
'    )\n' +
'    return r.content[0].text\n\n' +
'def chat(history, msg):\n' +
'    if len(history) > MAX_TURNS * 2:\n' +
'        summary = summarise(history)\n' +
'        history = [{"role":"assistant",\n' +
'                    "content": f"[Summary]\\n{summary}"}]\n' +
'    history.append({"role":"user","content": msg})\n' +
'    r = client.messages.create(\n' +
'        model="claude-opus-4-5", max_tokens=1000,\n' +
'        messages=history\n' +
'    )\n' +
'    history.append({"role":"assistant","content":r.content[0].text})\n' +
'    return r.content[0].text, history',
'Use cheap Haiku for summarisation; use Opus/Sonnet for final responses',
'L13 | Summarisation', 66);

bulletSlide('Document Chunking Strategies', [
  'Fixed-size chunks: Split every N tokens with overlap — good for vector search / embedding',
  'Semantic chunks: Split at paragraph/section boundaries — good for Q&A and summarisation',
  'Hierarchical: Chapter -> section -> paragraph levels — good for long-form document analysis',
  'Map-reduce: Process each chunk independently, then combine results — good for extraction',
  'Sliding window: Overlapping chunks (e.g., 500 tokens, 100 overlap) — when context spans boundaries',
  'Key parameter: Chunk overlap prevents information loss at boundaries (typically 10-20% overlap)',
], 'L13 | Chunking', 67);

codeSlide('Map-Reduce Summarisation',
'def map_reduce_summarise(text: str, chunk_size: int = 50000) -> str:\n' +
'    # Split\n' +
'    words = text.split()\n' +
'    chunks = [" ".join(words[i:i+chunk_size])\n' +
'              for i in range(0, len(words), chunk_size)]\n\n' +
'    # Map: summarise each chunk with Haiku\n' +
'    summaries = []\n' +
'    for chunk in chunks:\n' +
'        r = client.messages.create(\n' +
'            model="claude-haiku-4-5-20251001", max_tokens=500,\n' +
'            messages=[{"role":"user","content":f"Summarise:\\n{chunk}"}]\n' +
'        )\n' +
'        summaries.append(r.content[0].text)\n\n' +
'    # Reduce: combine with Opus\n' +
'    r = client.messages.create(\n' +
'        model="claude-opus-4-5", max_tokens=1000,\n' +
'        messages=[{"role":"user","content":\n' +
'            "Combine these summaries:\\n" + "\\n\\n".join(summaries)}]\n' +
'    )\n' +
'    return r.content[0].text',
'Cost tip: Use Haiku for map phase (cheap); Opus/Sonnet for reduce phase (quality)',
'L13 | Map-Reduce', 68);

tableSlide('System Prompt Design for Long Sessions',
  ['Do', 'Avoid'],
  [
    ['State critical constraints once, clearly', 'Repeating the same instruction 3x hoping it sticks'],
    ['Use numbered rules for easy reference', 'Long paragraph descriptions of behavior'],
    ['Include examples only when format is non-obvious', 'Many examples that inflate cost on every call'],
    ['Define abbreviations and custom terms', 'Assuming Claude knows your internal terminology'],
    ['Keep system prompt under 2K tokens if possible', 'Dumping the entire product documentation'],
  ],
  'L13 | System Prompt', 69);

summarySlide('L13 — Key Takeaways', [
  { icon: '🎀', title: '200K Window', body: 'Large but not infinite. Critical info at top and bottom. Middle is less reliable.' },
  { icon: '📝', title: 'Summarisation', body: 'Compress old history. Haiku is cheap for summarisation. Keep episodic memory.' },
  { icon: '📑', title: 'Chunking', body: 'Map-reduce for long docs. Semantic chunks for Q&A. Overlap prevents boundary loss.' },
  { icon: '⚙', title: 'System Prompt', body: 'Under 2K tokens. Numbered rules. Avoid repetition. Define custom terms.' },
], 'L13 | Summary', 74);
""")

# ─── L14 slides (75–86) ──────────────────────────────────────────────────────
a(r"""
// ══════════════════════════════════════════════════
// L14 — Prompt Evaluation & Iteration (12 slides)
// ══════════════════════════════════════════════════

heroSlide('L14: Prompt Evaluation\n& Iteration',
  'Metrics · LLM-as-judge · A/B testing · Versioning · Systematic improvement cycle',
  'L14 of 8', 75);

bulletSlide('Why Systematic Evaluation Matters', [
  'A prompt that works on 3 test cases may fail on the 4th — intuition alone is unreliable',
  'Prompt improvements by intuition may cause regressions on edge cases you did not test',
  'Goodharts Law: Optimising on a small test set leads to overfitting — hold out a validation set',
  'Without metrics, you cannot know if iteration is improving or degrading quality',
  'Evaluation is the difference between ad-hoc prompting and reliable prompt engineering',
  'Target: define success criteria before writing the first prompt, not after seeing the output',
], 'L14 | Why Eval', 76);

tableSlide('Evaluation Metrics by Task Type',
  ['Task', 'Primary Metric', 'Tool / Method'],
  [
    ['Classification', 'Accuracy, F1, Confusion Matrix', 'sklearn + labelled test set'],
    ['Extraction', 'Exact match, Partial match, F1', 'String matching + normalisation'],
    ['Summarisation', 'ROUGE-L, BERTScore, Human eval', 'evaluate library or LLM-as-judge'],
    ['Generation', 'Human rating 1-5, LLM-as-judge', 'Claude grading Claude outputs'],
    ['Format compliance', 'Parse success rate', 'json.loads() + Pydantic validation'],
    ['Cost / Latency', 'p50/p95 ms, $/1000 requests', 'Usage API + timing instrumentation'],
  ],
  'L14 | Metrics', 77);

codeSlide('LLM-as-Judge Pattern',
'EVAL_PROMPT = (\n' +
'  "You are an expert evaluator.\\n"\n' +
'  "Task: {task}\\nResponse: {response}\\n\\n"\n' +
'  "Score 1-5: accuracy, completeness, clarity, format.\\n"\n' +
'  "Return ONLY JSON: "\n' +
'  \'{{"accuracy":N,"completeness":N,"clarity":N,"format":N,\'\n' +
'  \'"overall":N,"critique":"one sentence"}}\'\n' +
')\n\n' +
'def evaluate(task: str, response: str) -> dict:\n' +
'    r = client.messages.create(\n' +
'        model="claude-haiku-4-5-20251001",\n' +
'        max_tokens=200,\n' +
'        messages=[{"role":"user",\n' +
'                   "content": EVAL_PROMPT.format(\n' +
'                       task=task, response=response)}]\n' +
'    )\n' +
'    return json.loads(r.content[0].text)',
'Use Haiku as judge — cheap, fast, surprisingly accurate on well-defined rubrics',
'L14 | LLM-Judge', 78);

codeSlide('A/B Prompt Comparison',
'def compare(prompt_a, prompt_b, test_cases, n_trials=3):\n' +
'    results = {"A": [], "B": []}\n' +
'    for case in test_cases:\n' +
'        for prompt, label in [(prompt_a,"A"),(prompt_b,"B")]:\n' +
'            scores = []\n' +
'            for _ in range(n_trials):   # multiple trials = lower variance\n' +
'                r = client.messages.create(\n' +
'                    model="claude-opus-4-5", max_tokens=500,\n' +
'                    messages=[{"role":"user",\n' +
'                               "content":prompt.format(**case)}]\n' +
'                )\n' +
'                s = evaluate(case["task"],r.content[0].text)\n' +
'                scores.append(s["overall"])\n' +
'            results[label].append(sum(scores)/len(scores))\n\n' +
'    a_mean = sum(results["A"])/len(results["A"])\n' +
'    b_mean = sum(results["B"])/len(results["B"])\n' +
'    return {"A": a_mean, "B": b_mean,\n' +
'            "winner": "A" if a_mean > b_mean else "B"}',
'Always compare on the SAME test set — different test sets introduce selection bias',
'L14 | A/B Test', 79);

tableSlide('The Iterative Improvement Cycle',
  ['Step', 'Action', 'Outcome'],
  [
    ['1. Baseline', 'Write the simplest first prompt', 'Initial performance score'],
    ['2. Failure analysis', 'Categorise errors on test set', 'Error taxonomy (5 categories)'],
    ['3. Hypothesis', 'Identify which prompt element causes each error type', 'Prioritised change list'],
    ['4. Intervention', 'Change ONE element at a time', 'New prompt variant to test'],
    ['5. Evaluation', 'Run full test suite on new variant', 'Delta vs. baseline score'],
    ['6. Decision', 'Accept, reject, or combine changes', 'Updated best prompt'],
    ['7. Repeat', 'Until target quality or diminishing returns', 'Production-ready prompt'],
  ],
  'L14 | Cycle', 80);

codeSlide('Prompt Versioning (Git-style)',
'# prompts/ticket_classifier/v3.txt\n' +
'# Changelog:\n' +
'# v1: Basic zero-shot (72% accuracy on 50-case test set)\n' +
'# v2: Added explicit output schema (81% accuracy)\n' +
'# v3: Added 4 few-shot examples, 1 per class (89% accuracy)\n' +
'# Test suite: tests/ticket_classifier_test.json\n' +
'# Last eval date: 2025-03-15\n' +
'# Eval model: claude-opus-4-5\n\n' +
'System: You are a customer support ticket classifier...\n' +
'[rest of prompt follows]',
'Rule: Never silently update a production prompt without running the full test suite',
'L14 | Versioning', 81);

tableSlide('Common Error Categories & Fixes',
  ['Error Category', 'Symptom', 'Fix'],
  [
    ['Hallucination', 'Invented facts not in the input', 'Add: "Only use information provided. Do not infer."'],
    ['Format deviation', 'Wrong structure or missing fields', 'Show exact template + add Pydantic validation'],
    ['Scope creep', 'Answers beyond the requested task', 'Add: "Answer only what is asked. Nothing else."'],
    ['Truncation', 'Response cut off before completion', 'Increase max_tokens; add "Complete the full response."'],
    ['Refusal', 'Unnecessary safety trigger', 'Add context explaining the legitimate use case'],
  ],
  'L14 | Error Types', 82);

summarySlide('L14 — Key Takeaways', [
  { icon: '📊', title: 'Metrics First', body: 'Define success before writing the first prompt. Choose metrics that match the task.' },
  { icon: '⚖', title: 'LLM-as-Judge', body: 'Scale evaluation with Haiku grading outputs. Works when ground truth unavailable.' },
  { icon: '🔬', title: 'A/B Testing', body: 'Same test set. Multiple trials. Change one thing at a time.' },
  { icon: '📄', title: 'Version Control', body: 'Prompts are code. Git-track with performance metadata alongside each version.' },
], 'L14 | Summary', 86);
""")

# ─── L15 slides (87–100) ──────────────────────────────────────────────────────
a(r"""
// ══════════════════════════════════════════════════
// L15 — Workshop: Prompt Optimisation Lab (14 slides)
// ══════════════════════════════════════════════════

heroSlide('L15: Workshop\nPrompt Optimisation Lab',
  'Hands-on practice: write, test, analyse, iterate · Three real-world challenges',
  'L15 of 8', 87);

bulletSlide('Lab Overview', [
  'This workshop consolidates all Unit 2 techniques in a structured 60-minute lab session',
  'Three progressively complex challenges covering different technique combinations',
  'Lab A: Sentiment classifier with structured JSON output — target 95%+ accuracy',
  'Lab B: Contract risk extraction — identify and score clauses with chain-of-thought',
  'Lab C: Persona-driven support agent — tone, format, escalation rules combined',
  'Full cycle: write baseline -> measure -> analyse failures -> iterate -> verify improvement',
], 'L15 | Overview', 88);

codeSlide('Lab A: Sentiment Classifier — Baseline',
'# Start with this minimal prompt (intentionally weak)\n' +
'BASELINE = "Classify the sentiment of this text: {text}"\n\n' +
'# Target output schema:\n' +
'# {\n' +
'#   "label": "positive"|"negative"|"neutral"|"mixed",\n' +
'#   "confidence": 0.0 to 1.0,\n' +
'#   "aspects": [{"aspect": str, "sentiment": "pos"|"neg"|"neu"}],\n' +
'#   "explanation": "one sentence"\n' +
'# }\n\n' +
'# Test cases (expected labels):\n' +
'# "Great product, terrible shipping!"  -> mixed\n' +
'# "The battery lasts all day."         -> positive\n' +
'# "Item arrived. Works."              -> neutral\n' +
'# "Completely broken, never buying again." -> negative\n' +
'# "Love the design but software is buggy." -> mixed',
'Run the baseline first — observe where it fails before improving anything',
'L15 | Lab A Setup', 89);

bulletSlide('Lab A — Iteration Guide', [
  'Iteration 1: Add explicit output schema (JSON with all fields) — expect +10% accuracy',
  'Iteration 2: Define "mixed" explicitly — "Use mixed when text contains both pos and neg aspects"',
  'Iteration 3: Add 1 few-shot example per label (4 demos total) — expect +15% accuracy',
  'Iteration 4: Seed the assistant turn with "{" to prevent JSON parsing errors',
  'Iteration 5: Add Pydantic validation with retry loop — should reach near 100% format compliance',
  'Target: 95%+ label accuracy + 100% valid JSON. Log each iteration score.',
], 'L15 | Lab A Iter', 90);

codeSlide('Lab B: Contract Risk Extraction',
'System: You are a legal risk analyst. Identify risks for the CLIENT.\n\n' +
'Return a JSON array. Each element:\n' +
'{\n' +
'  "clause_text": "exact quote from contract",\n' +
'  "risk_level": "HIGH"|"MEDIUM"|"LOW",\n' +
'  "risk_category": "Liability"|"IP"|"Payment"|"Termination"|"Other",\n' +
'  "explanation": "1-2 sentence plain English explanation",\n' +
'  "suggested_fix": "brief mitigation suggestion"\n' +
'}\n\n' +
'Test clause:\n' +
'"The Client grants the Vendor a perpetual, irrevocable, worldwide,\n' +
'royalty-free license to use, reproduce, modify, and distribute any\n' +
'materials provided by the Client, including the right to sublicense."',
'Expected: HIGH risk, IP category — perpetual + irrevocable + sublicense = severe IP risk',
'L15 | Lab B', 91);

codeSlide('Lab C: Technical Support Persona',
'You are Aria, Level 1 support specialist for CloudStore.\n\n' +
'Response format (always follow exactly):\n' +
'[ISSUE IDENTIFIED]: one-sentence restatement\n' +
'[STEPS TO TRY]:\n' +
'  1. ...\n' +
'  2. ...\n' +
'[EXPECTED OUTCOME]: what user should see\n' +
'[ESCALATE IF]: when to contact L2\n\n' +
'Rules:\n' +
'- Maximum 150 words per response\n' +
'- Never speculate about hardware failures\n' +
'- End with: "Did that help? [YES] / [NO]"\n' +
'- If NO: create ticket TKT-{random 5 digits}\n\n' +
'Forbidden: "Great question!" "Absolutely!" "As per my last email"',
'Test: submit "tried everything, nothing works" — should trigger immediate escalation',
'L15 | Lab C', 92);

tableSlide('Lab Debrief: Common Findings & Fixes',
  ['Issue Found', 'Root Cause', 'Fix'],
  [
    ['Wrong "mixed" label', 'No definition of "mixed" provided', 'Add definition + 1-2 few-shot mixed examples'],
    ['JSON missing fields', 'Schema listed as "optional" implicitly', 'Mark all fields required; allow null explicitly'],
    ['Aria says "Absolutely!"', 'Negative constraint not specific enough', 'Add exact forbidden phrase list'],
    ['All risks scored HIGH', 'No calibration between risk levels', 'Add 1 example each for HIGH, MEDIUM, LOW'],
    ['Response exceeds 150 words', 'Word limit instruction too soft', 'Add: "Count words. Revise if over 150."'],
    ['JSON parse error on retry', 'Error message not clear enough', 'Feed exact error + location to Claude on retry'],
  ],
  'L15 | Debrief', 93);

bulletSlide('Unit 2 Capability Checklist', [
  'I can write zero-shot and few-shot prompts appropriate to any task type',
  'I can apply chain-of-thought triggers and use the extended thinking API',
  'I can design stable, multi-turn personas with tone and communication constraints',
  'I can enforce JSON, XML, and custom output schemas with validation and retry',
  'I can manage long conversations using summarisation and map-reduce chunking',
  'I can measure prompt quality, run A/B tests, and iterate systematically',
], 'L15 | Checklist', 94);

summarySlide('Unit 2 Mastery — Complete', [
  { icon: '💡', title: 'Zero & Few-Shot', body: 'Right demo strategy for any task type and data availability.' },
  { icon: '🧠', title: 'Chain-of-Thought', body: 'Step-by-step reasoning for complex problems. Extended thinking for hardest tasks.' },
  { icon: '🌟', title: 'Persona Design', body: 'Stable multi-turn characters with controlled tone and communication rules.' },
  { icon: '{}', title: 'Structured Output', body: 'Schema-validated JSON/XML for downstream systems. Retry with error feedback.' },
  { icon: '🎀', title: 'Context Management', body: 'Summarisation, chunking, hierarchical memory for long sessions.' },
  { icon: '📊', title: 'Eval & Iteration', body: 'Metrics, LLM-as-judge, A/B testing, version control for production prompts.' },
], 'L15 | Unit Summary', 100);
""")

# ─── final save ──────────────────────────────────────────────────────────────
a(r"""
// ═══ Save ═══
prs.writeFile({ fileName: '/sessions/blissful-quirky-tesla/mnt/outputs/CSAI601_Unit2_Slides.pptx' })
   .then(() => console.log('SAVED: CSAI601_Unit2_Slides.pptx'))
   .catch(e => console.error('Error:', e));
""")

# Write to disk
with open(js_path, 'w') as f:
    f.write('\n'.join(lines))

print(f"Written {js_path}")
