from pathlib import Path
import base64, urllib.request

images = [
 ('911','https://images.porsche.com/f/338913/1280x1024/b7f3c2d593/911-desktop_5-4.jpg'),
 ('Taycan','https://images.porsche.com/f/338913/1280x1024/e178b7a186/taycan-desktop_5-4.jpg'),
 ('Macan','https://images.porsche.com/f/338913/1280x1024/3debd00362/macan-desktop_5-4.jpg'),
 ('Cayenne','https://images.porsche.com/f/338913/1280x1024/7c9b828a7a/denver-range-fallback-desktop-var2.jpg'),
]
slides=[]
for name,url in images:
    slides.append((name,url+'/m/filters:format(webp):quality(80)'))

p=Path('index.html'); html=p.read_text(encoding='utf-8')
css='''<style>.hero{position:relative;isolation:isolate;min-height:510px;display:flex;flex-direction:column;justify-content:end;overflow:hidden}.hero-image{position:absolute;inset:0;z-index:-2;background-position:center;background-size:cover;transition:opacity .3s}.hero:before{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(90deg,rgba(0,0,0,.76),rgba(0,0,0,.12)),linear-gradient(0deg,rgba(0,0,0,.55),transparent 65%)}.carousel-controls{display:flex;align-items:center;gap:12px;margin-top:26px}.carousel-controls button{width:44px;height:44px;border:1px solid #fff;background:rgba(0,0,0,.3);padding:0;font-size:1.4rem}.carousel-controls button:hover{background:white;color:#111}.carousel-count{font-size:.9rem;min-width:70px}.gallery{margin:55px 0 0}.gallery-head{display:flex;justify-content:space-between;gap:15px;align-items:end;flex-wrap:wrap}.gallery-scroll{display:grid;grid-auto-flow:column;grid-auto-columns:minmax(230px,30%);gap:16px;overflow-x:auto;scroll-snap-type:x mandatory;padding:18px 0 10px}.gallery-item{position:relative;aspect-ratio:5/4;overflow:hidden;border-radius:5px;scroll-snap-align:start;background:#222}.gallery-item img{width:100%;height:100%;object-fit:cover;display:block}.gallery-item strong{position:absolute;bottom:0;left:0;right:0;padding:40px 18px 18px;color:white;font-size:1.4rem;background:linear-gradient(transparent,rgba(0,0,0,.75))}@media(max-width:700px){.hero{min-height:480px}.gallery-scroll{grid-auto-columns:78%}}</style>'''
html=html.replace('</head>',css+'</head>',1)
html=html.replace('<section class="hero"><div class="eyebrow">','<section class="hero" aria-label="Destaques Porsche"><div class="hero-image" id="hero-image" role="img"></div><div class="eyebrow">',1)
html=html.replace('</p></section><main class="wrap">','</p><div class="carousel-controls"><button type="button" id="prev" aria-label="Imagem anterior">‹</button><span id="slide-label" class="carousel-count" aria-live="polite"></span><button type="button" id="next" aria-label="Próxima imagem">›</button></div></section><main class="wrap">',1)
gallery='''<section class="gallery"><div class="gallery-head"><div><h2>Explore os modelos.</h2><div class="muted">Imagens ilustrativas de modelos Porsche. Deslize para ver mais.</div></div></div><div class="gallery-scroll" aria-label="Galeria de modelos Porsche">'''
for name,src in slides: gallery+=f'<div class="gallery-item"><img src="{src}" alt="Porsche {name}" loading="lazy"><strong>{name}</strong></div>'
gallery+='</div></section>'
html=html.replace('<h2 class="section-title">Três perguntas. Uma visão.</h2>',gallery+'<h2 class="section-title">Três perguntas. Uma visão.</h2>',1)
import json
script='''<script>const SLIDES = '''+json.dumps([{'name':n,'src':s} for n,s in slides],ensure_ascii=False)+''';let currentSlide=0;function showSlide(){const slide=SLIDES[currentSlide];const image=document.getElementById('hero-image');image.style.backgroundImage='url("'+slide.src+'")';image.setAttribute('aria-label','Porsche '+slide.name);document.getElementById('slide-label').textContent=slide.name+' · '+(currentSlide+1)+' / '+SLIDES.length}document.getElementById('prev').addEventListener('click',()=>{currentSlide=(currentSlide+SLIDES.length-1)%SLIDES.length;showSlide()});document.getElementById('next').addEventListener('click',()=>{currentSlide=(currentSlide+1)%SLIDES.length;showSlide()});showSlide();</script>'''
html=html.replace('</body>',script+'</body>',1); p.write_text(html,encoding='utf-8')
print('HTML atualizado.')
