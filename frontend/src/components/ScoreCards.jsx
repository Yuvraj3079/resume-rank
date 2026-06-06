function getScoreClass(value) {
  if (value >= 75) {
    return "score-high";
  }

  if (value >= 50) {
    return "score-medium";
  }

  return "score-low";
}

function getScoreLabel(value) {
  if (value >= 75) {
    return "Strong Match";
  }

  if (value >= 50) {
    return "Moderate Match";
  }

  return "Weak Match";
}

function ScoreCard({ label, value }) {
  const score = value ?? 0;

  return (
    <div className="score-card">
      <p className="score-label">{label}</p>

      <p className={`score-value ${getScoreClass(score)}`}>
        {score}
        <span className="score-percent">%</span>
      </p>

      <p className={`score-status ${getScoreClass(score)}`}>
        {getScoreLabel(score)}
      </p>
    </div>
  );
}

function ScoreCards({ result }) {
  return (
    <div className="score-grid">
      <ScoreCard label="Overall Score" value={result.overall_score} />

      <ScoreCard label="Skills Score" value={result.skills_score} />

      <ScoreCard label="Semantic Score" value={result.semantic_score} />

      <ScoreCard label="Experience Score" value={result.experience_score} />
    </div>
  );
}

export default ScoreCards;
