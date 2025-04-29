import os
import requests
import fitz  # PyMuPDF (for PDFs)
import pandas as pd
from docx import Document
import time

# === CONFIGURATION ===
SAPLING_API_KEY = "B9DGKUZUQROHHROD9F4O4CKDLDVQESLZ"  # <-- Replace with your actual API key
PAPERS_FOLDER = "/mnt/c/Users/philm/Documents/papers"  # <-- Set your actual folder path for papers
#MAX_WORDS = 8000  # Limit text to 8000 words
DELAY_SECONDS = 3  # Delay to avoid hitting API rate limits

# === Text Extraction Functions ===
def extract_text_from_docx(file_path):
    """Extract text from .docx files."""
    doc = Document(file_path)
    return '\n'.join(para.text for para in doc.paragraphs)

def extract_text_from_pdf(file_path):
    """Extract text from .pdf files."""
    doc = fitz.open(file_path)
    return '\n'.join(page.get_text() for page in doc)

# === AI Detection Function with Sapling API ===
def check_text_for_ai(text):
    """Check the text with Sapling's AI detection API."""
    url = "https://api.sapling.ai/api/v1/aidetect"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "key": SAPLING_API_KEY,  # Use your API key
        "text": text
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            result = response.json()
            ai_score = result.get("score", None)
            return {"ai": ai_score}
        else:
            print(f"API Error {response.status_code}: {response.text}")
            return None
    except Exception as e:
        print(f"Request failed: {e}")
        return None

# === Main Function to Process Papers ===
def main():
    results = []

    # Loop through files in the target folder
    for filename in os.listdir(PAPERS_FOLDER):
        if filename.endswith((".docx", ".pdf")):
            file_path = os.path.join(PAPERS_FOLDER, filename)
            print(f"Processing: {filename}")

            try:
                # Extract text based on file type
                text = extract_text_from_docx(file_path) if filename.endswith(".docx") else extract_text_from_pdf(file_path)

                # Truncate text to the first 8000 words if necessary
                #words = text.split()
                #if len(words) > MAX_WORDS:
                    #words = words[:MAX_WORDS]
                    #text = " ".join(words)

                # Check AI score using Sapling API
                result = check_text_for_ai(text)
                if result:
                    ai_score = result.get("ai", "Error")
                    flag = "High AI Risk" if ai_score > 0.4 else "Low AI Risk"  # Change to 0.2 threshold
                else:
                    ai_score = "Error"
                    flag = "Error"

                # Append result to list
                results.append({
                    "Filename": filename,
                    "AI_Score": ai_score,
                    "Flag": flag
                })

            except Exception as e:
                print(f"Error processing {filename}: {e}")
                results.append({
                    "Filename": filename,
                    "AI_Score": "Error",
                    "Flag": "Error"
                })

            # Delay between requests to avoid hitting rate limits
            time.sleep(DELAY_SECONDS)

    # Save results to CSV
    df = pd.DataFrame(results)
    output_file = os.path.join(PAPERS_FOLDER, "sapling_ai_detection_results.csv")
    df.to_csv(output_file, index=False)
    print(f"\n✅ Detection complete. Results saved to: {output_file}")

if __name__ == "__main__":
    main()
