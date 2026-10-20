"""HakiYaKaziMCP — Kenya Labour Rights Tools (5 tools). All data DEMO."""
from __future__ import annotations

from typing import Annotated, Optional

from fastmcp import FastMCP
from pydantic import Field

# Annotations tell clients which tools are safe to auto-approve (read-only, no side effects).
READ_ONLY = {"readOnlyHint": True, "idempotentHint": True, "openWorldHint": False}

mcp = FastMCP(name="haki-ya-kazi-mcp", instructions="Kenya labour rights tools. DEMO data only.")

@mcp.tool(name="minimum_wage_lookup", description="Kenya statutory minimum wages under the Regulation of Wages (General) (Amendment) Order 2026, effective 1 May 2026: the general labourer, cleaner, gardener, house servant and day watchman minimum (KES 18,047.40 a month in Nairobi, Mombasa, Kisumu, Nakuru and Eldoret; KES 9,268 elsewhere) and two clerical and trades bands. Use when someone asks whether they are paid at least the minimum wage. sector is matched against the occupations in the table (spaces become underscores); an occupation that is not in the table returns matched false with the available keys and what is NOT covered (agriculture, private security, hospitality), never the general wage. The county argument is accepted but does not change the result. Returns the source, the matching wages with monthly (and where known daily and hourly) amounts, the available keys and a note. A DEMO table of figures reported by FKE and the press: verify against the Kenya Gazette. Read-only; no side effects.", annotations=READ_ONLY)
def minimum_wage_lookup(sector: Annotated[str | None, Field(description="Optional occupation keyword such as security guard, domestic worker or hospitality; spaces become underscores; partial match. Omit for all occupations.")] = None, county: Annotated[str | None, Field(description="Accepted but ignored: it is echoed back and does not change the wages returned.")] = None) -> dict:
    # Regulation of Wages (General) (Amendment) Order, 2026: effective 1 May 2026 (12% general increase), Legal Notices 108 and 109, Kenya Gazette Supplements 95 and 96.
    # Figures as reported by the Federation of Kenya Employers, Kenya Times, K24 and Kenyans.co.ke (cross-checked); verify against the Gazette.
    CITIES = "Nairobi, Mombasa, Kisumu, Nakuru and Eldoret"
    WAGES_2026 = {
        "general_labourer_cities": {"monthly_kes": 18047.40, "daily_kes": 868.44, "hourly_kes": 161.34, "note": f"General labourer, cleaner, sweeper, gardener, children's ayah, house servant, day watchman, messenger: {CITIES}"},
        "domestic_worker_cities": {"monthly_kes": 18047.40, "daily_kes": 868.44, "hourly_kes": 161.34, "note": f"Domestic workers (house servant, ayah, gardener, cleaner): {CITIES}"},
        "general_labourer_other_areas": {"monthly_kes": 9268, "note": "General labourer in other parts of the country (reported; daily and hourly rates not in this table)"},
        "junior_clerk_and_similar": {"monthly_kes": 23350.21, "note": "Machinists, shoe repairers, petrol station attendants, junior clerks, laundry operators, light tractor drivers (reported; the location band is not stated in the sources read)"},
        "general_clerk_and_similar": {"monthly_kes": 27796.51, "note": "Receptionists, telephone operators, storekeepers, general clerks, pattern designers, garment cutters (reported; the location band is not stated in the sources read)"},
    }
    NOT_IN_TABLE = "Not in this table: agricultural wages (a separate order raised them 15% in 2026), private security guards, hospitality and other regulated sectors. Check the Gazette or the Ministry of Labour."
    SOURCE = "Regulation of Wages (General) (Amendment) Order, 2026, effective 1 May 2026, as reported by FKE, Kenya Times, K24 and Kenyans.co.ke; DEMO table, verify against the Kenya Gazette"
    if sector:
        s = sector.lower().replace(" ", "_")
        matched = {k: v for k, v in WAGES_2026.items() if s in k}
        return {"source": SOURCE, "sector": sector, "county": county, "wages": matched, "matched": bool(matched), "available": list(WAGES_2026), "not_in_table": NOT_IN_TABLE,
                "note": "Minimum wages are set by Legal Notice; the county argument does not change the result. Verify at labour.go.ke."}
    return {"source": SOURCE, "all_minimum_wages": WAGES_2026, "not_in_table": NOT_IN_TABLE, "effective": "1 May 2026 (retroactive; gazetted by Legal Notices 108 and 109)", "portal": "labour.go.ke"}

@mcp.tool(name="unfair_dismissal_guide", description="Kenya unfair-dismissal guidance under the Employment Act 2007: statutory notice, the need for a valid reason, redundancy steps and pay, summary dismissal, constructive dismissal, discrimination, the remedy and the time limit to file. Use when someone describes how they were dismissed or laid off. Keywords in situation (no_notice, no_reason, redundancy, summary, constructive, discrimination) select entries; if none match it returns the general time-limit guidance; with no argument it returns all situations. Not legal advice; static summary labelled DEMO, so confirm with an advocate or the ELRC. Read-only.", annotations=READ_ONLY)
def unfair_dismissal_guide(situation: Annotated[str | None, Field(description="Optional description of what happened, such as no notice, redundancy or summary dismissal. Omit for all situations.")] = None) -> dict:
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

@mcp.tool(name="maternity_paternity_rights", description="Kenya maternity, paternity and adoption leave rights under the Employment Act 2007 (sections 29-30): leave length and pay, breastfeeding breaks, protection from dismissal, and how hospital bills are covered through SHA (which replaced NHIF in October 2024). Use when someone asks about leave for a new child. Keywords in query (maternity_leave, maternity_pay, paternity_leave, adoption, breastfeeding, protection) select entries; if none match, all rights are returned. Static summary labelled DEMO: verify current entitlements with the Ministry of Labour and sha.go.ke. Read-only.", annotations=READ_ONLY)
def maternity_paternity_rights(query: Annotated[str | None, Field(description="Optional topic such as paternity leave or breastfeeding. Omit for all rights.")] = None) -> dict:
    INFO = {
        "maternity_leave":  "3 months (90 days) fully paid. Can start 2 weeks before due date. Cannot be dismissed during.",
        "maternity_pay":    "Full basic salary during maternity leave. Employer pays (reimbursement from the health scheme is not automatic; SHA replaced NHIF in Oct 2024).",
        "paternity_leave":  "2 weeks (14 days) fully paid for fathers.",
        "adoption_leave":   "Female adopting a child under 3: 3 months leave. Male adopting: 2 weeks.",
        "breastfeeding":    "Right to 30-minute breastfeeding breaks twice daily for 3 months after return.",
        "protection":       "Cannot dismiss, demote, or discriminate against employee for taking maternity/paternity leave.",
        "nssf_maternity":   "Maternity hospital bills are covered through SHA (which replaced NHIF in Oct 2024) with prior SHA registration; verify details at sha.go.ke.",
    }
    if query:
        q = query.lower()
        matched = {k: v for k, v in INFO.items() if k in q or any(w in q for w in k.split("_"))}
        return {"source": "DEMO — Employment Act 2007 s.29-30", "query": query,
                "guidance": matched or INFO}
    return {"source": "DEMO — Employment Act 2007", "rights": INFO,
            "legal_basis": "Employment Act 2007, Sections 29-30", "ministry": "labour.go.ke"}

@mcp.tool(name="trade_union_directory", description="A short, partial directory of major Kenyan trade unions and worker-rights bodies (COTU-K, KNUT, KUDHEIHA, KEWU, KAWU) with their sector and contact details, plus the constitutional right to join a union. Use when someone asks which union covers their sector. A sector text filters the list (falls back to all if nothing matches). Contact numbers are unverified and the list is not exhaustive. Read-only.", annotations=READ_ONLY)
def trade_union_directory(sector: Annotated[str | None, Field(description="Optional sector text such as education, aviation or hospitality. Omit for all unions.")] = None) -> dict:
    UNIONS = [
        {"name": "COTU-K (Central Organization of Trade Unions Kenya)", "sector": "All sectors",
         "role": "Umbrella body for Kenya trade unions", "contact": "020-2721444 | cotu.co.ke"},
        {"name": "KNUT (Kenya National Union of Teachers)", "sector": "Education",
         "role": "TSC teachers' union", "contact": "020-2721990"},
        {"name": "KUDHEIHA (Kenya Union of Domestic, Hotel, Educational Institutions, Hospital & Allied Workers)",
         "sector": "Hospitality, domestic", "contact": "020-2726920"},
        {"name": "KEWU (Kenya Electrical Workers Union)", "sector": "Energy, electrical", "contact": "020-2222185"},
        {"name": "KAWU (Kenya Aviation Workers Union)", "sector": "Aviation", "contact": "0722200750"},
    ]
    if sector:
        UNIONS = [u for u in UNIONS if sector.lower() in u["sector"].lower()] or UNIONS
    return {"source": "DEMO — MOLE Trade Union Registry", "sector": sector, "unions": UNIONS,
            "right_to_join": "All workers have right to join a union under Kenya Constitution Art.41",
            "registration": "File with Labour Relations Court if denied union access"}

@mcp.tool(name="labour_court_guide", description="How to take a workplace dispute to the Employment and Labour Relations Court (ELRC) in Kenya: what it handles, how to file, cost, typical timeline, free legal help, reporting to the County Labour Office first, and NSSF disputes. Use when someone asks where or how to bring a labour claim. Keywords in query (jurisdiction, how_to_file, cost, timeline, free_help, labour_office, nssf_disputes) select entries; if none match, all guidance is returned. Not legal advice; static summary labelled DEMO, so verify fees and procedure with the court registry. Read-only.", annotations=READ_ONLY)
def labour_court_guide(query: Annotated[str | None, Field(description="Optional topic such as filing cost or free legal help. Omit for all guidance.")] = None) -> dict:
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

def main() -> None:
    """Console entry point."""
    mcp.run()
