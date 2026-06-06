function RecruiterSummary({ result }) {
  return (
    <div className="card-section ">
      <div className="summary-header">
        <div>
          <h2 className="section-title">Recruiter Summary</h2>
          <p className="small-muted-text">
            AI-generated recruiter-style assessment.
          </p>
        </div>
        <div className="summary-badges p-2">
          <span className="badge badge-blue">
            {result.hire_recommendation || "Unknown"}
          </span>
          <span className="badge badge-purple">
            Confidence: {result.confidence_level || "Low"}
          </span>

          <span className="badge badge-yellow">
            ATS Risk: {result.ats_risk || "Unknown"}
          </span>
        </div>
      </div>
      <p className="body-text mt-4">
        {result.recruiter_summary || "No recruiter summary available."}
      </p>
    </div>
  );
}
export default RecruiterSummary;
