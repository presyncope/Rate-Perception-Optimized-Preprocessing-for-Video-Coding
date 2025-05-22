# Rate-Perception Optimized Preprocessing for Video Coding

## Training
1. Modify the configuration in **config.py** or `configs/default.yaml`.
2. `python train.py`

## Convert ONNX
1. `python scripts/convert_onnx.py`

## Inference
1. `python inference.py`

## Setting up DVC Remote and Pulling Datasets
This project stores training data with [DVC](https://dvc.org/). Configure a remote and pull the data before training:

```bash
# Add the default remote (replace with your path)
dvc remote add -d origin <dvc-remote-url>

# (Optional) configure credentials
# dvc remote modify origin access_key_id <ACCESS_KEY>
# dvc remote modify origin secret_access_key <SECRET_KEY>

# Download dataset files
dvc pull
```

## Running the Prefect Flow
Training and evaluation can be orchestrated with [Prefect](https://www.prefect.io/):

```bash
# Execute the flow locally
prefect run -p flows/train_flow.py

# Or trigger a deployment registered with Prefect
prefect deployment run train-flow/main
```

Adjust the configuration paths as needed before running the flow.

## Accessing Experiment Results via MLflow
Experiments are tracked with [MLflow](https://mlflow.org/). To browse results:

```bash
# Start the MLflow tracking UI (defaults to http://localhost:5000)
mlflow ui
```

Open the provided URL in your browser to compare runs and download artifacts.
