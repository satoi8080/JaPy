"""
JaPy - 日本語Python方言

このパッケージは日本語でPythonプログラミングを可能にする
トランスパイラーです。

使用例:
    import japy

    # .japyファイルをトランスパイル
    python_code = japy.transpile_japy(japy_source_code)

    # キーワードマッピングを確認
    japy.check_keywords()
    japy.check_builtins()
"""

# メインモジュールからすべての機能をインポート
try:
    from .japy import *
except ImportError:
     # Unicodeファイル名に問題がある場合のフォールバック
    from .core import *

# バージョン情報
__version__ = "0.1.1"
__author__ = "Zhe"
__email__ = "i@zzhe.dev"

# パッケージレベルでの主要な機能を再エクスポート
__all__ = [
    # コア機能
    'transpile_japy',

    # マッピング辞書
    'KEYWORDS',
    'JAPY_KEYWORD_MAP',
    'PYTHON_TO_JAPY_MAP',
    'BUILTIN_FUNCTIONS',
    'BUILTIN_TYPES',
    'ALL_BUILTINS',
    'JAPY_BUILTINS_MAP',
    'BUILTINS_PYTHON_TO_JAPY_MAP',
    'JAPY_TRANSLATION_MAP',

    # 検証関数
    'check_keywords',
    'check_builtin_functions',
    'check_builtin_types',
    'check_builtins',

    # 定数
    'SOURCE_CODE',
    'PYTHON_CODE',

    # メタデータ
    '__version__',
    '__author__',
    '__email__',
]