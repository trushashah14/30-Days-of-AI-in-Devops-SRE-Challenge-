# Day 21: Generated Kubernetes Manifests 🚀 – Aug 28, 2025

## Challenge Description 🎯
Automatically generate production-ready Kubernetes Deployment and Service YAML using an LLM (Ollama, Llama3, GPT-3.5, etc.) from a simple service description.

## Objective 🚀
- Define service requirements (name, image, ports, replicas, environment variables)
- Use LLM to generate valid Kubernetes manifests
- Save and validate the YAML for direct application to clusters

## Code & Implementation 💻
- **Notebook**: [`k8s_manifest_generator.ipynb`](./k8s_manifest_generator.ipynb)  
  Main workflow for service description, prompt construction, LLM call, YAML extraction, and validation.
- **Step-by-Step Solution**: [`Step-by-Step-Solution.md`](./Step-by-Step-Solution.md)  
  Detailed explanation of each notebook step, including rationale and insights.
- **Output**:  
  - `deployment_and_service.yaml` – ready-to-apply Kubernetes manifests

## Workflow 🔄

1. **Define Service:**  
   Specify service name, image, replicas, ports, and environment variables.
2. **Prompt LLM:**  
   Construct a prompt for the LLM to generate Deployment and Service YAML.
3. **Generate YAML:**  
   Call Ollama API and extract only the YAML code from the response.
4. **Save & Validate:**  
   Write YAML to file and validate syntax before applying to Kubernetes.

## Why Each Step Was Chosen 📊
- **Service Description:**  
  Ensures all required fields are captured for manifest generation.
- **LLM Prompting:**  
  Automates YAML creation, reducing manual errors and saving time.
- **YAML Extraction & Validation:**  
  Guarantees only valid YAML is saved, avoiding deployment failures.

## Interpretation of Results 🧠
- **deployment_and_service.yaml:**  
  Contains a valid Deployment and Service manifest for the described application.
- **Validation Output:**  
  Confirms YAML is syntactically correct and ready for use.

## What Did I Learn 🧩
- LLMs can automate infrastructure as code tasks, reducing manual effort.
- Careful prompt engineering and output parsing are essential for reliable results.
- Automated validation prevents configuration errors in production.

## How to Use in Real-World DevOps/SRE 🌍

### Rapid Kubernetes Onboarding
**Use Case:**  
Quickly generate manifests for new services or microservices.

**Implementation:**  
- Fill out a service description form
- Use notebook or script to generate and validate YAML
- Apply directly to Kubernetes clusters

**Industry Examples:**  
- SaaS teams onboarding new features
- Platform teams standardizing deployments

## Where Was AI Used? 🤖

**AI Used:**  
- Local LLM (Ollama, e.g. Llama3) was used to generate Kubernetes manifests from  structured service descriptions.

**AI Technologies Used:**  
- Llama3 (LLM, via Ollama)
- Python (prompt orchestration, YAML extraction, validation)

## References 📖
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Ollama Documentation](https://ollama.com/docs)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [YAML Syntax Reference](https://yaml.org/spec/1.2/spec.html)

## Future Enhancements 🚀
- Add support for StatefulSets, Ingress, ConfigMaps, and Secrets
- Integrate with GitOps workflows for automated deployment
- Validate manifests against custom policies (OPA/Gatekeeper)
- Extend to multi-cluster and multi-cloud environments
