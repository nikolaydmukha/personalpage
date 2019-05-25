// User incomes
$(function() {
	// Datepickers
	var ifrom_init = false, ito_init = false;
	if ($('#ifrom').val()) ifrom_init = true;
	if ($('#ito').val()) ito_init = true;
	$('#ifrom,#ito').datepicker({
		dateFormat: 'dd.mm.yy',
		dayNames: ruDayNames,
		dayNamesMin: ruDayNamesMin,
		dayNamesShort: ruDayNamesShort,
		monthNames: ruMonthNames,
		monthNamesShort: ruMonthNamesShort,
		firstDay: 1
	});
	// Datepicker set date if no default value
	//if (!ito_init) $('#ito').datepicker('setDate', serverDate);
	var monthAgo = new Date(serverDate.getTime());
	monthAgo.setMonth(monthAgo.getMonth() - 1);
	if (!ifrom_init) $('#ifrom').datepicker('setDate', monthAgo);
	
	// Datepicker limits
	$('#ifrom').change(function () {
		$('#ito').datepicker('option', 'minDate', $(this).datepicker('getDate'));
	}).change();
	$('#ito').change(function () {
		$('#ifrom').datepicker('option', 'maxDate', $(this).datepicker('getDate'));
	}).change();
	$('#ito').datepicker('option', 'maxDate', serverDate);
	
});