$(function(){function e(e){e=e||window.event,e&&"function"==typeof e.preventDefault&&e.preventDefault()}var t={};if($(".pc_user_block").click(function(e){$(e.target).is("a")||($(this).hasClass("is-checked")?$(this).removeClass("is-checked").find(".hover_tooltip").removeClass("is-open"):$(this).addClass("is-checked").find(".hover_tooltip").addClass("is-open"))}),$(document).mouseup(function(e){var t=$(".pc_user_block");t.is(e.target)||0!==t.has(e.target).length||t.removeClass("is-checked").find(".hover_tooltip").removeClass("is-open")}),$(".has-sub-menu").on("click",function(t){e(t),$(this).closest(".side-menu-item").toggleClass("active")}),$(".channel-checkbox").on("change",function(){var e=$(this).closest(".b-channels-item");$(this).prop("checked")?e.addClass("active"):e.removeClass("active")}),$(".select-service-radio").on("change",function(){var e=$(this).closest(".l-select-service-item");$(this).prop("selected")||e.addClass("active").siblings().removeClass("active")}),t.popupFancybox={config:{margin:0,padding:0,helpers:{overlay:{locked:!1,css:{background:"rgba(153,153,153,0.8)"}}}},init:function(){$.fn.fancybox&&(jQuery.extend(jQuery.fancybox.defaults,this.config),$(".fancybox").fancybox()),$(".btn-close-fancybox").on("click",function(t){e(t),$.fancybox.close()})}},t.popupFancybox.init(),$.fn.datepicker){var a=new Date('year','month','day'),i=["Воскресенье","Понедельник","Вторник","Среда","Четверг","Пятница","Суббота"],o=["Вс","Пн","Вт","Ср","Чт","Пт","Сб"],n=["Вск","Пнд","Втр","Срд","Чтв","Птн","Сбт"],s=["Январь","Февраль","Март","Апрель","Май","Июнь","Июль","Август","Сентябрь","Октябрь","Ноябрь","Декабрь"],c=["Янв","Фев","Мар","Апр","Май","Июн","Июл","Авг","Сен","Окт","Ноя","Дек"],r=!1,l=!1;$("#ifrom").val()&&(r=!0),$("#ito").val()&&(l=!0),$("#ifrom, #ito").datepicker({dateFormat:"dd.mm.yy",dayNames:i,dayNamesMin:o,dayNamesShort:n,monthNames:s,monthNamesShort:c,firstDay:1});var d=new Date(a.getTime());d.setMonth(d.getMonth()-1),l||$("#ito").datepicker("setDate",a),r||$("#ifrom").datepicker("setDate",d),$("#ifrom").change(function(){$("#ito").datepicker("option","minDate",$(this).datepicker("getDate"))}).change(),$("#ito").change(function(){$("#ifrom").datepicker("option","maxDate",$(this).datepicker("getDate"))}).change(),$("#ito").datepicker("option","maxDate",a)}$.fn.mgnselect&&$(".mgn-select").mgnselect()});