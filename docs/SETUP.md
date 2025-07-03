# Setup Guide

This guide will walk you through setting up the CodeLlama project for development and usage.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Python 3.8 or higher**: Required for running the fine-tuning scripts
- **Node.js 16 or higher**: Required for the VS Code extension development
- **Git**: For version control
- **VS Code**: For testing the extension
- **CUDA-compatible GPU** (recommended): For efficient model fine-tuning

## Environment Setup

### 1. Clone the Repository

```bash
git clone https://github.com/samaraxmmar/codellama-project.git
cd codellama-project
```

### 2. Python Environment Setup

Create a virtual environment to isolate dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

### 3. VS Code Extension Setup

Navigate to the extension directory and install dependencies:

```bash
cd vscode-extension
npm install
```

Compile the TypeScript code:

```bash
npm run compile
```

## Dataset Preparation

The project uses the `samaxr/code-summary-java` dataset from Hugging Face. To download and prepare the dataset:

```bash
python scripts/download_and_process_dataset.py
```

This will create a JSONL file at `data/processed/code_finetuning_dataset.jsonl` ready for fine-tuning.

## Model Fine-tuning

### Training

To start fine-tuning the CodeLlama model:

```bash
cd finetuning/scripts
python train.py
```

**Note**: Fine-tuning requires significant computational resources. Consider using a GPU for faster training.

### Evaluation

After training, evaluate the model:

```bash
python evaluate.py
```

## VS Code Extension Development

### Testing the Extension

1. Open VS Code
2. Open the `vscode-extension` folder
3. Press `F5` to launch a new Extension Development Host window
4. The extension will be loaded and ready for testing

### Building the Extension

To package the extension for distribution:

```bash
npm install -g vsce
vsce package
```

This creates a `.vsix` file that can be installed in VS Code.

## Troubleshooting

### Common Issues

1. **CUDA out of memory**: Reduce batch size in training arguments
2. **Module not found**: Ensure virtual environment is activated
3. **Extension not loading**: Check TypeScript compilation errors

### Getting Help

- Check the [Issues](https://github.com/samaraxmmar/codellama-project/issues) page
- Read the [Contributing Guide](CONTRIBUTING.md)
- Contact the maintainers

