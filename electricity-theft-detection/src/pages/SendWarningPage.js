import React from "react";
import styles from "./SendWarningPage.module.css";

const SendWarningPage = () => {
  return (
    <div className={styles.container}>
      <h2 className={styles.heading}>Send Warning</h2>
      <p className={styles.description}>
        This interface allows admins to send automated warnings to users whose meters have been flagged by the AI system for suspicious activity or potential electricity theft.
      </p>

      <div className={styles.warningCard}>
        <h3 className={styles.cardTitle}>User ID: #U5678</h3>
        <p className={styles.cardInfo}>Flag Reason: Unusual consumption spike</p>
        <textarea
          className={styles.textArea}
          placeholder="Enter custom warning message or use default template..."
        />
        <button className={styles.sendButton}>Send Warning</button>
      </div>
    </div>
  );
};

export default SendWarningPage;