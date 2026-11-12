# -*- coding: utf-8 -*-
import json
import os
import re

DATA_PATH = os.path.join(os.path.dirname(__file__), "perkataan_bm_data.json")

def get_audio_filename(bm_word):
    clean = re.sub(r'[^a-zA-Z0-9]+', '_', bm_word.lower()).strip('_')
    return f"audio/{clean}.mp3"

with open(DATA_PATH, "r", encoding="utf-8") as f:
    vocab_list = json.load(f)

for item in vocab_list:
    item["audio"] = get_audio_filename(item["bm"])

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(vocab_list, f, ensure_ascii=False, indent=2)

print(f"Verified all {len(vocab_list)} items have correct native audio paths.")
