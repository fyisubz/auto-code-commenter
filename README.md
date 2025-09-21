# Auto Code Commenter 🤖💻

An AI-powered tool that automatically adds meaningful, context-aware comments to source code using advanced language models. Features an intuitive Gradio web interface, OpenAI/Grok API integration, and intelligent code analysis for efficient documentation generation and learning assistance.

## ✨ Features

### 💼 Core Functionality
- **Code Analysis**: Intelligent parsing and understanding of code structure and logic
- **Comment Generation**: AI-powered creation of meaningful, context-aware comments
- **Multi-Language Support**: Compatible with Python, JavaScript, Java, C++, and more
- **Educational Tool**: Helps beginners understand complex code patterns and logic

### 📊 AI Processing & Analysis
- **Context Understanding**: Advanced LLM analysis of code purpose and functionality
- **Documentation Style**: Professional-grade comment formatting and structure  
- **Code Patterns**: Recognition of design patterns, algorithms, and best practices
- **Logic Explanation**: Detailed breakdown of complex functions and control flows

### 🎯 Comment Management
- **Inline Comments**: Strategic placement of explanatory comments within code
- **Function Documentation**: Comprehensive docstrings with parameters and return values
- **Code Blocks**: Sectional comments explaining code logic and purpose
- **Export Options**: Save commented code in various formats for documentation

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
![Gradio](https://img.shields.io/badge/Gradio-FF7C00?style=for-the-badge&logo=python&logoColor=white)
![Grok](https://img.shields.io/badge/Grok-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)

- **Backend**: Python with OpenAI/Grok API integration for LLM processing
- **Frontend**: Gradio web interface with modern, responsive design  
- **AI Engine**: Advanced language models for intelligent code analysis
- **Processing**: Real-time code parsing and comment generation
- **Export**: Multiple format support for documented code output

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- OpenAI API key or Grok API access
- Internet connection for API calls

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/auto-code-commenter.git
   cd auto-code-commenter
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API keys**
   ```bash
   cp .env.example .env
   # Edit .env file with your API credentials
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

## 📋 Requirements

```txt
gradio>=4.0.0
openai>=1.0.0
python-dotenv>=1.0.0
requests>=2.28.0
tiktoken>=0.5.0
anthropic>=0.8.0
langchain>=0.1.0
```

## 🎯 Usage Guide

### Code Input
1. Paste your source code in the **Code Input** area
2. Select the **Programming Language** from dropdown
3. Choose **Comment Style** (Inline, Docstring, or Comprehensive)
4. Set **Detail Level** (Basic, Intermediate, Advanced)
5. Click **Generate Comments** to process

### Comment Generation
1. AI analyzes code structure and logic
2. Generates contextual comments and documentation
3. View **Before/After Comparison** in split view
4. Download commented code using **Export Code** button

### Advanced Features
1. Access **Batch Processing** for multiple files
2. Use **Custom Prompts** for specific commenting styles
3. Configure **API Settings** for different LLM providers
4. Save **Comment Templates** for consistent documentation

### Core Operations
- **Analyze Code**: Intelligent parsing of code structure
- **Generate Comments**: AI-powered comment creation
- **Compare Results**: Side-by-side before/after view
- **Export Documentation**: Save in multiple formats

## 📁 Project Structure

```
auto-code-commenter/
├── app.py                 # Gradio application entry point
├── requirements.txt       # Python dependencies

```

## 💾 API Configuration

```python
# .env file configuration
OPENAI_API_KEY=your_openai_api_key_here
GROK_API_KEY=your_grok_api_key_here

# Model Settings
LLM_MODEL=x-ai/grok-4-fast:free
MAX_TOKENS=2000000
TEMPERATURE=0.7
TIMEOUT=30

# Application Settings
GRADIO_PORT=7860
SHARE_GRADIO=False
DEBUG_MODE=False
```

## 📊 Features Breakdown

### Code Analysis System
- **Syntax Parsing**: Advanced parsing of code structure and components
- **Logic Understanding**: AI-powered comprehension of code functionality
- **Pattern Recognition**: Identification of design patterns and algorithms
- **Context Awareness**: Understanding of variable scope and function relationships

### Comment Generation Engine
- **Intelligent Placement**: Strategic positioning of comments for maximum clarity
- **Multi-Style Support**: Inline comments, docstrings, and block comments
- **Language Adaptation**: Commenting styles adapted to specific programming languages
- **Educational Focus**: Comments designed to help beginners understand code logic

### Export & Documentation
- **Multiple Formats**: Export as .py, .js, .java, .md, and more
- **Documentation Generation**: Create comprehensive code documentation
- **Batch Processing**: Handle multiple files simultaneously
- **Template System**: Consistent commenting styles across projects

## 🧪 Example Usage

### Input Code:
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

result = fibonacci(10)
print(result)
```

### AI-Generated Output:
```python
def fibonacci(n):
    """
    Calculate the nth Fibonacci number using recursive approach.
    
    Args:
        n (int): Position in the Fibonacci sequence (0-indexed)
        
    Returns:
        int: The nth Fibonacci number
        
    Time Complexity: O(2^n) - exponential due to repeated calculations
    Space Complexity: O(n) - due to recursion stack depth
    """
    # Base case: First two Fibonacci numbers are 0 and 1
    if n <= 1:
        return n
    
    # Recursive case: Sum of the two preceding Fibonacci numbers
    # F(n) = F(n-1) + F(n-2)
    return fibonacci(n-1) + fibonacci(n-2)

# Calculate the 10th Fibonacci number (55)
result = fibonacci(10)

# Output the result to console
print(result)  # Expected output: 55
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add new commenting feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

## 🛡️ License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **OpenAI** for providing powerful language models
- **Grok API** for advanced code understanding capabilities
- **Gradio** for excellent web interface framework
- **Python Community** for robust development ecosystem

## 📈 Future Enhancements

- [ ] IDE Plugin Development (VS Code, PyCharm, IntelliJ)
- [ ] Real-time code commenting during typing
- [ ] Team collaboration features with shared templates
- [ ] Advanced code quality analysis integration

---

**Built for developers who value clean, documented code** 🚀

⭐ **Star this repository if you find it helpful for code documentation!**
