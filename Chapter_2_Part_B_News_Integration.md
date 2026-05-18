# Chapter 2 Part B: News Integration with Langflow

**Time:** 1:25 PM - 1:50 PM (25 minutes)  
**Goal:** Build maritime news monitoring using Langflow visual workflow  
**Difficulty:** Intermediate  
**Prerequisites:** Completed Part A, Langflow access  
**Authors:** @Ethan Samuels @Wilson Wang

---

## 🎯 Learning Objectives

By the end of this section, you will:

1. ✅ Build a visual workflow in Langflow
2. ✅ Connect to RSS feed parser for maritime news
3. ✅ Export Langflow flow as a tool
4. ✅ Import tool into watsonx Orchestrate
5. ✅ Combine news + weather intelligence

---

## 📖 What We're Building

A Langflow workflow that:
- Monitors maritime news RSS feeds (Maritime Executive, gCaptain, Splash247)
- Parses and categorizes news articles
- Extracts incident information
- Returns structured news data
- Integrates with existing weather agent

---

## 🚀 Step-by-Step Instructions

### Step 1: Access Langflow (2 minutes)

**[TO BE COMPLETED BY @Ethan Samuels @Wilson Wang]**

Instructions for:
- Opening Langflow interface
- Creating new flow
- Understanding the visual editor

---

### Step 2: Build Visual Workflow (12 minutes)

**[TO BE COMPLETED BY @Ethan Samuels @Wilson Wang]**

#### Component 1: RSS Feed Input
- How to add RSS feed component
- Configure feed URLs
- Set refresh intervals

#### Component 2: News Parser
- Parse RSS feed data
- Extract title, date, summary, link
- Handle multiple sources

#### Component 3: Categorization Logic
- Categorize by incident type
- Add relevance scoring
- Filter by keywords

#### Component 4: Output Formatter
- Structure as JSON
- Include metadata
- Return to Orchestrate

---

### Step 3: Test in Langflow Playground (5 minutes)

**[TO BE COMPLETED BY @Ethan Samuels @Wilson Wang]**

Test cases:
- Query latest maritime news
- Search for specific incidents
- Filter by region
- Verify JSON output

---

### Step 4: Export as Tool (3 minutes)

**[TO BE COMPLETED BY @Ethan Samuels @Wilson Wang]**

Instructions for:
- Exporting flow as JSON
- Saving configuration
- Preparing for import

---

### Step 5: Import to Orchestrate (3 minutes)

**[TO BE COMPLETED BY @Ethan Samuels @Wilson Wang]**

CLI commands:
```bash
# Import Langflow tool
orchestrate tools import --kind langflow --file maritime_news_tool.json

# Verify import
orchestrate tools list | grep maritime_news
```

---

### Step 6: Add to Agent and Test (5 minutes)

**[TO BE COMPLETED BY @Ethan Samuels @Wilson Wang]**

Update agent with news tool:
```bash
orchestrate agents update --name maritime_weather_agent \
  --tools getWeatherForecast,get_maritime_news
```

Test queries:
- "What's the latest maritime news?"
- "Show me recent shipping incidents in Southeast Asia"
- "What's happening in the Gulf of Aden?" (combines weather + news)

---

## 🎓 Key Takeaways

**[TO BE COMPLETED BY @Ethan Samuels @Wilson Wang]**

- Visual workflow benefits
- Langflow vs. code
- Integration patterns
- Multi-source intelligence

---

## 🔧 Troubleshooting

**[TO BE COMPLETED BY @Ethan Samuels @Wilson Wang]**

Common issues and solutions

---

## 📊 Success Criteria

You've successfully completed Part B if:

- ✅ Langflow workflow created
- ✅ RSS feeds connected
- ✅ Tool exported and imported
- ✅ Agent uses news tool correctly
- ✅ Combined weather + news queries work

---

## 📚 Additional Resources

**[TO BE COMPLETED BY @Ethan Samuels @Wilson Wang]**

- Langflow documentation links
- RSS feed sources
- Example workflows

---

**Chapter Authors:** @Ethan Samuels @Wilson Wang  
**Last Updated:** [TO BE COMPLETED]  
**Version:** 1.0 (SKELETON)  
**Estimated Time:** 25 minutes  
**Difficulty:** ⭐⭐ Intermediate

---

[← Back to Part A](./Chapter_2_Part_A_Weather_Tool_with_Bob.md) | [Next: Part C →](./Chapter_2_Part_C_Automated_Reporting.md)