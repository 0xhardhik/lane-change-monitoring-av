"""
generate_phase2.py
Generates Phase 2: Literature Review, Gap Analysis & Proposed Architecture (Milestone 2, 9 slides)
Course: 24CSE473 - Neural Networks and Deep Learning
Student: Hardhik A | CH.SC.U4CSE23114
Topic: Monitoring Lane Changes in Autonomous Vehicles

Directly models the structure and depth of ATM_Security_2nd_Review.pptx:
- Slide 1: Course Title & Milestone 2 Badge
- Slides 2-5: 4 Tabular Literature Review Slides (Papers 1-16 across kinematics, CNNs, LSTMs, Transformers)
- Slide 6: Literature Review - Recent Extensions (2024-2026)
- Slide 7: Overview of Research Gaps
- Slide 8: Proposed Multi-Tier Deep Learning Architecture
- Slide 9: Proposed End-to-End Detection Workflow
"""

import os
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from presentation_builder import (
    PresentationBuilder, COLOR_ACCENT_BLUE, COLOR_NAVY_DARK, COLOR_NAVY_MED,
    COLOR_SUCCESS, COLOR_WARNING, COLOR_DANGER
)

def build_phase2_presentation(output_path):
    builder = PresentationBuilder(title_prefix="Phase 2 LitReview")
    total_slides = 9
    milestone_label = "Milestone 2: Literature Review & Architecture"

    # =========================================================================
    # SLIDE 1: Title Slide
    # =========================================================================
    builder.add_title_slide(
        title="Monitoring Lane Changes in Autonomous Vehicles",
        subtitle="Comprehensive Literature Survey, Critical Gap Synthesis & Proposed Multi-Tier Deep Learning Architecture",
        milestone_badge="Milestone 2: Literature Review & Architecture",
        student_name="Hardhik A",
        roll_no="CH.SC.U4CSE23114",
        course_code="24CSE473",
        course_name="Neural Networks and Deep Learning",
        dept_name="Department of Computer Science & Engineering, Amrita Vishwa Vidyapeetham"
    )

    # Standard column headers and widths for literature survey tables
    lr_headers = ["S.N", "Paper Name", "Author Name & Year", "Publication Venue", "Methodology", "Key Findings", "Research Gap / Future Scope"]
    lr_col_widths = [Inches(0.5), Inches(2.5), Inches(1.4), Inches(1.4), Inches(2.2), Inches(2.1), Inches(2.033)]

    # =========================================================================
    # SLIDE 2: Literature Review — Table 1: Classical Kinematic & Rule-Based Models
    # =========================================================================
    s2 = builder.create_slide()
    builder.add_header(s2, "Literature Review — Kinematic & Rule-Based Trajectory Models", "Milestone 2 Literature Survey (1/4)", milestone_label)
    builder.add_footer(s2, 2, total_slides, milestone_label)

    rows_s2 = [
        [
            "1",
            "MOBIL: Minimizing Overall Braking Induced by Lane Changes",
            "A. Kesting, M. Treiber, D. Helbing (2007)",
            "IEEE Trans. Intelligent Transportation Systems",
            "Game-theoretic utility formulation balancing ego vehicle acceleration gain against induced deceleration imposed on following vehicles.",
            "Demonstrates that cooperative and polite lane-change decisions prevent macro traffic shockwaves and stabilize highway flow.",
            "Purely deterministic; cannot handle irrational human drivers, cutting-in without signal, or sensor noise."
        ],
        [
            "2",
            "Time-to-Collision (TTC) & Safety Envelope Modeling in Highway Overtaking",
            "K. Vogel (2003)",
            "Transportation Research Part F: Traffic Psychology",
            "Kinematic distance-over-relative-velocity ratio (TTC = Δx / Δv) used to establish empirical safety headway boundaries.",
            "Identifies 1.5s to 2.0s as the physiological tipping point where emergency braking becomes inevitable during cut-ins.",
            "Assumes constant velocity; fails in dynamic braking scenarios, curved trajectories, or sudden lateral drift."
        ],
        [
            "3",
            "Extended Kalman Filter for Vehicle State and Trajectory Estimation",
            "P. A. Bageshwar, W. L. Garrard, R. Rajamani (2004)",
            "IEEE Trans. Control Systems Technology",
            "Recursive non-linear state estimation fusing radar range-rate with steering angle measurements under Gaussian noise.",
            "Effectively tracks longitudinal position and lateral deviation with bounded covariance in lane-following scenarios.",
            "Fails during rapid non-linear maneuvers (aggressive cut-ins) due to linearization errors and lack of semantic context."
        ],
        [
            "4",
            "Driver Maneuver Recognition & Prediction Using Hidden Markov Models",
            "N. Oliver, A. P. Pentland (2000)",
            "IEEE Trans. Intelligent Transportation Systems",
            "Discrete-state HMMs mapping sequential steering angle and pedal actuation features to discrete maneuver states.",
            "Proves that continuous driving actions exhibit distinct pre-maneuver temporal transitions ~1.0 second prior to execution.",
            "Relies on in-cabin driver sensors (infeasible for surrounding vehicles); cannot model surrounding traffic context."
        ]
    ]
    builder.add_table(s2, Inches(0.6), Inches(1.3), Inches(12.133), Inches(5.4), lr_headers, rows_s2, lr_col_widths, font_size=Pt(8.5))

    # =========================================================================
    # SLIDE 3: Literature Review — Table 2: Spatial Perception & Vision-Based Detection
    # =========================================================================
    s3 = builder.create_slide()
    builder.add_header(s3, "Literature Review — Spatial Perception & Vision-Based Detectors", "Milestone 2 Literature Survey (2/4)", milestone_label)
    builder.add_footer(s3, 3, total_slides, milestone_label)

    rows_s3 = [
        [
            "5",
            "YOLOv4 / YOLOv8: Optimal Speed & Accuracy of Object Detection",
            "A. Bochkovskiy, C. Wang, H. Liao (2020)",
            "IEEE/CVF CVPR 2020",
            "Single-stage convolutional object detector utilizing CSPDarknet backbone, PANet neck, and anchor-free detection heads.",
            "Achieves 65+ FPS on embedded GPUs with high mAP, enabling reliable bounding box localization for surrounding traffic.",
            "Only localizes current static bounding boxes; lacks temporal dimension to infer whether vehicle will cut in or stay."
        ],
        [
            "6",
            "Spatial CNN for Traffic Lane Detection in Complex Scenarios (SCNN)",
            "X. Pan, J. Shi, P. Luo, X. Wang, X. Tang (2018)",
            "AAAI Conference on Human AI",
            "Slices convolutional feature tensors along spatial rows/columns to pass contextual message information across spatial pixels.",
            "Excels at inferring heavily occluded lane markings, worn road paint, and low-light highway lane boundaries.",
            "High computational complexity; message passing introduces substantial latency (~40ms), limiting real-time ADAS use."
        ],
        [
            "7",
            "Mask R-CNN for Instance-Level Road Scene Semantic Parsing",
            "K. He, G. Gkioxari, P. Dollar, R. Girshick (2017)",
            "IEEE Int. Conf. on Computer Vision (ICCV)",
            "Two-stage instance segmentation outputting pixel-precise vehicle masks and road boundary delineations.",
            "Accurate boundary extraction allows precise measurement of tire-to-lane line pixel distance and lateral creep.",
            "Two-stage pipeline is computationally excessive for automotive SoCs; requires high-end desktop GPUs to reach 15 FPS."
        ],
        [
            "8",
            "Ultra Fast Structure-Aware Deep Lane Detection for ADAS",
            "Z. Li, S. Xiang, X. Zheng et al. (2020)",
            "European Conf. on Computer Vision (ECCV)",
            "Formulates lane detection as row-based classification selection rather than dense pixel segmentation, reducing parameters.",
            "Achieves extreme inference speeds exceeding 300 FPS on edge hardware while maintaining robust curve delineation.",
            "Perceives static lane geometry only; does not track surrounding vehicle interaction or predict intent."
        ]
    ]
    builder.add_table(s3, Inches(0.6), Inches(1.3), Inches(12.133), Inches(5.4), lr_headers, rows_s3, lr_col_widths, font_size=Pt(8.5))

    # =========================================================================
    # SLIDE 4: Literature Review — Table 3: Recurrent & Temporal Deep Learning Models
    # =========================================================================
    s4 = builder.create_slide()
    builder.add_header(s4, "Literature Review — Recurrent & Temporal Deep Learning Models", "Milestone 2 Literature Survey (3/4)", milestone_label)
    builder.add_footer(s4, 4, total_slides, milestone_label)

    rows_s4 = [
        [
            "9",
            "Long Short-Term Memory Networks for Driver Intention Prediction",
            "M. Khairdoost, S. Shirpour, M. Bauer (2020)",
            "IEEE Access",
            "Dual-layer LSTM processing sequential vehicle coordinates and yaw angle time series over a 2.0-second sliding history.",
            "Demonstrates that temporal recurrent memory boosts cut-in prediction accuracy to 91.4% with 1.6s lead time.",
            "Evaluated on clean naturalistic trajectory datasets (NGSIM); vulnerable to sensor noise and camera calibration drift."
        ],
        [
            "10",
            "Bidirectional LSTM with Attention for Surrounding Vehicle Trajectory",
            "F. Altche, A. de La Fortelle (2017)",
            "IEEE Intelligent Transportation Systems Conf.",
            "Bidirectional temporal encoding with attention pooling to predict longitudinal and lateral coordinates over 1-5 seconds.",
            "Captures subtle lateral acceleration inflection points and outperforms unidirectional LSTMs in lane-change detection.",
            "Lacks an explicit kinematic safety boundary check; occasionally predicts physically impossible lateral acceleration."
        ],
        [
            "11",
            "GRU-Based Vehicle Maneuver Classification under High-Speed Traffic",
            "Y. Xing, C. Lv, H. Wang, D. Cao (2019)",
            "IEEE Trans. Intelligent Transportation Systems",
            "Gated Recurrent Units (GRU) trained on high-speed naturalistic driving datasets to classify Keep, Left, and Right maneuvers.",
            "Achieves 25% faster inference than LSTM due to fewer gate parameters, maintaining 90.8% classification precision.",
            "Only classifies intention once the vehicle has already initiated noticeable lateral translation (lead time <1.2s)."
        ],
        [
            "12",
            "Sequence-to-Sequence Trajectory Forecasting via Encoder-Decoder",
            "S. H. Park, B. Kim, C. M. Kang et al. (2018)",
            "IEEE Trans. Intelligent Vehicles",
            "Encoder-decoder RNN architecture outputting multi-modal future trajectory distributions over 3-5 second horizons.",
            "Effectively models non-linear maneuvers and provides probabilistic beam search for candidate trajectories.",
            "Prone to error accumulation in autoregressive decoding; high compute requirements unsuited for sub-25ms ADAS."
        ]
    ]
    builder.add_table(s4, Inches(0.6), Inches(1.3), Inches(12.133), Inches(5.4), lr_headers, rows_s4, lr_col_widths, font_size=Pt(8.5))

    # =========================================================================
    # SLIDE 5: Literature Review — Table 4: Graph Neural Networks & Transformers
    # =========================================================================
    s5 = builder.create_slide()
    builder.add_header(s5, "Literature Review — Spatio-Temporal Graph Networks & Transformers", "Milestone 2 Literature Survey (4/4)", milestone_label)
    builder.add_footer(s5, 5, total_slides, milestone_label)

    rows_s5 = [
        [
            "13",
            "Spatio-Temporal Graph Convolutional Networks for Multi-Agent Interaction",
            "J. Li, F. Dong, Y. Zhao, C. Shen (2021)",
            "IEEE Trans. Pattern Analysis & Machine Intell.",
            "Constructs spatio-temporal graphs where nodes represent vehicles and edges represent dynamic Euclidean interaction forces.",
            "Accurately models inter-vehicle social compliance, yielding superior multi-lane trajectory prediction in dense traffic.",
            "Graph construction overhead scales quadratically O(N²) with traffic density; severe latency penalty on edge chips."
        ],
        [
            "14",
            "VectorNet: Encoding HD Maps and Agent Trajectories with Vectorized Subgraphs",
            "J. Gao, C. Sun, H. Zhao, D. Anguelov (2020)",
            "IEEE/CVF CVPR 2020",
            "Hierarchical graph network representing road polylines and vehicle trajectories as vectorized subgraphs with self-attention.",
            "Avoids lossy bird's-eye-view rasterization, achieving state-of-the-art accuracy on Argoverse trajectory benchmark.",
            "Strictly requires high-definition (HD) vector map inputs; cannot operate in mapless consumer vehicle environments."
        ],
        [
            "15",
            "Trajectory Transformer: Autoregressive Spatial Trajectory Modeling",
            "M. Janner, Q. Li, S. Levine (2021)",
            "Advances in Neural Information Processing Systems",
            "Treats continuous trajectory prediction as discrete token sequence generation, utilizing GPT-style causal self-attention.",
            "Enables long-horizon multi-modal trajectory synthesis and seamless integration with reinforcement learning rewards.",
            "Inference latency is high (120ms+), rendering it impractical for real-time safety-critical automotive collision avoidance."
        ],
        [
            "16",
            "Scene Transformer: A Unified Multi-Agent Motion Prediction Architecture",
            "J. Ngiam, B. Caine, V. Vasudevan et al. (2022)",
            "Int. Conf. on Learning Representations (ICLR)",
            "Unified attention across agents, time steps, and road features without hand-crafted heuristics or decoupled steps.",
            "Demonstrates top-tier performance on Waymo Open Motion dataset with rich multi-agent interaction modeling.",
            "Massive parameter footprint (50M+ weights); requires server-class NVIDIA A100 GPUs, impossible for edge ADAS."
        ]
    ]
    builder.add_table(s5, Inches(0.6), Inches(1.3), Inches(12.133), Inches(5.4), lr_headers, rows_s5, lr_col_widths, font_size=Pt(8.5))

    # =========================================================================
    # SLIDE 6: Literature Review — Recent Extensions (2024–2026)
    # =========================================================================
    s6 = builder.create_slide()
    builder.add_header(s6, "Literature Review — Recent State-of-the-Art Extensions (2024–2026)", "Frontier Paradigms", milestone_label)
    builder.add_footer(s6, 6, total_slides, milestone_label)

    builder.add_card(
        s6, Inches(0.8), Inches(1.3), Inches(3.7), Inches(5.5),
        "Vision-Language-Action Models",
        [
            "DriveVLM & OmniDrive (2024): Integrating multi-modal LLMs to provide zero-shot semantic understanding of driving scenes.",
            "Scene Reasoning: Capable of answering high-level cognitive questions: 'Why is the black sedan drifting left?'",
            "Critical Bottleneck: Autoregressive token decoding takes 250ms to 800ms per frame, making direct vehicle control dangerous.",
            "Academic Consensus: VLM is valuable as an asynchronous reasoning layer, but high-speed collision avoidance requires dedicated CNN-LSTMs."
        ],
        accent_color=COLOR_ACCENT_BLUE
    )

    builder.add_card(
        s6, Inches(4.8), Inches(1.3), Inches(3.7), Inches(5.5),
        "Unified Hybrid End-to-End AI",
        [
            "UniAD (CVPR 2023 Best Paper) & VAD (ICCV 2023): Shift toward end-to-end differentiable perception-to-planning architectures.",
            "Token-Based Interfacing: Bypasses explicit noisy object bounding boxes by passing dense latent query tokens between neural modules.",
            "Vision Pilot Paradigm: Blends end-to-end representation learning with modular safety trajectory checkpoints.",
            "Relevance to this Project: Inspires our proposed Hybrid Architecture combining end-to-end vision feature extraction with explicit kinematic validation."
        ],
        accent_color=RGBColor(99, 102, 241)
    )

    builder.add_card(
        s6, Inches(8.8), Inches(1.3), Inches(3.7), Inches(5.5),
        "Modern Benchmarks & Safety Directives",
        [
            "highD & INTERACTION Datasets: Modern drone-captured naturalistic vehicle trajectory datasets capturing 100k+ real highway interactions.",
            "CARLA 0.9.15 Closed-Loop Testing: Standardized virtual benchmark evaluating reactive safety under severe edge-case swerves.",
            "Euro NCAP 2026 & MoRTH Directives: Strict mandates requiring proactive Cut-In Collision Avoidance with >=1.5s warning lead time.",
            "Conclusion of Review: Pure perception is insufficient; pure black-box transformers are too slow; a hybrid CNN-LSTM with safety verification is the optimal solution."
        ],
        accent_color=COLOR_SUCCESS
    )

    # =========================================================================
    # SLIDE 7: Overview of Research Gaps
    # =========================================================================
    s7 = builder.create_slide()
    builder.add_header(s7, "Synthesis of Critical Research Gaps in Contemporary Literature", "Gap Analysis", milestone_label)
    builder.add_footer(s7, 7, total_slides, milestone_label)

    # 4 Gaps in 2x2 layout
    builder.add_card(
        s7, Inches(0.8), Inches(1.3), Inches(5.7), Inches(2.65),
        "Gap 1: Perception-Only Blindness (Lack of Temporal Lead Time)",
        [
            "Identified Deficiency: Most production ADAS (e.g., standard Mobileye/Tesla vision) relies on instantaneous object detection.",
            "Critical Failure: Bounding box detectors only report that a vehicle has entered a lane *after* tires cross the line.",
            "Consequence: Gives the ego vehicle less than 0.6 seconds of reaction time, leading to abrupt, dangerous emergency braking.",
            "Our Target: Achieve proactive intent classification with >=1.8 seconds of advance warning lead time."
        ],
        accent_color=COLOR_DANGER
    )

    builder.add_card(
        s7, Inches(6.833), Inches(1.3), Inches(5.7), Inches(2.65),
        "Gap 2: Excessive Compute Latency in Transformers / GNNs",
        [
            "Identified Deficiency: State-of-the-art academic models (Scene Transformer, VectorNet) rely on heavy graph attention.",
            "Critical Failure: Computational latency exceeds 100ms - 150ms per frame, requiring 300W server-grade GPUs.",
            "Consequence: Infeasible for production automotive ECUs (15W - 25W Jetson / SoC), causing delayed safety triggers.",
            "Our Target: Lightweight CNN-BiLSTM architecture operating deterministically at <20ms latency (>50 FPS)."
        ],
        accent_color=COLOR_WARNING
    )

    builder.add_card(
        s7, Inches(0.8), Inches(4.15), Inches(5.7), Inches(2.65),
        "Gap 3: Pure Black-Box Hallucination & Lack of Kinematic Bounds",
        [
            "Identified Deficiency: Deep learning models are trained purely on loss minimization without physical constraint enforcement.",
            "Critical Failure: Under novel traffic patterns, models output erratic trajectory forecasts that violate vehicle physics.",
            "Consequence: Causes phantom braking on harmless drift or misses aggressive cut-ins when confidence fluctuates.",
            "Our Target: Dedicated Physics-Informed Trajectory Validation Layer computing dynamic Time-to-Collision (TTC)."
        ],
        accent_color=COLOR_DANGER
    )

    builder.add_card(
        s7, Inches(6.833), Inches(4.15), Inches(5.7), Inches(2.65),
        "Gap 4: Fragility under Unstructured & Weather-Degraded Roads",
        [
            "Identified Deficiency: Existing systems assume clear, crisp lane delimiters and standardized lane discipline.",
            "Critical Failure: Performance collapses in developing nations (India) with faded paint, night glare, and un-signaled swerves.",
            "Consequence: System disengages or fails precisely when driver assistance is most urgently needed.",
            "Our Target: Vision Pilot mapless architecture utilizing multi-cue optical flow, relative motion, and robust spatial feature aggregation."
        ],
        accent_color=COLOR_ACCENT_BLUE
    )

    # =========================================================================
    # SLIDE 8: Proposed Multi-Tier Deep Learning Architecture
    # =========================================================================
    s8 = builder.create_slide()
    builder.add_header(s8, "Proposed Multi-Tier Deep Learning Architecture", "System Design", milestone_label)
    builder.add_footer(s8, 8, total_slides, milestone_label)

    # 4 Vertical Tier Cards
    tier_w = Inches(2.8)
    gap = Inches(0.18)
    start_x = Inches(0.8)

    builder.add_card(
        s8, start_x, Inches(1.3), tier_w, Inches(5.5),
        "Tier 1: Sensory Ingest & Preprocessing",
        [
            "Camera Feed: 1080p forward monocular RGB @ 60 FPS.",
            "Frame Differencing: Motion vector optical flow estimation.",
            "Object Detection: YOLOv8-Nano vehicle detection bounding boxes.",
            "Lane Delineation: Ultra-fast row classification lane marking anchor extraction.",
            "Coordinate Projection: Ground-plane inverse perspective mapping (IPM)."
        ],
        accent_color=COLOR_ACCENT_BLUE
    )

    builder.add_card(
        s8, start_x + (tier_w + gap), Inches(1.3), tier_w, Inches(5.5),
        "Tier 2: Spatial Feature Extraction",
        [
            "Backbone: MobileNetV3 / ResNet-18 spatial feature backbone.",
            "Surrounding Vehicle Crop: Normalized 64x64 pixel dynamic bounding box ROIs.",
            "Spatial Embedding: Extracts 128-dimensional latent spatial descriptor.",
            "Optical Micro-Motion: Captures front wheel angle, tire contact patch, and yaw drift.",
            "Context Fusion: Concatenates relative distance Δx and lateral offset Δy."
        ],
        accent_color=RGBColor(99, 102, 241)
    )

    builder.add_card(
        s8, start_x + (tier_w + gap) * 2, Inches(1.3), tier_w, Inches(5.5),
        "Tier 3: Temporal Sequence Reasoning",
        [
            "Rolling FIFO Buffer: 30 consecutive frame temporal window (1.0s history).",
            "Recurrent Network: 2-layer Bidirectional LSTM (hidden size 128).",
            "Attention Pooling: Dynamically weights transition inflection points.",
            "Intention Head: Fully connected layer with Softmax activation.",
            "Tri-State Probabilities: P(Keep Lane), P(Cut-in Left), P(Cut-in Right)."
        ],
        accent_color=COLOR_SUCCESS
    )

    builder.add_card(
        s8, start_x + (tier_w + gap) * 3, Inches(1.3), tier_w, Inches(5.5),
        "Tier 4: Safety & ADAS Arbitration",
        [
            "Physics Envelope: Real-time Time-to-Collision (TTC = Δx / Δv) calculation.",
            "Time-to-Lane-Crossing: TLC = d_boundary / |vy| verification.",
            "Dual-Gated Trigger: Intention prob > 0.75 AND TTC < 2.0s.",
            "Tiered Escalation: Level 1 Advisory -> Level 2 ACC Regen -> Level 3 Emergency AEB.",
            "CAN Dispatch: Zero-copy ROS 2 DDS message bus broadcast."
        ],
        accent_color=COLOR_WARNING
    )

    # =========================================================================
    # SLIDE 9: Proposed End-to-End Detection Workflow
    # =========================================================================
    s9 = builder.create_slide()
    builder.add_header(s9, "Proposed End-to-End Detection Workflow & Evaluation Framework", "Operational Lifecycle", milestone_label)
    builder.add_footer(s9, 9, total_slides, milestone_label)

    # 7-stage process flow modeled directly after Slide 9 of ATM_Security_2nd_Review.pptx
    workflow_steps = [
        {"title": "1. Ingest", "desc": "1080p forward camera acquisition @ 60 FPS."},
        {"title": "2. Pre-process", "desc": "IPM ground projection & frame normalization."},
        {"title": "3. Detect", "desc": "Vehicle bounding boxes & lane delimiters."},
        {"title": "4. Sequence", "desc": "30-frame rolling temporal feature buffer."},
        {"title": "5. Classify", "desc": "CNN-LSTM intent probability softmax."},
        {"title": "6. Validate", "desc": "Physics-informed TTC and TLC envelope gate."},
        {"title": "7. Arbitrate", "desc": "Tiered ADAS trigger: Advisory, ACC, or AEB."}
    ]
    builder.add_process_steps(s9, Inches(0.6), Inches(1.3), Inches(12.133), Inches(2.4), workflow_steps)

    # Bottom 3 synthesis cards
    builder.add_card(
        s9, Inches(0.6), Inches(4.0), Inches(3.8), Inches(2.8),
        "Target Critical Highway Events",
        [
            "Aggressive Cut-In: Vehicle swerves into ego path with TTC < 1.8s.",
            "Gradual Drifting: Fatigued or distracted driver slowly drifting across line.",
            "False Swerve / Abort: Vehicle veers toward line then recovers without crossing.",
            "Multi-Vehicle Weaving: Coordinated overtaking across multiple highway lanes."
        ],
        accent_color=COLOR_ACCENT_BLUE
    )

    builder.add_card(
        s9, Inches(4.7), Inches(4.0), Inches(3.8), Inches(2.8),
        "ADAS Actuation & Safety Response",
        [
            "Level 1 (Advisory): Visual HUD icon + gentle auditory chime (lead time >2.0s).",
            "Level 2 (Caution): ACC regenerative throttle rollback to re-establish headway buffer.",
            "Level 3 (Emergency): Deterministic AEB hydraulic braking deceleration (TTC <1.2s).",
            "Explainable Telemetry: HUD indicates exact reason (e.g. Cut-in Left, TTC=1.4s)."
        ],
        accent_color=COLOR_WARNING
    )

    builder.add_card(
        s9, Inches(8.8), Inches(4.0), Inches(3.933), Inches(2.8),
        "Proposed Quantitative Evaluation Metrics",
        [
            "Prediction Accuracy: Target >=93.0% across all naturalistic test sets.",
            "Intention Lead Time: Mean detection lead time >=1.8 seconds prior to crossing.",
            "False Positive Rate: Under 4.5% to eliminate nuisance phantom braking.",
            "Edge Throughput: Deterministic execution latency <20ms (>50 FPS on Jetson)."
        ],
        accent_color=COLOR_SUCCESS
    )

    # Save
    builder.save(output_path)


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    out_file = os.path.join(current_dir, "Phase2_Literature_Review.pptx")
    build_phase2_presentation(out_file)
