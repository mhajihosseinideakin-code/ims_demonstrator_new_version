# IMS Analysis Report — Grid-Forming Inverter — Large-Signal Recoverability under MRC
*Generated 2026-07-19 15:37 by IMS Platform (core engine)*

## System Model
- Model: `GridFormingInverter` ("grid_forming_inverter")
- States: delta, omega
- Inputs: P_set
- Parameters: `{'E': 1.0, 'V': 1.0, 'X': 0.3, 'tau_p': 0.05, 'm_p': 1.0}`

## Intrinsic Manifold
- Sweep parameter: `P_set`
- Manifold samples: 80 (80 stable / 0 unstable)

## Recoverability Assessment
- Nominal state: `[0.15056827 0.        ]`
- Scenarios analysed: 100
- Recoverable scenarios: 100 (100.0%)
- **Recoverability Index: 1.00**
- Margin to critical boundary: 3.0000
- **Risk level: LOW**

## Control Strategy
- Controller: Manifold-Reshaping Control (local LQR toward nearest manifold point)
- Design objective: Manifold-Reshaping Control (MRC), driving trajectories back onto the intrinsic manifold following large disturbances.

## Engineering Interpretation
The system exhibits a large recoverability region relative to the sampled disturbance envelope; nominal operation is well clear of the critical boundary.

## Notes
Open-loop Recoverability Index at radius=3.0: 1.00 vs. MRC closed-loop: 1.00 (0.0 pp improvement).

---
*This report was generated automatically by the IMS Platform core engine. IMS complements, and does not replace, established equilibrium-based stability analysis (small-signal, transient stability, eigenvalue/Lyapunov methods).*