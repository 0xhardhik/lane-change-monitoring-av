"""
generate_phase1.py
Generates Phase 1: Project Proposal (Milestone 1, 7 slides)
Course: 24CSE473 - Neural Networks and Deep Learning
Student: Hardhik A | CH.SC.U4CSE23114
Topic: Monitoring Lane Changes in Autonomous Vehicles
"""

import os
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from presentation_builder import PresentationBuilder, COLOR_ACCENT_BLUE, COLOR_NAVY_DARK, COLOR_SUCCESS, COLOR_WARNING

def build_phase1_presentation(output_path):
    builder = PresentationBuilder(title_prefix="Phase 1 Proposal")
    total_slides = 7
    milestone_label = "Milestone 1: Project Proposal"

    # =========================================================================
    # SLIDE 1: Title Slide
    # =========================================================================
    builder.add_title_slide(
        title="Monitoring Lane Changes in Autonomous Vehicles",
        subtitle="Predictive Intention Classification & Trajectory Safety Validation via Vision Pilot Deep Neural Networks",
        milestone_badge="Milestone 1: Project Proposal & Feasibility",
        student_name="Hardhik A",
        roll_no="CH.SC.U4CSE23114",
        course_code="24CSE473",
        course_name="Neural Networks and Deep Learning",
        dept_name="Department of Computer Science & Engineering, Amrita Vishwa Vidyapeetham"
    )

    # =========================================================================
    # SLIDE 2: Problem Formulation & Motivation
    # =========================================================================
    s2 = builder.create_slide()
    builder.add_header(s2, "Problem Formulation & Urban Highway Motivation", "Context & Urgency", milestone_label)
    builder.add_footer(s2, 2, total_slides, milestone_label)

    # 3 Cards layout
    builder.add_card(
        s2, Inches(0.8), Inches(1.3), Inches(3.7), Inches(5.5),
        "The Urbanization & Highway Challenge",
        [
            "High-Speed Highway Vulnerability: Modern multi-lane highways experience severe bottleneck congestion and frequent erratic cut-in maneuvers.",
            "Accident Severity: Over 45% of highway collisions and 70%+ of autonomous vehicle safety disengagements occur during unexpected lane transitions.",
            "Reaction Time Deficit: Human drivers take 1.2 to 1.5 seconds to react to an aggressive cut-in, which is fatal at highway velocities exceeding 100 km/h.",
            "Complex Indian Road Scenarios: Heterogeneous traffic, unstructured lane discipline, non-standardized vehicle sizes, and frequent un-signaled lane weaving."
        ],
        accent_color=COLOR_ACCENT_BLUE
    )

    builder.add_card(
        s2, Inches(4.8), Inches(1.3), Inches(3.7), Inches(5.5),
        "The Flaw of Reactive ADAS",
        [
            "Reactive Distance Keeping: Conventional radar-based ACC (Adaptive Cruise Control) only modulates velocity after a target vehicle has fully occupied the ego-lane.",
            "Late Braking Jerks: Belated reaction causes abrupt deceleration, passenger discomfort, and severe rear-end collision risks from following traffic.",
            "Lack of Intent Awareness: Existing commercial systems lack temporal memory—they perceive vehicle position but fail to predict behavioral intent.",
            "False Positive Fatigue: Overly conservative braking triggers unnecessary phantom stops, causing drivers to deactivate ADAS functions entirely."
        ],
        accent_color=RGBColor(217, 119, 6)
    )

    builder.add_card(
        s2, Inches(8.8), Inches(1.3), Inches(3.7), Inches(5.5),
        "The Deep Learning Opportunity",
        [
            "Proactive Intent Forecasting: Deep spatio-temporal neural networks can recognize subtle pre-maneuver cues 1.8+ seconds before lane line crossing.",
            "Micro-Motion Signatures: Detecting lateral drift velocity, subtle yaw-angle variation, steering wheel orientation, and front-wheel turn angles.",
            "Surrounding Spatial Context: Neural attention mechanisms model multi-vehicle interactions and gap-acceptance dynamics across adjacent lanes.",
            "Vision Pilot Integration: Camera-first, mapless perception provides a cost-effective, scalable foundation without reliance on million-dollar LiDAR setups."
        ],
        accent_color=COLOR_SUCCESS
    )

    # =========================================================================
    # SLIDE 3: Problem Statement & System Scope
    # =========================================================================
    s3 = builder.create_slide()
    builder.add_header(s3, "Formal Problem Statement & Architectural Scope", "Boundary Specification", milestone_label)
    builder.add_footer(s3, 3, total_slides, milestone_label)

    builder.add_card(
        s3, Inches(0.8), Inches(1.3), Inches(11.733), Inches(1.9),
        "Formal Problem Statement",
        [
            "Core Objective: Formulate, train, and validate a real-time, vision-first deep neural network monitoring framework capable of detecting surrounding vehicle lane-change intentions at least 1.8 seconds prior to lane boundary crossing.",
            "Safety Envelope Constraint: Dynamically arbitrate between Lane Keeping Assist (LKAS), Adaptive Cruise Control (ACC), and Emergency Collision Abort (AEB) by computing real-time Time-to-Collision (TTC) and Time-to-Lane-Crossing (TLC).",
            "Latency Mandate: Guarantee deterministic sub-25ms inference latency (>40 FPS) on embedded edge compute (NVIDIA Jetson / Automotive SoC) under mapless operating constraints."
        ],
        accent_color=COLOR_ACCENT_BLUE
    )

    # Scope Split: In-Scope vs Out-of-Scope
    builder.add_card(
        s3, Inches(0.8), Inches(3.45), Inches(5.7), Inches(3.35),
        "System In-Scope Deliverables",
        [
            "Monocular & Stereo Vision Ingestion: 1080p forward dashcam/windshield video streams @ 30-60 FPS.",
            "Spatio-Temporal Deep Learning: Spatial CNN feature extractor coupled to Bidirectional LSTM sequence modeling.",
            "Intent Tri-State Classification: Continuous probability distribution: P(Keep Lane), P(Cut-in Left), P(Cut-in Right).",
            "Kinematic Trajectory Validation: Enforcing physical safety barriers via dynamic Time-to-Collision (TTC) bounds.",
            "Multi-Tier ADAS Escalation: Three-tier alerting (Advisory Info -> Active Caution -> Emergency Abort Braking).",
            "Simulation & Edge Deployment: Benchmarked on highD highway dataset and synthetic CARLA / SODA environments."
        ],
        accent_color=COLOR_SUCCESS
    )

    builder.add_card(
        s3, Inches(6.833), Inches(3.45), Inches(5.7), Inches(3.35),
        "Out-of-Scope & Future Extensions",
        [
            "Off-Road Navigation: Not designed for dirt tracks, construction zones, or unpaved rural pathways lacking drivable surfaces.",
            "Mechanical Actuator Fabrication: Software-level decision generation; excludes physical brake/steering actuator hardware machining.",
            "Full 360° LiDAR Point Cloud Fusion: Pure camera-first vision architecture to ensure consumer vehicle commercial viability.",
            "Cloud-Dependent HD Mapping: System operates strictly mapless using real-time sensory perception without live cloud telemetry.",
            "Adverse Sensor Destruction: Physical lens mud splatters or complete hardware sensor failures are handled via fail-safe handoff."
        ],
        accent_color=RGBColor(220, 38, 38)
    )

    # =========================================================================
    # SLIDE 4: Core Objectives & Targeted ADAS Features
    # =========================================================================
    s4 = builder.create_slide()
    builder.add_header(s4, "Project Objectives & Targeted ADAS Feature Integration", "System Goals", milestone_label)
    builder.add_footer(s4, 4, total_slides, milestone_label)

    # 4 Pillar Cards in a 2x2 grid
    builder.add_card(
        s4, Inches(0.8), Inches(1.3), Inches(5.7), Inches(2.6),
        "1. Proactive Intention Classification",
        [
            "Lead Time Horizon: Detect intended lane change >= 1.8 seconds before the vehicle touches the lane delimiter marking.",
            "Multi-Class Softmax Output: Real-time inference outputting P(Keep), P(Cut-in Left), and P(Cut-in Right).",
            "Micro-Kinematic Sensitivity: Capture subtle yaw shifts and lateral acceleration (>0.18 m/s²) before macro displacement occurs."
        ],
        accent_color=COLOR_ACCENT_BLUE
    )

    builder.add_card(
        s4, Inches(6.833), Inches(1.3), Inches(5.7), Inches(2.6),
        "2. Spatio-Temporal Hybrid Modeling",
        [
            "Spatial Feature Representation: Extract high-dimensional spatial embeddings of surrounding vehicles using deep CNN backbones.",
            "Temporal Recurrent Sequence Reasoning: Employ Bidirectional LSTM / GRU cells over rolling 30-frame temporal buffers (1.0 - 2.0s).",
            "Attention Pooling: Dynamically weight critical transition frames over static cruising frames to reduce false alarms."
        ],
        accent_color=RGBColor(99, 102, 241)
    )

    builder.add_card(
        s4, Inches(0.8), Inches(4.15), Inches(5.7), Inches(2.65),
        "3. Physics-Informed Safety Layer",
        [
            "Deterministic Safety Bounds: Guard against black-box neural hallucination by verifying trajectories against physics equations.",
            "Dynamic Time-to-Collision (TTC): Continuous calculation of TTC = Δx / Δv to detect imminent deceleration threats.",
            "Lateral Trajectory Envelope: Model Time-to-Lane-Crossing (TLC) to distinguish intentional cut-ins from harmless vehicle drift."
        ],
        accent_color=COLOR_SUCCESS
    )

    builder.add_card(
        s4, Inches(6.833), Inches(4.15), Inches(5.7), Inches(2.65),
        "4. Targeted ADAS Ecosystem Integration",
        [
            "LKAS (Lane Keeping Assist): Suppress false lane departures when ego vehicle yields slightly to an aggressive cut-in.",
            "ACC (Adaptive Cruise Control): Early smooth regenerative braking 1.5s prior to cut-in completion, avoiding emergency lockups.",
            "AEB (Automatic Emergency Braking): Deterministic override triggering emergency deceleration if cut-in TTC collapses below 1.2s."
        ],
        accent_color=RGBColor(217, 119, 6)
    )

    # =========================================================================
    # SLIDE 5: High-Level System Workflow
    # =========================================================================
    s5 = builder.create_slide()
    builder.add_header(s5, "High-Level End-to-End System Workflow (6-Step Pipeline)", "Methodology Overview", milestone_label)
    builder.add_footer(s5, 5, total_slides, milestone_label)

    steps = [
        {"title": "1. Vision Ingest", "desc": "1080p RGB dashcam frame acquisition at 30-60 FPS."},
        {"title": "2. Spatial Detect", "desc": "YOLOv8 vehicle bounding box + DeepSORT tracking & lane segmentation."},
        {"title": "3. Sequence Buffer", "desc": "Rolling FIFO tensor of kinematic states & spatial tokens over 30 frames."},
        {"title": "4. Intent Classifier", "desc": "CNN-LSTM inference generates intention probabilities P(Keep, Left, Right)."},
        {"title": "5. Safety Envelope", "desc": "Kinematic verification calculating TTC = Δx/Δv and lateral velocity vy."},
        {"title": "6. ADAS Arbitration", "desc": "Tiered CAN-bus actuation: Advisory Info, Smooth ACC, or Active Emergency Brake."}
    ]
    builder.add_process_steps(s5, Inches(0.8), Inches(1.3), Inches(11.733), Inches(2.4), steps)

    # Detail Cards Below
    builder.add_card(
        s5, Inches(0.8), Inches(4.0), Inches(5.7), Inches(2.8),
        "Perception & Sequence Pipeline",
        [
            "High-Throughput Vision Acquisition: Standard monocular dashcam stream processed via OpenCV / V4L2 pipeline.",
            "Spatial Coordinate Normalization: Bounding box coordinates normalized to vehicle ground plane perspective.",
            "Multi-Object Tracking: DeepSORT maintains stable track IDs across occlusions, preventing tracklet fragmentation.",
            "Sliding-Window Feature Vector: Tracks relative distance (Δx), lateral offset (Δy), and optical flow motion vectors."
        ],
        accent_color=COLOR_ACCENT_BLUE
    )

    builder.add_card(
        s5, Inches(6.833), Inches(4.0), Inches(5.7), Inches(2.8),
        "Inference & Control Arbitration Pipeline",
        [
            "Recurrent Sequence Classification: Bidirectional LSTM processes temporal history to detect intention transitions.",
            "Dual-Threshold Safety Gate: Intention probability (>0.75) must coincide with critical kinematic safety violation.",
            "Deterministic Fail-Safe Fallback: If neural confidence drops (<0.50), system defaults to conservative distance ACC.",
            "Sub-Millisecond CAN Dispatch: Alert signals packaged into standardized ROS 2 / CAN-bus messages for instant actuation."
        ],
        accent_color=COLOR_SUCCESS
    )

    # =========================================================================
    # SLIDE 6: Sensor & Middleware Architecture
    # =========================================================================
    s6 = builder.create_slide()
    builder.add_header(s6, "Sensor Baseline, Edge Middleware & Mapless Operation", "Technical Infrastructure", milestone_label)
    builder.add_footer(s6, 6, total_slides, milestone_label)

    # 3 Column Cards
    builder.add_card(
        s6, Inches(0.8), Inches(1.3), Inches(3.7), Inches(5.5),
        "Sensory Ingestion Tier",
        [
            "Camera Configuration: Monocular high-dynamic-range (HDR) automotive-grade CMOS camera mounted behind windshield.",
            "Optical Specifications: 1920x1080 resolution, 60 FPS, 90° horizontal field-of-view (FOV) covering 3 highway lanes.",
            "Exposure Robustness: Hardware auto-exposure and tone mapping mitigating direct sunrise/sunset glare and tunnel transitions.",
            "Low-Cost Advantage: Costs under $150 compared to multi-beam LiDAR arrays costing upwards of $10,000, ensuring commercial viability."
        ],
        accent_color=COLOR_ACCENT_BLUE
    )

    builder.add_card(
        s6, Inches(4.8), Inches(1.3), Inches(3.7), Inches(5.5),
        "Edge Compute & Middleware",
        [
            "Hardware Target: NVIDIA Jetson Orin Nano / Xavier NX / Automotive Grade SoC (Snapdragon Ride / Mobileye EyeQ).",
            "Inference Engine: ONNX Runtime / TensorRT FP16 quantization delivering sub-20ms latency and 50+ FPS execution.",
            "Middleware Bus: ROS 2 Humble (Robot Operating System) with CycloneDDS for deterministic zero-copy intra-process transfer.",
            "Thermal & Power Budget: Designed to operate strictly within a 15W - 25W power envelope, preserving EV driving range."
        ],
        accent_color=RGBColor(99, 102, 241)
    )

    builder.add_card(
        s6, Inches(8.8), Inches(1.3), Inches(3.7), Inches(5.5),
        "Mapless Operational Paradigm",
        [
            "Zero Cloud Dependency: Operates completely offline without requiring cellular 5G coverage or live HD map downloads.",
            "Resilient Road Parsing: Dynamically infers lane boundaries, virtual lane centers, and curb delimiters purely from optical features.",
            "Unstructured Road Handling: Adapts seamlessly to faded lane markings, temporary construction zones, and rain-slicked asphalt.",
            "Privacy Preserving: Processes video strictly on edge RAM without streaming footage to external third-party cloud servers."
        ],
        accent_color=COLOR_SUCCESS
    )

    # =========================================================================
    # SLIDE 7: Feasibility, Challenges & Expected Deliverables
    # =========================================================================
    s7 = builder.create_slide()
    builder.add_header(s7, "Preliminary Feasibility, Challenges & Deliverables", "Execution Roadmap", milestone_label)
    builder.add_footer(s7, 7, total_slides, milestone_label)

    builder.add_card(
        s7, Inches(0.8), Inches(1.3), Inches(5.7), Inches(2.7),
        "Technical Feasibility & Dataset Grounding",
        [
            "highD Benchmark Dataset: Over 110,500 naturalistic German highway vehicles across 447,000 km, capturing 12,000+ lane change events.",
            "CARLA Autonomous Simulator: Synthetic closed-loop highway simulator for stress-testing aggressive cut-ins and emergency evasions.",
            "Empirical Precedents: Academic literature validates that CNN-LSTM models achieve >92% accuracy on highway cut-in datasets.",
            "GPU Compute Availability: PyTorch 2.x acceleration with CUDA 12 enables rapid prototype training and seamless ONNX export."
        ],
        accent_color=COLOR_SUCCESS
    )

    builder.add_card(
        s7, Inches(6.833), Inches(1.3), Inches(5.7), Inches(2.7),
        "Identified Technical Challenges & Mitigations",
        [
            "Adverse Weather / Rain Glare: Addressed via HSV color normalization, spatial attention, and synthetic noise data augmentation.",
            "Severe Vehicle Occlusion: Mitigated through Kalman-assisted DeepSORT tracking preserving bounding box priors across brief occlusions.",
            "Erratic False Swerves: Trajectory validation layer validates lateral velocity before triggering emergency brakes, clearing transient false alarms.",
            "Edge Compute Bottlenecks: Solved via FP16 TensorRT model quantization and pruned MobileNet/ResNet feature backbones."
        ],
        accent_color=RGBColor(220, 38, 38)
    )

    builder.add_card(
        s7, Inches(0.8), Inches(4.2), Inches(11.733), Inches(2.6),
        "Structured 3-Phase Milestone Roadmap & Deliverables",
        [
            "Milestone 1 (Current): Project Proposal & Feasibility Formulation — Scope definition, sensor baseline, and mathematical objective.",
            "Milestone 2 (Literature Review & Architecture): 4 comprehensive tabular literature survey slides (16+ benchmark papers), research gap synthesis, and multi-tier neural network architecture.",
            "Milestone 3 (Final Defense & Implementation): 21-slide definitive academic defense with tabular survey, confusion matrix evaluation, comparative benchmarks, and ISO 26262 compliance analysis.",
            "Live Interactive Demonstration: Runnable Python OpenCV HUD system showcasing real-time multi-lane traffic, cut-in scenarios, probability meters, and ADAS brake interventions."
        ],
        accent_color=COLOR_ACCENT_BLUE
    )

    # Save
    builder.save(output_path)


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    out_file = os.path.join(current_dir, "Phase1_Project_Proposal.pptx")
    build_phase1_presentation(out_file)
