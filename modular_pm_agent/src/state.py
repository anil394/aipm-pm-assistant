from typing import TypedDict

from src.models import RiskList, Schedule, TaskAllocationList, TaskList, Team


class AgentState(TypedDict):
    project_description: str
    team: Team
    tasks: TaskList
    dependencies: list[dict]
    schedule: Schedule
    task_allocations: TaskAllocationList
    risks: RiskList
    iteration_number: int
    max_iteration: int
    insights: list[str]
    project_risk_score_iterations: list[int]
