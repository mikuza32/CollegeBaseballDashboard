import React, {useEffect, useState} from "react"
import {Bar} from 'react-chartjs-2'
import {
    Chart as chartjs,
    LinearScale,
    CategoryScale,
    BarElement,
    Title,
    Tooltip,
    Legend,
} from 'chart.js'

chartjs.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

export default function IndividualWHIPCharts() {
    const [data, setData] = useState([]);
    const [order, setOrder] = useState("Ascending");
    const [pageSelected, setPageSelected] = useState(0);
    const [chartData, setChartData] = useState(null);
    const [chartWidth, setChartWidth] = useState(600);
    const chartSize = 15;

    useEffect(() => {
        async function fetchData() {
            try {
                const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || 'http://127.0.0.1:8000';
                const res = await fetch(`${API_BASE_URL}/individual_whip_stats`);
                const json = await res.json(data);
                if (json.data) {
                    setData(json.data);
                }
            } catch (error) {
                console.error("Could not retrieve WHIP stats", error);
            }
        }
        fetchData();
    }, []);

    useEffect(() => {
        if (!data || data.length === 0) {
            console.log("No data to process!")
            return;
        }

        let sortedData = [...data];
        if (order === "Ascending") {
            sortedData.sort((a, b) => parseFloat(a["WHIP"]) - parseFloat(b["WHIP"]));
        } else if (order === "Descending") {
            sortedData.sort((a, b) => parseFloat(b["WHIP"]) - (a["WHIP"]));
        } else if (order === "Alphabetical") {
            sortedData.sort((a, b) => a.Name.localeCompare(b.Name));
        }

        const totalPages = Math.ceil(sortedData.length / chartSize);
        if (pageSelected >= totalPages) {
            setPageSelected(0);
        }

        const startIndex = pageSelected * chartSize;
        const limitData = sortedData.slice(startIndex, startIndex + chartSize);
        console.log("Limited Data Shown: ", limitData.length);

        const newWidth = Math.max(600, limitData.length * 40);
        setChartWidth(newWidth);

        const labels = limitData.map(item => item.Name);
        const dataset = limitData.map(item => {
            const num = parseFloat(item["WHIP"]);
            return isNaN(num) ? 0 : num;
        });

        setChartData({
            labels: labels,
            datasets: [
                {
                    label: "Individual WHIP Stats",
                    data: dataset,
                    backgroundColor: "#32CD32"
                },
            ],
        });
    }, [data, order, pageSelected])

    const totalPages = data.length ? Math.ceil(data.length / chartSize) : 0;

    return (
        <div className="bg-black text-gray-200 p-6 rounded-lg shadow-lg">
            <h2 className="text-2xl font-semibold mb-4">Individual WHIP (Walks Hits per Innings Pitched)</h2>
            <select
                className="bg-gray-800 text-gray-200 p-2 rounded mb-4"
                value={order}
                onChange={(e) => setOrder(e.target.value)}
            >
                <option value="Ascending">Ascending</option>
                <option value="Descending">Descending</option>
                <option value="Alphabetical">Alphabetical</option>
            </select>
            <div className="mb-4">
                <select
                    className="bg-gray-800 text-gray-200 p-2 rounded"
                    value={pageSelected}
                    onChange={(e) => setPageSelected(Number(e.target.value))}
                >
                    {Array.from({length: totalPages}, (_, i) => (
                        <option key={i} value={i}>
                            {`${i * chartSize + 1} - ${Math.min((i + 1) * chartSize, data.length)}`}
                        </option>
                    ))}
                </select>
            </div>
        {chartData ? (
        <div style={{width: chartWidth, height: '500px'}}>
            <Bar
                data={chartData}
                options={{
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            labels: {color: '#e0e0e0'},
                        },
                        title: {
                            display: true,
                            text: 'Individual WHIP',
                            color: '#e0e0e0',
                        },
                    },
                    scales: {
                        x: {
                            ticks: { color: '#e0e0e0' },
                            grid: { color: 'rgba(255,255,255,0.1)' }
                        },
                        y: {
                            ticks: { color: '#e0e0e0' },
                            grid: { color: 'rgba(255,255,255,0.1)' }
                        }
                    }
                }}
            />
        </div>
    ) : (
        <p>Loading chart...</p>
    )}
    </div>
    );
};