import React, { useState } from "react";
import styles from "../styles/StarRating.module.css";

const StarRating = ({ initialRating = 0, onRatingChange }) => {
  const [rating, setRating] = useState(initialRating);

  const handleClick = (index, e) => {
    setRating(index);
    if (onRatingChange) {
      onRatingChange(index, e);
    }
  };

  return (
    <div className={styles.starContainer}>
      {[1, 2, 3, 4, 5].map((index) => (
        <span
          key={index}
          className={`${styles.star} ${index <= rating ? styles.filled : ""}`}
          onClick={() => handleClick(index)}
        >
          ★
        </span>
      ))}
    </div>
  );
};

export default StarRating;
