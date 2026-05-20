from database.db import cursor


def get_all_traces():

    cursor.execute("""
    SELECT * FROM traces
    ORDER BY start_time DESC
    """)

    rows = cursor.fetchall()

    traces = []

    for row in rows:

        traces.append({
            "trace_id": row[0],
            "agent": row[1],
            "task": row[2],
            "start_time": row[3],
            "end_time": row[4],
            "duration_seconds": row[5],
            "output": row[6]
        })

    return traces


def get_trace(trace_id: str):

    cursor.execute("""
    SELECT * FROM traces
    WHERE trace_id = ?
    """, (trace_id,))

    row = cursor.fetchone()

    if not row:
        return {"error": "Trace not found"}

    return {
        "trace_id": row[0],
        "agent": row[1],
        "task": row[2],
        "start_time": row[3],
        "end_time": row[4],
        "duration_seconds": row[5],
        "output": row[6]
    }
