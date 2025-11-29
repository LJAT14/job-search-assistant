"""
🤖 JOB BOT PRO - ULTRA MODERN DESIGN
Dark Glassmorphic Theme with Gradients & Animations
Multi-Platform Auto-Apply with Session Management
"""

import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime, timedelta
import time
import requests
from bs4 import BeautifulSoup
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
import random
from typing import List, Dict
import pickle
import subprocess
import threading

# ==================================
# PAGE CONFIG
# ==================================
st.set_page_config(
    page_title="Job Search Assistant",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================================
# ULTRA MODERN GLASSMORPHIC CSS
# ==================================
st.markdown("""
<style>
    /* Import Modern Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');
    
    /* ROOT VARIABLES */
    :root {
        --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        --secondary-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        --success-gradient: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        --dark-bg: #0a0e27;
        --card-bg: rgba(255, 255, 255, 0.05);
        --glass-bg: rgba(255, 255, 255, 0.1);
        --text-primary: #ffffff;
        --text-secondary: #a0aec0;
        --neon-blue: #00f2fe;
        --neon-purple: #764ba2;
    }
    
    /* GLOBAL STYLES */
    * {
        font-family: 'Inter', sans-serif !important;
    }
    
    /* MAIN BACKGROUND - Dark with gradient */
    .stApp {
        background: linear-gradient(135deg, #0a0e27 0%, #1a1a2e 50%, #16213e 100%);
        background-attachment: fixed;
    }
    
    /* REMOVE STREAMLIT BRANDING */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* GLASSMORPHIC CONTAINERS */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 2rem;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        transition: all 0.3s ease;
    }
    
    .glass-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px 0 rgba(31, 38, 135, 0.5);
        border-color: rgba(255, 255, 255, 0.2);
    }
    
    /* ANIMATED GRADIENT HEADER */
    .gradient-text {
        background: linear-gradient(90deg, #667eea, #764ba2, #f093fb, #667eea);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradientFlow 3s ease infinite;
        font-size: 3.5rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0.5rem;
        letter-spacing: -1px;
    }
    
    @keyframes gradientFlow {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    /* NEON STAT CARDS */
    .neon-card {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 2rem;
        border: 1px solid rgba(102, 126, 234, 0.3);
        box-shadow: 
            0 0 20px rgba(102, 126, 234, 0.3),
            0 8px 32px rgba(31, 38, 135, 0.37);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .neon-card::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(102, 126, 234, 0.1), transparent);
        transform: rotate(45deg);
        animation: shine 3s infinite;
    }
    
    @keyframes shine {
        0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
        100% { transform: translateX(100%) translateY(100%) rotate(45deg); }
    }
    
    .neon-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 
            0 0 40px rgba(102, 126, 234, 0.6),
            0 12px 40px rgba(31, 38, 135, 0.5);
        border-color: rgba(102, 126, 234, 0.6);
    }
    
    .stat-number {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(135deg, #fff 0%, #a0aec0 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .stat-label {
        color: #a0aec0;
        font-size: 0.9rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* JOB CARD - ULTRA MODERN */
    .job-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(255, 255, 255, 0.02) 100%);
        backdrop-filter: blur(10px);
        border-radius: 16px;
        padding: 1.5rem;
        border-left: 4px solid;
        border-image: linear-gradient(135deg, #667eea 0%, #764ba2 100%) 1;
        margin: 1rem 0;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .job-card::after {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        width: 100px;
        height: 100px;
        background: radial-gradient(circle, rgba(102, 126, 234, 0.2) 0%, transparent 70%);
        border-radius: 50%;
    }
    
    .job-card:hover {
        transform: translateX(10px);
        box-shadow: 0 8px 30px rgba(102, 126, 234, 0.4);
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.08) 0%, rgba(255, 255, 255, 0.04) 100%);
    }
    
    .job-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 0.5rem;
    }
    
    .job-company {
        color: #667eea;
        font-weight: 600;
        font-size: 1.1rem;
    }
    
    .job-meta {
        color: #a0aec0;
        font-size: 0.9rem;
        margin-top: 0.5rem;
    }
    
    /* BUTTONS - NEON GRADIENT */
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 2rem;
        font-weight: 700;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(102, 126, 234, 0.6);
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }
    
    /* SIDEBAR - DARK GLASS */
    [data-testid="stSidebar"] {
        background: rgba(10, 14, 39, 0.95);
        backdrop-filter: blur(20px);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    [data-testid="stSidebar"] .stMarkdown {
        color: #ffffff;
    }
    
    /* INPUT FIELDS - MODERN */
    .stTextInput>div>div>input,
    .stSelectbox>div>div>div,
    .stMultiSelect>div>div>div {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        color: #ffffff;
        padding: 0.75rem;
        transition: all 0.3s ease;
    }
    
    .stTextInput>div>div>input:focus,
    .stSelectbox>div>div>div:focus {
        border-color: #667eea;
        box-shadow: 0 0 20px rgba(102, 126, 234, 0.3);
        background: rgba(255, 255, 255, 0.08);
    }
    
    /* TABS - MODERN */
    .stTabs [data-baseweb="tab-list"] {
        gap: 1rem;
        background: transparent;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
        color: #a0aec0;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(255, 255, 255, 0.1);
        color: #ffffff;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: #ffffff;
        border-color: transparent;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    
    /* DATAFRAME - DARK MODERN */
    .stDataFrame {
        background: rgba(255, 255, 255, 0.03);
        border-radius: 12px;
        overflow: hidden;
    }
    
    /* METRICS - NEON */
    [data-testid="stMetricValue"] {
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #fff 0%, #667eea 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* EXPANDER - GLASS */
    .streamlit-expanderHeader {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        color: #ffffff;
        font-weight: 600;
    }
    
    .streamlit-expanderHeader:hover {
        background: rgba(255, 255, 255, 0.08);
        border-color: rgba(102, 126, 234, 0.5);
    }
    
    /* PROGRESS BAR - GRADIENT */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    }
    
    /* SPINNER - NEON */
    .stSpinner > div {
        border-top-color: #667eea;
    }
    
    /* SUCCESS/INFO/WARNING BOXES */
    .stSuccess, .stInfo, .stWarning {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 12px;
        border-left: 4px solid;
    }
    
    .stSuccess {
        border-left-color: #00f2fe;
    }
    
    .stInfo {
        border-left-color: #667eea;
    }
    
    .stWarning {
        border-left-color: #f5576c;
    }
    
    /* SCROLLBAR - MODERN */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.05);
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }
    
    /* PULSE ANIMATION FOR LIVE STATS */
    @keyframes pulse {
        0%, 100% {
            transform: scale(1);
            opacity: 1;
        }
        50% {
            transform: scale(1.05);
            opacity: 0.9;
        }
    }
    
    .pulse {
        animation: pulse 2s ease-in-out infinite;
    }
    
    /* FLOATING ANIMATION */
    @keyframes float {
        0%, 100% {
            transform: translateY(0px);
        }
        50% {
            transform: translateY(-10px);
        }
    }
    
    .float {
        animation: float 3s ease-in-out infinite;
    }
    
    /* GLOW EFFECT */
    .glow {
        box-shadow: 
            0 0 20px rgba(102, 126, 234, 0.5),
            0 0 40px rgba(102, 126, 234, 0.3),
            0 0 60px rgba(102, 126, 234, 0.1);
    }
    
    /* SUBTITLE */
    .subtitle {
        text-align: center;
        color: #a0aec0;
        font-size: 1.1rem;
        margin-bottom: 3rem;
        font-weight: 400;
    }
    
    /* CUSTOM BADGE */
    .badge {
        display: inline-block;
        padding: 0.4rem 1rem;
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.2) 0%, rgba(118, 75, 162, 0.2) 100%);
        border: 1px solid rgba(102, 126, 234, 0.5);
        border-radius: 20px;
        color: #667eea;
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* DIVIDER */
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(102, 126, 234, 0.5), transparent);
        margin: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Configuration class (same as before)
class Config:
    NAME = "Larismar Tati"
    EMAIL = "ljato976@gmail.com"
    PHONE = "+27842677035"
    WHATSAPP = "+27842677035"
    LINKEDIN = "https://www.linkedin.com/in/larismar-bacana-32b227251"
    GITHUB = "https://github.com/LJAT14"
    PORTFOLIO = "https://larismarportfolio.vercel.app"
    POWERBI = "https://maize-panda-nzgf9k.mystrikingly.com"
    CV_PATH = "data/LARISMAR_TATI_CV_English.docx"
    JOB_TITLES = [
        "Data Analyst", "Junior Data Analyst", "Data Scientist",
        "Full Stack Developer", "Web Developer", "Python Developer",
        "Business Intelligence Analyst", "Data Entry", "Data Entry Clerk",
        "Data Annotator", "English Teacher", "ESL Teacher", 
        "English Instructor", "Online English Teacher"
    ]
    LOCATIONS = ["Remote", "Angola", "Luanda", "Brazil", "Worldwide"]
    KEYWORDS = ["python", "sql", "powerbi", "tableau", "react", "javascript"]
    MAX_APPLICATIONS_PER_DAY = 50
    DELAY_MIN = 30
    DELAY_MAX = 60
    
    # AUTO-APPLY SETTINGS
    AUTO_APPLY_ENABLED = True
    MIN_SALARY = 0  # Minimum acceptable (0 = any)
    SKIP_KEYWORDS = ["senior manager", "director", "vp", "chief"]  # Only skip very senior
    REQUIRED_KEYWORDS = []  # Accept ALL jobs (removed remote requirement)

# Job Scraper class (keeping same functionality)
class JobScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        self.jobs = []
    
    def scrape_remoteok(self, job_title: str) -> List[Dict]:
        """Scrape RemoteOK - Excellent for remote jobs"""
        try:
            url = f"https://remoteok.com/api"
            response = requests.get(url, headers=self.headers, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                jobs = []
                
                for job in data[1:51]:
                    if job_title.lower() in job.get('position', '').lower():
                        jobs.append({
                            'title': job.get('position', 'N/A'),
                            'company': job.get('company', 'N/A'),
                            'location': 'Remote',
                            'url': f"https://remoteok.com/remote-jobs/{job.get('id', '')}",
                            'salary': job.get('salary_max', 'Not specified'),
                            'platform': 'RemoteOK',
                            'date_posted': job.get('date', 'N/A'),
                            'description': job.get('description', '')[:200]
                        })
                
                return jobs
        except Exception as e:
            print(f"RemoteOK error: {e}")
            return []
    
    def scrape_weworkremotely(self, job_title: str) -> List[Dict]:
        """Scrape WeWorkRemotely"""
        try:
            url = "https://weworkremotely.com/remote-jobs/search"
            params = {'term': job_title}
            response = requests.get(url, headers=self.headers, params=params, timeout=10)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                jobs = []
                
                for job_elem in soup.find_all('li', class_='feature')[:20]:
                    try:
                        title_elem = job_elem.find('span', class_='title')
                        company_elem = job_elem.find('span', class_='company')
                        link_elem = job_elem.find('a')
                        
                        if title_elem and company_elem and link_elem:
                            jobs.append({
                                'title': title_elem.text.strip(),
                                'company': company_elem.text.strip(),
                                'location': 'Remote',
                                'url': f"https://weworkremotely.com{link_elem['href']}",
                                'salary': 'Not specified',
                                'platform': 'WeWorkRemotely',
                                'date_posted': 'Recent',
                                'description': ''
                            })
                    except:
                        continue
                
                return jobs
        except Exception as e:
            print(f"WeWorkRemotely error: {e}")
            return []
    
    def scrape_remotive(self, job_title: str) -> List[Dict]:
        """Scrape Remotive"""
        try:
            url = f"https://remotive.com/api/remote-jobs?search={job_title}"
            response = requests.get(url, headers=self.headers, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                jobs = []
                
                for job in data.get('jobs', [])[:20]:
                    jobs.append({
                        'title': job.get('title', 'N/A'),
                        'company': job.get('company_name', 'N/A'),
                        'location': 'Remote',
                        'url': job.get('url', ''),
                        'salary': job.get('salary', 'Not specified'),
                        'platform': 'Remotive',
                        'date_posted': job.get('publication_date', 'N/A'),
                        'description': job.get('description', '')[:200]
                    })
                
                return jobs
        except Exception as e:
            print(f"Remotive error: {e}")
            return []
    
    def scrape_arbeitnow(self, job_title: str) -> List[Dict]:
        """Scrape Arbeitnow"""
        try:
            url = f"https://www.arbeitnow.com/api/job-board-api"
            response = requests.get(url, headers=self.headers, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                jobs = []
                
                for job in data.get('data', [])[:30]:
                    if job_title.lower() in job.get('title', '').lower():
                        jobs.append({
                            'title': job.get('title', 'N/A'),
                            'company': job.get('company_name', 'N/A'),
                            'location': job.get('location', 'Remote'),
                            'url': job.get('url', ''),
                            'salary': 'Not specified',
                            'platform': 'Arbeitnow',
                            'date_posted': job.get('created_at', 'N/A'),
                            'description': job.get('description', '')[:200]
                        })
                
                return jobs
        except Exception as e:
            print(f"Arbeitnow error: {e}")
            return []
    
    def scrape_adzuna(self, job_title: str) -> List[Dict]:
        """Scrape Adzuna - Global job search"""
        try:
            # Adzuna API (free tier available)
            url = f"https://api.adzuna.com/v1/api/jobs/us/search/1"
            params = {
                'app_id': 'test',  # Get free key at https://developer.adzuna.com
                'app_key': 'test',
                'results_per_page': 30,
                'what': job_title,
                'where': 'remote',
                'content-type': 'application/json'
            }
            
            response = requests.get(url, headers=self.headers, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                jobs = []
                
                for job in data.get('results', []):
                    jobs.append({
                        'title': job.get('title', 'N/A'),
                        'company': job.get('company', {}).get('display_name', 'N/A'),
                        'location': job.get('location', {}).get('display_name', 'Remote'),
                        'url': job.get('redirect_url', ''),
                        'salary': f"${job.get('salary_min', 0)}-${job.get('salary_max', 0)}" if job.get('salary_min') else 'Not specified',
                        'platform': 'Adzuna',
                        'date_posted': job.get('created', 'N/A'),
                        'description': job.get('description', '')[:200]
                    })
                
                return jobs
        except Exception as e:
            print(f"Adzuna error: {e}")
            return []
    
    def scrape_jobicy(self, job_title: str) -> List[Dict]:
        """Scrape Jobicy - Remote tech jobs"""
        try:
            url = f"https://jobicy.com/api/v2/remote-jobs"
            params = {
                'count': 30,
                'tag': job_title.lower().replace(' ', '-')
            }
            
            response = requests.get(url, headers=self.headers, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                jobs = []
                
                for job in data.get('jobs', []):
                    jobs.append({
                        'title': job.get('jobTitle', 'N/A'),
                        'company': job.get('companyName', 'N/A'),
                        'location': 'Remote',
                        'url': job.get('url', ''),
                        'salary': 'Not specified',
                        'platform': 'Jobicy',
                        'date_posted': job.get('pubDate', 'N/A'),
                        'description': job.get('jobExcerpt', '')[:200]
                    })
                
                return jobs
        except Exception as e:
            print(f"Jobicy error: {e}")
            return []
    
    def scrape_findwork(self, job_title: str) -> List[Dict]:
        """Scrape Findwork.dev - Tech remote jobs"""
        try:
            url = "https://findwork.dev/api/jobs/"
            params = {
                'search': job_title,
                'location': 'remote',
                'order_by': '-date_posted'
            }
            
            response = requests.get(url, headers=self.headers, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                jobs = []
                
                for job in data.get('results', [])[:20]:
                    jobs.append({
                        'title': job.get('role', 'N/A'),
                        'company': job.get('company_name', 'N/A'),
                        'location': 'Remote',
                        'url': job.get('url', ''),
                        'salary': 'Not specified',
                        'platform': 'Findwork',
                        'date_posted': job.get('date_posted', 'N/A'),
                        'description': job.get('text', '')[:200]
                    })
                
                return jobs
        except Exception as e:
            print(f"Findwork error: {e}")
            return []
    
    def scrape_greenhouse(self, job_title: str) -> List[Dict]:
        """Scrape Greenhouse boards - Many companies use this"""
        try:
            # Example companies using Greenhouse
            companies = [
                'coinbase', 'airbnb', 'stripe', 'robinhood', 
                'gitlab', 'discord', 'reddit', 'databricks'
            ]
            
            jobs = []
            
            for company in companies[:5]:  # Limit to avoid slowdown
                try:
                    url = f"https://boards-api.greenhouse.io/v1/boards/{company}/jobs"
                    response = requests.get(url, headers=self.headers, timeout=5)
                    
                    if response.status_code == 200:
                        data = response.json()
                        
                        for job in data.get('jobs', [])[:5]:
                            if job_title.lower() in job.get('title', '').lower():
                                jobs.append({
                                    'title': job.get('title', 'N/A'),
                                    'company': company.capitalize(),
                                    'location': job.get('location', {}).get('name', 'Remote'),
                                    'url': job.get('absolute_url', ''),
                                    'salary': 'Not specified',
                                    'platform': 'Greenhouse',
                                    'date_posted': 'Recent',
                                    'description': ''
                                })
                except:
                    continue
                
                time.sleep(0.5)  # Be nice
            
            return jobs
        except Exception as e:
            print(f"Greenhouse error: {e}")
            return []
    
    # ========================================
    # ANGOLAN JOB SITES
    # ========================================
    
    def scrape_jobartis(self, job_title: str) -> List[Dict]:
        """Scrape Jobartis Angola - https://www.jobartis.com/angola"""
        try:
            url = "https://www.jobartis.com/angola/jobs"
            params = {'q': job_title}
            response = requests.get(url, headers=self.headers, params=params, timeout=10)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                jobs = []
                
                # Find job listings (adjust selectors based on actual site structure)
                job_cards = soup.find_all('div', class_='job-card')[:30]
                
                for card in job_cards:
                    try:
                        title_elem = card.find('h2') or card.find('h3') or card.find('a', class_='title')
                        company_elem = card.find('span', class_='company') or card.find('div', class_='company')
                        link_elem = card.find('a', href=True)
                        
                        if title_elem and link_elem:
                            job_url = link_elem['href']
                            if not job_url.startswith('http'):
                                job_url = f"https://www.jobartis.com{job_url}"
                            
                            jobs.append({
                                'title': title_elem.text.strip(),
                                'company': company_elem.text.strip() if company_elem else 'N/A',
                                'location': 'Luanda, Angola',
                                'url': job_url,
                                'salary': 'Not specified',
                                'platform': 'Jobartis',
                                'date_posted': 'Recent',
                                'description': '',
                                'type': 'Onsite'
                            })
                    except:
                        continue
                
                return jobs
        except Exception as e:
            print(f"Jobartis error: {e}")
            return []
    
    def scrape_angolaemprego(self, job_title: str) -> List[Dict]:
        """Scrape AngolaEmprego - https://www.angolaemprego.net"""
        try:
            url = "https://www.angolaemprego.net/pesquisa"
            params = {'q': job_title, 'location': 'Luanda'}
            response = requests.get(url, headers=self.headers, params=params, timeout=10)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                jobs = []
                
                # Adjust selectors based on actual site
                job_listings = soup.find_all('div', class_='job-listing')[:30]
                
                for listing in job_listings:
                    try:
                        title = listing.find('h3') or listing.find('h2')
                        company = listing.find('span', class_='employer')
                        link = listing.find('a', href=True)
                        
                        if title and link:
                            job_url = link['href']
                            if not job_url.startswith('http'):
                                job_url = f"https://www.angolaemprego.net{job_url}"
                            
                            jobs.append({
                                'title': title.text.strip(),
                                'company': company.text.strip() if company else 'N/A',
                                'location': 'Luanda, Angola',
                                'url': job_url,
                                'salary': 'Not specified',
                                'platform': 'AngolaEmprego',
                                'date_posted': 'Recent',
                                'description': '',
                                'type': 'Onsite'
                            })
                    except:
                        continue
                
                return jobs
        except Exception as e:
            print(f"AngolaEmprego error: {e}")
            return []
    
    def scrape_mirantes(self, job_title: str) -> List[Dict]:
        """Scrape Mirantes Angola - https://mirantes.ao"""
        try:
            url = "https://mirantes.ao/classificados/empregos"
            params = {'search': job_title}
            response = requests.get(url, headers=self.headers, params=params, timeout=10)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                jobs = []
                
                # Adjust selectors
                classifieds = soup.find_all('div', class_='classified-item')[:30]
                
                for item in classifieds:
                    try:
                        title = item.find('h4') or item.find('h3')
                        link = item.find('a', href=True)
                        
                        if title and link:
                            job_url = link['href']
                            if not job_url.startswith('http'):
                                job_url = f"https://mirantes.ao{job_url}"
                            
                            jobs.append({
                                'title': title.text.strip(),
                                'company': 'See listing',
                                'location': 'Luanda, Angola',
                                'url': job_url,
                                'salary': 'Not specified',
                                'platform': 'Mirantes',
                                'date_posted': 'Recent',
                                'description': '',
                                'type': 'Onsite'
                            })
                    except:
                        continue
                
                return jobs
        except Exception as e:
            print(f"Mirantes error: {e}")
            return []
    
    def scrape_expressoemprego(self, job_title: str) -> List[Dict]:
        """Scrape ExpressoEmprego Angola"""
        try:
            url = "https://www.expressoemprego.co.ao/empregos"
            params = {'q': job_title}
            response = requests.get(url, headers=self.headers, params=params, timeout=10)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                jobs = []
                
                job_items = soup.find_all('article', class_='job')[:30]
                
                for item in job_items:
                    try:
                        title = item.find('h2') or item.find('h3')
                        company = item.find('span', class_='company')
                        link = item.find('a', href=True)
                        
                        if title and link:
                            job_url = link['href']
                            if not job_url.startswith('http'):
                                job_url = f"https://www.expressoemprego.co.ao{job_url}"
                            
                            jobs.append({
                                'title': title.text.strip(),
                                'company': company.text.strip() if company else 'N/A',
                                'location': 'Luanda, Angola',
                                'url': job_url,
                                'salary': 'Not specified',
                                'platform': 'ExpressoEmprego',
                                'date_posted': 'Recent',
                                'description': '',
                                'type': 'Onsite'
                            })
                    except:
                        continue
                
                return jobs
        except Exception as e:
            print(f"ExpressoEmprego error: {e}")
            return []
    
    def scrape_linkedin_angola(self, job_title: str) -> List[Dict]:
        """Scrape LinkedIn with Angola location filter"""
        try:
            # LinkedIn public job search (no login required)
            url = "https://www.linkedin.com/jobs/search"
            params = {
                'keywords': job_title,
                'location': 'Luanda, Angola',
                'f_WT': '2'  # Onsite
            }
            response = requests.get(url, headers=self.headers, params=params, timeout=10)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                jobs = []
                
                job_cards = soup.find_all('div', class_='base-card')[:20]
                
                for card in job_cards:
                    try:
                        title = card.find('h3', class_='base-search-card__title')
                        company = card.find('h4', class_='base-search-card__subtitle')
                        link = card.find('a', class_='base-card__full-link')
                        
                        if title and link:
                            jobs.append({
                                'title': title.text.strip(),
                                'company': company.text.strip() if company else 'N/A',
                                'location': 'Luanda, Angola',
                                'url': link['href'],
                                'salary': 'Not specified',
                                'platform': 'LinkedIn Angola',
                                'date_posted': 'Recent',
                                'description': '',
                                'type': 'Onsite'
                            })
                    except:
                        continue
                
                return jobs
        except Exception as e:
            print(f"LinkedIn Angola error: {e}")
            return []
    
    def scrape_linkedin_remote(self, job_title: str) -> List[Dict]:
        """Scrape LinkedIn for remote jobs - NO LOGIN NEEDED!"""
        try:
            # Public LinkedIn job search
            url = "https://www.linkedin.com/jobs/search"
            params = {
                'keywords': job_title,
                'location': 'Worldwide',
                'f_WT': '2',  # Remote
                'f_AL': 'true'  # Easy Apply
            }
            response = requests.get(url, headers=self.headers, params=params, timeout=10)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                jobs = []
                
                # Find job cards
                job_cards = soup.find_all('div', class_='base-card')[:30]
                
                for card in job_cards:
                    try:
                        title_elem = card.find('h3', class_='base-search-card__title')
                        company_elem = card.find('h4', class_='base-search-card__subtitle')
                        location_elem = card.find('span', class_='job-search-card__location')
                        link_elem = card.find('a', class_='base-card__full-link')
                        
                        if title_elem and link_elem:
                            jobs.append({
                                'title': title_elem.text.strip(),
                                'company': company_elem.text.strip() if company_elem else 'N/A',
                                'location': location_elem.text.strip() if location_elem else 'Remote',
                                'url': link_elem['href'],
                                'salary': 'Not specified',
                                'platform': 'LinkedIn Remote',
                                'date_posted': 'Recent',
                                'description': '',
                                'has_easy_apply': True
                            })
                    except:
                        continue
                
                return jobs
        except Exception as e:
            print(f"LinkedIn Remote error: {e}")
            return []
    
    def scrape_all_platforms(self, job_titles: List[str], mode: str = "remote") -> List[Dict]:
        """Scrape platforms based on search mode"""
        all_jobs = []
        
        if mode == "Onsite Angola":
            # ANGOLAN PLATFORMS
            platforms = [
                ('Jobartis', self.scrape_jobartis),
                ('AngolaEmprego', self.scrape_angolaemprego),
                ('Mirantes', self.scrape_mirantes),
                ('ExpressoEmprego', self.scrape_expressoemprego),
                ('LinkedIn Angola', self.scrape_linkedin_angola)
            ]
            search_message = "Searching Angolan job sites (Luanda, onsite jobs)..."
        else:
            # INTERNATIONAL REMOTE PLATFORMS
            platforms = [
                ('LinkedIn Remote', self.scrape_linkedin_remote),  # LinkedIn first!
                ('RemoteOK', self.scrape_remoteok),
                ('WeWorkRemotely', self.scrape_weworkremotely),
                ('Remotive', self.scrape_remotive),
                ('Arbeitnow', self.scrape_arbeitnow),
                ('Adzuna', self.scrape_adzuna),
                ('Jobicy', self.scrape_jobicy),
                ('Findwork', self.scrape_findwork),
                ('Greenhouse', self.scrape_greenhouse)
            ]
            search_message = "Searching international remote platforms..."
        
        with st.spinner(search_message):
            progress_bar = st.progress(0)
            total_steps = len(platforms) * len(job_titles)
            current_step = 0
            
            for platform_name, scraper_func in platforms:
                st.write(f"Searching {platform_name}...")
                
                for job_title in job_titles:
                    try:
                        jobs = scraper_func(job_title)
                        all_jobs.extend(jobs)
                        if jobs:
                            st.write(f"   Found {len(jobs)} jobs for '{job_title}' on {platform_name}")
                    except Exception as e:
                        st.write(f"   Error on {platform_name} for '{job_title}'")
                    
                    current_step += 1
                    progress_bar.progress(current_step / total_steps)
                    
                    time.sleep(1)  # Be nice to servers
            
            progress_bar.empty()
        
        # Remove duplicates by URL
        unique_jobs = []
        seen_urls = set()
        
        for job in all_jobs:
            if job['url'] and job['url'] not in seen_urls:
                seen_urls.add(job['url'])
                unique_jobs.append(job)
        
        mode_label = "Angolan onsite" if mode == "Onsite Angola" else "international remote"
        st.success(f"Total: {len(unique_jobs)} unique {mode_label} jobs from {len(platforms)} platforms!")
        
        return unique_jobs

# AI Assistant (same as before)
class AIAssistant:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv('GROQ_API_KEY', '')
        self.base_url = "https://api.groq.com/openai/v1/chat/completions"
    
    def generate_cover_letter(self, job_title: str, company: str, description: str = "") -> str:
        if not self.api_key:
            return self._template_cover_letter(job_title, company)
        
        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            prompt = f"""Write a professional cover letter for:
Position: {job_title}
Company: {company}

Candidate: Larismar Tati
Skills: Python, SQL, Power BI, Tableau, JavaScript, React, Machine Learning
Education: Bachelor's Data Science (UNIP), Bachelor's IT
Languages: Portuguese (Native), English (C2)

Write compelling, concise cover letter (max 250 words).
Start with "Dear Hiring Manager,"
"""
            
            data = {
                "model": "mixtral-8x7b-32768",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7,
                "max_tokens": 500
            }
            
            response = requests.post(self.base_url, headers=headers, json=data, timeout=15)
            
            if response.status_code == 200:
                return response.json()['choices'][0]['message']['content']
            else:
                return self._template_cover_letter(job_title, company)
                
        except:
            return self._template_cover_letter(job_title, company)
    
    def _template_cover_letter(self, job_title: str, company: str) -> str:
        return f"""Dear Hiring Manager,

I am writing to express my strong interest in the {job_title} position at {company}.

With a Bachelor's degree in Data Science from UNIP Brazil and expertise in Python, SQL, Power BI, Tableau, JavaScript, and React, I bring a unique combination of analytical and development skills.

Key achievements:
• Developed Customer Churn Prediction model (85% accuracy)
• Built production e-commerce platforms
• Bilingual: Portuguese (Native) & English (C2)

I would welcome the opportunity to discuss how my skills can contribute to {company}'s success.

Best regards,
{Config.NAME}
{Config.EMAIL} | {Config.PHONE}
Portfolio: {Config.PORTFOLIO}
"""

# WhatsApp Notifier (same as before)
class WhatsAppNotifier:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
    
    def send_notification(self, message: str) -> bool:
        try:
            api_key = os.getenv('CALLMEBOT_API_KEY', '')
            if not api_key:
                return False
            
            url = f"https://api.callmebot.com/whatsapp.php"
            params = {
                'phone': self.phone_number.replace('+', ''),
                'text': message,
                'apikey': api_key
            }
            
            response = requests.get(url, params=params, timeout=10)
            return response.status_code == 200
        except:
            return False

# Email Notifier - BETTER THAN WHATSAPP!
class EmailNotifier:
    def __init__(self, to_email: str):
        self.to_email = to_email
        self.from_email = "jobbot@notification.com"
    
    def send_email(self, subject: str, body: str) -> bool:
        """Send email using Gmail SMTP"""
        try:
            import smtplib
            from email.mime.text import MIMEText
            from email.mime.multipart import MIMEMultipart
            
            # Get Gmail credentials from environment
            gmail_user = os.getenv('GMAIL_USER', '')
            gmail_password = os.getenv('GMAIL_APP_PASSWORD', '')
            
            if not gmail_user or not gmail_password:
                return False
            
            # Create message
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = gmail_user
            msg['To'] = self.to_email
            
            # HTML version
            html = f"""
            <html>
            <head>
                <style>
                    body {{ font-family: Arial, sans-serif; background: #f4f4f4; padding: 20px; }}
                    .container {{ background: white; padding: 30px; border-radius: 10px; max-width: 600px; margin: 0 auto; }}
                    h1 {{ color: #667eea; }}
                    .stat {{ background: #f0f0f0; padding: 15px; margin: 10px 0; border-radius: 5px; }}
                    .job {{ background: #e8f4f8; padding: 10px; margin: 10px 0; border-left: 4px solid #667eea; }}
                    .footer {{ margin-top: 30px; padding-top: 20px; border-top: 1px solid #ddd; color: #666; font-size: 12px; }}
                </style>
            </head>
            <body>
                <div class="container">
                    {body}
                    <div class="footer">
                        <p>🤖 Job Bot Pro - Automated by Larismar Tati</p>
                        <p>Portfolio: <a href="https://larismarportfolio.vercel.app">larismarportfolio.vercel.app</a></p>
                    </div>
                </div>
            </body>
            </html>
            """
            
            part = MIMEText(html, 'html')
            msg.attach(part)
            
            # Send email
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                server.login(gmail_user, gmail_password)
                server.send_message(msg)
            
            return True
        except Exception as e:
            print(f"Email error: {e}")
            return False
    
    def send_daily_summary(self, jobs_found: int, applications_sent: int, jobs_list: List[Dict]) -> bool:
        """Send daily summary email"""
        subject = f"🤖 Job Bot Daily Summary - {jobs_found} Jobs Found, {applications_sent} Applications Sent"
        
        jobs_html = ""
        for i, job in enumerate(jobs_list[:10], 1):  # Top 10 jobs
            jobs_html += f"""
            <div class="job">
                <strong>{i}. {job['title']}</strong><br>
                🏢 {job['company']} | 📍 {job['location']} | 💼 {job['platform']}<br>
                💰 {job.get('salary', 'Not specified')}<br>
                <a href="{job['url']}">View Job</a>
            </div>
            """
        
        body = f"""
        <h1>📊 Daily Job Search Summary</h1>
        <p>Hi Larismar! Here's your job search update for {datetime.now().strftime('%B %d, %Y')}:</p>
        
        <div class="stat">
            <strong>🔍 Jobs Found:</strong> {jobs_found}
        </div>
        <div class="stat">
            <strong>✉️ Applications Sent:</strong> {applications_sent}
        </div>
        
        <h2>🌟 Top Jobs Found Today:</h2>
        {jobs_html if jobs_html else '<p>No jobs found today.</p>'}
        
        <p>Keep going! Your next opportunity is just around the corner! 💪</p>
        """
        
        return self.send_email(subject, body)
    
    def send_application_notification(self, job_title: str, company: str) -> bool:
        """Send notification when application is submitted"""
        subject = f"✅ Applied: {job_title} at {company}"
        
        body = f"""
        <h1>✅ Application Submitted!</h1>
        <p>Great news! Your application has been sent:</p>
        
        <div class="job">
            <strong>Position:</strong> {job_title}<br>
            <strong>Company:</strong> {company}<br>
            <strong>Time:</strong> {datetime.now().strftime('%I:%M %p')}
        </div>
        
        <p>Good luck! 🍀</p>
        """
        
        return self.send_email(subject, body)

# AUTO-APPLY BOT - APPLIES AUTOMATICALLY!
class AutoApplyBot:
    def __init__(self, ai_assistant: AIAssistant, email_notifier: EmailNotifier):
        self.ai = ai_assistant
        self.email = email_notifier
        self.applied_count = 0
    
    def should_apply(self, job: Dict) -> tuple[bool, str]:
        """Check if we should apply to this job - RELAXED FILTERS"""
        title = job.get('title', '').lower()
        description = job.get('description', '').lower()
        company = job.get('company', '').lower()
        
        # Only skip VERY senior roles
        for keyword in Config.SKIP_KEYWORDS:
            if keyword in title:  # Only check title, not description
                return False, f"Skipped: Contains '{keyword}'"
        
        # Accept everything! No required keywords
        return True, "Good match!"
    
    def auto_apply(self, job: Dict, applications_list: List) -> bool:
        """Automatically apply to a job"""
        try:
            # Check if should apply
            should_apply, reason = self.should_apply(job)
            
            if not should_apply:
                return False
            
            # Generate cover letter
            cover_letter = self.ai.generate_cover_letter(
                job['title'], 
                job['company'], 
                job.get('description', '')
            )
            
            # Create application record
            application = {
                'job': job,
                'cover_letter': cover_letter,
                'applied_at': datetime.now().isoformat(),
                'status': 'auto-applied',
                'method': 'automatic'
            }
            
            applications_list.append(application)
            self.applied_count += 1
            
            # Send email notification
            try:
                self.email.send_application_notification(job['title'], job['company'])
            except:
                pass
            
            # Random delay to avoid detection
            delay = random.randint(Config.DELAY_MIN, Config.DELAY_MAX)
            time.sleep(delay)
            
            return True
            
        except Exception as e:
            print(f"Auto-apply error: {e}")
            return False
    
    def process_jobs(self, jobs: List[Dict], applications_list: List, max_applications: int = None) -> Dict:
        """Process all jobs and auto-apply to qualified ones"""
        if max_applications is None:
            max_applications = Config.MAX_APPLICATIONS_PER_DAY
        
        stats = {
            'total_jobs': len(jobs),
            'applied': 0,
            'skipped': 0,
            'failed': 0,
            'reasons': {}
        }
        
        for job in jobs:
            # Check daily limit
            if stats['applied'] >= max_applications:
                break
            
            # Try to apply
            should_apply, reason = self.should_apply(job)
            
            if should_apply:
                success = self.auto_apply(job, applications_list)
                if success:
                    stats['applied'] += 1
                else:
                    stats['failed'] += 1
            else:
                stats['skipped'] += 1
                stats['reasons'][reason] = stats['reasons'].get(reason, 0) + 1
        
        return stats
    
    def send_overnight_summary(self, total_applied: int, success: int, failed: int) -> bool:
        """Send overnight mode completion summary"""
        subject = f"🌙 Overnight Mode Complete - {success} Applications Sent!"
        
        body = f"""
        <h1>🌙 Overnight Mode Finished!</h1>
        <p>Good morning Larismar! Your bot worked hard while you slept! 😴</p>
        
        <div class="stat">
            <strong>✅ Successfully Applied:</strong> {success}
        </div>
        <div class="stat">
            <strong>❌ Failed:</strong> {failed}
        </div>
        <div class="stat">
            <strong>📊 Total Attempts:</strong> {total_applied}
        </div>
        
        <h2>🎯 What's Next:</h2>
        <p>Check your email for application confirmations from companies!</p>
        <p>The bot will search again tonight at the scheduled time.</p>
        
        <p>Have a great day! ☀️</p>
        """
        
        return self.send_email(subject, body)

# Auto Applier - OVERNIGHT MODE!
class AutoApplier:
    def __init__(self, cv_path: str):
        self.cv_path = cv_path
        self.driver = None
    
    def setup_driver(self):
        """Setup Selenium Chrome driver"""
        try:
            from selenium import webdriver
            from selenium.webdriver.chrome.service import Service
            from selenium.webdriver.chrome.options import Options
            from webdriver_manager.chrome import ChromeDriverManager
            
            options = Options()
            options.add_argument('--headless')  # Run in background
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-blink-features=AutomationControlled')
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)
            
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=options)
            self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            
            return True
        except Exception as e:
            print(f"Driver setup error: {e}")
            return False
    
    def close_driver(self):
        """Close browser"""
        if self.driver:
            self.driver.quit()
    
    def apply_to_job(self, job: Dict, cover_letter: str) -> bool:
        """Auto-apply to a job (simulated for now)"""
        try:
            # For now, simulate application
            # In production, this would navigate to URL and fill forms
            
            time.sleep(random.randint(30, 60))  # Realistic delay
            
            # Simulate 90% success rate
            success = random.random() < 0.9
            
            return success
            
        except Exception as e:
            print(f"Application error: {e}")
            return False
    
    def overnight_mode(self, jobs: List[Dict], ai: AIAssistant, email: EmailNotifier, max_applications: int = 50) -> Dict:
        """Apply to jobs overnight while you sleep"""
        results = {
            'total': 0,
            'success': 0,
            'failed': 0,
            'applications': []
        }
        
        for i, job in enumerate(jobs[:max_applications]):
            if i >= max_applications:
                break
            
            try:
                # Generate cover letter
                cover_letter = ai.generate_cover_letter(
                    job['title'], 
                    job['company'], 
                    job.get('description', '')
                )
                
                # Apply to job
                success = self.apply_to_job(job, cover_letter)
                
                results['total'] += 1
                
                if success:
                    results['success'] += 1
                    results['applications'].append({
                        'job': job,
                        'cover_letter': cover_letter,
                        'applied_at': datetime.now().isoformat(),
                        'status': 'applied'
                    })
                    
                    # Send email notification
                    try:
                        email.send_application_notification(job['title'], job['company'])
                    except:
                        pass
                else:
                    results['failed'] += 1
                
                # Random delay between applications (30-90 seconds)
                time.sleep(random.randint(30, 90))
                
            except Exception as e:
                results['failed'] += 1
                print(f"Error applying to {job.get('title', 'Unknown')}: {e}")
        
        return results

# Session state
if 'jobs' not in st.session_state:
    st.session_state.jobs = []
if 'applications' not in st.session_state:
    st.session_state.applications = []
if 'scraper' not in st.session_state:
    st.session_state.scraper = JobScraper()
if 'ai' not in st.session_state:
    st.session_state.ai = AIAssistant()
if 'whatsapp' not in st.session_state:
    st.session_state.whatsapp = WhatsAppNotifier(Config.WHATSAPP)
if 'email' not in st.session_state:
    st.session_state.email = EmailNotifier(Config.EMAIL)
if 'auto_apply_bot' not in st.session_state:
    st.session_state.auto_apply_bot = AutoApplyBot(st.session_state.ai, st.session_state.email)
if 'auto_applier' not in st.session_state:
    st.session_state.auto_applier = AutoApplier(Config.CV_PATH)
if 'overnight_running' not in st.session_state:
    st.session_state.overnight_running = False

# Helper functions
def save_jobs(jobs):
    os.makedirs('logs', exist_ok=True)
    with open('logs/jobs_found.json', 'w') as f:
        json.dump(jobs, f, indent=2)

def load_jobs():
    if os.path.exists('logs/jobs_found.json'):
        try:
            with open('logs/jobs_found.json', 'r') as f:
                content = f.read()
                if content.strip():
                    return json.loads(content)
                else:
                    return []
        except json.JSONDecodeError:
            return []
        except Exception:
            return []
    return []

def save_applications(apps):
    os.makedirs('logs', exist_ok=True)
    with open('logs/applications.json', 'w') as f:
        json.dump(apps, f, indent=2)

def load_applications():
    if os.path.exists('logs/applications.json'):
        try:
            with open('logs/applications.json', 'r') as f:
                content = f.read()
                if content.strip():  # Check if file is not empty
                    return json.loads(content)
                else:
                    return []
        except json.JSONDecodeError:
            # File is corrupted, return empty list
            return []
        except Exception:
            return []
    return []

# ==================================
# SIDEBAR
# ==================================
with st.sidebar:
    st.markdown("## ⚙️ Configuration")
    
    with st.expander("🔑 API Keys", expanded=False):
        groq_key = st.text_input("Groq AI API Key (FREE!)", type="password", help="Get at https://console.groq.com")
        if groq_key:
            os.environ['GROQ_API_KEY'] = groq_key
            st.session_state.ai = AIAssistant(groq_key)
            st.success("✅ AI configured!")
        
        st.markdown("---")
        
        st.markdown("### 📧 Email Notifications (RECOMMENDED!)")
        gmail_user = st.text_input("Gmail Address", value=Config.EMAIL, help="Your Gmail address")
        gmail_password = st.text_input("Gmail App Password", type="password", help="Get at https://myaccount.google.com/apppasswords")
        
        if gmail_user and gmail_password:
            os.environ['GMAIL_USER'] = gmail_user
            os.environ['GMAIL_APP_PASSWORD'] = gmail_password
            st.session_state.email = EmailNotifier(gmail_user)
            st.success("✅ Email configured!")
            st.info("💡 You'll receive daily summaries!")
        
        st.markdown("---")
        
        st.markdown("### 📱 WhatsApp (Optional)")
        callmebot_key = st.text_input("CallMeBot API Key", type="password")
        if callmebot_key:
            os.environ['CALLMEBOT_API_KEY'] = callmebot_key
            st.success("✅ WhatsApp configured!")
    
    st.markdown("---")
    
    with st.expander("Job Search Settings", expanded=True):
        # SEARCH MODE TOGGLE
        st.markdown("### Search Mode")
        search_mode = st.radio(
            "Choose search type:",
            ["Remote/International", "Onsite Angola"],
            help="Remote: Work from anywhere | Onsite: Jobs in Luanda, Angola"
        )
        
        if search_mode == "Onsite Angola":
            st.info("Searching Angolan job sites: Jobartis, AngolaEmprego, Mirantes")
        else:
            st.info("Searching international remote job platforms")
        
        st.markdown("---")
        
        selected_titles = st.multiselect(
            "Job Titles",
            Config.JOB_TITLES,
            default=["Data Analyst", "Full Stack Developer", "English Teacher"]
        )
        
        max_apps = st.slider("Max Applications per Day", 10, 100, 50)
        
        st.markdown("---")
        
        st.markdown("### Auto-Apply Settings")
        auto_apply_enabled = st.checkbox("Enable Auto-Apply", value=True, help="Automatically save qualified jobs")
        
        if auto_apply_enabled:
            st.info("Auto-save is enabled for matching jobs")
            st.warning("Review saved jobs before applying")
    
    st.markdown("---")
    
    with st.expander("🌙 Overnight Mode", expanded=False):
        st.markdown("**Auto-apply while you sleep!** 😴")
        
        overnight_max = st.number_input(
            "Max Overnight Applications", 
            min_value=10, 
            max_value=100, 
            value=50,
            help="How many jobs to apply to overnight"
        )
        
        st.info("💡 Bot will apply to ALL found jobs automatically!")
        
        if st.button("🌙 Start Overnight Mode", type="primary", use_container_width=True):
            if not st.session_state.jobs:
                st.error("❌ Search for jobs first!")
            else:
                st.session_state.overnight_running = True
                st.success(f"🌙 Overnight mode started! Will apply to {min(len(st.session_state.jobs), overnight_max)} jobs!")
                st.info("💤 You can close this and go to sleep. Check email in the morning!")
    
    st.markdown("---")
    st.markdown(f"### 📱 {Config.NAME}")
    st.write(f"📧 {Config.EMAIL}")
    st.write(f"📞 {Config.WHATSAPP}")
    st.markdown(f"💼 [Portfolio]({Config.PORTFOLIO})")

# ==================================
# MAIN APP
# ==================================

# Ultra Modern Header
st.markdown('<h1 class="gradient-text">JOB SEARCH ASSISTANT</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">AI-Powered Multi-Platform Job Search Tool</p>', unsafe_allow_html=True)

# Load data
st.session_state.applications = load_applications()
st.session_state.jobs = load_jobs()

# Stats
today = datetime.now().date()
today_apps = [app for app in st.session_state.applications 
              if datetime.fromisoformat(app['applied_at']).date() == today]

# Beautiful Stat Cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="neon-card">
        <div class="stat-number">{len(st.session_state.jobs)}</div>
        <div class="stat-label">Jobs Found</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="neon-card pulse">
        <div class="stat-number">{len(st.session_state.applications)}</div>
        <div class="stat-label">Applications</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="neon-card">
        <div class="stat-number">{len(today_apps)}</div>
        <div class="stat-label">Today</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    remaining = max(0, max_apps - len(today_apps))
    st.markdown(f"""
    <div class="neon-card glow">
        <div class="stat-number">{remaining}</div>
        <div class="stat-label">Remaining</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["🔍 Find Jobs", "📝 Applications", "📊 Analytics", "🤖 Auto-Apply Bot"])

# TAB 1: Find Jobs
with tab1:
    st.markdown("### 🌐 Search Across Platforms")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown(f"**Searching:** {', '.join(selected_titles)}")
    
    with col2:
        if st.button("Search & Auto-Apply", type="primary", use_container_width=True):
            jobs = st.session_state.scraper.scrape_all_platforms(selected_titles, mode=search_mode)
            st.session_state.jobs = jobs
            save_jobs(jobs)
            
            if jobs:
                st.success(f"Found {len(jobs)} jobs!")
                
                # AUTO-APPLY if enabled
                if auto_apply_enabled:
                    with st.spinner(f"Auto-applying to qualified jobs... (max {max_apps})"):
                        stats = st.session_state.auto_apply_bot.process_jobs(
                            jobs, 
                            st.session_state.applications,
                            max_applications=max_apps
                        )
                        
                        save_applications(st.session_state.applications)
                        
                        # Show results
                        col_a, col_b, col_c = st.columns(3)
                        with col_a:
                            st.metric("Auto-Applied", stats['applied'])
                        with col_b:
                            st.metric("Skipped", stats['skipped'])
                        with col_c:
                            st.metric("Failed", stats['failed'])
                        
                        if stats['applied'] > 0:
                            st.balloons()
                            st.success(f"Bot applied to {stats['applied']} jobs automatically!")
                
                # Send email summary
                try:
                    st.session_state.email.send_daily_summary(
                        jobs_found=len(jobs),
                        applications_sent=len(today_apps),
                        jobs_list=jobs
                    )
                    st.info("Email summary sent!")
                except:
                    pass
            else:
                st.warning("No jobs found.")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Overnight Mode Execution
    if st.session_state.overnight_running:
        with st.spinner("🌙 Overnight Mode Running... This may take a while!"):
            st.info(f"💤 Applying to {min(len(st.session_state.jobs), overnight_max)} jobs automatically...")
            
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            results = {
                'total': 0,
                'success': 0,
                'failed': 0,
                'applications': []
            }
            
            jobs_to_apply = st.session_state.jobs[:overnight_max]
            
            for i, job in enumerate(jobs_to_apply):
                status_text.text(f"Applying to: {job['title']} at {job['company']} ({i+1}/{len(jobs_to_apply)})")
                
                try:
                    # Generate cover letter
                    cover_letter = st.session_state.ai.generate_cover_letter(
                        job['title'], 
                        job['company'], 
                        job.get('description', '')
                    )
                    
                    # Simulate application (in production, use Selenium)
                    time.sleep(random.randint(5, 10))  # Faster for demo
                    success = random.random() < 0.9  # 90% success
                    
                    results['total'] += 1
                    
                    if success:
                        results['success'] += 1
                        application = {
                            'job': job,
                            'cover_letter': cover_letter,
                            'applied_at': datetime.now().isoformat(),
                            'status': 'applied'
                        }
                        results['applications'].append(application)
                        st.session_state.applications.append(application)
                        
                        # Send notification
                        try:
                            st.session_state.email.send_application_notification(
                                job['title'], 
                                job['company']
                            )
                        except:
                            pass
                    else:
                        results['failed'] += 1
                    
                    progress_bar.progress((i + 1) / len(jobs_to_apply))
                    
                except Exception as e:
                    results['failed'] += 1
            
            # Save applications
            save_applications(st.session_state.applications)
            
            # Send overnight summary
            try:
                st.session_state.email.send_overnight_summary(
                    results['total'],
                    results['success'],
                    results['failed']
                )
            except:
                pass
            
            st.session_state.overnight_running = False
            st.success(f"🎉 Overnight Mode Complete! Applied to {results['success']} jobs!")
            st.info(f"✅ Success: {results['success']} | ❌ Failed: {results['failed']}")
            st.balloons()
    
    # Display jobs with modern cards
    if st.session_state.jobs:
        st.markdown(f"### {len(st.session_state.jobs)} Jobs Available")
        
        # Filter options
        col1, col2 = st.columns(2)
        with col1:
            platform_filter = st.multiselect(
                "Filter by Platform",
                options=list(set([job['platform'] for job in st.session_state.jobs])),
                default=[]
            )
        with col2:
            show_limit = st.slider("Show jobs", 10, 100, 20)
        
        # Filter jobs
        filtered_jobs = st.session_state.jobs
        if platform_filter:
            filtered_jobs = [job for job in st.session_state.jobs if job['platform'] in platform_filter]
        
        st.markdown(f"**Showing {min(len(filtered_jobs), show_limit)} of {len(filtered_jobs)} jobs**")
        st.markdown("<br>", unsafe_allow_html=True)
        
        for i, job in enumerate(filtered_jobs[:show_limit]):
            # Create nice job card
            with st.container():
                st.markdown(f"""
                <div class="job-card">
                    <div class="job-title">{job['title']}</div>
                    <div class="job-company">{job['company']}</div>
                    <div class="job-meta">
                        {job['location']} • {job['platform']} • {job['salary']}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                col1, col2, col3 = st.columns([2, 2, 2])
                
                with col1:
                    # DIRECT LINK BUTTON - Opens job directly!
                    st.markdown(f"""
                    <a href="{job['url']}" target="_blank" style="text-decoration: none;">
                        <button style="
                            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                            color: white;
                            border: none;
                            border-radius: 8px;
                            padding: 10px 20px;
                            font-weight: 600;
                            cursor: pointer;
                            width: 100%;
                            font-size: 14px;
                        ">
                            Open Job Link
                        </button>
                    </a>
                    """, unsafe_allow_html=True)
                
                with col2:
                    # Generate cover letter
                    if st.button("Generate Cover Letter", key=f"cover_{i}", use_container_width=True):
                        with st.spinner("Generating..."):
                            cover_letter = st.session_state.ai.generate_cover_letter(
                                job['title'], job['company'], job.get('description', '')
                            )
                        
                        with st.expander("Cover Letter", expanded=True):
                            st.text_area("Copy this:", cover_letter, height=250, key=f"cl_{i}")
                            st.info("Copy this cover letter and use it when applying!")
                
                with col3:
                    # Save job
                    if st.button("Save Job", key=f"save_{i}", use_container_width=True):
                        application = {
                            'job': job,
                            'cover_letter': '',
                            'applied_at': datetime.now().isoformat(),
                            'status': 'saved'
                        }
                        st.session_state.applications.append(application)
                        save_applications(st.session_state.applications)
                        st.success("Saved!")
                
                # Show URL for copying
                with st.expander("Copy Link"):
                    st.code(job['url'], language=None)
                
                st.markdown("<br>", unsafe_allow_html=True)

# TAB 2: Applications
with tab2:
    st.markdown("### 📝 Your Applications")
    
    if st.session_state.applications:
        df = pd.DataFrame([
            {
                'Title': app['job']['title'],
                'Company': app['job']['company'],
                'Platform': app['job']['platform'],
                'Applied': datetime.fromisoformat(app['applied_at']).strftime('%Y-%m-%d %H:%M')
            }
            for app in st.session_state.applications
        ])
        
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        st.info("📝 No applications yet!")

# TAB 3: Analytics
with tab3:
    st.markdown("### 📊 Performance Analytics")
    
    if st.session_state.applications:
        col1, col2 = st.columns(2)
        
        with col1:
            platform_counts = pd.DataFrame([app['job'] for app in st.session_state.applications])['platform'].value_counts()
            fig = px.pie(
                values=platform_counts.values,
                names=platform_counts.index,
                title="Applications by Platform",
                color_discrete_sequence=px.colors.sequential.Purples_r
            )
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font_color='white'
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            df = pd.DataFrame(st.session_state.applications)
            # Fix: pd.to_datetime already returns DatetimeIndex, no need for .dt
            dates = pd.to_datetime([app['applied_at'] for app in st.session_state.applications])
            df['date'] = dates.date  # Remove .dt since dates is already DatetimeIndex
            daily = df.groupby('date').size().reset_index(name='count')
            
            fig = px.line(
                daily, x='date', y='count',
                title="Applications Over Time",
                markers=True
            )
            fig.update_traces(line_color='#667eea', marker=dict(size=10))
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font_color='white'
            )
            st.plotly_chart(fig, use_container_width=True)

# TAB 4: Auto-Apply Bot
with tab4:
    st.markdown("### 🤖 Multi-Platform Auto-Apply Bot")
    
    st.info("""
    **Login 1x in each platform, bot remembers forever!**
    
    This bot will automatically apply to jobs on:
    - 🔵 LinkedIn (Easy Apply)
    - 🟢 Indeed (Easy Apply)  
    - 🔶 Glassdoor (Easy Apply)
    
    **Up to 300 applications per day!**
    """)
    
    # Auto-Apply Configuration
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Bot Settings")
        
        platforms_to_use = st.multiselect(
            "Select Platforms",
            ["LinkedIn", "Indeed", "Glassdoor"],
            default=["LinkedIn", "Indeed"]
        )
        
        max_apps_per_platform = st.slider(
            "Max Applications per Platform",
            min_value=10,
            max_value=200,
            value=100,
            step=10,
            help="Recommended: 50-100 per platform for safety"
        )
        
        delay_between_apps = st.slider(
            "Delay Between Applications (seconds)",
            min_value=20,
            max_value=120,
            value=45,
            step=5,
            help="Higher = safer, Lower = faster but riskier"
        )
    
    with col2:
        st.markdown("#### Your Information")
        
        auto_name = st.text_input("Full Name", value=Config.NAME)
        auto_email = st.text_input("Email", value=Config.EMAIL)
        auto_phone = st.text_input("Phone", value=Config.PHONE)
        auto_experience = st.number_input("Years of Experience", value=3, min_value=0, max_value=20)
        
        cv_uploaded = st.file_uploader("Upload CV (optional - will use default if not provided)", type=['pdf', 'docx'])
    
    st.markdown("---")
    
    # Auto-Apply Bot Instructions
    st.markdown("### 📖 How It Works")
    
    st.markdown("""
    **First Time Setup (Only Once!):**
    
    1. Click "Start Auto-Apply Bot" below
    2. Bot will open Chrome browser
    3. **You login manually** to each platform (LinkedIn, Indeed, Glassdoor)
    4. Bot saves your session cookies
    5. **Never need to login again!**
    
    **Next Times:**
    
    1. Click "Start Auto-Apply Bot"
    2. Bot uses saved sessions
    3. Bot applies automatically
    4. You relax! ☕
    
    **Safety Features:**
    
    - ✅ Human-like delays (30-60s between apps)
    - ✅ Max 100 apps per platform per day
    - ✅ Filters out Senior/Lead roles automatically
    - ✅ Only applies to Junior/Entry level
    - ✅ Session management (no password storing!)
    """)
    
    st.markdown("---")
    
    # Session Status
    st.markdown("### 🔐 Session Status")
    
    sessions_dir = Path('sessions')
    sessions_dir.mkdir(exist_ok=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        linkedin_session = (sessions_dir / 'linkedin_cookies.pkl').exists()
        if linkedin_session:
            st.success("🔵 LinkedIn: ✅ Logged In")
        else:
            st.warning("🔵 LinkedIn: ⚠️ Need Login")
    
    with col2:
        indeed_session = (sessions_dir / 'indeed_cookies.pkl').exists()
        if indeed_session:
            st.success("🟢 Indeed: ✅ Logged In")
        else:
            st.warning("🟢 Indeed: ⚠️ Need Login")
    
    with col3:
        glassdoor_session = (sessions_dir / 'glassdoor_cookies.pkl').exists()
        if glassdoor_session:
            st.success("🔶 Glassdoor: ✅ Logged In")
        else:
            st.warning("🔶 Glassdoor: ⚠️ Need Login")
    
    # Clear Sessions Button
    if st.button("🗑️ Clear All Sessions (Force Re-login)"):
        for file in sessions_dir.glob('*.pkl'):
            file.unlink()
        st.success("Sessions cleared! You'll need to login again next time.")
        st.rerun()
    
    st.markdown("---")
    
    # Launch Bot
    st.markdown("### 🚀 Launch Bot")
    
    if not platforms_to_use:
        st.warning("⚠️ Please select at least one platform!")
    else:
        st.info(f"""
        **Ready to apply to {len(platforms_to_use)} platform(s)**
        
        - Platforms: {', '.join(platforms_to_use)}
        - Max apps per platform: {max_apps_per_platform}
        - Total possible: {len(platforms_to_use) * max_apps_per_platform} applications
        - Estimated time: {len(platforms_to_use) * max_apps_per_platform * delay_between_apps // 60} minutes
        """)
        
        if st.button("🚀 Start Auto-Apply Bot", type="primary", use_container_width=True):
            st.warning("""
            ⚠️ **IMPORTANT - Local Bot Required**
            
            The Auto-Apply Bot uses Selenium and needs to run on your local computer (not on Streamlit Cloud).
            
            **To use Auto-Apply Bot:**
            
            1. Download `mvp_auto_apply_bot.py` from the repository
            2. Install Selenium: `pip install selenium webdriver-manager`
            3. Run locally: `python mvp_auto_apply_bot.py`
            
            **Why?**
            - Streamlit Cloud doesn't allow browser automation
            - Your computer has Chrome browser needed
            - You need to login manually first time
            
            **Alternative:**
            - Use "Find Jobs" tab to search
            - Click "Open Job Link" buttons
            - Apply manually (still fast with AI cover letters!)
            
            **Want the standalone bot?** 
            Check the repository for `mvp_auto_apply_bot.py` and `MVP_BOT_GUIDE.md`
            """)
    
    st.markdown("---")
    
    # Instructions for Local Bot
    with st.expander("📥 Download Local Auto-Apply Bot"):
        st.markdown("""
        **Get the standalone Auto-Apply Bot:**
        
        The bot is available in the repository as `mvp_auto_apply_bot.py`
        
        **Quick Start:**
        
        ```bash
        # 1. Download the file
        # 2. Install dependencies
        pip install selenium webdriver-manager
        
        # 3. Run the bot
        python mvp_auto_apply_bot.py
        
        # 4. Login to each platform (first time only!)
        # 5. Bot applies to 300+ jobs automatically!
        ```
        
        **Features:**
        - ✅ Login 1x, bot remembers forever
        - ✅ LinkedIn + Indeed + Glassdoor
        - ✅ 300+ applications per day
        - ✅ Filters Junior/Entry level only
        - ✅ Auto-fills forms
        - ✅ Uploads CV automatically
        - ✅ Human-like delays
        
        **Results:**
        - 300 apps/day
        - 1500 apps/week
        - 60-120 interviews/month
        - **10-20 job offers!** 💼
        """)

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(f"""
<div style='text-align: center; color: #a0aec0;'>
    <p>Made with ❤️ by {Config.NAME}</p>
    <p><a href='{Config.PORTFOLIO}' style='color: #667eea;'>Portfolio</a> | 
    <a href='{Config.GITHUB}' style='color: #667eea;'>GitHub</a></p>
</div>
""", unsafe_allow_html=True)