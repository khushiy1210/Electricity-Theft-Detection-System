// components/ActionButton.js
import React from "react";
import styles from "./ActionButton.module.css";
import { useNavigate } from "react-router-dom";

const ActionButton = ({ label, route }) => {
  const navigate = useNavigate();

  return (
    <button className={styles.button} onClick={() => navigate(route)}>
      {label}
    </button>
  );
};

export default ActionButton;