function RisksPanel({ title, items, emptyText = "No major risks detected" }) {
  return (
    <div className="card-section">
      <h2 className="panel-title">{title}</h2>
      {items && items.length > 0 ? (
        <ul className="list-items">
          {items.map((item, index) => (
            <li key={index} className="list-item">
              {item}
            </li>
          ))}
        </ul>
      ) : (
        <p className="muted-text">{emptyText}</p>
      )}
    </div>
  );
}
export default RisksPanel;
