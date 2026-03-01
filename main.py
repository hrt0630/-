from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

@app.get("/ui", response_class=HTMLResponse)
def ui():
    html_content = """
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>理解保証AI型授業 - Premium Edition</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no, viewport-fit=cover">
    <script>
        window.MathJax = {
            tex: { inlineMath: [['$', '$']], displayMath: [['$$', '$$']] },
            chtml: { displayAlign: 'center' }
        };
    </script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <style>
        :root { 
            --accent: #00d2ff; 
            --accent-glow: rgba(0, 210, 255, 0.3);
            --border: rgba(255, 255, 255, 0.1); 
            --panel-bg: rgba(255, 255, 255, 0.05);
        }
        body, html { margin: 0; padding: 0; width: 100%; height: 100vh; display: flex; justify-content: center; align-items: center; background: #010208; font-family: "Hiragino Sans", sans-serif; color: white; overflow: hidden; }
        .liquid-bg { position: fixed; inset: 0; z-index: -1; background: radial-gradient(circle at 50% 50%, #0a1128 0%, #000 100%); }
        
        /* ログイン画面 */
        #login-screen { position: fixed; inset: 0; z-index: 5000; display: flex; justify-content: center; align-items: center; background: rgba(0,0,0,0.8); backdrop-filter: blur(20px); transition: 0.8s; }
        .login-glass { background: var(--panel-bg); padding: 40px; border-radius: 30px; border: 1px solid var(--border); width: 320px; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
        
        /* メインシーン */
        .scene { display: flex; gap: 20px; width: 95%; max-width: 1200px; height: 85vh; opacity: 0; transform: translateY(20px); transition: 1s cubic-bezier(0.22, 1, 0.36, 1); }
        .scene.active { opacity: 1; transform: translateY(0); }
        
        .page-panel { flex: 1; background: var(--panel-bg); border: 1px solid var(--border); backdrop-filter: blur(30px); padding: 35px; display: flex; flex-direction: column; overflow-y: auto; border-radius: 24px; position: relative; scrollbar-width: none; }
        .page-panel::-webkit-scrollbar { display: none; }

        .grade-nav { display: flex; background: rgba(255,255,255,0.05); padding: 5px; border-radius: 15px; margin-bottom: 25px; border: 1px solid var(--border); }
        .grade-btn { flex: 1; border: none; background: transparent; color: rgba(255,255,255,0.5); padding: 12px; cursor: pointer; border-radius: 10px; font-weight: bold; transition: 0.3s; }
        .grade-btn.active { background: var(--accent); color: #000; box-shadow: 0 4px 15px var(--accent-glow); }

        .unit-card { background: rgba(255,255,255,0.03); padding: 20px; border-radius: 18px; margin-bottom: 12px; cursor: pointer; border: 1px solid var(--border); transition: 0.3s; position: relative; overflow: hidden; }
        .unit-card:hover { background: rgba(255,255,255,0.08); border-color: var(--accent); transform: translateX(5px); }

        .layer { display: none; }
        .layer.show { display: block; animation: fadeIn 0.5s ease forwards; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }

        .section-title { color: var(--accent); border-bottom: 1px solid var(--accent); margin: 20px 0 10px; padding-bottom: 5px; font-weight: bold; }
        .point-box { background: rgba(0, 210, 255, 0.05); border-radius: 15px; padding: 20px; margin: 15px 0; border-left: 5px solid var(--accent); }
        .review-box { background: rgba(247, 183, 49, 0.05); border-left: 5px solid #f7b731; padding: 15px; margin: 20px 0; border-radius: 0 10px 10px 0; color: #f7b731; }
        
        .btn-primary { width: 100%; padding: 18px; border-radius: 15px; background: #fff; color: #000; font-weight: 900; border: none; cursor: pointer; margin-top: 20px; transition: 0.3s; }
        .btn-primary:hover { background: var(--accent); transform: scale(1.02); }
        
        .input-field { width: 100%; padding: 15px; border-radius: 12px; border: 1px solid var(--border); background: rgba(255,255,255,0.05); color: #fff; margin-bottom: 10px; box-sizing: border-box; outline: none; }
        .hidden { display: none; }
    </style>
</head>
<body>
    <div class="liquid-bg"></div>
    <div id="login-screen">
        <div class="login-glass">
            <h2>AI Study Link</h2>
            <p style="font-size: 0.9em; opacity: 0.6;">すみれさんの専用学習ルーム</p>
            <input type="email" class="input-field" placeholder="Email">
            <input type="password" class="input-field" placeholder="Password">
            <button class="btn-primary" onclick="launch()">学習を始める</button>
        </div>
    </div>

    <div class="scene" id="scene">
        <div class="page-panel">
            <div id="left-home" class="layer show">
                <span style="color:var(--accent); font-weight:bold; letter-spacing:3px;">DASHBOARD</span>
                <h1 style="font-size:2.5em; margin: 10px 0;">こんにちは！</h1>
                <p style="line-height:1.8; opacity:0.7;">右側のリストから単元を選んでください。</p>
            </div>
            <div id="left-lesson" class="layer">
                <button onclick="goHome()" style="background:none; border:none; color:var(--accent); cursor:pointer; margin-bottom:20px;">← 戻る</button>
                <h2 id="lesson-title" style="color:var(--accent);"></h2>
                <div class="section-title">📘 教科書の解説</div>
                <div id="lesson-desc"></div>
                <div class="section-title">💡 例題</div>
                <div id="lesson-example"></div>
                <div id="review-section" class="hidden">
                    <div class="section-title">🔄 復習ポイント</div>
                    <div id="lesson-review" class="review-box"></div>
                </div>
            </div>
        </div>

        <div class="page-panel">
            <div id="right-list" class="layer show">
                <div class="grade-nav">
                    <button class="grade-btn active" onclick="setGrade(1)">中1</button>
                    <button class="grade-btn" onclick="setGrade(2)">中2</button>
                    <button class="grade-btn" onclick="setGrade(3)">中3</button>
                </div>
                <div id="unit-container"></div>
            </div>
            <div id="right-practice" class="layer">
                <div class="section-title">✍️ 演習問題</div>
                <div id="practice-body"></div>
                <button id="check-btn" class="btn-primary" onclick="checkPractice()">演習を採点する</button>
                <div id="ruidai-section" class="hidden">
                    <div class="section-title">🔥 仕上げの類題</div>
                    <div id="ruidai-body"></div>
                    <button class="btn-primary" onclick="checkFinal()">最終チェック完了</button>
                </div>
            </div>
        </div>
    </div>

    <script>
        let currentUnit = null;
        const mathData = {
            1: [
                { id: '1-1', title: "正の数・負の数", desc: "<div class='point-box'>$(-3) \\\\times (-2) = +6$</div>", example: "$-5 + 2 = -3$ <br> ", q: {t:"$(-10) \\\\div 2$", a:"-5"}, review: "異符号の割り算はマイナスになります！", ruidai: {t:"$(-4)^2$", a:"16"} },
                { id: '1-2', title: "文字の式", desc: "<div class='point-box'>$a \\\\times b = ab$</div>", example: "$x+x+x = 3x$", q: {t:"$5a - 2a$", a:"3a"}, review: "同じ文字の係数のみ計算可能です。", ruidai: {t:"$4x - 7x$", a:"-3x"} }
            ],
            2: [
                { id: '2-1', title: "式の計算", desc: "<div class='point-box'>$2(a + 3b) = 2a + 6b$</div>", example: "$4x - (x - 2y) = 3x + 2y$", q: {t:"$3a+5b-a$", a:"2a+5b"}, review: "かっこの前のマイナスに注意しましょう。", ruidai: {t:"$(-2x) \\\\times 4y$", a:"-8xy"} }
            ],
            3: [
                { id: '3-1', title: "多項式の展開", desc: "<div class='point-box'>$$(x+a)(y+b) = xy + bx + ay + ab$$</div>", example: "$(x+2)(y+3) = xy+3x+2y+6$", q: {t:"$(x+1)(y+5)$ の定数項は？", a:"5"}, review: "順番に4回掛けるのが基本です。", ruidai: {t:"$(x+2)^2$", a:"x^2+4x+4"} }
            ]
        };

        function launch() { 
            document.getElementById('login-screen').style.opacity = '0';
            setTimeout(() => {
                document.getElementById('login-screen').style.display = 'none';
                document.getElementById('scene').classList.add('active');
                setGrade(1);
            }, 800);
        }

        function setGrade(g) {
            document.querySelectorAll('.grade-btn').forEach((b, i) => b.classList.toggle('active', i+1 === g));
            const container = document.getElementById('unit-container');
            container.innerHTML = (mathData[g] || []).map(u => `
                <div class="unit-card" onclick="openUnit('${g}', '${u.id}')">
                    <div style="font-size:0.8em; opacity:0.5;">Unit ${u.id}</div>
                    <div style="font-weight:bold; margin-top:5px;">${u.title}</div>
                </div>
            `).join('');
        }

        function openUnit(grade, id) {
            currentUnit = mathData[grade].find(u => u.id === id);
            document.getElementById('lesson-title').innerText = currentUnit.title;
            document.getElementById('lesson-desc').innerHTML = currentUnit.desc;
            document.getElementById('lesson-example').innerHTML = currentUnit.example;
            document.getElementById('practice-body').innerHTML = `<p>${currentUnit.q.t}</p><input id='ans-q' class='input-field' placeholder='答えを入力...'>`;
            
            document.getElementById('review-section').classList.add('hidden');
            document.getElementById('ruidai-section').classList.add('hidden');
            document.getElementById('check-btn').classList.remove('hidden');

            document.querySelectorAll('.layer').forEach(l => l.classList.remove('show'));
            document.getElementById('left-lesson').classList.add('show');
            document.getElementById('right-practice').classList.add('show');
            if (window.MathJax) MathJax.typesetPromise();
        }

        function checkPractice() {
            const val = document.getElementById('ans-q').value.trim();
            if (val === currentUnit.q.a) {
                alert("✨ 正解！復習と類題に進みます。");
                document.getElementById('lesson-review').innerHTML = currentUnit.review;
                document.getElementById('ruidai-body').innerHTML = `<p>${currentUnit.ruidai.t}</p><input id='ans-r' class='input-field' placeholder='仕上げの答え...'>`;
                document.getElementById('review-section').classList.remove('hidden');
                document.getElementById('ruidai-section').classList.remove('hidden');
                document.getElementById('check-btn').classList.add('hidden');
                if (window.MathJax) MathJax.typesetPromise();
            } else { alert("もう一度考えてみよう！"); }
        }

        function checkFinal() {
            const val = document.getElementById('ans-r').value.trim();
            if (val === currentUnit.ruidai.a) {
                alert("🎊 完璧！この単元はマスターです！"); goHome();
            } else { alert("あともう少し！復習ポイントを読んでみて。"); }
        }

        function goHome() {
            document.querySelectorAll('.layer').forEach(l => l.classList.remove('show'));
            document.getElementById('left-home').classList.add('show');
            document.getElementById('right-list').classList.add('show');
        }
    </script>
</body>
</html>
"""
    return HTMLResponse(content=html_content)

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
