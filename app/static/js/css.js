$(document).ready(function(){
	var formcon=$(".dropdown-con");
	formcon.each(function(){
		if(1==$(this).has("form").length)
			formcon=$(this);
	});
	var login_input=formcon.find("input");
	login_input.each(function(){
		$(this).focus(function(){
			formcon.css("display","block");
		});
		$(this).blur(function(){
			formcon.css("display","");
		});
	});
});