def generate_study_plan(subjects, hours_per_week=20):
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    plan = {}

    total_priority = sum(s[1] for s in subjects)

    for day in days:
        plan[day] = []
        remaining = hours_per_week / 7

        for subject, priority, required_hours in subjects:
            allocate = (priority / total_priority) * remaining
            plan[day].append(f"{subject}: {round(allocate, 1)} hrs")

    return plan
