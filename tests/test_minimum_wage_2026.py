from haki_ya_kazi_mcp import server

_fn = lambda name: (getattr(server, name).fn if hasattr(getattr(server, name), "fn") else getattr(server, name))


def test_the_general_minimum_is_the_may_2026_figure_not_the_2024_one():
    """Regulation of Wages (General) (Amendment) Order 2026: KES 18,047.40 a month (868.44 a day) in the five cities, up from 16,113.75; 9,268 elsewhere."""
    r = _fn("minimum_wage_lookup")("domestic worker")
    w = r["wages"]["domestic_worker_cities"]
    assert w["monthly_kes"] == 18047.40 and w["daily_kes"] == 868.44 and r["matched"] is True
    assert _fn("minimum_wage_lookup")("general labourer")["wages"]["general_labourer_other_areas"]["monthly_kes"] == 9268


def test_an_occupation_not_in_the_table_is_not_silently_answered_with_the_general_wage():
    r = _fn("minimum_wage_lookup")("security guard")
    assert r["matched"] is False and r["wages"] == {} and "private security" in r["not_in_table"]


def test_no_unsourced_figures_from_the_old_table_remain():
    text = str(_fn("minimum_wage_lookup")(None))
    for stale in ("16168", "14642", "23756", "22572", "26390", "Wage Order 2024"):
        assert stale not in text, stale
