"""
case.registry
--------------

Registry of system models the case-based interface can build. This is the
single place a new model needs to be listed to become available through
the YAML/JSON case files, the interactive wizard, and the CLI -- everything
else in `case/` works generically against `DynamicalSystem`.
"""

from __future__ import annotations

from typing import Dict, Type

from ..core.system import DynamicalSystem
from ..models import GridFormingInverter, DCMicrogridCPL


MODEL_REGISTRY: Dict[str, Type[DynamicalSystem]] = {
    "grid_forming_inverter": GridFormingInverter,
    "dc_microgrid_cpl": DCMicrogridCPL,
}

#: Human-facing metadata used by the wizard and by validation error messages.
#: `param_help` documents every entry accepted in a case file's `params:` block.
MODEL_METADATA: Dict[str, dict] = {
    "grid_forming_inverter": {
        "label": "Droop-controlled grid-forming inverter (single converter, swing-type dynamics)",
        "states": ["delta (power angle, rad)", "omega (frequency deviation, rad/s)"],
        "inputs": ["P_set (active-power setpoint, p.u.)"],
        "param_help": {
            "E": "Inverter internal EMF magnitude (p.u.). Typical: 0.9-1.1",
            "V": "Grid bus voltage magnitude (p.u.). Typical: 0.9-1.1",
            "X": "Line reactance between inverter and grid (p.u.). Typical: 0.1-0.5",
            "tau_p": "Active-power droop filter time constant (s). Typical: 0.01-0.2",
            "m_p": "Droop gain (p.u. power / p.u. frequency error). Typical: 0.5-5",
        },
        "default_operating_input": [0.5],
        "default_state_guess": [0.3, 0.0],
        "default_manifold_range": [0.0, 0.95],
    },
    "dc_microgrid_cpl": {
        "label": "DC microgrid bus feeding a constant-power load (bistable large-signal case)",
        "states": ["i (inductor/line current, p.u.)", "v (DC bus voltage, p.u.)"],
        "inputs": ["P_load (constant-power load demand, p.u.)"],
        "param_help": {
            "L": "Line/converter inductance (H, normalised). Typical: 0.001-0.02",
            "C": "DC bus capacitance (F, normalised). Typical: 0.01-0.1",
            "r": "Line resistance / damping (p.u.). Must be large enough relative to "
                 "P/(C v^2) at operating power for a stable high-voltage equilibrium "
                 "to exist (Middlebrook criterion). Typical: 0.05-0.3",
            "Vin": "Source-side regulated voltage (p.u.). Typical: 1.0-1.3",
            "v_floor": "Numerical smoothing floor for the CPL's 1/v term (p.u.). Leave at default unless "
                       "you understand the smooth-clamp implementation.",
        },
        "default_operating_input": [0.5],
        "default_state_guess": [0.44, 1.13],
        "default_manifold_range": [0.05, 1.2],
    },
}


def list_models() -> str:
    """Return a human-readable listing of available models (used by CLI --list-models and error messages)."""
    lines = ["Available system models:"]
    for key, meta in MODEL_METADATA.items():
        lines.append(f"\n  {key}\n    {meta['label']}")
        lines.append(f"    states: {', '.join(meta['states'])}")
        lines.append(f"    inputs: {', '.join(meta['inputs'])}")
        lines.append("    params:")
        for pname, help_text in meta["param_help"].items():
            lines.append(f"      - {pname}: {help_text}")
    return "\n".join(lines)
