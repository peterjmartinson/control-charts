var module_7393124=(function(){var c={};i18n_getmessage=function(){return hs_i18n_getMessage(c,hsVars.language,arguments)};i18n_getlanguage=function(){return hsVars.language};var a=function(p){var i=3;var f="",e=p,q=p.querySelector(".hs-search-field__input"),d=p.querySelector(".hs-search-field__suggestions"),k=function(){var s=[];var t=p.querySelector("form");for(var r=0;r<t.querySelectorAll("input[type=hidden]").length;r++){var u=t.querySelectorAll("input[type=hidden]")[r];if(u.name!=="limit"){s.push(encodeURIComponent(u.name)+"="+encodeURIComponent(u.value))}}var v=s.join("&");return v};var m=function(s,u,r){var t;return function(){var y=this,x=arguments;var w=function(){t=null;if(!r){s.apply(y,x)}};var v=r&&!t;clearTimeout(t);t=setTimeout(w,u||200);if(v){s.apply(y,x)}}},n=function(){d.innerHTML="";q.focus();e.classList.remove("hs-search-field--open")},l=function(s){var r=[];r.push("<li id='results-for'>Results for \""+s.searchTerm+'"</li>');s.results.forEach(function(u,t){r.push("<li id='result"+t+"'><a href='"+u.url+"'>"+u.title+"</a></li>")});n();d.innerHTML=r.join("");e.classList.add("hs-search-field--open")},j=function(){var s=new XMLHttpRequest();var r="/_hcms/search?&term="+encodeURIComponent(f)+"&limit="+encodeURIComponent(i)+"&autocomplete=true&analytics=true&groupId=6088958162&"+k();s.open("GET",r,true);s.onload=function(){if(s.status>=200&&s.status<400){var t=JSON.parse(s.responseText);if(t.total>0){l(t);g()}else{n()}}else{console.error("Server reached, error retrieving results.")}};s.onerror=function(){console.error("Could not reach the server.")};s.send()},g=function(){var y=[];y.push(q);var w=d.getElementsByTagName("A");for(var s=0;s<w.length;s++){y.push(w[s])}var v=y[0],r=y[y.length-1];var u=function(z){if(z.target==r&&!z.shiftKey){z.preventDefault();v.focus()}else{if(z.target==v&&z.shiftKey){z.preventDefault();r.focus()}}},t=function(z){z.preventDefault();if(z.target==r){v.focus()}else{y.forEach(function(A){if(A==z.target){y[y.indexOf(A)+1].focus()}})}},x=function(z){z.preventDefault();if(z.target==v){r.focus()}else{y.forEach(function(A){if(A==z.target){y[y.indexOf(A)-1].focus()}})}};e.addEventListener("keydown",function(z){switch(z.which){case 9:u(z);break;case 27:n();break;case 38:x(z);break;case 40:t(z);break}})},h=m(function(){f=q.value;if(f.length>2){j()}else{if(f.length==0){n()}}},250),o=(function(){q.addEventListener("input",function(r){if((r.which!=9)&&(r.which!=40)&&(r.which!=38)&&(r.which!=27)&&(f!=q.value)){h()}})})()};if(document.attachEvent?document.readyState==="complete":document.readyState!=="loading"){var b=document.querySelectorAll(".hs-search-field");Array.prototype.forEach.call(b,function(e){var d=a(e)})}else{document.addEventListener("DOMContentLoaded",function(){var d=document.querySelectorAll(".hs-search-field");Array.prototype.forEach.call(d,function(f){var e=a(f)})})}})();