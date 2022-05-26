let over = document.getElementsByTagName('a')
for(el of over){
  el.addEventListener('mouseover', show);
}

function show(event){
  event.preventDefault();
  document.getElementById("popup").style.visibility="visible";
}

let out = document.getElementsByTagName('a')
for(el of out){
  el.addEventListener('mouseout', hide);
}

function hide(event){
    event.preventDefault();
    document.getElementById("popup").style.visibility="hidden";
  }