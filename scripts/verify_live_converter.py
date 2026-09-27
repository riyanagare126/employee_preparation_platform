import urllib.request
import json
import sys

print("[VERIFICATION] Checking live server at http://127.0.0.1:5000...")

try:
    # 1. Check frontend page
    with urllib.request.urlopen("http://127.0.0.1:5000/answer-builder.html", timeout=10) as resp:
        html = resp.read().decode("utf-8")
        assert "Honest-to-Professional Converter" in html
        assert "form-honest-converter" in html
        assert "honest-converter-section" in html
        print("  [OK] answer-builder.html serves converter markup correctly")

    # 2. Check live convert endpoint
    req = urllib.request.Request(
        "http://127.0.0.1:5000/api/converted-answers/convert",
        data=json.dumps({
            "question_type": "Why are you leaving your current job?",
            "raw_answer": "My manager is toxic and micromanages every commit. Compensation is below market.",
            "target_role": "Full Stack Developer",
            "target_company": "Microsoft"
        }).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        assert data.get("success") is True
        assert "professional_answer" in data["data"]
        assert len(data["data"]["red_flags"]) >= 1
        assert len(data["data"]["follow_up_questions"]) == 2
        print(f"  [OK] Live API /api/converted-answers/convert responded 200 with structured data:")
        print(f"       Professional Answer: {data['data']['professional_answer'][:80]}...")
        print(f"       Short 30s Answer:    {data['data']['short_answer'][:60]}...")
        print(f"       Red flags detected:  {len(data['data']['red_flags'])}")
        print(f"       Follow-up questions: {len(data['data']['follow_up_questions'])}")

    print("\n[ALL LIVE CONVERTER CHECKS PASSED SUCCESSFULLY!]")
except Exception as e:
    print(f"  [FAIL] Live verification failed: {e}")
    sys.exit(1)
