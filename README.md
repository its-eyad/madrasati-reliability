# madrasati-reliability
Reliability strategy for Madrasati education platform using AMIR framework (Report + Prototype + Checklist).
# Madrasati Reliability Strategy (AMIR Framework)

This repository contains the reliability design and prototype for the **Madrasati Education Platform** based on the AMIR framework.

## 📄 Report
See [report.pdf](./report.pdf) for the full assignment:
- Phase 1 (Understand) – Current state analysis & fault identification
- Phase 2 (Practice) – Architecture, code prototype, fault trees
- Phase 3 (Master) – Testing strategy, metrics, validation plan
- Phase 4 (Envision) – Vision 2030 alignment, scalability, ethics

## 💻 Prototype
A simple Python simulation that demonstrates **exam submission fallback**:
- If the exam server is up → answers are submitted normally
- If the server is down → answers are saved locally and synced later

### Run it:
```bash
python exam_sim.py
