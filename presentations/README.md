# Presentations

Demo decks generated from live Jenkins data (via Jenkins MCP) for the QA Rialto
automation programme.

| File | Description |
| --- | --- |
| `Managing_Automation_Builds_QA_Rialto.pptx` | 11-slide demo deck: how QA manages Jenkins automation builds across Rialto trunk, 8.7.x, 8.6.x and Rialto Internal Integration pipelines, plus the AI-assisted reporting workflow. |
| `generate_presentation.py` | Python script (uses `python-pptx`) that regenerates the deck. |

## Regenerate

```bash
pip install python-pptx
python presentations/generate_presentation.py
```

The script writes `Managing_Automation_Builds_QA_Rialto.pptx` next to itself.
