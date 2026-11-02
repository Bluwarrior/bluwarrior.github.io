# Portfolio Design & Architecture Specification

## 1. Visual Design System & Design Tokens

### 1.1 Color Palette
- **Canvas Base Background (`--bg`)**: `#090D16` (Deep slate noir)
- **Secondary Surface Background (`--bg-2`)**: `#0C1220` (Midnight navy surface)
- **Card Surface Default (`--surface`)**: `rgba(255, 255, 255, 0.03)`
- **Card Surface Elevated (`--surface-2`)**: `rgba(255, 255, 255, 0.055)`
- **Border Lines Primary (`--line`)**: `rgba(255, 255, 255, 0.075)`
- **Border Lines Subtle (`--line-soft`)**: `rgba(255, 255, 255, 0.04)`
- **Primary Text (`--text`)**: `#F1F4FA` (Off-white high contrast)
- **Secondary Text (`--text-2`)**: `#B4BDCF` (Slate silver)
- **Muted Body Text (`--muted`)**: `#868FA3` (Cool gray)
- **Dim Labels / Monospace (`--dim`)**: `#7E889E` (Slate cool gray — 4.8:1 WCAG AA compliant)
- **Primary Accent (`--accent`)**: `#7C8CFF` (Electric periwinkle/violet)
- **Accent Soft Glow (`--accent-soft`)**: `#C2CAFF` (Lavender glow)
- **Status Green (`--green`)**: `#3DDC97` (Emerald active indicator)
- **Status Red (`--red`)**: `#FF6B6B` (Coral crimson warning)

### 1.2 Typography
- **Primary Interface Font**: `Inter`, system-ui, -apple-system, sans-serif
- **Code, Data & Monospace Font**: `JetBrains Mono`, ui-monospace, monospace
- **Micro Labels**: Uppercase, 12px minimum floor, letter-spacing 0.04em, Monospace
- **Card Headings**: 21px to 25px, font-weight 600, letter-spacing -0.025em, Inter
- **Body Descriptions**: 13.5px to 15px, line-height 1.6 to 1.75, Inter

### 1.3 Container & Elevation Specs
- **Card Corner Radius**: 18px
- **Pill / Button Corner Radius**: 6px to 9px (buttons), 999px (status badges)
- **Card Hover State**: Translate Y -4px, border color transition to accent alpha, directional elevation shadow without zero-offset colored blur
- **Backdrop Blur Filter**: 14px to 16px blur on headers and modals

---

## 2. Interaction & Component Behavior

### 2.1 Universal Modal Dialog Architecture
Both `index.html` and `projects.html` utilize a shared, fully accessible modal dialog:
- **Backdrop**: Covers the full viewport, fixed positioning, semi-transparent background (`rgba(5, 8, 15, 0.82)`), backdrop blur filter (14px).
- **Dialog Container**: Centered horizontally and vertically, maximum width 620px, card corner radius (18px), midnight navy surface (`#0C1220`), subtle violet border line (`rgba(124, 140, 255, 0.28)`), elevation shadow (`0 24px 60px -12px rgba(0,0,0,0.9)`).
- **Dismiss Triggers**:
  - Top-right close button (`✕`)
  - Clicking anywhere on the blurred backdrop outside the dialog container
  - Pressing the keyboard `Escape` key
- **Scroll Lock**: Body scroll must be locked (`overflow: hidden`) whenever a modal is open.
- **Keyboard Navigation**: Focus trap within the modal, automatic focus on the close button upon opening, and return of focus to the triggering element upon closing.
- **URL Hash Synchronization**: Modals synchronize with `window.location.hash = '#project=' + itemId` or `'#research=' + researchId`, enabling deep-linking and browser Back button dismissal without leaving the page.

### 2.2 Modal Content Structure
Each modal dialog dynamically displays:
1. **Badges Row**:
   - Origin Chip (e.g., `ITT 2026 Conference Paper`, `Open Source Tooling`, `GDG Hackathon Build`, `Independent Project`).
   - Status Pill (e.g., `Peer-Reviewed / In Publication`, `Active Open Source`, `Active Prototype`).
2. **Title**: Item name in bold header font.
3. **Subtitle**: One-line domain descriptor in monospace font.
4. **Description**: Concise high-level summary of the system or research.
5. **Technical Architecture & Highlights**: Bulleted list detailing system topology, algorithms, evaluation metrics, or protocols.
6. **Tech Stack & Protocols Chips**: Specific tools, models, frameworks, and methodologies.
7. **Action Footer**:
   - For open-source items: Prominent primary button linking to GitHub.
   - For peer-reviewed research: Prominent primary action button linking directly to open or download the complete research paper PDF (`Personalized_Agent_Final.pdf`), accompanied by the conference status notice.
   - For internal/academic prototypes: Styled badge indicating prototype availability upon request.

### 2.3 Mobile & Responsive Navigation
- **Navigation Toggle & Drawer**: Below 1180px, the header displays an accessible toggle button (`#navToggle`) and slide-over navigation drawer (`#mobileNav`).
- **Touch Target Floor**: All interactive buttons adhere to the WCAG 44×44px minimum touch target size.

---

## 3. Page Routing & Interaction Rules

### 3.1 Landing Page (`index.html`)
- **Research Section**:
  - The research card (`Adaptive Multi-Agent Framework for Personalised Learning Support`) is **interactive** (`paper--interactive`, `role="button"`, `tabindex="0"`, `data-research="itt2026"`).
  - The expand arrow button inside the paper title row is strictly aligned to the top-right corner of the title block.
  - The side visual box labeled "Agent topology" strictly reflects the four components:
    1. **Learner Analysis Agent**: Analyzes misconceptions, error patterns, and recommended difficulty.
    2. **Assessment Agent**: Evaluates response score, feedback, and selects next question.
    3. **Tutor / Remediation Agent**: Delivers targeted scaffolding, dynamically skipped during challenge actions.
    4. **Deterministic Decision Engine**: Executes mastery update rule and action routing across explain, practice, remediate, and challenge.
  - Prominent direct action button on the card linking directly to open or download `Personalized_Agent_Final.pdf`.
  - Clicking elsewhere on the card or pressing `Enter`/`Space` opens the modal dialog with the complete research breakdown, 4-component agent topology details, empirical benchmarks, and conference publication info.
- **Featured Engineering Section**: Displays the 4 primary projects (FXsonic, FXbatch, Breachpoint, HandFlow Engine).
  - **FXsonic & FXbatch**: Clicking opens their respective modal preview, with an outbound link to GitHub inside the modal footer.
  - **Breachpoint & HandFlow Engine**: Clicking opens their respective modal dialogs detailing internal architecture and prototype status.
- **Section Footer**: Below the four project cards, the button navigates to `projects.html`.
- **Contact & Footer Section**:
  - Dedicated **Curriculum Vitae / Resume** hub replacing legacy QR scan card.
  - Dual action buttons: "Download 1-Page CV (PDF)" (`Joel_Lal_Resume_1Page_CareerFair.pdf`) and "Download Full 2-Page CV (PDF)" (`Joel_Lal_Resume_2Page_CareerFair.pdf`).

### 3.2 Projects Catalogue Page (`projects.html`)
- **Visual Identity**: Full parity with `index.html` (same sticky header, navigation tokens, background gradients, typography, and footer).
- **Navigation**: The brand mark links back to `index.html`. Nav links route back to `#research`, `#work`, and `#contact` on `index.html`, while `Projects` is marked active.
- **Catalog Grid**: Displays all 6 primary engineering projects (FXsonic, FXbatch, Breachpoint, HandFlow Engine, Hearth AI, Space42 AI Job Portal).
- **Interactions**: Every card triggers a modal dialog with full architectural highlights and repository or status notices.

---

## 4. Research Publication Specification & Metadata

### Item: ITT 2026 Conference Paper
- **ID**: `itt2026`
- **Display Title**: Adaptive Multi-Agent Framework for Personalised Learning Support
- **Category Eyebrow**: Academic Research / Multi-Agent LLMs
- **Venue & Host**: 12th International Conference on Information Technology Trends (ITT 2026), Higher Colleges of Technology (HCT Dubai)
- **Presentation Date**: October 2026
- **Status**: Peer-Reviewed / Conference Proceedings in Publication
- **Status Type**: `green`
- **Origin Badge**: ITT 2026 Conference Paper
- **Authorship**: Co-Author & Oral Presenter
- **Summary**:
  A lightweight multi-agent framework for personalised learning support in which a deterministic, rule-based decision engine uses the learner's current state to select the next instructional action and selectively activate only the agents required for it, minimizing resource usage and token latency.
- **Technical Architecture & Highlights**:
  - **Four-Component Topology**:
    - **Learner Analysis Agent**: Analyzes student learning misconceptions, error patterns, and calculates recommended difficulty progression based on tracked learning history.
    - **Assessment Agent**: Evaluates learner response accuracy, assigns response scores, generates granular pedagogical feedback, and selects the next assessment item.
    - **Tutor / Remediation Agent**: Provides targeted Socratic scaffolding and conceptual remediation, dynamically skipped during challenge actions to conserve compute.
    - **Deterministic Decision Engine**: Executes the mastery update rule (initial mastery 0.50) and state-based action routing across four instructional modes: explain, practice, remediate, and challenge.
  - **Deterministic State-Based Routing**: Replaces unconstrained LLM routing with deterministic code execution that tracks mastery updates, error counts, and recent misconceptions to route actions across four modes without latency penalties.
  - **Selective Agent Activation**: Eliminates redundant multi-agent invocations by skipping the Tutor/Remediation agent during challenge actions, achieving significant reductions in LLM calls, token usage, and latency compared to fixed multi-agent baselines.
  - **Empirical Benchmark & Evaluation**: Validated on 84 evaluated interactions across scripted learner profiles (strong, moderate, weak mastery) using Gemma 3 4B execution model and Gemma 3 12B automated LLM judge on AMD Ryzen 9 9950X / RTX 4070 SUPER hardware.
- **Research Paper PDF**: `Personalized_Agent_Final.pdf` (available via direct open/download buttons on card and modal dialog)
- **Tech Stack & Methodologies**: Multi-Agent Orchestration, Deterministic Decision Engine, Selective Agent Activation, Foundation LLMs (Gemma 3), Educational Scaffolding, Automated LLM Judge
- **Action Footer Notice**: Presented at Higher Colleges of Technology (HCT Dubai) — Official Conference Proceedings In Publication

---

## 5. Complete Project Metadata & Specifications

### Project 1: FXsonic
- **ID**: `fxsonic`
- **Display Name**: FXsonic
- **Category Eyebrow**: 01 / Audio Engine & DSP
- **Project Origin**: Open Source Organization (FXcodez)
- **Status**: Active Open Source
- **Status Type**: `accent`
- **Summary**: High-performance audio processing suite and algorithmic manipulation pipeline built in Python, optimizing batch normalization and real-time DSP filtering.
- **Architecture Highlights**:
  - Modular Python routines engineered for multi-format audio conversion and stream manipulation.
  - Signal normalization algorithms designed to minimize audio buffer latency during batch passes.
  - Standardized CLI parameters and automated pipeline integration across organizational repositories.
- **Tech Stack**: Python, Audio DSP, NumPy, CLI Architecture, Open Source
- **Repository URL**: `https://github.com/FXcodez/FXsonic`
- **Action Footer Notice**: None (outbound button to GitHub repository)

### Project 2: FXbatch
- **ID**: `fxbatch`
- **Display Name**: FXbatch
- **Category Eyebrow**: 02 / System Automation
- **Project Origin**: Open Source Organization (FXcodez)
- **Status**: Active Open Source
- **Status Type**: `accent`
- **Summary**: Automated batch workflow execution engine designed for scheduled multi-file conversions, system background orchestration, and developer automation.
- **Architecture Highlights**:
  - Core batch automation engine featuring robust exception handling and automated rollback states.
  - Data integrity validation routines preventing data loss during bulk asset conversions.
  - Modular configuration schemas allowing user-defined transformation rules and logging outputs.
- **Tech Stack**: Python, Automation, Threading, CLI Tooling, Open Source
- **Repository URL**: `https://github.com/FXcodez/FXbatch`
- **Action Footer Notice**: None (outbound button to GitHub repository)

### Project 3: Breachpoint
- **ID**: `breachpoint`
- **Display Name**: Breachpoint
- **Category Eyebrow**: 03 / Cybersecurity & AI
- **Project Origin**: Independent Outreach Project
- **Status**: Active Prototype (Educational Outreach)
- **Status Type**: `red`
- **Summary**: Interactive Capture-The-Flag training platform engineered for cybersecurity student literacy, pairing realistic simulated attacks with an embedded guidance AI.
- **Architecture Highlights**:
  - Realistic simulated webmail sandbox demonstrating phishing vectors, payload analysis, and credential harvesting.
  - Embedded "BreachBot" guidance AI that supplies context-aware hint scaffolding without leaking flag values.
  - Isolated browser-based challenge architecture preventing local environment execution vulnerabilities.
- **Tech Stack**: Python, Cybersecurity, CTF Architecture, AI Scaffolding, Threat Modeling
- **Repository URL**: None
- **Action Footer Notice**: Internal Prototype / Staged for Outreach

### Project 4: HandFlow Engine
- **ID**: `handflow`
- **Display Name**: HandFlow Engine
- **Category Eyebrow**: 04 / Computer Vision & HCI
- **Project Origin**: Independent Systems Project
- **Status**: Hardware Testbed (Ongoing R&D)
- **Status Type**: `accent`
- **Summary**: Real-time touchless human-computer interface mapping camera tracking data into smooth cursor motions and gesture triggers.
- **Architecture Highlights**:
  - Optical 21-landmark hand tracking running at 30+ frames per second via MediaPipe.
  - Contrast Limited Adaptive Histogram Equalization (CLAHE) preprocessing for illumination stability in dim lighting.
  - Adaptive exponential smoothing filter designed to eliminate cursor jitter without causing tracking latency.
- **Tech Stack**: Python, OpenCV, MediaPipe, CLAHE, HCI Design
- **Repository URL**: None
- **Action Footer Notice**: Hardware Testbed Prototype // Ongoing R&D

### Project 5: Hearth AI
- **ID**: `hearth`
- **Display Name**: Hearth AI
- **Category Eyebrow**: 05 / Telemetry & Machine Learning
- **Project Origin**: Academic Project (Murdoch University Dubai)
- **Status**: Research Prototype
- **Status Type**: `green`
- **Summary**: End-to-end health monitoring and telemetry pipeline integrating synthetic biometric data streams, modular hardware loggers, and predictive models.
- **Architecture Highlights**:
  - Synthetic streaming pipeline simulating continuous multi-variable biometric sensor feeds.
  - Modular hardware adapter interfaces designed to evaluate data logging throughput and fault isolation.
  - Predictive machine learning classification models identifying anomalous vital sign deviation thresholds.
- **Tech Stack**: Python, Machine Learning, Data Streaming, Telemetry, Synthetic Datasets
- **Repository URL**: None
- **Action Footer Notice**: Academic Coursework Prototype // Research Staged

### Project 6: Space42 AI Job Portal
- **ID**: `space42`
- **Display Name**: Space42 AI Job Portal
- **Category Eyebrow**: 06 / Asynchronous Prototype
- **Project Origin**: GDG Hackathon (University of Birmingham Dubai)
- **Status**: Hackathon Project
- **Status Type**: `accent`
- **Summary**: AI-powered recruitment engine featuring role-based candidate routing, asynchronous resume parsing, and a secure upload gateway.
- **Architecture Highlights**:
  - Dedicated "airlock.py" upload gateway featuring input sanitization and payload validation against prompt injection attacks.
  - Offloaded CPU-heavy resume text extraction into non-blocking asynchronous background threads to eliminate UI freezing.
  - Automated candidate assessment workflow evaluating candidate qualifications against dynamic job specifications.
- **Tech Stack**: Python, Flet UI, SQLite, Asyncio / Worker Threads, Input Sanitization
- **Repository URL**: None
- **Action Footer Notice**: GDG Hackathon (University of Birmingham Dubai) // Asynchronous Prototype
