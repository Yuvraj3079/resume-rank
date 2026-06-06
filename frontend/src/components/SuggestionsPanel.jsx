function SuggestionsPanel({ suggestions }) {
  return (
    <div className="card-section">
      <h2 className="panel-title">Improvement Suggestions</h2>

      {suggestions && suggestions.length > 0 ? (
        <ul className="list-items">
          {suggestions.map((suggestion, index) => (
            <li key={index} className="list-item">
              {suggestion}
            </li>
          ))}
        </ul>
      ) : (
        <p className="muted-text">No suggestions available.</p>
      )}
    </div>
  );
}

export default SuggestionsPanel;
