
(function($){$.fn.extend({leanModal:function(options){var defaults={top:50,overlay:0.5,closeButton:null};var overlay=$("<div id='lean_overlay'></div>");$("body").append(overlay);options=$.extend(defaults,options);return this.each(function(){var o=options;$(this).click(function(e){var modal_id=$(this).attr("href");$("#lean_overlay").click(function(){close_modal(modal_id)});$(o.closeButton).click(function(){close_modal(modal_id)});var modal_height=$(modal_id).outerHeight();var modal_width=$(modal_id).outerWidth();
$("#lean_overlay").css({"display":"block",opacity:0});$("#lean_overlay").fadeTo(200,o.overlay);$(modal_id).css({"display":"block","position":"fixed","opacity":0,"z-index":11000,"left":50+"%","margin-left":-(modal_width/2)+"px","top":100+"px"});$(modal_id).fadeTo(200,1);e.preventDefault()})});function close_modal(modal_id){$("#lean_overlay").fadeOut(200);$(modal_id).css({"display":"none"})}}})})(jQuery);


document.getElementById("modal_close").onclick = function(){
    var content = document.getElementById("content");
    content.style.opacity = 1;
    console.log("close");
}


document.getElementById("modal_trigger").onclick = function(){
    var content = document.getElementById("content");
    document.getElementById("modal").style.opacity = 1;
    content.style.opacity = 0.4;
}


function detectionresultopen(){
    document.getElementById("modal2").style.opacity = 1;
}


function detectionresultclose(){
    document.getElementById("modal2").style.opacity = 0;
}
