"""
presentation_builder.py
Core builder and styling utilities for the Lane Change Monitoring presentation suite.
Provides consistent academic themes, slide dimensions, headers, footers, tables, and cards.
"""

import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# 16:9 Widescreen dimensions
SLIDE_WIDTH = Inches(13.333)
SLIDE_HEIGHT = Inches(7.5)

# Academic Color Palette
COLOR_NAVY_DARK = RGBColor(10, 25, 47)      # #0A192F Deep Navy Primary
COLOR_NAVY_MED = RGBColor(23, 42, 69)       # #172A45 Medium Navy
COLOR_NAVY_LIGHT = RGBColor(35, 53, 84)     # #233554 Slate Navy
COLOR_ACCENT_BLUE = RGBColor(2, 132, 199)   # #0284C7 Modern Tech Cyan/Blue
COLOR_ACCENT_LIGHT = RGBColor(224, 242, 254)# #E0F2FE Light Cyan Tint
COLOR_BG_LIGHT = RGBColor(248, 250, 252)    # #F8FAFC Clean Canvas Light Gray
COLOR_CARD_BG = RGBColor(255, 255, 255)     # White Card Background
COLOR_CARD_BORDER = RGBColor(203, 213, 225) # Slate 300 Border
COLOR_TEXT_DARK = RGBColor(30, 41, 59)      # Slate 800 Body Text
COLOR_TEXT_MUTED = RGBColor(100, 116, 139)  # Slate 500 Secondary
COLOR_WHITE = RGBColor(255, 255, 255)       # White
COLOR_ROW_ALT = RGBColor(241, 245, 249)     # Slate 100 Alternate Table Row

# Semantic status colors
COLOR_SUCCESS = RGBColor(22, 163, 74)       # Green 600
COLOR_WARNING = RGBColor(217, 119, 6)       # Amber 600
COLOR_DANGER = RGBColor(220, 38, 38)        # Red 600
COLOR_INFO = RGBColor(2, 132, 199)          # Blue 600


class PresentationBuilder:
    def __init__(self, title_prefix="Lane Change Monitoring"):
        self.prs = pptx.Presentation()
        self.prs.slide_width = SLIDE_WIDTH
        self.prs.slide_height = SLIDE_HEIGHT
        self.blank_layout = self.prs.slide_layouts[6]
        self.title_prefix = title_prefix

    def create_slide(self):
        """Creates a blank slide with light slate canvas background."""
        slide = self.prs.slides.add_slide(self.blank_layout)
        bg = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE, 0, 0, SLIDE_WIDTH, SLIDE_HEIGHT
        )
        bg.fill.solid()
        bg.fill.fore_color.rgb = COLOR_BG_LIGHT
        bg.line.fill.background()
        return slide

    def add_title_slide(self, title, subtitle, milestone_badge, student_name="Hardhik A", 
                        roll_no="CH.SC.U4CSE23114", course_code="24CSE473", 
                        course_name="Neural Networks and Deep Learning", 
                        dept_name="Department of Computer Science & Engineering, Amrita Vishwa Vidyapeetham"):
        """Generates a high-impact, academic title slide with deep navy theme."""
        slide = self.prs.slides.add_slide(self.blank_layout)
        
        # Deep Navy background
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SLIDE_WIDTH, SLIDE_HEIGHT)
        bg.fill.solid()
        bg.fill.fore_color.rgb = COLOR_NAVY_DARK
        bg.line.fill.background()

        # Accent decorative bar
        bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.0), Inches(0.15), Inches(4.5))
        bar.fill.solid()
        bar.fill.fore_color.rgb = COLOR_ACCENT_BLUE
        bar.line.fill.background()

        # Course & Milestone pill badge
        badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.2), Inches(1.0), Inches(5.8), Inches(0.45))
        badge.fill.solid()
        badge.fill.fore_color.rgb = COLOR_NAVY_LIGHT
        badge.line.color.rgb = COLOR_ACCENT_BLUE
        badge.line.width = Pt(1)
        tf_b = badge.text_frame
        tf_b.word_wrap = True
        tf_b.vertical_anchor = MSO_ANCHOR.MIDDLE
        p_b = tf_b.paragraphs[0]
        p_b.text = f"COURSE: {course_code} - {course_name.upper()} | {milestone_badge.upper()}"
        p_b.font.size = Pt(10.5)
        p_b.font.bold = True
        p_b.font.color.rgb = COLOR_ACCENT_LIGHT

        # Main Title Box
        tb_title = slide.shapes.add_textbox(Inches(1.2), Inches(1.65), Inches(11.0), Inches(1.6))
        tf_title = tb_title.text_frame
        tf_title.word_wrap = True
        p_title = tf_title.paragraphs[0]
        p_title.text = title
        p_title.font.name = "Calibri"
        p_title.font.size = Pt(32)
        p_title.font.bold = True
        p_title.font.color.rgb = COLOR_WHITE

        # Subtitle Box
        tb_sub = slide.shapes.add_textbox(Inches(1.2), Inches(3.2), Inches(11.0), Inches(0.9))
        tf_sub = tb_sub.text_frame
        tf_sub.word_wrap = True
        p_sub = tf_sub.paragraphs[0]
        p_sub.text = subtitle
        p_sub.font.name = "Calibri"
        p_sub.font.size = Pt(16)
        p_sub.font.color.rgb = RGBColor(148, 163, 184) # Light Slate

        # Author Credential Card
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.2), Inches(4.3), Inches(10.8), Inches(1.5))
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_NAVY_MED
        card.line.color.rgb = COLOR_NAVY_LIGHT
        card.line.width = Pt(1)
        tf_c = card.text_frame
        tf_c.word_wrap = True
        tf_c.vertical_anchor = MSO_ANCHOR.MIDDLE

        p1 = tf_c.paragraphs[0]
        p1.text = f"Candidate: {student_name}  |  Roll Number: {roll_no}"
        p1.font.name = "Calibri"
        p1.font.size = Pt(15)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_WHITE

        p2 = tf_c.add_paragraph()
        p2.text = f"{dept_name}"
        p2.font.name = "Calibri"
        p2.font.size = Pt(12)
        p2.font.color.rgb = COLOR_ACCENT_LIGHT

        p3 = tf_c.add_paragraph()
        p3.text = "Evaluation Domain: Vision Pilot Hybrid End-to-End AI & Deep Spatio-Temporal ADAS"
        p3.font.name = "Calibri"
        p3.font.size = Pt(11)
        p3.font.color.rgb = RGBColor(148, 163, 184)

        # Footer Date/Institution
        tb_f = slide.shapes.add_textbox(Inches(1.2), Inches(6.5), Inches(10.8), Inches(0.4))
        tf_f = tb_f.text_frame
        p_f = tf_f.paragraphs[0]
        p_f.text = "Amrita Vishwa Vidyapeetham — Academic Project Presentation"
        p_f.font.size = Pt(10)
        p_f.font.color.rgb = RGBColor(100, 116, 139)

        return slide

    def add_header(self, slide, title_text, category_text, milestone_label):
        """Adds a standard academic header banner across the top."""
        # Top banner shape
        banner = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SLIDE_WIDTH, Inches(1.05))
        banner.fill.solid()
        banner.fill.fore_color.rgb = COLOR_NAVY_DARK
        banner.line.fill.background()

        # Accent bottom stripe
        stripe = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(1.02), SLIDE_WIDTH, Inches(0.04))
        stripe.fill.solid()
        stripe.fill.fore_color.rgb = COLOR_ACCENT_BLUE
        stripe.line.fill.background()

        # Text container
        tb = slide.shapes.add_textbox(Inches(0.6), Inches(0.1), Inches(9.5), Inches(0.85))
        tf = tb.text_frame
        tf.word_wrap = True
        
        # Category / Module small label
        p_cat = tf.paragraphs[0]
        p_cat.text = f"24CSE473 — NEURAL NETWORKS & DEEP LEARNING  |  {category_text.upper()}"
        p_cat.font.name = "Calibri"
        p_cat.font.size = Pt(9.5)
        p_cat.font.bold = True
        p_cat.font.color.rgb = COLOR_ACCENT_LIGHT

        # Slide Main Title
        p_title = tf.add_paragraph()
        p_title.text = title_text
        p_title.font.name = "Calibri"
        p_title.font.size = Pt(20)
        p_title.font.bold = True
        p_title.font.color.rgb = COLOR_WHITE

        # Milestone Badge on the right
        badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(10.3), Inches(0.28), Inches(2.4), Inches(0.45))
        badge.fill.solid()
        badge.fill.fore_color.rgb = COLOR_NAVY_MED
        badge.line.color.rgb = COLOR_ACCENT_BLUE
        badge.line.width = Pt(1)
        tf_b = badge.text_frame
        tf_b.word_wrap = False
        tf_b.vertical_anchor = MSO_ANCHOR.MIDDLE
        p_b = tf_b.paragraphs[0]
        p_b.text = milestone_label
        p_b.alignment = PP_ALIGN.CENTER
        p_b.font.name = "Calibri"
        p_b.font.size = Pt(10)
        p_b.font.bold = True
        p_b.font.color.rgb = COLOR_WHITE

    def add_footer(self, slide, current_slide, total_slides, milestone_label="Milestone Review"):
        """Adds standard bottom footer with student info, course, and page number."""
        # Top line divider
        divider = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.6), Inches(7.05), Inches(12.133), Inches(0.015))
        divider.fill.solid()
        divider.fill.fore_color.rgb = COLOR_CARD_BORDER
        divider.line.fill.background()

        # Left Info
        tb_left = slide.shapes.add_textbox(Inches(0.6), Inches(7.08), Inches(6.0), Inches(0.35))
        tf_left = tb_left.text_frame
        p_left = tf_left.paragraphs[0]
        p_left.text = "Hardhik A (CH.SC.U4CSE23114)  •  Monitoring Lane Changes in Autonomous Vehicles"
        p_left.font.name = "Calibri"
        p_left.font.size = Pt(9)
        p_left.font.color.rgb = COLOR_TEXT_MUTED

        # Center Milestone
        tb_mid = slide.shapes.add_textbox(Inches(6.8), Inches(7.08), Inches(3.5), Inches(0.35))
        tf_mid = tb_mid.text_frame
        p_mid = tf_mid.paragraphs[0]
        p_mid.text = f"24CSE473 Deep Learning  |  {milestone_label}"
        p_mid.font.name = "Calibri"
        p_mid.font.size = Pt(9)
        p_mid.font.color.rgb = COLOR_TEXT_MUTED

        # Right Slide Number
        tb_right = slide.shapes.add_textbox(Inches(10.8), Inches(7.08), Inches(1.9), Inches(0.35))
        tf_right = tb_right.text_frame
        p_right = tf_right.paragraphs[0]
        p_right.alignment = PP_ALIGN.RIGHT
        p_right.text = f"Slide {current_slide} of {total_slides}"
        p_right.font.name = "Calibri"
        p_right.font.size = Pt(9.5)
        p_right.font.bold = True
        p_right.font.color.rgb = COLOR_NAVY_DARK

    def add_card(self, slide, left, top, width, height, title, items, 
                 accent_color=COLOR_ACCENT_BLUE, card_bg=COLOR_CARD_BG, border_color=COLOR_CARD_BORDER):
        """Adds a clean academic card container with title and bullet points."""
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = card_bg
        card.line.color.rgb = border_color
        card.line.width = Pt(1)

        # Header accent bar inside card
        if accent_color:
            bar = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left + Inches(0.12), top + Inches(0.12), Inches(0.06), Inches(0.3))
            bar.fill.solid()
            bar.fill.fore_color.rgb = accent_color
            bar.line.fill.background()

        # Text Frame
        tb = slide.shapes.add_textbox(left + Inches(0.25), top + Inches(0.08), width - Inches(0.4), height - Inches(0.16))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.02)
        tf.margin_right = Inches(0.02)
        tf.margin_top = Inches(0.05)
        tf.margin_bottom = Inches(0.05)

        # Card Title
        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.name = "Calibri"
        p_t.font.size = Pt(13)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_NAVY_DARK

        # Card Items
        for item in items:
            p = tf.add_paragraph()
            p.space_after = Pt(4)
            p.space_before = Pt(2)
            
            # Format "Bold Key: Description" if separator present
            if ":" in item and not item.startswith("http"):
                key, val = item.split(":", 1)
                r_key = p.add_run()
                r_key.text = "• " + key.strip() + ": "
                r_key.font.name = "Calibri"
                r_key.font.size = Pt(10)
                r_key.font.bold = True
                r_key.font.color.rgb = COLOR_NAVY_MED

                r_val = p.add_run()
                r_val.text = val.strip()
                r_val.font.name = "Calibri"
                r_val.font.size = Pt(9.5)
                r_val.font.color.rgb = COLOR_TEXT_DARK
            else:
                p.text = "• " + item
                p.font.name = "Calibri"
                p.font.size = Pt(9.5)
                p.font.color.rgb = COLOR_TEXT_DARK

        return card

    def add_table(self, slide, left, top, width, height, headers, rows, col_widths=None, font_size=Pt(9)):
        """Creates a professional, clean academic table with navy header and alternating rows."""
        num_rows = len(rows) + 1
        num_cols = len(headers)

        table_shape = slide.shapes.add_table(num_rows, num_cols, left, top, width, height)
        table = table_shape.table

        # Set column widths if provided
        if col_widths and len(col_widths) == num_cols:
            for idx, w in enumerate(col_widths):
                table.columns[idx].width = w

        # Format Headers
        for col_idx, header_text in enumerate(headers):
            cell = table.cell(0, col_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = COLOR_NAVY_DARK
            cell.margin_left = Inches(0.08)
            cell.margin_right = Inches(0.08)
            cell.margin_top = Inches(0.05)
            cell.margin_bottom = Inches(0.05)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            
            p = cell.text_frame.paragraphs[0]
            p.text = header_text
            p.alignment = PP_ALIGN.CENTER if col_idx == 0 else PP_ALIGN.LEFT
            p.font.name = "Calibri"
            p.font.size = Pt(9.5)
            p.font.bold = True
            p.font.color.rgb = COLOR_WHITE

        # Format Data Rows
        for row_idx, row_data in enumerate(rows):
            actual_row = row_idx + 1
            bg_color = COLOR_ROW_ALT if (row_idx % 2 == 1) else COLOR_CARD_BG

            for col_idx, cell_value in enumerate(row_data):
                cell = table.cell(actual_row, col_idx)
                cell.fill.solid()
                cell.fill.fore_color.rgb = bg_color
                cell.margin_left = Inches(0.08)
                cell.margin_right = Inches(0.08)
                cell.margin_top = Inches(0.04)
                cell.margin_bottom = Inches(0.04)
                cell.vertical_anchor = MSO_ANCHOR.MIDDLE

                p = cell.text_frame.paragraphs[0]
                p.text = str(cell_value)
                p.alignment = PP_ALIGN.CENTER if col_idx == 0 else PP_ALIGN.LEFT
                p.font.name = "Calibri"
                p.font.size = font_size
                p.font.color.rgb = COLOR_TEXT_DARK

        return table_shape

    def add_process_steps(self, slide, left, top, total_width, height, steps):
        """Creates a horizontal step-by-step pipeline process flow."""
        n = len(steps)
        step_width = (total_width - Inches(0.15) * (n - 1)) / n

        for i, step in enumerate(steps):
            x = left + i * (step_width + Inches(0.15))
            
            # Step Box
            box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, top, step_width, height)
            box.fill.solid()
            box.fill.fore_color.rgb = COLOR_CARD_BG
            box.line.color.rgb = COLOR_ACCENT_BLUE if i == n-1 else COLOR_CARD_BORDER
            box.line.width = Pt(1.5) if i == n-1 else Pt(1)

            # Step number badge
            badge = slide.shapes.add_shape(MSO_SHAPE.OVAL, x + Inches(0.1), top + Inches(0.12), Inches(0.35), Inches(0.35))
            badge.fill.solid()
            badge.fill.fore_color.rgb = COLOR_ACCENT_BLUE
            badge.line.fill.background()
            tf_bd = badge.text_frame
            tf_bd.vertical_anchor = MSO_ANCHOR.MIDDLE
            p_bd = tf_bd.paragraphs[0]
            p_bd.alignment = PP_ALIGN.CENTER
            p_bd.text = str(i + 1)
            p_bd.font.name = "Calibri"
            p_bd.font.size = Pt(11)
            p_bd.font.bold = True
            p_bd.font.color.rgb = COLOR_WHITE

            # Step content
            tb = slide.shapes.add_textbox(x + Inches(0.1), top + Inches(0.52), step_width - Inches(0.2), height - Inches(0.6))
            tf = tb.text_frame
            tf.word_wrap = True
            tf.margin_left = Inches(0.02)
            tf.margin_right = Inches(0.02)
            tf.margin_top = Inches(0.02)

            p_title = tf.paragraphs[0]
            p_title.text = step.get("title", "")
            p_title.font.name = "Calibri"
            p_title.font.size = Pt(11)
            p_title.font.bold = True
            p_title.font.color.rgb = COLOR_NAVY_DARK

            desc = step.get("desc", "")
            p_desc = tf.add_paragraph()
            p_desc.text = desc
            p_desc.font.name = "Calibri"
            p_desc.font.size = Pt(8.5)
            p_desc.font.color.rgb = COLOR_TEXT_MUTED

    def add_metric_kpi(self, slide, left, top, width, height, number_str, label_str, subtext_str="", status="info"):
        """Creates an executive KPI metric box."""
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_BG
        card.line.color.rgb = COLOR_CARD_BORDER
        card.line.width = Pt(1)

        # Color mapping
        num_color = COLOR_ACCENT_BLUE
        if status == "success":
            num_color = COLOR_SUCCESS
        elif status == "danger":
            num_color = COLOR_DANGER
        elif status == "warning":
            num_color = COLOR_WARNING

        tb = slide.shapes.add_textbox(left + Inches(0.1), top + Inches(0.1), width - Inches(0.2), height - Inches(0.2))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.02)
        tf.margin_right = Inches(0.02)
        tf.margin_top = Inches(0.02)

        p_num = tf.paragraphs[0]
        p_num.text = number_str
        p_num.font.name = "Calibri"
        p_num.font.size = Pt(26)
        p_num.font.bold = True
        p_num.font.color.rgb = num_color

        p_lbl = tf.add_paragraph()
        p_lbl.text = label_str
        p_lbl.font.name = "Calibri"
        p_lbl.font.size = Pt(10.5)
        p_lbl.font.bold = True
        p_lbl.font.color.rgb = COLOR_NAVY_DARK

        if subtext_str:
            p_sub = tf.add_paragraph()
            p_sub.text = subtext_str
            p_sub.font.name = "Calibri"
            p_sub.font.size = Pt(8.5)
            p_sub.font.color.rgb = COLOR_TEXT_MUTED

    def save(self, output_path):
        """Saves the presentation."""
        self.prs.save(output_path)
        print(f"[OK] Presentation saved successfully to: {output_path}")
