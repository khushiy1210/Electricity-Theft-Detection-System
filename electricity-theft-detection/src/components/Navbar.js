import React from "react";
import { Link } from "react-router-dom";
import styles from "./Navbar.module.css";

function Navbar() {
  return (
    <nav className={styles.navbar}>
      <h2 className={styles.projectTitle}>Electricity Theft Detection</h2>
      <ul className={styles.navList}>
        <li><Link className={styles.navLink} to="/home">Home</Link></li>
        <li><Link className={styles.navLink} to="/dashboard">Dashboard</Link></li>
        <li><Link className={styles.navLink} to="/reports">Reports</Link></li>
        <li><Link className={styles.navLink} to="/settings">Settings</Link></li>
      </ul>
    </nav>
  );
}

export default Navbar;