import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Navbar from "./components/Navbar";
import Home from "./pages/Home";
// import Dashboard from "./pages/Dashboard";
import Reports from "./pages/Reports";
import Dashboard from './components/Dashboard';
import Settings from "./pages/Settings";
import SendWarningPage from "./pages/SendWarningPage";
import GenerateReportPage from "./pages/GenerateReportPage";
import DisableMeterPage from "./pages/DisableMeterPage";

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/home" element={<Home />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/reports" element={<Reports />} />
        <Route path="/settings" element={<Settings />} />
        <Route path="/send-warning" element={<SendWarningPage />} />
        <Route path="/generate-report" element={<GenerateReportPage />} />
        <Route path="/disable-meter" element={<DisableMeterPage />} />
        <Route path="/" element={<Home />} />
      </Routes>
    </Router>
  );
}

export default App;