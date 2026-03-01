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
    <title>理解保証AI型授業 - 完全版</title>
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
            --page-w: 520px; --book-h: 750px;
        }
        body, html {
            margin: 0; padding: 0; width: 100%; height: 100vh;
            display: flex; justify-content: center; align-items: center;
            background: #010208; font-family: "Hiragino Sans", sans-serif; color: white; overflow: hidden;
        }
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
        .choice-btn { background: rgba(255,255,255,0.08); border: 1px solid var(--border); color: white; padding: 10px 20px; border-radius: 8px; cursor: pointer; margin: 5px; transition: 0.2s; }
        .choice-btn.selected { background: var(--accent); color: black; font-weight: bold; }
        .index-item { background: rgba(255,255,255,0.06); padding: 25px; border-radius: 20px; margin-bottom: 15px; cursor: pointer; border: 1px solid transparent; transition: 0.3s; }
        .index-item:hover { border-color: var(--accent); background: rgba(0,210,255,0.1); }
        #hint-display { display: none; color: #f7b731; font-size: 14px; margin-top: 15px; padding: 15px; background: rgba(247, 183, 49, 0.1); border-radius: 10px; border: 1px solid rgba(247, 183, 49, 0.3); line-height: 1.6; }
    </style>
</head>
<body>
    <div class="liquid-bg"></div>
    <div id="login-screen">
        <div class="login-glass">
            <h2 style="letter-spacing:2px;">理解保証AI型授業</h2>
            <p style="opacity:0.7;">すみれさん、ログインしてください</p>
            <input type="email" class="login-input" placeholder="メールアドレス">
            <input type="password" class="login-input" placeholder="パスワード">
            <button class="btn-action" onclick="launch()">ログイン</button>
        </div>
    </div>

    <div class="scene" id="scene">
        <div class="page-panel">
            <div id="left-default" class="layer show">
                <p style="color:var(--accent); font-weight:bold;">CHAPTER 01</p>
                <h1 style="font-size:40px;">数と式</h1>
                <p style="opacity:0.8; line-height:1.8;">すみれさん、こんにちは！<br>今日は数学の基礎となる「展開」と「因数分解」をマスターしましょう。公式の意味を左ページで理解して、右ページで解いていきます。</p>
            </div>
            <div id="left-content" class="layer">
                <h2 id="unit-title-display" style="color:var(--accent); font-size:28px;"></h2>
                <div id="unit-description"></div>
            </div>
        </div>

        <div class="page-panel">
            <div id="right-default" class="layer show">
                <h3 style="font-weight:200; margin-bottom:20px;">学習カリキュラム</h3>
                <div class="index-item" onclick="loadUnit('unit1')">
                    <b style="color:var(--accent);">01</b> 多項式の展開（x, y 変数）
                </div>
                <div class="index-item" onclick="loadUnit('unit2')">
                    <b style="color:var(--accent);">02</b> 因数分解の基本（共通因数）
                </div>
            </div>
            <div id="right-content" class="layer">
                <div id="unit-examples"></div>
                <div style="height:1px; background:var(--border); margin:25px 0;"></div>
                <div id="exercise-flow"></div>
                <button class="btn-action" onclick="judgeScore()">採点して判定する</button>
                <div id="hint-display"></div>
                <p onclick="goHome()" style="color:var(--accent); cursor:pointer; text-align:center; margin-top:25px; font-size:14px; text-decoration:underline;">目次に戻る</p>
            </div>
        </div>
    </div>

    <script>
        let selectedChoice = null;
        let currentUnit = null;

        const unitData = {
            unit1: { 
                title: "多項式の展開", 
                desc: "<h3>基本公式</h3><div class='point-box'>$$(x+a)(y+b) = xy + bx + ay + ab$$</div><p><b>解説:</b> 4つの掛け算を順番に行う「分配法則」が基本です。符号（プラス・マイナス）のミスに気をつけましょう！</p>",
                examples: "<h3>例題と類題</h3><div class='example-box'><b>例題:</b> $(x+3)(y+5)$ を展開せよ<br>→ $xy + 5x + 3y + 15$</div><div class='example-box'><b>類題:</b> $(x-2)(y+4)$ を展開せよ<br>→ $xy + 4x - 2y - 8$</div>",
                q1: { txt: "$(x+4)(y+2)$ を展開したとき、$x$ の係数は？", choices: [2, 4, 8], ans: "2", feedback: "展開すると $xy + 2x + 4y + 8$ となります。$x$ の前にある数字は 2 ですね。" },
                q2: { txt: "$(x-5)(y+3)$ を展開せよ (半角英数)", ans: "xy+3x-5y-15", feedback: "分配法則で4回掛けます。$-5 \\times 3 = -15$ になる部分がポイントです。" },
                q3: { txt: "$(x-2)(y-4)$ の定数項は？", ans: "8", feedback: "定数項は数字だけの掛け算です。$-2 \\times -4 = +8$ となります。" }
            },
            unit2: {
                title: "因数分解の基本", 
                desc: "<h3>基本公式</h3><div class='point-box'>$$ax + ay = a(x + y)$$</div><p><b>解説:</b> 各項に共通して含まれている「共通因数」を見つけ出し、カッコの外に括りだす作業です。展開の逆の動きですね。</p>",
                examples: "<h3>例題と類題</h3><div class='example-box'><b>例題:</b> $3xy + 6x$ を因数分解せよ<br>→ $3x(y + 2)$</div><div class='example-box'><b>類題:</b> $x^2y - xy$ を因数分解せよ<br>→ $xy(x - 1)$</div>",
                q1: { txt: "$5xy + 10x$ の共通因数は？", choices: ["5x", "5", "x"], ans: "5x", feedback: "5と10はどちらも5で割れ、xも共通しています。" },
                q2: { txt: "$xy + 2x - 3y - 6$ を因数分解せよ", ans: "(x-3)(y+2)", feedback: "前2つを $x$ で、後ろ2つを $-3$ で括ると $(y+2)$ が共通して現れます。" },
                q3: { txt: "$2xy - 4y$ を因数分解したカッコ内は？ (2yを外に出す)", ans: "x-2", feedback: "$2y \\times x$ と $2y \\times (-2)$ に分解できます。" }
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
                <h3 style='margin-bottom:15px;'>演習問題</h3>
                <div class='q-card'><b>問1:</b> ${currentUnit.q1.txt}<br>
                ${currentUnit.q1.choices.map(c => `<button class='choice-btn' onclick='selectC(this, "${c}")'>${c}</button>`).join('')}</div>
                <div class='q-card'><b>問2:</b> ${currentUnit.q2.txt}<br><input id='ans2' class='login-input' placeholder='答えを入力...'></div>
                <div class='q-card'><b>問3:</b> ${currentUnit.q3.txt}<br><input id='ans3' class='login-input' placeholder='答えを入力...'></div>
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
            const a2 = document.getElementById('ans2').value.trim().replace(/\\s/g, "");
            const a3 = document.getElementById('ans3').value.trim();

            if(String(selectedChoice) === String(currentUnit.q1.ans)) score += 34; 
            else msg += "<b>【問1のヒント】</b>" + currentUnit.q1.feedback + "<br>";

            if(a2 === currentUnit.q2.ans) score += 33; 
            else msg += "<b>【問2のヒント】</b>" + currentUnit.q2.feedback + "<br>";

            if(a3 === String(currentUnit.q3.ans)) score += 33; 
            else msg += "<b>【問3のヒント】</b>" + currentUnit.q3.feedback + "<br>";

            const hd = document.getElementById('hint-display');
            if(score >= 80) { 
                alert("🎉 合格！すみれさん、すごいです！"); 
                goHome(); 
            } else { 
                hd.innerHTML = "<b>スコア: " + score + "% - もう少し！</b><br>" + msg;
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
