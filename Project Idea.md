# Capstone Project Proposals — 5 Options

**Theme:** Emerging-market systems combining deployable technology with **RAG-powered chat** (retrieval from past chats, telemetry, and approved documents) and **privacy-by-design** — **no public agent APIs** for sensitive data.

**Student context:** B.Sc. Electrical & Computer Engineering capstone proposal pack.

---

## Table of Contents

1. [Shared Architecture](#shared-architecture)
2. [Why Not Public Agents](#why-not-public-agents)
3. [Proposal 1 — Semantic Video Communication](#proposal-1--semantic-video-communication)
4. [Proposal 2 — Low-Bandwidth Video + Call Assistant](#proposal-2--low-bandwidth-video--call-assistant)
5. [Proposal 3 — RMG Heat-Stress Monitoring](#proposal-3--rmg-heat-stress-monitoring)
6. [Proposal 4 — Village Tele-Tutoring](#proposal-4--village-tele-tutoring)
7. [Proposal 5 — Secure Messenger (Telegram-Type)](#proposal-5--secure-messenger-telegram-type)
8. [Comparison Table](#comparison-table)
9. [How Proposals Connect](#how-proposals-connect)
10. [Faculty Cover Letter](#faculty-cover-letter)

---

## Shared Architecture

All proposals follow: **System under constraint** + **live telemetry** + **RAG chat** + **privacy controls**.

```
User chat message
    → Encrypt in transit (TLS 1.3 / E2E)
    → Session-scoped chat service
    → Privacy filter (PII redaction)
    → Inject allowed session telemetry
    → RAG: retrieve from past chats + approved corpora
    → Private LLM (Ollama / self-hosted) — cited answer only
    → Minimal encrypted audit log (optional)
```

### RAG Chat Rules (All Projects)

| Step | What happens |
|------|----------------|
| 1 | User asks in chat (worker, supervisor, student, caller). |
| 2 | System loads **only that user's session context** (sensor zone, call metrics, class ID). |
| 3 | **Privacy layer** redacts names, phone numbers, IDs if not needed. |
| 4 | **Retriever** searches **past encrypted chats** + **approved corpora** — not other users' data. |
| 5 | **Private LLM** answers using retrieved chunks + telemetry only; cites `[source_id]`. |
| 6 | Low confidence → safe fallback: "I don't have enough information." |

### Shared Privacy Protections

| Layer | Protection |
|-------|------------|
| Transport | TLS 1.3; WebRTC DTLS for video where applicable |
| Session isolation | No cross-user or cross-group retrieval |
| Corpus boundary | RAG indexes admin-approved docs — not the open web |
| PII minimization | Zone IDs, pseudonymous IDs; redacted logs |
| Chat retention | Configurable (7–30 days); user delete option |
| No training on chats | User messages not used for model fine-tuning |
| Local / edge option | Ollama on-prem for factory, school, or VPS |
| Access control | Role-based: worker/supervisor, student/teacher, caller-only |
| Transparency | UI privacy notice before first assistant use |

### Past-Chat RAG Rules

| Rule | Implementation |
|------|----------------|
| Scope | Only this user's or this group's past messages |
| Consent | First-use disclosure: assistant uses encrypted chat history |
| No public API | Ollama / self-hosted vLLM only |
| Encrypt history | AES-256 at rest; TLS in transit |
| Embeddings | Generated on private server or device |
| Retention | "Delete my memory" wipes index + messages |
| Citation | "From your chat on 12 Mar" or `[msg_id]` |
| Eval | Adversarial leak test: User A cannot retrieve User B's chats |

---

## Why Not Public Agents

| Risk (OpenAI / Claude / public APIs) | Consequence |
|--------------------------------------|-------------|
| Data leaves your control | Messages, telemetry, labor/child context sent to foreign cloud |
| Logging & retention | Provider may store prompts |
| Past chat in RAG | Full history in every request = maximum exposure |
| Compliance | RMG labor data, student homework — hard to justify |
| Breach surface | Vendor-stored prompts = secondary breach risk |

**Policy for all 5 proposals:** Sensitive chat and past-chat RAG run on **self-hosted or on-device** models inside the user's security boundary.

---

## Proposal 1 — Semantic Video Communication

### Title

**Retrieval-Grounded Semantic Video Communication for Ultra-Low Bitrate Mobile Networks**

### Track

Machine learning / multimedia **research**

### Problem

Video calls on 2G/3G and congested mobile networks fail below ~300 kbps. Classical codecs (H.264/H.265) produce blocky video or stalls. Learned codecs rarely combine **external retrieval memory** with evaluation on **Bangladesh/GCC network conditions**.

### Solution

Semantic video pipeline for **sub-200 kbps talking-head** calls:

1. **Semantic encoder** — compact representation (face, lip motion).
2. **Retrieval-augmented decoding** — retrieve similar patches/scenes from vector DB to reconstruct clearer video.
3. **Separate namespaces** — visual retrieval DB ≠ chat memory DB.

### RAG Chat (Support Assistant)

| User asks | RAG sources |
|-----------|-------------|
| "Why did quality drop again?" | Past chats + live telemetry + codec FAQ |
| "What bitrate worked last time?" | Past session summaries + trace corpus |
| "Compare to last week's call" | Historical telemetry + past chat |

Past-chat memory: encrypted per-user index; private Ollama + vector DB.

### Privacy

- No public LLM APIs for chat
- Visual retrieval and chat memory are **separate databases**
- Session isolation; delete-all-memory control
- 7-day default retention for eval

### Objectives

1. Semantic encoder for 150–200 kbps talking-head video
2. Retrieval-augmented decoding with patch/scene vector DB
3. Benchmark vs H.265 and non-retrieval learned baseline
4. Network emulation (Mahimahi / `tc netem`) with Bangladesh/GCC traces
5. Reproducible code, ablations, report

### Scope

**In:** 1:1 talking-head; 100–200 kbps; offline + real-time prototype (stretch)  
**Out:** Full consumer app; screen share; high-motion content; IMO feature parity

### Evaluation

- VMAF, LPIPS, PSNR; bitrate–distortion curves
- Optional MOS (10–20 users)
- Ablations: retrieval on/off, bitrate sweep, loss sensitivity
- RAG citation accuracy + cross-session leak tests

### Deliverables

1. Encoder + retrieval decoder + eval pipeline
2. Benchmark tables and ablation report
3. Private RAG support chat module
4. GitHub repo with configs and sample traces
5. Demo video vs H.265 on throttled link
6. Final report + privacy appendix

### Timeline (6 months)

| Month | Milestone |
|-------|-----------|
| 1 | Literature, dataset, H.265 baseline |
| 2 | Semantic encoder + basic decoder |
| 3 | Retrieval DB + augmented decoder |
| 4 | Network emulation + joint tests |
| 5 | Ablations, optional user study |
| 6 | Report, demo, repo cleanup |

### Resources

GPU workstation/cloud; PyTorch, FFmpeg, vector DB, Mahimahi

### CV Examples

- Semantic video with retrieval-grounded decoding: +X VMAF vs H.265 at 150 kbps
- Private RAG support chat: 0 cross-session leaks on adversarial eval

---

## Proposal 2 — Low-Bandwidth Video + Call Assistant

### Title

**A Network-Aware Low-Bandwidth Video Communication Platform with a Retrieval-Augmented Call Quality Assistant**

### Track

Software systems + networking + applied NLP (RAG) + HCI

### Problem

Users on weak mobile networks get frozen/pixelated calls without explanation. Apps adapt silently. Generic LLMs hallucinate technical advice without live state or **personal call history**.

### Solution

End-to-end platform:

1. **WebRTC 1:1 video** with adaptive bitrate (100–200 kbps target)
2. **Real-time telemetry** (RTT, loss, bitrate, resolution, stalls)
3. **RAG call assistant** — answers from live telemetry + FAQs + **encrypted past chats and past calls**

### RAG Chat (Primary Feature)

| User asks | RAG sources |
|-----------|-------------|
| "Why is video blurry?" | Live telemetry + FAQ + past calls/chats |
| "You suggested audio-only yesterday — do it now" | Past chat + current kbps/loss |
| "Same problem as last Tuesday" | Past chat retrieval + trace match |

Example answer:
> "Your link is at 110 kbps, 11% loss — similar to your chat on 8 Jun [chat:2026-06-08] on Dhaka 3G trace. I recommended audio-first mode then; applying now."

### Privacy

- **No public agent** — private Ollama on VPS or regional server
- E2E-encrypted chat; encrypted blobs on server
- RAG after decrypt inside private service (or on device in v2)
- Caller sees only own call history and chats
- Clear chat memory / clear all history controls
- Bengali/English privacy notice before first use

### Objectives

1. WebRTC MVP with adaptive bitrate
2. Telemetry API per session
3. Index corpora: traces, FAQs, playbooks (English/Bengali)
4. RAG chat with session context + past-chat memory
5. Optional auto-adaptation from policy/RAG suggestions
6. Evaluate QoE and RAG faithfulness

### Scope

**In:** 1:1 calls; RAG for network/quality/troubleshooting; bilingual FAQ  
**Out:** Groups, PSTN, stickers, global media farm at scale

### Evaluation

- Stall rate, time-to-first-frame, MOS
- 80 golden QA pairs — citation accuracy
- Cross-session leak test; PII redaction tests
- vs baseline WebRTC; RAG vs non-RAG ablation

### Deliverables

1. Demo: throttled call + "why is video bad?" chat
2. Telemetry dashboard
3. RAG service + corpus indexing pipeline
4. Open repo: frontend, signaling, rag-service, eval
5. Report + optional IMO/WhatsApp comparison clip

### Timeline (6 months)

| Month | Milestone |
|-------|-----------|
| 1 | WebRTC MVP + emulation |
| 2 | Adaptive bitrate + telemetry |
| 3 | Corpus + vector index |
| 4 | RAG + past-chat memory integration |
| 5 | QoE + RAG evaluation |
| 6 | UI polish, report, demo |

### Resources

VPS/TURN server; 2+ Android phones; FastAPI, WebRTC, vector DB, Ollama

### CV Examples

- Low-bandwidth video with 12% lower stall rate vs baseline on 2G traces
- RAG call assistant: 92% citation accuracy; encrypted past-chat memory

---

## Proposal 3 — RMG Heat-Stress Monitoring

### Title

**Textile Factory Heat-Stress Monitoring System with RAG Occupational Safety Assistant**

### Track

IoT systems + occupational safety + applied RAG + social impact

### Problem

Bangladesh RMG workers face extreme heat/humidity. Heat stress causes illness, lost productivity, and regulatory risk. Manual monitoring is absent; supervisors lack **instant, policy-grounded** guidance during heat spikes.

### Solution

1. **IoT sensors** (temp, humidity) on factory floors → **WBGT** computation
2. **Alerts** when thresholds exceeded
3. **RAG safety assistant** for supervisors — grounded in live sensors + ILO + Bangladesh labor law + factory policy

### RAG Chat (Primary Feature)

| User asks | RAG sources |
|-----------|-------------|
| "Can line 3 keep running?" | Zone WBGT + shift hours + ILO heat table |
| "What break is required now?" | Bangladesh labor rules + factory policy |
| "Why did alarm trigger?" | Sensor timeline + threshold config |

Answers must cite ILO, labor law, or factory policy chunks.

**Note:** Past-chat RAG for supervisor policy Q&A; worker anonymity via zone IDs.

### Privacy

- Worker anonymity: **zone_id** (Line 3), not worker names in RAG context
- On-prem deployment: RAG + LLM on factory LAN — chat never to public cloud
- Supervisor RBAC: only their floor's telemetry
- No medical diagnosis in chat — heat alert only
- Encrypted logs; 30-day retention; no training on worker messages
- No individual wearable tracking without written consent

### Objectives

1. Multi-zone sensor network + WBGT computation
2. Alert thresholds from ILO/WHO and Bangladesh references
3. Supervisor dashboard with zone heat maps
4. RAG chat over telemetry + policy corpora
5. Evaluate alerts + RAG citation accuracy

### Scope

**In:** 2–4 sensor zones; dashboard; Bengali/English RAG; lab or single-factory pilot  
**Out:** Nationwide deployment; medical diagnosis; legal case management

### Evaluation

- Alert precision/recall on simulated heat scenarios
- False alarms per 8-hour shift
- 80 safety QA golden set — citation faithfulness
- Privacy: worker cannot access other zones; PII injection fails

### Deliverables

1. Sensor network + dashboard
2. Alert system with configurable thresholds
3. RAG safety assistant with citation UI
4. GitHub: firmware/, backend/, rag-service/, eval/
5. Report with social impact and ethics section

### Timeline (6 months)

| Month | Milestone |
|-------|-----------|
| 1 | Literature, WBGT formulas, sensor prototype |
| 2 | Multi-zone deployment + time-series backend |
| 3 | Alert logic + dashboard |
| 4 | RAG corpus + chat UI |
| 5 | Simulated heat scenarios + golden QA eval |
| 6 | Pilot demo, report |

### Resources

ESP32 + temp/humidity sensors (~$50–150); FastAPI, TimescaleDB, vector DB, Ollama

### CV Examples

- WBGT monitoring: 0.89 alert F1 on simulated scenarios
- RAG safety assistant: 91% citation accuracy on occupational heat QA

---

## Proposal 4 — Village Tele-Tutoring

### Title

**Ultra-Low-Bandwidth Village Tele-Tutoring Platform with Retrieval-Augmented Lesson and Homework Assistant**

### Track

EdTech + low-bandwidth media + multilingual RAG + rural connectivity

### Problem

Village schools lack qualified teachers and stable internet. 2G/3G is expensive and slow. Standard platforms (Zoom, Meet) fail on village links. Generic AI tutors hallucinate off-curriculum content.

### Solution

1. **Teacher streams** face + slides at **sub-200 kbps** to village classroom
2. **Offline caching** of lessons for replay
3. **RAG homework assistant** — today's slides + NCTB curriculum + teacher notes (Bengali/English)

### RAG Chat (Primary Feature)

| Student asks | RAG sources |
|--------------|-------------|
| "Explain today's math Q3" | Today's slide + teacher notes |
| "Which chapter is this?" | NCTB curriculum chunk |
| "Show similar example" | Same chapter exercises only |

Never retrieves random web content.

### Privacy (Child-Data Priority)

- Pseudonymous student IDs; no public profiles
- Chat scoped to `class_id` + `session_date`
- Teacher approves notes before indexing
- Student chat **not** added to shared RAG index
- 7-day default retention; school policy documented
- COPPA-inspired: no ads, no profiling, no training on children's messages
- Optional offline RAG on Raspberry Pi at classroom
- Encrypted sync; local cache encrypted at rest
- **No public agent APIs**

### Objectives

1. Low-bitrate teacher → classroom stream under 200 kbps
2. Offline lesson cache and replay
3. Index NCTB curriculum + per-session materials
4. Bengali RAG homework chat with citations
5. Evaluate video QoE + homework QA accuracy

### Scope

**In:** One subject (e.g. Grade 8 Math); 1 teacher → 1 classroom; Bengali RAG  
**Out:** Full LMS; national rollout; all grades; proctored exams

### Evaluation

- VMAF/stall/MOS on 2G traces
- 60 NCTB-aligned homework problems — accuracy vs teacher answers
- Child prompt injection cannot access other students' data

### Deliverables

1. Teacher streaming + classroom receiver apps
2. Offline cache and replay
3. RAG homework assistant
4. QoE + homework eval reports
5. Demo video + ethics/privacy appendix

### Timeline (6 months)

| Month | Milestone |
|-------|-----------|
| 1 | NCTB corpus prep, network emulation |
| 2 | Low-bitrate video MVP |
| 3 | Slide upload, caching, offline replay |
| 4 | RAG indexing + Bengali student chat |
| 5 | QoE + homework golden set eval |
| 6 | Pilot demo, report |

### Resources

2–3 Android tablets; optional Raspberry Pi; VPS; NCTB PDFs; Ollama

### CV Examples

- Village tele-tutor at 180 kbps with lower stall rate on 2G traces
- Curriculum-grounded Bengali RAG: 88% correct on 60 NCTB homework QA pairs

---

## Proposal 5 — Secure Messenger (Telegram-Type)

### Title

**Secure Low-Bandwidth Messenger with Private On-Device Retrieval-Augmented Memory (Telegram-Grade Privacy)**

### Track

Security + messaging systems + private AI + optional low-bitwidth media

### Problem

Public messaging apps and **public AI agents** expose sensitive data. Telegram has E2E secret chats but **no private AI memory** over past messages. Users want AI help without sending chat history to OpenAI/Claude. Low-bandwidth regions need: **secure chat + survivable calls + private RAG**.

### Solution

**Telegram-class secure messenger** with:

1. **E2E encrypted 1:1 chat** (Signal-style patterns)
2. Optional low-bitrate voice/video (&lt;200 kbps) from Proposals 1/2
3. **Private RAG assistant** over **encrypted past chats** + user-uploaded docs
4. **Zero public agent policy** — architectural ban on public LLM APIs

### Telegram-Like Feature Map

| Feature | This app | Addition |
|---------|----------|----------|
| Secret chat E2E | ✅ Default for 1:1 | Private RAG on past E2E chats |
| Minimal server metadata | ✅ Ciphertext only | Encrypted embedding index |
| Voice messages | ✅ Low-bitrate | Local ASR + search past topics |
| Video call | Optional sub-200 kbps | RAG call assistant (Proposal 2 subset) |
| Cloud sync | Encrypted only | Device-only vs encrypted cloud index |
| Public channels | ❌ MVP scope | — |
| Public AI bots | ❌ **Rejected** | **Private agent only** |

### RAG Chat (Core Feature — Past Chat Memory)

```
User: "What did Ahmed say about the meeting time?"

1. Query encrypted index (chats with Ahmed only)
2. Retrieve top-3 message chunks [msg_42, msg_58, msg_71]
3. Private LLM answer with citations:
   "Ahmed said 3 PM Thursday [msg_58, 10 Mar]."
4. Never: full chat export to external API
```

### Privacy Tiers (Capstone Recommendation: Tier 3 Hybrid)

| Tier | Name | Past-chat RAG | Best for |
|------|------|---------------|----------|
| T1 | Device-only | Embeddings + LLM on phone | Maximum privacy |
| T2 | Private server | E2E chat; encrypted index on server | Speed + privacy |
| T3 | Hybrid | Docs on server; past chat on device | **Capstone sweet spot** |

### Security Controls

| Control | Detail |
|---------|--------|
| E2E encryption | Signal Protocol or libsodium (X25519 + AEAD) |
| Forward secrecy | New keys per session where possible |
| Server | Ciphertext + encrypted index blobs only |
| No public agent | Blocklist public LLM endpoints in app |
| On-device option | llama.cpp / Ollama for demos |
| Group RAG | Only group members' messages in group index |
| Delete | "Delete for everyone" + wipe from RAG index |
| Metadata minimization | No contact graph to third parties |

### Objectives

1. E2E messaging MVP (register, contacts, 1:1 chat)
2. Optional low-bitrate voice/video
3. Private RAG over encrypted past chat + user docs
4. Zero public agent policy
5. Eval: encryption checklist, RAG accuracy, leak tests, 2G delivery

### Scope

**In:** E2E 1:1 chat; private past-chat RAG; self-hosted backend; Bengali/English UI  
**Out:** Full Telegram parity; public AI integrations; unencrypted cloud RAG

### Evaluation

- 50 past-chat QA golden set
- 0 cross-user leaks on adversarial tests (target)
- Message delivery on emulated 2G traces
- Security threat-model checklist

### Deliverables

1. Android/Flutter secure messenger MVP
2. Self-hosted API + encrypted vector store
3. Private RAG with cited answers from past chat
4. Security appendix: threat model, why not public agents
5. Demo: public ChatGPT risk vs private memory
6. Optional low-bitrate call module

### Timeline (6 months)

| Month | Milestone |
|-------|-----------|
| 1 | E2E messaging MVP + crypto design doc |
| 2 | Encrypted sync + storage |
| 3 | Private embedding pipeline |
| 4 | Past-chat RAG + citation UI |
| 5 | Security + adversarial eval |
| 6 | Optional calls; report + demo |

### Business Comparison

| App | E2E | Low-bitrate calls | Private AI on past chats |
|-----|-----|-------------------|--------------------------|
| IMO | Partial | ✅ | ❌ |
| Telegram | Secret chats | ✅ | ❌ |
| WhatsApp | ✅ | ✅ | ❌ (Meta AI = public) |
| **This app** | ✅ | ✅ optional | ✅ |

**Pitch:** *Telegram-private chats + an assistant that remembers — without sending your life to OpenAI.*

### CV Examples

- E2E messenger with private RAG memory — zero public LLM API
- Adversarial eval: 0/50 cross-user memory leaks

---

## Comparison Table

| # | Title | Core domain | Past-chat RAG | Public agent | Primary eval |
|---|--------|-------------|---------------|--------------|--------------|
| **1** | Semantic video &lt;200 kbps | ML compression | ✅ support chat | ❌ banned | VMAF, LPIPS |
| **2** | Video + call assistant | WebRTC + adaptation | ✅ call/chat history | ❌ banned | Stall rate, MOS, RAG QA |
| **3** | RMG heat-stress | IoT + WBGT safety | Supervisor Q&A | ❌ banned | Alert F1, safety RAG |
| **4** | Village tele-tutoring | Rural EdTech | Session homework | ❌ banned | QoE, homework QA |
| **5** | Secure messenger | E2E + private AI | ✅ **core feature** | ❌ **architectural ban** | Leak tests, E2E audit |

---

## How Proposals Connect

```
Proposal 5 (Secure messenger E2E shell)
    ├── Proposal 2 (Low-bitrate calls + call assistant)
    │       └── Proposal 1 (Semantic video research → codec)
    └── Private past-chat RAG memory (no public APIs)

Proposal 3 & 4 = Independent social-impact tracks (factory safety, village education)
```

Proposals **1** and **2** prove low-bitrate media. Proposal **5** is the privacy shell. Proposals **2** and **5** can merge into one product: **secure calls + private assistant that remembers**.

---

## Faculty Cover Letter

Dear Faculty Supervisor,

I submit **five capstone proposals** under the theme of **constrained environments in emerging markets**. Each combines a **deployable system** with a **RAG-powered chat assistant** that retrieves answers from **encrypted past chats**, live telemetry (where applicable), and **approved document corpora** — not from generic LLM memory.

**Public agent APIs (OpenAI, Claude, etc.) are not used** for user chat, because past-chat retrieval would expose sensitive messages, call metadata, labor data, or child homework to third-party clouds. We deploy **self-hosted models (Ollama/vLLM)** and **E2E-encrypted storage** with session-scoped retrieval.

| Proposal | Summary |
|----------|---------|
| **1** | ML research: semantic video + retrieval decoding (&lt;200 kbps) + private support chat |
| **2** | Systems: low-bandwidth video calls + RAG call assistant with past-chat memory |
| **3** | IoT: RMG factory heat-stress monitoring + RAG safety assistant |
| **4** | EdTech: village tele-tutoring on 2G + child-safe curriculum RAG |
| **5** | Security: Telegram-grade E2E messenger + private past-chat RAG (no public agents) |

I request guidance on which proposal best fits capstone scope, lab resources, and evaluation criteria. I am prepared to narrow to **one primary proposal** upon approval.

Sincerely,  
[Your Name]  
B.Sc. Electrical & Computer Engineering  
North South University

---

## Evaluation Checklist (All Proposals)

- [ ] RAG citation accuracy on golden QA set
- [ ] Cross-user / cross-session leak adversarial tests
- [ ] PII redaction unit tests
- [ ] Privacy appendix in final report
- [ ] Confirmation: no public LLM API in production path
- [ ] User delete / clear memory functionality
- [ ] Privacy notice in UI (Bengali + English where applicable)

---

*Document version: 2026 — Capstone proposal pack (5 projects)*
