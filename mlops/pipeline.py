import subprocess
from prefect import task, Flow

@task
def load_data():
    """Fetch dataset tracked by DVC."""
    subprocess.run(["dvc", "pull"], check=True)

@task
def train_model():
    """Run the training script."""
    subprocess.run(["python", "train.py"], check=True)

@task
def evaluate_model():
    """Evaluate the trained model using the inference script."""
    subprocess.run(["python", "inference.py"], check=True)

@task
def register_model():
    """Placeholder for model registration step."""
    pass

with Flow("training-flow") as flow:
    data = load_data()
    model = train_model(upstream_tasks=[data])
    metrics = evaluate_model(upstream_tasks=[model])
    register_model(upstream_tasks=[metrics])


def main():
    flow.run()

if __name__ == "__main__":
    main()
