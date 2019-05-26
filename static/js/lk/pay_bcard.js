// Pay with bank card



$(function() {
	// Elements cache
	var isum = $('#isum'),
		ipay = $('#ipay'),
		iptabs = $('#ipay-tabs');
	
	/** Functions **/
	// Validate sum
	function validateSum(sum) {
        if (!sum.match(/^\d*$/)) throw 'Sum error: wrong sum "' + sum + '"';
        if (sum === '') {
            isum.validationErr('Введите сумму');
            return false;
        }
        sum = parseInt(sum);
        if (sum <= 0) {
            isum.validationErr('Неверная сумма');
            return false;
        }
        return sum;
    }
	
	/** Pay button **/
	ipay.clickActive(function() {
		clearvErr();
		// Get data
		var data = {
			sum: validateSum(isum.val())
		};
		// Check sum validation
		if (data.sum === false) return;
		// Get psp function
		var psp = iptabs.find('li.ui-state-active').attr('data-psp');
		var f = window['psp_'+psp];
		if ('function' !== typeof f) throw 'No psp function for "'+psp+'"';
		// Call psp function
		f(data, ipay);
	});
	
	/** UI **/
	// Basic UI
	$('[name=sum]').focus();
	$('[data-pay-tabs]').tabs();
});
