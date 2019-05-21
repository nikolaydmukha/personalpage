/**********************************
* Personal page traf page script  *
**********************************/

$(function() {
	$('div.value').on('click','div.mgn-select-item',function(){
		var pointer = $('#imonth option[value="'+$(this).find('.crutch').text()+'"]');
		$('#imonth > option').removeAttr('selected');
		pointer.attr('selected',true);
	});
	var abs = $('span.details');
	$('#absolute').clickActive(function() {
		if ($(abs[0]).is(':visible')) {
			abs.hide();
			$(this).text('Показать абсолютные значения трафика');
		} else {
			abs.show();
			$(this).text('Скрыть абсолютные значения трафика');
		}
	});
})