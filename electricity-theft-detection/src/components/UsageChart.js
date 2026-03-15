import { LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid, ResponsiveContainer } from 'recharts';
import styles from './UsageChart.module.css';

function UsageChart() {
  const data = [
    { date: '2025-09-18', usage: 120 },
    { date: '2025-09-19', usage: 150 },
    { date: '2025-09-20', usage: 100 },
    { date: '2025-09-21', usage: 130 },
    { date: '2025-09-22', usage: 350 }, // Possible anomaly
    { date: '2025-09-23', usage: 140 },
    { date: '2025-09-24', usage: 560 },
    { date: '2025-09-25', usage: 110 },
    { date: '2025-09-26', usage: 180 },
    { date: '2025-09-27', usage: 455 }
  ];

  return (
    <div className={styles.container}>
      <h2 className={styles.heading}>📈 Electricity Usage Trends</h2>
      <p className={styles.subtext}>
        Visualize daily electricity consumption and detect unusual spikes using AI-powered insights.
      </p>

      <div className={styles.chartWrapper}>
        <ResponsiveContainer width="100%" height={400}>
          <LineChart data={data}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="date" />
            <YAxis />
            <Tooltip />
            <Line type="monotone" dataKey="usage" stroke="#00c6ff" strokeWidth={3} dot={{ r: 4 }} />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}

export default UsageChart;