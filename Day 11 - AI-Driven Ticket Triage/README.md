# Day 11: AI-Driven Ticket Triage 🚦 – Aug 18, 2025

## Challenge Description 🎯
Automatically triage new incident tickets (from Jira, ServiceNow, etc.) using ML/NLP to classify them as network, database, or application issues, and auto-assign to the correct team using Jira components and automation.

## Objective 🚀
- Ingest new incident tickets from Jira API
- Use an ML model to classify ticket type (network, db, app)
- Tag tickets with the correct Jira component for team assignment
- Use Jira automation to assign tickets to the Component Lead
- Provide logs and visual feedback for triage actions

## Code & Implementation 💻
- **Ticket Triage Script**: [`ticket_triage.py`](./ticket_triage.py)  
  Main logic for fetching, classifying, and tagging Jira tickets.
- **Step-by-Step Solution**: [`Step-by-Step-Solution.md`](./Step-by-Step-Solution.md)  
  Detailed guide for setup, workflow, and Jira automation.
- **Sample Tickets**: [`create_tickets.py`](./create_tickets.py)  
  Script to create sample tickets in Jira for testing.
- **Training Data**: [`ticket_history.csv`](./ticket_history.csv)  
  Labeled historical tickets for ML model training.
- **Images**: [`images/`](./images/)  
  Screenshots of Jira automation, ticket creation, and script execution.

## Workflow 🔄
1. **Prepare Historical Data:**  
   Create and label `ticket_history.csv` for ML training.
2. **Train ML Model:**  
   Use `ticket_triage.py` to train a classifier on ticket categories.
3. **Jira Component Setup:**  
   Create components (Network, Database, Application) and set Component Leads.
4. **Jira Automation:**  
   Configure Jira automation to assign tickets to Component Lead when component is updated.
5. **Create Sample Tickets:**  
   Use `create_tickets.py` to add test tickets to Jira.
6. **Run Triage Script:**  
   Execute `ticket_triage.py` to fetch, classify, and tag tickets.
7. **Review Logs & Results:**  
   Check logs and Jira for correct assignment and tagging.

## Why Each Step Was Chosen 📊

- **ML Classification:**  
  Automates ticket sorting for speed and accuracy.
- **Jira Components:**  
  Enables team-based assignment and queueing.
- **Jira Automation:**  
  Ensures tickets are assigned to the right lead after tagging.
- **Logging:**  
  Provides transparency and debugging for every step.

## Interpretation of Results 🧠

- **Correct Tagging:**  
  Tickets are visible in the right team queues.
- **Auto-Assignment:**  
  Jira automation ensures tickets reach the right owner.
- **Logs:**  
  Show every ticket processed and tagged.

## What Did I Learn 🧩
- ML can automate ticket triage and improve accuracy.
- Jira components and automation streamline team assignment.
- Continuous feedback and iteration improve the workflow.

## How to Use in Real-World DevOps/SRE 🌍

### Automated Ticket Triage and Assignment
**Use Case:**  
Automatically triage and tag incoming tickets so teams can pick up relevant issues from their Jira component queue.

**Implementation:**  
- Train an ML model on historical ticket data to classify tickets into categories.
- Use Jira API to fetch new tickets and tag them with the correct component.
- Jira automation assigns tickets to the component lead, who can delegate further.

**Advantage:**  
- Reduces manual effort and speeds up ticket handling.
- Ensures tickets are visible to the right teams for faster resolution.

**Industry Example:**  
A tech company receives a high volume of support tickets daily. Their ML-based triage system tags tickets with components like "Network", "Database", and "Application". Jira automation assigns tickets to the component lead, and team members pick up tickets from their queue, reducing triage time from hours to minutes.

## Where Was AI Used? 🤖

- **AI Used:**  
  Machine learning (scikit-learn) was used to classify incident tickets into network, database, or application issues.  
  NLP and ML enabled automated ticket triage and tagging for Jira integration.

**AI Technologies Used:**  
- scikit-learn (ML classifier)
- Python (NLP, Jira API integration)

## References 📖
- [Jira REST API Documentation](https://developer.atlassian.com/cloud/jira/platform/rest/v2/)
- [Jira Automation](https://support.atlassian.com/jira-software-cloud/docs/automate-your-jira-cloud-processes/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Requests Documentation](https://docs.python-requests.org/en/master/)

## Future Enhancements 🚀
- Improve ML model with more data and advanced techniques (e.g., deep learning).
- Add support for multi-language ticket triage.
- Integrate with other tools and platforms for broader automation.


