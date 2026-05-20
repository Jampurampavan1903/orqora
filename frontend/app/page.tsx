import Link from "next/link"


async function getTraces() {

  const response = await fetch(
    "http://127.0.0.1:8000/traces",
    {
      cache: "no-store"
    }
  )

  return response.json()
}


export default async function Home() {

  const traces = await getTraces()

  return (

    <main className="min-h-screen bg-black text-white p-10">

      <h1 className="text-5xl font-bold mb-10">
        Orqora Observability
      </h1>

      <div className="space-y-6">

        {traces.map((trace: any) => (

          <Link
            href={`/trace/${trace.trace_id}`}
            key={trace.trace_id}
          >

            <div
              className="border border-gray-800 rounded-xl p-6 bg-zinc-900 hover:bg-zinc-800 transition"
            >

              <h2 className="text-2xl font-semibold mb-2">
                {trace.task}
              </h2>

              <p className="text-sm text-gray-400 mb-2">
                Trace ID: {trace.trace_id}
              </p>

              <p className="text-sm text-gray-400 mb-2">
                Agent: {trace.agent}
              </p>

              <p className="text-sm text-gray-400 mb-2">
                Duration: {trace.duration_seconds.toFixed(2)}s
              </p>

              <p className="text-sm text-gray-400">
                Started: {trace.start_time}
              </p>

            </div>

          </Link>

        ))}

      </div>

    </main>
  )
}
