# JaPy - 日本語カタカナPython方言

<div align="center">
<img src="https://raw.githubusercontent.com/satoi8080/JaPy/main/icon.svg" alt="JaPyロゴ - 青と赤を使用した「Ja」の文字デザイン。青い「J」の中にはPythonの蛇の目を表現した二つの白い円が配置され、愛と平和の融合を象徴している" width="64" height="64">

<sub><i>JaPyロゴ - 青と赤を使用した「Ja」の文字デザイン。<br>
青い「J」の中にはPythonの蛇の目を表現した二つの白い円が配置され、愛と平和の融合を象徴している</i></sub>
</div>


<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/japy-lang)
[![PyPI](https://img.shields.io/badge/PyPI-japy--lang-blue?logo=pypi)](https://pypi.org/project/japy-lang/)
![PyPI - Version](https://img.shields.io/pypi/v/japy-lang)
[![VS Code Extension](https://img.shields.io/badge/VS%20Code-Extension-blue?logo=visual-studio-code)](https://marketplace.visualstudio.com/items?itemName=Zhe.japy-language-support)

</div>


<div align="center">
<img src="https://raw.githubusercontent.com/satoi8080/JaPy/main/japy/japy.png" alt="JaPy - カタカナでプログラミング" width="400">
</div>

JaPyは日本語カタカナキーワードを使用するPythonの方言です。なぜか全部カタカナでプログラミングしたくなった時のためのツールです。Pythonの構文はそのままに、なんとなく日本語っぽくコーディングできます。

## 🌟 フィーチャー

- **フルカタカナキーワード**: `デフ`、`イフ`、`フォー`など、なんか日本語っぽいキーワード群
- **トランスパイラー**: JaPyコードを普通のPythonコードにコンバート
- **コマンドラインツール**: ファイル変換、実行、検証機能
- **VS Codeエクステンション**: シンタックスハイライトとオートコンプリートをサポート
- **ユニコード対応**: 日本語アイデンティファイアーの完全サポート

## 📦 インストレーション

### PyPIから（推奨）

```bash
# pipでインストール
pip install japy-lang

# または uvでインストール
uv add japy-lang
```

### ローカル開発版

```bash
# リポジトリをクローン
git clone https://github.com/satoi8080/JaPy.git
cd JaPy

# デペンデンシーをインストール
uv sync
```

### VS Codeエクステンション

#### VS Code Marketplaceから（推奨）

[VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=Zhe.japy-language-support)から直接インストールできます。

#### 手動ビルド・インストール

まずエクステンションをビルドしてからインストール：

```bash
cd vscode-extension

# デペンデンシーをインストール
npm install

# エクステンションをビルド
./build.sh
```

ビルド後、ジェネレートされた`.vsix`ファイルをインストール：

1. VS Codeで`Ctrl+Shift+P`（Mac: `Cmd+Shift+P`）
2. "Extensions: Install from VSIX..."をセレクト
3. `vscode-extension`フォルダ内の`japy-language-support-*.vsix`ファイルをセレクト

## 🚀 ユーセージ

### ベーシックなサンプル

```japy
# hello.japy
デフ 挨拶(名前):
    プリント(f"こんにちは、{名前}さん！")
    リターン トゥルー

クラス 人:
    デフ __init__(self, 名前, 年齢):
        self.名前 = 名前
        self.年齢 = 年齢

    デフ 自己紹介(self):
        プリント(f"私の名前は{self.名前}で、{self.年齢}歳です。")

# メイン実行
イフ __name__ == "__main__":
    人物 = 人("田中", 25)
    人物.自己紹介()
    挨拶(人物.名前)
```

### コマンドラインユーセージ

```bash
# JaPyファイルをトランスパイルしてエグゼキュート
uv run python -m japy --input=hello.japy --execute

# Pythonコードをアウトプットファイルにセーブ
uv run python -m japy --input=hello.japy --output=hello.py

# トランスパイルリザルトをディスプレイ（デフォルト）
uv run python -m japy --input=hello.japy --show

# トランスパイルリザルトを表示しない
uv run python -m japy --input=hello.japy --show=false

# ストリクトモードでトランスパイル（tokenizer使用）
uv run python -m japy --input=hello.japy --strict

# ストリクトモードでトランスパイルして実行
uv run python -m japy --input=hello.japy --strict --execute

# キーワードマッピングをバリデート
uv run python -m japy --validate

# デバッグモードで実行
uv run python -m japy --input=hello.japy --execute --debug
```

### コマンドラインオプション

利用可能なフラグ：

- `--input`: トランスパイルする.japyファイル（必須、--validateモード以外）
- `--output`: 出力Pythonファイル（指定しない場合は標準出力）
- `--execute`: トランスパイルされたPythonコードを実行
- `--show`: トランスパイルされたPythonコードを表示（デフォルト: true）
- `--strict`: ストリクトモード：tokenizerを使用してより正確なコード変換を行う
- `--validate`: キーワードと組み込み関数のマッピングを検証
- `--debug`: デバッグ出力を有効化

### 実用的なサンプル

```bash
# 1. JaPyファイルを作成して実行
echo 'プリント("ハロー、ワールド！")' > hello.japy
uv run python -m japy --input=hello.japy --execute

# 2. JaPyファイルをPythonファイルに変換
uv run python -m japy --input=hello.japy --output=hello.py

# 3. 変換結果を確認してから実行
uv run python -m japy --input=hello.japy --show --execute

# 4. システムの検証（開発者向け）
uv run python -m japy --validate
```

### プログラムからユーズ

```python
from japy import transpile_japy

japy_code = """
デフ テスト():
    プリント("こんにちは、JaPy！")
    リターン トゥルー
"""

python_code = transpile_japy(japy_code)
print(python_code)
exec(python_code)
```

### ストリクトモード（Strict Mode）

JaPyは2つの変換モードを提供しています：

#### 簡易モード（デフォルト）
- 文字列置換と正規表現（regex）を使用
- 高速でシンプルな変換
- 文字列やコメント内の日本語キーワードも置換される可能性があります

#### ストリクトモード（`--strict`）
- Pythonのtokenizerを使用
- より正確で安全な変換
- 文字列やコメント内の日本語キーワードを保護
- コードの構造を理解して適切に変換

**使用例：**

```japy
# test.japy
デフ テスト関数():
    メッセージ = "これはプリントという文字列です"  # このプリントは置換されません
    プリント(メッセージ)  # このプリントはprintに置換されます
```

**変換結果の違い：**

```bash
# 簡易モード（デフォルト）
uv run python -m japy --input=test.japy --show
# 結果: 文字列内の"プリント"も"print"に置換される

# 厳格モード
uv run python -m japy --input=test.japy --show --strict
# 結果: 文字列内の"プリント"は保護され、コード内の"プリント"のみ置換される
```

## 📚 ランゲージリファレンス

サポートされているキーワード、ビルトイン関数、ビルトイン型のコンプリートなリストは、[japy/ジャパイ.py](japy/ジャパイ.py)のソースコードをリファーしてください。

メジャーなキーワードサンプル：
- `デフ` → `def` (ファンクションデフィニション)
- `イフ` → `if` (コンディショナルブランチ)
- `フォー` → `for` (ループ)
- `プリント` → `print` (アウトプット)
- `レン` → `len` (レングス)

## 🛠️ デベロップメント

### テストエグゼキューション

```bash
# サンプルJaPyファイルをラン
uv run python -m japy --input=japy/ジャパイ.japy --execute

# ストリクトモードでテスト
uv run python -m japy --input=test_strict_mode.japy --show --strict

# キーワードマッピングをバリデート
uv run python -m japy --validate

# VS Code拡張機能のテストサンプルを実行
uv run python -m japy --input=vscode-extension/test-example.japy --execute

# デバッグモードでテスト
uv run python -m japy --input=japy/ジャパイ.japy --execute --debug
```

### VS Codeエクステンションのデベロップメント

ディテールは[vscode-extension/INSTALL.md](vscode-extension/INSTALL.md)をリファーしてください。

```bash
cd vscode-extension

# デペンデンシーをインストール
npm install

# エクステンションをビルド
./build.sh
```

## 📄 ライセンス

MIT License - ディテールは[LICENSE](LICENSE)ファイルをリファーしてください。

## 🔗 リンクス

- [GitHub リポジトリ](https://github.com/satoi8080/JaPy)
- [PyPI パッケージ](https://pypi.org/project/japy-lang/)
- [VS Codeエクステンションドキュメント](vscode-extension/README.md)
- [VS Codeエクステンションインストールガイド](vscode-extension/INSTALL.md)

---

**JaPy** - 日本語カタカナでプログラミングをエンジョイしよう！

~~なんでこんなものを作ったんだろう...~~
