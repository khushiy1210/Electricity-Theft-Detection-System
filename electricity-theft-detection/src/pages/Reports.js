import styles from './Reports.module.css';

function Reports() {
  return (
    <div className={styles.container}>
      <h2 className={styles.heading}>📄 Theft Detection Reports</h2>
      <p className={styles.subtext}>
        Review flagged electricity usage patterns and AI-generated alerts across smart meters.
      </p>

      <div className={styles.tableWrapper}>
        <table className={styles.table}>
          <thead>
            <tr>
              <th>Meter ID</th>
              <th>Usage</th>
              <th>Alert Level</th>
              <th>Date</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>001</td>
              <td>350 kWh</td>
              <td className={styles.high}>High</td>
              <td>2025-09-22</td>
            </tr>
            {/* Add more rows dynamically later */}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Reports;