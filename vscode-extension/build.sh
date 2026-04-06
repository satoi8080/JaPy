#!/bin/bash

# JaPy VS Code Extension Build Script
# 使用方法: ./build.sh [patch|minor|major|build]
#
# patch: パッチバージョンアップ (0.1.1 → 0.1.2) + git commit/tag/push
# minor: マイナーバージョンアップ (0.1.1 → 0.2.0) + git commit/tag/push
# major: メジャーバージョンアップ (0.1.1 → 1.0.0) + git commit/tag/push
# build: 現在のバージョンでビルドのみ実行 (git操作なし)

set -e  # エラーが発生したら即座に終了

# 色の定義
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 色付きメッセージを出力する関数群
print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# パラメータをチェック
if [ $# -eq 0 ]; then
    print_error "バージョンタイプまたはアクションを指定してください"
    echo "使用方法: $0 [patch|minor|major|build]"
    echo "  patch/minor/major: 新しいバージョンをリリース"
    echo "  build: 現在のバージョンでビルドのみ実行"
    exit 1
fi

VERSION_TYPE=$1

# バージョンタイプを検証
if [[ ! "$VERSION_TYPE" =~ ^(patch|minor|major|build)$ ]]; then
    print_error "無効なバージョンタイプ: $VERSION_TYPE"
    echo "サポートされているタイプ: patch, minor, major, build"
    exit 1
fi

# gitリポジトリかどうかをチェック
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    print_error "現在のディレクトリはgitリポジトリではありません"
    exit 1
fi

# 現在のバージョンを取得
CURRENT_VERSION=$(grep '"version"' package.json | sed 's/.*"version": "\(.*\)",/\1/')

# ビルドのみの場合の特別処理
if [ "$VERSION_TYPE" = "build" ]; then
    print_info "現在のバージョン $CURRENT_VERSION でビルドを実行します..."
    NEW_VERSION=$CURRENT_VERSION
else
    print_info "$VERSION_TYPE バージョンリリースフローを開始します..."

    # 作業ディレクトリがクリーンかどうかをチェック
    if ! git diff-index --quiet HEAD --; then
        print_error "作業ディレクトリにコミットされていない変更があります。先にコミットまたはステージしてください"
        git status --short
        exit 1
    fi

    # main/masterブランチにいるかチェック
    CURRENT_BRANCH=$(git branch --show-current)
    if [[ "$CURRENT_BRANCH" != "main" && "$CURRENT_BRANCH" != "master" ]]; then
        print_warning "現在main/masterブランチにいません (現在: $CURRENT_BRANCH)"
        read -p "続行しますか? (y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            print_info "リリースがキャンセルされました"
            exit 0
        fi
    fi

    # 最新のコードを取得
    print_info "最新のコードを取得中..."
    git pull origin $CURRENT_BRANCH

    print_info "現在のバージョン: $CURRENT_VERSION"

    # セマンティックバージョニングに基づく新しいバージョン番号を計算
    IFS='.' read -ra VERSION_PARTS <<< "$CURRENT_VERSION"
    MAJOR=${VERSION_PARTS[0]}
    MINOR=${VERSION_PARTS[1]}
    PATCH=${VERSION_PARTS[2]}

    # バージョンタイプに応じてバージョン番号を更新
    case $VERSION_TYPE in
        "patch")
            PATCH=$((PATCH + 1))  # バグ修正: z を +1
            ;;
        "minor")
            MINOR=$((MINOR + 1))  # 新機能: y を +1, z を 0 にリセット
            PATCH=0
            ;;
        "major")
            MAJOR=$((MAJOR + 1))  # 重大な変更: x を +1, y と z を 0 にリセット
            MINOR=0
            PATCH=0
            ;;
    esac

    NEW_VERSION="$MAJOR.$MINOR.$PATCH"
    print_info "新しいバージョン: $NEW_VERSION"

    # リリースを確認
    print_warning "バージョン $CURRENT_VERSION → $NEW_VERSION をリリースします"
    read -p "続行を確認しますか? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        print_info "リリースがキャンセルされました"
        exit 0
    fi

        # バージョン番号を更新
    print_info "バージョン番号を更新中..."
    sed -i.bak "s/\"version\": \"$CURRENT_VERSION\"/\"version\": \"$NEW_VERSION\"/" package.json
    sed -i.bak "s/\"version\": \"$CURRENT_VERSION\"/\"version\": \"$NEW_VERSION\"/" package-lock.json

    # バックアップファイルを削除
    rm -f package.json.bak package-lock.json.bak

    # 変更をコミット
    print_info "バージョン変更をコミット中..."
    git add package.json package-lock.json
    git commit -m "Bump VS Code extension version: $CURRENT_VERSION → $NEW_VERSION"

    # バージョンcommit上でGitタグを作成
    print_info "Gitタグを作成中..."
    git tag -a "vscode-v$NEW_VERSION" -m "Release VS Code extension version $NEW_VERSION"

    # まず分支をpush、その後tagをpush
    print_info "リモートリポジトリにプッシュ中..."
    git push origin $CURRENT_BRANCH
    git push origin "vscode-v$NEW_VERSION"

    print_success "バージョン $NEW_VERSION の準備が完了しました！"
fi

# Check if vsce is installed
if ! command -v vsce &> /dev/null; then
    print_info "📦 Installing vsce..."
    npm install -g vsce
fi

# Install dependencies if package.json exists and node_modules doesn't
if [ -f "package.json" ] && [ ! -d "node_modules" ]; then
    print_info "📦 Installing dependencies..."
    npm install
fi

# Validate the extension
print_info "🔍 Validating extension..."
vsce ls

# Package the extension
print_info "📦 Packaging extension..."
vsce package

# Check if packaging was successful
if [ $? -eq 0 ]; then
    print_success "Extension packaged successfully!"
    print_info "📁 Generated files:"
    ls -la *.vsix 2>/dev/null || echo "No .vsix files found"



    echo ""
    print_info "🎉 Next steps:"
    echo "1. Install the extension: code --install-extension japy-language-support-*.vsix"
    echo "2. Or publish to marketplace: vsce publish"
    echo "3. Create a .japy file to test syntax highlighting"

    if [ "$VERSION_TYPE" != "build" ]; then
        print_success "🎉 VS Code Extension リリースフローが完了しました！"
        print_info "新しいバージョン: $NEW_VERSION"
        print_info "Gitタグ: vscode-v$NEW_VERSION"
    fi
else
    print_error "Extension packaging failed!"
    exit 1
fi

exit 0
