def study_schedule(permanence_period, target_time):
    try:
        count = 0
        for entrada, saida in permanence_period:
            if entrada <= target_time and saida >= target_time:
                count += 1
        return count
    except TypeError:
        return None
