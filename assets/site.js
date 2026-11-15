(function(){
  var d=document, root=d.documentElement;
  root.classList.add('js');
  var reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
  // mobile menu
  var btn=d.querySelector('.menu-btn'), nav=d.querySelector('.nav');
  if(btn&&nav){btn.addEventListener('click',function(){var o=nav.classList.toggle('open');btn.setAttribute('aria-expanded',o);});}
  // video player (YouTube, privacy-enhanced; loads only when clicked)
  function closeV(){var m=d.querySelector('.vmodal');if(m){m.remove();d.body.style.overflow='';}}
  d.addEventListener('click',function(e){
    var b=e.target.closest&&e.target.closest('[data-yt]');
    if(b){e.preventDefault();var m=d.createElement('div');m.className='vmodal';m.setAttribute('role','dialog');m.setAttribute('aria-label','Video');
      m.innerHTML='<button class="vclose" type="button">Close ✕</button><div class="vbox"><iframe src="https://www.youtube-nocookie.com/embed/'+b.getAttribute('data-yt')+'?autoplay=1&rel=0" title="Edgeward demo video" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen></iframe></div>';
      d.body.appendChild(m);d.body.style.overflow='hidden';m.querySelector('.vclose').focus();return;}
    if(e.target.classList&&(e.target.classList.contains('vmodal')||e.target.classList.contains('vclose')))closeV();
  });
  d.addEventListener('keydown',function(e){if(e.key==='Escape')closeV();});
  // animated graphics: run only while on screen; hold a still frame if the visitor prefers less motion
  var scenes=[].slice.call(d.querySelectorAll('svg.scene'));
  scenes.forEach(function(s){ if(reduce&&s.pauseAnimations){ try{s.setCurrentTime(6);s.pauseAnimations();}catch(e){} } });
  var rv=[].slice.call(d.querySelectorAll('.rv'));
  if(!('IntersectionObserver' in window)){rv.forEach(function(e){e.classList.add('in');});return;}
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{rootMargin:'0px 0px -8% 0px'});
  rv.forEach(function(e){io.observe(e);});
  if(!reduce){
    var so=new IntersectionObserver(function(es){es.forEach(function(e){var s=e.target;if(!s.pauseAnimations)return;try{e.isIntersecting?s.unpauseAnimations():s.pauseAnimations();}catch(x){}});},{rootMargin:'120px'});
    scenes.forEach(function(s){so.observe(s);});
  }
})();
