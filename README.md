# Maritime Intelligence Workshop - GitHub Bootcamp Guide

**Workshop Date:** May 26, 2026  
**Duration:** 6.5 hours (10:00 AM - 4:30 PM)  
**Format:** Hands-on AI Development Workshop

---

## 📚 Guide Overview

This GitHub repository contains all materials for the Maritime Situational Awareness Workshop. The workshop teaches participants how to build AI-powered intelligence systems using IBM watsonx Orchestrate, Langflow, and IBM Bob.

---

## 🎯 Workshop Objectives

By the end of this workshop, you will:

1. ✅ Understand agentic AI concepts and capabilities
2. ✅ Build a simple document Q&A assistant
3. ✅ Create a working multi-source intelligence agent
4. ✅ Build and integrate a Langflow analysis tool
5. ✅ Generate visual decision support outputs
6. ✅ Have a clear path forward for PoC development

---

## 📋 Workshop Schedule

| Time | Duration | Chapter | Description |
|------|----------|---------|-------------|
| 10:00 - 10:15 | 15 min | **Introductions** | Introductions & name tags |
| 10:15 - 10:45 | 30 min | **Agenda & Use Cases** | Workshop agenda, objectives, and maritime intelligence use cases |
| 10:45 - 11:15 | 30 min | **[Chapter 0: Environment Setup](./chapters/Chapter_0_Environment_Setup.md)** | Technical setup (Orchestrate, Langflow, Bob) |
| 11:15 - 11:45 | 30 min | **Agentic AI Concepts** | Core concepts and capabilities |
| **11:45 - 12:15** | **30 min** | **[Chapter 1: Your First AI Assistant](./chapters/Chapter_1_Your_First_AI_Assistant.md)** | Simple document Q&A with Orchestrate |
| 12:15 - 1:00 | 45 min | **Lunch break** | Break |
| **1:00 - 2:15** | **75 min** | **[Chapter 2: Document Analysis Agent](./chapters/Chapter_2_Document_Analysis_Agent.md)** | Build weather tool with Bob |
| 2:15 - 2:30 | 15 min | **Afternoon break** | Break |
| 2:30 - 3:15 | 45 min | **[Chapter 3: Advanced Analysis](./chapters/Chapter_3_Langflow_Advanced_Analysis.md)** | Langflow integration |
| 3:15 - 3:30 | 15 min | **[Chapter 4: Visualisation](./chapters/Chapter_4_Visualisation_with_Bob.md)** | Bob-generated dashboards |
| 3:30 - 4:30 | 1h | **Wrap-up & Planning** | Pressure test, discovery workshop |

---

## 📖 Chapter Guides

### Chapter 1: Your First AI Assistant
**Time:** 11:45 AM - 12:15 PM (30 min)  
**Goal:** Get comfortable with watsonx Orchestrate

**What you'll do:**
- Create a simple agent
- Upload ONI Shipping Threat Report PDF
- Ask questions about the document
- Understand limitations → why we need automation

**Key takeaway:** *"Great for one document, but what about 50 reports daily?"*

📄 **[Go to Chapter 1 Guide →](./chapters/Chapter_1_Your_First_AI_Assistant.md)**

---

### Chapter 2: Document Analysis Agent with IBM Bob
**Time:** 1:00 PM - 2:15 PM (75 min)
**Innovation:** Bob generates everything!

**What you'll do:**
- Prompt Bob to generate Python weather tool
- Bob creates YAML configuration
- Import and test in Orchestrate

**Key takeaway:** *"AI-accelerated development - what took hours now takes minutes"*

📄 **[Go to Chapter 2 Guide →](./chapters/Chapter_2_Document_Analysis_Agent.md)**

---

### Chapter 3: Advanced Analysis with Langflow
**Time:** 2:30 PM - 3:15 PM (45 min)
**Goal:** Build visual workflows for maritime intelligence

**What you'll do:**
- Create a Langflow pipeline with visual blocks
- Pull live RSS feeds with Python Interpreter
- Extract structured maritime incidents using AI
- Return JSON data for downstream workflows

**Key takeaway:** *"Visual workflows turn RSS feeds into structured intelligence"*

📄 **[Go to Chapter 3 Guide →](./chapters/Chapter_3_Langflow_Advanced_Analysis.md)**

---

### Chapter 4: Visualisation with Bob
**Time:** 3:15 PM - 3:30 PM (15 min)
**Goal:** Generate dashboards and visualisations

**What you'll do:**
- Prompt Bob to create interactive maps
- Generate intelligence dashboards with Plotly
- Create visual decision support outputs
- Export visualisations for reporting

**Key takeaway:** *"Bob generates production-ready visualisations in minutes"*

📄 **[Go to Chapter 4 Guide →](./chapters/Chapter_4_Visualisation_with_Bob.md)**

---

## 🛠️ Technical Requirements

### Pre-Workshop Setup
- [ ] watsonx Orchestrate account provisioned
- [ ] Langflow account provisioned
- [ ] IBM Bob access confirmed
- [ ] ONI report downloaded for Chapter 1

### Participant Requirements
- Laptop with web browser (Chrome/Firefox)
- Stable internet connection
- Access credentials (sent 1 week before)

---

## 📁 Repository Structure

```
maritime-intelligence-ai-agent-development-workshop/
├── README.md                                    # This file
├── chapters/                                    # Workshop chapters
│   ├── Chapter_0_Environment_Setup.md          # Environment setup
│   ├── Chapter_1_Your_First_AI_Assistant.md    # Chapter 1 guide
│   ├── Chapter_2_Document_Analysis_Agent.md    # Chapter 2 guide
│   ├── Chapter_3_Langflow_Advanced_Analysis.md # Chapter 3 guide
│   ├── Chapter_4_Visualisation_with_Bob.md     # Chapter 4 guide
│   ├── assets/                                  # Sample data and files
│   └── images/                                  # Screenshots and images
└── reference/                                   # Additional resources (if needed)
```

---

## 🚀 Getting Started

### Before the Workshop

1. **Verify Access**
   - Log into watsonx Orchestrate
   - Log into Langflow
   - Test IBM Bob access

2. **Download Materials**
   - ONI Worldwide Threat to Shipping Report
   - Workshop slides (if provided)

3. **Review Prerequisites**
   - Basic understanding of APIs
   - Familiarity with JSON format
   - No coding experience required!

### During the Workshop

1. **Follow Along**
   - Each chapter has step-by-step instructions
   - Screenshots provided for reference
   - Instructors available for help

2. **Ask Questions**
   - No question is too basic
   - Share your screen if stuck
   - Help your neighbors

3. **Take Notes**
   - Document what works for you
   - Note any customizations
   - Capture ideas for your use cases

---

## 📚 Additional Resources

### Documentation
- [watsonx Orchestrate Documentation](https://www.ibm.com/docs/en/watsonx/watson-orchestrate)
- [Langflow Documentation](https://docs.langflow.org/)
- [IBM Bob Documentation](https://www.ibm.com/products/watsonx-code-assistant)

### Data Sources
- [ONI Worldwide Threat to Shipping Reports](https://www.oni.navy.mil/ONI-Reports/Shipping-Threat-Reports/)
- [Open-Meteo Weather API](https://open-meteo.com/)
- [Maritime News Sources](./reference/Maritime_News_Sources.md)

---

## 🎓 Learning Path

### Beginner Track
1. Complete Chapter 1 (Your First AI Assistant)
2. Follow Chapter 2 Part A (Weather Tool)
3. Understand the concepts
4. Ask questions

### Advanced Track
1. Complete all chapters
2. Customize the tools
3. Explore additional integrations
4. Plan your own use cases

---

## 🤝 Contributing

Found an issue or have a suggestion?
- Open an issue in this repository
- Submit a pull request
- Contact the workshop team

---

## 📝 License

This workshop material is provided for educational purposes for workshop personnel and authorized participants.

---

## 👥 Workshop Team

**IBM Team:**
- Libby Lavrova - Workshop Lead
- [Additional team members]

---

## 📞 Contact

For questions about this workshop:
- **Email:** libbyjen@nz1.ibm.com
- **Workshop Date:** May 26, 2026
- **Location:** [To be confirmed]

---

**Last Updated:** May 5, 2026  
**Version:** 1.0  
**Status:** Ready for Workshop