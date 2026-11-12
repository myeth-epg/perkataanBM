# -*- coding: utf-8 -*-
import os
import re
import json
import asyncio
import edge_tts

VOICE = "ms-MY-YasminNeural" # Authentic Malaysian Native Female Speaker (clear, educational, baku)
DATA_PATH = r"X:\scripts_custom\iflow-edugames-perkataanBM\perkataan_bm_data.json"
AUDIO_DIR = r"X:\scripts_custom\iflow-edugames-perkataanBM\audio"

os.makedirs(AUDIO_DIR, exist_ok=True)

with open(DATA_PATH, "r", encoding="utf-8") as f:
    vocab_list = json.load(f)

def get_filename(bm_word):
    clean = re.sub(r'[^a-zA-Z0-9]+', '_', bm_word.lower()).strip('_')
    return f"{clean}.mp3"

async def generate_audio_for_item(item, sem):
    bm_word = item["bm"]
    filename = get_filename(bm_word)
    filepath = os.path.join(AUDIO_DIR, filename)
    item["audio"] = f"audio/{filename}"

    if os.path.exists(filepath) and os.path.getsize(filepath) > 1000:
        return # already generated

    async with sem:
        try:
            # SJKC primary school friendly rate (-5% for slightly clearer articulation)
            tts = edge_tts.Communicate(text=bm_word, voice=VOICE, rate="-5%")
            await tts.save(filepath)
            print(f"[OK] {bm_word} -> {filename}")
        except Exception as e:
            print(f"[ERR] Failed for {bm_word}: {e}")

async def main():
    print(f"Total vocabulary to process: {len(vocab_list)}")
    sem = asyncio.Semaphore(5) # 5 concurrent downloads to be polite and fast
    tasks = [generate_audio_for_item(item, sem) for item in vocab_list]
    await asyncio.gather(*tasks)

    # Save updated json with audio paths
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(vocab_list, f, ensure_ascii=False, indent=2)
    print("Updated perkataan_bm_data.json with local audio paths.")

if __name__ == "__main__":
    asyncio.run(main())
