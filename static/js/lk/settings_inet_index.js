/** Inet settings script **/

$(function() {

	$('#ip_finder').on('input',function(){
		if ($(this).val().length > 2) {
			$('[data-scope-for]').hide();
			$('[data-scope-for^="'+$(this).val()+'"]').show();
		} else {
			$('[data-scope-for]').show();
		}
	});

	$('.port-cell').on('click','div.mgn-select-item',function(){
		var pointer = $(this).parent().parent().siblings('select[name="fw"]');
		pointer.children('option').removeAttr('selected');
		pointer.find('option[value="'+$('span.crutch',this).text().trim()+'"]').attr('selected',true);
	});
	
	// Enable save button on change
	var enSave = function(pointer) {
		pointer.prop('disabled', false);
		if (pointer.data('_oldtext')) pointer.text(pointer.data('_oldtext'));
	};
	$('[data-mac-for]').on('input',function(){
		enSave($('[data-scope-for="'+$(this).attr('data-mac-for')+'"]').find('.save'));
	});

	//nhk crutch
	$('.port-cell').on('mgn:selected','.mgn-select-item',function() {
		enSave($(this).closest('[data-scope-for]').find('.save'));
	}); 
	
	// Save button
	$('.save').clickActive(function() {
		// Get nearest parent tr
		var _button = $(this);
		var _targetIp = _button.attr('data-save-for');
        var _isvirus = _button.attr('data-is-virus');
		var _mac = $('[data-mac-for="'+_targetIp+'"]');
		//var _elem = $(this).closest('tr');
		var data = {
			formScope: 	$('[data-scope-for="'+_targetIp+'"]'),
			loading: 	_button,
			ip: 		_targetIp,
			mac: 		_mac.val(),
			fw: 		$('[data-fwport-for="'+_targetIp+'"]').val()
		};
        if (_isvirus == 1) data.keepLoading = true;
		ajax_form('/settings/inet/save', data, function (data) {
			if (!data.success) {
				if ('err' in data) {
					if (data.err.code == 31 || data.err.code == 32) { // Mac errors
						_mac.validationErr(data.err.text);
					} else {
                        if (_isvirus == 1) _button.removeClass('loading');
						niceErr(data.err.text);
					}
				} else {
					niceErr('Неизвестная ошибка');
				}
			} else {
				_button.prop('disabled', true);
				if (!_button.data('_oldtext')) _button.data('_oldtext', _button.text());
				_button.text('Сохранено');
                if (_isvirus == 1) location.href = '/settings/inet/antivirus_help';
			}
		});
	})
	
})