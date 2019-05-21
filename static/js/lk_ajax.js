/****************************
* Personal page AJAX lib   *
****************************/

// ajax post
function ajax_post(url, in_data, callback) {
	var disabled = [];
	var loading = [];
	var keepLoading = false;
	if ($('#Scrooge').length == 0) {
		niceErr('Ошибка безопасности связи #1');
		return false;
	}
	in_data[$('#Scrooge').val()] = $('#McDuck').val();
	if ('loading' in in_data) {
		if (!is_arr(in_data[loading])) in_data.loading = [in_data.loading];
		in_data.loading.forEach(function(elem) {
			$(elem).each(function() {
				if (!$(this).attr('disabled')) {
					$(this).attr('disabled', 'disabled');
					disabled.push($(this));
				}
				$(this).addClass('loading');
				loading.push($(this));
			});
		});
		delete in_data.loading;
	}
	if ('keepLoading' in in_data) {
		keepLoading = in_data.keepLoading;
		delete in_data.keepLoading;
	}
	console.dlog('ajax start', url, in_data);
    $.ajax({
        url: url,
        type: 'POST',
        dataType: 'json',
        data: JSON.stringify(in_data),
		headers: {
			'Content-type': 'application/json'
		},
        success: function(data) {
			console.dlog('ajax success', url, data);
			if (data === null) {
				niceErr('Ошибка связи #50');
			} 
			disabled.forEach(function(elem) {
				elem.removeAttr('disabled');
			});
			
            if (typeof data != 'object') {
                niceErr('Ошибка связи #1');
				loading.forEach(function(elem) {
					elem.removeClass('loading');
				});
                return false;
            }
			if (!data) {
                niceErr('Ошибка связи #2');
				loading.forEach(function(elem) {
					elem.removeClass('loading');
				});
				return false;
			}
            if (!('success' in data)) {
                niceErr('Ошибка связи #3');
				loading.forEach(function(elem) {
					elem.removeClass('loading');
				});
                return false;
            }
            if (data.success == 0) {
				loading.forEach(function(elem) {
					elem.removeClass('loading');
				});
                if (!'error' in data) {
					niceErr('Ошибка связи #4');
                    return false;
                }
				if ('errorCode' in data && $.isNumeric(data.errorCode)) {
                    if (_d.devel || _d.testing) {
                        // Devel error
                        if (data.errorCode == -65536) { // Access error: reload page
                            niceAlert('Ошибка доступа');
                        } else if (data.errorCode == -65537) { // Session expired: go to expired page
                            niceAlert('Ошибка сессии');
                        } else if (data.errorCode == -65538) {
                            niceAlert('Ошибка авторизации: '+data.error);
						} else {
                            // Devel server-side error
                            niceAlert('Ошибка '+data.errorCode+': '+data.error);
                        }
                    } else {
                        // Production error
                        if (data.errorCode == -65536) { // Access error: reload page
                            location.reload();
                        } else if (data.errorCode == -65537) { // Session expired: go to expired page
                            location.href = '/expired';
                        } else if (data.errorCode == -65538) {
                            location.href = '/?autherr='+data.error;
						} else {
							// Production server-side error
							location.href = '/showerror/'+data.errorCode;
						}
					}
				} else {
					niceErr('Ошибка связи #5');
				}
				return false;
            }
            if (!('data' in data)) {
                niceErr('Ошибка связи #6');
				loading.forEach(function(elem) {
					elem.removeClass('loading');
				});
                return false;
            }
			if (!keepLoading) {
				loading.forEach(function(elem) {
					elem.removeClass('loading');
				});
			}
            if (data.success) {
                callback(data.data, in_data);
            }
        },
        error: function(jqXHR, error, txt) {
			console.dlog('ajax error', url, jqXHR, error);
			loading.forEach(function(elem) {
				elem.removeClass('loading');
			});
			disabled.forEach(function(elem) {
				elem.removeAttr('disabled');
			});
			if (error == 'timeout') {
				niceErr('Запрос к серверу занял слишком много времени\n. Пожалуйста, проверьте Ваше интернет-соединение.\n Если оно в порядке, вероятно, на сервере возникли проблемы.');
			} else {
				if (jqXHR.status != 0) {
					if (jqXHR.status != 404) {
						if (error == 'parsererror') {
							if (jqXHR.responseText) {
								ajaxErr('Ошибка связи #7', error, jqXHR.responseText);
							} else {
								ajaxErr('Ошибка связи #8', 'empty response');
							}
						} else {
							ajaxErr('Ошибка #'+jqXHR.status, error, jqXHR.responseText);
						}
					} else {
						ajaxErr('Ошибка #'+jqXHR.status, 'not found', 'Метод '+url+' не существует');
					}
				} else {
					if (txt) error += "\n"+txt;
					niceErr('Ошибка связи #9', error);
				}
			}
        },
		complete: function() {
			console.dlog('ajax end', url);
		}
    })
}

// Ajax form
function ajax_form(url, in_data, callback) {
	var errField = false;
	if ('errField' in in_data) {
		errField = in_data.errField;
		delete in_data.errField;
	}
	var formScope = false;
	if ('formScope' in in_data) {
		formScope = in_data.formScope;
		delete in_data.formScope;
	}
	var validationErrOptions = {};
	if ('validationErrPos' in in_data) {
		validationErrOptions.pos = in_data.validationErrPos;
		delete in_data.validationErrPos;
	}
	clearvErr();
	ajax_post(url, in_data, function (data) {
		if (typeof data == 'object' && ('validationErrors' in data)) {
			console.dlog('ajax validation err', data.validationErrors);
			$.each(data.validationErrors, function(e, t) {
				$('#i'+e).validationErr(t, validationErrOptions);
			});
		} else if (typeof data == 'object' && ('multiValidationErrors' in data)) {
			if (formScope === false) throw 'Programming error: no scope for multiform';
			$.each(data.multiValidationErrors, function(e, t) {
				$(formScope).find('.'+e).validationErr(t, validationErrOptions);
			});
		} else {
			callback(data);
		}
	})
}

// Ajax error
function ajaxErr(header, text, data) {
	dispatchedErr(header, text, data);
}

// Dispatched error: if development or testing - show, else save and show user-friendly error number
var _errDispatchStarted = false;
function dispatchedErr(header, text, err_data, extraFields) {
	if (typeof header === 'undefined') header = '';
	if (typeof text === 'undefined') text = '';
	if (typeof err_data !== 'undefined') text += "\n"+err_data;
	if (_d.devel || _d.testing) {
		// Devel error
		niceErr(header, text);
	} else {
		// User-friendly error
		if (_errDispatchStarted) return;
		_errDispatchStarted = true;
		definer = header;
		if (extraFields && extraFields.definer) definer = extraFields.definer;
		var in_data = {header: header, text: text, definer: definer};
		if ($('#Scrooge').length == 0) {
			niceErr('Ошибка безопасности связи #2');
			return false;
		}
		in_data[$('#Scrooge').val()] = $('#McDuck').val();
		$.ajax('/usererr/dispatchClientError', {
			method: 'POST',
			dataType: 'text',
			data: JSON.stringify(in_data),
			headers: {
				'Content-type': 'application/json'
			},
			success: function (data) {
				if ($.isNumeric(data)) {
					if (data == '-1') {
						niceErr('Неизвестная ошибка на странице', 'Возможно, часть функций страницы не будет работать.\nПопробуйте отключить расширения браузера и открыть страницу заново.\n\nПодробности ошибки:\n'+text);
						console.log('Ignored JS error', 'header', header, 'text', text, 'data', err_data, 'extra', extraFields);
					} else {
						location.href = '/showerror/'+data;
					}
				} else {
					try {
						var decoded = JSON.parse(data);
						if (decoded && ('errorCode' in decoded)) {
							if (decoded.errorCode == -65537) {
								location.href = '/expired';
							} else {
								if ($.isNumeric(decoded.errorCode) && decoded.errorCode != 0) {
									location.href = '/showerror/'+decoded.errorCode;
								} else {
									if (decoded.error) {
										niceErr(decoded.error);
									} else {
										niceErr('Ошибка связи #10', data);
									}
								}
							}
						} else {
							niceErr('Ошибка связи #11', data);
						}
					} catch (e) {
						niceErr('Ошибка связи #12', data);
					}
				}
			},
			error: function(jqXHR, error) {
				if (error == 'timeout') {
					niceErr('Запрос к серверу занял слишком много времени\n. Пожалуйста, проверьте Ваше интернет-соединение.\n Если оно в порядке, вероятно, на сервере возникли проблемы.');
				} else {
					niceErr('Ошибка связи #13', jqXHR.status+"\n"+error+"\n"+jqXHR.responseText);
				}
			}
		})
	}
}