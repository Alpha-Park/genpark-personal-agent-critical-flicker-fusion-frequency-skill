"""
Example usage for Critical Flicker Fusion Frequency (CFFF) Skill.
Demonstrates analyzing visual psychophysics ascending/descending trials.
"""

from client import CriticalFlickerFusionClient


def main():
    client = CriticalFlickerFusionClient()

    print("=== 1. Evaluating CFFF Psychophysical Thresholds (Rested Morning State) ===")
    asc_trials = [38.2, 38.6, 38.4, 38.8]
    desc_trials = [39.4, 39.0, 39.2, 39.6]

    res_morning = client.evaluate_cfff_thresholds(
        ascending_trials_hz=asc_trials,
        descending_trials_hz=desc_trials,
        baseline_cfff_hz=38.5
    )
    print(f"Mean Ascending: {res_morning['mean_ascending_threshold_hz']} Hz | Mean Descending: {res_morning['mean_descending_threshold_hz']} Hz")
    print(f"Composite CFFF: {res_morning['composite_cfff_hz']} Hz (Delta: {res_morning['delta_from_baseline_hz']} Hz)")
    print(f"Hysteresis: {res_morning['threshold_hysteresis_hz']} Hz")
    print(f"Cortical Arousal Index: {res_morning['cortical_arousal_index']} / 100")
    print(f"Status: {res_morning['status']}")
    print(f"Guidance: {res_morning['actionable_guidance']}")

    print("\n=== 2. Evaluating CFFF After 6 Hours of Continuous Screen Work ===")
    asc_fatigued = [35.1, 35.5, 34.8, 35.2]
    desc_fatigued = [36.2, 35.8, 36.0, 35.9]

    res_fatigued = client.evaluate_cfff_thresholds(
        ascending_trials_hz=asc_fatigued,
        descending_trials_hz=desc_fatigued,
        baseline_cfff_hz=38.5
    )
    print(f"Composite CFFF: {res_fatigued['composite_cfff_hz']} Hz (Delta: {res_fatigued['delta_from_baseline_hz']} Hz)")
    print(f"Cortical Arousal Index: {res_fatigued['cortical_arousal_index']} / 100")
    print(f"Status: {res_fatigued['status']}")
    print(f"Guidance: {res_fatigued['actionable_guidance']}")


if __name__ == "__main__":
    main()
