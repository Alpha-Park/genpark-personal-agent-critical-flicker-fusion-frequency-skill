---
name: genpark-personal-agent-critical-flicker-fusion-frequency-skill
description: Deterministic evaluation of Critical Flicker Fusion Frequency (CFFF), cortical arousal, visual temporal resolution, and CNS neurotransmitter exhaustion.
version: 1.0.0
author: GenPark Autonomous Agents Ecosystem
license: MIT
tags:
  - personal-agent
  - ai-agent
  - openclaw
  - genpark
  - mcp
  - mcp-server
  - model-context-protocol
  - python
  - zero-dependency
  - wellness
  - productivity
  - production-ready
---

# Critical Flicker Fusion Frequency (CFFF) Skill

## Overview
The `genpark-personal-agent-critical-flicker-fusion-frequency-skill` empowers personal sovereign agents with psychophysiological monitoring of central nervous system (CNS) arousal. Critical Flicker Fusion Frequency (CFFF) represents the threshold rate (in Hertz) at which intermittent light pulses fuse into a continuous, steady visual perception. Because retinal photoreceptors and the visual cortex (V1) depend directly on cholinergic and dopaminergic tone, CFFF serves as an index of central alertness. Drops of $\ge 2.0\text{ Hz}$ below baseline detect mental exhaustion before behavioral performance fails.

## Physiological Model & Mathematics
1. **Ascending and Descending Thresholds**:
   $$\text{CFFF} = \frac{\overline{\text{CFFF}}_{\text{ascending}} + \overline{\text{CFFF}}_{\text{descending}}}{2}$$
2. **Threshold Hysteresis**:
   $$\text{Hysteresis} = |\overline{\text{CFFF}}_{\text{descending}} - \overline{\text{CFFF}}_{\text{ascending}}|$$
3. **Delta from Rested Baseline**:
   $$\Delta \text{CFFF} = \text{CFFF} - \text{CFFF}_{\text{baseline}}$$
   - $\Delta \text{CFFF} \ge +2.0\text{ Hz}$: High alertness and cortical arousal.
   - $\Delta \text{CFFF} \in [-1.0, +1.0]\text{ Hz}$: Steady, rested baseline.
   - $\Delta \text{CFFF} \le -2.0\text{ Hz}$: Central nervous system fatigue.
4. **Cortical Arousal & Cognitive Fatigue Index ($CACFI$)**:
   Maps frequency deviations and psychophysical hysteresis into a standardized 0 to 100 rating.

## Tools & Endpoints
- `evaluate_cfff_thresholds`: Calculates composite CFFF, hysteresis, baseline delta, and CNS fatigue score.
