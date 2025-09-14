import React from 'react';

function Insights({ dates, signals }) {
  return (
    <div>
      <h2>Actionable Trading Insights</h2>
      <table>
        <thead>
          <tr>
            <th>Date</th>
            <th>Signal</th>
          </tr>
        </thead>
        <tbody>
          {dates.map((date, i) => (
            <tr key={i}>
              <td>{date}</td>
              <td>{signals[i]}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Insights;