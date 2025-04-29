📄 AI Paper Detector with Sapling API
This project is a Python script that automatically scans .docx and .pdf files in a folder to detect AI-generated writing using the Sapling AI Detection API.
It flags papers that exceed a specified AI likelihood threshold and saves the results in a convenient CSV file.

🚀 Features
Supports batch scanning of .docx and .pdf files.

Works with the Sapling AI Detection API.

Flags documents as High AI Risk or Low AI Risk based on a customizable threshold (default > 0.2).

Automatically saves results into a CSV report.

Includes error handling and API rate limit management.

🛠 Requirements
Install the required libraries using:
pip install -r requirements.txt

Main dependencies:

requests

pandas

python-docx

PyMuPDF (for PDF reading)

📂 Project Structure
/your_project/
│
├── detect_ai_papers_sapling.py   # Main Python script
├── requirements.txt              # Python dependencies
├── README.md                     # This file
└── /papers/                      # Folder containing .docx and .pdf files
⚙️ Setup Instructions
Get a Sapling API Key:
Sign up at Sapling.ai.
Navigate to your dashboard and generate an API Key.

Configure the script:
Open detect_ai_papers_sapling.py.

Replace the placeholder:
SAPLING_API_KEY = "YOUR_API_KEY_HERE"

Set the path to your folder of papers:
PAPERS_FOLDER = "/path/to/your/papers"

Run the script:
python detect_ai_papers_sapling.py

View results:
After scanning, the script will generate a CSV file:

sapling_ai_detection_results.csv
The CSV will list each file with its AI score and risk flag.

⚡ Notes
API limits: Free Sapling accounts have very limited API calls. You may need a paid account for scanning a large number of documents.

Threshold: You can adjust the detection threshold easily inside the script if needed.

Large files: The script automatically trims text to a maximum of 8000 words for performance.

📜 License
This project is licensed under the MIT License.
See the LICENSE file for more information.

✍️ Author
Phillip Nott 
https://github.com/Phillip-Nott

🔥 Example Usage
python detect_ai_papers_sapling.py
After processing, check your papers/ folder for the CSV report!

🚨 Disclaimer
AI detection is not 100% accurate.
This tool provides risk indications, but final judgment should be made by a human reviewer.
