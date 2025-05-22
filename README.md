# Rate-Perception Optimized Preprocessing for Video Coding

###  Training
1. modify the configuration in **config.py**
2. `python train.py`
   - Metrics and checkpoints are logged to MLflow. Set `MLFLOW_TRACKING_URI` if you want to use a remote server.
### Convert ONNX
1. `python scripts/convert_onnx.py`

### Inference
1. `python inference.py`

### Prefect pipeline
1. `python -m mlops.pipeline`
