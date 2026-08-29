def roberts_schedule(weight: float) -> tuple[float, list[tuple[float, float]]]:
    """
    Roberts (1981) propofol dosing scheme.
    Loading dose 1 mg/kg, then:
        10 mg/kg/hr for 10 min
         8 mg/kg/hr for 10 min
         6 mg/kg/hr thereafter

    Returns:
        bolus_mg  : loading dose in mg
        schedule  : list of (duration_min, rate_mg_min)
    """
    bolus_mg = 1.0 * weight

    schedule = [
        (10, 10 * weight / 60),   # 10 mg/kg/hr → mg/min
        (10,  8 * weight / 60),
        (40,  6 * weight / 60),
    ]

    return bolus_mg, schedule