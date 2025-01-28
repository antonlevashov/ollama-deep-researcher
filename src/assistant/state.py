import operator
from dataclasses import dataclass, field
from typing_extensions import TypedDict, Annotated
from typing import Optional, List, Dict, Any

@dataclass(kw_only=True)
class SummaryState:
    research_topic: str = field(default=None) # Report topic     
    search_query: str = field(default=None) # Search query
    web_research_results: Annotated[list, operator.add] = field(default_factory=list) 
    sources_gathered: Annotated[list, operator.add] = field(default_factory=list) 
    research_loop_count: int = field(default=0) # Research loop count
    running_summary: str = field(default=None) # Final report

@dataclass(kw_only=True)
class SummaryStateInput(TypedDict):
    research_topic: str = field(default=None) # Report topic     

@dataclass(kw_only=True)
class SummaryStateOutput(TypedDict):
    running_summary: str = field(default=None) # Final report

class State(TypedDict):
    query: str
    research_results: Optional[List[Dict[str, Any]]]
    summary: Optional[str]
    follow_up_query: Optional[str]

def initial_state(query: str) -> State:
    """Initialize the state with the query and default values."""
    return State(
        query=query,
        research_results=None,
        summary=None,
        follow_up_query=None  # Initialize with None
    )