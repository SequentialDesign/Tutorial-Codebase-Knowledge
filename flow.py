from pocketflow import Flow
# Import all node classes from nodes.py
from nodes import (
    FetchRepo,
    IdentifyAbstractions,
    AnalyzeRelationships,
    OrderChapters,
    WriteChapters,
    TranslateTutorial,  # New node
    CombineTutorial
)

def create_tutorial_flow():
    """Creates and returns the codebase tutorial generation flow with bilingual support."""

    # Instantiate nodes
    fetch_repo = FetchRepo()
    identify_abstractions = IdentifyAbstractions(max_retries=3, wait=10)
    analyze_relationships = AnalyzeRelationships(max_retries=3, wait=10)
    order_chapters = OrderChapters(max_retries=3, wait=10)
    write_chapters = WriteChapters(max_retries=3, wait=10)  # This is a BatchNode
    
    # New translation node - handles translation of English to Castilian
    translate_tutorial = TranslateTutorial(max_retries=3, wait=10)
    
    # Updated combine tutorial node that handles both languages
    combine_tutorial = CombineTutorial()

    # Connect nodes in sequence based on the design
    fetch_repo >> identify_abstractions
    identify_abstractions >> analyze_relationships
    analyze_relationships >> order_chapters
    order_chapters >> write_chapters
    
    # Add new translation step before combining
    write_chapters >> translate_tutorial
    translate_tutorial >> combine_tutorial

    # Create the flow starting with FetchRepo
    tutorial_flow = Flow(start=fetch_repo)

    return tutorial_flow
