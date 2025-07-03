# Contribution Guide

Thank you for your interest in contributing to the CodeLlama project! This document explains how to contribute effectively.

## 🚀 How to Contribute

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/YOUR-USERNAME/codellama-project.git
cd codellama-project
```

### 2. Environment Setup

```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# For the VS Code extension
cd vscode-extension
npm install
```

### 3. Create a Branch

```bash
git checkout -b feature/your-feature-name
```

## 📝 Types of Contributions

### Code
- Fine-tuning script improvements
- New features for the VS Code extension
- Performance optimizations
- Bug fixes

### Documentation
- README improvements
- Adding tutorials
- API documentation
- Usage examples

### Datasets
- New quality datasets
- Preprocessing improvements
- Data validation

## 🔍 Code Standards

### Python
- Follow PEP 8
- Use docstrings for functions
- Unit tests with pytest
- Type hints recommended

```python
def process_dataset(data: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Processes the dataset for fine-tuning.
    
    Args:
        data: List of raw examples
        
    Returns:
        List of processed examples
    """
    pass
```

### TypeScript (VS Code Extension)
- Use strict TypeScript
- JSDoc comments
- Tests with Mocha/Jest

```typescript
/**
 * Generates code with the CodeLlama model
 * @param prompt The input prompt
 * @returns The generated code
 */
async function generateCode(prompt: string): Promise<string> {
    // Implementation
}
```

## 🧪 Tests

### Python Tests
```bash
# Run all tests
pytest

# Tests with coverage
pytest --cov=finetuning
```

### Extension Tests
```bash
cd vscode-extension
npm test
```

## 📋 Review Process

1. **Create a Pull Request**
   - Clear description of changes
   - Reference related issues
   - Include screenshots if relevant

2. **Pre-submission Checklist**
   - [ ] Tests pass
   - [ ] Code formatted correctly
   - [ ] Documentation updated
   - [ ] No merge conflicts

3. **Review Process**
   - At least one review required
   - CI/CD must pass
   - Constructive discussions encouraged

## 🐛 Reporting Bugs

Use GitHub issue templates with:
- Problem description
- Steps to reproduce
- Environment (OS, versions)
- Error logs if applicable

## 💡 Proposing Features

1. Check if it doesn't already exist
2. Create an issue with the "Feature Request" template
3. Discuss the approach before implementation
4. Implement after agreement

## 📞 Communication

- **GitHub Issues**: For bugs and features
- **Discussions**: For general questions
- **Email**: For private questions

## 🏆 Recognition

All contributors will be mentioned in:
- The AUTHORS.md file
- Release notes
- The main README

## 📜 Code of Conduct

- Respectful and inclusive
- Constructive in criticism
- Open to different perspectives
- Focus on improving the project

Thank you for helping to make this project better! 🚀


