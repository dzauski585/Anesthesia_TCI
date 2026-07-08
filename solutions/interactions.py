"""
interactions.py  --  two-drug response surfaces done honestly.

One function covers synergy, additivity, and infra-additivity via a single
interaction parameter `alpha` (Greco form):

    Ua = Ce_a/Ce50_a ; Ub = Ce_b/Ce50_b
    U  = Ua + Ub + alpha*Ua*Ub
    Effect = U^gamma / (1 + U^gamma)        # 0..1, = 0.5 when U = 1

    alpha > 0  synergy        (propofol+opioid, propofol+dexmedetomidine)
    alpha = 0  additive       (propofol+KETAMINE -- the famous exception)
    alpha < 0  infra-additive (mild antagonism, also seen with ketamine)

The alpha values in INTERACTION_TABLE are qualitative/illustrative. For the
propofol-remifentanil tolerance-of-laryngoscopy surface, substitute the
published Ce50/gamma/alpha from Bouillon 2004 where marked.
"""

import numpy as np


def response_surface(ce_a, ce50_a, ce_b, ce50_b, alpha=0.0, gamma=4.0):
    """Combined drug effect, 0..1 (e.g. probability of tolerance/asleep)."""
    Ua = ce_a / ce50_a
    Ub = ce_b / ce50_b
    U = Ua + Ub + alpha * Ua * Ub
    return U ** gamma / (1.0 + U ** gamma)


# Qualitative interactions for the HYPNOTIC endpoint.  KEY POINT: ketamine is
# the exception -- additive/infra-additive, NOT synergistic like opioids.
INTERACTION_TABLE = {
    ("propofol", "remifentanil"):
        dict(alpha=2.0, kind="synergistic",
             note="Strong synergy (Bouillon 2004; Minto 2000). Dose-sparing."),
    ("propofol", "dexmedetomidine"):
        dict(alpha=1.0, kind="synergistic",
             note="Synergistic for sedation; opioid- and propofol-sparing."),
    ("propofol", "ketamine"):
        dict(alpha=0.0, kind="additive",
             note="ADDITIVE (sometimes infra-additive) for HYPNOSIS "
                  "(Hendrickx 2008; Hui 1995). NOT synergistic. Ketamine's "
                  "ketofol benefit is analgesia + hemodynamic stability, not "
                  "a hypnotic-depth bonus."),
}


def p_single(Ce, C50, gamma):
    """Week 18 single-drug endpoint probability: P = Ce^g / (C50^g + Ce^g).
    C50 is the effect-site concentration giving a 50% chance of the event."""
    return Ce ** gamma / (C50 ** gamma + Ce ** gamma)


def p_event(CeP, CeR, C50P, C50R, alpha, gamma):
    """Week 18 two-drug (propofol+remifentanil) endpoint probability on the
    Greco surface. Same maths as response_surface, named for the clinical
    endpoints (loss of responsiveness, tolerance of laryngoscopy)."""
    return response_surface(CeP, C50P, CeR, C50R, alpha=alpha, gamma=gamma)


def lookup_interaction(drug_a, drug_b):
    """Order-independent lookup; returns the dict or an additive default."""
    key = (drug_a, drug_b)
    if key in INTERACTION_TABLE:
        return INTERACTION_TABLE[key]
    if (drug_b, drug_a) in INTERACTION_TABLE:
        return INTERACTION_TABLE[(drug_b, drug_a)]
    return dict(alpha=0.0, kind="additive (assumed)",
                note="No data in table; assumed additive.")


def isobologram(ce50_a, ce50_b, alpha=0.0, gamma=4.0, effect=0.5, n=50):
    """Return (a_vals, b_vals): pairs of concentrations giving `effect`.

    A bowed-toward-origin curve = synergy; a straight line = additive."""
    target_U = (effect / (1 - effect)) ** (1.0 / gamma)   # U that gives `effect`
    a_vals = np.linspace(0, ce50_a * target_U, n)
    b_vals = []
    for ca in a_vals:
        Ua = ca / ce50_a
        # solve Ua + Ub + alpha*Ua*Ub = target_U  for Ub
        # Ub*(1 + alpha*Ua) = target_U - Ua
        denom = 1.0 + alpha * Ua
        Ub = (target_U - Ua) / denom if denom != 0 else 0.0
        b_vals.append(max(Ub, 0.0) * ce50_b)
    return a_vals, np.array(b_vals)


if __name__ == "__main__":
    # by-hand checks from Vol 2 (Ce50=1, gamma=4, Ua=Ub=0.5)
    assert abs(response_surface(0.5, 1, 0.5, 1, alpha=0.0) - 0.5) < 1e-9
    syn = response_surface(0.5, 1, 0.5, 1, alpha=2.0)
    infra = response_surface(0.5, 1, 0.5, 1, alpha=-0.5)
    assert syn > 0.83 and infra < 0.38
    print("additive=0.500  synergy=%.3f  infra-additive=%.3f" % (syn, infra))

    info = lookup_interaction("propofol", "ketamine")
    print("propofol+ketamine ->", info["kind"])
    assert info["alpha"] == 0.0       # not synergistic

    # Week 18 endpoints (by-hand checks from Vol 3)
    # single-drug unresponsiveness, C50=2.8, gamma=1.5, Ce=2.0 -> ~0.38
    assert abs(p_single(2.0, 2.8, 1.5) - 0.376) < 0.01
    # two-drug laryngoscopy, C50P=C50R=3.0, alpha=3, gamma=4, Ce 1.5/1.5 -> ~0.90
    assert abs(p_event(1.5, 1.5, 3.0, 3.0, 3.0, 4.0) - 0.904) < 0.01
    print("interactions.py self-tests passed.")
