# IMS Analysis Report — My DC microgrid bus feeding a constant-power load Study
*Generated 2026-07-19 15:52 by IMS Platform (core engine)*

## System Model
- Model: `DCMicrogridCPL` ("My DC microgrid bus feeding a constant-power load Study")
- States: i, v
- Inputs: P_load
- Parameters: `{'L': 0.005, 'C': 0.05, 'r': 0.15, 'Vin': 1.2, 'v_floor': 0.05}`

## Intrinsic Manifold
- Sweep parameter: `dc_microgrid_cpl_operating_param`
- Manifold samples: 60 (60 stable / 0 unstable)

## Recoverability Assessment
- Nominal state: `[0.44093582 1.13385963]`
- Scenarios analysed: 60
- Recoverable scenarios: 58 (96.7%)
- **Recoverability Index: 0.97**
- Margin to critical boundary: 0.8743
- **Risk level: LOW**

## Control Strategy
- Controller: Manifold-Reshaping Control (local LQR gain schedule over the intrinsic manifold)
- Design objective: Manifold-Reshaping Control (MRC), driving trajectories back onto the intrinsic manifold following large disturbances.

## Engineering Interpretation
The system exhibits a large recoverability region relative to the sampled disturbance envelope; nominal operation is well clear of the critical boundary.

## Notes
Open-loop Recoverability Index: 0.93 vs. MRC closed-loop: 0.97 (+3.3 percentage points).

---
*This report was generated automatically by the IMS Platform core engine. IMS complements, and does not replace, established equilibrium-based stability analysis (small-signal, transient stability, eigenvalue/Lyapunov methods).*