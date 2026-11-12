import json

with open(r'X:\scripts_custom\iflow-edugames-perkataanBM\perkataan_bm_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

json_str = json.dumps(data, ensure_ascii=False)

html_content = '''<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>华小国语词汇连连乐 | Permainan Kosa Kata BM SJK(C)</title>
    <style>
        * {
            box-sizing: border-box;
            user-select: none;
            -webkit-user-select: none;
        }

        body {
            font-family: 'Comic Sans MS', 'Chalkboard SE', 'Segoe UI', 'Microsoft YaHei', sans-serif;
            background: linear-gradient(135deg, #70e1f5 0%, #ffd194 100%);
            margin: 0;
            padding: 10px;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow-x: hidden;
        }

        .game-area {
            position: relative;
            width: 880px;
            max-width: 98vw;
            min-height: 600px;
            background: linear-gradient(to bottom, #ffffff 0%, #f4faff 100%);
            border: 6px solid #4CAF50;
            border-radius: 24px;
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.25);
            padding: 20px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            overflow: hidden;
        }

        /* Top Header Bar */
        .top-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 10px;
            padding-bottom: 12px;
            border-bottom: 3px dashed #b2dfdb;
        }

        .level-badge {
            background: #e8f5e9;
            color: #1b5e20;
            padding: 6px 16px;
            border-radius: 20px;
            font-size: 1.15em;
            font-weight: bold;
            border: 2px solid #81c784;
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .score-box {
            display: flex;
            gap: 10px;
            font-size: 0.95em;
        }

        .score-item {
            padding: 2px 10px;
            border-radius: 12px;
            font-weight: bold;
        }
        .score-betul { background: #c8e6c9; color: #2e7d32; }
        .score-salah { background: #ffcdd2; color: #c62828; }

        .control-buttons {
            display: flex;
            gap: 8px;
            align-items: center;
        }

        .top-btn {
            background: #ffffff;
            border: 2px solid #90caf9;
            color: #1565c0;
            padding: 6px 12px;
            font-size: 0.95em;
            border-radius: 15px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            gap: 4px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.08);
        }

        .top-btn:hover {
            background: #e3f2fd;
            transform: translateY(-2px);
        }

        .category-select {
            padding: 6px 12px;
            border-radius: 15px;
            border: 2px solid #81c784;
            font-family: inherit;
            font-weight: bold;
            background: #ffffff;
            color: #2e7d32;
            cursor: pointer;
            outline: none;
            font-size: 0.92em;
        }

        /* Instruction Header */
        .instruction-box {
            text-align: center;
            margin-top: 10px;
            margin-bottom: 5px;
        }

        .instruction-text {
            font-size: 1.25em;
            color: #1976d2;
            font-weight: bold;
            text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.8);
        }

        .sub-instruction {
            font-size: 0.95em;
            color: #666;
            margin-top: 2px;
        }

        /* Chinese Word Card (Question Prompt) */
        .question-card-container {
            display: flex;
            justify-content: center;
            margin: 15px 0;
        }

        .question-card {
            background: linear-gradient(135deg, #fff9c4 0%, #fff59d 100%);
            border: 5px solid #fbc02d;
            border-radius: 22px;
            padding: 16px 40px;
            text-align: center;
            box-shadow: 0 8px 18px rgba(251, 192, 45, 0.35);
            min-width: 320px;
            max-width: 90%;
            transition: transform 0.3s;
        }

        .question-card:hover {
            transform: scale(1.02);
        }

        .cat-tag {
            display: inline-block;
            background: #ffe082;
            color: #795548;
            font-size: 0.85em;
            padding: 3px 12px;
            border-radius: 12px;
            margin-bottom: 6px;
            font-weight: bold;
        }

        .chinese-word {
            font-size: 3em;
            font-weight: 900;
            color: #d84315;
            letter-spacing: 4px;
            margin: 2px 0;
            text-shadow: 2px 2px 0px #fff;
        }

        .pinyin-text {
            font-size: 1.15em;
            color: #5d4037;
            font-weight: bold;
        }

        /* 4 BM Choices Options Grid */
        .options-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 16px;
            margin: 15px 0;
        }

        .option-btn {
            background: #ffffff;
            border: 4px solid #42a5f5;
            border-radius: 18px;
            padding: 14px 18px;
            font-family: inherit;
            font-size: 1.35em;
            font-weight: bold;
            color: #1565c0;
            cursor: pointer;
            transition: all 0.25s ease;
            box-shadow: 0 5px 12px rgba(66, 165, 245, 0.2);
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 14px;
            text-align: left;
        }

        .option-left {
            display: flex;
            align-items: center;
            gap: 14px;
            flex-grow: 1;
        }

        .option-btn:hover:not(:disabled) {
            transform: translateY(-3px) scale(1.02);
            background: #e3f2fd;
            border-color: #1e88e5;
            box-shadow: 0 8px 16px rgba(30, 136, 229, 0.3);
        }

        .option-badge {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 38px;
            height: 38px;
            border-radius: 50%;
            background: #bbdefb;
            color: #0d47a1;
            font-size: 1.05em;
            font-weight: 900;
            flex-shrink: 0;
            border: 2px solid #64b5f6;
        }

        .option-label {
            flex-grow: 1;
            word-break: break-word;
        }

        .option-audio-btn {
            background: #e3f2fd;
            border: 1px solid #90caf9;
            border-radius: 50%;
            width: 34px;
            height: 34px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.9em;
            cursor: pointer;
            color: #1565c0;
            transition: transform 0.2s, background 0.2s;
            flex-shrink: 0;
        }

        .option-audio-btn:hover {
            transform: scale(1.15);
            background: #bbdefb;
        }

        /* States for Options */
        .option-btn.correct {
            background: #4caf50 !important;
            border-color: #2e7d32 !important;
            color: #ffffff !important;
            animation: bounce 0.6s ease;
            box-shadow: 0 6px 18px rgba(76, 175, 80, 0.5) !important;
        }
        .option-btn.correct .option-badge {
            background: #ffffff !important;
            color: #2e7d32 !important;
            border-color: #ffffff !important;
        }
        .option-btn.correct .option-audio-btn {
            background: rgba(255,255,255,0.3) !important;
            color: #ffffff !important;
            border-color: #ffffff !important;
        }

        .option-btn.incorrect {
            background: #ef5350 !important;
            border-color: #c62828 !important;
            color: #ffffff !important;
            animation: shake 0.5s ease;
            opacity: 0.65;
            cursor: not-allowed;
        }
        .option-btn.incorrect .option-badge {
            background: #ffcdd2 !important;
            color: #c62828 !important;
            border-color: #ffffff !important;
        }

        .option-btn.grayed-out {
            background: #eeeeee !important;
            border-color: #bdbdbd !important;
            color: #9e9e9e !important;
            opacity: 0.45;
            cursor: not-allowed;
            box-shadow: none !important;
        }

        /* Keyframe animations */
        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
            40% { transform: translateY(-16px); }
            60% { transform: translateY(-8px); }
        }

        @keyframes shake {
            0%, 100% { transform: translateX(0); }
            20%, 60% { transform: translateX(-10px); }
            40%, 80% { transform: translateX(10px); }
        }

        /* Feedback and Learning Card */
        .feedback-area {
            min-height: 50px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            margin-top: 5px;
        }

        .feedback-banner {
            font-size: 1.6em;
            font-weight: 900;
            padding: 4px 20px;
            border-radius: 12px;
            transition: all 0.3s;
            text-align: center;
        }

        .learning-card {
            display: none;
            background: #f1f8e9;
            border: 3px solid #81c784;
            border-radius: 16px;
            padding: 14px 20px;
            margin-top: 10px;
            width: 100%;
            text-align: center;
            box-shadow: 0 4px 10px rgba(0,0,0,0.06);
            animation: fadeIn 0.4s ease;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(8px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .learning-head {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 12px;
            flex-wrap: wrap;
            margin-bottom: 8px;
        }

        .learning-bm {
            font-size: 1.7em;
            font-weight: 900;
            color: #2e7d32;
        }

        .learning-zh {
            font-size: 1.3em;
            color: #424242;
            font-weight: bold;
        }

        .pronounce-btn {
            background: #e8f5e9;
            border: 2px solid #4caf50;
            color: #2e7d32;
            border-radius: 50%;
            width: 42px;
            height: 42px;
            font-size: 1.3em;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: transform 0.2s, background 0.2s;
            box-shadow: 0 2px 6px rgba(46, 125, 50, 0.25);
        }
        .pronounce-btn:hover {
            transform: scale(1.15);
            background: #c8e6c9;
        }

        .native-speaker-tag {
            display: inline-block;
            background: #c8e6c9;
            color: #1b5e20;
            font-size: 0.8em;
            padding: 2px 10px;
            border-radius: 10px;
            font-weight: bold;
            margin-left: 6px;
        }

        .example-sentence {
            font-size: 1.1em;
            color: #37474f;
            margin: 6px 0;
            line-height: 1.4;
        }

        .example-sentence strong {
            color: #00796b;
        }

        .example-sentence-zh {
            font-size: 0.95em;
            color: #78909c;
        }

        /* Next Button */
        .bottom-action-bar {
            display: flex;
            justify-content: center;
            margin-top: 10px;
        }

        .next-btn {
            display: none;
            background: linear-gradient(135deg, #ff9800 0%, #f57c00 100%);
            color: #ffffff;
            border: none;
            padding: 10px 32px;
            border-radius: 25px;
            font-size: 1.25em;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(245, 124, 0, 0.4);
            transition: transform 0.2s, background 0.2s;
        }

        .next-btn:hover {
            transform: scale(1.05);
            background: linear-gradient(135deg, #ffa726 0%, #fb8c00 100%);
        }

        /* End Screen modal */
        .celebrate-screen {
            display: none;
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            background: rgba(255, 255, 255, 0.96);
            border-radius: 18px;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 20px;
            z-index: 100;
        }

        .celebrate-trophy {
            font-size: 4.5em;
            animation: bounce 1.2s infinite;
        }

        .restart-btn {
            background: #4caf50;
            color: white;
            border: none;
            padding: 12px 36px;
            font-size: 1.3em;
            font-weight: bold;
            border-radius: 25px;
            cursor: pointer;
            margin-top: 20px;
            box-shadow: 0 5px 15px rgba(76, 175, 80, 0.4);
        }

        /* Responsive Mobile Layout */
        @media (max-width: 768px) {
            body {
                padding: 4px;
            }

            .game-area {
                width: 100%;
                min-height: 98vh;
                padding: 12px 10px;
                border-width: 4px;
                border-radius: 16px;
            }

            .top-bar {
                font-size: 0.85em;
                gap: 6px;
            }

            .level-badge {
                font-size: 1em;
                padding: 4px 10px;
            }

            .instruction-text {
                font-size: 1.05em;
            }

            .question-card {
                padding: 10px 20px;
                min-width: 250px;
            }

            .chinese-word {
                font-size: 2.3em;
                letter-spacing: 2px;
            }

            .pinyin-text {
                font-size: 0.95em;
            }

            .options-grid {
                grid-template-columns: 1fr;
                gap: 10px;
                margin: 10px 0;
            }

            .option-btn {
                font-size: 1.15em;
                padding: 10px 14px;
                gap: 10px;
            }

            .option-badge {
                width: 32px;
                height: 32px;
                font-size: 0.95em;
            }

            .learning-bm {
                font-size: 1.3em;
            }

            .example-sentence {
                font-size: 0.95em;
            }

            .feedback-banner {
                font-size: 1.25em;
            }
        }
    </style>
</head>
<body>

    <!-- Audio SFX -->
    <audio id="sfx-correct">
        <source src="correct.mp3" type="audio/mpeg">
    </audio>
    <audio id="sfx-wrong">
        <source src="wrong.mp3" type="audio/mpeg">
    </audio>
    <audio id="sfx-timeout">
        <source src="timeout.mp3" type="audio/mpeg">
    </audio>
    <audio id="bgm-music" loop>
        <source src="bgm.mp3" type="audio/mpeg">
    </audio>

    <div class="game-area" id="game-area">
        <!-- Top status bar -->
        <div class="top-bar">
            <div class="level-badge">
                <span id="level-text">第 1 关</span>
                <div class="score-box">
                    <span class="score-item score-betul">✅ <span id="score-b">0</span></span>
                    <span class="score-item score-salah">❌ <span id="score-s">0</span></span>
                </div>
            </div>

            <div class="control-buttons">
                <select class="category-select" id="category-filter" onchange="changeCategory()">
                    <option value="ALL">🌟 全部词汇 (Semua)</option>
                    <option value="动词 / Kata Kerja">🏃 动词 (Kata Kerja)</option>
                    <option value="形容词 / Kata Adjektif">✨ 形容词 (Kata Adjektif)</option>
                    <option value="身体部位 / Anggota Badan">👀 身体部位 (Badan)</option>
                    <option value="家庭与人物 / Keluarga">👨‍👩‍👧 家庭人物 (Keluarga)</option>
                    <option value="职业 / Pekerjaan">💼 职业 (Pekerjaan)</option>
                    <option value="动物 / Haiwan">🐱 动物 (Haiwan)</option>
                    <option value="水果蔬菜 / Buah & Sayur">🍎 水果蔬菜 (Buah/Sayur)</option>
                    <option value="用品 / Benda">🎒 学校用品 (Benda)</option>
                    <option value="场所与交通 / Tempat & Kenderaan">🏫 场所交通 (Tempat/Kenderaan)</option>
                    <option value="道德与自然 / Nilai & Alam">🌈 道德与自然 (Nilai/Alam)</option>
                </select>

                <button class="top-btn" id="sfx-toggle-btn" onclick="toggleSFX()">🔊 音效</button>
                <button class="top-btn" id="bgm-toggle-btn" onclick="toggleBGM()">🎵 音乐</button>
            </div>
        </div>

        <!-- Instructions -->
        <div class="instruction-box">
            <div class="instruction-text">请看中文词汇，选出正确的国语 (Bahasa Malaysia)！</div>
            <div class="sub-instruction">Pilih perkataan Bahasa Melayu yang betul bagi maksud perkataan Cina di bawah.</div>
        </div>

        <!-- Central Question Prompt (Chinese Word) -->
        <div class="question-card-container">
            <div class="question-card" id="question-card">
                <div class="cat-tag" id="cat-tag">分类标签</div>
                <div class="chinese-word" id="chinese-word">中文词</div>
                <div class="pinyin-text" id="pinyin-text">pīn yīn</div>
            </div>
        </div>

        <!-- 4 Options Grid (A, B, C, D) -->
        <div class="options-grid" id="options-grid">
            <!-- Buttons dynamically populated -->
        </div>

        <!-- Feedback & Learning Expansion Card -->
        <div class="feedback-area">
            <div class="feedback-banner" id="feedback-banner"></div>

            <div class="learning-card" id="learning-card">
                <div class="learning-head">
                    <span class="learning-bm" id="card-bm">perkataan</span>
                    <button class="pronounce-btn" id="pronounce-btn" title="点击聆听真人发音 (Dengar sebutan asli)" onclick="playNativeBM()">🔊</button>
                    <span class="learning-zh" id="card-zh">（中文释义）</span>
                    <span class="native-speaker-tag">🇲🇾 真人原声发音</span>
                </div>
                <div class="example-sentence" id="card-example-bm">Contoh ayat...</div>
                <div class="example-sentence-zh" id="card-example-zh">例句中文翻译...</div>
            </div>
        </div>

        <!-- Next Question Action Button -->
        <div class="bottom-action-bar">
            <button class="next-btn" id="next-btn" onclick="nextQuestion()">下一题 (Seterusnya) ➔</button>
        </div>

        <!-- Game Completion Screen -->
        <div class="celebrate-screen" id="celebrate-screen">
            <div class="celebrate-trophy">🏆🎉</div>
            <h1 style="color: #2e7d32; margin: 10px 0;">Tahniah! 恭喜通关！</h1>
            <p style="font-size: 1.3em; color: #424242; margin: 8px 0;">你已经完成了本单元的所有词汇练习！</p>
            <div style="font-size: 1.2em; margin: 15px 0;">
                <p>✅ 答对题数：<strong id="final-correct" style="color: #2e7d32;">0</strong></p>
                <p>❌ 答错次数：<strong id="final-wrong" style="color: #c62828;">0</strong></p>
                <p>🎯 答题正确率：<strong id="final-accuracy" style="color: #1565c0;">100%</strong></p>
            </div>
            <button class="restart-btn" onclick="restartGame()">再玩一次 (Main Semula) 🔄</button>
        </div>
    </div>

    <!-- Embedded Fallback Data with Local Native Audio Paths -->
    <script id="embedded-data" type="application/json">
''' + json_str + '''
    </script>

    <script>
        let allVocabulary = [];
        let activePool = [];
        let currentIndex = 0;
        let currentQuestion = null;
        let gameActive = false;
        let autoNextTimer = null;
        let currentVoiceAudio = null;

        let scoreBetul = 0;
        let scoreSalah = 0;
        let hasMadeMistakeThisRound = false;

        let sfxEnabled = true;
        let bgmEnabled = false;

        // Shuffle Utility
        function shuffle(array) {
            const arr = [...array];
            for (let i = arr.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [arr[i], arr[j]] = [arr[j], arr[i]];
            }
            return arr;
        }

        // Audio Controls
        function toggleSFX() {
            sfxEnabled = !sfxEnabled;
            const btn = document.getElementById('sfx-toggle-btn');
            btn.innerHTML = sfxEnabled ? "🔊 音效" : "🔇 音效";
            btn.style.color = sfxEnabled ? "#1565c0" : "#757575";
        }

        function toggleBGM() {
            const bgm = document.getElementById('bgm-music');
            const btn = document.getElementById('bgm-toggle-btn');
            if (bgmEnabled) {
                bgm.pause();
                bgmEnabled = false;
                btn.innerHTML = "🎵 音乐";
                btn.style.color = "#1565c0";
            } else {
                bgm.volume = 0.35;
                bgm.play().then(() => {
                    bgmEnabled = true;
                    btn.innerHTML = "🎶 音乐: 开";
                    btn.style.color = "#2e7d32";
                }).catch(e => {
                    console.log("BGM autoplay blocked until interaction:", e);
                });
            }
        }

        function playSound(id) {
            if (!sfxEnabled) return;
            const audio = document.getElementById(id);
            if (audio) {
                audio.currentTime = 0;
                audio.play().catch(e => console.log("Sound play error:", e));
            }
        }

        // Native Malaysian Speaker Audio Playback
        function playNativeBM(audioSrc) {
            if (!sfxEnabled) return;
            if (!audioSrc && currentQuestion && currentQuestion.audio) {
                audioSrc = currentQuestion.audio;
            }
            if (!audioSrc) return;

            if (currentVoiceAudio) {
                currentVoiceAudio.pause();
                currentVoiceAudio.currentTime = 0;
            }

            currentVoiceAudio = new Audio(audioSrc);
            currentVoiceAudio.volume = 1.0;
            currentVoiceAudio.play().catch(e => {
                console.log("Native audio playback failed:", e);
            });
        }

        // Data Loading
        async function initGameData() {
            try {
                const res = await fetch('perkataan_bm_data.json');
                if (!res.ok) throw new Error("Fetch failed");
                allVocabulary = await res.json();
            } catch (err) {
                console.warn("Using embedded fallback data:", err);
                const embeddedTag = document.getElementById('embedded-data');
                allVocabulary = JSON.parse(embeddedTag.textContent);
            }

            changeCategory();
        }

        function changeCategory() {
            const selectedCat = document.getElementById('category-filter').value;
            if (selectedCat === "ALL") {
                activePool = shuffle(allVocabulary);
            } else {
                const filtered = allVocabulary.filter(item => item.category === selectedCat);
                activePool = shuffle(filtered);
            }

            currentIndex = 0;
            scoreBetul = 0;
            scoreSalah = 0;
            document.getElementById('score-b').textContent = "0";
            document.getElementById('score-s').textContent = "0";
            document.getElementById('celebrate-screen').style.display = 'none';

            loadNextQuestion();
        }

        // Distractor choices generator (3 wrong choices with authentic audio)
        function generateOptions(correctItem) {
            let wrongs = [];
            let seen = new Set();
            seen.add(correctItem.bm.toLowerCase());

            // First try same category
            const sameCat = allVocabulary.filter(item => 
                item.category === correctItem.category && item.bm.toLowerCase() !== correctItem.bm.toLowerCase()
            );
            const shuffledSame = shuffle(sameCat);
            for (let item of shuffledSame) {
                if (!seen.has(item.bm.toLowerCase())) {
                    wrongs.push(item);
                    seen.add(item.bm.toLowerCase());
                    if (wrongs.length >= 3) break;
                }
            }

            // If not enough, draw from all pool
            if (wrongs.length < 3) {
                const shuffledAll = shuffle(allVocabulary);
                for (let item of shuffledAll) {
                    if (!seen.has(item.bm.toLowerCase())) {
                        wrongs.push(item);
                        seen.add(item.bm.toLowerCase());
                        if (wrongs.length >= 3) break;
                    }
                }
            }

            // Create 4 choices
            const choices = [
                { text: correctItem.bm, audio: correctItem.audio, isCorrect: true },
                { text: wrongs[0].bm, audio: wrongs[0].audio, isCorrect: false },
                { text: wrongs[1].bm, audio: wrongs[1].audio, isCorrect: false },
                { text: wrongs[2].bm, audio: wrongs[2].audio, isCorrect: false }
            ];

            return shuffle(choices);
        }

        function loadNextQuestion() {
            if (autoNextTimer) clearTimeout(autoNextTimer);
            if (currentVoiceAudio) {
                currentVoiceAudio.pause();
                currentVoiceAudio.currentTime = 0;
            }

            if (currentIndex >= activePool.length) {
                showCelebration();
                return;
            }

            gameActive = true;
            hasMadeMistakeThisRound = false;
            currentQuestion = activePool[currentIndex];

            // Update Top Level Header
            document.getElementById('level-text').textContent = `第 ${currentIndex + 1} 关 / 共 ${activePool.length} 关`;

            // Update Question Box
            document.getElementById('cat-tag').textContent = currentQuestion.category;
            document.getElementById('chinese-word').textContent = currentQuestion.chinese;
            document.getElementById('pinyin-text').textContent = currentQuestion.pinyin || "";

            // Reset UI states
            document.getElementById('feedback-banner').textContent = "";
            document.getElementById('learning-card').style.display = "none";
            document.getElementById('next-btn').style.display = "none";

            // Generate 4 Options
            const choices = generateOptions(currentQuestion);
            const grid = document.getElementById('options-grid');
            grid.innerHTML = "";

            const letters = ["A", "B", "C", "D"];
            choices.forEach((choice, idx) => {
                const btn = document.createElement('button');
                btn.className = "option-btn";
                btn.innerHTML = `
                    <div class="option-left">
                        <span class="option-badge">${letters[idx]}</span>
                        <span class="option-label">${choice.text}</span>
                    </div>
                    <span class="option-audio-btn" title="试听发音 (Dengar)" onclick="event.stopPropagation(); playNativeBM('${choice.audio}')">🔊</span>
                `;
                btn.onclick = () => onSelectChoice(choice, btn);
                grid.appendChild(btn);
            });
        }

        function onSelectChoice(choice, btn) {
            if (!gameActive) return;

            const banner = document.getElementById('feedback-banner');
            const allOptionBtns = document.querySelectorAll('.option-btn');

            if (choice.isCorrect) {
                gameActive = false;
                playSound('sfx-correct');

                if (!hasMadeMistakeThisRound) {
                    scoreBetul++;
                    document.getElementById('score-b').textContent = scoreBetul;
                }

                btn.classList.add('correct');

                // Dim other buttons
                allOptionBtns.forEach(b => {
                    if (b !== btn) b.classList.add('grayed-out');
                    b.disabled = true;
                });

                banner.innerHTML = "🎉 太棒了！答对了！(Tahniah! Betul!)";
                banner.style.color = "#2e7d32";

                // Populate Learning Card
                document.getElementById('card-bm').textContent = currentQuestion.bm;
                document.getElementById('card-zh').textContent = `（${currentQuestion.chinese}）`;
                document.getElementById('card-example-bm').innerHTML = highlightWord(currentQuestion.example_bm, currentQuestion.bm);
                document.getElementById('card-example-zh').textContent = currentQuestion.example_zh;
                document.getElementById('learning-card').style.display = "block";

                // Play REAL Malaysian native speaker voice!
                setTimeout(() => {
                    playNativeBM(currentQuestion.audio);
                }, 400);

                // Show Next Button
                document.getElementById('next-btn').style.display = "inline-block";

                // Auto advance after 3.5 seconds
                autoNextTimer = setTimeout(() => {
                    nextQuestion();
                }, 3500);

            } else {
                playSound('sfx-wrong');
                btn.classList.add('incorrect');
                btn.disabled = true;

                if (!hasMadeMistakeThisRound) {
                    hasMadeMistakeThisRound = true;
                    scoreSalah++;
                    document.getElementById('score-s').textContent = scoreSalah;
                }

                banner.innerHTML = "❌ 不对哦，再试一次！(Cuba lagi ya!)";
                banner.style.color = "#c62828";
            }
        }

        function highlightWord(sentence, word) {
            if (!sentence || !word) return sentence || "";
            // regex case-insensitive match for base word
            const regex = new RegExp(`(${word})`, 'gi');
            return sentence.replace(regex, `<strong>$1</strong>`);
        }

        function nextQuestion() {
            if (autoNextTimer) clearTimeout(autoNextTimer);
            currentIndex++;
            loadNextQuestion();
        }

        function showCelebration() {
            gameActive = false;
            document.getElementById('celebrate-screen').style.display = 'flex';
            document.getElementById('final-correct').textContent = scoreBetul;
            document.getElementById('final-wrong').textContent = scoreSalah;
            const total = scoreBetul + scoreSalah;
            const acc = total > 0 ? Math.round((scoreBetul / total) * 100) : 100;
            document.getElementById('final-accuracy').textContent = acc + "%";
            playSound('sfx-correct');
        }

        function restartGame() {
            changeCategory();
        }

        window.onload = () => {
            initGameData();
        };
    </script>
</body>
</html>
'''

with open(r'X:\scripts_custom\iflow-edugames-perkataanBM\index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Generated updated X:\\scripts_custom\\iflow-edugames-perkataanBM\\index.html with native Malaysian audio successfully!")
