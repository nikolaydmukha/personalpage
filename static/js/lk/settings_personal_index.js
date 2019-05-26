// Personal settings

$(document).ready(function() {

	$('.value').on('click','div.mgn-select-item',function(){
		var pointer = $(this).parent().parent().siblings('select[name="access_external"]');
		pointer.children('option').removeAttr('selected');
		pointer.find('option[value="'+$('span.crutch',this).text()+'"]').attr('selected',true);
	});


	// Save button
	$('#settings_save').clickActive(function() {
		$('#settings_save_status').text('');
		var data = {loading: this};
		var notConfirmed = false;
		var accessLost = false;
		['rinet', 'external'].forEach(function(suffix) {
			var val = $('#iaccess_'+suffix).val();
			data['access_'+suffix] = val;
		});
		if ((__ipType == 'rinet' || __ipType == 'external') && (data['access_external'] == 2 || data['access_external'] == 3)) {
			notConfirmed = !confirm('Сохранив настройки, Вы ограничите доступ к некоторым опциям Личного Кабинета, в том числе и к этой странице.\n\
				Вновь открыть доступ Вы сможете только с устройства, авторизованного в сети RiNet и находящегося по адресу Вашего подключения.\n\
				Продолжить сохранение настроек?');
			accessLost = !__admin;
		} else if (__oldExt != data['access_external'] && data['access_external'] == 1) {
			notConfirmed = !confirm('Сохранив настройки, Вы вернёте возможность управления услугами в Личном Кабинете с любого адреса.\nПродолжить сохранение настроек?');
			__oldExt = data['access_external'];
		}
		
		if (notConfirmed) return;
		
		ajax_form('/settings/personal/save', data, function(data) {
			if (data.success) {
				$('#settings_save_status').text('Сохранено.');
				if (accessLost) location.href = '/';
			} else {
				$('#settings_save_status').text('Ошибка сохранения.');
			}
		});
	});
});