"""
JaPy - 日本語Python方言

このモジュールはジャパイ.pyのエイリアスとして機能し、
ASCIIファイル名を好むユーザーに日本語Python方言機能への
簡単なアクセスを提供します。

すべての機能はメインのジャパイモジュールからインポートされます。
さらに、このモジュールはコマンドライン インターフェース機能を提供します。
"""

import sys
from pathlib import Path
from absl import app
from absl import flags
from absl import logging

# メインのジャパイモジュールからすべての機能をインポート
from .ジャパイ import *

FLAGS = flags.FLAGS

# コマンドラインフラグを定義
flags.DEFINE_string('input', None, 'トランスパイルする.japyファイル')
flags.DEFINE_string('output', None, '出力Pythonファイル（デフォルト: 元ファイル名.py）')
flags.DEFINE_boolean('execute', False, 'トランスパイルされたPythonコードを実行')
flags.DEFINE_boolean('show', True, 'トランスパイルされたPythonコードを表示')
flags.DEFINE_boolean('validate', False, 'キーワードと組み込み関数のマッピングを検証')
flags.DEFINE_boolean('debug', False, 'デバッグ出力を有効化')

# inputはmain()で条件付きで必須としてマークされます

# 明確性のためにメインコンポーネントを明示的に再エクスポート
__all__ = [
    'KEYWORDS',
    'JAPY_KEYWORD_MAP',
    'PYTHON_TO_JAPY_MAP',
    'BUILTIN_FUNCTIONS',
    'JAPY_BUILTINS_MAP',
    'BUILTINS_PYTHON_TO_JAPY_MAP',
    'JAPY_TRANSLATION_MAP',
    'transpile_japy',
    'check_keywords',
    'check_builtins',
    'SOURCE_CODE',
    'PYTHON_CODE'
]


def main(argv):
    """コマンドラインインターフェースのメイン関数。"""
    if FLAGS.debug:
        logging.set_verbosity(logging.DEBUG)
        logging.debug('デバッグモードが有効になりました')
        logging.debug('非フラグ引数: %s', argv)

    # 検証モード
    if FLAGS.validate:
        logging.info('キーワードと組み込み関数のマッピングを検証中...')
        try:
            check_keywords()
            check_builtins()
            logging.info('✓ すべての検証が成功しました')
        except ValueError as e:
            logging.error('検証に失敗しました: %s', e)
            sys.exit(1)
        return

    # 入力ファイルを読み込み（非検証モードでは必須）
    if not FLAGS.input:
        logging.error('入力ファイルが必要です（--input=<ファイル>を使用してください）')
        sys.exit(1)

    input_path = Path(FLAGS.input)
    if not input_path.exists():
        logging.error('入力ファイルが存在しません: %s', FLAGS.input)
        sys.exit(1)

    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            japy_code = f.read()
        logging.debug('%sから%d文字を読み込みました', FLAGS.input, len(japy_code))
    except Exception as e:
        logging.error('入力ファイルの読み込みに失敗しました: %s', e)
        sys.exit(1)

    # コードをトランスパイル
    try:
        python_code = transpile_japy(japy_code)
        logging.debug('トランスパイルが正常に完了しました')
    except Exception as e:
        logging.error('トランスパイルに失敗しました: %s', e)
        sys.exit(1)

    # トランスパイルされたコードを出力
    if FLAGS.output:
        # ファイルに書き込み
        try:
            with open(FLAGS.output, 'w', encoding='utf-8') as f:
                f.write(python_code)
            logging.info('トランスパイルされたコードを%sに書き込みました', FLAGS.output)
        except Exception as e:
            logging.error('出力ファイルの書き込みに失敗しました: %s', e)
            sys.exit(1)
    elif FLAGS.show:
        # 標準出力に印刷
        print("# トランスパイルされたPythonコード:")
        print(python_code)

    # トランスパイルされたコードを実行
    if FLAGS.execute:
        logging.info('トランスパイルされたコードを実行中...')
        try:
            exec(python_code)
        except Exception as e:
            logging.error('実行に失敗しました: %s', e)
            sys.exit(1)


if __name__ == '__main__':
    app.run(main)
