/****************************
* Personal page main script *
****************************/


// Click on active button function
$.fn.clickActive = function(callback) {
	$(this).click(function(event) {
		event.stopPropagation();
		event.preventDefault();
		if ($(this).hasClass('loading')) return;
		callback.apply(this, arguments);
	});
};

// Numeric input
$.fn.numeric = function(callback) {
	var _e = $(this);
	_e.on('keydown', function(event) {
		 if ( event.keyCode == 46 || event.keyCode == 8 || event.keyCode == 9 || event.keyCode == 27 ||
             // Allow: Ctrl+A
            (event.keyCode == 65 && event.ctrlKey === true) ||
             //Allow: Ctrl+V
			 (event.keyCode == 86 && event.ctrlKey === true) ||
			 //Allow: Ctrl+C
			 (event.keyCode == 67 && event.ctrlKey === true) ||
			 //Allow: Enter
			 (event.keyCode == 13) ||
			 // Allow: home, end, left, right
            (event.keyCode >= 35 && event.keyCode <= 39)) {
                 // let it happen, don't do anything
                 return;
		} else {
			//do refresh if it is Ctrl+R
			if (event.ctrlKey === true && event.keyCode == 82) {
				location.reload(true);
				return;
			}
            // Ensure that it is a number and stop the keypress
            if ((event.keyCode < 48 || event.keyCode > 57) && (event.keyCode < 96 || event.keyCode > 105 )) {
                event.preventDefault();
            }
        }
	});
	_e.on('input', function() {
		var _ee = $(this);
		_ee.val(_ee.val().replace(/[^\d]+/, ''));
	})
}


// Masked inputs
function refreshFilter() {
	$('[input-filter=phone]').mask("+7 (999) 999-9999");
	$('[input-filter=number]').numeric();
}

$(function () {
	/**** UI ****/
	refreshFilter();
	// Checkboxes
	$('body').find('input[type=checkbox]').closest('label').removeClass('checked');
	$('body').find('input[type=checkbox]:checked').closest('label').addClass('checked');
	$('input[type="checkbox"]').on('change',function(){
		if($(this).prop('checked')){
			$(this).closest('label').addClass('checked');
		} else {
			$(this).closest('label').removeClass('checked');
		}
	});
	// Accordions
	$("[data-accordion]").accordion({
		heightStyle: "content",
		collapsible: true
	});
	// Expandable lists
	var list_state = $.find('[data-state]');
	var condition;
	for(var i = 0; i < list_state.length; i++){
		condition = $(list_state[i]).data('state');
		if (condition == "close") {
			$(list_state[i]).text('Показать');
			$(list_state[i]).closest('.pc_sub_title').next('.pc_info_block').hide();
		} else if (condition == "open") {
			$(list_state[i]).text('Скрыть');
		}
	}
	$('.more').on('click', function(e) {
		e.preventDefault();
		var self = $(this);
		if (self.data('state') == 'close') {
			self.closest('.pc_sub_title').next('.pc_info_block').slideDown(250,function(){
				self.text('Скрыть').data('state','open').attr('data-state','open');
			});
		} else if ( self.data('state') == 'open' ) {
			self.closest('.pc_sub_title').next('.pc_info_block').slideUp(250,function(){
				self.text('Показать').data('state','close').attr('data-state','close');
			});
		}
	});

	// Fancybox close
	$('[act=fancybox-close]').click(function() {$.fancybox.close();});

	// Bootstrap select
	$('[data-bootstrap-select]').selectpicker();

	// Disabled
	$('[disabler]').change(function() {
		var dis = !XOR($(this).is('[disabler-invert]'), $(this).prop('checked')),
			clear = $(this).is('[disabler-clear]'),
			elem = $('#'+$(this).attr('disabler'));
		if (dis) {
			if (clear) {
				elem.data('_disabler_val', elem.val());
				elem.val('');
			}
			elem.prop('disabled', true);
		} else {
			if (clear) elem.val(elem.data('_disabler_val'));
			elem.prop('disabled', false);
		}
	});

	// Tabs
	$('[data-simple-tabs]').each(function() {
		$(this).tabs({
			active: 0
		}).addClass('tabs_'+$(this).find('[data-content-tab]').length+'')
	});
	$('[data-pay-tabs]').tabs();

	// Info-letter
	$('.info-letter-click').click(function(e) {
		if (e.target == this) {
			$(this).find('.text').toggle();
		}
	});
	$('.info-letter-click .text .text-container .closer').click(function() {
		$(this).closest('.text').css('display', 'none');

	});

	/**** INIT ****/
	console.log('Page loaded');
	if (window['dbg']) dbg();
});