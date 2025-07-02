import keyword
import builtins
import re
from typing import cast

KEYWORDS = keyword.kwlist

JAPY_KEYWORD_MAP = {
    # --- Logical and Constants ---
    'トゥルー': 'True',
    'フォルス': 'False',
    'ノン': 'None',

    # --- Control Flow ---
    'イフ': 'if',
    'エリフ': 'elif',
    'エルス': 'else',
    'フォー': 'for',
    'ホワイル': 'while',
    'ブレーク': 'break',
    'コンティニュー': 'continue',

    # --- Functions and Classes ---
    'デフ': 'def',
    'クラス': 'class',
    'リターン': 'return',
    'イールド': 'yield',
    'ラムダ': 'lambda',

    # --- Operators ---
    'アンド': 'and',
    'オア': 'or',
    'ノット': 'not',
    'イン': 'in',
    'イズ': 'is',

    # --- Error Handling ---
    'トライ': 'try',
    'エクセプト': 'except',
    'ファイナリー': 'finally',
    'レイズ': 'raise',

    # --- Modules and Scope ---
    'インポート': 'import',
    'フロム': 'from',
    'アズ': 'as',
    'グローバル': 'global',
    'ノンローカル': 'nonlocal',

    # --- Async ---
    'エイシンク': 'async',
    'アウェイト': 'await',

    # --- Miscellaneous ---
    'パス': 'pass',
    'デル': 'del',
    'ウィズ': 'with',
    'アサート': 'assert',
}

PYTHON_TO_JAPY_MAP = {value: key for key, value in JAPY_KEYWORD_MAP.items()}

BUILTIN_FUNCTIONS = sorted([name for name in dir(builtins) if not name.startswith('_') and callable(getattr(builtins, name)) and not isinstance(getattr(builtins, name), type)])

JAPY_BUILTINS_MAP = {
    # --- I/O and Interaction ---
    'プリント': 'print',
    'インプット': 'input',
    'ヘルプ': 'help',

    # --- Data Structure & Collection ---
    'レン': 'len',
    'サム': 'sum',
    'マックス': 'max',
    'ミン': 'min',
    'ソーテッド': 'sorted',
    'リバースド': 'reversed',
    'ディル': 'dir',

    # --- Functional / Iteration Tools ---
    'オール': 'all',
    'エニー': 'any',
    'マップ': 'map',
    'フィルター': 'filter',
    'ジップ': 'zip',
    'スライス': 'slice',
    'イター': 'iter',
    'ネクスト': 'next',
    'エイター': 'aiter',
    'エイネクスト': 'anext',
    'レンジ': 'range',

    # --- Math & Numbers ---
    'エービーエス': 'abs',
    'パウ': 'pow',
    'ラウンド': 'round',
    'ディブモッド': 'divmod',

    # --- Object & Attribute ---
    'イズインスタンス': 'isinstance',
    'イズサブクラス': 'issubclass',
    'ハズアトリブ': 'hasattr',
    'ゲットアトリブ': 'getattr',
    'セットアトリブ': 'setattr',
    'デルアトリブ': 'delattr',

    # --- Representation & Encoding ---
    'アスキー': 'ascii',
    'ビン': 'bin',
    'レップ': 'repr',
    'フォーマット': 'format',
    'ヘックス': 'hex',
    'オクト': 'oct',
    'キャラ': 'chr',
    'オーアールディー': 'ord',

    # --- Other Core Functions ---
    'コーラブル': 'callable',
    'コンパイル': 'compile',
    'エバル': 'eval',
    'エグゼック': 'exec',
    'グローバルズ': 'globals',
    'ハッシュ': 'hash',
    'アイディー': 'id',
    'ローカルズ': 'locals',
    'オープン': 'open',
    'バーズ': 'vars',

    # --- REPL/Environment Specific ---
    'ブレークポイント': 'breakpoint',
    'コピーライト': 'copyright',
    'クレジッツ': 'credits',
    'エグジット': 'exit',
    'ライセンス': 'license',
    'クイット': 'quit',
}

BUILTINS_PYTHON_TO_JAPY_MAP = {value: key for key, value in JAPY_BUILTINS_MAP.items()}


# Check if all keywords are in JAPY_KEYWORD_MAP
def check_keywords():
    for word in KEYWORDS:
        if word not in PYTHON_TO_JAPY_MAP:
            raise ValueError(f"Keyword '{word}' not found in JAPY_KEYWORD_MAP")
    print("All keywords are in JAPY_KEYWORD_MAP")


# Check if all built-in functions are in JAPY_BUILTINS_MAP
def check_builtins():
    for word in BUILTIN_FUNCTIONS:
        if word not in BUILTINS_PYTHON_TO_JAPY_MAP:
            raise ValueError(f"Built-in function '{word}' not found in JAPY_BUILTINS_MAP")
    print("All built-in functions are in JAPY_BUILTINS_MAP")


JAPY_TRANSLATION_MAP = {**JAPY_KEYWORD_MAP, **JAPY_BUILTINS_MAP}


def transpile_japy(source_code: str) -> str:
    """
    Translates a JaPy source code string into an equivalent Python source string.

    This function operates by replacing JaPy keywords and function names with their
    Python equivalents. The core logic relies on two key principles:

    1.  **Length-based Sorting**: To prevent incorrect partial substitutions (e.g.,
        "インポート" becoming "inポート"), all JaPy terms are sorted from longest
        to shortest before replacement.
    2.  **Whole-Word Matching**: Regular expressions with word boundaries (\\b) are
        used to ensure only complete words are replaced.

    This specific version uses `typing.cast` to explicitly resolve a type
    hinting warning that may arise when processing the output of
    `sorted(dict.keys())`, ensuring compatibility with static analysis tools.

    Args:
        source_code (str): The input string containing the JaPy source code.

    Returns:
        str: The transpiled Python source code string.
    """

    # 1. Extract the keys from the translation map. Note that `dict.keys()`
    #    returns a `dict_keys` view object, not a list.
    all_japy_words = JAPY_TRANSLATION_MAP.keys()

    # 2. Sort the JaPy terms by length in descending order. This is the most
    #    critical step of the algorithm. It ensures that longer words are
    #    processed before their shorter substrings, preventing errors like
    #    "インポート" (import) being incorrectly replaced by "inポート".
    sorted_japy_words = sorted(all_japy_words, key=len, reverse=True)

    # 3. Iterate through the sorted terms and replace them in the source code.
    for word_from_list in sorted_japy_words:
        # Explicitly cast the item to a string to satisfy the type checker.
        # Some static analysis tools may not be able to infer that an item
        # from `sorted(dict.keys())` is a string, which `re.escape` requires.
        # This cast assures the type checker of the variable's type.
        japy_word = cast(str, word_from_list)

        # Look up the corresponding Python term.
        python_word = JAPY_TRANSLATION_MAP[japy_word]

        # Build a regex pattern for whole-word replacement. `\b` is a word
        # boundary, and `re.escape` handles any potential special regex characters.
        pattern = r'\b' + re.escape(japy_word) + r'\b'
        source_code = re.sub(pattern, python_word, source_code)

    return source_code


SOURCE_CODE = """
デフ メイン():
    プリント('ハロー、ジャパイ！')
メイン()
"""


PYTHON_CODE = transpile_japy(SOURCE_CODE)

if __name__ == '__main__':
    check_keywords()
    check_builtins()
    print(PYTHON_CODE)
    exec(PYTHON_CODE)