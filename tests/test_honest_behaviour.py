from haki_ya_kazi_mcp import server

_fn = lambda name: (getattr(server, name).fn if hasattr(getattr(server, name), "fn") else getattr(server, name))


def test_the_county_argument_really_is_ignored_as_the_description_says():
    a, b = _fn("minimum_wage_lookup")(sector="security guard", county="Nairobi"), _fn("minimum_wage_lookup")(sector="security guard", county="Turkana")
    assert a["wages"] == b["wages"]


def test_the_nssf_is_not_listed_as_a_trade_union():
    """The NSSF is a statutory pension fund, not a union."""
    assert all("NSSF" not in u["name"] for u in _fn("trade_union_directory")()["unions"])
