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
   - For peer-reviewed research: Structured badge indicating conference presentation and forthcoming proceedings publication.
   - For internal/academic prototypes: Styled badge indicating prototype availability upon request.

### 2.3 Mobile & Responsive Navigation
- **Navigation Toggle & Drawer**: Below 1180px, the header displays an accessible toggle button (`#navToggle`) and slide-over navigation drawer (`#mobileNav`).
- **Touch Target Floor**: All interactive buttons adhere to the WCAG 44×44px minimum touch target size.

---

## 3. Page Routing & Interaction Rules

### 3.1 Landing Page (`index.html`)
- **Research Section**:
  - The research card (`Adaptive Multi-Agent Framework for Personalised Learning Support`) must be **interactive** (`card--interactive`, `role="button"`, `tabindex="0"`, `data-research="itt2026"`).
  - Hovering triggers elevated card styling (`transform: translateY(-4px)`, accent border glow).
  - Clicking or pressing `Enter`/`Space` opens the modal dialog with the complete research breakdown, agent pipeline details, and conference publication info.
- **Featured Engineering Section**: Displays the 4 primary projects (FXsonic, FXbatch, Breachpoint, HandFlow Engine).
  - **FXsonic & FXbatch**: Clicking opens their respective modal preview, with an outbound link to GitHub inside the modal footer.
  - **Breachpoint & HandFlow Engine**: Clicking opens their respective modal dialogs detailing internal architecture and prototype status.
- **Section Footer**: Below the four project cards, the button `Explore All Projects & Architecture Specs →` navigates to `projects.html`.

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
  An autonomous multi-agent orchestration architecture utilizing specialized collaborative LLM agents to dynamically evaluate student learning trajectories, calibrate problem difficulty in real time, and deliver adaptive pedagogical scaffolding without solution leakage.
- **Technical Architecture & Highlights**:
  - **Tri-Agent Modular Topology**:
    - **Agent 01 (Trajectory Diagnosis)**: Analyzes real-time user code submissions and query histories to map competency gaps against standard knowledge graphs.
    - **Agent 02 (Difficulty Calibration)**: Dynamically adjusts task complexity parameters and problem constraints based on cognitive load indicators and error frequencies.
    - **Agent 03 (Contextual Scaffolding)**: Generates progressive, Socratic hints and conceptual nudges designed to support problem-solving while strictly preventing direct solution disclosure.
  - **Prompt Strategy & Task Decomposition**: Systematically evaluated chain-of-thought, role-constrained, and least-to-most prompting techniques across multiple foundation models to minimize inter-agent latency.
  - **Hallucination Mitigation**: Implemented strict cross-agent state verification where the Scaffolding Agent cross-references the Diagnosis Agent's state before emitting responses to the student.
  - **Empirical Evaluation**: Conducted benchmark testing across varying student cohort simulation scenarios to measure pedagogical relevance, intervention accuracy, and response consistency.
- **Tech Stack & Methodologies**: Multi-Agent Orchestration, Foundation LLMs, Prompt Decomposition, Socratic Scaffolding, Adaptive Learning Systems, Educational Data Mining
- **Action Footer Notice**: Presented at HCT Dubai — Official Conference Proceedings Currently in Publication

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
- **Category Eyebrow**: 06 / AI Recruitment & Web Security
- **Project Origin**: GDG Hackathon (University of Birmingham Dubai)
- **Status**: Competition Prototype (Award Finalist)
- **Status Type**: `accent`
- **Summary**: AI-powered recruitment engine featuring role-based candidate routing, asynchronous resume parsing, and a secure upload gateway.
- **Architecture Highlights**:
  - Dedicated "airlock.py" upload gateway featuring input sanitization and payload validation against prompt injection attacks.
  - Offloaded CPU-heavy resume text extraction into non-blocking asynchronous background threads to eliminate UI freezing.
  - Automated candidate assessment workflow evaluating candidate qualifications against dynamic job specifications.
- **Tech Stack**: Python, Flet UI, SQLite, Asyncio / Worker Threads, Input Sanitization
- **Repository URL**: None
- **Action Footer Notice**: Hackathon Competition Prototype // Award Finalist