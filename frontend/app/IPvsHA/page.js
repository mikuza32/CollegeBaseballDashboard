"use client"
import { useEffect, useState } from "react";
import { Scatter } from 'react-chartjs-2'
import HamburgerMenu from "../HamburgerMenu/page";
import {
    Chart as chartjs,
    LinearScale,
    PointElement,
    Tooltip,
    Legend,
    Title,
} from 'chart.js'

chartjs.register(LinearScale, PointElement, Tooltip, Legend, Title);

export default function IPvsHA() {
    const [data, setData] = useState([]);
    const [chartData, setChartData] = useState(null);

    useEffect(() => {
        async function fetchData() {
            try {
                const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || 'http://127.0.0.1:8000';
                const res = await fetch(`${API_BASE_URL}/individual_whip_stats`);
                const json = await res.json();
                if (json.data) {
                    setData(json.data);
                } else {
                    console.error("No properties in response", json);
                }
            } catch (error) {
                console.error("Error fetching Batting Average Data", error);
            }
        }
        fetchData();
    }, []);

    useEffect(() => {
        if (!data || data.length === 0) return;

        const scatterPlot = data.map(item => ({
            x: parseFloat(item.IP),
            y: parseFloat(item.HA),
            Name: item.Name,
            Team: item.Team
        }));

        setChartData({
            datasets: [
                {
                    label: 'Innings Pitched vs. Hits Allowed',
                    data: scatterPlot,
                    backgroundColor: '#32CD32',
                },
            ],
        });
    }, [data]);

    const chartOptions = {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            title: {
                display: true,
                text: 'Innings Pitched vs. Hits Allowed',
                color: '#e0e0e0',
            },
            legend: {
                labels: {color: '#e0e0e0'},
            },
            tooltip: {
                callbacks: {
                    label: function (context) {
                        const {x, y, Name, Team} = context.raw;
                        return [
                            `Name: ${Name}`,
                            `School: ${Team}`,
                            `Innings Pitched: ${x}`,
                            `Hits Allowed: ${y}`,
                        ];
                    },
                },
            },
        },

        scales: {
            x: {
                title: {display: true, text: 'Innings Pitched', color: '#e0e0e0'},
                ticks: {color: '#e0e0e0'},
                grid: {color: 'rgba(255,255,255,0.1)'},
            },
            y: {
                title: {display: true, text: 'Hits Allowed', color: '#e0e0e0'},
                ticks: {color: '#e0e0e0'},
                grid: {color: 'rgba(255,255,255,0.1)'},
            },
        },
    };

    return (
        <div className=" min-h-screen bg-black text-gray-50 p-6 rounded-lg shadow-lg  overflow-x-auto">
            <header className="flex items-center justify-between p-4">
                <HamburgerMenu />
            </header>
            <h1 className=" text-4xl font-extrabold text-center mb-10">NCAA Division 1 Baseball: Innings Pitched vs. Hits Allowed</h1>
            {chartData ? (
                <div className="w-full h-screen">
                    <Scatter data={chartData} options={chartOptions} />
                </div>
            ) : (
                <p>Loading data...</p>
            )}
        </div>
    );
}