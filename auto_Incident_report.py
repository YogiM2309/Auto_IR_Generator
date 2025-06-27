import requests

# Change this if your Ollama endpoint is remote
OLLAMA_API_URL = "http://localhost:11434/api/generate"

def get_user_inputs():
    print("Enter incident report details:\n")
    start_date = input("Start Date (YYYY-MM-DD): ")
    reported_date = input("Reported Date (YYYY-MM-DD): ")
    incident_details = input("Brief description of the incident:\n")
    return start_date, reported_date, incident_details

def construct_prompt(start_date, reported_date, incident_details):
    prompt = f"""
You are a cybersecurity analyst tasked with generating a professional security incident investigation report.

Generate a full report based on the following input:
Start Date: {start_date}
Reported Date: {reported_date}
Incident Details: {incident_details}

Include the following sections:

1. Executive Summary
2. Investigation Details
3. Tools Used
4. Indicators of Compromise (IOCs)
5. Recommendations
6. Conclusion

Ensure the report is formal, concise, and clearly structured.
"""
    return prompt.strip()

def generate_report(prompt):
    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False  # For full output instead of chunks
    }
    response = requests.post(OLLAMA_API_URL, json=payload)
    if response.status_code == 200:
        return response.json()['response']
    else:
        print("Error:", response.text)
        return None

def save_report(text, filename="incident_report.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"\n✅ Report saved to {filename}")

def main():
    start_date, reported_date, incident_details = get_user_inputs()
    prompt = construct_prompt(start_date, reported_date, incident_details)
    print("\n⏳ Generating report with LLaMA 3...")
    report = generate_report(prompt)
    if report:
        print("\n📄 --- Generated Report ---\n")
        print(report)
        save_report(report)

if __name__ == "__main__":
    main()
