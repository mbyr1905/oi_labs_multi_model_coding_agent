from typing import TypedDict, Optional, Dict, List


class AgentState(TypedDict):
    prd_text: str
    figma_image_path: Optional[str]
    system_spec: Optional[Dict]
    pages: Optional[List[str]]
    components: Optional[List[str]]
    architecture_plan: dict
    task_plan: dict
    backend_code: dict
    frontend_code: dict
    code_key: str
    output_dir: str