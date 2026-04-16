# 🤖 Agent-Orchestration Framework with LangChain  
Project Code: #M-13-26  

## 📌 Project Overview  
This project demonstrates a complete Agent-Orchestration Framework built using LangChain. It showcases how multiple AI agents can collaborate, use tools, and automate workflows to perform complex tasks. The system evolves from a simple agent to a fully functional multi-agent workflow automation system with API and UI.

## 🎯 Objective  
- Build intelligent AI agents using LangChain  
- Enable collaboration between multiple agents  
- Integrate tools and memory into agents  
- Automate a real-world workflow  
- Provide API and frontend interface for interaction  

## 🔄 Workflow  
User Input → Research Agent → Summarizer Agent → Email Agent → Output  

## 🧠 Features  
- Multi-agent collaboration system  
- Tool integration (Calculator, Weather API)  
- Memory-based reasoning (ConversationBufferMemory)  
- Automated workflow execution  
- REST API using Flask  
- Responsive frontend interface  
- Modular and scalable architecture  

## 🧩 Milestones  

### Milestone 1 — Basic Agent  
- Created a simple conversational agent  
- Implemented prompt templates  
- Built console-based interaction  
File: console_agent.py  

### Milestone 2 — Tool Integration  
- Added Calculator tool  
- Added simulated Weather API  
- Enabled agent to use tools dynamically  
File: tools_agent.py  

### Milestone 3 — Multi-Agent System  
- Implemented multiple agents: Research Agent, Summarizer Agent, Email Agent  
- Added memory using ConversationBufferMemory  
- Enabled agent communication  
File: multi_agent_system.py  

### Milestone 4 — Workflow Automation  
- Designed full workflow system  
- Built REST API using Flask  
- Developed responsive UI  
- Integrated frontend with backend  
Files: workflow_agents.py, workflow_api.py, index.html  

## 📁 Project Structure  
LangChain_Project  
│  
├── console_agent.py  
├── tools_agent.py  
├── multi_agent_system.py  
├── workflow_agents.py  
├── workflow_api.py  
├── templates  
│     └── index.html  
├── README.md  
├── .env  
└── pyvenv.cfg  

## ⚙️ Installation & Setup  

1. Clone Repository  
git clone https://github.com/Afreen-Akbar-Ali/Agent-Orchestration-LangChain.git  
cd Agent-Orchestration-LangChain  

2. Install Dependencies  
pip install langchain==0.1.0 flask  

3. Run Application  
python workflow_api.py  

4. Open in Browser  
http://127.0.0.1:5000  

## 🧪 Example Inputs  
- Artificial Intelligence  
- Machine Learning  
- Python  
- Data Science  

## 📊 Use Cases  
- Automated research assistance  
- Email drafting  
- Content summarization  
- Business workflow automation  
- AI-based chatbot systems  

## ⚖️ Advantages  
- Modular and scalable design  
- Improved efficiency through collaboration  
- Memory-based contextual understanding  
- Tool-enhanced capabilities  

## ⚠️ Limitations  
- Increased system complexity  
- Requires proper orchestration  
- Dependency on external libraries  
- Version compatibility issues  

## 🚀 Future Scope  
- Integration with real APIs  
- Database-based memory storage  
- More specialized agents  
- Cloud deployment  
- Voice-based interaction  

## 🏁 Conclusion  
This project successfully demonstrates how multiple AI agents can collaborate to automate complex workflows. It highlights the practical application of LangChain in building scalable and intelligent systems.

## 👩‍💻 Author  
Afreen  
