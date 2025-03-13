"use client"

import Head from "next/head";
import IndividualBattingAverageCharts from "./IndividualBattingAverage/page";
import IndividualSluggingPercentageCharts from "@/app/IndividualSLGPCT/page";
import IndividualEarnedRunAverageCharts from "./IndividualERA/page";
import IndividualWHIPCharts from "./IndividualWHIP/page";
import HamburgerMenu from "./HamburgerMenu/page";



export default function Home() {

  return (
    <div className="min-h-screen" style={{ backgroundColor: "#121212", color: "#FFFFFF" }}>
      <Head>
        <title>Division 1 Baseball Statistics</title>
        <meta name="description" content="Zane's Interactive Baseball Dashboard" />
        <link rel="icon" href="/favicon.ico"/>
      </Head>
      <header className="flex items-center justify-between p-4">
        <HamburgerMenu />
      </header>
      <h1 className=" text-4xl font-extrabold text-center mb-10">NCAA D1 Baseball Statistics Dashboard</h1>
      <main className="grid grid-cols-2 grid-rows-2 gap-4 p-4 shadow-stone-600">
        <div className="flex items-center justify-center bg-stone-800 rounded-2xl p-4">
          <IndividualBattingAverageCharts />
        </div>
        <div className="flex items-center justify-center bg-stone-800 rounded-2xl p-4">
          <IndividualSluggingPercentageCharts />
        </div>
        <div className="flex items-center justify-center bg-stone-800 rounded-2xl p-4">
          <IndividualEarnedRunAverageCharts />
        </div>
        <div className="flex items-center justify-center bg-stone-800 rounded-2xl p-4">
          <IndividualWHIPCharts />
        </div>
      </main>
    </div>
  );
}