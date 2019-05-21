/****************************************
*  Personal page UI after login script  *
****************************************/

$(function() {
    var regularHandlers = {};
	/**** Regular action functions ****/
    regularHandlers.clarifyContactName = function(callback) {
        if (typeof callback !== 'function') callback = function() {};
        console.dlog('clarify contact name: not implemented');
        callback();
    }
    
	/**** Just logged in handler: on login actions ****/
    // Show regular actions
    function showRegulars(callback) {
        if (typeof callback !== 'function') callback = function() {};
        console.dlog('show regulars', _d.regular);
        var regular = _d.regular.slice();
        function nextRegular() {
            if (!regular.length) {
                console.dlog('regulars complete');
                return callback();
            }
            var next = regular.shift();
            if (!Object.prototype.hasOwnProperty.call(regularHandlers, next)) {
                throw 'Regular action not found: '+next;
            }
            if (typeof regularHandlers[next] !== 'function') {
                throw 'Regular action '+next+' is not callable';
            }
            regularHandlers[next](nextRegular);
        }
        nextRegular();    
    }
    // Show push messages
    function showPushes(callback) {
        if (typeof callback !== 'function') callback = function() {};
        console.dlog('show pushes');
        ajax_post('/messages/getpush', {loading: $(this)}, function (data) { // Get push messages
            var pushMessages = data.messages;
            function nextPushMessage() {
                if (!pushMessages.length) {
                    console.dlog('pushes complete');
                    return callback();
                }
                var next = pushMessages.shift();
                showPushMessage(next.id, nextPushMessage);
            }
            nextPushMessage();
        });
    }
	/**** Just logged in handler: on login actions ****/
	if (_d.justLoggedIn) {
        console.dlog('Just logged in. Do onlogin actions')
        // Do logged in notifications
		showPushes(showRegulars);
	}
});