psywar_noise_detector.py
class PsywarNoiseDetector:
    def __init__(self):
        self.fear_keywords = ['သေမလား', 'စစ်ဖြစ်မလား', 'ပြေးပါ']
        self.urgency_triggers = ['အခုပဲ', 'ချက်ချင်း']

    def detect(self, posts):
        fear = sum(1 for p in posts if any(k in p for k in self.fear_keywords))
        urgency = sum(1 for p in posts if any(u in p for u in self.urgency_triggers))
        score = (fear * 0.5 + urgency * 0.5) / len(posts) if posts else 0
        return {"psywar_noise_score": round(score, 3), "recommendation": "COUNTER" if score > 0.6 else "Monitor"}
