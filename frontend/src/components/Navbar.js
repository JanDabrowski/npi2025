import React from "react";
import { useNavigate, Link } from "react-router-dom";
import styles from "../styles/Navbar.module.css";

const Navbar = () => {
  const navigate = useNavigate();

  const handleHomeClick = () => {
    const token = localStorage.getItem("access_token");
    console.log(token);

    if (token) {
      return "/books"; // Jeśli token jest, przekierowujemy na /books
    } else {
      return "/"; // Jeśli tokena nie ma, przekierowujemy na stronę główną
    }
  };
  
  const handleLogout = () => {
    localStorage.removeItem("access_token");
    navigate("/");
  };

  return (
    <header className={styles.navbar}>
      <nav>
        <ul>
          <li>
            <Link to={handleHomeClick()} className={styles.navButton}>
              Strona Główna
            </Link>
          </li>
          <li>
            <Link to="/rental-history" className={styles.navButton}>Moja historia</Link>
          </li>
          <li>
            <Link to="/about">O nas</Link>
          </li>
          <li>
            <Link to="/contact">Kontakt</Link>
          </li>
          <li>
            <button onClick={handleLogout} className={styles.logoutButton}>
              Wyloguj się
            </button>
          </li>
        </ul>
      </nav>
    </header>
  );
};

export default Navbar;
