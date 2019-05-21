/****************************
* Personal page tools lib   *
****************************/

/***** Fallbacks ******/
if (!('forEach' in Array.prototype)) {
	Array.prototype.forEach= function(action, that /*opt*/) {
		for (var i= 0, n= this.length; i<n; i++)
			if (i in this)
				action.call(that, this[i], i, this);
	};
}

/***** Variables ******/
var ruDayNames = ['Воскресенье', 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота'];
var ruDayNamesMin = ['Вс', 'Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб'];
var ruDayNamesShort = ['Вск', 'Пнд', 'Втр', 'Срд', 'Чтв', 'Птн', 'Сбт'];
var ruMonthNames = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'];
var ruMonthNamesShort = ['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн', 'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек'];

/***** Type helpers ******/
function is_arr(val) {
	return Object.prototype.toString.call(val) === '[object Array]';
}
function XOR(a,b) {
  return ( a || b ) && !( a && b );
}


/***** Misc helpers *****/
// Short reload wrapper (comfortable usage of context)
function reload() {
	location.reload();
}

///////// Format time function
function zerofy(i) {
	if (String(i).length < 2) return '0'+i;
	return i;
}
function formatTime(d) {
	return zerofy(d.getHours())+':'+zerofy(d.getMinutes())+' '+zerofy(d.getMonth() + 1)+'.'+zerofy(d.getDate())+'.'+d.getFullYear();
}


// Console log
console.dlog = function() {
	if (_d.devel) console.log.apply(this, arguments);
}
console.pdlog = function (label, obj) {
	if (_d.devel) console.log(label, JSON.stringify(obj, null, '\t'));
}

// URL args
function getUrlVars(){
	var vars = {}, hash, val;
	idx = window.location.href.indexOf('?');
	if (idx == -1) return vars;
	var hashes = location.href.slice(idx + 1).split('&');
	for (var i = 0; i < hashes.length; i++) {
		hash = hashes[i].split('=');
		idx = hash.shift();
		val = hash.length? hash.join('=') : true;
		vars[idx] = val;
	}
	return vars;
}
function getUrlVar(name) {
	return getUrlVars()[name];
}
function unsetUrlVar(name) {
	var vars = getUrlVars(), parts = [], path, idx = window.location.href.indexOf('?');
	if (idx == -1) return;
	$.each(vars, function (i,v) {
		if (i != name) {
			parts.push(i+(v === true ? '' : '='+v));
		}
	});
	path = location.href.slice(0, idx)+(parts.length ? '?'+parts.join('&') : '');
	if (path != location.href) location.href = path;
}

// Storage
function storageSet(name, val) {
	if (typeof(Storage) === 'undefined') return NULL;
	localStorage[name] = JSON.stringify({val: val});
	return true;
}
function storageGet(name) {
	if (typeof(Storage) === 'undefined') return NULL;
	if (name in localStorage) {
		var val = JSON.parse(localStorage[name]);
		return val.val;
	}
	return NULL;
}
function storageExists(name) {
	if (typeof(Storage) === 'undefined') return NULL;
	return (name in localStorage);
}
function storageDel(name) {
	if (typeof(Storage) === 'undefined') return NULL;
	localStorage.removeItem(name);
	return true;
}
function storageSupport() {
	return (typeof(Storage) !== 'undefined')
}