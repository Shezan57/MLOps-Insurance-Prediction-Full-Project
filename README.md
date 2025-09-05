# 🛡️ Insurance Premium Prediction – End‑to‑End MLOps Project

A production‑ready, cloud‑native Machine Learning system that predicts insurance (vehicle) premiums using a fully automated MLOps lifecycle: from raw data ingestion → validation → transformation → model training → evaluation with drift detection → versioned model registry on S3 → containerized deployment behind a CI/CD pipeline → real‑time prediction API.

> This repository is intentionally engineered to demonstrate architectural maturity, scalability, observability, and DevOps alignment for recruiters & hiring managers.

---

## 🚀 At a Glance

| Capability | Implemented |
|------------|-------------|
| Modular Project Template (auto scaffold) | ✅ |
| Reusable Local Package via `setup.py` / `pyproject.toml` | ✅ |
| Data Source: MongoDB Atlas (Raw → Data Lake) | ✅ |
| Data Ingestion / Validation / Transformation Pipelines | ✅ |
| Feature Engineering + EDA Notebooks | ✅ |
| Custom Logger & Exception Framework | ✅ |
| Model Training (Config‑Driven) | ✅ |
| Model Evaluation (performance drift threshold) | ✅ |
| Model Registry (Amazon S3) | ✅ |
| Model Pusher (promote best model) | ✅ |
| Prediction Service (`app.py`) | ✅ |
| Containerization (Docker + .dockerignore) | ✅ |
| CI/CD (GitHub Actions + Self‑Hosted EC2 Runner) | ✅ |
| Cloud Infra: AWS (IAM, S3, ECR, EC2) | ✅ |
| Secure Secrets via GitHub Actions Secrets | ✅ |

---

## 🧩 Tech Stack & Services

- **Language / Runtime:** Python 3.10  
- **Core Python Packaging:** `setup.py`, `pyproject.toml` (PEP 517/518 compliant)
- **Data Store:** MongoDB Atlas (cloud NoSQL, schema‑flexible ingestion)
- **Cloud Platform:** AWS (S3 for model registry, ECR for images, EC2 for hosting & runner, IAM for security)
- **CI/CD:** GitHub Actions (with self‑hosted EC2 runner for full control & private networking)
- **Containerization:** Docker (multi-stage ready structure potential)
- **Orchestration Style:** Explicit pipeline classes & artifacts (clean separation of concerns)
- **Configuration Management:** Centralized `constants/__init__.py` + typed config entities
- **Model Lifecycle:** Custom evaluation threshold & promotion logic
- **Observability:** Central logging + exception wrapping
- **Serving Layer:** Flask (via `app.py`) – form / API endpoints (port 5080)
- **Artifact Management:** Local `artifact/` directory (git‑ignored) + S3 registry
- **Notebooks:** Exploratory Data Analysis & Feature Engineering
- **Security:** Environment variables for MongoDB & AWS creds (never committed)

---

## 🗺️ High-Level Architecture

```mermaid
flowchart LR
    A[MongoDB Atlas\n(Raw Collection)] --> B[Data Ingestion Component]
    B -->|Raw → DataFrame| C[Data Validation\n(schema + checks)]
    C -->|Valid Data| D[Data Transformation\n(Feature Eng + Encoding + Splits)]
    D --> E[Model Trainer\n(ML Estimators)]
    E --> F[Model Evaluation\n(Compare vs Prod)]
    F -->|If Improved ≥ Threshold| G[Model Pusher]
    G --> H[(S3 Model Registry\nmodel-registry/)]
    H --> I[Prediction Service\n(app.py / Docker)]
    I --> J[User / Client\n(UI / API)]
    F -->|If Not Improved| E
```

---

## 🧱 Project Structure (Representative)

```
MLOps-Insurance-Prediction-Full-Project/
├── app.py
├── setup.py
├── pyproject.toml
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .github/
│   └── workflows/
│       └── aws.yaml
├── constants/
│   └── __init__.py
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │   ├── model_evaluation.py
│   │   └── model_pusher.py
│   ├── configuration/
│   │   ├── mongo_db_connections.py
│   │   └── aws_connection.py
│   ├── data_access/
│   │   └── proj1_data.py
│   ├── entity/
│   │   ├── config_entity.py
│   │   ├── artifact_entity.py
│   │   ├── estimator.py
│   │   └── s3_estimator.py
│   ├── aws_storage/
│   │   └── (S3 push/pull utilities)
│   ├── pipeline/
│   │   └── training_pipeline.py
│   ├── utils/
│   │   └── main_utils.py
│   ├── logger/
│   │   └── __init__.py
│   ├── exception/
│   │   └── __init__.py
│   └── (other helpers…)
├── notebook/
│   ├── mongoDB_demo.ipynb
│   ├── EDA.ipynb
│   └── feature_engineering.ipynb
├── templates/
│   └── (HTML Forms / Result Pages)
├── static/
│   └── (CSS / JS / Assets)
├── config/
│   └── schema.yaml
├── artifact/                # (ignored: intermediate artifacts, models, transforms)
└── README.md
```

> NOTE: Some file names are inferred from described workflow; actual repository may differ slightly.

---

## 🧪 Pipeline Components (Core Responsibilities)

| Component | Purpose | Key Output Artifact |
|-----------|---------|---------------------|
| Data Ingestion | Pull dataset from MongoDB Atlas | Raw / Ingested DataFrames |
| Data Validation | Schema + nulls + type & domain checks | Validation Report |
| Data Transformation | Feature engineering, encoding, scaling, splitting | Transformer object + train/test sets |
| Model Trainer | Train ML models (e.g., regression) | Trained Model + Metrics |
| Model Evaluation | Compare new vs production (threshold: 0.02) | Evaluation Decision |
| Model Pusher | Register improved model to S3 | Versioned Model in Registry |
| Prediction Pipeline | Load best model + transformer | Real-time predictions |

---

## 🧾 Configuration & Constants

Centralized in `constants/__init__.py`:
- `MONGODB_URL` (env provided)
- AWS credentials (via env → injected)
- `MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE = 0.02`
- `MODEL_BUCKET_NAME = "my-model-mlopsproj"`
- `MODEL_PUSHER_S3_KEY = "model-registry"`

---

## 🔐 Environment Variables (Never Commit Secrets)

Example (local shell):

```bash
# Mongo
export MONGODB_URL="mongodb+srv://<username>:<password>@cluster-url/db?retryWrites=true&w=majority"

# AWS
export AWS_ACCESS_KEY_ID="YOUR_KEY"
export AWS_SECRET_ACCESS_KEY="YOUR_SECRET"
export AWS_DEFAULT_REGION="us-east-1"
```

GitHub Repository → Settings → Secrets and Variables → Actions:
```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_DEFAULT_REGION
ECR_REPO   # e.g., <aws_account_id>.dkr.ecr.us-east-1.amazonaws.com/vehicleproj
```

---

## 🗄️ Data Layer

- Source: MongoDB Atlas (flexible ingestion of semi-structured data)
- Ingestion converts BSON/JSON → pandas DataFrame
- Schema constraints enforced via `config/schema.yaml`
- Validation report optionally extended for:
  - Missing ratio thresholds
  - Drift (future extension)
  - Category cardinality anomalies

---

## 🧬 Feature Engineering (Examples)

- Handling numerical vs categorical separation
- Encoding strategies (One‑Hot / Ordinal / Target Encoding potential)
- Scaling: Standard / Robust (configurable)
- Train/Test split persisted with transformer object
- Reproducibility: consistent random seeds

---

## 🤖 Model Lifecycle Strategy

1. Train candidate model with transformed datasets
2. Evaluate against existing production model (if one exists)
3. Promote only if: `new_score - prod_score >= 0.02`
4. Store promoted model & preprocessor in:
   ```
   s3://my-model-mlopsproj/model-registry/<timestamp>/
   ```
5. Prediction service always loads the latest “active” model

---

## 📦 Packaging & Reusability

- `setup.py` + `pyproject.toml` allow `pip install -e .` usage
- Local imports like:
  ```python
  from src.components.data_ingestion import DataIngestion
  ```
- Encourages modular testability and potential PyPI publication.

---

## 🛠️ Local Development – Quick Start

```bash
# 1. Clone
git clone https://github.com/Shezan57/MLOps-Insurance-Prediction-Full-Project.git
cd MLOps-Insurance-Prediction-Full-Project

# 2. Create environment
conda create -n vehicle python=3.10 -y
conda activate vehicle

# 3. Install dependencies
pip install -r requirements.txt

# 4. (Optional) Install package locally
pip install -e .

# 5. Export required environment vars (see section above)

# 6. Run training (example)
python demo.py   # or: python -m src.pipeline.training_pipeline

# 7. Launch app
python app.py
# Access: http://localhost:5080
```

Docker build & run:
```bash
docker build -t insurance-mlops .
docker run -p 5080:5080 --env-file .env insurance-mlops
```

---

## 🚢 CI/CD Workflow Highlights

| Stage | Action |
|-------|--------|
| Push / PR | Triggers GitHub Actions workflow (`aws.yaml`) |
| Build | Docker image built on self-hosted EC2 runner |
| Auth | AWS credentials from GitHub Secrets |
| Publish | Push image → Amazon ECR |
| Deploy | Pull + run updated container on EC2 host (runner) |
| Serve | Flask app exposed on port 5080 (Security Group inbound rule) |

> Self‑Hosted Runner Advantage: Full control, access to private VPC resources, cost transparency, no cold start.

---

## 🗃️ Model Registry (S3 Strategy)

- Bucket: `my-model-mlopsproj`
- Logical layout:
  ```
  model-registry/
    ├── 2024_12_01_15_30/
    │    ├── model.pkl
    │    └── transformer.pkl
    └── latest/  (optional symlink or pointer pattern)
  ```
- Future Enhancements: add metadata JSON (metrics, hashes, lineage)

---

## 🧾 Logging & Exception Handling

- Unified logging module (timestamped, severity levels)
- Exceptions wrapped in custom class for enriched debug context
- Extendable to log aggregation tools (CloudWatch / ELK) later

---

## 🌐 Prediction API

Typical flow (example pseudo):
```python
from src.pipeline.prediction_pipeline import PredictionPipeline

pipeline = PredictionPipeline()
prediction = pipeline.predict(input_dict)
```

Web Interface (form submission) → preprocess → predict → render result.

Training endpoint:
```
/training
```
Triggers full pipeline (for controlled retraining in controlled environments).

---

## 📊 EDA & Notebooks

Located under `notebook/`:
- `mongoDB_demo.ipynb`: Data pull test from Atlas
- `EDA.ipynb`: Profiling, correlation, distributions
- `feature_engineering.ipynb`: Transformation prototyping

> Recommendation: Export finalized transformation logic into production transformer classes.

---

## 🧪 Testing (Suggested Future Addition)

Recommended structure (planned roadmap):
```
tests/
  ├── test_data_validation.py
  ├── test_transformation.py
  ├── test_model_training.py
  └── conftest.py
```
Potential frameworks: `pytest`, `great_expectations`, `pydantic` for schema.

---

## 🧭 Key Differentiators for Recruiters

- Demonstrates end-to-end ML system thinking (not just a model script)
- Cloud-native with production deployment readiness
- Clean separation between configuration, entities, components, and pipelines
- Environment & secret hygiene (no credentials in code)
- Extensible architecture (plug new models, validation rules, or storage backends)
- CI/CD integration with real infrastructure (ECR + EC2 runner)
- Emphasis on model governance (evaluation threshold + registry)

---

## 📌 Roadmap / Potential Enhancements

| Priority | Enhancement |
|----------|-------------|
| ⭐ | Add automated unit & integration tests |
| ⭐ | Introduce model performance monitoring & drift dashboards |
| ⭐ | Add experiment tracking (MLflow / Weights & Biases) |
| ⭐ | Add data quality store (Great Expectations) |
| ⭐ | Implement async batch scoring job |
| ⭐ | Add feature store integration |
| ⭐ | Blue/Green or Shadow Deployment for new models |
| ⭐ | Add lineage metadata (model card JSON) |
| ⭐ | Terraform infrastructure as code (S3, ECR, IAM, EC2) |
| ⭐ | Canary rollout with health probes |
| ⭐ | Container security scanning (Trivy / Grype) |

---

## ❓ FAQ

| Question | Answer |
|----------|--------|
| Where do I change schema rules? | `config/schema.yaml` |
| How is a new model accepted? | Must exceed previous score by >= `MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE` |
| Where are artifacts stored? | Local `artifact/` (ignored) + S3 for final promoted models |
| How do I retrain? | Hit `/training` route or execute pipeline module |
| Which port is exposed? | 5080 (configure via security group + app code) |

---

## 🧑‍💼 Author / Contact

**Developer:** @Shezan57  
**GitHub:** [MLOps-Insurance-Prediction-Full-Project](https://github.com/Shezan57/MLOps-Insurance-Prediction-Full-Project)  
Feel free to open issues, suggest enhancements, or reach out for collaboration.

---

## 🔐 Disclaimer

This project is educational & demonstrative. Replace placeholder credentials, secure secrets via vaulting if used in production, and review IAM policies for least privilege before real-world deployment.

---

## ⭐ Support

If you find this architecture valuable:
- Star the repository
- Share with peers
- Fork and extend with your own experiments

> “A strong MLOps foundation multiplies the value of every model you build.”

---

### ✅ Ready to Explore

Clone → Configure env → Run training → Launch app → Predict → Inspect S3 model versions.  
Let this repository speak to your ability to ship production-grade ML systems.

Happy Building! 🚀
