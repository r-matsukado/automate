$(function() {
    // アラートを定義
    Alert = {
        show: function($div, msg) {
            $div.find('.alert-msg').text(msg);
            if ($div.css('display') === 'none') {
                //コールバックで1秒後にフェードアウト
                $div.fadeIn("slow", function () {
                    $(this).delay(1000).fadeOut("slow");
                });
            }
        },
        info: function(msg) {
            this.show($('#alert-info'), msg);
        },
        warn: function(msg) {
            this.show($('#alert-warn'), msg);
        }
    }
    $('body').on('click', '.alert-close', function() {
        $(this).parents('.alert').hide();
    });

});

// Ajaxの共通接続処理
// $.ajaxはpromise()を返す
function ajaxConnect(type,url,data) {
    return $.ajax({
            type: type,
            url: url,
            data: data,
            timeout: 10000,
            beforeSend: function(xhr, settings) {
               xhr.setRequestHeader("X-CSRFToken", $("input[name='csrfmiddlewaretoken']").val());
            },
            //contentType: "application/json;charset=utf-8",
            //dataType: "json"
        });
}
