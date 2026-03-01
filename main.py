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
    <title>AI理解保証システム - Intelligent Edition</title>
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
            --ai-color: #a29bfe;
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

        /* AI・ビジュアル要素 */
        .visual-box { background: rgba(255,255,255,0.02); border-radius: 15px; padding: 20px; margin: 15px 0; border: 1px solid var(--border); }
        .section-title { color: var(--accent); border-bottom: 1px solid var(--accent); margin-top: 25px; padding-bottom: 5px; font-weight: bold; }
        .ai-box { background: rgba(162, 155, 254, 0.1); border: 1px solid var(--ai-color); border-radius: 15px; padding: 20px; margin-top: 20px; position: relative; }
        .ai-badge { position: absolute; top: -10px; left: 20px; background: var(--ai-color); color: #000; padding: 2px 10px; border-radius: 5px; font-size: 0.7em; font-weight: bold; }

        .btn-primary { width: 100%; padding: 18px; border-radius: 15px; background: #fff; color: #000; font-weight: 900; border: none; cursor: pointer; margin-top: 20px; }
        .input-field { width: 100%; padding: 15px; border-radius: 12px; border: 1px solid var(--border); background: rgba(255,255,255,0.05); color: #fff; margin-bottom: 10px; box-sizing: border-box; outline: none; }
        
        .layer { display: none; } .layer.show { display: block; }
        .hidden { display: none; }
    </style>
</head>
<body>
    <div class="liquid-bg"></div>
    <div id="login-screen">
        <div class="login-glass">
            <h2 style="color:var(--accent);">AI Study Link</h2>
            <p style="font-size: 0.8em; opacity: 0.6; margin-bottom:20px;">すみれさんの理解度をAIが学習中</p>
            <input type="email" class="input-field" placeholder="Email">
            <input type="password" class="input-field" placeholder="Password">
            <button class="btn-primary" onclick="launch()">学習を開始</button>
        </div>
    </div>

    <div class="scene" id="scene">
        <div class="page-panel">
            <div id="left-home" class="layer show">
                <h1 style="font-size:2.5em; margin: 0;">Hi, すみれ!</h1>
                <p style="opacity:0.7;">今日の学習状況をAIが分析しています。</p>
                
                <div class="ai-box">
                    <div class="ai-badge">AI ANALYSIS</div>
                    <div id="ai-insight">
                        「分析を開始します。右から単元を選んでね。すみれさんの解き方のクセを見抜くよ！」
                    </div>
                </div>

                <div class="section-title">📊 習得スコア</div>
                <div id="mastery-list" style="margin-top:10px; font-size:0.9em;">
                    まだデータがありません。
                </div>
            </div>
            
            <div id="left-lesson" class="layer">
                <button onclick="goHome()" style="background:none; border:none; color:var(--accent); cursor:pointer;">← 戻る</button>
                <h2 id="lesson-title"></h2>
                <div class="section-title">🧭 イメージで理解</div>
                <div id="visual-content"></div>
                <div class="section-title">📘 公式・ルール</div>
                <div id="lesson-desc"></div>
                <div id="review-section" class="hidden">
                    <div class="section-title">🔄 AI復習講義</div>
                    <div id="lesson-review" style="background:rgba(247,183,49,0.1); padding:15px; border-radius:10px; color:var(--warning);"></div>
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
                <button id="check-btn" class="btn-primary" onclick="checkPractice()">AI判定を受ける</button>
                
                <div id="ruidai-section" class="hidden">
                    <div class="section-title">🔥 仕上げの類題</div>
                    <div id="ruidai-body"></div>
                    <button class="btn-primary" onclick="checkFinal()">完了して記録する</button>
                </div>
            </div>
        </div>
    </div>

    <script>
        // AI学習用データ
        let aiBrain = {
            mistakeLogs: {}, // 単元ごとのミス記録
            mastery: {},     // 習得度 0-100
            totalSessions: 0
        };

        const mathData = {
            1: [
                { id:'1-1', title:"正の数・負の数", visual:"<div class='visual-box'><b>数直線イメージ</b><br><br>マイナスを掛ける＝「逆を向く」と覚えよう！</div>", desc:"$(- ) \\\\times (- ) = +$ は、反対の反対は正面！という意味だよ。", q:{t:"$(-3) \\\\times (-4)$", a:"12", type:"sign_check"}, review:"正解！マイナスの掛け算は『逆を向いてから逆へ進む』からプラスになるんだね。", ruidai:{t:"$(-2) \\\\times (-3) \\\\times (-2)$", a:"-12"} },
                { id:'1-3', title:"方程式", visual:"<div class='visual-box'><b>天秤イメージ</b><br><br>＝は天秤。左から2引いたら、右からも2引く！</div>", desc:"移項（＝をまたぐ）ときは、符号をひっくり返そう。", q:{t:"$x + 8 = 3$", a:"-5", type:"transition_check"}, review:"移項したあとの計算もバッチリだね。$x = 3 - 8$ の形を作れたかな？", ruidai:{t:"$x + 12 = 4$", a:"-8"} }
            ],
            2: [
                { id:'2-1', title:"連立方程式", visual:"<div class='visual-box'><b>犯人特定イメージ</b><br>2つのヒントから共通の犯人（xとy）を絞り込むよ。</div>", desc:"加減法で、まずは片方の文字を消去しよう！", q:{t:"$x+y=10, x-y=2$ の $x$ は？", a:"6", type:"elimination_check"}, review:"文字を消す感覚、掴めてきたね！", ruidai:{t:"$x+y=8, x-y=2$ の $x$ は？", a:"5"} }
            ],
            3: [
                { id:'3-1', title:"三平方の定理", visual:"<div class='visual-box'><b>ピタゴラスイメージ</b><br><br>直角三角形の辺の長さの魔法のルール！</div>", desc:"$a^2 + b^2 = c^2$。斜辺（一番長いとこ）が $c$ だよ。", q:{t:"辺が6と8の直角三角形の斜辺は？", a:"10", type:"geometry_check"}, review:"2乗の計算が速いね！その調子。", ruidai:{t:"辺が9と12の直角三角形の斜辺は？", a:"15"} }
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
                alert("AI判定：正解！すみれさんのロジックは正しいです。");
                aiBrain.mastery[currentUnit.title] = (aiBrain.mastery[currentUnit.title] || 0) + 20;
                document.getElementById('lesson-review').innerHTML = currentUnit.review;
                document.getElementById('ruidai-body').innerHTML = `<p>${currentUnit.ruidai.t}</p><input id='ans-r' class='input-field' placeholder='類題...'>`;
                document.getElementById('review-section').classList.remove('hidden');
                document.getElementById('ruidai-section').classList.remove('hidden');
                document.getElementById('check-btn').classList.add('hidden');
            } else { 
                // AI学習プロセス
                aiBrain.mistakeLogs[currentUnit.title] = (aiBrain.mistakeLogs[currentUnit.title] || 0) + 1;
                updateAIInsight();
                alert("AIヒント：少し考え方がズレているかも？左のイメージ図をもう一度見てみて。");
            }
        }

        function updateAIInsight() {
            const insight = document.getElementById('ai-insight');
            const mistakes = aiBrain.mistakeLogs[currentUnit.title];
            if (mistakes >= 2) {
                insight.innerHTML = `🤖 <b>分析完了:</b> すみれさんは「${currentUnit.title}」の${currentUnit.q.type === 'sign_check' ? '符号のルール' : '計算の順序'}でつまずく傾向があるよ。次はここを重点的に教えるね！`;
            }
        }

        function checkFinal() {
            if (document.getElementById('ans-r').value.trim() === currentUnit.ruidai.a) {
                aiBrain.mastery[currentUnit.title] = Math.min((aiBrain.mastery[currentUnit.title] || 0) + 30, 100);
                alert("🎊 類題もクリア！習得度が上がりました！");
                updateMasteryUI();
                goHome();
            } else { alert("あともう少し！"); }
        }

        function updateMasteryUI() {
            const list = document.getElementById('mastery-list');
            list.innerHTML = Object.entries(aiBrain.mastery).map(([title, score]) => `
                <div style="margin-bottom:10px;">
                    <div style="display:flex; justify-content:space-between;"><span>${title}</span><span>${score}%</span></div>
                    <div style="width:100%; height:4px; background:rgba(255,255,255,0.1); border-radius:2px; margin-top:4px;">
                        <div style="width:${score}%; height:100%; background:var(--accent); border-radius:2px;"></div>
                    </div>
                </div>
            `).join('');
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
