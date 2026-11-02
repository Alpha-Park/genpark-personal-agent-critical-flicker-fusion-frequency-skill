"""
Critical Flicker Fusion Frequency (CFFF) & Cortical Arousal Engine.
Provides deterministic, zero-dependency psychophysiological modeling of visual cortex temporal resolution,
ascending/descending flicker-fusion thresholds, and central nervous system (CNS) fatigue.
"""

from typing import Dict, Any, List, Optional


class CriticalFlickerFusionClient:
    """
    Deterministic client for calculating Critical Flicker Fusion Frequency (CFFF) in Hertz (Hz).
    Pure Python standard library implementation based on neuroergonomic visual psychophysics.
    """

    def __init__(self):
        pass

    def evaluate_cfff_thresholds(
        self,
        ascending_trials_hz: List[float],
        descending_trials_hz: List[float],
        baseline_cfff_hz: float = 38.0
    ) -> Dict[str, Any]:
        """
        Evaluates CFFF psychophysical test series:
        - ascending_trials_hz: frequencies where subject first perceived fusion (steady light).
        - descending_trials_hz: frequencies where subject first perceived flicker.
        - baseline_cfff_hz: user's rested baseline threshold (standard adult normative: 35 - 42 Hz).
        """
        if not ascending_trials_hz or not descending_trials_hz:
            return {"error": "Both ascending and descending trial arrays must be non-empty"}

        mean_asc = sum(ascending_trials_hz) / len(ascending_trials_hz)
        mean_desc = sum(descending_trials_hz) / len(descending_trials_hz)

        # Composite CFFF threshold
        cfff_threshold = round((mean_asc + mean_desc) / 2.0, 2)
        hysteresis = round(abs(mean_desc - mean_asc), 2)

        # Delta relative to personal rested baseline
        delta_hz = round(cfff_threshold - baseline_cfff_hz, 2)

        # Cortical Arousal & Cognitive Fatigue Index (CACFI, 0 - 100):
        # Baseline = 70. Delta >= +2.0 -> 90+ (High Alertness). Delta <= -2.5 -> < 40 (CNS Fatigue).
        cns_score = 70.0 + (delta_hz * 12.0) - (hysteresis * 3.0)
        cacfi_score = round(min(100.0, max(5.0, cns_score)), 1)

        is_cns_exhausted = delta_hz <= -2.0
        is_hyper_alert = delta_hz >= 2.5

        if cacfi_score >= 80.0:
            status = "HIGH_CORTICAL_AROUSAL"
            interpretation = "Visual cortex temporal processing speed is elevated; high central alertness and synaptic transmission speed."
            guidance = "Optimal cognitive state for complex analytical reasoning, coding, and precision decision-making."
        elif cacfi_score >= 60.0:
            status = "NORMAL_RESTED_COGNITIVE_STATE"
            interpretation = "CFFF thresholds aligned with normative resting baseline; steady cortical activation."
            guidance = "Standard sustained cognitive capacity. Maintain balanced 50/10 focus-to-rest work cadence."
        elif is_cns_exhausted:
            status = "CENTRAL_NERVOUS_SYSTEM_FATIGUE"
            interpretation = f"Marked reduction in CFFF threshold ({delta_hz} Hz below baseline); indicates cortical exhaustion and reduced neurotransmitter turnover."
            guidance = "Decline in visual processing speed detected. Take a 20-minute sensory rest pause and eliminate high-stakes choices."
        else:
            status = "MILD_COGNITIVE_DECLINE"
            interpretation = "Slight downward drift in flicker-fusion frequency; beginning of attention fatigue accumulation."
            guidance = "Step away from visual display terminals for 5 minutes, hydrate, and practice distant gaze accommodation."

        return {
            "mean_ascending_threshold_hz": round(mean_asc, 2),
            "mean_descending_threshold_hz": round(mean_desc, 2),
            "composite_cfff_hz": cfff_threshold,
            "threshold_hysteresis_hz": hysteresis,
            "baseline_cfff_hz": baseline_cfff_hz,
            "delta_from_baseline_hz": delta_hz,
            "cortical_arousal_index": cacfi_score,
            "status": status,
            "physiological_interpretation": interpretation,
            "actionable_guidance": guidance
        }
