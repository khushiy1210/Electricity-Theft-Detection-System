import React from "react";
import styles from "./GenerateReportPage.module.css";

const GenerateReportPage = () => {
  return (
    <div className={styles.container}>
      <h2 className={styles.heading}>Generate Report</h2>
      <p className={styles.description}>
        Use this dashboard to generate detailed reports on electricity consumption patterns, flagged theft cases, and AI-detected anomalies across the smart grid.
      </p>

      <div className={styles.reportCard}>
        <h3 className={styles.cardTitle}>Report Type</h3>
        <select className={styles.dropdown}>
          <option>Usage Summary</option>
          <option>Theft Detection Logs</option>
          <option>AI Anomaly Insights</option>
        </select>

        <h3 className={styles.cardTitle}>Select Time Range</h3>
        <input type="date" className={styles.datePicker} />
        <input type="date" className={styles.datePicker} />

        <button className={styles.generateButton}>Generate Report</button>
      </div>
    </div>
  );
};

export default GenerateReportPage;