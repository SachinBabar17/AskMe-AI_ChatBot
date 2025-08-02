# AskMe Chatbot

AskMe is a simple web-based chatbot that uses the Hugging Face API to generate AI-powered responses to user questions.

## Prerequisites

- **Python 3.8+** installed on your system
- **pip** (Python package manager)
- A **Hugging Face API token** ([get one here](https://huggingface.co/settings/tokens))
- Internet connection

## Setup Instructions

1. **Clone or Download the Repository**

   ```
   git clone <your-repo-url>
   cd 1_AskME
   ```

2. **Create and Activate a Virtual Environment (Recommended)**

   ```
   python -m venv venv
   venv\Scripts\activate   # On Windows
   # source venv/bin/activate   # On macOS/Linux
   ```

3. **Install Required Python Packages**

   ```
   pip install flask requests python-dotenv
   ```

4. **Set Up Your Hugging Face API Token**

   - Create a file named `.env` in the project root directory.
   - Add your Hugging Face token to the file:
     ```
     HF_TOKEN=your_huggingface_token_here
     ```

5. **Project Structure**

   ```
   1_AskME/
   ├── app.py
   ├── .env
   ├── templates/
   │   └── index.html
   └── static/
       └── script.js
   ```

6. **Run the Application**

   ```
   python app.py
   ```

7. **Access the Chatbot**

   - Open your browser and go to: [http://localhost:5000](http://localhost:5000)

## Technologies Used

- Python, Flask, Requests, python-dotenv
- Hugging Face Inference API
- HTML, CSS, JavaScript (Fetch API)

## Usage

- Type your question in the input box and press **Send** or hit **Enter**.
- The chatbot will reply using the Hugging Face AI model.

---

**Note:**  
Your Hugging Face API token is required for the chatbot to function. Keep it secure and do not share it publicly.