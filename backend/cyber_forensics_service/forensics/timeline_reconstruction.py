from typing import List, Dict

def build_timeline(logs: List[Dict]) -> List[Dict]:
    """
    Extract and sort logs into a chronological timeline with actor, event, impact.
    """
    timeline = []
    for log in logs:
        entry = {
            "timestamp": log.get("timestamp"),
            "actor": log.get("actor"),
            "event": log.get("event"),
            "impact": log.get("impact")
        }
        timeline.append(entry)
    timeline.sort(key=lambda x: x["timestamp"])
    return timeline