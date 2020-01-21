$(document).ready(function () {
   //alert("MC.cookiePolicy.js");
   if (window.location.search.indexOf('deletemcp') > -1) {
     var d = new Date();
     var domain = (window.location.host.indexOf('minitab.com') > -1) ? ';domain=.minitab.com' : '';

      d.setFullYear(d.getFullYear() - 1);
      document.cookie = "mcp=1; path=/" + domain + "; expires=" + d.toUTCString();
   }

   var cookies = document.cookie.split(';');
   //alert("cookies:\n\n" + cookies);
   for (var i = 0; i < cookies.length; i++) {
      var c = cookies[i].trim();
      var cnv = c.split("=");
      if (cnv[0] === "mcp") {
         // we're using the mere existence of the cookie to indicate it was accepted
         //alert("c:\n\n" + c);
         return;
      }
   }

   // we're here, so the cookie policy cookie does not exist
   var $cpToaster = $('#cpToaster');
   var $cpButton = $("#cpButton");
   //alert("$cpToaster:\n'" + $cpToaster.text() + "'\n\n$cpButton\n'" + $cpButton.text() + "'");
   if ($cpToaster.length === 0 || $cpButton.length === 0) {
      // need both for it to work
      return;
   }

   // spacer is not required, but without it, the toaster hides the language selector
   var $cpToasterSpacer = null;
   var $parent = $('form');
   if ($parent.length === 0) {
      $parent = $('body');
   }
   if ($parent.length > 0) {
      $parent.append('<div id="cpToasterSpacer" style="display: none;">&nbsp;</div>');
      $cpToasterSpacer = $('#cpToasterSpacer');
      if ($cpToasterSpacer.length > 0) {
         var h = $cpToaster.outerHeight();
         $cpToasterSpacer.css('height', h);
         //alert("about to:\n$cpToasterSpacer.show('slow')");
         $cpToasterSpacer.show('slow');
      }
   }

   $cpToaster.removeClass('mtb-cpToast');
   $cpButton.click(function () {
     var expiresDate = new Date();
     var domain = (window.location.host.indexOf('minitab.com') > -1) ? ';domain=.minitab.com' : '';

      expiresDate.setFullYear(expiresDate.getFullYear() + 1);
      document.cookie = "mcp=1; path=/" + domain + "; expires=" + expiresDate.toUTCString();
      $cpToaster.addClass('mtb-cpToast');
      if ($cpToasterSpacer && $cpToasterSpacer.length > 0) {
         $cpToasterSpacer.hide('slow');
      }
   });
   
// Cookie Policy Text HTML update based on Browser language 
// requires HTML page to include charset utf-8 for correct encoding of characters:
//  <meta charset="utf-8"/> or 
//  <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
// navigator language property supported in all browsers, IE11+
   
var userLang = navigator.language || navigator.userLanguage;
/* alert("navigator lang: "+userLang); */



var cpAgreementText = {
de: "Durch Ihre Nutzung dieser Website stimmen Sie zu, dass Cookies verwendet werden. Cookies dienen zu Analysezwecken und zum Bereitstellen personalisierter Inhalte.",
en: "By using this site you agree to the use of cookies for analytics and personalized content in accordance with our <span class=\"mtb-keep\"><a href=\"https://www.minitab.com/legal/privacy-policy\">Policy</a>.</span>",
es: "Al utilizar este sitio, usted acepta el uso de cookies para efectos de análisis y contenido personalizado.",
fr: "En utilisant ce site, vous acceptez l'utilisation de cookies à des fins d'analyse et de personnalisation du contenu.",
ja: "本サイトを使用すると、分析およびコンテンツのカスタマイズのためにクッキーが使用されることに同意したことになります。",
ko: "이 사이트를 사용하면 분석 및 사용자 개인 컨텐츠에 대한 쿠키 사용에 동의하는 것입니다.",
pt: "Ao usar esse site, você concorda com a utilização de cookies para análises e conteúdo personalizado.",
zh: "使用此网站，即表示您同意对数据分析和个性化内容使用 Cookie。"
};

var cpReadPolicyText = {
de: "Lesen Sie unsere Richtlinien",
en: "",
es: "Leer nuestra política",
fr: "Lisez notre politique",
ja: "当社のプライバシーポリシーをご確認ください",
ko: "당사의 개인정보 보호정책을 확인하십시오",
pt: "Leia nossa política",
zh: "请阅读我们的政策"
};

var cpOK = {
de: "OK",
en: "OK",
es: "Aceptar",
fr: "OK",
ja: "OK",
ko: "확인",
pt: "OK",
zh: "确定"
};

if(userLang.split('-')[0].length) {
    var lang = userLang.split('-')[0];
    // alert("browser language: "+lang); 
    if(lang == 'de'||lang =='es'||lang =='fr'||lang =='ja'||lang =='ko'||lang =='pt'||lang =='zh'){    
     // non-JQuery 
     /*document.getElementById("cp.agreementText").innerHTML = cpAgreementText[lang];
     document.getElementById("cp.readPolicyText").innerHTML = cpReadPolicyText[lang];
     document.getElementById("cp.OK").innerHTML = cpOK[lang];*/
   
     // JQuery
     $("#cp\\.agreementText").html(cpAgreementText[lang]);
     $("#cp\\.readPolicyText").html(cpReadPolicyText[lang]);
     $("#cp\\.OK").html(cpOK[lang]);
    }
    
//else exiting en-US content remains
    
}

   
});
// http://uxd.minitab.com/uxpatternlibrary/dev/_lib/Marketing/Composites/Minitab_17_3/code_cookies.html
