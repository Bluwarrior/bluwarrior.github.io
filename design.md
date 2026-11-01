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
- **Dim Labels / Monospace (`--dim`)**: `#5A6377` (Muted slate)
- **Primary Accent (`--accent`)**: `#7C8CFF` (Electric periwinkle/violet)
- **Accent Soft Glow (`--accent-soft`)**: `#C2CAFF` (Lavender glow)
- **Status Green (`--green`)**: `#3DDC97` (Emerald active indicator)
- **Status Red (`--red`)**: `#FF6B6B` (Coral crimson warning)

### 1.2 Typography
- **Primary Interface Font**: `Inter`, system-ui, -apple-system, sans-serif
- **Code, Data & Monospace Font**: `JetBrains Mono`, ui-monospace, monospace
- **Micro Labels**: Uppercase, 8px to 9.5px, letter-spacing 0.12em to 0.2em, Monospace
- **Card Headings**: 21px to 25px, font-weight 600, letter-spacing -0.025em, Inter
- **Body Descriptions**: 13.5px to 14.5px, line-height 1.6 to 1.75, Inter

### 1.3 Container & Elevation Specs
- **Card Corner Radius**: 18px
- **Pill / Button Corner Radius**: 6px to 9px (buttons), 999px (status badges)
- **Card Hover State**: Translate Y -4px, border color transition to accent alpha, box shadow expansion
- **Backdrop Blur Filter**: 14px to 16px blur on headers and modals

---

## 2. Interaction & Component Behavior

### 2.1 Modal Dialog Architecture
Both `index.html` and `projects.html` must share an accessible, responsive modal dialog:
- **Backdrop**: Covers the full viewport, fixed positioning, semi-transparent background (`rgba(5, 8, 15, 0.8)`), backdrop blur filter (14px).
- **Dialog Container**: Centered horizontally and vertically, maximum width 620px, card corner radius (18px), midnight navy surface (`#0C1220`), subtle violet border line.
- **Dismiss Triggers**:
  - Top-right close button (`✕`)
  - Clicking anywhere on the blurred backdrop outside the dialog box
  - Pressing the keyboard `Escape` key
- **Scroll Lock**: The body document scroll must be locked when the modal is active.

### 2.2 Modal Content Structure
Each modal dialog must display:
1. **Badges Row**:
   - Origin Chip (e.g., `Open Source Tooling`, `Academic Research Prototype`, `GDG Hackathon Build`, `Independent Project`).
   - Development Status Pill (e.g., `Active Open Source`, `Functional Prototype`, `Hardware Testbed`).
2. **Title**: Project name in bold header font.
3. **Subtitle**: One-line domain descriptor in monospace font.
4. **Description**: Concise high-level summary of what the system does.
5. **Technical Architecture & Highlights**: Bulleted list detailing algorithms, system modules, data pipelines, or security mechanisms.
6. **Tech Stack Chips**: Specific programming languages, frameworks, and protocols used.
7. **Action Footer**:
   - For projects with active public code: A prominent button linking directly to the GitHub repository.
   - For internal/academic projects: A styled badge indicating `Internal Prototype / Staged for Outreach` or `Source Available Upon Request`.

---

## 3. Page Routing & Interaction Rules

### 3.1 Landing Page (`index.html`)
- **Featured Engineering Section**: Displays the existing 4 projects (FXsonic, FXbatch, Breachpoint, HandFlow Engine).
- **Click Behavior on Landing Page**:
  - **FXsonic & FXbatch**: Retain direct outbound link functionality to their GitHub repositories (`https://github.com/FXcodez/FXsonic` and `https://github.com/FXcodez/FXbatch`).
  - **Breachpoint & HandFlow Engine**: Intercept click events to prevent external navigation and open their respective modal dialog with full project details and origin disclosures.
- **Section Footer**: Below the four project cards, include a prominent button labeled `Explore All Projects & Architecture Specs →` that navigates to `projects.html`.

### 3.2 Projects Catalogue Page (`projects.html`)
- **Visual Identity**: Shares 100% visual parity with `index.html` (same sticky header, navigation tokens, background gradients, typography, and footer).
- **Navigation Update**: The header brand mark links back to `index.html`. Navigation items route to `index.html` sections (`Research`, `Contact`), while `Projects` is marked active.
- **Project Grid Scope**: Displays all 6 primary engineering projects:
  1. FXsonic
  2. FXbatch
  3. Breachpoint
  4. HandFlow Engine
  5. Hearth AI
  6. Space42 AI Job Portal
- **Click Behavior on `projects.html`**:
  - **All cards are interactive**: Clicking any card opens the modal dialog.
  - **FXsonic & FXbatch Modal Behavior**: Clicking their cards opens the modal first, displaying their full architecture breakdown. Inside the modal footer, an action button provides the external link to GitHub.

---

## 4. Complete Project Metadata & Specifications

### Project 1: FXsonic
- **Display Name**: FXsonic
- **Category Eyebrow**: Audio Engine & DSP
- **Project Origin**: Open Source Organization (FXcodez)
- **Status**: Active Open Source
- **Summary**: High-performance audio processing suite and algorithmic manipulation pipeline built in Python, optimizing batch normalization and real-time DSP filtering.
- **Architecture Highlights**:
  - Modular Python routines engineered for multi-format audio conversion and stream manipulation.
  - Signal normalization algorithms designed to minimize audio buffer latency during batch passes.
  - Standardized CLI parameters and automated pipeline integration across organizational repositories.
- **Tech Stack**: Python, Audio DSP, NumPy, CLI Architecture, Open Source
- **Repository URL**: `https://github.com/FXcodez/FXsonic`

### Project 2: FXbatch
- **Display Name**: FXbatch
- **Category Eyebrow**: System Automation
- **Project Origin**: Open Source Organization (FXcodez)
- **Status**: Active Open Source
- **Summary**: Automated batch workflow execution engine designed for scheduled multi-file conversions, system background orchestration, and developer automation.
- **Architecture Highlights**:
  - Core batch automation engine featuring robust exception handling and automated rollback states.
  - Data integrity validation routines preventing data loss during bulk asset conversions.
  - Modular configuration schemas allowing user-defined transformation rules and logging outputs.
- **Tech Stack**: Python, Automation, Threading, CLI Tooling, Open Source
- **Repository URL**: `https://github.com/FXcodez/FXbatch`

### Project 3: Breachpoint
- **Display Name**: Breachpoint
- **Category Eyebrow**: Cybersecurity & AI
- **Project Origin**: Independent Outreach Project
- **Status**: Active Prototype (Educational Outreach)
- **Summary**: Interactive Capture-The-Flag training platform engineered for cybersecurity student literacy, pairing realistic simulated attacks with an embedded guidance AI.
- **Architecture Highlights**:
  - Realistic simulated webmail sandbox demonstrating phishing vectors, payload analysis, and credential harvesting.
  - Embedded "BreachBot" guidance AI that supplies context-aware hint scaffolding without leaking flag values.
  - Isolated browser-based challenge architecture preventing local environment execution vulnerabilities.
- **Tech Stack**: Python, Cybersecurity, CTF Architecture, AI Scaffolding, Threat Modeling
- **Repository URL**: None (Internal Outreach Prototype)

### Project 4: HandFlow Engine
- **Display Name**: HandFlow Engine
- **Category Eyebrow**: Computer Vision & HCI
- **Project Origin**: Independent Systems Project
- **Status**: Hardware Testbed (Ongoing R&D)
- **Summary**: Real-time touchless human-computer interface mapping camera tracking data into smooth cursor motions and gesture triggers.
- **Architecture Highlights**:
  - Optical 21-landmark hand tracking running at 30+ frames per second via MediaPipe.
  - Contrast Limited Adaptive Histogram Equalization (CLAHE) preprocessing for illumination stability in dim lighting.
  - Adaptive exponential smoothing filter designed to eliminate cursor jitter without causing tracking latency.
- **Tech Stack**: Python, OpenCV, MediaPipe, CLAHE, HCI Design
- **Repository URL**: None (Hardware Testbed Prototype)

### Project 5: Hearth AI
- **Display Name**: Hearth AI
- **Category Eyebrow**: Telemetry & Machine Learning
- **Project Origin**: Academic Project (Murdoch University Dubai)
- **Status**: Research Prototype
- **Summary**: End-to-end health monitoring and telemetry pipeline integrating synthetic biometric data streams, modular hardware loggers, and predictive models.
- **Architecture Highlights**:
  - Synthetic streaming pipeline simulating continuous multi-variable biometric sensor feeds.
  - Modular hardware adapter interfaces designed to evaluate data logging throughput and fault isolation.
  - Predictive machine learning classification models identifying anomalous vital sign deviation thresholds.
- **Tech Stack**: Python, Machine Learning, Data Streaming, Telemetry, Synthetic Datasets
- **Repository URL**: None (Academic Coursework Prototype)

### Project 6: Space42 AI Job Portal
- **Display Name**: Space42 AI Job Portal
- **Category Eyebrow**: AI Recruitment & Web Security
- **Project Origin**: GDG Hackathon (University of Birmingham Dubai)
- **Status**: Competition Prototype (Award Finalist)
- **Summary**: AI-powered recruitment engine featuring role-based candidate routing, asynchronous resume parsing, and a secure upload gateway.
- **Architecture Highlights**:
  - Dedicated "airlock.py" upload gateway featuring input sanitization and payload validation against prompt injection attacks.
  - Offloaded CPU-heavy resume text extraction into non-blocking asynchronous background threads to eliminate UI freezing.
  - Automated candidate assessment workflow evaluating candidate qualifications against dynamic job specifications.
- **Tech Stack**: Python, Flet UI, SQLite, Asyncio / Worker Threads, Input Sanitization
- **Repository URL**: None (Hackathon Competition Prototype)