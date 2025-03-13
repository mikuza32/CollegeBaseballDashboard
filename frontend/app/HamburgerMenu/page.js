"use client"
import { useEffect, useState } from "react";
import Link from "next/link";
import Aos from "aos";

export default function HamburgerMenu() {
  const [isOpen, setIsOpen] = useState(false);

  const handleHover = () => {
    setIsOpen(true);
  }

  const handleLeave = () => {
    setIsOpen(false);
  }

  useEffect(() => {
    Aos.init({
      duration: 800,
      once: false,
    });
  }, []);

  return (
    <div
      onMouseEnter={handleHover}
      onMouseLeave={handleLeave}
      className="relative"
    >
      <button
        aria-label="Toggle menu"
        aria-pressed={isOpen}
        className="flex flex-col justify-center items-center w-12 h-14 bg-gray-950 text-slate-800 rounded shadow transition"
        data-aos="fade-up"
      >
        <span
          className={`bg-gray-50 block w-10 h-1 rounded-sm transition-all duration-300 ease-out ${
            isOpen ? "rotate-48 translate-y-1.5 translate-x-0.5 bg-red-600" : ""
          }`}
        ></span>
        <span
          className={`bg-gray-50 block w-10 h-1 rounded-sm my-1 transition-all duration-300 ease-out ${
            isOpen ? "-rotate-50 -translate-y-0.5 translate-x-0.2 bg-red-600" : ""
          }`}
        ></span>
        <span
          className={`bg-gray-50 block w-10 h-1 rounded-sm transition-all duration-300 ease-out ${
            isOpen ? "opacity-0" : "opacity-100"
          }`}
        ></span>
      </button>
      {isOpen && (
        <div className="absolute left-0 mt-0 w-48 bg-gray-950 rounded shadow-lg z-10 transition-all duration-300 ease-out">
          <ul>
            <li>
              <Link href="/" legacyBehavior>
                <a className="block px-4 py-2 text-white hover:bg-gray-700 rounded text-xs">
                  Home
                </a>
              </Link>
            </li>
            <li>
              <Link href="/ABvsAVG" legacyBehavior>
                <a className="block px-4 py-2 text-white hover:bg-gray-700 rounded text-xs">
                  At Bats vs. AVG
                </a>
              </Link>
            </li>
            <li>
              <Link href="/GPvsHits" legacyBehavior>
                <a className="block px-4 py-2 text-white hover:bg-gray-700 rounded text-xs">
                  Games Played vs. Total Hits
                </a>
              </Link>
            </li>
            <li>
              <Link href="/BAvsHits" legacyBehavior>
                <a className="block px-4 py-2 text-white hover:bg-gray-700 rounded text-xs">
                  Batting Average vs. Total Hits
                </a>
              </Link>
            </li>
            <li>
              <Link href="/GPvsSLGPCT" legacyBehavior>
                <a className="block px-4 py-2 text-white hover:bg-gray-700 rounded text-xs">
                  Games Played vs. SLG Percentage
                </a>
              </Link>
            </li>
            <li>
              <Link href="/ABvsTB" legacyBehavior>
                <a className="block px-4 py-2 text-white hover:bg-gray-700 rounded text-xs">
                  At Bats vs. Total Bases
                </a>
              </Link>
            </li>
            <li>
              <Link href="/APPvsRA" legacyBehavior>
                <a className="block px-4 py-2 text-white hover:bg-gray-700 rounded text-xs">
                  Appearances vs. Runs Allowed
                </a>
              </Link>
            </li>
            <li>
              <Link href="/IPvsAPP" legacyBehavior>
                <a className="block px-4 py-2 text-white hover:bg-gray-700 rounded text-xs">
                  Innings Pitched vs. Appearances
                </a>
              </Link>
            </li>
            <li>
              <Link href="/IPvsER" legacyBehavior>
                <a className="block px-4 py-2 text-white hover:bg-gray-700 rounded text-xs">
                  Innings Pitched vs. Runs Allowed
                </a>
              </Link>
            </li>
            <li>
              <Link href="/IPvsBB" legacyBehavior>
                <a className="block px-4 py-2 text-white hover:bg-gray-700 rounded text-xs">
                  Innings Pitched vs. Walks Allowed
                </a>
              </Link>
            </li>
            <li>
              <Link href="/IPvsHA" legacyBehavior>
                <a className="block px-4 py-2 text-white hover:bg-gray-700 rounded text-xs">
                  Innings Pitched vs. Hits Allowed
                </a>
              </Link>
            </li>
            <li>
              <Link href="/HAvsBB" legacyBehavior>
                <a className="block px-4 py-2 text-white hover:bg-gray-700 rounded text-xs">
                  Hits Allowed vs. Walks Allowed
                </a>
              </Link>
            </li>
          </ul>
        </div>
      )}
    </div>
  );
}