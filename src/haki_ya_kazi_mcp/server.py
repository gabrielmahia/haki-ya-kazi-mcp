"""HakiYaKaziMCP — Kenya Labour Rights Tools (5 tools). All data DEMO."""
from __future__ import annotations
from typing import Optional
from fastmcp import FastMCP
mcp = FastMCP(name="haki-ya-kazi-mcp", instructions="Kenya labour rights tools. DEMO data only.")

@mcp.tool(name="minimum_wage_lookup", description="Kenya minimum wage by sector and county. DEMO.")
def minimum_wage_lookup(sector: Optional[str] = None, county: Optional[str] = None) -> dict:
    WAGES_2025 = {
        "general_laborer_nairobi": {"monthly_kes": 16168, "daily_kes": 538, "note": "General laborer, Nairobi/Mombasa/Kisumu"},
        "general_laborer_other":   {"monthly_kes": 14642, "daily_kes": 487, "note": "General laborer, other areas"},
        "clerical_officer":        {"monthly_kes": 25000, "daily_kes": 833, "note": "Clerical/office workers"},
        "security_guard_nairobi":  {"monthly_kes": 23756, "daily_kes": 791, "note": "Security guards, Nairobi"},
        "domestic_worker_nairobi": {"monthly_kes": 16168, "daily_kes": 538, "note": "Domestic workers, Nairobi"},
        "teacher_p1":              {"monthly_kes": 26390, "note": "P1 teacher (TSC scale)"},
        "agriculture":             {"monthly_kes": 14642, "note": "Agricultural workers, general"},
        "hospitality":             {"monthly_kes": 22572, "note": "Hotel/hospitality workers"},
    }
    if sector:
        s = sector.lower().replace(" ","_")
        matched = {k: v for k, v in WAGES_2025.items() if s in k}
        return {"source": "DEMO — Ministry of Labour Wage Order 2024", "sector": sector, "county": county,
                "wages": matched or {"general": WAGES_2025["general_laborer_nairobi"]},
                "note": "Wages reviewed annually. Verify at parliament.go.ke/labour or Ministry of Labour."}
    return {"source": "DEMO — Ministry of Labour Wage Order 2024", "all_minimum_wages": WAGES_2025,
            "annual_review": "Wages set by Legal Notice each April/May",
            "portal": "labour.go.ke | 020-2729800"}

@mcp.tool(name="unfair_dismissal_guide", description="Kenya unfair dismissal rights under Employment Act 2007. DEMO.")
def unfair_dismissal_guide(situation: Optional[str] = None) -> dict:
    SITUATIONS = {
        "no_notice":       "Entitled to statutory notice: 28 days (monthly paid) or 7 days (weekly paid). Or payment in lieu.",
        "no_reason":       "Employer must give valid reason for termination. Absence of reason = unfair dismissal.",
        "redundancy":      "Must follow: genuine redundancy + fair selection + notice + redundancy pay (15 days per year served).",
        "summary":         "Allowed only for gross misconduct. Examples: theft, assault, gross negligence, insubordination. Must be proved.",
        "constructive":    "Resignation due to employer making work impossible = treated as dismissal. File complaint within 3 years.",
        "discrimination":  "Dismissal due to gender, pregnancy, disability, HIV status, union membership = automatically unfair.",
    }
    if situation:
        s = situation.lower()
        matched = {k: v for k, v in SITUATIONS.items() if k in s or any(w in s for w in k.split("_"))}
        return {"source": "DEMO — Employment Act 2007 (Kenya)", "situation": situation,
                "guidance": matched or {"general": "File complaint at ELRC within 3 years of dismissal."},
                "remedy": "Reinstatement, or 1-12 months salary compensation. ELRC has discretion."}
    return {"source": "DEMO — Employment Act 2007", "all_situations": SITUATIONS,
            "time_limit": "File within 3 years of dismissal at ELRC",
            "free_advice": "Federation of Kenya Employers (FKE) for employer guidance. COTU for worker guidance."}

@mcp.tool(name="maternity_paternity_rights", description="Kenya maternity and paternity leave rights. DEMO.")
def maternity_paternity_rights(query: Optional[str] = None) -> dict:
    INFO = {
        "maternity_leave":  "3 months (90 days) fully paid. Can start 2 weeks before due date. Cannot be dismissed during.",
        "maternity_pay":    "Full basic salary during maternity leave. Employer pays (reimburse via NHIF not automatic).",
        "paternity_leave":  "2 weeks (14 days) fully paid for fathers.",
        "adoption_leave":   "Female adopting a child under 3: 3 months leave. Male adopting: 2 weeks.",
        "breastfeeding":    "Right to 30-minute breastfeeding breaks twice daily for 3 months after return.",
        "protection":       "Cannot dismiss, demote, or discriminate against employee for taking maternity/paternity leave.",
        "nssf_maternity":   "NHIF covers maternity hospital bills. ANC visits and normal delivery at NHIF-accredited facilities.",
    }
    if query:
        q = query.lower()
        matched = {k: v for k, v in INFO.items() if k in q or any(w in q for w in k.split("_"))}
        return {"source": "DEMO — Employment Act 2007 s.29-30", "query": query,
                "guidance": matched or INFO}
    return {"source": "DEMO — Employment Act 2007", "rights": INFO,
            "legal_basis": "Employment Act 2007, Sections 29-30", "ministry": "labour.go.ke"}

@mcp.tool(name="trade_union_directory", description="Kenya trade union directory and worker rights organizations. DEMO.")
def trade_union_directory(sector: Optional[str] = None) -> dict:
    UNIONS = [
        {"name": "COTU-K (Central Organization of Trade Unions Kenya)", "sector": "All sectors",
         "role": "Umbrella body for Kenya trade unions", "contact": "020-2721444 | cotu.co.ke"},
        {"name": "KNUT (Kenya National Union of Teachers)", "sector": "Education",
         "role": "TSC teachers' union", "contact": "020-2721990"},
        {"name": "KUDHEIHA (Kenya Union of Domestic, Hotel, Educational Institutions, Hospital & Allied Workers)",
         "sector": "Hospitality, domestic", "contact": "020-2726920"},
        {"name": "KEWU (Kenya Electrical Workers Union)", "sector": "Energy, electrical", "contact": "020-2222185"},
        {"name": "KAWU (Kenya Aviation Workers Union)", "sector": "Aviation", "contact": "0722200750"},
        {"name": "NSSF (National Social Security Fund)", "sector": "All — provident fund", "contact": "nssf.or.ke | 020-2733333"},
    ]
    if sector:
        UNIONS = [u for u in UNIONS if sector.lower() in u["sector"].lower()] or UNIONS
    return {"source": "DEMO — MOLE Trade Union Registry", "sector": sector, "unions": UNIONS,
            "right_to_join": "All workers have right to join a union under Kenya Constitution Art.41",
            "registration": "File with Labour Relations Court if denied union access"}

@mcp.tool(name="labour_court_guide", description="Labour Relations Court and ELRC guidance in Kenya. DEMO.")
def labour_court_guide(query: Optional[str] = None) -> dict:
    INFO = {
        "jurisdiction": "ELRC handles: dismissal, wages, discrimination, collective bargaining disputes.",
        "how_to_file":  "Complete Form A (available at court registries). File at Nairobi ELRC or county ELRC (Mombasa, Kisumu, Nakuru, Nyeri, Garissa, Eldoret).",
        "cost":         "Filing fee: KES 3,000 for individuals. No filing fee for workers earning under minimum wage.",
        "timeline":     "Hearing within 60 days. Judgment within 6 months typically.",
        "free_help":    "Legal aid: FIDA Kenya (women), LSK Legal Aid, Kituo Cha Sheria (labour rights NGO)",
        "labour_office":"Report labour violations to nearest County Labour Office first — free mediation available.",
        "nssf_disputes":"NSSF disputes: NSSF Complaints Unit or ELRC. Employer non-remittance: criminal offence.",
    }
    if query:
        q = query.lower()
        matched = {k: v for k, v in INFO.items() if k in q or any(w in q for w in k.split("_"))}
        return {"source": "DEMO — ELRC and judiciary.go.ke", "query": query,
                "guidance": matched or INFO}
    return {"source": "DEMO — Kenya Employment and Labour Relations Court", "guidance": INFO,
            "registry": "judiciary.go.ke/labour | 020-2222288",
            "disclaimer": "Not legal advice. Consult an advocate or free legal aid."}
