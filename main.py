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
    <title>AI理解保証システム - Never Get Lost</title>
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
            --warning: #f7b731;
            --border: rgba(255, 255, 255, 0.1); 
            --panel-bg: rgba(255, 255, 255, 0.05);
        }
        body, html { margin: 0; padding: 0; width: 100%; height: 100vh; display: flex; justify-content: center; align-items: center; background: #010208; font-family: "Hiragino Sans", sans-serif; color: white; overflow: hidden; }
        .liquid-bg { position: fixed; inset: 0; z-index: -1; background: radial-gradient(circle at 50% 50%, #0a1128 0%, #000 100%); }
        
        /* ログイン */
        #login-screen { position: fixed; inset: 0; z-index: 5000; display: flex; justify-content: center; align-items: center; background: rgba(0,0,0,0.9); backdrop-filter: blur(20px); transition: 0.8s; }
        .login-glass { background: var(--panel-bg); padding: 40px; border-radius: 30px; border: 1px solid var(--border); width: 320px; text-align: center; }
        
        /* メインレイアウト */
        .scene { display: flex; gap: 20px; width: 95%; max-width: 1250px; height: 88vh; opacity: 0; transform: translateY(20px); transition: 1s; }
        .scene.active { opacity: 1; transform: translateY(0); }
        
        .page-panel { flex: 1; background: var(--panel-bg); border: 1px solid var(--border); backdrop-filter: blur(30px); padding: 30px; display: flex; flex-direction: column; overflow-y: auto; border-radius: 24px; scrollbar-width: none; }
        .page-panel::-webkit-scrollbar { display: none; }

        .grade-nav { display: flex; background: rgba(255,255,255,0.05); padding: 5px; border-radius: 15px; margin-bottom: 20px; }
        .grade-btn { flex: 1; border: none; background: transparent; color: rgba(255,255,255,0.5); padding: 12px; cursor: pointer; border-radius: 10px; font-weight: bold; }
        .grade-btn.active { background: var(--accent); color: #000; }

        .unit-card { background: rgba(255,255,255,0.03); padding: 18px; border-radius: 15px; margin-bottom: 10px; cursor: pointer; border: 1px solid var(--border); transition: 0.3s; }
        .unit-card:hover { border-color: var(--accent); background: rgba(255,255,255,0.08); }

        /* ビジュアル・セクション */
        .visual-box { background: rgba(255,255,255,0.02); border-radius: 15px; padding: 20px; margin: 15px 0; border: 1px solid var(--border); line-height: 1.6; }
        .section-title { color: var(--accent); border-bottom: 1px solid var(--accent); margin-top: 25px; padding-bottom: 5px; font-weight: bold; }
        .review-box { background: rgba(247, 183, 49, 0.05); border-left: 4px solid var(--warning); padding: 15px; margin: 20px 0; color: var(--warning); font-size: 0.9em; }
        
        .btn-primary { width: 100%; padding: 18px; border-radius: 15px; background: #fff; color: #000; font-weight: 900; border: none; cursor: pointer; margin-top: 20px; transition: 0.3s; }
        .input-field { width: 100%; padding: 15px; border-radius: 12px; border: 1px solid var(--border); background: rgba(255,255,255,0.05); color: #fff; margin-bottom: 10px; box-sizing: border-box; outline: none; }
        
        .layer { display: none; } .layer.show { display: block; }
        .hidden { display: none; }
    </style>
</head>
<body>
    <div class="liquid-bg"></div>
    <div id="login-screen">
        <div class="login-glass">
            <h2>AI Study Link</h2>
            <p style="font-size: 0.8em; opacity: 0.6; margin-bottom:20px;">すみれさんのための学習ルーム</p>
            <input type="email" class="input-field" placeholder="Email">
            <input type="password" class="input-field" placeholder="Password">
            <button class="btn-primary" onclick="launch()">学習を開始</button>
        </div>
    </div>

    <div class="scene" id="scene">
        <div class="page-panel">
            <div id="left-home" class="layer show">
                <h1 style="font-size:2.5em; margin: 0;">Hi, すみれ!</h1>
                <p style="opacity:0.7;">右のリストから単元を選んでね。</p>
                <div id="ai-status" style="margin-top:30px; padding:20px; background:rgba(0,210,255,0.1); border-radius:15px; border:1px solid var(--accent);">
                    🤖 <b>AI分析エンジン起動中:</b><br>
                    <span id="ai-msg">学習を開始すると、あなたの苦手な傾向を分析してここに表示します。</span>
                </div>
            </div>
            <div id="left-lesson" class="layer">
                <button onclick="goHome()" style="background:none; border:none; color:var(--accent); cursor:pointer;">← 戻る</button>
                <h2 id="lesson-title" style="margin: 10px 0;"></h2>
                <div class="section-title">🧭 イメージ解説</div>
                <div id="visual-content"></div>
                <div class="section-title">📘 大事なルール</div>
                <div id="lesson-desc"></div>
                <div id="review-section" class="hidden">
                    <div class="section-title">🔄 復習アドバイス</div>
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
                <button id="check-btn" class="btn-primary" onclick="checkPractice()">答えを判定</button>
                <div id="ruidai-section" class="hidden">
                    <div class="section-title">🔥 仕上げの類題</div>
                    <div id="ruidai-body"></div>
                    <button class="btn-primary" onclick="checkFinal()">完了！</button>
                </div>
            </div>
        </div>
    </div>

    <script>
        let stats = { totalMistakes: 0, sessionMistakes: 0, weakUnits: [] };

        const mathData = {
            1: [
                { id:'1-1', title:"正の数・負の数", visual:"<div class='visual-box'><b>【数直線のイメージ】</b><br>0より右がプラス（増える）、左がマイナス（減る）。<br>$-7+3$ は「左に7歩行ってから、右に3歩戻る」ということ！</div>", desc:"マイナス同士の掛け算は「逆の逆」だからプラスになるよ！", q:{t:"$(-5) + 8$", a:"3", h:"右に8歩進む力が勝つよ！"}, review:"異符号の足し算は、絶対値が大きい方の符号を優先しましょう。", ruidai:{t:"$(-10) + 4$", a:"-6"} },
                { id:'1-2', title:"文字の式", visual:"<div class='visual-box'><b>【りんごの箱詰め】</b><br>$x$はりんご1個の値段。$3x$はりんご3個。中身がわからないものを文字でおくんだ！</div>", desc:"$a \\\\times b$ は $ab$ と書くのがルール。数字は文字の前に書こう。", q:{t:"$2a + 4a$", a:"6a", h:"りんご2個＋りんご4個＝？"}, review:"文字が同じなら、数字（係数）の部分だけ計算すればOK！", ruidai:{t:"$7x - 3x$", a:"4x"} },
                { id:'1-3', title:"方程式", visual:"<div class='visual-box'><b>【天秤のルール】</b><br>右と左が釣り合っています。片方に何かをしたら、もう片方にも同じことをしないとダメ！</div>", desc:"＝をまたぐときは符号が入れ替わる「移項」を使おう。", q:{t:"$x + 6 = 15$", a:"9", h:"両方の皿から6を引いてみよう。"}, review:"$x = ...$ の形にするのがゴールだよ。", ruidai:{t:"$x - 4 = 10$", a:"14"} },
                { id:'1-4', title:"比例と反比例", visual:"<div class='visual-box'><b>【グラフの形】</b><br>比例はまっすぐな直線。反比例はなめらかなカーブ（双曲線）になるよ。</div>", desc:"比例は $y=ax$。 $a$ は決まった数字（比例定数）だよ。", q:{t:"$y=2x$ で $x=5$ の時の $y$", a:"10", h:"$2 \\\\times 5$ を計算！"}, review:"片方が2倍、3倍になると、もう片方も2倍、3倍になるのが比例。", ruidai:{t:"$y=4x$ で $x=3$ の時の $y$", a:"12"} }
            ],
            2: [
                { id:'2-1', title:"式の計算", visual:"<div class='visual-box'><b>【分配法則】</b><br>外にある数字を、かっこ内の全員に平等に配る（掛ける）イメージ。</div>", desc:"$2(a+b) = 2a+2b$ になるよ。マイナスがついている時は符号に注意！", q:{t:"$3(x - 4)$ を展開せよ", a:"3x-12", h:"3をxと-4の両方に掛けて。"}, review:"かっこを外した後の符号ミスが一番多いから気をつけて！", ruidai:{t:"$2(a + 5)$", a:"2a+10"} },
                { id:'2-2', title:"連立方程式", visual:"<div class='visual-box'><b>【犯人探し】</b><br>2つのヒントから、$x$と$y$という2人の正体を突き止めるゲームだよ。</div>", desc:"加減法（足し引きして文字を消す）か代入法を使おう。", q:{t:"$x+y=5, x=2$ のとき $y$ は？", a:"3", h:"$2+y=5$ を解くだけ！"}, review:"片方の文字がわかれば、もう片方はすぐに見つかるよ。", ruidai:{t:"$x+y=10, y=4$ のとき $x$ は？", a:"6"} },
                { id:'2-3', title:"一次関数", visual:"<div class='visual-box'><b>【坂道の傾き】</b><br>$y=ax+b$ の $a$ は坂の急さ（傾き）、$b$ はスタート地点（切片）だよ。</div>", desc:"$x$ が1増えた時に $y$ がどれだけ増えるかが $a$。グラフを描くとわかりやすい！", q:{t:"傾き3、切片5の式は？", a:"y=3x+5", h:"そのまま $ax+b$ に当てはめて。"}, review:"切片 $b$ は $x=0$ の時の $y$ の値のことだよ。", ruidai:{t:"傾き2、切片-3の式は？", a:"y=2x-3"} },
                { id:'2-4', title:"図形の性質", visual:"<div class='visual-box'><b>【三角形の秘密】</b><br>どんな三角形も、3つの角を全部合わせると $180^\\\\circ$ になる！</div>", desc:"平行線の錯角や同位角が等しいこともよく使うよ。", q:{t:"2角が40, 60の三角形の残りの角は？", a:"80", h:"$180 - (40+60)$"}, review:"外角の性質も覚えると、計算がぐっと楽になるよ。", ruidai:{t:"2角が50, 50の三角形の残りの角は？", a:"80"} }
            ],
            3: [
                { id:'3-1', title:"展開と因数分解", visual:"<div class='visual-box'><b>【パズル】</b><br>展開は「バラバラにする」、因数分解は「箱にまとめる」作業だよ。</div>", desc:"公式 $(x+a)(x+b) = x^2+(a+b)x+ab$ を使いこなそう。", q:{t:"$(x+3)(x+2)$ を展開せよ", a:"x^2+5x+6", h:"足して5、掛けて6。"}, review:"因数分解は、掛けて後ろの数字、足して真ん中の数字になるペアを探そう。", ruidai:{t:"$(x+1)(x+4)$", a:"x^2+5x+4"} },
                { id:'3-2', title:"平方根", visual:"<div class='visual-box'><b>【2乗の逆】</b><br>$\\\\sqrt{9}$ は「2乗して9になる正の数」だから 3 のこと。</div>", desc:"$\\\\sqrt{}$ の中身をできるだけ小さくするのが基本だよ。", q:{t:"$\\\\sqrt{36}$ は？", a:"6", h:"何を2乗したら36になる？"}, review:"$\\\\sqrt{a} \\\\times \\\\sqrt{b} = \\\\sqrt{ab}$ のルールを忘れずに。", ruidai:{t:"$\\\\sqrt{49}$", a:"7"} },
                { id:'3-3', title:"二次方程式", visual:"<div class='visual-box'><b>【答えが2つ？】</b><br>2次方程式は、答えが2つ出てくることが多いのが特徴だよ。</div>", desc:"因数分解を使うか、最強の「解の公式」を使おう。", q:{t:"$x^2 = 25$ の解は？(半角,小さい順に , で区切る)", a:"-5,5", h:"プラスとマイナスの両方あるよ。"}, review:"$x^2=k \\\\Rightarrow x = \\\\pm \\\\sqrt{k}$ が基本の形。", ruidai:{t:"$x^2 = 16$", a:"-4,4"} },
                { id:'3-4', title:"三平方の定理", visual:"<div class='visual-box'><b>【ピタゴラス】</b><br>直角三角形なら $a^2+b^2=c^2$ が必ず成り立つ魔法の法則！</div>", desc:"一番長い辺（斜辺）を $c$ にするのがルールだよ。", q:{t:"辺が3, 4の直角三角形の斜辺は？", a:"5", h:"$3^2+4^2 = 9+16 = 25$"}, review:"特別な直角三角形（$1:2:\\\\sqrt{3}$ など）の比も覚えると無敵！", ruidai:{t:"辺が5, 12の直角三角形の斜辺は？", a:"13"} }
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
            container.innerHTML = (mathData[g] || []).map(u => `<div class="unit-card" onclick="openUnit('${g}', '${u.id}')">${u.title}</div>`).join('');
        }

        function openUnit(grade, id) {
            currentUnit = mathData[grade].find(u => u.id === id);
            stats.sessionMistakes = 0;
            document.getElementById('lesson-title').innerText = currentUnit.title;
            document.getElementById('visual-content').innerHTML = currentUnit.visual;
            document.getElementById('lesson-desc').innerHTML = currentUnit.desc;
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
                alert("✨ 正解！");
                document.getElementById('lesson-review').innerHTML = currentUnit.review;
                document.getElementById('ruidai-body').innerHTML = `<p>${currentUnit.ruidai.t}</p><input id='ans-r' class='input-field' placeholder='類題の答え...'>`;
                document.getElementById('review-section').classList.remove('hidden');
                document.getElementById('ruidai-section').classList.remove('hidden');
                document.getElementById('check-btn').classList.add('hidden');
                if (window.MathJax) MathJax.typesetPromise();
            } else { 
                stats.totalMistakes++; stats.sessionMistakes++;
                alert(`ヒント：${currentUnit.q.h}`);
                updateAI();
            }
        }

        function updateAI() {
            const msg = document.getElementById('ai-msg');
            if (stats.totalMistakes >= 3) {
                msg.innerHTML = `⚠️ <b>要注意:</b> 「${currentUnit.title}」でつまずきが見られます。イメージ解説をもう一度ゆっくり読んで、基礎を固めるのが近道だよ！`;
            }
        }

        function checkFinal() {
            if (document.getElementById('ans-r').value.trim() === currentUnit.ruidai.a) {
                alert("🎊 完璧！"); goHome();
            } else { alert("あともう一歩！復習を読んでみて。"); }
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
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
