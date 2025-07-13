#!/bin/bash

# JaPy 自動リリーススクリプト
# 使用方法: ./scripts/release.sh [patch|minor|major|tag]
#
# patch: パッチバージョンアップ (0.1.1 → 0.1.2)
# minor: マイナーバージョンアップ (0.1.1 → 0.2.0)
# major: メジャーバージョンアップ (0.1.1 → 1.0.0)
# tag:   現在のバージョンにタグのみ追加

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
    echo "使用方法: $0 [patch|minor|major|tag]"
    echo "  patch/minor/major: 新しいバージョンをリリース"
    echo "  tag: 現在のバージョンにタグを追加"
    exit 1
fi

VERSION_TYPE=$1

# バージョンタイプを検証
if [[ ! "$VERSION_TYPE" =~ ^(patch|minor|major|tag)$ ]]; then
    print_error "無効なバージョンタイプ: $VERSION_TYPE"
    echo "サポートされているタイプ: patch, minor, major, tag"
    exit 1
fi

# gitリポジトリかどうかをチェック
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    print_error "現在のディレクトリはgitリポジトリではありません"
    exit 1
fi

# 現在のバージョンを取得
CURRENT_VERSION=$(grep -E '^version = ' pyproject.toml | sed 's/version = "\(.*\)"/\1/')

# タグのみの場合の特別処理
if [ "$VERSION_TYPE" = "tag" ]; then
    print_info "現在のバージョン $CURRENT_VERSION にタグを追加します..."

    # 既存のタグをチェック（重複回避）
    if git tag -l "v$CURRENT_VERSION" | grep -q "v$CURRENT_VERSION"; then
        print_warning "タグ v$CURRENT_VERSION は既に存在します"
        read -p "既存のタグを削除して再作成しますか? (y/N): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            print_info "既存のタグを削除中..."
            git tag -d "v$CURRENT_VERSION" 2>/dev/null || true
            git push origin --delete "v$CURRENT_VERSION" 2>/dev/null || true
        else
            print_info "タグ作成をキャンセルしました"
            exit 0
        fi
    fi

    # 新しいタグを作成
    print_info "Gitタグ v$CURRENT_VERSION を作成中..."
    git tag -a "v$CURRENT_VERSION" -m "Release version $CURRENT_VERSION"

    # リモートリポジトリにプッシュ
    print_info "タグをリモートリポジトリにプッシュ中..."
    git push origin "v$CURRENT_VERSION"

    print_success "🎉 タグ v$CURRENT_VERSION が作成されました！"
    exit 0
fi

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
sed -i.bak "s/version = \"$CURRENT_VERSION\"/version = \"$NEW_VERSION\"/" pyproject.toml
sed -i.bak "s/__version__ = \"$CURRENT_VERSION\"/__version__ = \"$NEW_VERSION\"/" japy/__init__.py

# バックアップファイルを削除
rm -f pyproject.toml.bak japy/__init__.py.bak

# ビルドファイルを削除
print_info "ビルドファイルを削除中..."
rm -rf dist/ build/ *.egg-info/

# パッケージをビルド
print_info "パッケージをビルド中..."
pyproject-build

# パッケージ品質をチェック
print_info "パッケージ品質をチェック中..."
twine check dist/*

# 変更をコミット
print_info "バージョン変更をコミット中..."
git add pyproject.toml japy/__init__.py
git commit -m "Bump version: $CURRENT_VERSION → $NEW_VERSION"

# Gitタグを作成
print_info "Gitタグを作成中..."
git tag -a "v$NEW_VERSION" -m "Release version $NEW_VERSION"

# リモートにプッシュ
print_info "リモートリポジトリにプッシュ中..."
git push origin $CURRENT_BRANCH
git push origin "v$NEW_VERSION"

print_success "バージョン $NEW_VERSION の準備が完了しました！"

# PyPIへの公開オプションを提供
print_warning "PyPIに公開しますか？"
echo "1) TestPyPIに公開 (テスト環境での検証用)"
echo "2) 正式PyPIに公開 (本番環境、全世界に公開)"
echo "3) 公開をスキップ (後で手動実行)"
read -p "選択してください (1/2/3): " -n 1 -r
echo

case $REPLY in
    1)
        print_info "TestPyPIに公開中..."
        twine upload --repository testpypi dist/*
        print_success "TestPyPIに公開されました: https://test.pypi.org/project/japy-lang/$NEW_VERSION/"
        ;;
    2)
        print_info "正式PyPIに公開中..."
        twine upload dist/*
        print_success "PyPIに公開されました: https://pypi.org/project/japy-lang/$NEW_VERSION/"
        ;;
    3)
        print_info "公開をスキップしました。後で手動で公開できます:"
        echo "  twine upload --repository testpypi dist/*  # TestPyPI用"
        echo "  twine upload dist/*                        # 正式PyPI用"
        ;;
    *)
        print_warning "無効な選択です。公開をスキップします"
        ;;
esac

print_success "🎉 リリースフローが完了しました！"
print_info "新しいバージョン: $NEW_VERSION"
print_info "Gitタグ: v$NEW_VERSION"

exit 0
