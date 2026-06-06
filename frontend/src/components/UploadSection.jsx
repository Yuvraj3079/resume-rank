/* eslint-disable no-unused-vars */
function UploadSection({
  file,
  setFile,
  resume,
  setResume,
  jd,
  setJd,
  evaluateResume,
  loading,
}) {
  return (
    <div className="input-panel">
      <div>
        <h2 className="section-title">Candidate Input</h2>

        <p className="muted-text mt-1">
          Upload a resume PDF and paste a full job description from LinkedIn.
        </p>
      </div>

      <div>
        <label className="input-label">Upload Resume PDF</label>

        <input
          type="file"
          accept=".pdf"
          onChange={(event) => setFile(event.target.files[0])}
          className="file-input"
        />
      </div>

      <div>
        <label className="input-label">Resume Skills</label>

        <textarea
          rows="4"
          value={resume}
          onChange={(event) => setResume(event.target.value)}
          placeholder="Python, FastAPI, Docker, AWS"
          className="text-area"
        />
      </div>

      <div>
        <label className="input-label">Full Job Description</label>

        <textarea
          rows="8"
          value={jd}
          onChange={(event) => setJd(event.target.value)}
          placeholder="Paste the full LinkedIn job description here..."
          className="text-area"
        />
      </div>

      <button
        onClick={evaluateResume}
        disabled={loading}
        className="primary-button">
        {loading ? "Analyzing..." : "Evaluate Candidate"}
      </button>
    </div>
  );
}

export default UploadSection;
