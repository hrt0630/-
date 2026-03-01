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
    <title>数学マスターシステム - すみれEdition</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no, viewport-fit=cover">
    <script>
        window.MathJax = {
            tex: { inlineMath: [['$', '$']], displayMath: [['$$', '$$']] },
            chtml: { displayAlign: 'center' }
        };
    </script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <style>
        :root { --accent: #00d2ff; --border: rgba(255, 255, 255, 0.1); --panel-bg: rgba(255, 255, 255, 0.05); }
        body, html { margin: 0; padding: 0; width: 100%; height: 100vh; display: flex; justify-content: center; align-items: center; background: #010208; font-family: "Hiragino Sans", sans-serif; color: white; overflow: hidden; }
        .liquid-bg { position: fixed; inset: 0; z-index: -1; background: radial-gradient(circle at 50% 50%, #0a1128 0%, #000 100%); }
        
        .scene { display: flex; gap: 20px; width: 95%; max-width: 1200px; height: 90vh; }
        .page-panel { flex: 1; background: var(--panel-bg); border: 1px solid var(--border); backdrop-filter: blur(30px); padding: 30px; display: flex; flex-direction: column; overflow-y: auto; border-radius: 20px; scrollbar-width: none; }
        .page-panel::-webkit-scrollbar { display: none; }
        
        .grade-nav { display: flex; background: rgba(255,255,255,0.05); padding: 5px; border-radius: 12px; margin-bottom: 20px; }
        .grade-btn { flex: 1; border: none; background: transparent; color: rgba(255,255,255,0.5); padding: 10px; cursor: pointer; border-radius: 8px; font-weight: bold; }
        .grade-btn.active { background: var(--accent); color: #000; }

        .unit-card { background: rgba(255,255,255,0.03); padding: 15px; border-radius: 10px; margin-bottom: 10px; cursor: pointer; border: 1px solid var(--border); transition: 0.3s; }
        .unit-card:hover { border-color: var(--accent); background: rgba(255,255,255,0.08); }

        .section-title { color: var(--accent); border-bottom: 1px solid var(--accent); margin: 20px 0 10px; padding-bottom: 5px; font-size: 1.1em; font-weight: bold; }
        .point-box { background: rgba(0, 210, 255, 0.05); border-left: 4px solid var(--accent); padding: 15px; margin: 10px 0; border-radius: 0 10px 10px 0; }
        .review-box { background: rgba(247, 183, 49, 0.05); border-left: 4px solid #f7b731; padding: 15px; margin: 20px 0; border-radius: 0 10px 10px 0; color: #f7b731; }
        
        .input-field { width: 100%; padding: 12px; border-radius: 8px; border: 1px solid var(--border); background: rgba(255,255,255,0.05); color: #fff; margin-top: 5px; box-sizing: border-box; outline: none; }
        .input-field:focus { border-color: var(--accent); }
        .btn-primary { width: 100%; padding: 15px; border-radius: 10px; background: #fff; color: #000; font-weight: bold; border: none; cursor: pointer; margin-top: 20px; transition: 0.3s; }
        .btn-primary:hover { background: var(--accent); transform: scale(1.02); }
        
        .layer { display: none; } .layer.show { display: block; animation: fadeIn 0.5s ease; }
        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
        .hidden { display: none; }
    </style>
</head>
<body>
    <div class="liquid-bg"></div>
    <div class="scene">
        <div class="page-panel">
            <div id="left-home" class="layer show">
                <h1 style="font-size: 2.5em;">Study System</h1>
                <p style="opacity: 0.7;">右のリストから単元を選んでください。<br>解説、例題、演習、復習、類題のサイクルで完璧にします。</p>
            </div>
            <div id="left-content" class="layer">
                <button onclick="goHome()" style="background:none; border:none; color:var(--accent); cursor:pointer; font-weight:bold;">← 戻る</button>
                <h2 id="display-title" style="font-size: 1.8em; margin: 10px 0;"></h2>
                
                <div class="section-title">📘 教科書の解説・図形</div>
                <div id="display-desc"></div>

                <div class="section-title">💡 例題</div>
                <div id="display-example"></div>

                <div id="review-section" class="hidden">
                    <div class="section-title">🔄 復習ポイント</div>
                    <div id="display-review" class="review-box"></div>
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
                <div id="unit-list"></div>
            </div>
            <div id="right-practice" class="layer">
                <div class="section-title">✍️ 演習問題</div>
                <div id="display-q"></div>
                <button id="check-btn" class="btn-primary" onclick="checkPractice()">演習を採点する</button>

                <div id="ruidai-section" class="hidden">
                    <div class="section-title">🔥 仕上げの類題</div>
                    <div id="display-ruidai"></div>
                    <button class="btn-primary" onclick="checkFinal()">最終チェック完了</button>
                </div>
            </div>
        </div>
    </div>

    <script>
        let currentUnit = null;
        const mathData = {
            1: [
                { title: "正の数・負の数", desc: "<div class='point-box'>0より小さい数を負の数と呼びます。</div>

[Image of a number line with positive and negative numbers]
", example: "$-5 + 3 = -2$<br>絶対値が大きい方の符号を使いましょう。", q: { t: "$(-8) + 2$", a: "-6" }, review: "符号のミスはありませんでしたか？絶対値の引き算を忘れずに！", ruidai: { t: "$(-12) + 5$", a: "-7" } },
                { title: "文字の式", desc: "<div class='point-box'>$a \\\\times b = ab$ のように記号を省略します。</div>", example: "$x+x+x = 3x$", q: { t: "$5a - 2a$", a: "3a" }, review: "文字が同じもの同士だけ足し引きできます。", ruidai: { t: "$x + 4x$", a: "5x" } },
                { title: "方程式", desc: "<div class='point-box'>＝をまたいで移動することを「移項」といいます。</div>", example: "$x + 5 = 8 \\\\Rightarrow x = 8 - 5 = 3$", q: { t: "$x - 4 = 6$", a: "10" }, review: "移項すると符号が逆転（＋がー）することを再確認しましょう。", ruidai: { t: "$x + 7 = 2$", a: "-5" } },
                { title: "比例と反比例", desc: "<div class='point-box'>$y = ax$ (比例) , $y = a/x$ (反比例)</div>", example: "$y=2x$ で $x=3$ なら $y=6$", q: { t: "$y=3x$ で $x=4$ のときの $y$", a: "12" }, review: "比例は一方が増えるともう一方も一定の割合で増えます。", ruidai: { t: "$y=5x$ で $x=2$ のときの $y$", a: "10" } }
            ],
            2: [
                { title: "式の計算", desc: "<div class='point-box'>かっこを外すときは分配法則！</div>", example: "$2(a + 3b) = 2a + 6b$", q: { t: "$3(2x + y)$", a: "6x+3y" }, review: "かっこの中の全ての項に数字を掛けるのがポイントです。", ruidai: { t: "$4(a - 2b)$", a: "4a-8b" } },
                { title: "連立方程式", desc: "<div class='point-box'>2つの方程式から1つの文字を消します。</div>", example: "$x+y=5, x-y=1$ を足すと $2x=6$", q: { t: "$x+y=3, x-y=1$ の $x$", a: "2" }, review: "加減法で消えないときは、片方の式を数倍してみましょう。", ruidai: { t: "$x+y=10, x-y=4$ の $x$", a: "7" } },
                { title: "一次関数", desc: "<div class='point-box'>$y = ax + b$</div>", example: "傾きが3、切片が2なら $y=3x+2$", q: { t: "傾き2、切片-5の式は？", a: "y=2x-5" }, review: "傾き $a$ は変化の割合とも呼ばれます。", ruidai: { t: "傾き-1、切片4の式は？", a: "y=-x+4" } },
                { title: "図形の性質", desc: "<div class='point-box'>三角形の内角の和は180度。</div>", example: "2つの角が50度の時の残り1つは $180-100=80$", q: { t: "角が60度、70度の三角形の残りの角は？", a: "50" }, review: "外角の性質（隣り合わない2つの内角の和）も便利ですよ！", ruidai: { t: "直角三角形で1つの角が30度の時の、もう一つの鋭角は？", a: "60" } }
            ],
            3: [
                { title: "多項式の展開", desc: "<div class='point-box'>公式: $(x+a)(x+b) = x^2+(a+b)x+ab$</div>", example: "$(x+2)(x+3) = x^2+5x+6$", q: { t: "$(x+1)(x+4)$ を展開せよ", a: "x^2+5x+4" }, review: "真ん中の項は「足し算」、後ろの項は「掛け算」です。", ruidai: { t: "$(x+2)(x+5)$", a: "x^2+7x+10" } },
                { title: "因数分解", desc: "<div class='point-box'>展開の逆！掛け算の形に戻します。</div>", example: "$x^2+5x+6 = (x+2)(x+3)$", q: { t: "$x^2+3x+2$ を因数分解せよ", a: "(x+1)(x+2)" }, review: "まずは共通因数（同じ文字や数字）がないか探すのが鉄則です。", ruidai: { t: "$x^2+7x+12$", a: "(x+3)(x+4)" } },
                { title: "平方根", desc: "<div class='point-box'>2乗して$a$になる数を、$a$の平方根といいます。</div>", example: "$\\\\sqrt{12} = 2\\\\sqrt{3}$", q: { t: "$\\\\sqrt{2} \\\\times \\\\sqrt{8}$", a: "4" }, review: "$\\\\sqrt{a} \\\\times \\\\sqrt{a} = a$ になる性質を使いましょう。", ruidai: { t: "$\\\\sqrt{3} \\\\times \\\\sqrt{12}$", a: "6" } },
                { title: "三平方の定理", desc: "<div class='point-box'>$a^2 + b^2 = c^2$</div>", example: "3cm, 4cm の辺の斜辺は $\\\\sqrt{9+16}=5$", q: { t: "辺が5と12の直角三角形の斜辺は？", a: "13" }, review: "必ず一番長い「斜辺」を $c$ に置いて計算してくださいね。", ruidai: { t: "辺が6と8の直角三角形の斜辺は？", a: "10" } }
            ]
        };

        function setGrade(g) {
            document.querySelectorAll('.grade-btn').forEach((b, i) => b.classList.toggle('active', i+1 === g));
            const list = document.getElementById('unit-list');
            list.innerHTML = mathData[g].map((u, i) => `<div class="unit-card" onclick="startUnit(${g}, ${i})">${u.title}</div>`).join('');
        }

        function startUnit(g, i) {
            currentUnit = mathData[g][i];
            document.getElementById('display-title').innerText = currentUnit.title;
            document.getElementById('display-desc').innerHTML = currentUnit.desc;
            document.getElementById('display-example').innerHTML = currentUnit.example;
            document.getElementById('display-q').innerHTML = `<p>${currentUnit.q.t}</p><input id='ans-q' class='input-field' placeholder='答えを入力...'>`;
            
            document.getElementById('review-section').classList.add('hidden');
            document.getElementById('ruidai-section').classList.add('hidden');
            document.getElementById('check-btn').classList.remove('hidden');

            document.querySelectorAll('.layer').forEach(l => l.classList.remove('show'));
            document.getElementById('left-content').classList.add('show');
            document.getElementById('right-practice').classList.add('show');
            if(window.MathJax) MathJax.typesetPromise();
        }

        function checkPractice() {
            const ans = document.getElementById('ans-q').value.trim();
            if (ans === currentUnit.q.a) {
                alert("✨ 正解！復習ポイントと類題が表示されました。");
                document.getElementById('display-review').innerHTML = currentUnit.review;
                document.getElementById('display-ruidai').innerHTML = `<p>${currentUnit.ruidai.t}</p><input id='ans-r' class='input-field' placeholder='仕上げの答え...'>`;
                document.getElementById('review-section').classList.remove('hidden');
                document.getElementById('ruidai-section').classList.remove('hidden');
                document.getElementById('check-btn').classList.add('hidden');
                if(window.MathJax) MathJax.typesetPromise();
            } else { alert("おっと、もう一度解いてみよう！"); }
        }

        function checkFinal() {
            const ans = document.getElementById('ans-r').value.trim();
            if (ans === currentUnit.ruidai.a) {
                alert("🎊 完璧です！この単元はもう大丈夫ですね。"); goHome();
            } else { alert("あともう少し！復習ポイントを読み直してみて。"); }
        }

        function goHome() {
            document.querySelectorAll('.layer').forEach(l => l.classList.remove('show'));
            document.getElementById('left-home').classList.add('show');
            document.getElementById('right-list').classList.add('show');
        }

        setGrade(1);
    </script>
</body>
</html>
"""
    return HTMLResponse(content=html_content)

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
