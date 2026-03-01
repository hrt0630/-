from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

@app.get("/ui", response_class=HTMLResponse)
def ui():
    # すみれさん専用のアプリ画面（HTML/CSS/JS）
    html_content = """
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>理解保証AI型授業 - x & y Edition</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no, viewport-fit=cover">
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <style>
        :root {
            --accent: #00d2ff; --purple-glow: #7000ff; --border: rgba(255, 255, 255, 0.15);
            --page-w: 520px; --book-h: 700px;
        }
        body, html {
            margin: 0; padding: 0; width: 100%; height: 100vh;
            display: flex; justify-content: center; align-items: center;
            background: #010208; font-family: "Hiragino Sans", sans-serif; color: white; overflow: hidden;
        }
        .liquid-bg { position: fixed; inset: 0; z-index: -1; background: linear-gradient(135deg, #050a30 0%, #000000 50%, #1a0033 100%); }
        #login-screen { position: fixed; inset: 0; z-index: 5000; display: flex; justify-content: center; align-items: center; background: rgba(1, 2, 8, 0.7); backdrop-filter: blur(60px); transition: 1s; }
        .login-glass { background: rgba(255, 255, 255, 0.04); padding: 50px; border-radius: 40px; border: 1px solid var(--border); width: 420px; text-align: center; }
        .scene { display: flex; gap: 8px; width: calc(var(--page-w) * 2); height: var(--book-h); opacity: 0; transition: 1.2s; position: relative; z-index: 10; pointer-events: none; }
        .scene.active { opacity: 1; pointer-events: auto; }
        .page-panel { flex: 1; background: rgba(255, 255, 255, 0.03); border: 1px solid var(--border); backdrop-filter: blur(45px); padding: 55px; box-sizing: border-box; display: flex; flex-direction: column; position: relative; overflow-y: auto; border-radius: 20px; }
        .layer { display: none; opacity: 0; transition: 0.6s; }
        .layer.show { display: block; opacity: 1; }
        .point-box { background: rgba(0, 210, 255, 0.08); border: 1px solid var(--accent); border-radius: 15px; padding: 25px; margin: 20px 0; border-left: 5px solid var(--accent); }
        .btn-action { width: 100%; height: 60px; border-radius: 18px; background: white; color: #010208; font-weight: 900; border: none; cursor: pointer; transition: 0.3s; margin-top: 10px; }
        .btn-action:hover { background: var(--accent); color: white; }
        .login-input { width: 100%; height: 55px; border-radius: 15px; border: 1px solid var(--border); background: rgba(255,255,255,0.08); color: white; padding: 0 20px; margin-bottom: 12px; box-sizing: border-box; outline: none; }
        .q-card { background: rgba(255,255,255,0.05); padding: 20px; border-radius: 15px; margin-bottom: 15px; border-left: 4px solid var(--accent); }
        .choice-btn { background: rgba(255,255,255,0.08); border: 1px solid var(--border); color: white; padding: 10px; border-radius: 8px; cursor: pointer; margin: 4px; transition: 0.2s; }
        .choice-btn.selected { background: var(--accent); color: black; }
        .index-item { background: rgba(255,255,255,0.06); padding: 25px; border-radius: 20px; margin-bottom: 18px; cursor: pointer; transition: 0.3s; border: 1px solid transparent; }
        .index-item:hover { background: rgba(0, 210, 255, 0.1); border-color: var(--accent); }
        #hint-display { display: none; color: #f7b731; font-size: 13px; margin-top: 10px; padding: 10px; background: rgba(247, 183, 49, 0.1); border-radius: 8px; }
    </style>
</head>
<body>
    <div class="liquid-bg"></div>
    <div id="login-screen">
        <div class="login-glass">
            <h2 style="font-family: 'Hiragino Sans'; font-weight: 200;">理解保証AI型授業</h2>
            <p style="opacity: 0.7;">すみれさん、ログインしてください</p>
            <input type="email" class="login-input" placeholder="メールアドレス">
            <input type="password" class="login-input" placeholder="パスワード">
            <button class="btn-action" onclick="launch()">ログイン</button>
        </div>
    </div>

    <div class="scene" id="scene">
        <div class="page-panel">
            <div id="left-default" class="layer show">
                <p style="color: var(--accent); font-weight: bold; letter-spacing: 2px;">CHAPTER 01</p>
                <h1 style="font-size: 45px;">数と式</h1>
                <p style="opacity: 0.6; line-height: 1.8;">すみれさん、今日は「展開」と「因数分解」をマスターしましょう。基礎から丁寧に解説します。</p>
            </div>
            <div id="left-content" class="layer">
                <h2 id="unit-title-display" style="color: var(--accent);"></h2>
                <div id="unit-description"></div>
            </div>
        </div>
        <div class="page-panel">
            <div id="right-default" class="layer show">
                <h3 style="font-weight: 200; margin-bottom: 30px;">学習カリキュラム</h3>
                <div class="index-item" onclick="loadUnit('unit1')">01 多項式の展開（x, y 変数）</div>
                <div class="index-item" onclick="loadUnit('unit2')">02 因数分解の基本</div>
            </div>
            <div id="right-exercise" class="layer">
                <div id="exercise-flow"></div>
                <button class="btn-action" onclick="judgeScore()">採点する</button>
                <div id="hint-display"></div>
                <p onclick="goHome()" style="color:var(--accent); cursor:pointer; text-align:center; margin-top:20px; font-size: 14px;">目次に戻る</p>
            </div>
        </div>
    </div>

    <script>
        let selectedChoice = null;
        let currentUnit = null;

        const unitData = {
            unit1: { 
                title: "多項式の展開", 
                desc: "<div class='point-box'>$$(x+a)(y+b) = xy + bx + ay + ab$$</div><p>全ての項を順番に掛け合わせるのがコツです。</p>",
                q1: { txt: "$(x+4)(y+2)$ を展開したとき、$x$ の係数は？", choices: [2, 4, 8, 1], ans: "2", feedback: "展開すると $xy + 2x + 4y + 8$ となります。$x$ の前にある数字を確認しましょう。" },
                q2: { txt: "$(x-5)(y+3)$ を展開せよ (半角英数)", ans: "xy+3x-5y-15", feedback: "分配法則で4回掛けます。$-5$ と $3$ の掛け算に注意。" },
                q3: { txt: "$(x-2)(y-4)$ の定数項は？", ans: "8", feedback: "定数項は数字だけの掛け算です。$-2 \\times -4 = 8$ ですね。" }
            },
            unit2: {
                title: "因数分解の基本",
                desc: "<div class='point-box'>$$ax + ay = a(x + y)$$</div><p>共通している「共通因数」を見つけ出して、カッコの外に出します。</p>",
                q1: { txt: "$5xy + 10x$ の共通因数は？", choices: ["5x", "5", "x", "10x"], ans: "5x", feedback: "5と10はどちらも5で割れ、どちらの項にもxが含まれています。" },
                q2: { txt: "$xy + 2x - 3y - 6$ を因数分解せよ", ans: "(x-3)(y+2)", feedback: "前2つをxで、後ろ2つを-3でくくってみましょう。" },
                q3: { txt: "$2xy - 4y$ を因数分解したカッコ内は？ (2yを出した場合)", ans: "x-2", feedback: "各項を2yで割ると、x と -2 が残ります。" }
            }
        };

        function launch() { 
            document.getElementById('login-screen').style.opacity = '0';
            setTimeout(() => {
                document.getElementById('login-screen').style.display = 'none'; 
                document.getElementById('scene').classList.add('active'); 
            }, 800);
        }

        function loadUnit(id) {
            currentUnit = unitData[id];
            selectedChoice = null;
            document.getElementById('unit-title-display').innerText = currentUnit.title;
            document.getElementById('unit-description').innerHTML = currentUnit.desc;
            
            document.getElementById('exercise-flow').innerHTML = `
                <div class='q-card'><b>問1: </b>${currentUnit.q1.txt}<br>
                <div style='margin-top:10px;'>${currentUnit.q1.choices.map(c => `<button class='choice-btn' onclick='selectC(this, "${c}")'>${c}</button>`).join('')}</div></div>
                <div class='q-card'><b>問2: </b>${currentUnit.q2.txt}<br><input id='ans2' class='login-input' style='height:45px; margin-top:10px;'></div>
                <div class='q-card'><b>問3: </b>${currentUnit.q3.txt}<br><input id='ans3' class='login-input' style='height:45px; margin-top:10px;'></div>
            `;

            document.querySelectorAll('.layer').forEach(l => l.classList.remove('show'));
            document.getElementById('left-content').classList.add('show');
            document.getElementById('right-exercise').classList.add('show');
            document.getElementById('hint-display').style.display = 'none';
            if(window.MathJax) MathJax.typesetPromise();
        }

        function selectC(btn, val) {
            document.querySelectorAll('.choice-btn').forEach(b => b.classList.remove('selected'));
            btn.classList.add('selected');
            selectedChoice = val;
        }

        function judgeScore() {
            let score = 0;
            let msg = "";
            const a2 = document.getElementById('ans2').value.trim().replace(/\\s/g, "");
            const a3 = document.getElementById('ans3').value.trim();

            if(selectedChoice === currentUnit.q1.ans) score += 34; else msg += "【問1】" + currentUnit.q1.feedback + "<br>";
            if(a2 === currentUnit.q2.ans) score += 33; else msg += "【問2】" + currentUnit.q2.feedback + "<br>";
            if(a3 === currentUnit.q3.ans) score += 33; else msg += "【問3】" + currentUnit.q3.feedback + "<br>";

            if(score >= 80) {
                alert("合格です！すみれさん、素晴らしい！");
                goHome();
            } else {
                const hd = document.getElementById('hint-display');
                hd.innerHTML = "<b>スコア: " + score + "% - もう少しです！ヒント:</b><br>" + msg;
                hd.style.display = 'block';
            }
        }

        function goHome() {
            document.querySelectorAll('.layer').forEach(l => l.classList.remove('show'));
            document.getElementById('left-default').classList.add('show');
            document.getElementById('right-default').classList.add('show');
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
