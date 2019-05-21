/**
 * Created by NKH on 01.07.14.
 */
$(document).ready(function () {
    //стилизованные радио - чекбоксы
    // html scheme

    //radio
    //<label class="radio checked">
    //<input type="radio" name="group-name">
    //</label>

    //checkbox
    //<label class="checkbox checked">
    //<input type="checkbox">
    //</label>


    $('body').find('input[type=checkbox]:checked').closest('label').addClass('checked').closest('[data-item]').addClass('active');
    $('body').find('input[type=radio]:checked').closest('label').addClass('checked').closest('[data-item]').addClass('active');

    $('body').find('input[type=radio]:disabled').closest('label').addClass('disabled');
    $('body').find('input[type=checkbox]:disabled').closest('label').addClass('disabled');
    var el;
    $('label').on('mouseup', function () {

        var _this = $(this);
        var input = _this.find('input');
        var name = input.attr('name');
        var label;

        if(!input.prop("disabled")) {
            if( _this.hasClass('radio') || _this.hasClass('checkbox') ) {
                label = _this;
            } else  {
                label = _this.find('label.radio, label.checkbox');
            }

            if(label.hasClass('checkbox')) {
                if(input.prop('checked') == false) {
                    label.addClass('checked').closest('[data-item]').addClass('active');
                }
                else {
                    label.removeClass('checked').closest('[data-item]').removeClass('active');
                }
            }
            else if(label.hasClass('radio')) {

                if (!label.hasClass('checked')) {

                    var allInputs = label.closest('form').find('label.radio input[name='+name+']');

                    for (var i = 0; i < allInputs.length; i++) {

                        if($(allInputs[i]).prop('checked')) {

                            $(allInputs[i]).prop('checked',false).closest('label').removeClass('checked').closest('[data-item]').removeClass('active');

                        }

                    }
                    label.addClass('checked').closest('[data-item]').addClass('active');

                } else if(input.attr('type')=='checkbox') {
                    label.removeClass('checked').closest('[data-item]').removeClass('active');
                }
            }
        }
    });
});