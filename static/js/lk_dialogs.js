/****************************
* Personal page dialogs lib *
****************************/


// Fancybox dialog wrapper
function fancyDialog(div, callback, closeCallback) {
	$.fancybox.open(div, {
		afterClose: function() {
			closeCallback && closeCallback();
		}
	});
	// Bind fancyCancel button to fancybox close
	$(div).find('.fancyCancel').unbind().click(function () { $.fancybox.close(); });
	// Bind fancyOk button to ajax post
	$(div).find('.fancyOk').addClass('g-btn btn-primary').unbind().click(function () {
		$.fancybox.close();
		callback && callback();
	});
}

// Fancybox ajax dialog wrapper
function fancyAjaxYesNo(div, url, data, callback) {
	$.fancybox(div);
	// Bind fancyCancel button to fancybox close
	$(div).find('.btn-close-fancybox').unbind().clickActive(function () { $.fancybox.close(); });
	// Bind fancyOk button to ajax post
	$(div).find('.btn-primary').unbind().clickActive(function () {
		data.loading = [$(this)];
		ajax_post(url, data, function (res) {
			$.fancybox.close();
			callback(res);
		});
	});
}

// Fancybox ajax form wrapper. Fields is array of input ids without i (they are keys of posted data)
function fancyAjaxForm(div, url, callback, data) {
	$.fancybox.open(div, {
		afterClose: function() {
			clearvErr();
		}
	});
	var fld = $(div).find('[field]:not([disabled])');
	if (fld.length > 0) fld[0].focus();
	// Bind fancyCancel button to fancybox close
	$(div).find('.fancyCancel').unbind().clickActive(function () { $.fancybox.close(); });
	// Bind fancyOk button to ajax post
	$(div).find('.fancyOk').unbind().clickActive(function () {
		if (!data) data = {};
		data['loading'] = [$(this)];
		var fldIdx = {};
		$(div).find('[field]').each(function() {
			if (!$(this).is('[fieldExclude]')) {
				var field = $(this).attr('field');
				var matches, val,
					is_cb = false;
				if ($(this).is(':checkbox')) {
					val = $(this).prop('checked');
					is_cb = true;
				} else {
					val = $(this).val();
				}
				if (matches = field.match(/^(.+)\[\]$/)) { // arr field
					if (!(matches[1] in data)) data[matches[1]] = [];
					if (!is_cb) {
						data[matches[1]].push(val);
					} else {
						if (!(matches[1] in fldIdx)) fldIdx[matches[1]] = -1;
						fldIdx[matches[1]]++;
						if (val) {
							data[matches[1]].push(fldIdx[matches[1]]);
						}
					}
				} else { // plain field
					data[field] = val;
				}
			}
		});
		ajax_form(url, data, function (res) {
			$.fancybox.close();
			callback(res);
		});
	});
}

// Fancybox window
function fancyWindow(content, callback) {
	var div = $('<div/>');
	div.append(content);
	var content = '<div id="_fancyDiv" class="b-popup popup-sm"><div class="b-popup-body">'+div.html()+'</div><div class="b-popup-footer"><button class="g-btn btn-primary btn-close-fancybox">ОК</button></div></div>';
	div.remove();
	$.fancybox({
		content: content,
		afterClose: function() {
			$('#_fancyDiv').remove();
			callback && callback();
		}
	});
	$('#_fancyDiv').find('button').click(function () {$.fancybox.close()});
}

// Nice alert (to use as window alert)
function niceAlert(text, header, callback) {
	// Make text an escaped html with newline changed to <br/> 
	var lines = [];
	text.split("\n").forEach(function (line) {
		var div = $('<div/>');
		div.text(line);
		lines.push(div.html());
	});
	text = lines.join('<br/>');
	// Create content div
	var div = $('<div/>');
	div.html(text);
	// Make header if needed
	if (header) {
		var h4 = $('<h4/>');
		h4.text(header);
		div.prepend(h4);
	}
	// Call fancyWindow
	fancyWindow(div, callback);
}

    
// Show push message by id function
function showPushMessage(id, closeCallback) {
    console.dlog('show push message', id);
    ajax_post('/messages/getf', {id: id, loading: $(this)}, function (data) { // Get message
        $('#_msgMsgHead').html(data.ftitle);
        $('#_msgMsgBody').html(data.fmessage);
        fancyDialog($('#_msgMsg'), function() {
            ajax_post('/messages/setread', {id: id}, function(){});
        }, closeCallback);
    });
}