/**********************************
* Personal page stat page script  *
**********************************/

$(function() {
	/**** UI ****/
	$('[href][data-cbox-inline]').fancybox({
		overlayOpacity: '0.8',
		overlayColor: '#000',
		showNavArrows: false,
		padding: '0'
	});
	var mySelect = $('#first-disabled2');
	$('#special').on('click', function () {
		mySelect.find('option:selected').attr('disabled', 'disabled');
		mySelect.selectpicker('refresh');
	});
});