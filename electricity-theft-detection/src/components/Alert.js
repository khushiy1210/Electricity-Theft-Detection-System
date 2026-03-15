function Alert() {
  const alerts = [
    { user: "User1", level: "High", time: "2025-09-22 10:30" },
    { user: "User2", level: "Medium", time: "2025-09-21 15:45" },
  ];

  return (
    <div>
      <h3>Recent Alerts</h3>
      <ul>
        {alerts.map((a, idx) => (
          <li key={idx} style={{color: a.level==="High"?"red":"orange"}}>
            {a.user} - {a.level} - {a.time}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Alert;
