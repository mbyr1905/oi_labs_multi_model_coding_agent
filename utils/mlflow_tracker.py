import mlflow

mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("ai_coding_agent") 
mlflow.langchain.autolog()  # Enable autologging for LangChain interactions

def start_run(run_name: str):

    mlflow.set_experiment("ai_coding_agent")

    run = mlflow.start_run(run_name=run_name)

    return run


def log_param(key, value):

    mlflow.log_param(key, value)


def log_metric(key, value):

    mlflow.log_metric(key, value)


def log_text(text, filename):

    mlflow.log_text(text, filename)


def end_run():

    mlflow.end_run()