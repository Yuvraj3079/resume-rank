function SkillsTags({ title, skills, color = "red" }) {
  const colorClasses = {
    red: "badge-red",
    green: "badge-green",
    yellow: "badge-yellow",
    blue: "badge-blue",
  };
  return (
    <div className="card-section">
      <h2 className="panel-title">{title}</h2>

      {skills && skills.length > 0 ? (
        <div className="tag-container">
          {skills.map((skill, index) => (
            <span key={index} className={`skill-tag ${colorClasses[color]}`}>
              {skill}
            </span>
          ))}
        </div>
      ) : (
        <p className="muted-text">None detected.</p>
      )}
    </div>
  );
}

export default SkillsTags;
