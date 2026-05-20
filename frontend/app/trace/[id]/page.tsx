interface PageProps {
  params: Promise<{
    id: string
  }>
}

async function getTrace(id: string) {

  const response = await fetch(
    `http://127.0.0.1:8000/trace/${id}`,
    {
      cache: "no-store"
    }
  )

  return response.json()
}

export default async function TracePage({
  params
}: PageProps) {

  const { id } = await params

  const trace = await getTrace(id)

  return (
    <main className="min-h-screen bg-black text-white p-10">

      <h1 className="text-5xl font-bold mb-10">
        Trace Inspection
      </h1>

      <div className="bg-zinc-900 border border-zinc-800 rounded-xl p-8">

        <p className="mb-4">
          <strong>Trace ID:</strong> {trace.trace_id}
        </p>

        <p className="mb-4">
          <strong>Agent:</strong> {trace.agent}
        </p>

        <p className="mb-4">
          <strong>Task:</strong> {trace.task}
        </p>

        <p className="mb-4">
          <strong>Duration:</strong>{" "}
          {trace.duration_seconds?.toFixed(2)}s
        </p>

        <p className="mb-8">
          <strong>Started:</strong> {trace.start_time}
        </p>

        <div className="bg-black p-6 rounded-lg overflow-auto border border-zinc-700">

          <pre className="whitespace-pre-wrap text-sm text-green-400">
            {trace.output}
          </pre>

        </div>

      </div>

    </main>
  )
}
