from upsonic import Task, Agent
from upsonic.safety_engine.policies.pii_policies import PIIBlockPolicy

async def main(inputs):
    user_query = inputs.get("user_query")
    answering_task = Task(f"Answer the user question {user_query}")

    agent = Agent(
        model="openai/gpt-4o-mini",
        agent_policy=PIIBlockPolicy,
        agent_policy_feedback=True,
        agent_policy_feedback_loop=3  # Allow up to 3 retries
    )

    result = await agent.print_do_async(answering_task)

    return {
        "bot_response": result
    }
