from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

@app.get("/ui", response_class=HTMLResponse)
def ui():
    # 修正ポイント: 文字列をしっかり最後まで閉じ、returnを追加しました
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
        body, html { margin: 0; padding: 0; width: 100%; height: 100vh; display: flex; justify-content: center; align-items: center; background: #010208; font-family: "Hiragino Sans", "Meiryo", sans-serif; color: white; overflow: hidden; }
        .liquid-bg { position: fixed; inset: 0; z-index: -1; background: radial-gradient(circle at 50% 50%, #0a1128 0%, #000 100%); }
        
        #login-screen { position: fixed; inset: 0; z-index: 5000; display: flex; justify-content: center; align-items: center; background: rgba(0,0,0,0.8); backdrop-filter: blur(20px); transition: 0.8s; }
        .login-glass { background: var(--panel-bg); padding: 40px; border-radius: 30px; border: 1px solid var(--border); width: 320px; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
        
        .scene { display: flex; gap: 20px; width: 90%; max-width: 1100px; height: 85vh; opacity: 0; transform: translateY(20px); transition: 1s cubic-bezier(0.22, 1, 0.36, 1); }
        .scene.active { opacity: 1; transform: translateY(0); }
        
        .page-panel { flex: 1; background: var(--panel-bg); border: 1px solid var(--border); backdrop-filter: blur(30px); padding: 35px; display: flex; flex-direction: column; overflow-y: auto; border-radius: 24px; position: relative; scrollbar-width: none; }
        .page-panel::-webkit-scrollbar { display: none; }

        .grade-nav { display: flex; background: rgba(255,255,255,0.05); padding: 5px; border-radius: 15px; margin-bottom: 25px; border: 1px solid var(--border); }
        .grade-btn { flex: 1; border: none; background: transparent; color: rgba(255,255,255,0.5); padding: 12px; cursor: pointer; border-radius: 10px; font-weight: bold; transition: 0.3s; }
        .grade-btn.active { background: var(--accent); color: #000; box-shadow: 0 4px 15px var(--accent-glow); }

        .unit-card { background: rgba(255,255,255,0.03); padding: 20px; border-radius: 18px; margin-bottom: 12px; cursor: pointer; border: 1px solid var(--border); transition: 0.3s; position: relative; overflow: hidden; }
        .unit-card:hover { background: rgba(255,255,255,0.08); border-color: var(--accent); transform: translateX(5px); }
        .unit-card::before { content: ''; position: absolute; left: 0; top: 0; height: 100%; width: 4px; background: var(--accent); opacity: 0; transition: 0.3s; }
        .unit-card:hover::before { opacity: 1; }

        .layer { display: none; animation: fadeIn 0.5s ease forwards; }
        .layer.show { display: block; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }

        .point-box { background: rgba(0, 210, 255, 0.05); border-radius: 15px; padding: 20px; margin: 20px 0; border-left: 5px solid var(--accent); }
        .example-box { background: rgba(255,255,255,0.03); padding: 15px; border-radius: 12px; border: 1px dashed var(--border); margin: 10px 0; font-size: 0.95em; }
        
        .btn-primary { width: 100%; padding: 18px; border-radius: 15px; background: #fff; color: #000; font-weight: 900; border: none; cursor: pointer; margin-top: 20px; transition: 0.3s; }
        .btn-primary:hover { background: var(--accent); transform: scale(1.02); }
        
        .input-field { width: 100%; padding: 15px; border-radius: 12px; border: 1px solid var(--border); background: rgba(255,255,255,0.05); color: #fff; margin-bottom: 10px; box-sizing: border-box; outline: none; }
        .input-field:focus { border-color: var(--accent); }

        #hint-area { display: none; margin-top: 20px; padding: 20px; background: rgba(247, 183, 49, 0.1); border-radius: 15px; border: 1px solid rgba(247, 183, 49, 0.2); color: #f7b731; line-height: 1.6; }
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
                <p style="line-height:1.8; opacity:0.7;">右側のリストから学びたい単元を選んでください。<br>学年ごとに整理されています。</p>
            </div>
            <div id="left-lesson" class="layer">
                <button onclick="goHome()" style="background:none; border:none; color:var(--accent); cursor:pointer; margin-bottom:20px;">← 戻る</button>
                <h2 id="lesson-title" style="font-size:1.8em; color:var(--accent);"></h2>
                <div id="lesson-body"></div>
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
                <div id="practice-head"></div>
                <div id="practice-body"></div>
                <button class="btn-primary" onclick="checkAnswers()">結果を判定する</button>
                <div id="hint-area"></div>
            </div>
        </div>
    </div>

    <script>
        let currentUnit = null;
        const mathData = {
            1: [
                { id: '1-1', title: "正の数・負の数", desc: "<div class='point-box'>$(-3) \\\\times (-2) = +6$</div><p>符号のルールを覚えよう！</p>", examples: "<div class='example-box'><b>例題:</b> $(-5) + (+2) = -3$</div>", q: [ {t:"$(-10) \\\\div 2$", a:"-5", h:"マイナスとプラスの割り算はマイナス！"}, {t:"$(-4)^2$", a:"16", h:"$(-4) \\\\times (-4)$ です。"} ] },
                { id: '1-2', title: "文字の式", desc: "<div class='point-box'>$a \\\\times b = ab$</div><p>掛け算の記号を省くのがルール！</p>", examples: "<div class='example-box'><b>例題:</b> $x \\\\times (-3) = -3x$</div>", q: [ {t:"$x+x+x$", a:"3x", h:"同じ文字を足すと係数が増えます。"}, {t:"$5a - 2a$", a:"3a", h:"文字の部分はそのままで数字を計算。"} ] }
            ],
            2: [
                { id: '2-1', title: "式の計算", desc: "<div class='point-box'>$2(a + 3b) = 2a + 6b$</div><p>分配法則でカッコを外そう。</p>", examples: "<div class='example-box'><b>例題:</b> $4x - (x - 2y) = 3x + 2y$</div>", q: [ {t:"$3a+5b-a$", a:"2a+5b", h:"a同士をまとめましょう。"}, {t:"$(-2x) \\\\times 4y$", a:"-8xy", h:"数字は数字、文字は文字で。"} ] }
            ],
            3: [
                { id: '3-1', title: "多項式の展開", desc: "<div class='point-box'>$$(x+a)(y+b) = xy + bx + ay + ab$$</div>", examples: "<div class='example-box'><b>例題:</b> $(x+2)(y+3) = xy+3x+2y+6$</div>", q: [ {t:"$(x+1)(y+5)$ の定数項は？", a:"5", h:"$1 \\\\times 5$ の部分です。"}, {t:"$(x-2)(y+4)$ を展開せよ", a:"xy+4x-2y-8", h:"4回順番に掛け算です。"} ] },
                { id: '3-2', title: "因数分解", desc: "<div class='point-box'>$$ax + ay = a(x + y)$$</div>", examples: "<div class='example-box'><b>例題:</b> $4xy + 8x = 4x(y + 2)$</div>", q: [ {t:"$3ax + 6ay$ の共通因数は？", a:"3a", h:"3とaがどちらにもあります。"}, {t:"$x^2 + 2x$ を因数分解せよ", a:"x(x+2)", h:"xを外に出しましょう。"} ] }
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
            container.innerHTML = mathData[g].map(u => `
                <div class="unit-card" onclick="openUnit('${g}', '${u.id}')">
                    <div style="font-size:0.8em; opacity:0.5;">Unit ${u.id}</div>
                    <div style="font-weight:bold; margin-top:5px;">${u.title}</div>
                </div>
            `).join('');
        }

        function openUnit(grade, id) {
            currentUnit = mathData[grade].find(u => u.id === id);
            document.getElementById('lesson-title').innerText = currentUnit.title;
            document.getElementById('lesson-body').innerHTML = currentUnit.desc + currentUnit.examples;
            
            document.getElementById('practice-head').innerHTML = `<h3 style="color:var(--accent);">演習問題</h3>`;
            document.getElementById('practice-body').innerHTML = currentUnit.q.map((question, i) => `
                <div class="q-card">
                    <p><b>Q${i+1}:</b> ${question.t}</p>
                    <input type="text" class="input-field" id="q-ans-${i}" placeholder="答えを入力...">
                </div>
            `).join('');

            document.querySelectorAll('.layer').forEach(l => l.classList.remove('show'));
            document.getElementById('left-lesson').classList.add('show');
            document.getElementById('right-practice').classList.add('show');
            document.getElementById('hint-area').style.display = 'none';
            if (window.MathJax) MathJax.typesetPromise();
        }

        function checkAnswers() {
            let correctCount = 0;
            let feedback = "";
            currentUnit.q.forEach((question, i) => {
                const val = document.getElementById(`q-ans-${i}`).value.trim();
                if (val === question.a) correctCount++;
                else feedback += `<b>Q${i+1}のヒント:</b> ${question.h}<br>`;
            });

            if (correctCount === currentUnit.q.length) {
                alert("✨ Perfect! すみれさん、全問正解です！");
                goHome();
            } else {
                const ha = document.getElementById('hint-area');
                ha.innerHTML = feedback;
                ha.style.display = 'block';
            }
        }

        function goHome() {
            document.querySelectorAll('.layer').forEach(l => l.classList.remove('show'));
            document.getElementById('left-home').classList.add('show');
            document.getElementById('right-list').classList.add('show');
            if (window.MathJax) MathJax.typesetPromise();
        }
    </script>
</body>
</html>
"""
    # 修正ポイント: returnを追加しました
    return HTMLResponse(content=html_content)

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
