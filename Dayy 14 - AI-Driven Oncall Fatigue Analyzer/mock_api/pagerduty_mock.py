import random
from datetime import datetime, timedelta

def generate_mock_incidents(engineers, days=30):
    incidents = []
    rotation_schedule = {}

    # Simulate a round-robin on-call rotation
    for day in range(days):
        date = datetime.now() - timedelta(days=day)
        on_call_engineer = engineers[day % len(engineers)]
        rotation_schedule[date.date()] = on_call_engineer

        # Simulate incident volume based on weekday/weekend
        is_weekend = date.weekday() >= 5
        base_incidents = random.randint(1, 3) if not is_weekend else random.randint(0, 2)

        for _ in range(base_incidents):
            hour = random.choices(
                population=list(range(24)),
                weights=[1]*6 + [2]*10 + [1]*8,  # fewer alerts at night
                k=1
            )[0]
            timestamp = datetime(date.year, date.month, date.day, hour, random.randint(0, 59))

            incidents.append({
                "id": f"INC-{random.randint(1000,9999)}",
                "created_at": timestamp.isoformat(),
                "assigned_to": on_call_engineer,
                "urgency": random.choices(["high", "low"], weights=[0.3, 0.7])[0],
                "status": random.choice(["triggered", "acknowledged", "resolved"]),
                "summary": f"Mock incident for {on_call_engineer} at {timestamp.strftime('%H:%M')}"
            })

    return incidents