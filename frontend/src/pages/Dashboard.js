// frontend/src/pages/Dashboard.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import {
  BarChart, Bar, XAxis, YAxis, Tooltip,
  RadarChart, Radar, PolarGrid, PolarAngleAxis, PolarRadiusAxis
} from 'recharts';

export default function Dashboard() {
  const [boxer, setBoxer] = useState(null);

  useEffect(() => {
    axios.get('/api/boxer-stats/2/')
      .then(res => setBoxer(res.data))
      .catch(err => console.error(err));
  }, []);

  if (!boxer) return <div>Loading…</div>;

  const statsData = [
    { stat: 'Strength',  value: boxer.stats.strength  },
    { stat: 'Endurance',   value: boxer.stats.endurance   },
    { stat: 'Speed',     value: boxer.stats.speed     },
    { stat: 'Reflex',    value: boxer.stats.reflex    },
    { stat: 'Boxing IQ', value: boxer.stats.boxing_iq },
    { stat: 'Heart',     value: boxer.stats.heart     },
  ];

  return (
    <div>
      <h2>
        {boxer.alias} — {boxer.first_name} {boxer.last_name}
      </h2>

      <div className="dashboard-layout">
        {/* Left: Horizontal Bar Chart */}
        <BarChart
          layout="vertical"
          width={400}
          height={400}
          data={statsData}
          
        >
          <XAxis type="number" domain={[0, 100]} />
          <YAxis type="category" dataKey="stat" width={100}/>
          <Tooltip />
          <Bar dataKey="value" />
        </BarChart>

        {/* Center: Info Cards */}
        <div className="info-cards">
          <div className="card">Sex: {boxer.sex}</div>
          <div className="card">Age: {boxer.age}</div>
          <div className="card">Nationality: {boxer.nationality}</div>
          <div className="card">Stance: {boxer.stance}</div>
          <div className="card">
            Height: {boxer.height_imperial} / {boxer.height_metric} cm
          </div>
          <div className="card">
            Reach: {boxer.reach_imperial} / {boxer.reach_metric} cm
          </div>
          <div className="card">Division: {boxer.division}</div>
          <div className="card">
            Record: {boxer.fight_record.wins}–{boxer.fight_record.losses}–{boxer.fight_record.draws}
          </div>
          <div className="card">
            KOs: {boxer.fight_record.wins_by_knockout} / LKO: {boxer.fight_record.losses_by_knockout}
          </div>
        </div>

        {/* Right: Radar (Hexagon) Chart */}
        <RadarChart
          outerRadius={120}
          width={400}
          height={400}
          data={statsData}
        >
          <PolarGrid />
          <PolarAngleAxis 
            dataKey="stat"
          />
          <PolarRadiusAxis domain={[0,100]} />
          <Radar dataKey="value" fillOpacity={0.6} />
        </RadarChart>
      </div>
    </div>
  );
}
