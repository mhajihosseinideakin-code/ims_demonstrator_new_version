# IMS Analysis Report — My Droop-controlled grid-forming inverter Study
*Generated 2026-07-19 15:54 by IMS Platform (core engine)*

## System Model
- Model: `GridFormingInverter` ("My Droop-controlled grid-forming inverter Study")
- States: delta, omega
- Inputs: P_set
- Parameters: `{'E': 1.0, 'V': 1.0, 'X': 0.3, 'tau_p': 0.05, 'm_p': 1.0}`

## Intrinsic Manifold
- Sweep parameter: `grid_forming_inverter_operating_param`
- Manifold samples: 60 (60 stable / 0 unstable)

## Recoverability Assessment
- Nominal state: `[0.15056827 0.        ]`
- Scenarios analysed: 60
- Recoverable scenarios: 60 (100.0%)
- **Recoverability Index: 1.00**
- Margin to critical boundary: 2.0000
- **Risk level: LOW**

## Control Strategy
- Controller: Manifold-Reshaping Control (local LQR gain schedule over the intrinsic manifold)
- Design objective: Manifold-Reshaping Control (MRC), driving trajectories back onto the intrinsic manifold following large disturbances.

## Engineering Interpretation
The system exhibits a large recoverability region relative to the sampled disturbance envelope; nominal operation is well clear of the critical boundary.

## Notes
Open-loop Recoverability Index: 1.00 vs. MRC closed-loop: 1.00 (+0.0 percentage points).

---
*This report was generated automatically by the IMS Platform core engine. IMS complements, and does not replace, established equilibrium-based stability analysis (small-signal, transient stability, eigenvalue/Lyapunov methods).*