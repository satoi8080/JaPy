# JaPy VS Code Extension Installation Guide

## 前提条件

1. **Node.js** (v22以上)
2. **npm** (Node.jsに含まれています)
3. **Visual Studio Code**
4. **vsce** (Visual Studio Code Extension Manager)
5. **TypeScript** (開発時のみ必要)

## インストール手順

### 1. 依存関係のインストール

```bash
# vsce をグローバルにインストール
npm install -g vsce

# プロジェクトの依存関係をインストール（package.jsonがある場合）
npm install
```

### 2. 拡張機能のビルド

#### 自動ビルド（推奨）
```bash
# ビルドスクリプトを実行可能にする
chmod +x build.sh

# ビルド実行
./build.sh
```

#### 手動ビルド
```bash
# 拡張機能の検証
vsce ls

# パッケージ作成
vsce package
```

### 3. VS Codeへのインストール

#### 方法1: コマンドライン
```bash
# 生成された.vsixファイルをインストール
code --install-extension japy-language-support-*.vsix
```

#### 方法2: VS Code UI
1. VS Codeを開く
2. `Ctrl+Shift+P` (Mac: `Cmd+Shift+P`) でコマンドパレットを開く
3. "Extensions: Install from VSIX..." を選択
4. 生成された `.vsix` ファイルを選択

### 4. 動作確認

1. 新しいファイルを作成し、`.japy` 拡張子で保存
2. JaPyコードを書いて構文ハイライトとコード補完を確認

```japy
デフ テスト():
    プリント("こんにちは、JaPy！")
    リターン トゥルー

テスト()
```

#### コード補完のテスト
1. `.japy` ファイルで以下を入力してみてください：
   - `デフ` と入力 → 関数定義の補完が表示される
   - `プリント` と入力 → print関数の補完が表示される
   - `イフ` と入力 → if文の補完が表示される
   - `Ctrl+Space` (Mac: `Cmd+Space`) で手動補完を起動

2. 補完機能には以下が含まれます：
   - **キーワード**: イフ、エリフ、デフ、クラス など
   - **組み込み関数**: プリント、レン、マックス など
   - **組み込み型**: ストリング、リスト、ディクト など

## トラブルシューティング

### 問題: vsce が見つからない
```bash
npm install -g vsce
```

### 問題: 権限エラー
```bash
# macOS/Linux
sudo npm install -g vsce

# または npm の設定を変更
npm config set prefix ~/.npm-global
export PATH=~/.npm-global/bin:$PATH
```

### 問題: 構文ハイライトが動作しない
1. VS Codeを再起動
2. ファイルの言語モードが "JaPy" になっているか確認
3. 右下の言語表示をクリックして "JaPy" を選択

### 問題: コード補完が動作しない
1. VS Codeを再起動
2. 拡張機能が正しくインストールされているか確認
3. Developer Consoleでエラーを確認 (`Help` > `Toggle Developer Tools`)
4. TypeScriptコンパイルエラーがないか確認: `npm run compile`

### 問題: 日本語文字が正しく表示されない
1. VS Codeの設定で適切なフォントを選択
   - 推奨: "Consolas", "Yu Gothic UI", "Meiryo"
2. エンコーディングがUTF-8になっているか確認

## 開発者向け

### 拡張機能の更新
1. ソースコードを修正
2. `package.json` のバージョンを更新
3. 再ビルド: `./build.sh`
4. 再インストール

### マーケットプレイスへの公開
```bash
# 初回公開
vsce publish

# バージョンアップ公開
vsce publish patch  # 0.0.1 -> 0.0.2
vsce publish minor  # 0.1.0 -> 0.2.0
vsce publish major  # 1.0.0 -> 2.0.0
```

### デバッグ
1. VS Codeで拡張機能フォルダを開く
2. `F5` を押して新しいExtension Development Hostを起動
3. 新しいウィンドウで `.japy` ファイルをテスト

## ファイル構造

```
vscode-extension/
├── package.json                    # 拡張機能の設定
├── tsconfig.json                   # TypeScript設定
├── language-configuration.json     # 言語設定
├── src/                            # TypeScriptソースコード
│   ├── extension.ts                # メイン拡張機能ロジック
│   └── completionProvider.ts       # コード補完プロバイダー
├── out/                            # コンパイル済みJavaScript
├── syntaxes/
│   └── japy.tmLanguage.json        # 構文定義
├── themes/
│   └── japy-dark-color-theme.json  # カラーテーマ
├── build.sh                        # ビルドスクリプト
├── README.md                       # 説明書
└── INSTALL.md                      # このファイル
```

## サポート

問題や質問がある場合は、GitHubのIssuesページで報告してください。
