import uuid
import mlflow
import os
from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END
from graph.state import AgentState
from agents.requirement_agent import requirement_agent
from utils.logger import logger
from utils.mlflow_tracker import start_run, end_run


def load_prd():
    with open("inputs/PRD.txt", "r", encoding="utf-8") as f:
        return f.read()


def build_graph():

    builder = StateGraph(AgentState)
    builder.add_node("requirement_agent", requirement_agent)
    builder.add_edge(START, "requirement_agent")
    builder.add_edge("requirement_agent", END)
    graph = builder.compile()
    return graph


def main():
    try:
        run = start_run("AI_Coding_Pipeline_Run")
        
        logger.info("Starting AI coding pipeline")
        prd_text = load_prd()
        state = {
            "prd_text": prd_text,
            "figma_image_path": "inputs/figma.png",
            "system_spec": None,
            "pages": None,
            "components": None
        }
        graph = build_graph()
        logger.info("Invoking LangGraph workflow")
        config = {"configurable": {"thread_id": "1"}}
        result = graph.invoke(state, config=config)
        logger.info("LangGraph workflow completed")
        end_run()
    except Exception as e:
        logger.error(f"Error in main: {e}")
        raise e

if __name__ == "__main__":
    main()