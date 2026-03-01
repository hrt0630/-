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
    <title>理解保証AI型授業 - 教科書Edition</title>
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
            --accent: #00d2ff; --border: rgba(255, 255, 255, 0.15);
            --page-w: 520px; --book-h: 700px;
        }
        body, html {
            margin: 0; padding: 0; width: 100%; height: 100vh;
            display: flex; justify-content: center; align-items: center;
            background: #010208; font-family: "Hiragino Sans", sans-serif; color: white; overflow: hidden;
        }
        .liquid-bg { position: fixed; inset: 0; z-index: -1; background: linear-gradient(135deg, #050a30 0%, #000000 50%, #1a0033 100%); }
        #login-screen { position: fixed; inset: 0; z-index: 5000; display: flex; justify-content: center; align-items: center; background: rgba(1, 2, 8, 0.7); backdrop-filter: blur(60px); }
        .login-glass { background: rgba(255, 255, 255, 0.04); padding: 50px; border-radius: 40px; border: 1px solid var(--border); width: 400px; text-align: center; }
        .scene { display: flex; gap: 10px; width: 1060px; height: var(--book-h); opacity: 0; transition: 1s; }
        .scene.active { opacity: 1; }
        .page-panel { flex: 1; background: rgba(255, 255, 255, 0.03); border: 1px solid var(--border); backdrop-filter: blur(40px); padding: 40px; display: flex; flex-direction: column; overflow-y: auto; border-radius: 24px; }
        .layer { display: none; } .layer.show { display: block; }
        .point-box { background: rgba(0, 210, 255, 0.08); border: 1px solid var(--accent); border-radius: 12px; padding: 20px; margin: 15px 0; border-left: 5px solid var(--accent); }
        .example-box { background: rgba(255,255,255,0.05); padding: 15px; border-radius: 10px; border: 1px dashed #aaa; margin: 10px 0; font-size: 14px; }
        .btn-action { width: 100%; height: 55px; border-radius: 15px; background: white; color: #010208; font-weight: 900; border: none; cursor: pointer; margin-top: 10px; }
        .login-input { width: 100%; height: 50px; border-radius: 12px; border: 1px solid var(--border); background: rgba(255,255,255,0.08); color: white; padding: 0 15px; margin-bottom: 10px; box-sizing: border-box; }
        .q-card { background: rgba(255,255,255,0.05); padding: 15px; border-radius: 12px; margin-bottom: 15px; border-left: 4px solid var(--accent); }
        .choice-btn { background: rgba(255,255,255,0.08); border: 1px solid var(--border); color: white; padding: 8px 15px; border-radius: 6px; cursor: pointer; margin: 4px; }
        .choice-btn.selected { background: var(--accent); color: black; }
        .index-item { background: rgba(255,255,255,0.06); padding: 20px; border-radius: 15px; margin-bottom: 12px; cursor: pointer; }
        #hint-display { display: none; color: #f7b731; font-size: 13px; margin-top: 10px; padding: 10px; background: rgba(247, 183, 49, 0.1); border-radius: 8px; }
    </style>
</head>
<body>
    <div class="liquid-bg"></div>
    <div id="login-screen">
        <div class="login-glass">
            <h2>理解保証AI型授業</h2>
            <p>すみれさん、ログインしてください</p>
            <input type="email" class="login-input" placeholder="メールアドレス">
            <input type="password" class="login-input" placeholder="パスワード">
            <button class="btn-action" onclick="launch()">ログイン</button>
        </div>
    </div>

    <div class="scene" id="scene">
        <div class="page-panel">
            <div id="left-default" class="layer show">
                <p style="color:var(--accent);">CHAPTER 01</p>
                <h1>数と式</h1>
                <p>左ページで基本を学び、右ページで問題を解くスタイルです。</p>
            </div>
            <div id="left-content" class="layer">
                <h2 id="unit-title-display" style="color:var(--accent);"></h2>
                <div id="unit-description"></div>
            </div>
        </div>

        <div class="page-panel">
            <div id="right-default" class="layer show">
                <h3>学習カリキュラム</h3>
                <div class="index-item" onclick="loadUnit('unit1')">01 多項式の展開</div>
                <div class="index-item" onclick="loadUnit('unit2')">02 因数分解の基本</div>
            </div>
            <div id="right-content" class="layer">
                <div id="unit-examples"></div>
                <hr style="border:0; border-top:1px solid var(--border); margin:20px 0;">
                <div id="exercise-flow"></div>
                <button class="btn-action" onclick="judgeScore()">採点する</button>
                <div id="hint-display"></div>
                <p onclick="goHome()" style="color:var(--accent); cursor:pointer; text-align:center; margin-top:20px; font-size:14px;">目次に戻る</p>
            </div>
        </div>
    </div>

    <script>
        let selectedChoice = null;
        let currentUnit = null;

        const unitData = {
            unit1: { 
                title: "多項式の展開", 
                desc: "<h3>基本公式</h3><div class='point-box'>$$(x+a)(y+b) = xy + bx + ay + ab$$</div><p>すべての項を1つずつ掛け合わせる「分配法則」を使います。</p>",
                examples: "<h3>例題・類題</h3><div class='example-box'><b>例題:</b> $(x+3)(y+5)$ を展開せよ<br>解: $xy + 5x + 3y + 15$</div><div class='example-box'><b>類題:</b> $(x-2)(y+4)$ を展開せよ<br>解: $xy + 4x - 2y - 8$</div>",
                q1: { txt: "$(x+4)(y+2)$ の $x$ の係数は？", choices: [2, 4, 8], ans: "2", feedback: "展開すると $2x$ が出てきます。" },
                q2: { txt: "$(x-5)(y+3)$ を展開せよ", ans: "xy+3x-5y-15", feedback: "$-5 \\times 3 = -15$ です。" },
                q3: { txt: "$(x-2)(y-4)$ の定数項は？", ans: "8", feedback: "$-2 \\times -4 = 8$ です。" }
            },
            unit2: {
                title: "因数分解の基本", 
                desc: "<h3>基本公式</h3><div class='point-box'>$$ax + ay = a(x + y)$$</div><p>共通する「共通因数」をカッコの外にくくりだします。</p>",
                examples: "<h3>例題・類題</h3><div class='example-box'><b>例題:</b> $3xy + 6x$ を因数分解せよ<br>解: $3x(y + 2)$</div><div class='example-box'><b>類題:</b> $x^2y - xy$ を因数分解せよ<br>解: $xy(x - 1)$</div>",
                q1: { txt: "$5xy + 10x$ の共通因数は？", choices: ["5x", "5", "x"], ans: "5x", feedback: "5とxが共通しています。" },
                q2: { txt: "$xy + 2x - 3y - 6$ を因数分解せよ", ans: "(x-3)(y+2)", feedback: "共通の塊 $(y+2)$ を作ります。" },
                q3: { txt: "$2xy - 4y$ を因数分解したカッコ内は？", ans: "x-2", feedback: "$2y(x-2)$ になります。" }
            }
        };

        function refreshMath() { if (window.MathJax) { MathJax.typesetPromise(); } }

        function launch() { 
            document.getElementById('login-screen').style.display = 'none'; 
            document.getElementById('scene').classList.add('active'); 
            refreshMath();
        }

        function loadUnit(id) {
            currentUnit = unitData[id];
            selectedChoice = null;
            document.getElementById('unit-title-display').innerText = currentUnit.title;
            document.getElementById('unit-description').innerHTML = currentUnit.desc;
            document.getElementById('unit-examples').innerHTML = currentUnit.examples;
            
            document.getElementById('exercise-flow').innerHTML = `
                <h3>演習問題</h3>
                <div class='q-card'><b>問1:</b> ${currentUnit.q1.txt}<br>
                ${currentUnit.q1.choices.map(c => `<button class='choice-btn' onclick='selectC(this, "${c}")'>${c}</button>`).join('')}</div>
                <div class='q-card'><b>問2:</b> ${currentUnit.q2.txt}<br><input id='ans2' class='login-input'></div>
                <div class='q-card'><b>問3:</b> ${currentUnit.q3.txt}<br><input id='ans3' class='login-input'></div>
            `;

            document.querySelectorAll('.layer').forEach(l => l.classList.remove('show'));
            document.getElementById('left-content').classList.add('show');
            document.getElementById('right-content').classList.add('show');
            document.getElementById('hint-display').style.display = 'none';
            refreshMath();
        }

        function selectC(btn, val) {
            document.querySelectorAll('.choice-btn').forEach(b => b.classList.remove('selected'));
            btn.classList.add('selected');
            selectedChoice = val;
        }

        function judgeScore() {
            let score = 0; let msg = "";
            const a2 = document.getElementById('ans2').value.trim();
            const a3 = document.getElementById('ans3').value.trim();
            if(String(selectedChoice) === String(currentUnit.q1.ans)) score += 34; else msg += "問1: " + currentUnit.q1.feedback + "<br>";
            if(a2 === currentUnit.q2.ans) score += 33; else msg += "問2: " + currentUnit.q2.feedback + "<br>";
            if(a3 === String(currentUnit.q3.ans)) score += 33; else msg += "問3: " + currentUnit.q3.feedback + "<br>";

            if(score >= 80) { alert("合格！"); goHome(); }
            else { 
                const hd = document.getElementById('hint-display');
                hd.innerHTML = "スコア: " + score + "<br>" + msg;
                hd.style.display = 'block';
                refreshMath();
            }
        }

        function goHome() {
            document.querySelectorAll('.layer').forEach(l => l.classList.remove('show'));
            document.getElementById('left-default').classList.add('show');
            document.getElementById('right-default').classList.add('show');
            refreshMath();
        }
    </script>
</body>
</html>
