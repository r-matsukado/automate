$(function() {
    // 実行ボタン押下イベント
    $('#btn-file-exec').click(function(event){
        // Ajaxの更新箇所を初期化
        $('#modal-content').empty();
        // HTMLでの送信をキャンセル
        event.preventDefault();
        var $form = $('#ope-fm');
        var opeKbn = $('#ope-kbn').val();

        ajaxConnect('post','/opefile/ajax/modal/init',$form.serialize())
        .done(function(data, textStatus, jqXHR){
            // 成功したときの処理
            var resultStatus = data.resultStatus;
            var modalTitle = '';
            var content = '';
            if (resultStatus == 'SUCCESS') {
                var file_list = data.file_list;
                if (!$.isEmptyObject(file_list)) {
                    modalTitle = '以下のデスクトップ上のファイルを' + (opeKbn == 'ope_kbn_move' ? '移動' : '削除') + 'します。よろしいですか？';
                    content += '<table id="modal-file-list-table" class="table table-striped">';
                    //content += '<thead><tr><th scope="col">デスクトップ上のファイル</th></tr></thead>';
                    content += '<tbody>';
                    file_list.forEach( function( value ) {
                        content += '<tr><td>' + value + '</td></tr>';
                    });
                    content += '</tbody></table>';
                     $('#btn-file-ok').show();
                } else {
                    modalTitle = 'あなたのデスクトップはキレイです！'
                    content += '<p>デスクトップ上にファイルは存在しません！</p>';
                    $('#btn-file-ok').hide();
                }

            } else if (resultStatus == 'ERROR_INVALID_PRAMETER') {
                // 引数がエラーの場合
                modalTitle = '入力値エラーです！';
                content += '<p>移動先ファルダはフォルダを含んだパスを入力してください（^人^）<br/>例)/Users/user_name/Desktop/moveFolder</p>';
                $('#btn-file-ok').hide();
            }
            $('#checkModalLabel').text(modalTitle);
            $(content).appendTo('#modal-content');


        }).fail(function(jqXHR, textStatus, errorThrown){
               // 失敗したときの処理
               // TODO:モーダルのタイトル変更

               // TODO:モーダルの内容を変更
               var errContent = '<p>エラーが発生しました！<br/>しばらくお待ちください</p>';

               // TODO:OKボタンを非活性
        });
    });

    // OKボタン押下イベント
    $('#btn-file-ok').click(function(event){
        // HTMLでの送信をキャンセル
        event.preventDefault();
        var $form = $('#ope-fm');
        ajaxConnect('post','/opefile/ajax/modal/file/exec',$form.serialize())
        .done(function(data, textStatus, jqXHR){

            var resultStatus = data.resultStatus;
            $('#checkModalLabel').modal('hide');
            // TODO:処理成功時の処理
            if (resultStatus == 'SUCCESS') {
                Alert.info('処理が完了しました！');
            } else if (resultStatus == 'ERROR_FILE_NOT_FOUND') {
                // システムエラーの場合、アラートを表示する
                Alert.warn('処理が失敗しました...処理対象のファイルがすでに消されている可能性があります');
            }
            $('#checkModal').modal('hide');
        }).fail(function(jqXHR, textStatus, errorThrown){

        });

    });


});

// TODO:js内で表示できる共通のモーダルダイアログがあった方がいいかも・・・