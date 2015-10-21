$(document).ready(function(){
	var option= {
		type : 'div',
		url : '/CRD04'
	}
	$('#body').dform('ajax',option);

	$.dform.addType("button", function(options) {
	    // Return a new button element that has all options that
	    // don't have a registered subscriber as attributes
	    return $("<button>").dform('attr', options).html("");
	});


});
function ST_OPEN_CARD(obj,card_id){
	remove_card();
	$(obj).addClass('OPEN_CARD');
	var option=[];
	option.type='div';
	option.url='/'+card_id;
	$('body').dform('ajax',option);
}

function ST_CLOSE_PAGE(obj){
	remove_card();
	$(obj).addClass('OPEN_CARD');
}

function remove_card(){
	$('.OPEN_CARD').removeClass('OPEN_CARD');
	$('.card').remove();
}
