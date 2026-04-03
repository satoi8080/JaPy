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

from importlib.metadata import PackageNotFoundError, version

from .ジャパイ import (
    ALL_BUILTINS,
    BUILTIN_FUNCTIONS,
    BUILTIN_TYPES,
    BUILTINS_PYTHON_TO_JAPY_MAP,
    JAPY_BUILTINS_MAP,
    JAPY_KEYWORD_MAP,
    JAPY_TRANSLATION_MAP,
    KEYWORDS,
    PYTHON_TO_JAPY_MAP,
    SOURCE_CODE,
    check_builtin_functions,
    check_builtin_types,
    check_builtins,
    check_keywords,
    transpile_japy,
)

try:
    __version__ = version("japy-lang")
except PackageNotFoundError:
    __version__ = "unknown"

__all__ = [
    "transpile_japy",
    "KEYWORDS",
    "JAPY_KEYWORD_MAP",
    "PYTHON_TO_JAPY_MAP",
    "BUILTIN_FUNCTIONS",
    "BUILTIN_TYPES",
    "ALL_BUILTINS",
    "JAPY_BUILTINS_MAP",
    "BUILTINS_PYTHON_TO_JAPY_MAP",
    "JAPY_TRANSLATION_MAP",
    "check_keywords",
    "check_builtin_functions",
    "check_builtin_types",
    "check_builtins",
    "SOURCE_CODE",
    "__version__",
]
