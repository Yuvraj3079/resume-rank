/* eslint-disable no-unused-vars */
import { useEffect, useState } from "react";
import Loader from "./components/Loader";
import RecruiterSummary from "./components/RecruiterSummary";
import RewritePanel from "./components/RewritePanel";
import RisksPanel from "./components/RisksPanel";
import ScoreCards from "./components/ScoreCards";
import SkillsTags from "./components/SkillsTags";
import SuggestionsPanel from "./components/SuggestionsPanel";
import UploadSection from "./components/UploadSection";
import "./styles/dashboard.css";
function App() {
  const [file, setFile] = useState(null);

  const [resume, setResume] = useState("");

  const [jd, setJd] = useState("");

  const [result, setResult] = useState(null);

  const [loading, setLoading] = useState(false);

  const [error, setError] = useState("");

  const [parsedJd, setParsedJd] = useState(null);

  useEffect(() => {
    const savedResult = localStorage.getItem("last_result");

    const savedResume = localStorage.getItem("last_resume");

    const savedJd = localStorage.getItem("last_jd");

    const savedParsedJd = localStorage.getItem("last_parsed_jd");

    if (savedParsedJd) {
      setParsedJd(JSON.parse(savedParsedJd));
    }

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

  async function extractResumeFromPdf() {
    if (!file) {
      return resume;
    }

    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch("http://127.0.0.1:8000/upload", {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      throw new Error("Resume upload failed.");
    }

    const data = await response.json();

    const extractedSkills = data.resume_data?.skills || data.skills || [];

    if (extractedSkills.length === 0) {
      throw new Error("No skills extracted from resume.");
    }

    const skillsText = extractedSkills.join(", ");

    setResume(skillsText);

    localStorage.setItem("last_resume", skillsText);

    return skillsText;
  }
  async function parseJdText() {
    if (!jd.trim()) {
      throw new Error("Job description is empty.");
    }

    const response = await fetch("http://127.0.0.1:8000/parse-jd", {
      method: "POST",

      headers: {
        "Content-Type": "application/json",
      },

      body: JSON.stringify({
        jd_text: jd,
      }),
    });

    if (!response.ok) {
      throw new Error("Job description parsing failed.");
    }

    const data = await response.json();

    setParsedJd(data);

    localStorage.setItem("last_parsed_jd", JSON.stringify(data));

    localStorage.setItem("last_jd", jd);

    return data;
  }

  async function evaluateResume() {
    if (!file && !resume.trim()) {
      setError("Please upload a resume PDF or enter resume skills.");
      return;
    }

    if (!jd.trim()) {
      setError("Please paste a job description.");
      return;
    }

    try {
      setLoading(true);
      setError("");

      const finalResumeText = await extractResumeFromPdf();

      const finalParsedJd = await parseJdText();

      const response = await fetch("http://127.0.0.1:8000/evaluate", {
        method: "POST",

        headers: {
          "Content-Type": "application/json",
        },

        body: JSON.stringify({
          resume: {
            name: "Yuvraj",

            skills: finalResumeText
              .split(",")
              .map((skill) => skill.trim())
              .filter(Boolean),

            experience: [
              {
                company: "Demo Company",
                role: "Backend Developer",
              },
            ],
          },

          jd: finalParsedJd,
        }),
      });

      if (!response.ok) {
        throw new Error("Evaluation request failed.");
      }

      const data = await response.json();

      setResult(data);

      localStorage.setItem("last_result", JSON.stringify(data));
    } catch (err) {
      console.error(err);
      setError(err.message || "Failed to evaluate candidate.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="app-page">
      <header className="app-header">
        <h1 className="app-title">AI Resume Ranker</h1>

        <p className="app-subtitle">
          Upload resumes, evaluate job fit, identify ATS gaps, generate
          recruiter insights, and create AI-powered resume improvemnt
          suggesions.
        </p>
      </header>
      <div className="app-grid">
        <div className="sidebar-column">
          <UploadSection
            file={file}
            setFile={setFile}
            resume={resume}
            setResume={setResume}
            jd={jd}
            setJd={setJd}
            evaluateResume={evaluateResume}
            loading={loading}
          />
          {parsedJd && (
            <div className="card-section-dark mt-6">
              <h2 className="panel-title">Parsed Job Description</h2>

              <p className="body-text">
                <strong>Title:</strong> {parsedJd.title}
              </p>

              <p className="small-muted-text mt-3">Required Skills:</p>

              <p className="body-text">{parsedJd.required_skills.join(", ")}</p>

              <p className="small-muted-text mt-3">Preferred Skills:</p>

              <p className="body-text">
                {parsedJd.preferred_skills.join(", ")}
              </p>
            </div>
          )}
          {loading && (
            <div className="loader-wrapper">
              <Loader />
            </div>
          )}

          {error && <div className="error-banner">{error}</div>}
        </div>
        <div className="results-column">
          {!result && (
            <div className="empty-state">
              <h2 className="section-title">No evaluation yet</h2>
              <p className="muted-text mt-2">
                Upload a resume or manually enter skills, then evaluate
              </p>
            </div>
          )}
          {result && (
            <>
              <ScoreCards result={result} />
              <RecruiterSummary result={result} />
              <div className="two-column-grid">
                <SkillsTags
                  title="Matched Skills"
                  skills={result.matched_skills}
                  color="green"
                />
                <SkillsTags
                  title="Missing Critical Skills"
                  skills={result.missing_critical_skills}
                  color="red"
                />
                <SkillsTags
                  title="Missing Secondary Skills"
                  skills={result.missing_secondary_skills}
                  color="yellow"
                />
                <SkillsTags
                  title="Technical Gaps"
                  skills={result.technical_gaps}
                  color="blue"
                />
              </div>

              <div className="two-column-grid">
                <RisksPanel
                  title="Strengths"
                  items={result.strengths}
                  emptyText="No major strengths detected."
                />

                <RisksPanel
                  title="Weaknesses"
                  items={result.weaknesses}
                  emptyText="No major weaknesses detected."
                />

                <RisksPanel
                  title="Interview Risks"
                  items={result.interview_risks}
                  emptyText="No interview risks detected."
                />

                <RisksPanel
                  title="Recruiter Questions"
                  items={result.recruiter_questions}
                  emptyText="No recruiter questions available."
                />
              </div>

              <RewritePanel bullets={result.rewritten_bullets} />

              <SuggestionsPanel suggestions={result.improvement_suggestions} />
            </>
          )}
        </div>
      </div>{" "}
    </div> // app-page
  );
}

export default App;
