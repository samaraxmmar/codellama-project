# CodeLlama Project - Fine-tuning and VS Code Extension

This repository contains a complete project for fine-tuning the CodeLlama model and developing a VS Code extension using this fine-tuned model.

## 🎯 Project Objectives

This project aims to create an intelligent development assistant based on CodeLlama, capable of:
- Generating code from natural language descriptions
- Providing contextual code completion suggestions
- Assisting developers in their daily workflow via a VS Code extension

## 📁 Project Structure

```
codellama-project/
├── .github/workflows/     # CI/CD Workflows
├── data/                  # Datasets for fine-tuning
│   ├── raw/              # Raw data
│   └── processed/        # Prepared data
├── finetuning/           # Fine-tuning scripts and models
│   ├── scripts/          # Training and evaluation scripts
│   └── models/           # Fine-tuned models
├── vscode-extension/     # VS Code Extension
│   ├── src/              # Extension source code
│   └── package.json      # Extension configuration
├── notebooks/            # Jupyter exploration notebooks
├── docs/                 # Additional documentation
└── README.md            # This file
```

## 🚀 Installation and Configuration

### Prerequisites

- Python 3.8+
- Node.js 16+
- VS Code
- GPU recommended for fine-tuning

### Python Dependencies Installation

```bash
pip install -r requirements.txt
```

### VS Code Extension Configuration

```bash
cd vscode-extension
npm install
npm run compile
```

## 📊 Dataset

The dataset used for fine-tuning is in JSONL format and contains prompt-completion pairs for different programming languages. Each entry follows the format:

```json
{"prompt": "def factorial(n):", "completion": "\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n-1)"}
```

## 🔧 Model Fine-tuning

To start fine-tuning:

```bash
cd finetuning/scripts
python train.py
```

To evaluate the model:

```bash
python evaluate.py
```

## 🔌 VS Code Extension

The extension provides the following features:

- **Code Generation**: `Ctrl+Shift+G`
- **Intelligent Completion**: Automatic suggestions
- **Multi-language Support**: JavaScript, Python, TypeScript, Java, C++

### Extension Installation

1. Open VS Code
2. Press `F5` to launch the extension in development mode
3. Or package the extension with `vsce package`

## 🤝 Contribution

Contributions are welcome! See the `CONTRIBUTING.md` file for more information.

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## 👨‍💻 Author

**Samar Ammar** - Machine Learning Engineer
- GitHub: [@samaraxmmar](https://github.com/samaraxmmar)
- LinkedIn: [samar-ammar-342163221](https://linkedin.com/in/samar-ammar-342163221)

## 🙏 Acknowledgments

- Meta AI for the CodeLlama model
- Hugging Face for fine-tuning tools
- The open-source community for resources and inspiration


