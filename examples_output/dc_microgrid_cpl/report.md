# IMS Analysis Report — DC Microgrid with Constant-Power Load — Bistable Recoverability under MRC
*Generated 2026-07-19 15:30 by IMS Platform (core engine)*

## System Model
- Model: `DCMicrogridCPL` ("dc_microgrid_cpl")
- States: i, v
- Inputs: P_load
- Parameters: `{'L': 0.005, 'C': 0.05, 'r': 0.15, 'Vin': 1.2, 'v_floor': 0.05}`

## Intrinsic Manifold
- Sweep parameter: `P_load`
- Manifold samples: 60 (60 stable / 0 unstable)

## Recoverability Assessment
- Nominal state: `[0.44093582 1.13385963]`
- Scenarios analysed: 150
- Recoverable scenarios: 148 (98.7%)
- **Recoverability Index: 0.99**
- Margin to critical boundary: 0.8743
- **Risk level: LOW**

## Control Strategy
- Controller: Manifold-Reshaping Control (local LQR toward nearest manifold point)
- Design objective: Manifold-Reshaping Control (MRC), driving trajectories back onto the intrinsic manifold following large disturbances.

## Engineering Interpretation
The system exhibits a large recoverability region relative to the sampled disturbance envelope; nominal operation is well clear of the critical boundary.

## Notes
Open-loop Recoverability Index at radius=0.9: 0.96 vs. MRC closed-loop: 0.99 (2.7 pp improvement). This system has a genuine saddle-type unstable equilibrium (the classical CPL large-signal instability); it is the intrinsic-manifold-adjacent critical boundary separating recoverable from non-recoverable disturbances in open loop.

---
*This report was generated automatically by the IMS Platform core engine. IMS complements, and does not replace, established equilibrium-based stability analysis (small-signal, transient stability, eigenvalue/Lyapunov methods).*