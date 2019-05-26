// User dpay

$(function() {
	var rulogin = $(':radio[name=ulogin]');
	$('#dpay_enable').clickActive(function() {
		var cbox = rulogin.filter(':checked');
		var login = cbox.val();
		if (rulogin.length > 1) {
			var service = cbox.attr('data-service-name');
			$('#confirm-data').text(login+' ('+service+')');
		}
		fancyAjaxYesNo('#dpay_confirmation', '/dpay/enable', {login: login}, function(data) {
			if (data.success) {
				niceAlert('Услуга "Обещанный платеж" активирована.\nИзменения вступят в силу через 1-10 мин.', '', reload);
			} else {
				niceErr('Ошибка', data.err.text);
			}
		});
	});
	
	var f, first = true;
	rulogin.change(f = function (){
		var login = rulogin.filter(':checked').attr('data-login');
		console.log('show', login);
		$('.dpaydata').hide();
		var div = $('.dpaydata[data-login='+login+']');
		div.show();
		if (first) {
			first = false;
		} else {
			div.effect('highlight');
		}
	});
	f();
});