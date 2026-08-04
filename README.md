# AI CyberShield - AI-Powered Cybersecurity Assistant

![AI CyberShield Banner](https://via.placeholder.com/1200x400/1e3a8a/ffffff?text=AI+CyberShield)

A comprehensive web application that provides AI-powered cybersecurity tools including phishing detection, password strength analysis, URL checking, and an AI cybersecurity assistant. Built with Python, Flask, and Google's Gemini AI.

## 🌟 Features

### 🔍 Phishing Email Detector
- Analyze emails and messages for potential phishing attempts
- Identify suspicious patterns and common phishing tactics
- Get instant risk assessment

### 🧱 Password Strength Analyzer
- Evaluate password strength on a scale of 1-10
- Get immediate feedback on password security
- Learn how to create stronger passwords

### 🌐 Malicious URL Checker
- Check URLs for potential security risks
- Identify suspicious domains and patterns
- Get safety recommendations

### 💬 AI Cybersecurity Assistant
- Get instant answers to cybersecurity questions
- Learn about security best practices
- Understand complex security concepts in simple terms

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Google Gemini API key (free tier available)
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/cyber-security-ai.git
   cd cyber-security-ai
   ```

2. **Set up a virtual environment**
   ```bash
   # For Windows
   python -m venv venv
   .\venv\Scripts\activate

   # For macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your API key**
   - Get your Google Gemini API key from [Google AI Studio](https://aistudio.google.com/)
   - Open `app.py` and replace `YOUR_API_KEY` with your actual API key:
     ```python
     genai.configure(api_key="YOUR_API_KEY")
     ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the application**
   Open your web browser and visit: `http://localhost:5000`

## 🛠️ How It Works

### Backend Architecture
- Built with Python and Flask web framework
- Uses Google's Gemini AI for natural language processing
- RESTful API endpoints for each feature
- Error handling and input validation

### Frontend Design
- Responsive UI built with Tailwind CSS
- Interactive tabs for easy navigation
- Sample data for quick testing
- Real-time feedback and loading states

### AI Integration
- Uses Google's Gemini 2.5 Flash model
- Optimized prompts for accurate responses
- Rate limiting and error handling

## 📚 Usage Guide

### Phishing Email Detection
1. Navigate to the "Phishing Detector" tab
2. Paste the suspicious email content
3. Click "Analyze Email"
4. Review the analysis results

### Password Strength Analysis
1. Go to the "Password Analyzer" tab
2. Enter a password to test
3. View the strength rating and suggestions
4. Try different passwords to compare

### URL Safety Check
1. Select the "URL Checker" tab
2. Enter the URL to analyze
3. Click "Check URL"
4. Review the safety assessment

### AI Cybersecurity Assistant
1. Open the "AI Assistant" tab
2. Type your cybersecurity question
3. Press Enter or click the send button
4. Get an instant, informative response

## 🔧 Troubleshooting

### Common Issues
- **API Key Errors**: Ensure your Google Gemini API key is correctly set in `app.py`
- **Connection Issues**: Verify your internet connection
- **Empty Responses**: Try rephrasing your question or using different input

### Getting Help
If you encounter any issues, please:
1. Check the browser's developer console for errors (F12)
2. Review the terminal output for backend errors
3. Ensure all dependencies are installed correctly

## 📦 Dependencies

### Backend
- Flask 2.3.3
- google-generativeai 0.3.2
- python-dotenv 1.0.0
- requests 2.31.0

### Frontend
- Tailwind CSS 2.2.19
- Font Awesome 6.0.0
- Vanilla JavaScript

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Google for the Gemini AI
- The open-source community for various libraries and tools
- All contributors who helped improve this project

## 📬 Contact

For questions or feedback, please contact:
- Email: your.email@example.com
- GitHub: [@yourusername](https://github.com/yourusername)

---

<div align="center">
  Made with ❤️ for better cybersecurity
</div>
