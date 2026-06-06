function RewritePanel({ bullets }) {
  return (
    <div className="card-section">
      <h2 className="panel-title">AI Resume Rewrite Suggestions</h2>

      {bullets && bullets.length > 0 ? (
        <ul className="list-items">
          {bullets.map((bullet, index) => (
            <li key={index} className="rewrite-item">
              {bullet}
            </li>
          ))}
        </ul>
      ) : (
        <p className="muted-text">No rewrite suggestions available.</p>
      )}
    </div>
  );
}

export default RewritePanel;
