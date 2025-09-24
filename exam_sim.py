---

## 2️⃣ exam_sim.py (الكود التجريبي)

```python
# exam_sim.py
# Simple simulation of exam submission reliability in Madrasati

def submit_exam(server_up=True):
    if server_up:
        return "✅ Exam submitted successfully!"
    else:
        return "⚠️ Server down → Answers saved locally and will sync later."

if __name__ == "__main__":
    print(submit_exam(True))
    print(submit_exam(False))
