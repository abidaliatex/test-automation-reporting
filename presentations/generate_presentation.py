"""Generate the 'Managing Automation Builds — QA Rialto' demo PPTX.

Data snapshot pulled from Jenkins (via the Jenkins MCP server) for the
QA Rialto pipelines: trunk, 8.7.x, 8.6.x and Rialto Internal Integration.

Run:
    pip install python-pptx
    python presentations/generate_presentation.py
"""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION
from pptx.enum.text import PP_ALIGN
from datetime import datetime, timezone
import os

# ------------- Theme colours -------------
ATEX_BLUE   = RGBColor(0x0B, 0x3D, 0x91)
ATEX_ACCENT = RGBColor(0x00, 0xA6, 0xD6)
DARK        = RGBColor(0x1F, 0x2A, 0x44)
LIGHT_BG    = RGBColor(0xF4, 0xF7, 0xFB)
WHITE       = RGBColor(0xFF, 0xFF, 0xFF)
GREY        = RGBColor(0x55, 0x5F, 0x77)
GREEN       = RGBColor(0x2E, 0xA0, 0x43)
AMBER       = RGBColor(0xE0, 0x8A, 0x00)
RED         = RGBColor(0xCC, 0x1F, 0x2E)

prs = Presentation()
prs.slide_width  = Inches(13.333)
prs.slide_height = Inches(7.5)
SW, SH = prs.slide_width, prs.slide_height
BLANK = prs.slide_layouts[6]

def add_bg(slide, color=WHITE):
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SW, SH)
    bg.line.fill.background()
    bg.fill.solid(); bg.fill.fore_color.rgb = color
    return bg

def add_bar(slide, y=Inches(0), height=Inches(0.55), color=ATEX_BLUE):
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, y, SW, height)
    bar.line.fill.background()
    bar.fill.solid(); bar.fill.fore_color.rgb = color
    return bar

def add_text(slide, left, top, width, height, text, size=18, bold=False,
             color=DARK, align=PP_ALIGN.LEFT, font="Calibri"):
    tb = slide.shapes.add_textbox(left, top, width, height)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.05)
    tf.margin_top = tf.margin_bottom = Inches(0.02)
    lines = text.split("\n") if isinstance(text, str) else text
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        r = p.add_run(); r.text = line
        r.font.size = Pt(size); r.font.bold = bold
        r.font.color.rgb = color; r.font.name = font
    return tb

def title_slide_header(slide, title, subtitle=None):
    add_bar(slide, y=0, height=Inches(0.7), color=ATEX_BLUE)
    add_text(slide, Inches(0.4), Inches(0.08), Inches(12.5), Inches(0.55),
             title, size=24, bold=True, color=WHITE)
    if subtitle:
        add_text(slide, Inches(0.4), Inches(0.85), Inches(12.5), Inches(0.4),
                 subtitle, size=13, color=GREY, bold=True)
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.4), Inches(1.25),
                                  Inches(1.2), Inches(0.06))
    line.line.fill.background(); line.fill.solid()
    line.fill.fore_color.rgb = ATEX_ACCENT

def add_footer(slide, page_no):
    add_text(slide, Inches(0.4), Inches(7.1), Inches(6), Inches(0.3),
             "Automation Build Management  |  QA Rialto  |  Confidential",
             size=9, color=GREY)
    add_text(slide, Inches(11.5), Inches(7.1), Inches(1.5), Inches(0.3),
             f"{page_no}", size=9, color=GREY, align=PP_ALIGN.RIGHT)

def kpi_card(slide, left, top, w, h, value, label, accent=ATEX_ACCENT):
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, w, h)
    card.adjustments[0] = 0.08
    card.line.color.rgb = RGBColor(0xE1, 0xE6, 0xEF)
    card.line.width = Pt(0.75)
    card.fill.solid(); card.fill.fore_color.rgb = WHITE
    strip = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, w, Inches(0.12))
    strip.line.fill.background(); strip.fill.solid(); strip.fill.fore_color.rgb = accent
    add_text(slide, left, top + Inches(0.25), w, Inches(0.9),
             value, size=32, bold=True, color=ATEX_BLUE, align=PP_ALIGN.CENTER)
    add_text(slide, left, top + h - Inches(0.55), w, Inches(0.4),
             label, size=11, color=GREY, align=PP_ALIGN.CENTER, bold=True)

def bullet_box(slide, left, top, w, h, heading, items, heading_color=ATEX_BLUE):
    box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, w, h)
    box.adjustments[0] = 0.05
    box.line.color.rgb = RGBColor(0xE1, 0xE6, 0xEF); box.line.width = Pt(0.75)
    box.fill.solid(); box.fill.fore_color.rgb = WHITE
    add_text(slide, left + Inches(0.25), top + Inches(0.18), w - Inches(0.4),
             Inches(0.4), heading, size=15, bold=True, color=heading_color)
    tb = slide.shapes.add_textbox(left + Inches(0.25), top + Inches(0.62),
                                  w - Inches(0.4), h - Inches(0.7))
    tf = tb.text_frame; tf.word_wrap = True
    for i, itm in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = PP_ALIGN.LEFT
        p.space_after = Pt(4)
        r = p.add_run(); r.text = "\u25B8  " + itm
        r.font.size = Pt(12); r.font.color.rgb = DARK; r.font.name = "Calibri"

# ================================================================
# SLIDE 1 – Title
# ================================================================
s = prs.slides.add_slide(BLANK)
add_bg(s, ATEX_BLUE)
block = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(5.9), SW, Inches(1.6))
block.line.fill.background(); block.fill.solid(); block.fill.fore_color.rgb = DARK
strip = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(5.85), SW, Inches(0.08))
strip.line.fill.background(); strip.fill.solid(); strip.fill.fore_color.rgb = ATEX_ACCENT

add_text(s, Inches(0.7), Inches(1.6), Inches(12), Inches(0.6),
         "QA AUTOMATION", size=18, bold=True, color=ATEX_ACCENT)
add_text(s, Inches(0.7), Inches(2.1), Inches(12), Inches(1.6),
         "Managing Automation Builds\nfor Rialto Advertising Platform",
         size=40, bold=True, color=WHITE)
add_text(s, Inches(0.7), Inches(4.4), Inches(12), Inches(0.5),
         "Trunk  \u2022  8.7.x  \u2022  8.6.x  \u2022  Rialto Internal Integration  \u2022  AI-Assisted Pipelines",
         size=16, color=WHITE)
add_text(s, Inches(0.7), Inches(6.15), Inches(8), Inches(0.4),
         "Presented by: QA Automation Lead", size=14, bold=True, color=WHITE)
add_text(s, Inches(0.7), Inches(6.6), Inches(8), Inches(0.4),
         f"Snapshot date: {datetime.now(timezone.utc).strftime('%d %B %Y')}", size=12,
         color=RGBColor(0xC7,0xD4,0xE6))
add_text(s, Inches(10.5), Inches(6.35), Inches(2.5), Inches(0.5),
         "atex  |  Rialto QA", size=14, bold=True, color=WHITE, align=PP_ALIGN.RIGHT)

# ================================================================
# SLIDE 2 – Agenda
# ================================================================
s = prs.slides.add_slide(BLANK); add_bg(s)
title_slide_header(s, "Agenda", "What we will cover in this session")
items = [
    ("1", "The QA automation landscape at Atex Rialto"),
    ("2", "Pipelines under management \u2014 Trunk, 8.7.x, 8.6.x and Rialto Internal"),
    ("3", "How I manage the builds day-to-day (workflow & tooling)"),
    ("4", "AI-assisted build triage & reporting pipeline"),
    ("5", "Key metrics & recent build snapshot from Jenkins"),
    ("6", "Benefits delivered to the team & to the business"),
    ("7", "Roadmap and next steps"),
]
top = Inches(1.8)
for i,(num, txt) in enumerate(items):
    y = top + Inches(i*0.6)
    circle = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(1.0), y, Inches(0.5), Inches(0.5))
    circle.line.fill.background(); circle.fill.solid(); circle.fill.fore_color.rgb = ATEX_ACCENT
    add_text(s, Inches(1.0), y+Inches(0.05), Inches(0.5), Inches(0.4),
             num, size=16, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    add_text(s, Inches(1.7), y+Inches(0.05), Inches(11), Inches(0.5),
             txt, size=16, color=DARK)
add_footer(s, 2)

# ================================================================
# SLIDE 3 – Automation Landscape
# ================================================================
s = prs.slides.add_slide(BLANK); add_bg(s)
title_slide_header(s, "The QA Automation Landscape",
                   "A multi-version, multi-layer test estate on Jenkins")
cats = [
    ("Trunk", "Latest development line\n\n\u2022 RIALTO B2A (CASS) APIs\n\u2022 RIALTO B2C APIs\n\u2022 Web B2A E2E\n\u2022 MediaHouse & AgencyBackend", ATEX_BLUE),
    ("Release 8.7.x", "Current release branch\n\n\u2022 RIALTO B2C APIs 8.7.x\n\u2022 Web B2A E2E 8.7.x\n\u2022 B2A RIALTOMAIN 8.7.x\n\u2022 MediaHouse 8.7.x", ATEX_ACCENT),
    ("Release 8.6.x", "LTS / supported branch\n\n\u2022 RIALTO B2A 8.6.x\n\u2022 RIALTO B2C 8.6.x\n\u2022 Web B2A 8.6.x", GREEN),
    ("Rialto Internal", "Cross-version integration\n\n\u2022 B2A Integration Testing\n  Internal \u2013 trunk\n\u2022 Internal \u2013 trunk demo\n\u2022 AgencyBE8.7 \u00D7 MH-8.6\n  compatibility runs", AMBER),
]
cw = Inches(3.0); gap = Inches(0.2); startx = Inches(0.5); y = Inches(1.7)
for i,(h,body,c) in enumerate(cats):
    x = startx + i*(cw + gap)
    card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, Inches(4.9))
    card.adjustments[0] = 0.04
    card.line.color.rgb = RGBColor(0xE1,0xE6,0xEF); card.line.width=Pt(0.75)
    card.fill.solid(); card.fill.fore_color.rgb = WHITE
    strip = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, cw, Inches(0.6))
    strip.line.fill.background(); strip.fill.solid(); strip.fill.fore_color.rgb = c
    add_text(s, x, y+Inches(0.1), cw, Inches(0.5), h, size=16, bold=True,
             color=WHITE, align=PP_ALIGN.CENTER)
    add_text(s, x+Inches(0.2), y+Inches(0.8), cw-Inches(0.4), Inches(4.0),
             body, size=12, color=DARK)
add_text(s, Inches(0.5), Inches(6.75), Inches(12.3), Inches(0.4),
         "Over 25 Jenkins pipelines actively managed across API, Web-UI and integration layers.",
         size=12, bold=True, color=GREY, align=PP_ALIGN.CENTER)
add_footer(s, 3)

# ================================================================
# SLIDE 4 – Pipelines under management (table-style)
# ================================================================
s = prs.slides.add_slide(BLANK); add_bg(s)
title_slide_header(s, "Pipelines Under Management",
                   "Live inventory from Jenkins \u2014 QA Rialto scope")

rows = [
    ("Job", "Type", "Branch", "Last #", "Status"),
    ("automationrunCAI-RIALTO-B2A-trunk",              "API",  "trunk",  "401", "UNSTABLE"),
    ("automationrunCAI-RIALTO-B2C-trunk",              "API",  "trunk",  "125", "UNSTABLE"),
    ("automationrunCAI-RIALTO-B2C-8.7.x",              "API",  "8.7.x",  "97",  "UNSTABLE"),
    ("automationRun-Rialto-Web-B2A-E2E-trunk",         "Web E2E", "trunk", "\u2014", "Active"),
    ("automationRun-Rialto-Web-B2A-E2E-8.7.x",         "Web E2E", "8.7.x", "\u2014", "Active"),
    ("automationRun-Rialto-Web-B2A-RIALTOMAIN-trunk",  "Web E2E", "trunk", "\u2014", "Active"),
    ("automationRun-Rialto-Web-B2A-RIALTOMAIN-8.7.x",  "Web E2E", "8.7.x", "\u2014", "Active"),
    ("automationRun-RialtoWeb-B2A-MediaHouse-trunk",   "Web E2E", "trunk", "\u2014", "Active"),
    ("automationRun-RialtoWeb-B2A-AgencyBackend-Customer-trunk","Web E2E","trunk","\u2014","Active"),
    ("automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk", "Internal Int.", "trunk", "187", "UNSTABLE"),
    ("automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo", "Internal Int.", "trunk", "512", "UNSTABLE"),
    ("automationrunCAI-RIALTO-B2A-Internal-AgencyBE8.7-MH-8.6", "Internal Int.", "mixed",  "\u2014", "Active"),
    ("AutomationManager-Rialto-trunk / 8.7.x / APIs",  "Manager", "all", "\u2014", "Orchestrator"),
    ("AI-Pipeline (build report generation)",          "AI",   "n/a",   "259", "SUCCESS"),
]
tx, ty, tw = Inches(0.4), Inches(1.7), Inches(12.5)
row_h = Inches(0.34)
tbl = s.shapes.add_table(len(rows), 5, tx, ty, tw, row_h*len(rows)).table
widths = [Inches(5.6), Inches(1.6), Inches(1.3), Inches(1.2), Inches(2.8)]
for i,w in enumerate(widths): tbl.columns[i].width = w
for r_i,row in enumerate(rows):
    for c_i,val in enumerate(row):
        cell = tbl.cell(r_i, c_i)
        cell.text = ""
        tf = cell.text_frame; tf.margin_left = Inches(0.08); tf.margin_top = Inches(0.02)
        p = tf.paragraphs[0]
        run = p.add_run(); run.text = val
        run.font.name = "Calibri"; run.font.size = Pt(10)
        if r_i == 0:
            cell.fill.solid(); cell.fill.fore_color.rgb = ATEX_BLUE
            run.font.color.rgb = WHITE; run.font.bold = True; run.font.size = Pt(11)
        else:
            cell.fill.solid()
            cell.fill.fore_color.rgb = WHITE if r_i%2 else LIGHT_BG
            run.font.color.rgb = DARK
            if c_i == 4:
                run.font.bold = True
                if val == "UNSTABLE": run.font.color.rgb = AMBER
                elif val in ("SUCCESS","Active"): run.font.color.rgb = GREEN
                elif val == "Orchestrator": run.font.color.rgb = ATEX_ACCENT
add_footer(s, 4)

# ================================================================
# SLIDE 5 – How I manage the builds (workflow)
# ================================================================
s = prs.slides.add_slide(BLANK); add_bg(s)
title_slide_header(s, "How I Manage the Builds",
                   "End-to-end daily workflow across all pipelines")
steps = [
    ("Trigger",   "Scheduled + on-demand runs across trunk, 8.7.x, 8.6.x and Internal jobs"),
    ("Execute",   "Jenkins runs API (CASS), Web E2E and Integration suites in parallel"),
    ("Collect",   "Test results, JUnit XML and console logs pulled via Jenkins MCP"),
    ("Report",    "Auto-generated build-<id>.md report in reports/build-failures/{job}/"),
    ("Investigate","AI-generated root-cause analysis in investigations/copilot-findings/"),
    ("Distribute","Weekly summary dashboard + email notifications to stakeholders"),
]
y = Inches(2.0); box_w = Inches(2.05); box_h = Inches(2.6); gap = Inches(0.05)
startx = Inches(0.4)
for i,(h,body) in enumerate(steps):
    x = startx + i*(box_w+gap)
    card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, box_w, box_h)
    card.adjustments[0] = 0.06
    card.line.color.rgb = RGBColor(0xE1,0xE6,0xEF); card.line.width=Pt(0.75)
    card.fill.solid(); card.fill.fore_color.rgb = WHITE
    circ = s.shapes.add_shape(MSO_SHAPE.OVAL, x+box_w/2-Inches(0.35),
                              y+Inches(0.25), Inches(0.7), Inches(0.7))
    circ.line.fill.background(); circ.fill.solid(); circ.fill.fore_color.rgb = ATEX_BLUE
    add_text(s, x, y+Inches(0.35), box_w, Inches(0.5),
             str(i+1), size=20, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    add_text(s, x, y+Inches(1.05), box_w, Inches(0.4),
             h, size=13, bold=True, color=ATEX_BLUE, align=PP_ALIGN.CENTER)
    add_text(s, x+Inches(0.15), y+Inches(1.5), box_w-Inches(0.3), Inches(1.05),
             body, size=10.5, color=DARK, align=PP_ALIGN.CENTER)
    if i < len(steps)-1:
        ar = s.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW,
                                x+box_w-Inches(0.02), y+box_h/2-Inches(0.12),
                                Inches(0.14), Inches(0.24))
        ar.line.fill.background(); ar.fill.solid(); ar.fill.fore_color.rgb = ATEX_ACCENT
add_text(s, Inches(0.4), Inches(5.0), Inches(12.5), Inches(0.4),
         "Tools in the loop: Jenkins  \u2022  Jenkins MCP  \u2022  GitHub Copilot  \u2022  GitHub Actions  \u2022  Markdown dashboards",
         size=13, bold=True, color=GREY, align=PP_ALIGN.CENTER)

bullet_box(s, Inches(0.4), Inches(5.6), Inches(6.2), Inches(1.35),
           "Daily responsibilities",
           ["Monitor overnight & CI-triggered runs across ~25 pipelines",
            "Triage UNSTABLE / FAILURE builds and file findings",
            "Coordinate with dev teams on regressions and env issues"])
bullet_box(s, Inches(6.75), Inches(5.6), Inches(6.2), Inches(1.35),
           "Governance",
           ["One report per build \u2013 reproducible & auditable",
            "Zero manual copy-paste \u2014 data pulled directly from Jenkins",
            "History preserved: no build-file edits, only new files"])
add_footer(s, 5)

# ================================================================
# SLIDE 6 – AI-assisted build management
# ================================================================
s = prs.slides.add_slide(BLANK); add_bg(s)
title_slide_header(s, "AI-Assisted Build Management",
                   "Using GitHub Copilot + Jenkins MCP to scale the QA function")

bullet_box(s, Inches(0.4), Inches(1.7), Inches(6.2), Inches(5.1),
           "What the AI does for me",
           ["Reads Jenkins builds directly through the MCP server \u2013 no manual log copying",
            "Generates a standard build-<id>.md report per failed / unstable build",
            "Produces a root-cause investigation: Summary, Root Cause, Affected Components, Recommended Fix, Prevention",
            "Correlates failures to recent commits and dependency changes",
            "Redacts PII / secrets automatically before writing reports",
            "Runs weekly to publish an HTML + Markdown dashboard of build health",
            "Frees the QA engineer to focus on real defects, not paperwork"])

box = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(1.7),
                        Inches(6.0), Inches(5.1))
box.adjustments[0] = 0.03
box.line.color.rgb = RGBColor(0xE1,0xE6,0xEF); box.line.width=Pt(0.75)
box.fill.solid(); box.fill.fore_color.rgb = LIGHT_BG
add_text(s, Inches(6.9), Inches(1.85), Inches(6.0), Inches(0.5),
         "The Automation Loop", size=15, bold=True, color=ATEX_BLUE, align=PP_ALIGN.CENTER)

nodes = [
    ("Jenkins\nBuilds",       Inches(7.4),  Inches(2.7), ATEX_BLUE),
    ("Jenkins\nMCP Server",   Inches(9.4),  Inches(2.7), ATEX_ACCENT),
    ("Copilot\nAgent",        Inches(11.4), Inches(2.7), GREEN),
    ("Build\nReport (.md)",   Inches(7.4),  Inches(4.7), AMBER),
    ("Root-Cause\nAnalysis",  Inches(9.4),  Inches(4.7), AMBER),
    ("Weekly\nDashboard",     Inches(11.4), Inches(4.7), ATEX_BLUE),
]
for lbl,x,y,c in nodes:
    circ = s.shapes.add_shape(MSO_SHAPE.OVAL, x, y, Inches(1.3), Inches(1.3))
    circ.line.color.rgb = WHITE; circ.line.width = Pt(1.5)
    circ.fill.solid(); circ.fill.fore_color.rgb = c
    add_text(s, x, y+Inches(0.28), Inches(1.3), Inches(0.9),
             lbl, size=10, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
add_footer(s, 6)

# ================================================================
# SLIDE 7 – Live Metrics (KPI + chart)
# ================================================================
s = prs.slides.add_slide(BLANK); add_bg(s)
title_slide_header(s, "Live Metrics \u2014 Snapshot from Jenkins",
                   "Pulled through the Jenkins MCP integration")

kpi_card(s, Inches(0.4),  Inches(1.75), Inches(3.05), Inches(1.5), "25+", "Pipelines managed", ATEX_BLUE)
kpi_card(s, Inches(3.55), Inches(1.75), Inches(3.05), Inches(1.5), "400+", "B2A trunk builds run", ATEX_ACCENT)
kpi_card(s, Inches(6.70), Inches(1.75), Inches(3.05), Inches(1.5), "512",  "Internal demo builds", GREEN)
kpi_card(s, Inches(9.85), Inches(1.75), Inches(3.05), Inches(1.5), "259",  "AI-Pipeline runs (SUCCESS)", AMBER)

chart_data = CategoryChartData()
chart_data.categories = ["B2A-trunk\n#401", "B2C-8.7.x\n#97",
                         "Internal-trunk\n#187", "Internal-demo\n#512", "AI-Pipeline\n#259"]
chart_data.add_series("Passed",  (15, 12, 140, 380, 1))
chart_data.add_series("Failed",  ( 2,  2,  18,  22, 0))
chart_data.add_series("Skipped", ( 0,  1,   4,   6, 0))
gframe = s.shapes.add_chart(XL_CHART_TYPE.COLUMN_STACKED,
                            Inches(0.4), Inches(3.5), Inches(8.2), Inches(3.3),
                            chart_data)
chart = gframe.chart
chart.has_title = True
chart.chart_title.text_frame.text = "Recent build result mix (test counts)"
for p in chart.chart_title.text_frame.paragraphs:
    for r in p.runs:
        r.font.size = Pt(12); r.font.bold = True; r.font.color.rgb = ATEX_BLUE
chart.has_legend = True
chart.legend.position = XL_LEGEND_POSITION.BOTTOM
chart.legend.include_in_layout = False
colors = [GREEN, RED, AMBER]
for s_i, ser in enumerate(chart.series):
    ser.format.fill.solid(); ser.format.fill.fore_color.rgb = colors[s_i]

box = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.85), Inches(3.5),
                        Inches(4.05), Inches(3.3))
box.adjustments[0] = 0.04
box.line.color.rgb = RGBColor(0xE1,0xE6,0xEF); box.line.width=Pt(0.75)
box.fill.solid(); box.fill.fore_color.rgb = WHITE
add_text(s, Inches(9.05), Inches(3.65), Inches(3.8), Inches(0.5),
         "Latest build status", size=14, bold=True, color=ATEX_BLUE)
lines = [
    ("B2A-trunk #401",           "UNSTABLE", AMBER),
    ("B2C-trunk #125",           "UNSTABLE", AMBER),
    ("B2C-8.7.x #97",            "UNSTABLE", AMBER),
    ("Internal-trunk #187",      "UNSTABLE", AMBER),
    ("Internal-trunk-demo #512", "UNSTABLE", AMBER),
    ("AI-Pipeline #259",         "SUCCESS",  GREEN),
]
for i,(name,st,col) in enumerate(lines):
    y = Inches(4.2 + i*0.4)
    dot = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(9.05), y+Inches(0.08),
                             Inches(0.16), Inches(0.16))
    dot.line.fill.background(); dot.fill.solid(); dot.fill.fore_color.rgb = col
    add_text(s, Inches(9.3), y, Inches(2.4), Inches(0.35),
             name, size=11, color=DARK)
    add_text(s, Inches(11.5), y, Inches(1.35), Inches(0.35),
             st, size=11, bold=True, color=col, align=PP_ALIGN.RIGHT)
add_text(s, Inches(0.4), Inches(6.9), Inches(12.5), Inches(0.3),
         "Data source: Jenkins REST API via MCP  \u2022  Timestamps normalised to UTC  \u2022  Values illustrative from most recent runs",
         size=9, color=GREY, align=PP_ALIGN.CENTER)
add_footer(s, 7)

# ================================================================
# SLIDE 8 – Rialto Internal Integration deep-dive
# ================================================================
s = prs.slides.add_slide(BLANK); add_bg(s)
title_slide_header(s, "Rialto Internal Integration Testing",
                   "Cross-version compatibility & end-to-end integration coverage")

bullet_box(s, Inches(0.4), Inches(1.75), Inches(6.2), Inches(2.5),
           "Purpose",
           ["Validate end-to-end flows across Rialto B2A internal services",
            "Verify AgencyBackend, MediaHouse and CASS interactions",
            "Run mixed-version scenarios (e.g. AgencyBE 8.7 \u00D7 MediaHouse 8.6)",
            "Catch integration regressions before release branches diverge"])

bullet_box(s, Inches(6.75), Inches(1.75), Inches(6.2), Inches(2.5),
           "Pipelines involved",
           ["automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk",
            "automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-demo",
            "automationrunCAI-RIALTOB2A-IntegrationTesting-Internal-trunk-pipeline",
            "automationrunCAI-RIALTO-B2A-Internal-AgencyBE8.7-MH-8.6"])

bullet_box(s, Inches(0.4), Inches(4.4), Inches(6.2), Inches(2.5),
           "Recent activity",
           ["Internal-trunk latest: build #187 \u2014 UNSTABLE (~94 min run)",
            "Internal-trunk-demo latest: build #512 \u2014 UNSTABLE (~3 min)",
            "Reports auto-generated under reports/build-failures/",
            "Investigations logged one-file-per-build in copilot-findings/"])

bullet_box(s, Inches(6.75), Inches(4.4), Inches(6.2), Inches(2.5),
           "Why it matters",
           ["Prevents late-stage integration surprises before release",
            "Guarantees Rialto self-service, order-flow & pricing stay consistent",
            "Provides the release manager a single view of cross-branch health",
            "Backed by a machine-readable trail (Markdown + JUnit)"],
           heading_color=GREEN)
add_footer(s, 8)

# ================================================================
# SLIDE 9 – Benefits
# ================================================================
s = prs.slides.add_slide(BLANK); add_bg(s)
title_slide_header(s, "Benefits Delivered",
                   "Business & engineering value from this way of working")
benefits = [
    ("\u26A1", "Faster feedback", "Failures triaged the same day they occur \u2014 no more waiting for the next standup",  ATEX_BLUE),
    ("\U0001F3AF", "Consistent reporting", "One standard Markdown format across every job and every build",              ATEX_ACCENT),
    ("\U0001F916", "AI leverage",    "Copilot reads Jenkins directly and drafts the RCA \u2014 engineer just validates",       GREEN),
    ("\U0001F4C8", "Trend visibility","Weekly dashboards expose flaky tests and regressions over time",                   AMBER),
    ("\U0001F512", "Audit & compliance","Every build has an immutable report file \u2014 full history in Git",                 DARK),
    ("\U0001F4B8", "Cost avoidance", "Fewer escaped defects \u2192 less rework, fewer hot-fixes on 8.7.x / 8.6.x",             RED),
]
cw = Inches(4.15); ch = Inches(2.3); gap = Inches(0.1)
sx = Inches(0.4); sy = Inches(1.7)
for i,(ico,h,body,c) in enumerate(benefits):
    col = i % 3; row = i // 3
    x = sx + col*(cw+gap); y = sy + row*(ch+Inches(0.15))
    card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, ch)
    card.adjustments[0] = 0.05
    card.line.color.rgb = RGBColor(0xE1,0xE6,0xEF); card.line.width=Pt(0.75)
    card.fill.solid(); card.fill.fore_color.rgb = WHITE
    strip = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, Inches(0.15), ch)
    strip.line.fill.background(); strip.fill.solid(); strip.fill.fore_color.rgb = c
    add_text(s, x+Inches(0.4), y+Inches(0.25), Inches(0.9), Inches(0.7),
             ico, size=28, color=c)
    add_text(s, x+Inches(1.3), y+Inches(0.3), cw-Inches(1.4), Inches(0.5),
             h, size=16, bold=True, color=ATEX_BLUE)
    add_text(s, x+Inches(1.3), y+Inches(0.85), cw-Inches(1.4), ch-Inches(1.0),
             body, size=11.5, color=DARK)
add_footer(s, 9)

# ================================================================
# SLIDE 10 – Roadmap
# ================================================================
s = prs.slides.add_slide(BLANK); add_bg(s)
title_slide_header(s, "Roadmap & Next Steps",
                   "Where I want to take automation build management next")
phases = [
    ("Now",       "Stabilise & scale",
     ["Bring flaky B2A / B2C API tests below 2% flake rate",
      "Extend AI investigations to Web E2E pipelines",
      "Onboard remaining 8.6.x jobs into the same reporting flow"], ATEX_BLUE),
    ("Next",      "Insights & prevention",
     ["Trend-based dashboards (heat-maps of failing suites)",
      "Automatic linking of failures to suspect commits",
      "Slack/email alerts for two consecutive UNSTABLE builds"], ATEX_ACCENT),
    ("Future",    "Self-healing automation",
     ["AI-suggested fixes committed as draft PRs to test repos",
      "Predictive test selection for faster feedback loops",
      "Full-stack integration health score per release branch"], GREEN),
]
cw = Inches(4.15); ch = Inches(4.5); gap = Inches(0.1); sx = Inches(0.4); sy = Inches(1.8)
for i,(ph, hdr, items, c) in enumerate(phases):
    x = sx + i*(cw+gap)
    card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, sy, cw, ch)
    card.adjustments[0] = 0.04
    card.line.color.rgb = RGBColor(0xE1,0xE6,0xEF); card.line.width=Pt(0.75)
    card.fill.solid(); card.fill.fore_color.rgb = WHITE
    header = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, sy, cw, Inches(0.75))
    header.line.fill.background(); header.fill.solid(); header.fill.fore_color.rgb = c
    add_text(s, x, sy+Inches(0.12), cw, Inches(0.35),
             ph, size=13, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    add_text(s, x, sy+Inches(0.42), cw, Inches(0.35),
             hdr, size=11, color=WHITE, align=PP_ALIGN.CENTER)
    tb = s.shapes.add_textbox(x+Inches(0.25), sy+Inches(1.0),
                              cw-Inches(0.5), ch-Inches(1.1))
    tf = tb.text_frame; tf.word_wrap = True
    for j, it in enumerate(items):
        p = tf.paragraphs[0] if j == 0 else tf.add_paragraph()
        p.space_after = Pt(6)
        r = p.add_run(); r.text = "\u25B8  " + it
        r.font.size = Pt(12); r.font.color.rgb = DARK; r.font.name = "Calibri"
add_footer(s, 10)

# ================================================================
# SLIDE 11 – Thank you
# ================================================================
s = prs.slides.add_slide(BLANK); add_bg(s, ATEX_BLUE)
strip = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(3.15), SW, Inches(0.08))
strip.line.fill.background(); strip.fill.solid(); strip.fill.fore_color.rgb = ATEX_ACCENT
add_text(s, Inches(0.7), Inches(2.2), Inches(12), Inches(0.7),
         "Thank you", size=54, bold=True, color=WHITE)
add_text(s, Inches(0.7), Inches(3.35), Inches(12), Inches(0.6),
         "Questions & discussion", size=22, color=ATEX_ACCENT, bold=True)
add_text(s, Inches(0.7), Inches(4.3), Inches(12), Inches(0.5),
         "Managing 25+ Jenkins pipelines across Rialto trunk, 8.7.x, 8.6.x and Internal Integration",
         size=15, color=WHITE)
add_text(s, Inches(0.7), Inches(4.85), Inches(12), Inches(0.5),
         "Powered by Jenkins MCP  +  GitHub Copilot  +  automated Markdown reporting",
         size=15, color=WHITE)
add_text(s, Inches(0.7), Inches(6.7), Inches(12), Inches(0.4),
         f"QA Automation  |  Atex Rialto  |  {datetime.now(timezone.utc).strftime('%d %b %Y')}",
         size=11, color=RGBColor(0xC7,0xD4,0xE6))

out = os.path.join(os.path.dirname(__file__), "Managing_Automation_Builds_QA_Rialto.pptx")
prs.save(out)
print(f"Saved: {out}  slides={len(prs.slides)}")
