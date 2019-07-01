// Authentication page script

$(function() {
	$('#auth_user').focus();
	/** Logpass recovery **/

	var iRMethod = $(':radio[name=recover_method]');
	var iRString = $('#irecover_string');
	var iRTitle = $('#irecover_title');
	var iRSMS = $('#irecover_sms').children(':checkbox');
	var iREmail = $('#irecover_email').children(':checkbox');

	// Show password
	$('#show').click(function() {
		if ($('#auth_pwd').is(':password')) {
			$('#auth_pwd').attr('type', 'text');
			$(this).addClass('active');
		} else {
			$('#auth_pwd').attr('type', 'password');
			$(this).removeClass('active');
		}
	});

	// Show recovery form
	$('#recover_recover').clickActive(function() {
		$('#authorize').hide();
		$('span[type]').hide();
		$('#passwd_recover').show();
		iRString.focus().select();
	});
	if (getUrlVar('recoverpass') === true) {
		$('#recover_recover').click();
	}

	// Cancel recovery form
	$('.recover_cancel').clickActive(function() {
		$('#authorize').show();
		$('#passwd_recover').hide();
		$('#auth_user').focus().select();
		unsetUrlVar('recoverpass');
	});

	// Recovery method switch
	iRMethod.change(function() {
		var method = iRMethod.filter(':checked').val();

		$(this)	// Crude fix for stupid nkh input bug
			.closest('form')
				.children('label')
					.removeClass('checked')
			.end()
			.find(':radio:checked')
				.closest('label')
					.addClass('checked');
		// Select method
		$('span[type]').hide();
		switch (method) {
			case 'login':
				iRString.unmask();
				// iRString.attr('placeholder', 'Логин');
				iRString.removeAttr('input-filter');
				iRTitle.text('Логин абонента:');
			break;
			case 'email':
				iRString.unmask();
				iRString.removeAttr('input-filter');
				// iRString.attr('placeholder', 'E-mail');
				$('span[type="email"]').show();
				iRTitle.text('E-mail:');
			break;
			case 'phone':
				iRString.attr('input-filter', 'phone');
				refreshFilter();
				// iRString.attr('placeholder', 'Телефон');
				$('span[type="phone"]').show();
				iRTitle.text('Телефон:');
			break;
			default:
				throw 'Wrong recover method: "'+method+'"';
		}
		setTimeout(function() {
			iRString.val('').focus();
		},0);
	});

	// Recover first stage button
	var recoverId;
	$('#passwd_recover_send').clickActive(function() {
		var method = iRMethod.filter(':checked').val();
		var data = {loading: $(this)};
		data.recover_string = $('#irecover_string').val();
		ajax_form('/acct/loginPasswordRecover/'+method, data, function(result) {
			if (!result.success) {
				niceAlert(result.msg);
			} else {
				recoverId = result.id;
				if (result.action == 'requestClarification') {
					fancyAjaxForm('#recoverClarify', '/acct/loginPasswordRecoverContacts', recoverContactsSelect, {id: recoverId}); // >> requestClarification, recoverContactsSelect
				} else if (result.action == 'selectContact') {
					ajax_post('/acct/loginPasswordRecoverContacts', {id: recoverId}, recoverContactsSelect); // >> recoverContactsSelect
				}
			}
		});
	});

	// Recover contact selection (stage 2 or 3)
	function recoverContactsSelect(res) {
		if (!res.success) {
			niceAlert(res.msg);
		} else {
			var iTbl = $('#recoverContactsTable>tbody');
			iTbl.empty();
			res.contacts.forEach(function(contact) {
				iTbl.append(
					'<tr><td>'
						+'<label><input style="position: relative;opacity:1;" type="checkbox" field="contacts[]" checked="checked" '+((contact.type == 'email')?'disabled="disabled"':'')+' />'+contact.contact+'</label>'
					+'</td></tr>'
				);
			});
			fancyAjaxForm('#recoverContacts', '/acct/loginPasswordRecoverSend', function(result) {
				niceAlert(result.msg);
			}, {id: recoverId});
		}
	}
});