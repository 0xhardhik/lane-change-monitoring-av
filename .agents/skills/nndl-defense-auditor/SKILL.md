---
name: nndl-defense-auditor
description: Automated audit, geometric bounding verification, tabular literature validation, and Viva Voce defense rubric for 24CSE473 Neural Networks and Deep Learning lane change monitoring project.
---

# NNDL Defense & Quality Audit Rubric

## Project Metadata
- **Course**: 24CSE473 — Neural Networks and Deep Learning
- **Student**: Hardhik A | **Register Number**: CH.SC.U4CSE23114
- **Institution**: Department of Computer Science & Engineering, Amrita Vishwa Vidyapeetham
- **Topic**: Monitoring Lane Changes in Autonomous Vehicles: Deep Learning Frameworks for Maneuver Observation and Trajectory Validation

## Automated Audit Invariants & Quality Standards

### 1. Presentation Geometric Bounds
- Slide Dimensions: 16:9 Widescreen standard ($13.333'' \times 7.500''$).
- Maximum coordinate limits for all slide shapes:
  - Width boundary: $x + w \le 13.334''$
  - Height boundary: $y + h \le 7.501''$
- Zero overlap between adjacent card containers (minimum spacing $\ge 0.18''$).
- Student credentials (`Hardhik A | CH.SC.U4CSE23114 | 24CSE473`) must appear on all title slides and running footers.

### 2. Multi-Milestone Slide & Table Structure
- **Phase 1: Project Proposal** (`Phase1_Project_Proposal.pptx`): Exactly 7 slides. Modeled after `atm_security_slides.pptx`.
- **Phase 2: Literature Review** (`Phase2_Literature_Review.pptx`): Exactly 9 slides. Modeled after `ATM_Security_2nd_Review.pptx`.
  - Slides 2–5 MUST be 4 dedicated structured literature review tables covering 16 peer-reviewed papers across:
    1. Kinematic & Rule-Based Models (MOBIL, Vogel, EKF, Oliver HMM)
    2. Spatial Perception & Vision Detectors (YOLOv4/v8, SCNN, Mask R-CNN, Ultra-Fast Lane)
    3. Recurrent & Temporal Deep Learning (Khairdoost LSTM, Altche BiLSTM, Xing GRU, Park Seq2Seq)
    4. Graph Neural Networks & Transformers (ST-GCN, VectorNet, Trajectory Transformer, Scene Transformer/UniAD)
  - Slide 6: Frontier Paradigms (2024–2026).
  - Slide 7: Synthesized Research Gaps.
  - Slide 8: 4-Tier Deep Learning Architecture.
  - Slide 9: 7-Stage End-to-End Operational Lifecycle.
- **Phase 3: Final Project Defense** (`Phase3_Final_Presentation.pptx`): Exactly 21 slides. Modeled after `Beige Illustrated Research Presentation.pdf`.
  - Slides 7–10 MUST be 4 dedicated 6-column tables covering all 16 papers.
  - Slide 14: MobileNetV3 + BiLSTM + Attention deep learning architecture.
  - Slide 15: Mathematical formulations ($P(I)$, $TTC$, $TTC_{\text{adj}}$, $TLC$, Dual-Gated Arbitration).
  - Slide 16: Tech stack, datasets (highD, CARLA), and Jetson Orin Nano hardware profiling.
  - Slide 17: 3-Class Confusion Matrix ($N = 4,000$) with precision, recall, and F1 metrics.
  - Slide 18: Comparative Performance Benchmark Table across 6 capabilities.
  - Slide 19: Environmental Robustness, Edge Cases & ISO 26262 ASIL-B compliance.
  - Slide 20: Future Roadmap, V2X Integration & MoRTH 2026/2027 Guidelines.
  - Slide 21: Conclusion & Academic Defense Q&A.

### 3. Interactive Demonstration Suite Verification Checklist
- Located at `C:\Users\ahard\.gemini\antigravity\scratch\lane_change_project\demo\`.
- Headless execution command: `python demo_lane_monitor.py --test-mode`.
- **Scenario 1 (Normal Cruise)**:
  - $P(\text{Keep Lane}) = 1.00$, $TTC > 10.0\text{s}$, stable longitudinal distance, green Advisory state.
- **Scenario 2 (Aggressive Cut-In)**:
  - Advance warning lead time $\ge 1.8\text{s}$.
  - Level 2 Caution ($-0.15g$ ACC rollback) triggers as lateral drift begins.
  - Level 3 Emergency AEB ($-0.8g$ hydraulic braking) engages at critical TTC threshold.
  - Ego vehicle smoothly stabilizes at $\sim 14\text{m}$ trailing headway without vehicle teleportation.
- **Scenario 3 (Aborted Swerve / Recovery)**:
  - Adjacent vehicle drifts towards ego lane, triggering initial caution.
  - Driver swerves back ($v_y$ sign reversal detected within $120\text{ms}$).
  - Safety validation layer immediately vetoes neural threat, restoring green status with zero phantom braking.
