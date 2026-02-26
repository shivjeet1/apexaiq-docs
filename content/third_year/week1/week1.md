---
layout: default
title: "WEEK1 - Detailed Research & Topics"
---

# ApexaiQ Internship 2026: Week 1 Research

### The Main Problem ApexaiQ Solves
Most companies have a "Visibility Gap." The Cloud team, Security team, and IT team all have different lists of assets. ApexaiQ connects to all these tools (agentless), pulls the data, and deduplicates it. It gives a single "Source of Truth" so you know exactly what you own and what is at risk.

### 5 Pain Points for ApexaiQ customers

| For Enterprises (Big Companies) | For MSPs (Service Providers) |
| :--- | :--- |
| **Shadow IT:** Employees using apps or cloud servers without telling IT. | **Scalability:** Managing 50+ different clients using just Excel sheets. |
| **Audit Fatigue:** Spending weeks gathering data for compliance like ISO or HIPAA. | **Margin Pressure:** Proving value to the client to justify their monthly fees. |
| **Tool Sprawl:** Having 50 tools that don't talk to each other. | **Asset Billing:** Finding "hidden" devices they should be charging for. |
| **Technical Debt:** Old servers (like Windows 2008) that are risky but still running. | **SLA Liability:** Getting blamed if a client is hacked because of a missed patch. |
| **Asset Hygiene:** Devices missing basic security like EDR or proper patches. | **Engineer Burnout:** Constant firefighting instead of doing actual work. |

---

### Core Research Topics

**1. Cyber Assets & Discovery**
* **Cyber Asset:** Anything with an IP or login—Laptops, S3 buckets, or User IDs.
* **Asset Discovery:** Finding what's on the network.
* **Attack Surface:** The total number of points where a hacker can enter.

**2. Vulnerabilities & Remediation**
* **CVE:** Unique ID for a bug.
* **CPE:** Standard name for software/hardware.
* **Remediation:** Actually fixing the bug (usually by patching).
* **Non-CVE Vulns:** Risks without an ID, like weak passwords or out-of-date (EOL) software.
* **CVSS (Common Vulnerability Scoring System):** The standard 0-10 score. Note: A "10" is bad, but it doesn't mean it’s being hacked *right now*.
* **EPSS (Exploit Prediction Scoring System):** A probability score (0 to 1) that predicts if a bug will be exploited in the next 30 days. High EPSS is often more urgent than a high CVSS.
* **CISA KEV (Known Exploited Vulnerabilities):** The US Govt's "Must-Fix" list. If a bug is on this list, it means hackers are already using it in the wild.
* **SSVC (Stakeholder-Specific Vulnerability Categorization):** A decision tree used to decide action based on how much the asset matters to the business.

**3. Operations: ITAM vs ITSM vs CMDB**
* **ITAM:** Focuses on the asset lifecycle and cost. (Do we own it? Is it old?)
* **ITSM:** Focuses on service and tickets. (Fixing a user's broken laptop.)
* **CMDB:** Shows relationships. (If this Server goes down, which App will break?)


**4. Security Tools**
* **EDR:** The security guard on the laptop (e.g., CrowdStrike).
* **XDR:** The full CCTV system for the whole network.
* **CAASM (ApexaiQ):** The auditor who checks if the EDR is actually installed on every machine.

---

### ApexaiQ Specific Points
* **ApexaiQ Score:** A security credit score (60-180). High is good.
* **Normalize First/Last Seen:** Making sure timestamps from different tools match up.
* **SLA Compliance:** Checking if you are fixing critical bugs within the company's deadline.
* **Multi-tenancy:** One dashboard managing multiple clients separately.
* **RBAC:** Restricting access based on roles (e.g., Interns can't delete logs).
* **MTTR:** Mean Time to Repair—how fast you fix things on average.
* **False Positives:** When a tool wrongly says there is a bug.

### Competitor Landscape
Apart from the ones mentioned before, these are the main players in the CAASM/Asset Management space:
* **Axonius:** Direct competitor in CAASM.
* **Lansweeper:** Strong on network discovery.
* **Balbix:** Focuses on risk and cyber resilience.
* **Armis:** Specialized in IoT and unmanaged devices.
* **Device42:** More focused on data center and cloud inventory.

### Architecture & Traffic
* **North-South vs. East-West Traffic:**
    * **North-South:** Traffic moving between your network and the Internet (entering/leaving).
    * **East-West:** Traffic moving *inside* your data center between servers. This is where hackers hide once they are inside.
* **Micro-segmentation:** Dividing the network into tiny zones so that if one asset is hacked, the hacker can't move to others easily.
* **Data Deduplication:** The "secret sauce" of ApexaiQ. Matching a laptop seen by AWS, CrowdStrike, and Intune into a single "Golden Record."

### Compliance & Business Logic
* **SLO vs. SLA:**
    * **SLA (Service Level Agreement):** The legal promise to a client (e.g., "99.9% uptime").
    * **SLO (Service Level Objective):** The internal goal (e.g., "We aim for 99.99% so we never break our SLA").
* **SOC2 / ISO 27001:** The big compliance audits. ApexaiQ is used to automate the "Inventory" part of these audits, which usually takes months to do manually.
* **API Rate Limiting:** A technical hurdle. When ApexaiQ pulls data from Axonius or AWS, it has to be careful not to ask too fast, or it will be temporarily blocked.

---


### Research Tasks Checklist
- [x] Understand why ApexaiQ is better than just using a CMDB.
- [x] Difference between EDR (Real-time) and CAASM (Auditing).
- [x] How Multi-tenancy works for an MSP managing 50 clients.
- [x] Why False Positives are the biggest enemy of a Security Analyst.
- [x] The impact of Technical Debt on an organization's attack surface.
