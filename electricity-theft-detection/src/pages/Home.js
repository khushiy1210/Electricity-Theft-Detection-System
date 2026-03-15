import React, { useState, useEffect } from "react";
import styles from "./Home.module.css";

function Home() {
  const [showLogin, setShowLogin] = useState(false);
  const [isCreateMode, setIsCreateMode] = useState(false);
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  // Load initial login state and defaults
  useEffect(() => {
    const logged = localStorage.getItem("isAdminLoggedIn") === "true";
    setIsLoggedIn(logged);
  }, []);

  // Helper to read saved credentials; fallback to default admin/admin123
  const getSavedCredentials = () => {
    const savedUser = localStorage.getItem("adminUsername");
    const savedPass = localStorage.getItem("adminPassword");
    return {
      savedUser: savedUser || "admin",
      savedPass: savedPass || "admin123",
    };
  };

  // LOGIN
  const handleLogin = (e) => {
    e.preventDefault();
    const { savedUser, savedPass } = getSavedCredentials();

    if (username === savedUser && password === savedPass) {
      localStorage.setItem("isAdminLoggedIn", "true");
      setIsLoggedIn(true);
      setShowLogin(false);
      setError("");
      setSuccess("");
      // clear fields for security
      setUsername("");
      setPassword("");
    } else {
      setError("Invalid username or password");
      setSuccess("");
    }
  };

  // CREATE NEW ADMIN
  const handleCreateAdmin = (e) => {
    e.preventDefault();
    if (!username.trim() || !password) {
      setError("Please enter both username and password");
      setSuccess("");
      return;
    }

    localStorage.setItem("adminUsername", username.trim());
    localStorage.setItem("adminPassword", password);
    setSuccess("Admin account created successfully. Please login.");
    setError("");
    // switch to login mode and prefill login fields with created creds
    setIsCreateMode(false);
    setTimeout(() => {
      setUsername(localStorage.getItem("adminUsername"));
      setPassword(localStorage.getItem("adminPassword"));
    }, 50);
  };

  // LOGOUT
  const handleLogout = () => {
    localStorage.removeItem("isAdminLoggedIn");
    setIsLoggedIn(false);
  };

  // close modal and clear messages
  const closeModal = () => {
    setShowLogin(false);
    setIsCreateMode(false);
    setError("");
    setSuccess("");
    setUsername("");
    setPassword("");
  };

  return (
    <div className={styles.container}>
      {/* HEADER */}
      <header className={styles.header}>
        <h1 className={styles.logo}>ELECTRICITY THEFT DETECTION</h1>
        <div className={styles.headerRight}>
          {isLoggedIn ? (
            <button onClick={handleLogout} className={styles.logoutBtn}>
              Logout
            </button>
          ) : (
            <button
              onClick={() => {
                setShowLogin(true);
                setIsCreateMode(false);
                setError("");
                setSuccess("");
                // prefill default username for convenience
                const { savedUser } = getSavedCredentials();
                setUsername(savedUser);
                setPassword("");
              }}
              className={styles.loginBtn}
            >
              Admin Login
            </button>
          )}
        </div>
      </header>

      {/* HERO */}
      <section className={styles.hero}>
        <h1 className={styles.title}>Electricity Theft Detection System</h1>
        <p className={styles.subtitle}>
          AI-powered solution to monitor usage, detect anomalies, and prevent electricity theft in smart grids.
        </p>
        <a href="#features" className={styles.cta}>Explore Features</a>
      </section>

      {/* FEATURES */}
      <section id="features" className={styles.features}>
        <h2>Key Features</h2>
        <ul>
          <li>Real-time electricity usage monitoring</li>
          <li>AI-based anomaly detection</li>
          <li>Location-based theft alerts</li>
          <li>Automated report generation</li>
        </ul>
      </section>

      {/* FOOTER */}
      <footer className={styles.footer}>
        <p>© 2025 Electricity Theft Detection System. All rights reserved.</p>
      </footer>

      {/* MODAL */}
      {showLogin && (
        <div className={styles.modalOverlay} role="dialog" aria-modal="true">
          <div className={styles.modal}>
            <h2>{isCreateMode ? "Create Admin Account" : "Admin Login"}</h2>

            {error && <p className={styles.error}>{error}</p>}
            {success && <p className={styles.success}>{success}</p>}

            <form onSubmit={isCreateMode ? handleCreateAdmin : handleLogin}>
              <input
                type="text"
                placeholder="Username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                className={styles.input}
                required
                autoFocus
              />
              <input
                type="password"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className={styles.input}
                required
              />
              <button type="submit" className={styles.submitBtn}>
                {isCreateMode ? "Create Admin" : "Login"}
              </button>
            </form>

            <div className={styles.modalActions}>
              <button
                className={styles.toggleBtn}
                onClick={() => {
                  setIsCreateMode((m) => !m);
                  setError("");
                  setSuccess("");
                  // clear fields when toggling
                  setUsername("");
                  setPassword("");
                }}
              >
                {isCreateMode ? "← Back to Login" : "Create New Admin"}
              </button>

              <button className={styles.closeBtn} onClick={closeModal}>
                ✖ Close
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default Home;
