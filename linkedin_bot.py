"""
LinkedIn Easy Apply Bot
Automatically applies to jobs using LinkedIn Easy Apply feature
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import random
import json
from datetime import datetime

class LinkedInEasyApplyBot:
    def __init__(self):
        """Initialize the bot"""
        self.driver = None
        self.applications = []
        
    def setup_driver(self):
        """Setup Chrome driver"""
        print("Setting up Chrome driver...")
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        
        # Use existing Chrome profile (keeps you logged in!)
        # Change path to your Chrome profile location
        # options.add_argument(r"user-data-dir=C:\Users\Pauli\AppData\Local\Google\Chrome\User Data")
        # options.add_argument("profile-directory=Default")
        
        self.driver = webdriver.Chrome(options=options)
        print("Driver ready!")
        
    def login_prompt(self):
        """Prompt user to login manually"""
        print("\n" + "="*60)
        print("LINKEDIN LOGIN REQUIRED")
        print("="*60)
        print("\n1. A Chrome window will open")
        print("2. LOGIN MANUALLY on LinkedIn")
        print("3. After login, come back here and press ENTER")
        print("\nOpening LinkedIn...")
        
        self.driver.get("https://www.linkedin.com/login")
        
        input("\n>>> Press ENTER after you've logged in... ")
        print("\n✅ Login confirmed! Starting job search...\n")
        
    def search_jobs(self, keywords, location="", remote=True, easy_apply_only=True):
        """Search for jobs on LinkedIn"""
        print(f"\n🔍 Searching: {keywords} | Location: {location or 'Worldwide'}")
        
        # Build search URL
        base_url = "https://www.linkedin.com/jobs/search/?"
        params = []
        
        if keywords:
            params.append(f"keywords={keywords.replace(' ', '%20')}")
        
        if location:
            params.append(f"location={location.replace(' ', '%20')}")
        
        if remote:
            params.append("f_WT=2")  # Remote filter
        
        if easy_apply_only:
            params.append("f_AL=true")  # Easy Apply filter
        
        params.append("sortBy=DD")  # Sort by date
        
        search_url = base_url + "&".join(params)
        
        print(f"URL: {search_url}")
        self.driver.get(search_url)
        time.sleep(3)
        
        return self.get_job_listings()
        
    def get_job_listings(self):
        """Get all job listings from current page"""
        jobs = []
        
        try:
            # Scroll to load more jobs
            self.scroll_job_list()
            
            # Find all job cards
            job_cards = self.driver.find_elements(By.CSS_SELECTOR, "div.job-card-container")
            
            print(f"Found {len(job_cards)} jobs on this page")
            
            for card in job_cards:
                try:
                    job = self.extract_job_info(card)
                    if job:
                        jobs.append(job)
                except Exception as e:
                    print(f"Error extracting job: {e}")
                    continue
            
        except Exception as e:
            print(f"Error getting job listings: {e}")
        
        return jobs
    
    def scroll_job_list(self):
        """Scroll through job list to load more"""
        try:
            job_list = self.driver.find_element(By.CLASS_NAME, "jobs-search-results-list")
            
            # Scroll multiple times
            for i in range(5):
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", job_list)
                time.sleep(1)
                
        except Exception as e:
            print(f"Scroll error: {e}")
    
    def extract_job_info(self, card):
        """Extract job information from card"""
        try:
            title = card.find_element(By.CSS_SELECTOR, "a.job-card-list__title").text
            company = card.find_element(By.CSS_SELECTOR, "a.job-card-container__company-name").text
            location = card.find_element(By.CSS_SELECTOR, "li.job-card-container__metadata-item").text
            link = card.find_element(By.CSS_SELECTOR, "a.job-card-list__title").get_attribute("href")
            
            return {
                'title': title,
                'company': company,
                'location': location,
                'url': link,
                'card': card
            }
        except Exception as e:
            return None
    
    def easy_apply(self, job):
        """Apply to job using Easy Apply"""
        try:
            print(f"\n📝 Applying: {job['title']} at {job['company']}")
            
            # Click on job card to open details
            job['card'].click()
            time.sleep(2)
            
            # Find and click Easy Apply button
            try:
                easy_apply_btn = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.jobs-apply-button"))
                )
                easy_apply_btn.click()
                time.sleep(2)
            except:
                print("   ⚠️ Easy Apply button not found")
                return False
            
            # Fill out application form
            success = self.fill_application_form()
            
            if success:
                self.applications.append({
                    'job': job,
                    'applied_at': datetime.now().isoformat(),
                    'status': 'applied'
                })
                print(f"   ✅ Applied successfully!")
                return True
            else:
                print(f"   ❌ Application failed")
                return False
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
            return False
    
    def fill_application_form(self):
        """Fill out LinkedIn Easy Apply form"""
        try:
            max_pages = 5
            current_page = 0
            
            while current_page < max_pages:
                current_page += 1
                print(f"   Page {current_page}...")
                
                # Fill text inputs
                self.fill_text_fields()
                
                # Handle dropdowns
                self.fill_dropdowns()
                
                # Handle radio buttons
                self.fill_radio_buttons()
                
                time.sleep(1)
                
                # Check for Next or Submit button
                try:
                    # Try Next button first
                    next_btn = self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='Continue to next step']")
                    next_btn.click()
                    time.sleep(2)
                    continue
                except:
                    pass
                
                try:
                    # Try Review button
                    review_btn = self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='Review your application']")
                    review_btn.click()
                    time.sleep(2)
                    continue
                except:
                    pass
                
                try:
                    # Try Submit button
                    submit_btn = self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='Submit application']")
                    submit_btn.click()
                    time.sleep(2)
                    print("   ✅ Application submitted!")
                    
                    # Close confirmation modal
                    try:
                        close_btn = self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='Dismiss']")
                        close_btn.click()
                    except:
                        pass
                    
                    return True
                except:
                    pass
                
                # If no buttons found, might be done
                break
            
            return False
            
        except Exception as e:
            print(f"   Form fill error: {e}")
            return False
    
    def fill_text_fields(self):
        """Fill text input fields with default answers"""
        try:
            inputs = self.driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
            
            for input_field in inputs:
                try:
                    label = input_field.get_attribute("aria-label") or ""
                    
                    # Skip if already filled
                    if input_field.get_attribute("value"):
                        continue
                    
                    # Default answers for common questions
                    if "phone" in label.lower():
                        input_field.send_keys("+27842677035")
                    elif "email" in label.lower():
                        input_field.send_keys("ljato976@gmail.com")
                    elif "year" in label.lower() and "experience" in label.lower():
                        input_field.send_keys("3")
                    elif "salary" in label.lower() or "compensation" in label.lower():
                        input_field.send_keys("60000")
                    
                except Exception as e:
                    continue
                    
        except Exception as e:
            pass
    
    def fill_dropdowns(self):
        """Handle dropdown selections"""
        try:
            # Try to select first option in dropdowns
            selects = self.driver.find_elements(By.TAG_NAME, "select")
            
            for select in selects:
                try:
                    options = select.find_elements(By.TAG_NAME, "option")
                    if len(options) > 1:
                        options[1].click()  # Select first non-empty option
                except:
                    continue
                    
        except Exception as e:
            pass
    
    def fill_radio_buttons(self):
        """Handle radio button selections"""
        try:
            # Usually select "Yes" for eligibility questions
            radio_groups = self.driver.find_elements(By.CSS_SELECTOR, "fieldset")
            
            for group in radio_groups:
                try:
                    label = group.find_element(By.TAG_NAME, "legend").text.lower()
                    
                    # For eligibility questions, select Yes
                    if "eligible" in label or "authorized" in label or "require" in label:
                        yes_option = group.find_element(By.CSS_SELECTOR, "label[for*='Yes']")
                        yes_option.click()
                        
                except Exception as e:
                    continue
                    
        except Exception as e:
            pass
    
    def run(self, searches):
        """
        Run the bot with multiple searches
        
        searches = [
            {'keywords': 'Data Analyst', 'location': '', 'remote': True},
            {'keywords': 'Data Analyst', 'location': 'Luanda, Angola', 'remote': False},
        ]
        """
        try:
            # Setup
            self.setup_driver()
            self.login_prompt()
            
            total_applied = 0
            
            # Run each search
            for search in searches:
                print("\n" + "="*60)
                print(f"SEARCH: {search['keywords']}")
                print("="*60)
                
                jobs = self.search_jobs(
                    keywords=search['keywords'],
                    location=search.get('location', ''),
                    remote=search.get('remote', True)
                )
                
                print(f"\nFound {len(jobs)} Easy Apply jobs")
                
                # Apply to each job
                for i, job in enumerate(jobs, 1):
                    print(f"\n[{i}/{len(jobs)}]")
                    
                    success = self.easy_apply(job)
                    
                    if success:
                        total_applied += 1
                    
                    # Random delay to avoid detection
                    delay = random.randint(10, 20)
                    print(f"   Waiting {delay}s...")
                    time.sleep(delay)
                    
                    # Stop if reached limit
                    if total_applied >= 50:
                        print("\n⚠️ Reached 50 applications limit for safety")
                        break
                
                if total_applied >= 50:
                    break
            
            # Save results
            self.save_results()
            
            print("\n" + "="*60)
            print(f"✅ DONE! Applied to {total_applied} jobs")
            print("="*60)
            
        except Exception as e:
            print(f"\n❌ Error: {e}")
        finally:
            if self.driver:
                input("\nPress ENTER to close browser...")
                self.driver.quit()
    
    def save_results(self):
        """Save application results to file"""
        filename = f"linkedin_applications_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(filename, 'w') as f:
            json.dump(self.applications, f, indent=2)
        
        print(f"\n💾 Results saved to: {filename}")


# ===========================================
# USAGE EXAMPLE
# ===========================================

if __name__ == "__main__":
    print("""
    ╔════════════════════════════════════════════╗
    ║   LINKEDIN EASY APPLY BOT                  ║
    ║   Automatic Job Applications               ║
    ╚════════════════════════════════════════════╝
    """)
    
    # Create bot
    bot = LinkedInEasyApplyBot()
    
    # Define searches
    searches = [
        # REMOTE JOBS
        {
            'keywords': 'Data Analyst',
            'location': '',
            'remote': True
        },
        {
            'keywords': 'Python Developer',
            'location': '',
            'remote': True
        },
        {
            'keywords': 'English Teacher',
            'location': '',
            'remote': True
        },
        
        # ANGOLA ONSITE JOBS
        {
            'keywords': 'Data Analyst',
            'location': 'Luanda, Angola',
            'remote': False
        },
        {
            'keywords': 'Data Entry',
            'location': 'Luanda, Angola',
            'remote': False
        },
    ]
    
    # RUN BOT
    bot.run(searches)
    
    print("\n✅ All done! Check the JSON file for results.")