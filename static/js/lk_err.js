/**************************************
* Personal page error handlers script *
**************************************/

// Nice error
var __errReady = false;
$(function(){
	__errReady = true;
	if (__errQueue.length > 0) {
		__niceErr.apply(this, __errQueue.shift());
	}
});
var __errVisible = false;
var __errQueue = [];
function __niceErr(error, text) {
	__errVisible = true;
	// Make text an escaped html with newline changed to <br/> 
	var lines = [];
	if (typeof text == 'object' && 'message' in text) {
		text = text.message + ( ('code' in text)?' ('+text.code+')':'' );
	} else if (typeof text == 'undefined') {
		text = '';
	}
	text.split("\n").forEach(function (line) {
		var div = $('<div/>');
		div.text(line);
		lines.push(div.html());
	});

	// Fill elements
	$('#_errMsg').addClass('b-popup popup-sm');
	$('#_errMsgHead').text(error);
	$('#_errMsgBody').addClass('b-popup-body').html(lines.join('<br/>').replace('\n', '<br/>'));
	// Show alert
	fancyDialog('#_errMsg', undefined, function() {
		if (__errQueue.length > 0) {
			setTimeout(function() {
				__niceErr.apply(this, __errQueue.shift());
			}, 200);
		} else {
			__errVisible = false;
		}
	});
}
function niceErr(error, text) {
	if (__errVisible || !__errReady || __errQueue.length > 0) {
		__errQueue.push([error, text]);
	} else {
		__niceErr(error, text);
	}
}


// JQuery validation error
function clearvErr() {
	$('.validation-err').each(function() {
		$(this).removeClass('error validation-err').qtip('destroy');
	});
}
$.fn.resetErr = function () {
	if ($(this).length < 1) return;
	$(this).removeClass('validation-err');
	$(this).qtip('destroy', true);
	$(this).removeClass('error');
}
$.fn.validationErr = function(message, options) {
	if (typeof options === 'undefined') options = {};
	$(this).addClass('error');
	$(this).addClass('validation-err');
	var classes = 'qtip-error';
	if ('addClasses' in options) {
		classes += ' '+options.addClasses;
	}
	var my = ('pos' in options)? options.pos.my : 'left center';
	var at = ('pos' in options)? options.pos.at : 'center right';
	$(this).qtip({
		content: {
			text: message
		},
		position: {
			my: my,
			at: at,
			adjust: {
				x: 10,
				y: -10,
				method: 'shift flip',
				resize: true,
				scroll: true,
			}
		},
		show: {
			event: false,
			ready: true
		},
		hide: false,
		style: {
			tip: {
			// corner: true
			},
			width: 200,
			def: false,
			classes: classes
		}
	});
	var _elem = $(this);
	if ('clearFields' in options) {
		$(options.clearFields).one('change', function() {
			_elem.resetErr();
		});
		$(options.clearFields).one('input', function() {
			_elem.resetErr();
		});
	}
	if ('sneaky' in options) {
		if (options.sneaky) {
			$(document).one('mouseup', function() {
				_elem.resetErr();
			});
		}
	}
	$(this).one('change', function() {
		$(this).resetErr();
	});
	$(this).one('input', function() {
		$(this).resetErr();
	});
	if ($('input.error:focus').length == 0)
		$(this).focus();
	return false;
}

// On error: JS AJAX error handler
window.onerror = function(msg, url, line, col, error) {
	var extra = !col ? '' : '\ncolumn: ' + col;
	extra += !error ? '' : '\nerror: ' + error;
	var pathArray = location.href.split( '/' );
	var protocol = pathArray[0];
	var host = pathArray[2];
	var baseurl = protocol + '//' + host;
	if ('dispatchedErr' in window && url.startsWith(baseurl)) {
		dispatchedErr('Javascript error', 'Error: ' + msg + '\nurl: ' + url + '\nline: ' + line + extra, '', {definer: url+':'+line+':'+col});
	} else {
		alert('Javascript error\n' + msg + '\nurl: ' + url + '\nline: ' + line + extra, '', {definer: url+':'+line+':'+col});
	}
	return false;
}