"""
integrators.py  --  Euler vs solve_ivp, and why solve_ivp is the engine.

Run `python integrators.py` to see:
  (1) On the linear three-compartment model, a small-step Euler loop and
      solve_ivp agree closely -- but Euler needs a SMALL step, while solve_ivp
      controls its own error automatically.
  (2) The SAME derivative-function style extends, with no change of method, to
      a NONLINEAR (Michaelis-Menten) elimination term. That is exactly why we
      use solve_ivp as the engine: it handles linear and nonlinear models the
      same way.

Euler stays in the course as the most transparent way to UNDERSTAND stepping;
solve_ivp is the working engine.
"""

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

V1 = 0.228 * 70
k10, k12, k13, k21, k31 = 0.119, 0.112, 0.0419, 0.055, 0.0033
DOSE, T_END = 100.0, 60.0


def deriv_linear(t, y):
    A1, A2, A3 = y
    dA1 = -(k10 + k12 + k13) * A1 + k21 * A2 + k31 * A3
    dA2 = k12 * A1 - k21 * A2
    dA3 = k13 * A1 - k31 * A3
    return [dA1, dA2, dA3]


def euler(dt):
    y = np.array([DOSE, 0.0, 0.0])
    t, T, CP = 0.0, [0.0], [y[0] / V1]
    while t < T_END:
        dy = np.array(deriv_linear(t, y))      # the same equations as solve_ivp uses
        y = y + dy * dt                         # the Euler update
        t += dt
        T.append(t); CP.append(y[0] / V1)
    return np.array(T), np.array(CP)


# Nonlinear (saturable) elimination -- still just a derivative function
VMAX, KM = 30.0, 5.0     # mg/min, mg/L  (illustrative Michaelis-Menten)

def deriv_nonlinear(t, y):
    A1, A2, A3 = y
    Cp = A1 / V1
    elim = VMAX * Cp / (KM + Cp)               # depends on concentration -> nonlinear
    dA1 = -elim - (k12 + k13) * A1 + k21 * A2 + k31 * A3
    dA2 = k12 * A1 - k21 * A2
    dA3 = k13 * A1 - k31 * A3
    return [dA1, dA2, dA3]


if __name__ == "__main__":
    t_eval = np.linspace(0, T_END, 361)
    sol = solve_ivp(deriv_linear, (0, T_END), [DOSE, 0, 0],
                    t_eval=t_eval, method="LSODA", rtol=1e-8, atol=1e-10)
    te_good, cpe_good = euler(0.05)
    te_bad, cpe_bad = euler(1.0)

    fig, ax = plt.subplots(1, 2, figsize=(11, 4))
    ax[0].plot(sol.t, sol.y[0] / V1, "k-", lw=3, alpha=.4, label="solve_ivp (engine)")
    ax[0].plot(te_good, cpe_good, "b-", label="Euler dt=0.05 (good)")
    ax[0].plot(te_bad, cpe_bad, "r--", label="Euler dt=1.0 (BAD)")
    ax[0].set_title("Linear PK: solve_ivp vs Euler")
    ax[0].set_xlabel("min"); ax[0].set_ylabel("Cp (ug/mL)"); ax[0].legend()

    soln = solve_ivp(deriv_nonlinear, (0, T_END), [DOSE, 0, 0],
                     t_eval=t_eval, method="LSODA")
    ax[1].plot(soln.t, soln.y[0] / V1, "m-", label="solve_ivp (nonlinear MM)")
    ax[1].set_title("Same method handles nonlinear elimination")
    ax[1].set_xlabel("min"); ax[1].set_ylabel("Cp (ug/mL)"); ax[1].legend()
    plt.tight_layout(); plt.show()

    err = np.max(np.abs(np.interp(sol.t, te_good, cpe_good) - sol.y[0] / V1))
    print("Max |Euler(0.05) - solve_ivp| on linear model: %.3e ug/mL" % err)
