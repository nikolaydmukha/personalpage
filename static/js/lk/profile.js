// User profile

var __doClickWrongName = false;

$(document).ready(function() {

	$('#ipincode').numeric();

	// Save button
	$('#profile_save').clickActive(function() {
		var data = {loading: this};
		['firstname', 'middlename', 'surname', 'email', 'mobile','pincode'].forEach(function(field) {
			data[field] = $('#i'+field).val();
		});
		['sms', 'advmail'].forEach(function(field) {
			data[field] = $('#i'+field).prop('checked')?1:0;
		});
		$('#profile_save_err').text();
		
		ajax_form('/profile/save', data, function(data) {
			if (!data.success) {
				niceErr('Неизвестная ошибка');
			} else {
				if (data.changes) {
					var ch = [];
					$.each(data.changes, function(i,v) {
						ch.push(v['fieldname']);
					});
					$('#profile_save_status').text('Сохранено: '+ch.join(', '));
				} else {
					$('#profile_save_status').text('Нет изменений');
				}
			}
		});
	});
	
	
	//Wrong name button
	$('#wrongname').clickActive(function() {
		fancyAjaxForm('#wrongname_form', '/profile/wrongname', function(data) {
			if (!data.success) {
				niceErr('Неизвестная ошибка');
			} else {
				niceAlert('Спасибо за заявку!\nНаши менеджеры свяжутся с Вами в ближайшее время.');
			}
		});	
	});
	
	if (__doClickWrongName) $('#wrongname').click();

});