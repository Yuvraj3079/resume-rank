/* eslint-disable no-unused-vars */
import { useEffect, useState } from "react";

function App() {
  const [resume, setResume] = useState("");

  const [jd, setJd] = useState("");

  const [result, setResult] = useState(null);

  const [loading, setLoading] = useState(false);

  const [error, setError] = useState("");

  useEffect(() => {
    const savedResult = localStorage.getItem("last_result");

    const savedResume = localStorage.getItem("last_resume");

    const savedJd = localStorage.getItem("last_jd");

    if (savedResult) {
      setResult(JSON.parse(savedResult));
    }

    if (savedResume) {
      setResume(savedResume);
    }

    if (savedJd) {
      setJd(savedJd);
    }
  }, []);

  async function evaluateResume() {
    try {
      setLoading(true);

      setError("");

      const response = await fetch(
        "http://127.0.0.1:8000/evaluate",

        {
          method: "POST",

          headers: {
            "Content-Type": "application/json",
          },

          body: JSON.stringify({
            resume: {
              name: "Yuvraj",

              skills: resume.split(","),

              experience: [
                {
                  company: "Demo Company",

                  role: "Backend Developer",
                },
              ],
            },

            jd: {
              title: "Backend Engineer",

              required_skills: jd.split(","),

              preferred_skills: [],
            },
          }),
        },
      );

      if (!response.ok) {
        throw new Error("Backend request failed");
      }

      const data = await response.json();

      setResult(data);

      localStorage.setItem("last_result", JSON.stringify(data));

      localStorage.setItem("last_resume", resume);

      localStorage.setItem("last_jd", jd);
    } catch (err) {
      setError("Failed to evaluate resume.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="min-h-screen p-10">
      <h1 className=" text-5xl font-bold mb-10">AI Resume Ranker</h1>

      <div className="max-w-3xl space-y-6">
        <div>
          <label className="block mb-2 text-lg">Resume Skills</label>

          <textarea
            rows="5"
            value={resume}
            onChange={(e) => setResume(e.target.value)}
            placeholder="Python, FastAPI, Docker"
            className="w-full p-4 rounded-xl bg-slate-800 text-white"
          />
        </div>

        <div>
          <label className="block mb-2 text-lg">Job Description Skills</label>

          <textarea
            rows="5"
            value={jd}
            onChange={(e) => setJd(e.target.value)}
            placeholder="Python, FastAPI, Docker"
            className="w-full p-4 rounded-xl bg-slate-800 text-white"
          />
        </div>

        <button
          onClick={evaluateResume}
          disabled={loading}
          className="bg-blue-600 px-6 py-3 rounded-xl hover:bg-blue-700 disabled:opacity-50">
          {loading ? "Analyzing Candidate..." : "Evaluate Resume"}
        </button>

        {error && <div className="bg-red-500 p-4 rounded-xl">{error}</div>}
      </div>

      {result && (
        <div className="mt-12 space-y-6 max-w-4xl">
          <div className="bg-slate-800 p-6 rounded-2xl">
            <h2 className=" text-3xl mb-6 ">Evaluation Result</h2>

            <div className=" grid grid-cols-2 gap-4">
              <div>Overall Score: {result.overall_score}</div>

              <div>Skills Score: {result.skills_score}</div>

              <div>Semantic Score: {result.semantic_score}</div>

              <div>Experience Score: {result.experience_score}</div>
            </div>
          </div>

          <div className="bg-slate-800 p-6 rounded-2xl">
            <h2 className=" text-2xl mb-4">Recruiter Summary</h2>

            <p>{result.recruiter_summary}</p>
          </div>

          <div className=" bg-slate-800 p-6 rounded-2xl ">
            <h2 className=" text-2xl mb-4">Missing Skills</h2>

            <div className=" flex flex-wrap gap-3 ">
              {result.missing_critical_skills.map((skill, index) => (
                <span
                  key={index}
                  className=" bg-red-500 px-3 py-2 rounded-full ">
                  {skill}
                </span>
              ))}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
