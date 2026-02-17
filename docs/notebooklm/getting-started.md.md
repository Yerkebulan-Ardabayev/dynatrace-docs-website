# Dynatrace Documentation: getting-started.md

Generated: 2026-02-17

Files combined: 1

---


## Source: getting-started.md


# Getting Started with Dynatrace

Welcome to Dynatrace! This guide will help you get started with monitoring your applications and infrastructure.

## What is Dynatrace?

Dynatrace is an AI-powered, full-stack monitoring platform that provides:

- **Application Performance Monitoring (APM)**
- **Infrastructure Monitoring**
- **Digital Experience Monitoring**
- **AIOps and automation**

## Quick Start Steps

### 1. Choose Your Deployment

Dynatrace offers two deployment options:

=== "SaaS"

    **Recommended for most users**
    
    - Fully managed by Dynatrace
    - Automatic updates
    - No infrastructure management needed
    
    [Learn more about SaaS →](#)

=== "Managed"

    **For on-premises deployment**
    
    - Self-hosted in your data center
    - Full control over your data
    - Meets specific compliance requirements
    
    [Learn more about Managed →](managed/index.md)

### 2. Install OneAgent

OneAgent is the all-in-one monitoring agent:

```bash
# Example installation on Linux
wget -O Dynatrace-OneAgent.sh "<download-url>"
sudo /bin/sh Dynatrace-OneAgent.sh
```

[Full installation guide →](#)

### 3. Start Monitoring

Once OneAgent is installed, Dynatrace automatically discovers and monitors:

- ✅ Applications and services  
- ✅ Processes and infrastructure
- ✅ Network connections
- ✅ User experiences

## Next Steps

- [Explore your environment](#)
- [Set up synthetic monitoring](#)
- [Create custom dashboards](#)
- [Configure alerts](#)

## Need Help?

- 🤖 [Ask the AI Assistant](../ai/gemini.md)
- 📚 [Browse full documentation](index.md)
- 🔬 [Deep dive with NotebookLM](../ai/notebooklm.md)


---
