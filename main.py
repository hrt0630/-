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
    <title>理解保証AI型授業 - 中学数学全単元コンプリート</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no, viewport-fit=cover">
    <script>
        window.MathJax = {
            tex: { inlineMath: [['$', '$']], displayMath: [['$$', '$$']] },
            chtml: { displayAlign: 'center' }
        };
    </script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <style>
        :root { --accent: #00d2ff; --border: rgba(255, 255, 255, 0.15); --page-w: 520px; --book-h: 850px; }
        body, html { margin: 0; padding: 0; width: 100%; height: 100vh; display: flex; justify-content: center; align-items: center; background: #010208; font-family: "Hiragino Sans", sans-serif; color: white; overflow: hidden; }
        .liquid-bg { position: fixed; inset: 0; z-index: -1; background: linear-gradient(135deg, #050a30 0%, #000000 50%, #1a0033 100%); }
        #login-screen { position: fixed; inset: 0; z-index: 5000; display: flex; justify-content: center; align-items: center; background: rgba(1, 2, 8, 0.7); backdrop-filter: blur(60px); }
        .login-glass { background: rgba(255, 255, 255, 0.04); padding: 50px; border-radius: 40px; border: 1px solid var(--border); width: 400px; text-align: center; }
        .scene { display: flex; gap: 15px; width: 1080px; height: var(--book-h); opacity: 0; transition: 1s; }
        .scene.active { opacity: 1; }
        .page-panel { flex: 1; background: rgba(255, 255, 255, 0.03); border: 1px solid var(--border); backdrop-filter: blur(40px); padding: 40px; display: flex; flex-direction: column; overflow-y: auto; border-radius: 24px; box-shadow: 0 20px 50px rgba(0,0,0,0.5); }
        .layer { display: none; } .layer.show { display: block; }
        .point-box { background: rgba(0, 210, 255, 0.08); border: 1px solid var(--accent); border-radius: 12px; padding: 20px; margin: 15px 0; border-left: 5px solid var(--accent); }
        .example-box { background: rgba(255,255,255,0.05); padding: 18px; border-radius: 12px; border: 1px dashed rgba(255,255,255,0.3); margin: 12px 0; font-size: 14px; line-height: 1.6; }
        .btn-action { width: 100%; height: 55px; border-radius: 15px; background: white; color: #010208; font-weight: 900; border: none; cursor: pointer; margin-top: 15px; transition: 0.3s; }
        .btn-action:hover { background: var(--accent); color: white; transform: translateY(-2px); }
        .login-input { width: 100%; height: 50px; border-radius: 12px; border: 1px solid var(--border); background: rgba(255,255,255,0.08); color: white; padding: 0 15px; margin-bottom: 10px; box-sizing: border-box; }
        .q-card { background: rgba(255,255,255,0.05); padding: 20px; border-radius: 15px; margin-bottom: 15px; border-left: 4px solid var(--accent); }
        .choice-btn { background: rgba(255,255,255,0.08); border: 1px solid var(--border); color: white; padding: 10px 20px; border-radius: 8px; cursor: pointer; margin: 5px; }
        .choice-btn.selected { background: var(--accent); color: black; font-weight: bold; }
        .index-item { background: rgba(255,255,255,0.06); padding: 15px; border-radius: 12px; margin-bottom: 10px; cursor: pointer; border: 1px solid transparent; transition: 0.2s; font-size: 14px; }
        .index-item:hover { border-color: var(--accent); background: rgba(0,210,255,0.1); }
        .grade-tab { display: flex; gap: 10px; margin-bottom: 20px; }
        .tab-btn { flex: 1; padding: 10px; background: rgba(255,255,255,0.1); border: 1px solid var(--border); color: white; border-radius: 8px; cursor: pointer; }
        .tab-btn.active { background: var(--accent); color: black; font-weight: bold; }
        #hint-display { display: none; color: #f7b731; font-size: 14px; margin-top: 15px; padding: 15px; background: rgba(247, 183, 49, 0.1); border-radius: 10px; border: 1px solid rgba(247, 183, 49, 0.3); }
    </style>
</head>
<body>
    <div class="liquid-bg"></div>
    <div id="login-screen"><div class="login-glass"><h2>理解保証AI型授業</h2><p>すみれさん、ログインしてください</p><input type="email" class="login-input" placeholder="メールアドレス"><input type="password" class="login-input" placeholder="パスワード"><button class="btn-action" onclick="launch()">ログイン</button></div></div>

    <div class="scene" id="scene">
        <div class="page-panel">
            <div id="left-default" class="layer show">
                <p style="color:var(--accent); font-weight:bold;">COMPREHENSIVE CURRICULUM</p>
                <h1 style="font-size:36px;">中学数学 全学年</h1>
                <p style="opacity:0.8; line-height:1.6;">1年生から3年生までの全単元を収録しました。左側の解説を読み、右側の問題に挑戦しましょう。</p>
            </div>
            <div id="left-content" class="layer">
                <h2 id="unit-title-display" style="color:var(--accent);"></h2>
                <div id="unit-description"></div>
            </div>
        </div>

        <div class="page-panel">
            <div id="right-default" class="layer show">
                <div class="grade-tab">
                    <button class="tab-btn active" onclick="switchGrade(1)">中1</button>
                    <button class="tab-btn" onclick="switchGrade(2)">中2</button>
                    <button class="tab-btn" onclick="switchGrade(3)">中3</button>
                </div>
                <div id="curriculum-list"></div>
            </div>
            <div id="right-content" class="layer">
                <div id="unit-examples"></div>
                <div style="height:1px; background:var(--border); margin:20px 0;"></div>
                <div id="exercise-flow"></div>
                <button class="btn-action" onclick="judgeScore()">採点して判定する</button>
                <div id="hint-display"></div>
                <p onclick="goHome()" style="color:var(--accent); cursor:pointer; text-align:center; margin-top:20px; font-size:14px;">目次に戻る</p>
            </div>
        </div>
    </div>

    <script>
        let selectedChoice = null; let currentUnit = null; let currentGrade = 1;

        const allData = {
            1: [
                { id: 'm1_1', title: "正の数・負の数", desc: "<div class='point-box'>$(-3) \\times (-2) = +6$</div><p>同じ符号ならプラス、違う符号ならマイナス！</p>", examples: "<div class='example-box'><b>例題:</b> $(-5) + (+2) = -3$</div>", q1: { txt: "$(-8) \\div (-2)$ の答えは？", choices: [4, -4, 16], ans: "4", feedback: "マイナス同士の割り算はプラスになります。" }, q2: { txt: "$(-3)^2$ を計算せよ", ans: "9", feedback: "$(-3) \\times (-3)$ です。" }, q3: { txt: "$5 - (-2)$ は？", ans: "7", feedback: "引き算のマイナスは足し算に変わります。" } },
                { id: 'm1_2', title: "文字の式", desc: "<div class='point-box'>$3a + 2a = 5a$</div><p>同じ文字の仲間（同類項）をまとめます。</p>", examples: "<div class='example-box'><b>例題:</b> $5x - 3x = 2x$</div>", q1: { txt: "$4a \\times 3$ は？", choices: ["12a", "7a", "12"], ans: "12a", feedback: "数字の部分を掛け算します。" }, q2: { txt: "$2(x+4)$ を展開せよ", ans: "2x+8", feedback: "2をxと4の両方に掛けます。" }, q3: { txt: "$x=3$のとき$2x+5$の値は？", ans: "11", feedback: "$2 \\times 3 + 5$ です。" } }
            ],
            2: [
                { id: 'm2_1', title: "連立方程式", desc: "<div class='point-box'>代入法と加減法</div><p>2つの文字を1つ消去するのがコツです。</p>", examples: "<div class='example-box'>$x+y=5, x-y=1 \\rightarrow 2x=6, x=3$</div>", q1: { txt: "$x+y=10, x=3$のとき$y$は？", choices: [7, 13, 3], ans: "7", feedback: "xに3を代入します。" }, q2: { txt: "$2x=6$ の $x$ は？", ans: "3", feedback: "両辺を2で割ります。" }, q3: { txt: "$x+y=2, x=y$のときxは？", ans: "1", feedback: "$y+y=2$より$2y=2$です。" } },
                { id: 'm2_2', title: "一次関数", desc: "<div class='point-box'>$y = ax + b$</div><p>aは傾き（変化の割合）、bは切片です。</p>", examples: "<div class='example-box'>$y=2x+3$ なら、切片は3。</div>", q1: { txt: "$y=3x+2$ の傾きは？", choices: [3, 2, 5], ans: "3", feedback: "xの係数が傾きです。" }, q2: { txt: "$y=x+5$で$x=2$のときのyは？", ans: "7", feedback: "$2+5$です。" }, q3: { txt: "$y=2x+b$が(0,4)を通るときbは？", ans: "4", feedback: "x=0のときのyの値が切片bです。" } }
            ],
            3: [
                { id: 'unit1', title: "多項式の展開", desc: "<div class='point-box'>$$(x+a)(y+b) = xy + bx + ay + ab$$</div><p>順番に掛ける分配法則が基本！</p>", examples: "<div class='example-box'><b>例題:</b> $(x+3)(y+5) = xy+5x+3y+15$</div>", q1: { txt: "$(x+4)(y+2)$ の $x$ の係数は？", choices: [2, 4, 8], ans: "2", feedback: "展開すると $2x$ が出ます。" }, q2: { txt: "$(x-5)(y+3)$ を展開せよ", ans: "xy+3x-5y-15", feedback: "$-5 \\times 3 = -15$ に注意。" }, q3: { txt: "$(x-2)(y-4)$ の定数項は？", ans: "8", feedback: "$-2 \\times -4 = 8$ です。" } },
                { id: 'unit2', title: "因数分解の基本", desc: "<div class='point-box'>$$ax + ay = a(x + y)$$</div><p>共通因数を外に出します。</p>", examples: "<div class='example-box'><b>例題:</b> $3xy+6x = 3x(y+2)$</div>", q1: { txt: "$5xy+10x$ の共通因数は？", choices: ["5x", "5", "x"], ans: "5x", feedback: "5とxが共通しています。" }, q2: { txt: "$xy+2x-3y-6$ を因数分解せよ", ans: "(x-3)(y+2)", feedback: "塊 $(y+2)$ を作ります。" }, q3: { txt: "$2xy-4y$ の共通因数 2y を出したカッコ内は？", ans: "x-2", feedback: "$2y(x-2)$ になります。" } }
            ]
        };

        function switchGrade(g) {
            currentGrade = g;
            document.querySelectorAll('.tab-btn').forEach((b, i) => b.classList.toggle('active', i+1 === g));
            const list = document.getElementById('curriculum-list');
            list.innerHTML = allData[g].map(u => `<div class='index-item' onclick='loadUnitById("${u.id}")'>${u.title}</div>`).join('');
        }

        function loadUnitById(id) {
            currentUnit = allData[currentGrade].find(u => u.id === id);
            selectedChoice = null;
            document.getElementById('unit-title-display').innerText = currentUnit.title;
            document.getElementById('unit-description').innerHTML = currentUnit.desc;
            document.getElementById('unit-examples').innerHTML = currentUnit.examples;
            document.getElementById('exercise-flow').innerHTML = `<h3>演習問題</h3><div class='q-card'><b>問1:</b> ${currentUnit.q1.txt}<br>${currentUnit.q1.choices.map(c => `<button class='choice-btn' onclick='selectC(this, "${c}")'>${c}</button>`).join('')}</div><div class='q-card'><b>問2:</b> ${currentUnit.q2.txt}<br><input id='ans2' class='login-input'></div><div class='q-card'><b>問3:</b> ${currentUnit.q3.txt}<br><input id='ans3' class='login-input'></div>`;
            document.querySelectorAll('.layer').forEach(l => l.classList.remove('show'));
            document.getElementById('left-content').classList.add('show');
            document.getElementById('right-content').classList.add('show');
            document.getElementById('hint-display').style.display = 'none';
            refreshMath();
        }

        function refreshMath() { if (window.MathJax) { MathJax.typesetPromise(); } }
        function launch() { document.getElementById('login-screen').style.display = 'none'; document.getElementById('scene').classList.add('active'); switchGrade(1); }
        function selectC(btn, val) { document.querySelectorAll('.choice-btn').forEach(b => b.classList.remove('selected')); btn.classList.add('selected'); selectedChoice = val; }
        function judgeScore() {
            let score = 0; let msg = "";
            const a2 = document.getElementById('ans2').value.trim(); const a3 = document.getElementById('ans3').value.trim();
            if(String(selectedChoice) === String(currentUnit.q1.ans)) score += 34; else msg += "問1: " + currentUnit.q1.feedback + "<br>";
            if(a2 === currentUnit.q2.ans) score += 33; else msg += "問2: " + currentUnit.q2.feedback + "<br>";
            if(a3 === String(currentUnit.q3.ans)) score += 33; else msg += "問3: " + currentUnit.q3.feedback + "<br>";
            const hd = document.getElementById('hint-display');
            if(score >= 80) { alert("合格！"); goHome(); } else { hd.innerHTML = "スコア: " + score + "<br>" + msg; hd.style.display = 'block'; refreshMath(); }
        }
        function goHome() { document.querySelectorAll('.layer').forEach(l => l.classList.remove('show')); document.getElementById('left-default').classList.add('show'); document.getElementById('right-default').classList.add('show'); }
    </script>
</body>
</html>
"""
    return HTMLResponse(content=html_content)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
