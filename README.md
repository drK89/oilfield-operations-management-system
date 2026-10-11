# Oilfield Operations Management System

A database-backed Python application for managing oilfield assets, specialist teams, work orders and operational allocations.

## Portfolio highlights

- object-oriented service layer and normalised SQLite schema;
- asset/team CRUD foundation and foreign-key integrity;
- overlap detection for shared asset and team allocations;
- controlled work-order lifecycle with invalid-transition protection;
- immutable event-style audit log;
- operational KPI dashboard and REST API with OpenAPI documentation;
- automated tests, Docker and continuous integration.

The bundled records are synthetic. Authentication and enterprise permission management are intentionally outside this public demonstration and would be required before operational deployment.

## Quick start

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pip install -e .
python seed_demo.py
streamlit run dashboard.py
uvicorn oilfield_ops.api:app --reload
python -m unittest discover -s tests -v
```

API documentation appears at `http://127.0.0.1:8000/docs`.

## Author

**Dr Khaldoun Shaker**  
Petroleum & Reservoir Engineer | Energy Data Analytics  
Edinburgh, United Kingdom · [GitHub](https://github.com/drK89)

## Licence

Copyright (c) 2026 Khaldoun Shaker. All rights reserved. See [LICENSE](LICENSE).
