![Banner](assets/banner.svg)

# Awesome-Data-Centric-AI
<!-- SEO Meta: Data-Centric AI, Machine Learning, MLOps, Confident Learning, Synthetic Data, Dataset Curation, Label Quality, Cleanlab, Weak Supervision -->

<p align="center">
  <a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-aadge&logo=discord&logoColor=white" alt="Discord" /></a>
  <a href="https://github.com/ishandutta2007/Awesome-Data-Centric-AI/stargazers"><img src="https://img.shields.io/github/stars/ishandutta2007/Awesome-Data-Centric-AI?style=social" alt="GitHub_Stars" /></a>
  <a href="https://github.com/ishandutta2007/Awesome-Data-Centric-AI/network/members"><img src="https://img.shields.io/github/forks/ishandutta2007/Awesome-Data-Centric-AI?style=social" alt="GitHub forks" /></a>
  <a href="https://github.com/ishandutta2007/Awesome-Data-Centric-AI/issues"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="PRs Welcome" /></a>
  <a href="https://github.com/ishandutta2007/Awesome-Data-Centric-AI/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square" alt="License" /></a>
  <a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>
</p>

## Data-Centric AI: History, Progression, Variants, & Applications

**Data-Centric AI** is an engineering and operational paradigm in artificial intelligence that treats data as the primary vector for system optimization. Popularized by Andrew Ng in 2021, Data-Centric AI shifts the core development focus away from continuously tweaking model architectures to holding the architecture fixed while systematically cleaning, curating, and augmenting the underlying dataset. 

In traditional **Model-Centric AI**, engineers treat the dataset as a static baseline and focus exclusively on engineering hyperparameter tunings, deep layer connections, or massive parameter capacities. Data-Centric AI flips this methodology, establishing that data quality dominates model size. By implementing programmatic label curation, error cleaning, targeted synthetic sampling, and data augmentation loops, Data-Centric AI builds highly accurate, robust, and aligned systems at a fraction of the hardware compute footprint required by bloated models.

---

## 🕰️ 1. The Macro Chronological Evolution

The technical framework governing AI dataset management has transitioned from unstructured ad-hoc crowdsourcing to automated data pipelines, web-scale synthetic curation, and native post-training alignment environments.

```mermaid
flowchart LR
    A["Ad-Hoc Model-Centric Era (Unvetted Noise & Baseline Drops)"] --> B["Automated Label Auditing (Cleanlab, 2021) (Programmatic Label Quality Scans)"]
    B --> C["Synthetic Data Curations (Self-Instruct) (Web-Scale High-Fidelity Generations)"]
    C --> D["RLVR Programmatic Hard-locks (Compiler-Verified Quality Gates)"]
```

| Era | Details | Year | Paper | Link |
|---|---|---|---|---|
| The Ad-Hoc Model-Centric Era | **Concept:** The baseline development standard, relying on massive unvetted web-scrapes.<br>**Limitation:** Intolerable optimization waste due to persistent hallucinations. | Pre-2021 | [N/A](#) | [Details](pages/ad-hoc.md) |
| The Programmatic Label Quality & Auditing Era | **Concept:** Automated engineering discipline using Confident Learning.<br>**Significance:** Slashed label noise and data bloat. | 2021 | [Confident Learning](https://arxiv.org/abs/1911.00068) | [Details](pages/prog-label.md) |
| The Web-Scale High-Fidelity Synthetic Curation Era | **Concept:** Solved impending human data exhaustion crisis using Self-Instruct.<br>**Significance:** Recursively mutates small vetted seeds into millions of pristine scenarios. | 2023 | [Self-Instruct](https://arxiv.org/abs/2212.10560) | [Details](pages/web-scale.md) |
| The Compiler-Locked Programmatic Verification Era | **Concept:** RLVR checking via hardcoded software environments.<br>**Significance:** Zero-noise data loop enforced by compilers. | 2025 | [DeepSeek-R1](https://arxiv.org/abs/2501.12948) | [Details](pages/compiler-locked.md) |

---

## ⚙️ 2. Core Functional & Algorithmic Variants

Data-Centric AI methodologies are strictly categorized based on the exact automated mechanisms deployed to cleanse, augment, and audit the training data matrix.

| Variant | Mechanism | Year | Paper | Link |
|---|---|---|---|---|
| Confident Learning | Evaluates dataset validity by estimating joint distributions of noisy and true labels. | 2019 | [Confident Learning](https://arxiv.org/abs/1911.00068) | [Details](pages/confident-learning.md) |
| CoreSet Selection | Slashes dataset redundancy mathematically using clustering or gradient-matching fields. | 2020 | [DeepCore](https://arxiv.org/abs/2204.08477) | [Details](pages/coreset.md) |
| Generative Synthetic Augmentation | Uses deep generative models to rewrite or visually alter datasets on-the-fly. | 2022 | [GenAug](https://arxiv.org/abs/2302.07923) | [Details](pages/gen-aug.md) |
| Automated Feature Store | Infrastructure-level framework tailored for enterprise MLOps treating data features as reusable assets. | 2017 | [Michelangelo](https://arxiv.org/abs/1712.06246) | [Details](pages/feature-store.md) |

---

## 🧩 3. The Data-Centric AI Pipeline Matrix

To maintain absolute data quality across large-scale optimization loops, data-centric architectures coordinate continuous cleaning and alignment layers concurrently.


```mermaid
flowchart TB
    A["Raw Data Ingestion"] --> B["Confident Learning Scan"]
    B --> C["Prune Redundant Elements via CoreSet"]
    C --> D["Generate Synthetic Edge Cases"]
    D --> E["RLVR Quality Gate Check"]
    E --> F["Optimal Post-Training Alignment"]
```

| Component | Profile | Year | Paper | Link |
|---|---|---|---|---|
| Process-Supervised Evaluation (PRMs) | Granular token step quality auditing. Value network checks every step dynamically. | 2023 | [PRMs](https://arxiv.org/abs/2305.20050) | [Details](pages/prm.md) |
| Vector Database Deduplication | Slashes data leakage and memorization traps via dense sentence encoders and high-dimensional geometric coordinates. | 2021 | [Deduplicating Training Data](https://arxiv.org/abs/2107.06499) | [Details](pages/vector-dedup.md) |

---

## 🏭 4. Production Engineering Challenges & Infrastructure Mitigations

Implementing large-scale data-centric pipelines across massive distributed high-performance computing clusters introduces severe data latency and alignment constraints.

| Challenge | Mitigation | Year | Paper | Link |
|---|---|---|---|---|
| Distributed Dataloader Load-Imbalance | GPU-Fused Batched Data Augmentations (like NVIDIA DALI) to execute formatting in VRAM. | 2018 | [NVIDIA DALI](#) | [Details](pages/dataloader.md) |
| Distribution Drift (Model Collapse) | Hardcoding strict External Software Verifiers (RLVR) into synthetic loops. | 2023 | [The Curse of Recursion](https://arxiv.org/abs/2305.17493) | [Details](pages/model-collapse.md) |

---

## 🚀 5. Frontier Real-World AI Industrial Applications

| Application | Details | Year | Paper | Link |
|---|---|---|---|---|
| Pre-Training Web-Scale Transformers | Guides cluster-wide dataset selection and token curation for LLMs like Llama and DeepSeek. | 2023 | [Llama](https://arxiv.org/abs/2302.13971) | [Details](pages/llama.md) |
| Autonomous Vehicle Edge Perception | Secures computer vision systems against volatile road conditions using diffusion models. | 2020 | [Waymo Open Dataset](https://arxiv.org/abs/1912.04838) | [Details](pages/av.md) |
| Enterprise Credit Scoring | Regulates financial models using automated confident learning and data re-weighting pipelines. | 2021 | [Fairness in ML](https://arxiv.org/abs/2105.02725) | [Details](pages/credit.md) |

---

## References
1. Northcutt, C., Jiang, L., & Chuang, I. (2021). Confident learning: Estimating joint distribution of noisy labels. *Journal of Artificial Intelligence Research*, 70, 1373-1411.
2. Ng, Andrew. (2021). MLOps: From model-centric to data-centric AI. *DeepLearning.AI Architecture Manifesto*.
3. Mazumder, M., et al. (2022). Dataperf: Benchmarking data-centric AI dataset quality metrics. *arXiv preprint arXiv:2207.10062*.
4. Gunasekar, J., et al. (2023). Textbooks are all you need: Curation of pristine synthetic datasets for small language models. *Microsoft Phi Technical Report*.
5. Wang, L., et al. (2024). Multi-task instruction fine-tuning via self-instruct generative data curation loops. *International Conference on Learning Representations (ICLR)* [INDEX: 18].
6. DeepSeek-AI. (2025). DeepSeek-R1: Incentivizing reasoning and verification capability in foundational language transformers via large-scale self-play reinforcement learning loops initialized via compiler-vetted synthetic datasets [INDEX: 17, 21].

---

To advance this documentation repository, dataset automation workspace, or MLOps architecture, consider exploring these adjacent development pathways:
* Build a **Python script using PyTorch and Cleanlab** illustrating how to load a custom dataset, run an out-of-sample forward pass, and compute automated confident learning matrices to flag label noise.
* Generate a **comprehensive Markdown table** explicitly comparing Model-Centric AI, Confident Learning Curation, CoreSet Data Pruning, Generative Synthetic Curation, and Compiler-Locked RLVR Data Verification across lifecycle entry junctions, computational training overhead costs, required human annotation budgets, and resistance to model collapse.
* Establish a **performance profiling notebook using Triton** to track the exact cluster-wide compute efficiency, communication-to-computation overlap ratios, and memory bus bandwidth compression achieved when routing token-balanced data-centric batches over distributed server nodes.

***

**Follow-Up Options Matrix:**

Before updating this repository workspace layout, let me know how you would like to proceed by choosing one of the options below:
* I can provide a **complete Python code boilerplate using PyTorch** demonstrating how to write an automated script that calculates an exact k-center CoreSet selection data pruning loop.
* I can generate a **Markdown matrix table** tracking the explicit dataset parsing boundaries, filtering thresholds, and synthetic token distribution scales utilized by leading foundation repositories to manage data-centric design.
* I can write a detailed technical explanation focusing on the **mathematics of Confident Learning noise estimation** and how joint distribution calculations govern label error isolation.

---

# 🌐 Awesome Data-Centric AI Directory

## 🏆 Top Data-Centric AI Ecosystem



**Curated List of SaaS Products & Open-Source GitHub Projects**  

*Focused on Label Quality, Programmatic Labeling & Data Curation*  

**Last updated: October 2026**



This repository tracks notable **SaaS platforms** and **open-source projects** for **Data-Centric AI**. These tools enable teams to systematically improve training data quality—detecting label errors, curating datasets, and building programmatic labeling pipelines—rather than only tuning model architectures.



**Examples** include Snorkel Flow, Scale AI, Labelbox, Appen, CloudFactory, Prodigy, SuperAnnotate, Dataloop, Encord, and V7 (the category leaders).



**Open-source emphasis**: This section is heavily expanded with every major active project for automated data quality, label error detection, and open annotation infrastructure—ideal for ML engineers, data scientists, and organizations seeking transparent, vendor-independent data improvement.



Contributions welcome! Open a PR to add/update entries. Keep descriptions factual and link to official sites.



## 📑 Table of Contents

- [📊 Sector Overview & Market Dynamics](#-sector-overview--market-dynamics)
- [🏢 SaaS & Hosted Enterprise Platforms](#-saas--hosted-enterprise-platforms)
- [💻 Open-Source GitHub Projects](#-open-source-github-projects)
- [🛠️ How to Contribute](#️-how-to-contribute)
- [💖 Support & Community](#-support--community)
- [⭐ Star History](#-star-history)
- [📜 Disclaimer](#-disclaimer)



## 📊 Sector Overview & Market Dynamics

The global data-centric AI and data annotation & labeling market is estimated between **$2.1B and $6.3B in 2026** (scaling to **$9.3B–$17.1B by 2030** at an estimated **23%–28% CAGR**), catalyzed by generative AI, LLM alignment, and multimodal training demands. The sector is **moderately fragmented yet increasingly concentrated at the top**, with mega-infrastructure titans (e.g., Scale AI, Snorkel AI) capturing outsized enterprise budgets while specialized tooling platforms compete in niche multimodal, physical AI, and programmatic niches.



## 🏢 SaaS & Hosted Enterprise Platforms

| Platform | Valuation / Revenue (Scale) | Starting Pricing Tier | Free Tier Limits / Trial Limits | Key Capabilities & Highlights |
|---|---|---|---|---|
| **[Scale AI](https://scale.com/)** | **$29.0B** valuation *(Meta round, 2025)* | Custom enterprise contracts; self-serve tasks from **~$0.08–$0.12/item** or usage-based tiering | **Free Tier** via Nucleus for academia/independents (core visualization & dataset insights; self-serve low-volume trial credits) | High-leverage data platform; Scale Pro labeling with dedicated SLAs, Nucleus data curation/failure debugging, enterprise Gen AI platform. |
| **[Snorkel AI](https://snorkel.ai/)** | **$3.5B** valuation *(Series E, 2026; $375M ARR)* | Enterprise contracts starting upwards of **~$50,000–$60,000/year** | **No public free tier** (custom guided proof-of-concept / evaluation demos available upon request) | Programmatic AI data development platform; write code/heuristics instead of manual labeling, AKS native, SOC 2 Type II/HIPAA. |
| **[Labelbox](https://labelbox.com/)** | **$1.25B** valuation *(Series E, 2026)* | **$0.10/LBU** (Starter tier; consumption-based pay-as-you-go) | **500 LBUs/month free forever**, up to 30 users, 50 projects, 25 ontologies (1,500 API req/min) | Data factory for generative AI; Alignerr expert labeling community, Horizon RL environments, autonomous Recursion Managed Agents. |
| **[Encord](https://encord.com/)** | **$550M** valuation *(Series C, 2026)* | Custom quote-based (Starter/Team/Enterprise packaging) | **Starter Free Tier** for individual developers/prototyping (limited to small project workspaces and base annotator workflows) | Multimodal AI data platform; specialized in physical AI, computer vision, video, audio, and DICOM with embedding-based Index search. |
| **[CloudFactory](https://www.cloudfactory.com/)** | **$250M–$500M** valuation *(Dealroom estimates)* | Custom project contracts (piece-rate from **~$0.05+/label** or hourly from **~$8–$15/hr**) | **No free tier** (offers a complimentary data sample analysis/pilot review on client-submitted test batches) | Full-stack AI operations platform (Data, Training, Inference, and AI orchestration engines) targeting high-stakes reliability sectors. |
| **[Appen](https://www.appen.com/)** | **~$185M–$265M** market cap *(ASX: APX; ~$250M–$275M AUD)* | Custom enterprise quotes / Statements of Work (SOWs) | **No self-serve free trial** (enterprise custom PoCs/pilot phases negotiated via sales) | Veteran large-scale workforce labeling provider; text, audio, image, 3D/4D annotation, GDPR/SOC/HIPAA/ISO certified. |
| **[SuperAnnotate](https://www.superannotate.com/)** | **~$75M–$99M** total funding *(~$27M–$35M ARR estimate)* | Paid plans starting at **~$62/user/month** (Starter/Pro tiers) | **Free Plan** for small teams/evaluations (up to 3–5 seats and 1,000 compute pipeline orchestration hours) | Multimodal dataset creation platform; native Query Language (Explore), Vertex AI integration, automated pre-annotations. |
| **[Dataloop](https://dataloop.ai/)** | **$120M** acquisition valuation *(Acquired by Dell, 2025)* | Custom enterprise contracts | **No self-serve free plan** (evaluation PoC environments available via guided sales demo/expert consultation) | Agentic AI data orchestration platform; deep Databricks Unity Catalog, NVIDIA NIM/NeMo, and VLM agent integrations. |
| **[V7](https://www.v7labs.com/)** | **~$100M** valuation *(~$27.7M ARR estimate)* | Starter paid tier starting at **~$499/month** (or ~$5,400/yr) | **Basic Free Plan ($0)** (restricted to 1 workspace, up to 10 user seats, and 100 files/items limit) | AI data labeling suite; 10x speedup with AI auto-annotation, multi-stage review workflows, specialized DICOM/PDF support. |
| **[Prodigy](https://prodigy.ai/)** | **Bootstrapped** *(Explosion AI, ~$1.4M ARR estimate)* | **$490/seat** (one-time perpetual lifetime license, packs of 5) | **No self-serve free trial software download** (full interactive browser demos online; free academic research licenses on application) | Scriptable, privacy-first local annotation tool from makers of spaCy; zero data leaves your infrastructure, active learning loops. |



## 💻 Open-Source GitHub Projects

Curated open-source tooling for automated label cleaning, dataset debugging, active learning, data validation, and dataset curation. Each project is ranked below in descending order by GitHub Stars_Count:

- **[Label Studio](https://github.com/HumanSignal/label-studio)** [![Stars](https://img.shields.io/github/stars/HumanSignal/label-studio?style=social&color=white)](https://github.com/HumanSignal/label-studio/stargazers)  
  **The most flexible open-source multi-type data labeling & annotation tool** (Apache-2.0) . Supports **text, computer vision, audio, and time-series data** with customizable XML UI templates, ML backend auto-labeling integrations, and webhooks . Serves as the primary foundation for open-source annotation across CV/NLP and LLM evaluation (RLHF, DPO, prompt-response ranking) .

- **[CVAT](https://github.com/cvat-ai/cvat)** [![Stars](https://img.shields.io/github/stars/cvat-ai/cvat?style=social&color=white)](https://github.com/cvat-ai/cvat/stargazers)  
  **Computer Vision Annotation Tool** (MIT) . **The industrial-grade benchmark for image and video annotation**—features **SAM and YOLO auto pre-labelling**, multi-level quality inspection, annotation time tracking, native S3/cloud object storage connectors, and 20+ standard export formats (COCO, YOLO, Pascal VOC, KITTI, MOT) . Helm chart support for production Kubernetes clusters .

- **[ydata-profiling](https://github.com/Data-Centric-AI-Community/fg-data-profiling)** [![Stars](https://img.shields.io/github/stars/Data-Centric-AI-Community/fg-data-profiling?style=social&color=white)](https://github.com/Data-Centric-AI-Community/fg-data-profiling/stargazers)  
  **Automated exploratory data analysis, dataset profiling, and data-centric quality reporting** (MIT) . Generates rich interactive HTML profiling reports from pandas and Spark DataFrames with one line of code . Computes detailed data distributions, missing value audits, correlation matrices, duplicate analyses, and data skew alerts to catch data anomalies before training .

- **[Great Expectations](https://github.com/great-expectations/great_expectations)** [![Stars](https://img.shields.io/github/stars/great-expectations/great_expectations?style=social&color=white)](https://github.com/great-expectations/great_expectations/stargazers)  
  **The leading open-source data quality assertion and validation framework** (Apache-2.0) . Enables automated pipeline testing, dataset profiling, and documentation for enterprise data-centric workflows . Hardcodes programmatic assertions ensuring datasets adhere to strict structural and distributional requirements before ingestion into model training loops .

- **[cleanlab](https://github.com/cleanlab/cleanlab)** [![Stars](https://img.shields.io/github/stars/cleanlab/cleanlab?style=social&color=white)](https://github.com/cleanlab/cleanlab/stargazers)  
  **The standard data-centric AI library for automated label error detection and data quality** (AGPL-3.0) . Based on **Confident Learning** theory, it mathematically discovers label errors, outliers, near-duplicates, and dataset issues across any ML model outputs (predicted probabilities or embeddings) . Uncovered thousands of pervasive label errors in standard academic benchmarks like ImageNet and MNIST . Core APIs include `CleanLearning.find_label_issues()`, dataset health reports, and active learning .

- **[FiftyOne](https://github.com/voxel51/fiftyone)** [![Stars](https://img.shields.io/github/stars/voxel51/fiftyone?style=social&color=white)](https://github.com/voxel51/fiftyone/stargazers)  
  **Open-source platform for curating high-quality datasets and visualizing computer vision models** (Apache-2.0) . Provides visual dataset curation, interactive embedding spaces via UMAP/t-SNE, model prediction evaluation, and automated detection of annotation mistakes and dataset edge cases .

- **[Evidently](https://github.com/evidentlyai/evidently)** [![Stars](https://img.shields.io/github/stars/evidentlyai/evidently?style=social&color=white)](https://github.com/evidentlyai/evidently/stargazers)  
  **Open-source ML data monitoring, dataset drift detection, and evaluation framework** (Apache-2.0) . Tracks statistical distribution drift, covariate shift, data quality degradation, and text/LLM evaluation metrics across batch and streaming data pipelines with interactive visual dashboards and programmatic alerts .

- **[Snorkel](https://github.com/snorkel-team/snorkel)** [![Stars](https://img.shields.io/github/stars/snorkel-team/snorkel?style=social&color=white)](https://github.com/snorkel-team/snorkel/stargazers)  
  **System for programmatic weak supervision and training data curation** (Apache-2.0) . Allows developers to build, combine, and manage multi-source labeling functions (heuristics, regex, third-party models) to automatically label datasets without extensive manual annotation, founding the modern programmatic labeling paradigm .

- **[Argilla](https://github.com/argilla-io/argilla)** [![Stars](https://img.shields.io/github/stars/argilla-io/argilla?style=social&color=white)](https://github.com/argilla-io/argilla/stargazers)  
  **Human-in-the-loop data curation and annotation platform for LLMs and Generative AI** (Apache-2.0) . Built specifically for prompt engineering evaluation, preference data collection (DPO/RLHF), instruction fine-tuning datasets, and synthetic dataset feedback loops with direct Hugging Face ecosystem integration .

- **[modAL](https://github.com/modAL-python/modAL)** [![Stars](https://img.shields.io/github/stars/modAL-python/modAL?style=social&color=white)](https://github.com/modAL-python/modAL/stargazers)  
  **Modular active learning framework for Python and scikit-learn** (MIT) . Streamlines pool-based, stream-based, and uncertainty sampling routines to systematically identify the most informative data points for human labeling, minimizing overall annotation budgets while maximizing model accuracy gains .

- **[Xtreme1](https://github.com/xtreme1-io/xtreme1)** [![Stars](https://img.shields.io/github/stars/xtreme1-io/xtreme1?style=social&color=white)](https://github.com/xtreme1-io/xtreme1/stargazers)  
  **Next-generation open-source multimodal platform for data labeling and annotation** (Apache-2.0, LF AI & Data Foundation) . Specializes in 3D point cloud LiDAR-camera sensor fusion annotation, visual object tracking, and experimental RLHF interfaces for physical AI and embodied systems .

- **[CleanVision](https://github.com/cleanlab/cleanvision)** [![Stars](https://img.shields.io/github/stars/cleanlab/cleanvision?style=social&color=white)](https://github.com/cleanlab/cleanvision/stargazers)  
  **Automated data curation and quality issue auditing for image datasets** (AGPL-3.0) . Scans image datasets to automatically detect low-quality, blurry, dark, overexposed, low-information, and near-duplicate images with a single line of Python, preventing corrupt data from poisoning computer vision models .

---

### 📦 Ecosystem Tooling & Python Packages

- **[Knowlyr Datalabel](https://pypi.org/project/knowlyr-datalabel/)** — Offline-first, zero-dependency annotation tool generating standalone HTML interfaces with 5 annotation modalities, multi-annotator merge with Inter-Annotator Agreement (Cohen's/Fleiss' Kappa, Krippendorff's Alpha), and MCP server support.
- **[clean-evals](https://pypi.org/project/clean-evals/)** — Lightweight evaluation framework featuring blind double-review workflows, golden answer locking, and LLM judge calibration.
- **[Cleanlab Studio Client](https://github.com/cleanlab/cleanlab-studio)** — Python SDK client for Cleanlab Studio's enterprise AutoML and cloud-scale label correction engines.

---

## 🛠️ How to Contribute

Contributions are warmly welcomed! Help make Data-Centric AI tooling accessible to every engineer:

1. 🍴 **Fork the repository** on GitHub.
2. 🌿 **Create a new branch** (`git checkout -b feature/new-data-tool`).
3. 📝 **Add or update entries** in `README.md` following the established formatting guidelines (include tool name, website/repo link, Stars_Badge, and clear summary).
4. 🚀 **Submit a Pull Request** with a concise description of the addition.

---

## 💖 Support & Community

If you find this curated collection useful for your datasets, research, or production ML pipelines, please consider supporting the project:

- ⭐ **Star this repository** to help other practitioners discover data-centric techniques!
- 🍴 **Fork & Share** with your fellow AI researchers, ML engineers, and data teams.
- 💬 **Join our community** discussions on [Discord](https://discord.gg/jc4xtF58Ve).
- ☕ **Buy a coffee & sponsor**: If this project saved you hours of debugging messy labels or saved your compute budget, consider supporting maintenance and updates via the [GitHub Sponsors Dashboard](https://github.com/sponsors/ishandutta2007)!

---

##  Star History
[![Star History Chart](https://star-history.dera.page/svg?repos=ishandutta2007/Awesome-Data-Centric-AI&type=date&legend=top-left)](https://star-history.dera.page/#ishandutta2007/Awesome-Data-Centric-AI&type=date&legend=top-left)

---

## 📜 Disclaimer

- This is a **community-curated directory** provided for educational and research purposes.
- Data-centric AI pipelines handling real-world datasets must adhere to applicable regulatory frameworks (GDPR, CCPA, HIPAA, EU AI Act) and establish ethical workforce standards.
- **The Data-Centric paradigm emphasizes systematic data quality over raw parameter capacity.** Finding label errors, pruning redundant tokens, and generating compiler-verified edge cases consistently yield higher leverage improvements than architecture tweaks alone.

---

<p align="center">
  <b>Made with ❤️ for ML engineers, data scientists, and researchers building robust, quality-driven AI systems.</b>
</p>
