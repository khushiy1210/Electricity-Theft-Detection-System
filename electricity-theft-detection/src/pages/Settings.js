import React from 'react';
import './Settings.css'; // Make sure this CSS file exists

const Settings = () => {
  return (
    <div className="settings-container">
      <h1>System Settings</h1>

      <section className="settings-section">
        <h2>Detection Parameters</h2>
        <label>
          Alert Threshold (%):
          <input type="number" placeholder="e.g. 15" />
        </label>
        <label>
          Sampling Interval (mins):
          <input type="number" placeholder="e.g. 30" />
        </label>
        <button>Update Parameters</button>
      </section>

      <section className="settings-section">
        <h2>Notifications</h2>
        <label>
          <input type="checkbox" />
          Enable Email Alerts
        </label>
        <label>
          <input type="checkbox" />
          Enable SMS Alerts
        </label>
        <select>
          <option>Immediate</option>
          <option>Hourly Summary</option>
          <option>Daily Digest</option>
        </select>
      </section>

      <section className="settings-section">
        <h2>Access Control</h2>
        <label>
          Admin Email:
          <input type="email" placeholder="admin@example.com" />
        </label>
        <label>
          <input type="checkbox" />
          Allow Data Export
        </label>
        <button>Save Access Settings</button>
      </section>

      <section className="settings-section danger-zone">
        <h2>Danger Zone</h2>
        <button className="delete-btn">Reset Detection Model</button>
      </section>
    </div>
  );
};

export default Settings;