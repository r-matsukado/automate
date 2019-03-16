from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .src.main.file_utils import file_ope
import json
from django.http import JsonResponse
import logging
import sys
from enum import Enum

class ResultStatus(Enum):
    SUCCESS = 'SUCCESS'

    ERROR_INVALID_PRAMETER = 'ERROR_INVALID_PRAMETER'
    ERROR_FILE_NOT_FOUND = 'ERROR_FILE_NOT_FOUND'


logger = logging.getLogger(__name__)
# モジュールごとにログを出力する設定

# 画面初期表示
def index(request):
    return render(request, 'opefile/index.html')

# モーダル初期表示
def ajaxInitForModal(request):
    '''
    モーダル初期表示に、フィイルの一覧をJSON形式で返す
    :return:
    '''
    logger.info('>>> start : {}'.format(sys._getframe().f_code.co_name))
    context = {}
    if request.method == 'POST' and request.is_ajax:

        # 操作区分が移動の場合のみ、パスの入力チェックを行う
        if (request.POST.get('ope-kbn') == 'ope_kbn_move') :
            # 引数チェック
            if not file_ope.is_folder_path(request.POST.get('move_folder_path')) :
                context = {
                    'resultStatus' : ResultStatus.ERROR_INVALID_PRAMETER.value,
                    'file_list' : []
                }
                return JsonResponse(context)

        # ファイルの一覧を取得
        file_list = file_ope.get_desktop_file_list()
        context = {
            'resultStatus' : ResultStatus.SUCCESS.value,
            'file_list': file_list,
        }
    return JsonResponse(context)

# ファイル操作を実行
def opeFileExec(request):
    context = {}
    if request.method == 'POST' and request.is_ajax:
        try:
            # 操作区分に応じて処理
            ope_kbn = request.POST.get('ope-kbn')
            move_folder_path = request.POST.get('move_folder_path')
            if ope_kbn == 'ope_kbn_move':
                file_ope.move_file_on_desktop(move_folder_path)
                context = {'resultStatus' : ResultStatus.SUCCESS.value}
                logger.info('>>> success : move file')
            elif ope_kbn == 'ope_kbn_delete':
                file_ope.delete_file_on_desktop()
                context = {'resultStatus': ResultStatus.SUCCESS.value}
                logger.info('>>> success : delete file')
        # このエラーは事前にチェックするので、発生しない可能性がある
        except SyntaxError:
            context = {'resultStatus' : ResultStatus.ERROR_INVALID_PRAMETER.value,}
            logger.error('>>> ERROR_INVALID_PRAMETER : move file')

        except FileNotFoundError:
            context = {'resultStatus' : ResultStatus.ERROR_FILE_NOT_FOUND.value,}
            logger.error('>>> ERROR_FILE_NOT_FOUND : move file')

    return JsonResponse(context)