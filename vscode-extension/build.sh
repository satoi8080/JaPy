#!/bin/bash

# JaPy VS Code Extension Build Script

echo "🚀 Building JaPy VS Code Extension..."

# Check if vsce is installed
if ! command -v vsce &> /dev/null; then
    echo "❌ vsce (Visual Studio Code Extension Manager) is not installed."
    echo "📦 Installing vsce..."
    npm install -g vsce
fi

# Install dependencies if package.json exists and node_modules doesn't
if [ -f "package.json" ] && [ ! -d "node_modules" ]; then
    echo "📦 Installing dependencies..."
    npm install
fi

# Validate the extension
echo "🔍 Validating extension..."
vsce ls

# Package the extension
echo "📦 Packaging extension..."
vsce package

# Check if packaging was successful
if [ $? -eq 0 ]; then
    echo "✅ Extension packaged successfully!"
    echo "📁 Generated files:"
    ls -la *.vsix 2>/dev/null || echo "No .vsix files found"

    echo ""
    echo "🎉 Next steps:"
    echo "1. Install the extension: code --install-extension japy-language-support-*.vsix"
    echo "2. Or publish to marketplace: vsce publish"
    echo "3. Create a .japy file to test syntax highlighting"
else
    echo "❌ Extension packaging failed!"
    exit 1
fi
