import React from "react";
import styles from "./DisableMeterPage.module.css";

const DisableMeterPage = () => {
  return (
    <div className={styles.container}>
      <h2 className={styles.heading}>Disable Meter</h2>
      <p className={styles.description}>
        Admins can remotely disable smart meters flagged by the AI system for electricity theft. This action helps maintain grid integrity and prevent unauthorized consumption.
      </p>

      <div className={styles.card}>
        <h3 className={styles.cardTitle}>Flagged Meter ID: #A1023</h3>
        <p className={styles.cardInfo}>Status: Theft Detected</p>
        <button className={styles.disableButton}>Disable Meter</button>
      </div>
    </div>
  );
};

export default DisableMeterPage;