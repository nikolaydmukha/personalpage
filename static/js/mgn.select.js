$.fn.mgnselect = function(params) {
	var 
		$elem = $(this),
		that = this;

	$elem.each(function(){
		var 
			$this = $(this),
			$node = buildHtml($this);
		
		$node.insertBefore($this);
	});
	
	function buildHtml($elem) {
		$elem.hide();
		
		var 
			bFind = false;
			node = '\
				<div class="mgn-select-wrap"> \
					<div class="mgn-select-choosed"></div>\
					<div class="mgn-select-list">\
					</div>\
				</div>\
			';
		
		$node = $(node);

		$node.addClass($elem.data("layout") ? $elem.data("layout") : "basic");

		$('li', $elem).each(function(){
			var html = $(this).html(),
				$newNode = null;
			if($(this).is('[data-selected]')) {
				bFind = true;
				$('.mgn-select-choosed', $node).html(html);
				$('.mgn-select-choosed', $node).data('elem', $(this));
				
			}
			
			$newNode = $('<div/>')
				.addClass('mgn-select-item')
				.html(html);

			$.each($(this).data(), function(index){
				$newNode.attr('data-'+index, typeof this == "object" ? JSON.stringify(this) : this);
			});
			
			$('.mgn-select-list', $node).append($newNode);
		});
		
		if(!bFind) {
			var $li = $('li:first', $elem),
				html = $li.html();
			
			$('.mgn-select-choosed', $node).html(html);
			$('.mgn-select-choosed', $node).data('elem', $li);
			$('.mgn-select-item:first', $node).addClass('active');
		}
		
		return $node;
	}
	
	$(document).on('click touchend', '.mgn-select-wrap', function(e) {
		e.stopPropagation();
		$('.mgn-select-wrap').not($(this)).removeClass('active');
		$(this).toggleClass('active');
		return false;
	});
	
	$(document).on('click touchend', '.mgn-select-item', function(e) {
		e.stopPropagation();
		var $this = $(this),
			$choosed = $this.parents('.mgn-select-wrap').find('.mgn-select-choosed');

		$(this).siblings('.mgn-select-item').removeClass('active');
		$(this).addClass('active');
		
		$choosed.html($this.html());
		$choosed.data('elem', $this);
		
		$(this).trigger('mgn:selected', {elem : this});
		$('.mgn-select-wrap').removeClass('active');
		
		return false;
	});
	
	$(document).on('click touchend', function(){
		$('.mgn-select-wrap').removeClass('active');
	});
}