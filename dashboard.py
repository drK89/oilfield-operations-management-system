from pathlib import Path
import pandas as pd,streamlit as st
from oilfield_ops import OperationsService,ConflictError
s=OperationsService(Path("data/operations.sqlite")); st.set_page_config(page_title="Oilfield Operations",layout="wide"); st.title("Oilfield Operations Management System"); m=s.dashboard(); cols=st.columns(4)
for col,(k,v) in zip(cols,m.items()): col.metric(k.replace("_"," ").title(),v)
tab1,tab2,tab3=st.tabs(["Work orders","Allocations","Audit trail"])
with tab1: st.dataframe(pd.DataFrame(s.rows("work_orders")),use_container_width=True)
with tab2: st.dataframe(pd.DataFrame(s.rows("allocations")),use_container_width=True)
with tab3: st.dataframe(pd.DataFrame(s.rows("audit_log")),use_container_width=True)
