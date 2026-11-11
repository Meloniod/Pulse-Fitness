from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter
from openpyxl.formatting.rule import FormulaRule

OUT = Path(__file__).resolve().parents[1] / "tracker" / "PULSE_Personal_Trainer_Tracker.xlsx"
NAVY, LIME, PALE, WHITE = "111D27", "C7F36B", "F0F5E7", "FFFFFF"

wb = Workbook()
start = wb.active
start.title = "START HERE"
sheets = {
    "START HERE": [
        ["PULSE PERSONAL TRAINER TRACKER"], ["Purpose", "Companion workbook for independent personal trainers."],
        ["How to use", "Read USER GUIDE, then complete the client, programme, session, nutrition and payment tabs."],
        ["Google Sheets", "Upload this XLSX to Google Drive and open with Google Sheets. Check formulas and dropdowns after import."],
        ["Privacy", "Use fictional data for demos. Protect real client records and collect only necessary information."],
        ["Scope", "Nutrition is client-reported logging, not dietary or medical advice. Payment tab tracks status; it does not process payments."]
    ],
    "USER GUIDE": [
        ["AREA", "INSTRUCTIONS"], ["CLIENT REGISTER", "Add one row per client. Update status when the relationship changes."],
        ["EXERCISE LIBRARY", "Maintain a reusable list of exercises and coaching notes."],
        ["PROGRAMME PLANNER", "Plan exercises by client, week and training day."],
        ["SESSION LOG", "Record the date, time, delivery mode and completion status for every session."],
        ["PROGRESS TRACKER", "Only record agreed metrics after confirming consent and purpose."],
        ["NUTRITION LOG", "Enter client-reported meals, calories, protein and water."],
        ["PAYMENT REGISTER", "Record amount, date and manual payment status. Never store card details."]
    ],
    "DASHBOARD": [
        ["PULSE DASHBOARD", "VALUE"], ["Total clients", "=COUNTA('CLIENT REGISTER'!A2:A500)"],
        ["Active clients", '=COUNTIF(\'CLIENT REGISTER\'!H2:H500,"Active")'],
        ["Sessions logged", "=COUNTA('SESSION LOG'!A2:A500)"],
        ["Completed sessions", '=COUNTIF(\'SESSION LOG\'!H2:H500,"Completed")'],
        ["Revenue received (ZAR)", '=SUMIF(\'PAYMENT REGISTER\'!F2:F500,"Paid",\'PAYMENT REGISTER\'!E2:E500)'],
        ["Outstanding (ZAR)", '=SUMIF(\'PAYMENT REGISTER\'!F2:F500,"<>Paid",\'PAYMENT REGISTER\'!E2:E500)'],
        ["Nutrition entries", "=COUNTA('NUTRITION LOG'!A2:A500)"]
    ],
    "CLIENT REGISTER": [["Client ID","Full Name","Email","Phone","Start Date","Goal","Delivery Mode","Status","Notes"],["C-001","Sample Client","sample@example.com","","2026-11-01","Strength","Hybrid","Active","Fictional sample only"]],
    "EXERCISE LIBRARY": [["Exercise ID","Exercise Name","Movement Pattern","Equipment","Level","Coaching Notes"],["EX-001","Bodyweight Squat","Squat","None","Beginner","Adapt to ability and coach safe technique"]],
    "PROGRAMME PLANNER": [["Programme ID","Programme Name","Client","Goal","Week","Day","Exercise","Sets","Reps","Rest Seconds","Notes"],["P-001","Strength Foundation","Sample Client","Strength",1,1,"Squat",3,8,90,"Adapt to client capability"]],
    "SESSION LOG": [["Session ID","Date","Time","Client","Delivery Mode","Session Type","Duration Minutes","Status","Notes"],["S-001","2026-11-11","09:00","Sample Client","In-person","Strength",60,"Scheduled","Fictional sample only"]],
    "PROGRESS TRACKER": [["Record ID","Date","Client","Metric","Value","Unit","Consent Confirmed","Notes"],["PR-001","2026-11-11","Sample Client","Performance note","","text","Yes","Only record necessary agreed information"]],
    "NUTRITION LOG": [["Entry ID","Date","Client","Meal","Calories","Protein Grams","Water Millilitres","Client Reported","Notes"],["N-001","2026-11-11","Sample Client","Breakfast",420,28,500,"Yes","Fictional sample only"]],
    "PAYMENT REGISTER": [["Payment ID","Date","Client","Description","Amount ZAR","Status","Reference","Notes"],["PAY-001","2026-11-01","Sample Client","Monthly coaching",1500,"Pending","","Fictional sample only"]],
    "SETTINGS": [["CLIENT STATUS","DELIVERY MODE","SESSION STATUS","PAYMENT STATUS","YES / NO"],["Lead","In-person","Scheduled","Pending","Yes"],["Active","Online","Completed","Paid","No"],["On hold","Hybrid","Cancelled","Overdue",""] ,["Archived","","","",""]]
}
for name, rows in sheets.items():
    ws = start if name == "START HERE" else wb.create_sheet(name)
    for row in rows:
        ws.append(row)
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = ws.dimensions if name not in ("START HERE","USER GUIDE","DASHBOARD","SETTINGS") else "A1:B1"
    for cell in ws[1]:
        cell.fill = PatternFill("solid", fgColor=NAVY)
        cell.font = Font(color=WHITE, bold=True)
        cell.alignment = Alignment(vertical="center")
    for col in ws.columns:
        letter = get_column_letter(col[0].column)
        max_len = max((len(str(c.value or "")) for c in col), default=10)
        ws.column_dimensions[letter].width = min(max(max_len + 3, 14), 42)
    ws.sheet_view.showGridLines = False
    for row in ws.iter_rows(min_row=2):
        for cell in row:
            if cell.row % 2 == 0:
                cell.fill = PatternFill("solid", fgColor="F7F9F7")
            cell.alignment = Alignment(vertical="top", wrap_text=True)
    ws.row_dimensions[1].height = 26

# Data validation lists refer to SETTINGS values.
validations = {
    "CLIENT REGISTER": [("H2:H500", "'SETTINGS'!$A$2:$A$5"), ("G2:G500", "'SETTINGS'!$B$2:$B$4")],
    "SESSION LOG": [("H2:H500", "'SETTINGS'!$C$2:$C$4"), ("E2:E500", "'SETTINGS'!$B$2:$B$4")],
    "PAYMENT REGISTER": [("F2:F500", "'SETTINGS'!$D$2:$D$4")],
    "PROGRESS TRACKER": [("G2:G500", "'SETTINGS'!$E$2:$E$3")],
    "NUTRITION LOG": [("H2:H500", "'SETTINGS'!$E$2:$E$3")]
}
for sheet, rules in validations.items():
    ws = wb[sheet]
    for target, formula in rules:
        dv = DataValidation(type="list", formula1=f"={formula}", allow_blank=True)
        ws.add_data_validation(dv)
        dv.add(target)

wb.calculation.fullCalcOnLoad = True
wb.calculation.forceFullCalc = True
OUT.parent.mkdir(parents=True, exist_ok=True)
wb.save(OUT)
print(f"Created {OUT}")
