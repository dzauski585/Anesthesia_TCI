def deriv(t, y, drug, rate):
    """Rates of change for [A1, A2, A3, Ce].
    t    : time (min). solve_ivp passes it in, even though we don't use it
    y    : [A1, A2, A3, Ce]  amounts in mg (A) and effect-site conc (Ce)
    drug : a Drug
    rate : current infusion rate into A1 (mg/min)
    """
    A1, A2, A3, Ce = y          # unpack: one name per position
    Cp = A1 / drug.V1

    # The model:
    #   dA1/dt = rate − (k10 + k12 + k13)·A1 + k21·A2 + k31·A3
    #   dA2/dt = k12·A1 − k21·A2
    #   dA3/dt = k13·A1 − k31·A3
    #   dCe/dt = ke0·(Cp − Ce)
    # TODO: one line of Python per equation (the constants live on `drug`)
    # TODO: return all four, in the same order as y
    ...
