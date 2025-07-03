# CodeLlama Assistant - VS Code Extension

This VS Code extension leverages a fine-tuned CodeLlama model to provide intelligent code development assistance.

## Features

- **Code Generation**: Generate code from natural language descriptions
- **Code Completion**: Automatically complete your code as you type
- **Intelligent Autocompletion**: Contextual suggestions while typing

## Installation

1. Clone this repository
2. Navigate to the `vscode-extension` folder
3. Install dependencies: `npm install`
4. Compile the extension: `npm run compile`
5. Open VS Code and press `F5` to launch the extension in development mode

## Usage

### Code Generation
1. Select text describing what you want to generate
2. Use the shortcut `Ctrl+Shift+G` (or `Cmd+Shift+G` on Mac)
3. The generated code will be inserted at the cursor position

### Code Completion
1. Start typing your code
2. Use the "Complete Code with CodeLlama" command from the command palette
3. The completion will be inserted automatically

### Autocompletion
The extension automatically provides suggestions as you type, especially after typing a dot (`.`).

## Configuration

Ensure your fine-tuned CodeLlama model is deployed and accessible via a REST API at the address configured in `src/extension.ts` (default: `http://localhost:8000/generate`).

## Supported Languages

- JavaScript
- TypeScript
- Python
- Java
- C++

## Development

To contribute to this extension:

1. Fork the repository
2. Create a branch for your feature
3. Implement your changes
4. Test the extension
5. Submit a pull request

## License

MIT License


