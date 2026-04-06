# VS Code用JaPy言語サポート

[![VS Code Marketplace](https://img.shields.io/badge/VS%20Code-Marketplace-blue?logo=visual-studio-code)](https://marketplace.visualstudio.com/items?itemName=Zhe.japy-language-support)

[JaPy](https://github.com/satoi8080/JaPy)用VS Code拡張機能 - 日本語キーワードを使用するPython方言（`.japy`ファイル対応）

## 機能

- **シンタックスハイライト**: JaPyキーワード・組み込み関数・型の完全なハイライト
- **コード補完**: キーワード・関数・型のIntelliSenseサポート（関数は自動で括弧 `()` を挿入）
- **言語設定**: 自動インデント、括弧マッチング、コメントトグル
- **カスタムテーマ**: 日本語キーワードに最適化されたJaPy Darkテーマ
- **Unicode対応**: 識別子での日本語文字の適切な処理

## インストール

### VS Code Marketplace から（推奨）
[VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=Zhe.japy-language-support) から直接インストール：

1. VS Codeを開く
2. 拡張機能ビュー（`Ctrl+Shift+X` / `Cmd+Shift+X`）を開く
3. "JaPy Language Support" を検索して "インストール" をクリック

### VSIXから
1. `.vsix` ファイルをダウンロード
2. `Ctrl+Shift+P`（`Cmd+Shift+P`）→ "Extensions: Install from VSIX" → ファイルを選択

## 使用例

```japy
# JaPy サンプルコード
デフ 挨拶(名前):
    プリント(f"こんにちは、{名前}さん！")
    リターン トゥルー

クラス 人:
    デフ __init__(self, 名前, 年齢):
        self.名前 = 名前
        self.年齢 = 年齢

    デフ 自己紹介(self):
        プリント(f"私の名前は{self.名前}で、{self.年齢}歳です。")

イフ __name__ == "__main__":
    人物 = 人("田中", 25)
    人物.自己紹介()
    挨拶(人物.名前)
```

## ライセンス

MIT License
