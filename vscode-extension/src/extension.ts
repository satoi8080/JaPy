import * as vscode from 'vscode';
import { JapyCompletionProvider } from './completionProvider';

export function activate(context: vscode.ExtensionContext) {
    console.log('JaPy Language Support extension is now active!');

    // Register completion provider for JaPy language
    const completionProvider = vscode.languages.registerCompletionItemProvider(
        'japy',
        new JapyCompletionProvider(),
        // Trigger characters for completion
        '.',  // For method/attribute completion
        ' ',  // For keyword completion after space
        '\n', // For new line completion
        '\t'  // For tab completion
    );

    context.subscriptions.push(completionProvider);
}

export function deactivate() {
    console.log('JaPy Language Support extension is now deactivated!');
}
