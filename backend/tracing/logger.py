from datetime import datetime
import uuid

from database.db import connection, cursor


def create_trace(agent_name: str, task: str):

    trace = {
        "trace_id": str(uuid.uuid4()),
        "agent": agent_name,
        "task": task,
        "start_time": datetime.utcnow().isoformat()
    }

    return trace


def close_trace(trace: dict, output: str):

    end_time = datetime.utcnow()

    trace["end_time"] = end_time.isoformat()

    start = datetime.fromisoformat(
        trace["start_time"]
    )

    trace["duration_seconds"] = (
        end_time - start
    ).total_seconds()

    trace["output"] = output

    save_trace(trace)

    return trace


def save_trace(trace: dict):

    cursor.execute("""
    INSERT INTO traces VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        trace["trace_id"],
        trace["agent"],
        trace["task"],
        trace["start_time"],
        trace["end_time"],
        trace["duration_seconds"],
        str(trace["output"])
    ))

    connection.commit()
