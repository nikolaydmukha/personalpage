// User internet block (idle)

$(function() {
	var f, first = true;
	var rulogin = $(':radio[name=ulogin]');
	var ronoff = $('.onoff-letter');
	rulogin.change(f = function (){
		var login = rulogin.filter(':checked').attr('data-login');
		console.log('show', login);
		$('.idledata').hide();
		var div = $('.idledata[data-login='+login+']');
		div.show();
		if (div[0].hasAttribute('data-enabled')) {
			ronoff.text('ы');
		} else {
			ronoff.text('');
		}
		if (first) {
			first = false;
		} else {
			div.effect('highlight');
		}
	});
	f();
	
	
	$('#switch_block').clickActive(function() {
		var cbox = rulogin.filter(':checked');
		var login = cbox.val();
		var elogin = cbox.attr('data-login');
		console.log(login);
		if (rulogin.length > 1) {
			var service = cbox.attr('data-service-name');
			$('#confirm-data').text(login+' ('+service+')');
		}
		var div = $('.idledata[data-login='+elogin+']');
		var sw;
		if (div[0].hasAttribute('data-enabled')) {
			sw = 0;
		} else {
			sw = 1;
		}
		fancyAjaxYesNo('#block_confirmation', '/block/sw', {login: login, sw: sw}, function(data) {
			if (data.success) {
				niceAlert('Услуга блокировки '+((sw == 0)?'де':'')+'активирована.\nИзменения вступят в силу через 1-10 мин.', '', reload);
			} else {
				niceErr('Ошибка', data.err.text);
			}
		});
	});
});