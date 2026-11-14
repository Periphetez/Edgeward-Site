(function(){
  var d=document, root=d.documentElement;
  root.classList.add('js');
  var reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
  // mobile menu
  var btn=d.querySelector('.menu-btn'), nav=d.querySelector('.nav');
  if(btn&&nav){btn.addEventListener('click',function(){var o=nav.classList.toggle('open');btn.setAttribute('aria-expanded',o);});}
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
