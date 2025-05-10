from typing import List, Dict

def correlate_evidence(osint: List[Dict], financial_data: List[Dict], timeline: List[Dict]) -> Dict:
    """
    Match OSINT, financial data, and cyber logs into a unified case file.
    """
    case_file = {
        "osint": osint,
        "financial_data": financial_data,
        "timeline": timeline
    }
    return case_file