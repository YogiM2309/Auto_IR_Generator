# Auto_IR_Generator
Project Title : Automatic Security Incident report Generation using LLM (local) and based on manual prompts.
uses a locally hosted LLaMA 3 model (via Ollama or llama-cpp-python) to generate an automatic security incident investigation report, based on manual prompts such as:
•	start date
•	reported date
•	incident details (can be full narrative or keywords)
It generates a report with the following structure:
•	Executive Summary
•	Investigation Details
•	Tools Used
•	Indicators of Compromise (IOCs)
•	Recommendations
•	Conclusion


**Requirements**
•	Ollama installed and running llama3 (e.g., ollama run llama3)
•	Python 3.8+
•	Installed requests (for HTTP call to local Ollama API)
Install:
step1 : download Ollam
Go to https://ollama.com/download and download ollama as per your Operating system ( Window / Linux / MacOS)
  - Execute ollamasetup.exe and once it is completed check if it is running by opening browser and type localhost:11434
step 2 : download Model - search for llama3 and execute it from bash / powershell
  - To pull model  C:\ollama pull llama3.2
  -  To Run model C:\ollama run llama3.2
    
pip install requests

Install dependencies using:

```bash
pip install -r requirements.txt

**How to Run**
run auto_Incident_report.py
