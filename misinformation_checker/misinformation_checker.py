misinformation_checker/misinformation_checker.py
import joblib
import pandas as pd

class MyanmarMisinfoChecker:
    def __init__(self):
        self.emotion_keywords = ['လှုပ်', 'သေဆုံး', 'အန္တရာယ်', 'သတိပေး']
        self.source_keywords = ['သတင်း', 'အစိုးရ', 'တပ်မတော်']

    def predict(self, text):
        flags = []
        if any(word in text for word in self.emotion_keywords):
            flags.append("High emotional trigger")
        if not any(src in text for src in self.source_keywords):
            flags.append("No verified source")
        return {"result": "FALSE" if flags else "UNCLEAR", "flags": flags}
