import * as vscode from 'vscode';

export class JapyCompletionProvider implements vscode.CompletionItemProvider {

    // JaPy to Python keyword mappings
    private readonly keywordMappings = {
        // Logical and Constants
        'トゥルー': 'True',
        'フォルス': 'False',
        'ノン': 'None',

        // Control Flow
        'イフ': 'if',
        'エリフ': 'elif',
        'エルス': 'else',
        'フォー': 'for',
        'ホワイル': 'while',
        'ブレーク': 'break',
        'コンティニュー': 'continue',

        // Functions and Classes
        'デフ': 'def',
        'クラス': 'class',
        'リターン': 'return',
        'イールド': 'yield',
        'ラムダ': 'lambda',

        // Operators
        'アンド': 'and',
        'オア': 'or',
        'ノット': 'not',
        'イン': 'in',
        'イズ': 'is',

        // Error Handling
        'トライ': 'try',
        'エクセプト': 'except',
        'ファイナリー': 'finally',
        'レイズ': 'raise',

        // Modules and Scope
        'インポート': 'import',
        'フロム': 'from',
        'アズ': 'as',
        'グローバル': 'global',
        'ノンローカル': 'nonlocal',

        // Async
        'エイシンク': 'async',
        'アウェイト': 'await',

        // Miscellaneous
        'パス': 'pass',
        'デル': 'del',
        'ウィズ': 'with',
        'アサート': 'assert'
    };

    // JaPy to Python built-in function mappings
    private readonly builtinFunctionMappings = {
        // I/O and Interaction
        'プリント': 'print',
        'インプット': 'input',
        'ヘルプ': 'help',

        // Data Structure & Collection
        'レン': 'len',
        'サム': 'sum',
        'マックス': 'max',
        'ミン': 'min',
        'ソーテッド': 'sorted',
        'リバースド': 'reversed',
        'ディル': 'dir',

        // Functional / Iteration Tools
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

        // Math & Numbers
        'エービーエス': 'abs',
        'パウ': 'pow',
        'ラウンド': 'round',
        'ディブモッド': 'divmod',

        // Object & Attribute
        'イズインスタンス': 'isinstance',
        'イズサブクラス': 'issubclass',
        'ハズアトリブ': 'hasattr',
        'ゲットアトリブ': 'getattr',
        'セットアトリブ': 'setattr',
        'デルアトリブ': 'delattr',

        // String & Representation
        'アスキー': 'ascii',
        'ビン': 'bin',
        'レップ': 'repr',
        'フォーマット': 'format',
        'ヘックス': 'hex',
        'オクト': 'oct',
        'キャラ': 'chr',
        'オーアールディー': 'ord',

        // Advanced Functions
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

        // REPL/Environment Specific
        'ブレークポイント': 'breakpoint',
        'コピーライト': 'copyright',
        'クレジッツ': 'credits',
        'エグジット': 'exit',
        'ライセンス': 'license',
        'クイット': 'quit'
    };

    // JaPy Built-in Types mappings
    private readonly builtinTypeMappings = {
        // Basic Types
        'ブール': 'bool',
        'イント': 'int',
        'フロート': 'float',
        'ストリング': 'str',

        // Collections
        'リスト': 'list',
        'タプル': 'tuple',
        'ディクト': 'dict',
        'セット': 'set',
        'フローズンセット': 'frozenset',

        // Advanced Types
        'バイツ': 'bytes',
        'バイトアレイ': 'bytearray',
        'コンプレックス': 'complex',
        'エニュメレート': 'enumerate',
        'メモリビュー': 'memoryview',
        'オブジェクト': 'object',
        'タイプ': 'type',
        'スーパー': 'super',
        'プロパティ': 'property',
        'クラスメソッド': 'classmethod',
        'スタティックメソッド': 'staticmethod'
    };

    provideCompletionItems(
        _document: vscode.TextDocument,
        _position: vscode.Position,
        _token: vscode.CancellationToken,
        _context: vscode.CompletionContext
    ): vscode.ProviderResult<vscode.CompletionItem[] | vscode.CompletionList> {

        const completionItems: vscode.CompletionItem[] = [];

        // Add keyword completions
        Object.entries(this.keywordMappings).forEach(([japyKeyword, pythonKeyword]) => {
            const item = new vscode.CompletionItem(japyKeyword, vscode.CompletionItemKind.Keyword);
            item.detail = `Python: ${pythonKeyword}`;
            item.documentation = new vscode.MarkdownString(
                `**JaPy キーワード:** \`${japyKeyword}\`\n\n**対応するPython:** \`${pythonKeyword}\`\n\n---\n\n*JaPyでは日本語キーワードを使用してPythonと同じ機能を実現できます*`
            );
            completionItems.push(item);
        });

        // Add built-in function completions
        Object.entries(this.builtinFunctionMappings).forEach(([japyFunc, pythonFunc]) => {
            const item = new vscode.CompletionItem(japyFunc, vscode.CompletionItemKind.Function);
            item.detail = `Python: ${pythonFunc}()`;
            item.documentation = new vscode.MarkdownString(
                `**JaPy 組み込み関数:** \`${japyFunc}()\`\n\n**対応するPython:** \`${pythonFunc}()\`\n\n---\n\n*JaPyでは日本語関数名を使用してPythonの組み込み関数を呼び出せます*`
            );
            // Add parentheses for functions
            item.insertText = `${japyFunc}()`;
            item.command = {
                command: 'cursorLeft',
                title: 'Move cursor left'
            };
            completionItems.push(item);
        });

        // Add built-in type completions
        Object.entries(this.builtinTypeMappings).forEach(([japyType, pythonType]) => {
            const item = new vscode.CompletionItem(japyType, vscode.CompletionItemKind.Class);
            item.detail = `Python: ${pythonType}`;
            item.documentation = new vscode.MarkdownString(
                `**JaPy 組み込み型:** \`${japyType}\`\n\n**対応するPython:** \`${pythonType}\`\n\n---\n\n*JaPyでは日本語型名を使用してPythonのデータ型を扱えます*`
            );
            completionItems.push(item);
        });

        return completionItems;
    }
}
