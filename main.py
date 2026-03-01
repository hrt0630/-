{\rtf1\ansi\ansicpg932\cocoartf2868
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red183\green111\blue179;\red24\green24\blue24;\red193\green193\blue193;
\red67\green192\blue160;\red140\green211\blue254;\red202\green202\blue202;\red212\green214\blue154;\red194\green126\blue101;
\red70\green137\blue204;\red89\green138\blue67;\red205\green173\blue106;\red167\green197\blue152;}
{\*\expandedcolortbl;;\cssrgb\c77255\c52549\c75294;\cssrgb\c12157\c12157\c12157;\cssrgb\c80000\c80000\c80000;
\cssrgb\c30588\c78824\c69020;\cssrgb\c61176\c86275\c99608;\cssrgb\c83137\c83137\c83137;\cssrgb\c86275\c86275\c66667;\cssrgb\c80784\c56863\c47059;
\cssrgb\c33725\c61176\c83922;\cssrgb\c41569\c60000\c33333;\cssrgb\c84314\c72941\c49020;\cssrgb\c70980\c80784\c65882;}
\paperw11900\paperh16840\margl1440\margr1440\vieww30040\viewh18980\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 from\cf4 \strokec4  \cf5 \strokec5 fastapi\cf4 \strokec4  \cf2 \strokec2 import\cf4 \strokec4  \cf5 \strokec5 FastAPI\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 from\cf4 \strokec4  \cf5 \strokec5 fastapi\cf4 \strokec4 .\cf5 \strokec5 responses\cf4 \strokec4  \cf2 \strokec2 import\cf4 \strokec4  \cf5 \strokec5 HTMLResponse\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 app\cf4 \strokec4  \cf7 \strokec7 =\cf4 \strokec4  \cf5 \strokec5 FastAPI\cf4 \strokec4 ()\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf8 \cb3 \strokec8 @\cf6 \strokec6 app\cf8 \strokec8 .get\cf4 \strokec4 (\cf9 \strokec9 "/ui"\cf4 \strokec4 , \cf6 \strokec6 response_class\cf7 \strokec7 =\cf5 \strokec5 HTMLResponse\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf10 \cb3 \strokec10 def\cf4 \strokec4  \cf8 \strokec8 ui\cf4 \strokec4 ():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf11 \strokec11 # f-string\uc0\u12391 \u12398 \u27874 \u25324 \u24359 \u12456 \u12521 \u12540 \u12434 \u36991 \u12369 \u12427 \u12383 \u12417 \u12289 \{\{ \}\} \u12391 \u20445 \u35703 \u12375 \u12388 \u12388 \u12289 \cf4 \cb1 \strokec4 \
\cb3     \cf11 \strokec11 # \uc0\u12354 \u12394 \u12383 \u12364 \u20316 \u25104 \u12375 \u12383 \u12467 \u12540 \u12489 \u12398 \u27083 \u36896 \u12434 \u23436 \u20840 \u12395 \u32173 \u25345 \u12375 \u12390 \u12356 \u12414 \u12377 \u12290 \cf4 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 return\cf4 \strokec4  \cf10 \strokec10 f\cf9 \strokec9 """\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf9 \cb3 \strokec9 <!DOCTYPE html>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9 <html lang="ja">\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9 <head>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9     <meta charset="UTF-8">\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9     <title>\uc0\u29702 \u35299 \u20445 \u35388 AI\u22411 \u25480 \u26989  - x & y Edition</title>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9     \cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9     <meta name="apple-mobile-web-app-capable" content="yes">\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9     <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9     <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no, viewport-fit=cover">\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9     <link rel="apple-touch-icon" href="https://cdn-icons-png.flaticon.com/512/5968/5968350.png">\cf4 \cb1 \strokec4 \
\
\cf9 \cb3 \strokec9     <script>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         window.MathJax = \cf12 \strokec12 \{\{\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             tex: \cf12 \strokec12 \{\{\cf9 \strokec9  inlineMath: [['$', '$']], displayMath: [['$$', '$$']] \cf12 \strokec12 \}\}\cf9 \strokec9 ,\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             options: \cf12 \strokec12 \{\{\cf9 \strokec9  skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre'] \cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         \cf12 \strokec12 \}\}\cf9 \strokec9 ;\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9     </script>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9     <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9     <style>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         :root \cf12 \strokec12 \{\{\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             --accent: #00d2ff;\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             --purple-glow: #7000ff;\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             --border: rgba(255, 255, 255, 0.15);\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             --page-w: 520px;\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             --book-h: 700px;\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             --success: #00ffaa;\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         \cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\
\cf9 \cb3 \strokec9         body, html \cf12 \strokec12 \{\{\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             margin: 0; padding: 0; width: 100%; height: 100vh;\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             display: flex; justify-content: center; align-items: center;\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             background: #010208; font-family: "Hiragino Mincho ProN", "serif";\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             color: white; overflow: hidden;\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         \cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\
\cf9 \cb3 \strokec9         .liquid-bg \cf12 \strokec12 \{\{\cf9 \strokec9  position: fixed; inset: 0; z-index: -1; background: linear-gradient(135deg, #050a30 0%, #000000 50%, #1a0033 100%); \cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         .blob \cf12 \strokec12 \{\{\cf9 \strokec9  position: absolute; width: 80vw; height: 80vw; border-radius: 50%; filter: blur(120px); opacity: 0.35; mix-blend-mode: screen; animation: move 20s infinite alternate ease-in-out; \cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         .b1 \cf12 \strokec12 \{\{\cf9 \strokec9  background: var(--accent); top: -20%; left: -10%; \cf12 \strokec12 \}\}\cf9 \strokec9  \cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         .b2 \cf12 \strokec12 \{\{\cf9 \strokec9  background: var(--purple-glow); bottom: -20%; right: -10%; animation-delay: -5s; \cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         @keyframes move \cf12 \strokec12 \{\{\cf9 \strokec9  0% \cf12 \strokec12 \{\{\cf9 \strokec9  transform: translate(-5%, -5%); \cf12 \strokec12 \}\}\cf9 \strokec9  100% \cf12 \strokec12 \{\{\cf9 \strokec9  transform: translate(10%, 10%); \cf12 \strokec12 \}\}\cf9 \strokec9  \cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\
\cf9 \cb3 \strokec9         #login-screen \cf12 \strokec12 \{\{\cf9 \strokec9  position: fixed; inset: 0; z-index: 5000; display: flex; justify-content: center; align-items: center; background: rgba(1, 2, 8, 0.7); backdrop-filter: blur(60px); transition: 1s; \cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         .login-glass \cf12 \strokec12 \{\{\cf9 \strokec9  background: rgba(255, 255, 255, 0.04); padding: 50px; border-radius: 40px; border: 1px solid var(--border); width: 420px; text-align: center; \cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\
\cf9 \cb3 \strokec9         .scene \cf12 \strokec12 \{\{\cf9 \strokec9  display: flex; gap: 8px; width: calc(var(--page-w) * 2); height: var(--book-h); opacity: 0; transform: scale(0.98); transition: 1.2s; position: relative; z-index: 10; \cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         .scene.active \cf12 \strokec12 \{\{\cf9 \strokec9  opacity: 1; transform: scale(1); \cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\
\cf9 \cb3 \strokec9         .page-panel \cf12 \strokec12 \{\{\cf9 \strokec9  flex: 1; background: rgba(255, 255, 255, 0.03); border: 1px solid var(--border); backdrop-filter: blur(45px); padding: 55px; box-sizing: border-box; display: flex; flex-direction: column; position: relative; overflow-y: auto; \cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         .left-p \cf12 \strokec12 \{\{\cf9 \strokec9  border-radius: 45px 15px 15px 45px; \cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         .right-p \cf12 \strokec12 \{\{\cf9 \strokec9  border-radius: 15px 45px 45px 15px; font-family: "Hiragino Sans", sans-serif; \cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\
\cf9 \cb3 \strokec9         .layer \cf12 \strokec12 \{\{\cf9 \strokec9  position: absolute; inset: 0; padding: 55px; opacity: 0; transform: translateY(20px); transition: 0.6s; pointer-events: none; \cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         .layer.show \cf12 \strokec12 \{\{\cf9 \strokec9  opacity: 1; transform: translateY(0); pointer-events: auto; z-index: 5; \cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\
\cf9 \cb3 \strokec9         .chapter-label \cf12 \strokec12 \{\{\cf9 \strokec9  color: var(--accent); font-size: 14px; font-weight: bold; letter-spacing: 2px; margin-bottom: 10px; \cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         .point-box \cf12 \strokec12 \{\{\cf9 \strokec9  background: rgba(0, 210, 255, 0.08); border: 1px solid var(--accent); border-radius: 15px; padding: 25px; margin: 20px 0; position: relative; \cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         .point-box::before \cf12 \strokec12 \{\{\cf9 \strokec9  content: "POINT"; position: absolute; top: -12px; left: 20px; background: var(--accent); color: black; font-size: 10px; font-weight: 900; padding: 2px 10px; border-radius: 5px; \cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         \cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         .term-box \cf12 \strokec12 \{\{\cf9 \strokec9  font-size: 13px; background: rgba(255,255,255,0.05); padding: 15px; border-radius: 10px; margin: 10px 0; border: 1px dashed var(--accent); \cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\
\cf9 \cb3 \strokec9         .btn-action \cf12 \strokec12 \{\{\cf9 \strokec9  width: 100%; height: 60px; border-radius: 18px; background: white; color: #010208; font-weight: 900; border: none; cursor: pointer; transition: 0.3s; margin-top: 10px; \cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         .btn-action:hover \cf12 \strokec12 \{\{\cf9 \strokec9  background: var(--accent); color: white; \cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         \cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         .btn-hint \cf12 \strokec12 \{\{\cf9 \strokec9  background: rgba(247, 183, 49, 0.2); border: 1px solid #f7b731; color: #f7b731; font-size: 10px; padding: 2px 8px; border-radius: 5px; cursor: pointer; \cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         \cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         .login-input \cf12 \strokec12 \{\{\cf9 \strokec9  width: 100%; height: 55px; border-radius: 15px; border: 1px solid var(--border); background: rgba(255,255,255,0.08); color: white; padding: 0 20px; margin-bottom: 12px; box-sizing: border-box; outline: none; \cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\
\cf9 \cb3 \strokec9         .q-card \cf12 \strokec12 \{\{\cf9 \strokec9  background: rgba(255,255,255,0.05); padding: 20px; border-radius: 15px; margin-bottom: 15px; border-left: 4px solid var(--accent); \cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         .choice-btn \cf12 \strokec12 \{\{\cf9 \strokec9  background: rgba(255,255,255,0.08); border: 1px solid var(--border); color: white; padding: 10px; border-radius: 8px; cursor: pointer; margin: 4px; \cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         .choice-btn.selected \cf12 \strokec12 \{\{\cf9 \strokec9  background: var(--accent); color: black; \cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         \cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         #hint-text \cf12 \strokec12 \{\{\cf9 \strokec9  display: none; color: #f7b731; font-size: 12px; margin-top: 10px; padding: 10px; background: rgba(247, 183, 49, 0.1); border-radius: 8px; border: 1px solid rgba(247,183,49,0.3); \cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         .index-item \cf12 \strokec12 \{\{\cf9 \strokec9  background: rgba(255,255,255,0.06); padding: 25px; border-radius: 20px; margin-bottom: 18px; cursor: pointer; border: 1px solid transparent; transition: 0.3s; \cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         .index-item:hover \cf12 \strokec12 \{\{\cf9 \strokec9  background: rgba(0, 210, 255, 0.1); border-color: var(--accent); transform: translateX(8px); \cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9     </style>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9 </head>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9 <body>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9     <div class="liquid-bg"><div class="blob b1"></div><div class="blob b2"></div></div>\cf4 \cb1 \strokec4 \
\
\cf9 \cb3 \strokec9     <div id="login-screen">\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         <div class="login-glass">\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             <h2 style="font-weight: 100; margin-bottom: 30px; font-family: 'Hiragino Sans';">\uc0\u29702 \u35299 \u20445 \u35388 AI\u22411 \u25480 \u26989 </h2>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             <input type="email" class="login-input" placeholder="\uc0\u12513 \u12540 \u12523 \u12450 \u12489 \u12524 \u12473 ">\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             <input type="password" class="login-input" placeholder="\uc0\u12497 \u12473 \u12527 \u12540 \u12489 ">\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             <button class="btn-action" onclick="launch()">\uc0\u12525 \u12464 \u12452 \u12531 </button>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         </div>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9     </div>\cf4 \cb1 \strokec4 \
\
\cf9 \cb3 \strokec9     <div class="scene" id="scene">\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         <div class="page-panel left-p">\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             <div id="left-default" class="layer show">\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 <div class="chapter-label">CHAPTER 01</div>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 <h1 style="font-size: 60px; margin: 0;">\uc0\u25968 \u12392 \u24335 </h1>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 <p style="opacity: 0.6; margin-top: 20px; font-size: 18px; line-height: 1.8;">\uc0\u23637 \u38283 \u12392 \u22240 \u25968 \u20998 \u35299 \u12398 \u19990 \u30028 \u12408 \u12424 \u12358 \u12371 \u12381 \u12290 \u12371 \u12371 \u12391 \u12399  $x$ \u12420  $y$ \u12434 \u33258 \u30001 \u33258 \u22312 \u12395 \u25805 \u12427 \u25216 \u34899 \u12434 \u23398 \u12403 \u12414 \u12377 \u12290 </p>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             </div>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             <div id="left-content" class="layer">\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 <div class="chapter-label">\uc0\u31532 1\u31680 \u65306 \u23637 \u38283 \u12398 \u20844 \u24335 </div>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 <h2 id="unit-title-display" style="font-size: 32px; margin-bottom: 10px;"></h2>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 <div id="unit-description"></div>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             </div>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         </div>\cf4 \cb1 \strokec4 \
\
\cf9 \cb3 \strokec9         <div class="page-panel right-p">\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             <div id="right-default" class="layer show">\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 <h2 style="font-weight: 100; margin-bottom: 30px;">\uc0\u23398 \u32722 \u12459 \u12522 \u12461 \u12517 \u12521 \u12512 </h2>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 <div class="index-item" onclick="loadUnit('unit1')"><span>01</span><br><b>\uc0\u22810 \u38917 \u24335 \u12398 \u23637 \u38283 \u65288 $x, y$ \u22793 \u25968 \u29256 \u65289 </b></div>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 <div class="index-item" onclick="loadUnit('unit2')"><span>02</span><br><b>2\uc0\u27425 \u38306 \u25968 \u12398 \u27770 \u23450 </b></div>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             </div>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             \cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             <div id="right-lecture-more" class="layer">\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 <div class="chapter-label">EXPLANATION 2</div>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 <div id="unit-more-desc"></div>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 <button class="btn-action" onclick="showExercise()">\uc0\u28436 \u32722 \u21839 \u38988 \u12395 \u36914 \u12416 </button>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             </div>\cf4 \cb1 \strokec4 \
\
\cf9 \cb3 \strokec9             <div id="right-exercise" class="layer">\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 <div style="display:flex; justify-content:space-between; align-items:center;">\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                     <p style="color:#f7b731; font-weight:bold; font-size:12px; margin:0;">FINAL EXERCISE</p>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                     <span style="font-size:12px; opacity:0.5;">\uc0\u21512 \u26684 : 80%\u20197 \u19978 </span>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 </div>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 <div id="exercise-flow"></div>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 <button class="btn-action" onclick="judgeScore()">\uc0\u21028 \u23450 \u12377 \u12427 </button>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 <p onclick="goHome()" style="color:var(--accent); cursor:pointer; margin-top:25px; text-align:center; font-size:12px;">\uc0\u8592  \u30446 \u27425 \u12395 \u25147 \u12427 </p>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             </div>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         </div>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9     </div>\cf4 \cb1 \strokec4 \
\
\cf9 \cb3 \strokec9     <script>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         let selectedChoice = null;\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         let currentUnit = null;\cf4 \cb1 \strokec4 \
\
\cf9 \cb3 \strokec9         const unitData = \cf12 \strokec12 \{\{\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             unit1: \cf12 \strokec12 \{\{\cf9 \strokec9  \cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 title: "\uc0\u22810 \u38917 \u24335 \u12398 \u23637 \u38283  ($x, y$)", \cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 desc: `<p>\uc0\u20844 \u24335 \u12434  $x$ \u12392  $y$ \u12391 \u25972 \u29702 \u12375 \u12414 \u12375 \u12423 \u12358 \u12290 </p>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                        <div class="point-box">$$(x+a)(y+b) = xy + bx + ay + ab$$</div>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                        <div class="term-box">\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                          <b style="color:var(--accent)">\uc0\u29992 \u35486 \u35299 \u35500 \u65306 \u23450 \u25968 \u38917 \u65288 \u12390 \u12356 \u12377 \u12358 \u12371 \u12358 \u65289 </b><br>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                          \uc0\u24335 \u12398 \u20013 \u12391 \u12289 $x$ \u12420  $y$ \u12392 \u12356 \u12387 \u12383 \u25991 \u23383 \u12364 \u25499 \u12369 \u12425 \u12428 \u12390 \u12356 \u12394 \u12356 <b>\u12300 \u12383 \u12384 \u12398 \u25968 \u23383 \u12398 \u12415 \u12301 </b>\u12398 \u38917 \u12398 \u12371 \u12392 \u12391 \u12377 \u12290 <br>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                          \uc0\u20363 \u65306 $x + y + 5$ \u12398 \u22580 \u21512 \u12289 \u23450 \u25968 \u38917 \u12399  $5$ \u12391 \u12377 \u12290 \cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                        </div>`,\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 more: `<h3>\uc0\u25991 \u23383 \u12364 \u28151 \u12374 \u12387 \u12390 \u12418 \u22522 \u26412 \u12399 \u21516 \u12376 </h3>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                        <p>\uc0\u20998 \u37197 \u27861 \u21063 \u12434 \u20351 \u12387 \u12390 \u12289 \u24038 \u12398 \u12459 \u12483 \u12467 \u12398 \u21508 \u38917 \u12434 \u12289 \u21491 \u12398 \u12459 \u12483 \u12467 \u12398 \u21508 \u38917 \u12395 \u38918 \u30058 \u12395 \u25499 \u12369 \u12390 \u12356 \u12365 \u12414 \u12377 \u12290 </p>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                        <div class="point-box">$$(x+3)(y-2) = xy - 2x + 3y - 6$$</div>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                        <p style="font-size:13px; opacity:0.7;">\uc0\u12371 \u12398 \u22580 \u21512 \u12398 \u23450 \u25968 \u38917 \u12399  $-6$ \u12391 \u12377 \u12397 \u12290 </p>`,\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 q1: \cf12 \strokec12 \{\{\cf9 \strokec9  txt: "$(x+4)(y+2)$ \uc0\u12434 \u23637 \u38283 \u12375 \u12383 \u12392 \u12365 \u12289 $x$ \u12398 \u20418 \u25968 \u12399 \u65311 ", choices: [2, 4, 8, 1], ans: 2 \cf12 \strokec12 \}\}\cf9 \strokec9 ,\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 q2: \cf12 \strokec12 \{\{\cf9 \strokec9  txt: "$(x-5)(y+3)$ \uc0\u12434 \u23637 \u38283 \u12379 \u12424 \u12290 ", ans: "xy+3x-5y-15" \cf12 \strokec12 \}\}\cf9 \strokec9 ,\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 q3: \cf12 \strokec12 \{\{\cf9 \strokec9  txt: "$(x-2)(y-4)$ \uc0\u12434 \u23637 \u38283 \u12375 \u12383 \u12392 \u12365 \u12398 \u23450 \u25968 \u38917 \u12399 \u65311 ", ans: 8, hint: "\u23450 \u25968 \u38917 \u12399 \u12459 \u12483 \u12467 \u20869 \u12398 \u12300 \u25968 \u23383 \u65288 \u31526 \u21495 \u12434 \u21547 \u12416 \u65289 \u12301 \u12393 \u12358 \u12375 \u12434 \u25499 \u12369 \u21512 \u12431 \u12379 \u12383 \u12418 \u12398 \u12391 \u12377 \u12290 $-2 \cf12 \strokec12 \\\\\cf9 \strokec9 times -4$ \uc0\u12399 \u65311 " \cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             \cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         \cf12 \strokec12 \}\}\cf9 \strokec9 ;\cf4 \cb1 \strokec4 \
\
\cf9 \cb3 \strokec9         function refreshMath() \cf12 \strokec12 \{\{\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             if (window.MathJax && window.MathJax.typesetPromise) \cf12 \strokec12 \{\{\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 MathJax.typesetPromise();\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             \cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         \cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\
\cf9 \cb3 \strokec9         function launch() \cf12 \strokec12 \{\{\cf9 \strokec9  \cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             document.getElementById('login-screen').style.opacity = '0'; \cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             setTimeout(() => \cf12 \strokec12 \{\{\cf9 \strokec9  \cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 document.getElementById('login-screen').style.display = 'none'; \cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 document.getElementById('scene').classList.add('active'); \cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 refreshMath();\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             \cf12 \strokec12 \}\}\cf9 \strokec9 , 800); \cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         \cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\
\cf9 \cb3 \strokec9         function loadUnit(unitId) \cf12 \strokec12 \{\{\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             currentUnit = unitData[unitId];\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             document.getElementById('unit-title-display').innerText = currentUnit.title;\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             document.getElementById('unit-description').innerHTML = currentUnit.desc;\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             document.getElementById('unit-more-desc').innerHTML = currentUnit.more;\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             \cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             document.querySelectorAll('.layer').forEach(l => l.classList.remove('show'));\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             setTimeout(() => \cf12 \strokec12 \{\{\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 document.getElementById('left-content').classList.add('show');\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 document.getElementById('right-lecture-more').classList.add('show');\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 refreshMath();\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             \cf12 \strokec12 \}\}\cf9 \strokec9 , 400);\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         \cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\
\cf9 \cb3 \strokec9         function showExercise() \cf12 \strokec12 \{\{\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             const data = currentUnit;\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             document.getElementById('exercise-flow').innerHTML = `\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 <div class="q-card">\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                     <small style="color:var(--accent)">1. \uc0\u36984 \u25246 \u24335  (40%)</small><br>$\cf12 \strokec12 \{\{\cf9 \strokec9 data.q1.txt\cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                     <div style="margin-top:10px;">\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                         $\cf12 \strokec12 \{\{\cf9 \strokec9 data.q1.choices.map(c => `<button class="choice-btn" onclick="setChoice(this, $\cf12 \strokec12 \{\{\cf9 \strokec9 c\cf12 \strokec12 \}\}\cf9 \strokec9 )">$\cf12 \strokec12 \{\{\cf9 \strokec9 c\cf12 \strokec12 \}\}\cf9 \strokec9 </button>`).join('')\cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                     </div>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 </div>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 <div class="q-card">\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                     <small style="color:var(--accent)">2. \uc0\u35352 \u36848 \u24335  (40%)</small><br>$\cf12 \strokec12 \{\{\cf9 \strokec9 data.q2.txt\cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                     <input type="text" id="ans2" class="login-input" style="height:45px; margin-top:10px; font-size:16px;" placeholder="xy+3x...">\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 </div>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 <div class="q-card">\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                     <div style="display:flex; justify-content:space-between;">\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                         <small style="color:var(--accent)">3. \uc0\u39006 \u38988  (20%)</small> \cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                         <button class="btn-hint" onclick="toggleHint()">\uc0\u12498 \u12531 \u12488 \u12434 \u35211 \u12427 </button>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                     </div>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                     <p style="margin:5px 0;">$\cf12 \strokec12 \{\{\cf9 \strokec9 data.q3.txt\cf12 \strokec12 \}\}\cf9 \strokec9 </p>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                     <input type="number" id="ans3" class="login-input" style="height:45px; margin-top:5px;">\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                     <div id="hint-text">$\cf12 \strokec12 \{\{\cf9 \strokec9 data.q3.hint\cf12 \strokec12 \}\}\cf9 \strokec9 </div>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 </div>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             `;\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             document.getElementById('right-lecture-more').classList.remove('show');\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             setTimeout(() => \cf12 \strokec12 \{\{\cf9 \strokec9  \cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 document.getElementById('right-exercise').classList.add('show'); \cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 refreshMath();\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             \cf12 \strokec12 \}\}\cf9 \strokec9 , 400);\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         \cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\
\cf9 \cb3 \strokec9         function setChoice(btn, val) \cf12 \strokec12 \{\{\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             document.querySelectorAll('.choice-btn').forEach(b => b.classList.remove('selected'));\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             btn.classList.add('selected');\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             selectedChoice = val;\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         \cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\
\cf9 \cb3 \strokec9         function toggleHint() \cf12 \strokec12 \{\{\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             const h = document.getElementById('hint-text');\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             h.style.display = (h.style.display === 'block') ? 'none' : 'block';\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         \cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\
\cf9 \cb3 \strokec9         function judgeScore() \cf12 \strokec12 \{\{\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             let score = 0;\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             const a2 = document.getElementById('ans2').value.replace(/\cf12 \strokec12 \\\\\\\\\cf9 \strokec9 s/g, "");\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             if(selectedChoice === currentUnit.q1.ans) score += 40;\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             if(a2 === currentUnit.q2.ans) score += 40;\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             if(parseInt(document.getElementById('ans3').value) === currentUnit.q3.ans) score += 20;\cf4 \cb1 \strokec4 \
\
\cf9 \cb3 \strokec9             if(score >= 80) \cf12 \strokec12 \{\{\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 alert("\uc0\u32032 \u26228 \u12425 \u12375 \u12356 \u65281 \u29702 \u35299 \u24230 \u12473 \u12467 \u12450 : " + score + "%\cf12 \strokec12 \\\\\cf9 \strokec9 n\uc0\u21336 \u20803 \u12434 \u12510 \u12473 \u12479 \u12540 \u12375 \u12414 \u12375 \u12383 \u65281 ");\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 goHome();\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             \cf12 \strokec12 \}\}\cf9 \strokec9  else \cf12 \strokec12 \{\{\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 alert("\uc0\u12473 \u12467 \u12450 : " + score + "%\cf12 \strokec12 \\\\\cf9 \strokec9 n80%\uc0\u20197 \u19978 \u12391 \u21512 \u26684 \u12391 \u12377 \u12290 \u25945 \u31185 \u26360 \u12434 \u12418 \u12358 \u19968 \u24230 \u35211 \u30452 \u12375 \u12414 \u12375 \u12423 \u12358 \u65281 ");\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             \cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         \cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\
\cf9 \cb3 \strokec9         function goHome() \cf12 \strokec12 \{\{\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             document.querySelectorAll('.layer').forEach(l => l.classList.remove('show'));\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             setTimeout(() => \cf12 \strokec12 \{\{\cf9 \strokec9  \cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 document.getElementById('left-default').classList.add('show'); \cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 document.getElementById('right-default').classList.add('show'); \cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9                 refreshMath();\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9             \cf12 \strokec12 \}\}\cf9 \strokec9 , 400);\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9         \cf12 \strokec12 \}\}\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9     </script>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9 </body>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9 </html>\cf4 \cb1 \strokec4 \
\cf9 \cb3 \strokec9 """\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf11 \cb3 \strokec11 # \uc0\u12467 \u12540 \u12489 \u12398 \u26368 \u24460 \u12398 \u19968 \u30058 \u19979 \u12395 \u36861 \u21152 \cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 if\cf4 \strokec4  \cf6 \strokec6 __name__\cf4 \strokec4  \cf7 \strokec7 ==\cf4 \strokec4  \cf9 \strokec9 "__main__"\cf4 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf2 \strokec2 import\cf4 \strokec4  \cf5 \strokec5 uvicorn\cf4 \cb1 \strokec4 \
\cb3     \cf5 \strokec5 uvicorn\cf4 \strokec4 .\cf8 \strokec8 run\cf4 \strokec4 (\cf6 \strokec6 app\cf4 \strokec4 , \cf6 \strokec6 host\cf7 \strokec7 =\cf9 \strokec9 "0.0.0.0"\cf4 \strokec4 , \cf6 \strokec6 port\cf7 \strokec7 =\cf13 \strokec13 10000\cf4 \strokec4 )\cb1 \
}