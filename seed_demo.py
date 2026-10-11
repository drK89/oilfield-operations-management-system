from pathlib import Path
from oilfield_ops import OperationsService
DB=Path(__file__).resolve().parent/"data"/"operations.sqlite"
def main():
    s=OperationsService(DB)
    for args in [("A-101","Alpha Production Well","well","available","Central North Sea"),("V-201","Intervention Vessel","vessel","available","Aberdeen"),("EQ-301","Wireline Unit","equipment","available","Aberdeen")]:
        try:s.add_asset(*args)
        except Exception:pass
    for args in [("T-WL","Wireline Team","well intervention"),("T-ME","Mechanical Team","maintenance")]:
        try:s.add_team(*args)
        except Exception:pass
    if not s.rows("work_orders"): s.create_work_order("A-101","T-WL","Investigate production decline","high","2026-10-12T08:00","2026-10-12T18:00")
    print(s.dashboard())
if __name__=="__main__":main()
