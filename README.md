# haki-ya-kazi-mcp

[![haki-ya-kazi-mcp Glama score](https://glama.ai/mcp/servers/gabrielmahia/haki-ya-kazi-mcp/badges/score.svg)](https://glama.ai/mcp/servers/gabrielmahia/haki-ya-kazi-mcp)
[![smithery badge](https://smithery.ai/badge/@gabrielmahia/haki-ya-kazi-mcp)](https://smithery.ai/server/@gabrielmahia/haki-ya-kazi-mcp)


---
**Compatible with `claude-sonnet-5`** (released 2026-06-30) — Anthropic's most agentic
Sonnet yet. Runs multi-step tool chains end-to-end without stopping short.
Install: `pip install haki-ya-kazi-mcp` · Use with any MCP client.

---


> Kenya labour rights via MCP — minimum wages, dismissal, maternity rights, trade unions, ELRC

[![PyPI](https://img.shields.io/badge/PyPI-v0.1.0-blue)](https://github.com/gabrielmahia/haki-ya-kazi-mcp)
[![License](https://img.shields.io/badge/License-MIT-green)](https://github.com/gabrielmahia/haki-ya-kazi-mcp)
[![Layer](https://img.shields.io/badge/Layer-Social-purple)](https://github.com/gabrielmahia/haki-ya-kazi-mcp)

## Install

```bash
pip install haki-ya-kazi-mcp
```

## What it does

5 MCP tools covering Kenya labour rights and employment law. 1st world equivalent: **ACAS / NLRB**.

| Tool | Description |
|------|-------------|
| `minimum_wage_lookup` | Kenya minimum wage by sector and county |
| `unfair_dismissal_guide` | Unfair dismissal rights under Kenya Employment Act 2007 |
| `maternity_paternity_rights` | Maternity (90 days) and paternity (14 days) rights |
| `trade_union_directory` | Kenya trade union directory and worker rights organizations |
| `labour_court_guide` | ELRC filing guide — costs, timeline, free legal aid |

## Usage

```bash
# Run as standalone MCP server
haki-ya-kazi-mcp

# Or add to Claude Desktop / any MCP client
# Add to your MCP config: {"command": "haki-ya-kazi-mcp"}
```

## Part of the Kenya Coordination Infrastructure Stack

This is one of 23 MCP servers covering the full coordination infrastructure of East Africa:

**Economic:** mpesa · mkopo · bima · soko · sifa · remit · kra · faida  
**Physical:** wapimaji · nishati · usafiri · ardhi  
**Social:** afya · afya-ya-akili · elimu · kazi · haki-ya-kazi · kilimo · jumuia  
**Civic:** nyumba · habari · mazingira · civic-agent-kit  

→ [The Nairobi Stack](https://gabrielmahia.github.io/nairobi-stack)  
→ [Full Portfolio](https://gabrielmahia.github.io)

## Trust Integrity

All data in this server is **clearly labeled DEMO** where synthetic. Verify all operational data with the relevant Kenyan government authority before use.

## License

MIT © Gabriel Mahia | [AI-KungFU](https://github.com/gabrielmahia) | contact@aikungfu.dev

> *Decision infrastructure for East Africa*

## Part of the East Africa Coordination Stack

This MCP server is one of 32 tools in the Kenya coordination infrastructure.
Connect it to [`africa-coord-bus`](https://github.com/gabrielmahia/africa-coord-bus) —
the coordination event bus that routes signals between domains automatically.

```bash
pip install africa-coord-bus
```

All 32 servers: [pypi.org/user/gmahia](https://pypi.org/user/gmahia/)
Live demo: [coord-cascade-demo](https://github.com/gabrielmahia/coord-cascade-demo)