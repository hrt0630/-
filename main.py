from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/ui", response_class=HTMLResponse)
def ui():
    # f-stringでの波括弧エラーを避けるため、{{ }} で保護しつつ、
    # あなたが作成したコードの構造を完全に維持しています。
    return f"""
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>理解保証AI型授業 - x & y Edition</title>
    
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no, viewport-fit=cover">
    <link rel="apple-touch-icon" href="https://cdn-icons-png.flaticon.com/512/5968/5968350.png">

    <script>
        window.MathJax = {{
            tex: {{ inlineMath: [['$', '$']], displayMath: [['$$', '$$']] }},
            options: {{ skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre'] }}
        }};
    </script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <style>
        :root {{
            --accent: #00d2ff;
            --purple-glow: #7000ff;
            --border: rgba(255, 255, 255, 0.15);
            --page-w: 520px;
            --book-h: 700px;
            --success: #00ffaa;
        }}

        body, html {{
            margin: 0; padding: 0; width: 100%; height: 100vh;
            display: flex; justify-content: center; align-items: center;
            background: #010208; font-family: "Hiragino Mincho ProN", "serif";
            color: white; overflow: hidden;
        }}

        .liquid-bg {{ position: fixed; inset: 0; z-index: -1; background: linear-gradient(135deg, #050a30 0%, #000000 50%, #1a0033 100%); }}
        .blob {{ position: absolute; width: 80vw; height: 80vw; border-radius: 50%; filter: blur(120px); opacity: 0.35; mix-blend-mode: screen; animation: move 20s infinite alternate ease-in-out; }}
        .b1 {{ background: var(--accent); top: -20%; left: -10%; }} 
        .b2 {{ background: var(--purple-glow); bottom: -20%; right: -10%; animation-delay: -5s; }}
        @keyframes move {{ 0% {{ transform: translate(-5%, -5%); }} 100% {{ transform: translate(10%, 10%); }} }}

        #login-screen {{ position: fixed; inset: 0; z-index: 5000; display: flex; justify-content: center; align-items: center; background: rgba(1, 2, 8, 0.7); backdrop-filter: blur(60px); transition: 1s; }}
        .login-glass {{ background: rgba(255, 255, 255, 0.04); padding: 50px; border-radius: 40px; border: 1px solid var(--border); width: 420px; text-align: center; }}

        .scene {{ display: flex; gap: 8px; width: calc(var(--page-w) * 2); height: var(--book-h); opacity: 0; transform: scale(0.98); transition: 1.2s; position: relative; z-index: 10; }}
        .scene.active {{ opacity: 1; transform: scale(1); }}

        .page-panel {{ flex: 1; background: rgba(255, 255, 255, 0.03); border: 1px solid var(--border); backdrop-filter: blur(45px); padding: 55px; box-sizing: border-box; display: flex; flex-direction: column; position: relative; overflow-y: auto; }}
        .left-p {{ border-radius: 45px 15px 15px 45px; }}
        .right-p {{ border-radius: 15px 45px 45px 15px; font-family: "Hiragino Sans", sans-serif; }}

        .layer {{ position: absolute; inset: 0; padding: 55px; opacity: 0; transform: translateY(20px); transition: 0.6s; pointer-events: none; }}
        .layer.show {{ opacity: 1; transform: translateY(0); pointer-events: auto; z-index: 5; }}

        .chapter-label {{ color: var(--accent); font-size: 14px; font-weight: bold; letter-spacing: 2px; margin-bottom: 10px; }}
        .point-box {{ background: rgba(0, 210, 255, 0.08); border: 1px solid var(--accent); border-radius: 15px; padding: 25px; margin: 20px 0; position: relative; }}
        .point-box::before {{ content: "POINT"; position: absolute; top: -12px; left: 20px; background: var(--accent); color: black; font-size: 10px; font-weight: 900; padding: 2px 10px; border-radius: 5px; }}
        
        .term-box {{ font-size: 13px; background: rgba(255,255,255,0.05); padding: 15px; border-radius: 10px; margin: 10px 0; border: 1px dashed var(--accent); }}

        .btn-action {{ width: 100%; height: 60px; border-radius: 18px; background: white; color: #010208; font-weight: 900; border: none; cursor: pointer; transition: 0.3s; margin-top: 10px; }}
        .btn-action:hover {{ background: var(--accent); color: white; }}
        
        .btn-hint {{ background: rgba(247, 183, 49, 0.2); border: 1px solid #f7b731; color: #f7b731; font-size: 10px; padding: 2px 8px; border-radius: 5px; cursor: pointer; }}
        
        .login-input {{ width: 100%; height: 55px; border-radius: 15px; border: 1px solid var(--border); background: rgba(255,255,255,0.08); color: white; padding: 0 20px; margin-bottom: 12px; box-sizing: border-box; outline: none; }}

        .q-card {{ background: rgba(255,255,255,0.05); padding: 20px; border-radius: 15px; margin-bottom: 15px; border-left: 4px solid var(--accent); }}
        .choice-btn {{ background: rgba(255,255,255,0.08); border: 1px solid var(--border); color: white; padding: 10px; border-radius: 8px; cursor: pointer; margin: 4px; }}
        .choice-btn.selected {{ background: var(--accent); color: black; }}
        
        #hint-text {{ display: none; color: #f7b731; font-size: 12px; margin-top: 10px; padding: 10px; background: rgba(247, 183, 49, 0.1); border-radius: 8px; border: 1px solid rgba(247,183,49,0.3); }}
        .index-item {{ background: rgba(255,255,255,0.06); padding: 25px; border-radius: 20px; margin-bottom: 18px; cursor: pointer; border: 1px solid transparent; transition: 0.3s; }}
        .index-item:hover {{ background: rgba(0, 210, 255, 0.1); border-color: var(--accent); transform: translateX(8px); }}
    </style>
</head>
<body>
    <div class="liquid-bg"><div class="blob b1"></div><div class="blob b2"></div></div>

    <div id="login-screen">
        <div class="login-glass">
            <h2 style="font-weight: 100; margin-bottom: 30px; font-family: 'Hiragino Sans';">理解保証AI型授業</h2>
            <input type="email" class="login-input" placeholder="メールアドレス">
            <input type="password" class="login-input" placeholder="パスワード">
            <button class="btn-action" onclick="launch()">ログイン</button>
        </div>
    </div>

    <div class="scene" id="scene">
        <div class="page-panel left-p">
            <div id="left-default" class="layer show">
                <div class="chapter-label">CHAPTER 01</div>
                <h1 style="font-size: 60px; margin: 0;">数と式</h1>
                <p style="opacity: 0.6; margin-top: 20px; font-size: 18px; line-height: 1.8;">展開と因数分解の世界へようこそ。ここでは $x$ や $y$ を自由自在に操る技術を学びます。</p>
            </div>
            <div id="left-content" class="layer">
                <div class="chapter-label">第1節：展開の公式</div>
                <h2 id="unit-title-display" style="font-size: 32px; margin-bottom: 10px;"></h2>
                <div id="unit-description"></div>
            </div>
        </div>

        <div class="page-panel right-p">
            <div id="right-default" class="layer show">
                <h2 style="font-weight: 100; margin-bottom: 30px;">学習カリキュラム</h2>
                <div class="index-item" onclick="loadUnit('unit1')"><span>01</span><br><b>多項式の展開（$x, y$ 変数版）</b></div>
                <div class="index-item" onclick="loadUnit('unit2')"><span>02</span><br><b>2次関数の決定</b></div>
            </div>
            
            <div id="right-lecture-more" class="layer">
                <div class="chapter-label">EXPLANATION 2</div>
                <div id="unit-more-desc"></div>
                <button class="btn-action" onclick="showExercise()">演習問題に進む</button>
            </div>

            <div id="right-exercise" class="layer">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <p style="color:#f7b731; font-weight:bold; font-size:12px; margin:0;">FINAL EXERCISE</p>
                    <span style="font-size:12px; opacity:0.5;">合格: 80%以上</span>
                </div>
                <div id="exercise-flow"></div>
                <button class="btn-action" onclick="judgeScore()">判定する</button>
                <p onclick="goHome()" style="color:var(--accent); cursor:pointer; margin-top:25px; text-align:center; font-size:12px;">← 目次に戻る</p>
            </div>
        </div>
    </div>

    <script>
        let selectedChoice = null;
        let currentUnit = null;

        const unitData = {
            unit1: { 
                title: "多項式の展開 ($x, y$)", 
                desc: `<p>公式を $x$ と $y$ で整理しましょう。</p>
                       <div class="point-box">$$(x+a)(y+b) = xy + bx + ay + ab$$</div>
                       <div class="term-box">
                         <b style="color:var(--accent)">用語解説：定数項（ていすうこう）</b><br>
                         式の中で、$x$ や $y$ といった文字が掛けられていない<b>「ただの数字のみ」</b>の項のことです。
                       </div>`,
                more: `<h3>文字が混ざっても基本は同じ</h3>
                       <p>分配法則を使って、順番に掛けていきます。</p>
                       <div class="point-box">$$(x+3)(y-2) = xy - 2x + 3y - 6$$</div>`,
                q1: { txt: "$(x+4)(y+2)$ を展開したとき、$x$ の係数は？", choices: [2, 4, 8, 1], ans: 2, feedback: "展開すると $xy + 2x + 4y + 8$ となります。$x$ に掛かっている数字を見てみましょう。" },
                q2: { txt: "$(x-5)(y+3)$ を展開せよ。", ans: "xy+3x-5y-15", feedback: "分配法則で4回掛け算をします。$-5 \times 3$ の符号に注意！" },
                q3: { txt: "$(x-2)(y-4)$ を展開したときの定数項は？", ans: 8, hint: "定数項はカッコ内の「数字」どうしを掛けたものです。", feedback: "$-2 \times -4 = 8$ ですね。マイナス同士の掛け算はプラスになります。" }
            },
            // ↓ここから「1」の要望：CHAPTER 02 の追加
            unit2: {
                title: "因数分解の基本 ($x, y$)",
                desc: `<p>展開の逆、共通因数でくくる技術です。</p>
                       <div class="point-box">$$ax + ay = a(x + y)$$</div>
                       <div class="term-box">
                         <b style="color:var(--accent)">ポイント</b><br>
                         すべての項に含まれている文字や数字（共通因数）を見つけ出すのがコツです。
                       </div>`,
                more: `<h3>複雑な式の因数分解</h3>
                       <p>複数の文字があっても、共通するものを見つければ簡単です。</p>
                       <div class="point-box">$$3xy - 6x = 3x(y - 2)$$</div>`,
                q1: { txt: "$5xy + 10x$ を因数分解したとき、カッコの外に出る共通因数は？", choices: ["5x", "5", "x", "10x"], ans: "5x", feedback: "5と10はどちらも5で割れ、どちらの項にもxが含まれています。" },
                q2: { txt: "$xy + 2x - 3y - 6$ を因数分解せよ。", ans: "(x-3)(y+2)", feedback: "前の2つ $x(y+2)$ と後ろの2つ $-3(y+2)$ で分けると共通の $(y+2)$ が見つかります。" },
                q3: { txt: "$2xy - 4y$ を因数分解した際のカッコ内は？ (共通因数 $2y$ を出した場合)", ans: "x-2", hint: "各項を $2y$ で割ってみましょう。", feedback: "$2xy \div 2y = x$、$-4y \div 2y = -2$ です。" }
            }
        };

        function refreshMath() {{
            if (window.MathJax && window.MathJax.typesetPromise) {{
                MathJax.typesetPromise();
            }}
        }}

        function launch() {{ 
            document.getElementById('login-screen').style.opacity = '0'; 
            setTimeout(() => {{ 
                document.getElementById('login-screen').style.display = 'none'; 
                document.getElementById('scene').classList.add('active'); 
                refreshMath();
            }}, 800); 
        }}

        function loadUnit(unitId) {{
            currentUnit = unitData[unitId];
            document.getElementById('unit-title-display').innerText = currentUnit.title;
            document.getElementById('unit-description').innerHTML = currentUnit.desc;
            document.getElementById('unit-more-desc').innerHTML = currentUnit.more;
            
            document.querySelectorAll('.layer').forEach(l => l.classList.remove('show'));
            setTimeout(() => {{
                document.getElementById('left-content').classList.add('show');
                document.getElementById('right-lecture-more').classList.add('show');
                refreshMath();
            }}, 400);
        }}

        function showExercise() {{
            const data = currentUnit;
            document.getElementById('exercise-flow').innerHTML = `
                <div class="q-card">
                    <small style="color:var(--accent)">1. 選択式 (40%)</small><br>${{data.q1.txt}}
                    <div style="margin-top:10px;">
                        ${{data.q1.choices.map(c => `<button class="choice-btn" onclick="setChoice(this, ${{c}})">${{c}}</button>`).join('')}}
                    </div>
                </div>
                <div class="q-card">
                    <small style="color:var(--accent)">2. 記述式 (40%)</small><br>${{data.q2.txt}}
                    <input type="text" id="ans2" class="login-input" style="height:45px; margin-top:10px; font-size:16px;" placeholder="xy+3x...">
                </div>
                <div class="q-card">
                    <div style="display:flex; justify-content:space-between;">
                        <small style="color:var(--accent)">3. 類題 (20%)</small> 
                        <button class="btn-hint" onclick="toggleHint()">ヒントを見る</button>
                    </div>
                    <p style="margin:5px 0;">${{data.q3.txt}}</p>
                    <input type="number" id="ans3" class="login-input" style="height:45px; margin-top:5px;">
                    <div id="hint-text">${{data.q3.hint}}</div>
                </div>
            `;
            document.getElementById('right-lecture-more').classList.remove('show');
            setTimeout(() => {{ 
                document.getElementById('right-exercise').classList.add('show'); 
                refreshMath();
            }}, 400);
        }}

        function setChoice(btn, val) {{
            document.querySelectorAll('.choice-btn').forEach(b => b.classList.remove('selected'));
            btn.classList.add('selected');
            selectedChoice = val;
        }}

        function toggleHint() {{
            const h = document.getElementById('hint-text');
            h.style.display = (h.style.display === 'block') ? 'none' : 'block';
        }}

        function toggleHint() {
            const h = document.getElementById('hint-text');
            h.style.display = (h.style.display === 'block') ? 'none' : 'block';
        }

        function judgeScore() {
            let score = 0;
            let feedbackMsg = "";
            const a2 = document.getElementById('ans2').value.replace(/\s/g, "");
            const a3 = parseInt(document.getElementById('ans3').value);

            // Q1判定
            if(selectedChoice === currentUnit.q1.ans) {
                score += 40;
            } else {
                feedbackMsg += "【問1のヒント】" + (currentUnit.q1.feedback || "") + "\\n";
            }

            // Q2判定
            if(a2 === currentUnit.q2.ans) {
                score += 40;
            } else {
                feedbackMsg += "【問2のヒント】" + (currentUnit.q2.feedback || "") + "\\n";
            }

            // Q3判定
            if(a3 === currentUnit.q3.ans) {
                score += 20;
            } else {
                feedbackMsg += "【問3のヒント】" + (currentUnit.q3.feedback || "") + "\\n";
            }

            if(score >= 80) {
                alert("素晴らしい！理解度スコア: " + score + "%\\n単元をマスターしました！");
                goHome();
            } else {
                alert("スコア: " + score + "%\\n80%以上で合格です。\\n\\n" + feedbackMsg);
            }
        }

        function goHome() {{
            document.querySelectorAll('.layer').forEach(l => l.classList.remove('show'));
            setTimeout(() => {{ 
                document.getElementById('left-default').classList.add('show'); 
                document.getElementById('right-default').classList.add('show'); 
                refreshMath();
            }}, 400);
        }}
    </script>
</body>
</html>
"""

# コードの最後の一番下に追加
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)
