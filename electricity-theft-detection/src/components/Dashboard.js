import React from "react";
import UsageChart from "./UsageChart";
import Alert from "./Alert";
import ActionButton from "./ActionButton";
import styles from "./Dashboard.module.css";

function Dashboard() {
  return (
    <div className={styles.dashboardContainer}>
      <h2 className={styles.dashboardTitle}>Electricity Theft Detection Dashboard</h2>

      <div className={styles.metricsGrid}>
        <div className={styles.metricCard}>Total Users: 150</div>
        <div className={styles.metricCard}>Total Usage: 12,000 kWh</div>
        <div className={styles.metricCard}>Theft Cases Detected: 5</div>
        <div className={styles.metricCard}>Suspicious Usage: 3%</div>
        <div className={styles.metricCard}>AI Accuracy: 96.4%</div>
      </div>

      <div className={styles.chartSection}>
        <h3>Usage Trends</h3>
        <UsageChart />
      </div>

      <div className={styles.alertSection}>
        <h3>Recent Theft Alerts</h3>
        <Alert />
      </div>

      <div className={styles.actions}>
        <ActionButton label="Send Warning" route="/send-warning" />
        <ActionButton label="Generate Report" route="/generate-report" />
        <ActionButton label="Disable Meter" route="/disable-meter" />
      </div>
    </div>
  );
}

export default Dashboard;