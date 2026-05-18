# Quick Start Guide

**For:** Workshop Participants  
**Purpose:** Fast reference for the workshop day

---

## 🚀 Before You Arrive

### 1. Verify Access (Do this 1 week before)

- [ ] Log into watsonx Orchestrate
- [ ] Log into Langflow  
- [ ] Test IBM Bob access
- [ ] Download ONI report for Chapter 1

### 2. Technical Setup

**Required:**
- Laptop with Chrome or Firefox
- Stable internet connection
- Access credentials (check email)

**Optional:**
- Second monitor for reference materials
- Notebook for ideas

---

## 📅 Workshop Day Schedule

| Time | Chapter | What You'll Build |
|------|---------|-------------------|
| 10:00-11:45 | Setup | Get all tools working |
| **11:45-12:15** | **Chapter 1** | **Simple document Q&A** |
| 12:15-1:00 | LUNCH | Break |
| **1:00-1:25** | **Chapter 2A** | **Weather tool (Bob)** |
| **1:25-1:50** | **Chapter 2B** | **News monitoring (Langflow)** |
| **1:50-2:15** | **Chapter 2C** | **Automated reports (Bob)** |
| 2:15-2:30 | BREAK | Afternoon break |
| **3:15-3:30** | **Chapter 3** | **Visualizations (Bob)** |
| 3:30-4:30 | Wrap-up | Planning & discussion |

---

## 📖 Chapter Quick Links

### Chapter 1: Your First AI Assistant (30 min)
**Goal:** Get comfortable with Orchestrate  
**What:** Upload PDF, ask questions  
**Key Takeaway:** "Great for one document, but what about 50?"

👉 [Go to Chapter 1](./Chapter_1_Your_First_AI_Assistant.md)

---

### Chapter 2 Part A: Weather Tool with Bob (25 min)
**Goal:** AI-generated code  
**What:** Bob creates Python weather tool  
**Key Takeaway:** "30x faster development with AI"

👉 [Go to Chapter 2 Part A](./Chapter_2_Part_A_Weather_Tool_with_Bob.md)

---

### Chapter 2 Part B: News Integration (25 min)
**Goal:** Visual workflow building  
**What:** Langflow RSS feed parser  
**Key Takeaway:** "No-code complex logic"

👉 [Go to Chapter 2 Part B](./Chapter_2_Part_B_News_Integration.md)

---

### Chapter 2 Part C: Automated Reporting (25 min)
**Goal:** End-to-end automation  
**What:** Bob creates reports & alerts  
**Key Takeaway:** "10x faster with AI assistance"

👉 [Go to Chapter 2 Part C](./Chapter_2_Part_C_Automated_Reporting.md)

---

### Chapter 3: Visualization with Bob (15 min)
**Goal:** Rapid prototyping  
**What:** Interactive maps & dashboards  
**Key Takeaway:** "56x faster visualization"

👉 [Go to Chapter 3](./Chapter_3_Visualization_with_Bob.md)

---

## 🆘 Quick Troubleshooting

### Can't log into Orchestrate?
1. Check email for credentials
2. Try password reset
3. Ask instructor for help

### Tool not working?
1. Check internet connection
2. Refresh the page
3. Try in incognito mode
4. Ask instructor

### Stuck on a step?
1. Re-read the instruction
2. Check the troubleshooting section
3. Ask your neighbor
4. Raise your hand for help

---

## 💡 Pro Tips

### During the Workshop

1. **Don't rush** - It's okay to fall behind, instructors will help
2. **Ask questions** - No question is too basic
3. **Help others** - Teaching reinforces learning
4. **Take notes** - Capture ideas for your use cases
5. **Experiment** - Try variations of the examples

### After Each Chapter

- ✅ Verify it works before moving on
- ✅ Take a screenshot of success
- ✅ Note any customizations you made
- ✅ Think about your use cases

---

## 📝 Key Commands Reference

### Orchestrate CLI

```bash
# Authenticate
orchestrate env activate [environment-name]

# List tools
orchestrate tools list

# Import tool
orchestrate tools import --kind openapi --file tool.yaml

# Create agent
orchestrate agents create --name agent_name --tools tool1,tool2

# Update agent
orchestrate agents update --name agent_name --instructions "..."

# List agents
orchestrate agents list
```

### Common Coordinates (NZ)

```
Wellington: -41.2865, 174.7762
Auckland: -36.8485, 174.7633
Christchurch: -43.5321, 172.6362
```

---

## 🎯 Success Metrics

You'll know you're successful if:

**After Chapter 1:**
- ✅ Created an agent
- ✅ Uploaded a document
- ✅ Asked 5+ questions successfully

**After Chapter 2:**
- ✅ Weather tool works
- ✅ News monitoring works
- ✅ Reports generate automatically

**After Chapter 3:**
- ✅ Interactive map displays
- ✅ Dashboard shows data
- ✅ Can export visualizations

**End of Day:**
- ✅ Complete maritime intelligence system
- ✅ Understand AI-assisted development
- ✅ Ideas for your own use cases

---

## 📚 Resources

### During Workshop
- Main guide: [README.md](./README.md)
- Contributor guide: [CONTRIBUTOR_GUIDE.md](./CONTRIBUTOR_GUIDE.md)
- This quick start: You're reading it!

### After Workshop
- watsonx Orchestrate docs
- Langflow documentation
- IBM Bob resources
- Workshop recordings (if available)

---

## 🤝 Getting Help

### During Workshop
1. **Raise your hand** - Instructors are here to help
2. **Ask your neighbor** - Peer learning works!
3. **Check troubleshooting** - In each chapter guide

---

## 🎉 Have Fun!

This is a hands-on workshop. You'll build real, working systems. Don't worry about perfection - focus on learning and experimenting!

**See you at the workshop!**

---

**Last Updated:** May 5, 2026  
**Version:** 1.0