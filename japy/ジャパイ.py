import builtins
import keyword
from typing import cast

KEYWORDS = keyword.kwlist

JAPY_KEYWORD_MAP = {
    # --- Logical and Constants ---
    "トゥルー": "True",
    "フォルス": "False",
    "ノン": "None",
    # --- Control Flow ---
    "イフ": "if",
    "エリフ": "elif",
    "エルス": "else",
    "フォー": "for",
    "ホワイル": "while",
    "ブレーク": "break",
    "コンティニュー": "continue",
    # --- Functions and Classes ---
    "デフ": "def",
    "クラス": "class",
    "リターン": "return",
    "イールド": "yield",
    "ラムダ": "lambda",
    # --- Operators ---
    "アンド": "and",
    "オア": "or",
    "ノット": "not",
    "イン": "in",
    "イズ": "is",
    # --- Error Handling ---
    "トライ": "try",
    "エクセプト": "except",
    "ファイナリー": "finally",
    "レイズ": "raise",
    # --- Modules and Scope ---
    "インポート": "import",
    "フロム": "from",
    "アズ": "as",
    "グローバル": "global",
    "ノンローカル": "nonlocal",
    # --- Async ---
    "エイシンク": "async",
    "アウェイト": "await",
    # --- Miscellaneous ---
    "パス": "pass",
    "デル": "del",
    "ウィズ": "with",
    "アサート": "assert",
}

PYTHON_TO_JAPY_MAP = {value: key for key, value in JAPY_KEYWORD_MAP.items()}

BUILTIN_FUNCTIONS = sorted(
    [
        name
        for name in dir(builtins)
        if not name.startswith("_")
        and callable(getattr(builtins, name))
        and not isinstance(getattr(builtins, name), type)
    ]
)

# Common built-in types that are frequently used as functions
BUILTIN_TYPES = sorted(
    [
        "bool",
        "int",
        "float",
        "str",
        "list",
        "tuple",
        "dict",
        "set",
        "frozenset",
        "bytes",
        "bytearray",
        "complex",
        "enumerate",
        "filter",
        "map",
        "range",
        "reversed",
        "slice",
        "zip",
        "memoryview",
        "object",
        "type",
        "super",
        "property",
        "classmethod",
        "staticmethod",
    ]
)

# All built-in objects that should have Japanese translations
ALL_BUILTINS = BUILTIN_FUNCTIONS + BUILTIN_TYPES

JAPY_BUILTINS_MAP = {
    # --- I/O and Interaction ---
    "プリント": "print",
    "インプット": "input",
    "ヘルプ": "help",
    # --- Data Structure & Collection ---
    "レン": "len",
    "サム": "sum",
    "マックス": "max",
    "ミン": "min",
    "ソーテッド": "sorted",
    "リバースド": "reversed",
    "ディル": "dir",
    # --- Functional / Iteration Tools ---
    "オール": "all",
    "エニー": "any",
    "マップ": "map",
    "フィルター": "filter",
    "ジップ": "zip",
    "スライス": "slice",
    "イター": "iter",
    "ネクスト": "next",
    "エイター": "aiter",
    "エイネクスト": "anext",
    "レンジ": "range",
    # --- Math & Numbers ---
    "エービーエス": "abs",
    "パウ": "pow",
    "ラウンド": "round",
    "ディブモッド": "divmod",
    # --- Object & Attribute ---
    "イズインスタンス": "isinstance",
    "イズサブクラス": "issubclass",
    "ハズアトリブ": "hasattr",
    "ゲットアトリブ": "getattr",
    "セットアトリブ": "setattr",
    "デルアトリブ": "delattr",
    # --- Representation & Encoding ---
    "アスキー": "ascii",
    "ビン": "bin",
    "レップ": "repr",
    "フォーマット": "format",
    "ヘックス": "hex",
    "オクト": "oct",
    "キャラ": "chr",
    "オーアールディー": "ord",
    # --- Other Core Functions ---
    "コーラブル": "callable",
    "コンパイル": "compile",
    "エバル": "eval",
    "エグゼック": "exec",
    "グローバルズ": "globals",
    "ハッシュ": "hash",
    "アイディー": "id",
    "ローカルズ": "locals",
    "オープン": "open",
    "バーズ": "vars",
    # --- Built-in Types ---
    "ブール": "bool",
    "イント": "int",
    "フロート": "float",
    "ストリング": "str",
    "リスト": "list",
    "タプル": "tuple",
    "ディクト": "dict",
    "セット": "set",
    "フローズンセット": "frozenset",
    "バイツ": "bytes",
    "バイトアレイ": "bytearray",
    "コンプレックス": "complex",
    "エニュメレート": "enumerate",
    "メモリビュー": "memoryview",
    # --- Advanced Types ---
    "オブジェクト": "object",
    "タイプ": "type",
    "スーパー": "super",
    "プロパティ": "property",
    "クラスメソッド": "classmethod",
    "スタティックメソッド": "staticmethod",
    # --- REPL/Environment Specific ---
    "ブレークポイント": "breakpoint",
    "コピーライト": "copyright",
    "クレジッツ": "credits",
    "エグジット": "exit",
    "ライセンス": "license",
    "クイット": "quit",
}

BUILTINS_PYTHON_TO_JAPY_MAP = {value: key for key, value in JAPY_BUILTINS_MAP.items()}

# Symbol mapping dictionary - supports Japanese symbol replacement
JAPY_SYMBOL_MAP = {
    # --- Brackets ---
    "（": "(",
    "）": ")",
    "【": "[",
    "】": "]",
    "｛": "{",
    "｝": "}",
    # --- Quotes ---
    "「": '"',
    "」": '"',
    "『": "'",
    "』": "'",
    # --- Punctuation ---
    "、": ",",
    "。": ".",
    "：": ":",
    "；": ";",
    "！": "!",
    "？": "?",
    "…": "...",
    # --- Operators ---
    "＋": "+",
    "－": "-",
    "×": "*",
    "÷": "/",
    "＝": "=",
    "＜": "<",
    "＞": ">",
    "％": "%",
    "＃": "#",
    "＠": "@",
    "＆": "&",
    "｜": "|",
    "＾": "^",
    "～": "~",
    "￥": "\\",
    # --- Other symbols ---
    "＿": "_",
    "＄": "$",
    "＊": "*",
    "／": "/",
    "＼": "\\",
    "・": ".",
}

# Full-width number mapping
JAPY_NUMBER_MAP = {
    "０": "0",
    "１": "1",
    "２": "2",
    "３": "3",
    "４": "4",
    "５": "5",
    "６": "6",
    "７": "7",
    "８": "8",
    "９": "9",
}

# Reverse mapping
SYMBOL_PYTHON_TO_JAPY_MAP = {value: key for key, value in JAPY_SYMBOL_MAP.items()}


# Check if all keywords are in JAPY_KEYWORD_MAP
def check_keywords():
    for word in KEYWORDS:
        if word not in PYTHON_TO_JAPY_MAP:
            raise ValueError(f"Keyword '{word}' not found in JAPY_KEYWORD_MAP")
    print("All keywords are in JAPY_KEYWORD_MAP")


# Check if all built-in functions are in JAPY_BUILTINS_MAP
def check_builtin_functions():
    missing = []
    for word in BUILTIN_FUNCTIONS:
        if word not in BUILTINS_PYTHON_TO_JAPY_MAP:
            missing.append(word)

    if missing:
        raise ValueError(
            f"Built-in functions not found in JAPY_BUILTINS_MAP: {missing}"
        )
    print("All built-in functions are in JAPY_BUILTINS_MAP")


# Check if all built-in types are in JAPY_BUILTINS_MAP
def check_builtin_types():
    missing = []
    for word in BUILTIN_TYPES:
        if word not in BUILTINS_PYTHON_TO_JAPY_MAP:
            missing.append(word)

    if missing:
        raise ValueError(f"Built-in types not found in JAPY_BUILTINS_MAP: {missing}")
    print("All built-in types are in JAPY_BUILTINS_MAP")


# Check if all built-ins (functions + types) are in JAPY_BUILTINS_MAP
def check_builtins():
    check_builtin_functions()
    check_builtin_types()

    # Additional comprehensive check
    missing = []
    for word in ALL_BUILTINS:
        if word not in BUILTINS_PYTHON_TO_JAPY_MAP:
            missing.append(word)

    if missing:
        raise ValueError(f"Built-ins not found in JAPY_BUILTINS_MAP: {missing}")

    print(f"All {len(ALL_BUILTINS)} built-ins are in JAPY_BUILTINS_MAP")
    print(f"  - Functions: {len(BUILTIN_FUNCTIONS)}")
    print(f"  - Types: {len(BUILTIN_TYPES)}")
    print(f"  - Total mappings: {len(JAPY_BUILTINS_MAP)}")


JAPY_TRANSLATION_MAP = {**JAPY_KEYWORD_MAP, **JAPY_BUILTINS_MAP}


def transpile_japy(source_code: str) -> str:
    """
    Translates a JaPy source code string into an equivalent Python source string.

    This function replaces JaPy keywords, function names, numbers, and symbols with their
    Python equivalents. The replacement is performed using regular expressions for all types.

    1. Number replacement (full-width to ASCII)
    2. Symbol replacement (Japanese/Full-width to ASCII)
    3. Keyword/function replacement (longest first, word boundary)
    """
    import re
    from typing import cast

    # 1. Replace full-width numbers with ASCII numbers
    for japy_number, python_number in JAPY_NUMBER_MAP.items():
        source_code = source_code.replace(japy_number, python_number)

    # 2. Replace symbols (punctuation, brackets, operators, etc.)
    # Sort by length descending to avoid partial replacement issues
    for japy_symbol in sorted(JAPY_SYMBOL_MAP.keys(), key=len, reverse=True):
        python_symbol = JAPY_SYMBOL_MAP[japy_symbol]
        source_code = source_code.replace(japy_symbol, python_symbol)

    # 3. Replace keywords and builtins using regex with word boundaries
    all_japy_words = JAPY_TRANSLATION_MAP.keys()
    sorted_japy_words = sorted(all_japy_words, key=len, reverse=True)
    for word_from_list in sorted_japy_words:
        japy_word = cast(str, word_from_list)
        python_word = JAPY_TRANSLATION_MAP[japy_word]
        # Use word boundary for safe replacement
        pattern = re.compile(r"\b" + re.escape(japy_word) + r"\b")
        source_code = pattern.sub(python_word, source_code)

    return source_code


SOURCE_CODE = """
デフ メイン():
    プリント('ハロー、ジャパイ！')
メイン()
"""


PYTHON_CODE = transpile_japy(SOURCE_CODE)

if __name__ == "__main__":
    check_keywords()
    check_builtins()
    print(PYTHON_CODE)
    exec(PYTHON_CODE)
