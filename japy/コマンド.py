"""
JaPy - コマンドラインインターフェース

`python -m japy` および `japy` コマンドのエントリーポイント。
"""

import sys
from pathlib import Path

from absl import app, flags, logging

from .ジャパイ import check_builtins, check_keywords, transpile_japy

FLAGS = flags.FLAGS

flags.DEFINE_string("input", None, "トランスパイルする.japyファイル")
flags.DEFINE_string("output", None, "出力Pythonファイル（デフォルト: 元ファイル名.py）")
flags.DEFINE_boolean("execute", False, "トランスパイルされたPythonコードを実行")
flags.DEFINE_boolean("show", True, "トランスパイルされたPythonコードを表示")
flags.DEFINE_boolean("validate", False, "キーワードと組み込み関数のマッピングを検証")
flags.DEFINE_boolean("debug", False, "デバッグ出力を有効化")
flags.DEFINE_boolean(
    "strict", False, "ストリクトモード：tokenizerでより正確なコード変換を行う"
)


def main(argv):
    """コマンドラインインターフェースのメイン関数。"""
    if FLAGS.debug:
        logging.set_verbosity(logging.DEBUG)
        logging.debug("デバッグモードが有効になりました")
        logging.debug("非フラグ引数: %s", argv)

    if FLAGS.validate:
        logging.info("キーワードと組み込み関数のマッピングを検証中...")
        try:
            check_keywords()
            check_builtins()
            logging.info("✓ すべての検証が成功しました")
        except ValueError as e:
            logging.error("検証に失敗しました: %s", e)
            sys.exit(1)
        return

    if not FLAGS.input:
        logging.error("入力ファイルが必要です（--input=<ファイル>を使用してください）")
        sys.exit(1)

    input_path = Path(FLAGS.input)
    if not input_path.exists():
        logging.error("入力ファイルが存在しません: %s", FLAGS.input)
        sys.exit(1)

    try:
        with open(input_path, "r", encoding="utf-8") as f:
            japy_code = f.read()
        logging.debug("%sから%d文字を読み込みました", FLAGS.input, len(japy_code))
    except Exception as e:
        logging.error("入力ファイルの読み込みに失敗しました: %s", e)
        sys.exit(1)

    try:
        python_code = transpile_japy(japy_code, strict=FLAGS.strict)
        if FLAGS.strict:
            logging.info("ストリクトモード：tokenizerで正確に変換します")
        else:
            logging.debug("簡易モード（regex）で変換します")
        logging.debug("トランスパイルが正常に完了しました")
    except Exception as e:
        logging.error("トランスパイルに失敗しました: %s", e)
        sys.exit(1)

    if FLAGS.output:
        try:
            with open(FLAGS.output, "w", encoding="utf-8") as f:
                f.write(python_code)
            logging.info("トランスパイルされたコードを%sに書き込みました", FLAGS.output)
        except Exception as e:
            logging.error("出力ファイルの書き込みに失敗しました: %s", e)
            sys.exit(1)
    elif FLAGS.show:
        print("# トランスパイルされたPythonコード:")
        print(python_code)

    if FLAGS.execute:
        logging.info("トランスパイルされたコードを実行中...")
        try:
            exec(python_code)
        except Exception as e:
            logging.error("実行に失敗しました: %s", e)
            sys.exit(1)


def cli_main():
    """コマンドライン用のエントリーポイント。"""
    app.run(main)
