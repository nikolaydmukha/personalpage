/****************************
*  Personal page UI script  *
****************************/

$(function() {
	/**** UI ****/
	// Small user menu
	// $('.pc_user_block').click(function(e) {
	// 	if ($(e.target).is('a')) return;
	// 	if (!$(this).hasClass('is-checked')) {
	// 		$(this).addClass('is-checked').find('.hover_tooltip').addClass('is-open');
	// 	} else {
	// 		$(this).removeClass('is-checked').find('.hover_tooltip').removeClass('is-open');
	// 	}
	// });
	$(document).mouseup(function (e) {
		var container = $('.pc_user_block');
		if (!container.is(e.target) && container.has(e.target).length === 0) {
			container.removeClass('is-checked').find('.hover_tooltip').removeClass('is-open');
		}
	});
	// Main menu
	if ($('#main_menu').length > 0) {
		// Expand main menu item for active subitem
		var active = false;
		var _e = $('#main_menu').find('li a.active');
		if (_e.length > 0) {
			active = $(_e[0]).closest('div').prev().index('.ui-accordion-header');
			console.dlog('setting active tab', active);
		}
		$('#main_menu').accordion({
			heightStyle: "content",
			active: active,
			collapsible: true,
			header: 'h5'
		});
	}
});