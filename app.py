import uuid
import mlflow
import os
from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END
from graph.state import AgentState
from utils.logger import logger
from utils.mlflow_tracker import start_run, end_success_run, fail_run, log_error
from agents.requirement_agent import requirement_agent
from agents.architecture_agent import architecture_agent
from agents.task_agent import task_agent
from agents.backend_code_agent import backend_code_agent
from agents.file_writer_agent import file_writer_agent
from agents.frontend_code_agent import frontend_code_agent 
from agents.integration_agent import integration_agent
from agents.debug_agent import debug_agent
from agents.evaluation_agent import evaluation_agent
from agents.execution_agent import execution_agent

def evaluation_router(state):
    decision = state["evaluation"]["decision"]
    retry_count = state.get("retry_count", 0)
    if decision == "good":
        return "end"
    if retry_count >= 2:
        return "end"
    return "retry"

def load_prd():
    with open("inputs/PRD.txt", "r", encoding="utf-8") as f:
        return f.read()

def build_graph():

    builder = StateGraph(AgentState)
    builder.add_node("requirement_agent", requirement_agent)
    builder.add_node("architecture_agent", architecture_agent)
    builder.add_node("task_agent", task_agent)
    builder.add_node("backend_code_agent", backend_code_agent)
    builder.add_node("backend_code_writer_agent", file_writer_agent)
    builder.add_node("frontend_code_agent", frontend_code_agent)
    builder.add_node("frontend_code_writer_agent", file_writer_agent)
    builder.add_node("integration_agent", integration_agent)
    builder.add_node("integration_code_writer", file_writer_agent)
    builder.add_node("debug_agent", debug_agent)
    builder.add_node("debug_code_writer", file_writer_agent)
    builder.add_node("execution_agent", execution_agent)
    builder.add_node("evaluation_agent", evaluation_agent)
    
    builder.add_edge(START, "requirement_agent")
    builder.add_edge("requirement_agent", "architecture_agent")
    builder.add_edge("architecture_agent", "task_agent")
    builder.add_edge("task_agent", "backend_code_agent")
    builder.add_edge("backend_code_agent", "backend_code_writer_agent")
    builder.add_edge("backend_code_writer_agent", "frontend_code_agent")
    builder.add_edge("frontend_code_agent", "frontend_code_writer_agent")
    builder.add_edge("frontend_code_writer_agent", "integration_agent")
    builder.add_edge("integration_agent", "integration_code_writer")
    builder.add_edge("integration_code_writer", "debug_agent")
    builder.add_edge("debug_agent", "debug_code_writer")
    builder.add_edge("debug_code_writer", "execution_agent")
    builder.add_edge("execution_agent", "evaluation_agent")
    builder.add_conditional_edges("evaluation_agent",evaluation_router,{"retry": "backend_code_agent","end": END})
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
        end_success_run()
    except Exception as e:
        logger.error(f"Error in main: {e}")
        log_error(e)
        fail_run()
        raise e

if __name__ == "__main__":
    main()