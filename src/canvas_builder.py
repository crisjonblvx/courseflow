"""
CourseFlow Canvas Builder
Creates course structure in Canvas from parsed syllabus data
Smart merge: skips items that already exist (by name)
"""

import os
import json
import requests
from datetime import datetime
from syllabus_parser import COURSE_DATA

# Canvas API Configuration
CANVAS_BASE_URL = os.getenv("CANVAS_BASE_URL", "https://vuu.instructure.com")
CANVAS_TOKEN = os.getenv("CANVAS_API_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {CANVAS_TOKEN}",
    "Content-Type": "application/json"
}

def api_get(endpoint, params=None):
    """GET request to Canvas API"""
    url = f"{CANVAS_BASE_URL}/api/v1{endpoint}"
    response = requests.get(url, headers=HEADERS, params=params or {})
    response.raise_for_status()
    return response.json()

def api_post(endpoint, data):
    """POST request to Canvas API"""
    url = f"{CANVAS_BASE_URL}/api/v1{endpoint}"
    response = requests.post(url, headers=HEADERS, json=data)
    response.raise_for_status()
    return response.json()

def api_put(endpoint, data):
    """PUT request to Canvas API"""
    url = f"{CANVAS_BASE_URL}/api/v1{endpoint}"
    response = requests.put(url, headers=HEADERS, json=data)
    response.raise_for_status()
    return response.json()


class SmartCourseBuilder:
    """Builds Canvas course structure with smart merge (skip existing)"""
    
    def __init__(self, course_id, course_data, dry_run=True):
        self.course_id = course_id
        self.data = course_data
        self.dry_run = dry_run
        self.log = []
        
        # Cache of existing items (populated on build)
        self.existing_modules = {}
        self.existing_assignments = {}
        self.existing_quizzes = {}
        self.existing_pages = {}
    
    def _log(self, action, item, details=""):
        """Log an action"""
        prefix = "[DRY RUN] " if self.dry_run else ""
        entry = f"{prefix}{action}: {item}"
        if details:
            entry += f" ({details})"
        self.log.append(entry)
        print(entry)
    
    def fetch_existing(self):
        """Fetch all existing items in the course"""
        print("📋 Fetching existing course content...")
        
        # Fetch modules
        modules = api_get(f"/courses/{self.course_id}/modules", {"per_page": 100})
        self.existing_modules = {m["name"].lower().strip(): m for m in modules}
        print(f"   Found {len(self.existing_modules)} existing modules")
        
        # Fetch assignments
        assignments = api_get(f"/courses/{self.course_id}/assignments", {"per_page": 100})
        self.existing_assignments = {a["name"].lower().strip(): a for a in assignments}
        print(f"   Found {len(self.existing_assignments)} existing assignments")
        
        # Fetch quizzes
        quizzes = api_get(f"/courses/{self.course_id}/quizzes", {"per_page": 100})
        self.existing_quizzes = {q["title"].lower().strip(): q for q in quizzes}
        print(f"   Found {len(self.existing_quizzes)} existing quizzes")
        
        # Fetch pages
        pages = api_get(f"/courses/{self.course_id}/pages", {"per_page": 100})
        self.existing_pages = {p["title"].lower().strip(): p for p in pages}
        print(f"   Found {len(self.existing_pages)} existing pages")
        print()
    
    def create_module(self, name, position, unlock_at=None):
        """Create a module if it doesn't exist"""
        name_key = name.lower().strip()
        
        if name_key in self.existing_modules:
            self._log("⏭️  SKIP MODULE", name, "already exists")
            return self.existing_modules[name_key]
        
        module_data = {
            "module": {
                "name": name,
                "position": position,
                "unlock_at": unlock_at
            }
        }
        
        if self.dry_run:
            self._log("✅ CREATE MODULE", name, f"position {position}")
            return {"id": f"dry_run_module_{position}", "name": name}
        
        result = api_post(f"/courses/{self.course_id}/modules", module_data)
        self._log("✅ CREATE MODULE", name, f"id={result['id']}")
        self.existing_modules[name_key] = result
        return result
    
    def create_assignment(self, name, points, due_at, description, submission_types=None):
        """Create an assignment if it doesn't exist"""
        name_key = name.lower().strip()
        
        if name_key in self.existing_assignments:
            self._log("⏭️  SKIP ASSIGNMENT", name, "already exists")
            return self.existing_assignments[name_key]
        
        assignment_data = {
            "assignment": {
                "name": name,
                "points_possible": points,
                "due_at": due_at,
                "description": description,
                "submission_types": submission_types or ["online_upload"],
                "published": False
            }
        }
        
        if self.dry_run:
            self._log("✅ CREATE ASSIGNMENT", name, f"{points} pts, due {due_at[:10] if due_at else 'N/A'}")
            return {"id": f"dry_run_assignment_{name}", "name": name}
        
        result = api_post(f"/courses/{self.course_id}/assignments", assignment_data)
        self._log("✅ CREATE ASSIGNMENT", name, f"id={result['id']}")
        self.existing_assignments[name_key] = result
        return result
    
    def create_quiz(self, name, points, due_at, description):
        """Create a quiz if it doesn't exist"""
        name_key = name.lower().strip()
        
        if name_key in self.existing_quizzes:
            self._log("⏭️  SKIP QUIZ", name, "already exists")
            return self.existing_quizzes[name_key]
        
        quiz_data = {
            "quiz": {
                "title": name,
                "quiz_type": "assignment",
                "points_possible": points,
                "due_at": due_at,
                "description": description,
                "time_limit": 30,
                "allowed_attempts": 2,
                "published": False
            }
        }
        
        if self.dry_run:
            self._log("✅ CREATE QUIZ", name, f"{points} pts, due {due_at[:10] if due_at else 'N/A'}")
            return {"id": f"dry_run_quiz_{name}", "name": name}
        
        result = api_post(f"/courses/{self.course_id}/quizzes", quiz_data)
        self._log("✅ CREATE QUIZ", name, f"id={result['id']}")
        self.existing_quizzes[name_key] = result
        return result
    
    def create_page(self, title, body):
        """Create a page if it doesn't exist"""
        title_key = title.lower().strip()
        
        if title_key in self.existing_pages:
            self._log("⏭️  SKIP PAGE", title, "already exists")
            return self.existing_pages[title_key]
        
        page_data = {
            "wiki_page": {
                "title": title,
                "body": body,
                "published": False
            }
        }
        
        if self.dry_run:
            self._log("✅ CREATE PAGE", title)
            return {"url": title.lower().replace(" ", "-"), "title": title}
        
        result = api_post(f"/courses/{self.course_id}/pages", page_data)
        self._log("✅ CREATE PAGE", title, f"url={result['url']}")
        self.existing_pages[title_key] = result
        return result
    
    def build_course_overview_page(self):
        """Create the course overview page"""
        info = self.data["course_info"]
        grading = self.data["grading"]
        
        html = f"""
<h2>📚 {info['code']}: {info['title']}</h2>

<h3>Course Information</h3>
<ul>
    <li><strong>Term:</strong> {info['term']}</li>
    <li><strong>Schedule:</strong> {info['schedule']}</li>
    <li><strong>Location:</strong> {info['location']}</li>
    <li><strong>Credits:</strong> {info['credits']}</li>
</ul>

<h3>Instructor</h3>
<ul>
    <li><strong>Name:</strong> {info['instructor']}</li>
    <li><strong>Email:</strong> <a href="mailto:{info['email']}">{info['email']}</a></li>
    <li><strong>Phone:</strong> {info['phone']}</li>
</ul>

<h3>Office Hours</h3>
<ul>
    {"".join(f"<li>{oh}</li>" for oh in info['office_hours'])}
</ul>

<hr>

<h3>Grading Breakdown</h3>
<table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse; width: 100%;">
    <thead style="background-color: #f0f0f0;">
        <tr><th>Component</th><th>Weight</th><th>Description</th></tr>
    </thead>
    <tbody>
        {"".join(f'<tr><td>{name}</td><td>{details["weight"]}%</td><td>{details["description"]}</td></tr>' for name, details in grading.items())}
    </tbody>
</table>

<hr>

<h3>⚠️ Attendance Policy: The "5 for 5" Rule</h3>
<p><strong>"{self.data['attendance_policy']['rationale']}"</strong></p>
<ul>
    <li>You are allowed {self.data['attendance_policy']['allowed_absences']} unexcused absences</li>
    <li><strong>Consequence:</strong> {self.data['attendance_policy']['consequence']}</li>
</ul>
"""
        return self.create_page(f"{info['code']} Course Overview", html)
    
    def build_module_overview_page(self, module):
        """Create an overview page for a module"""
        if module.get("week") == "break":
            return None
        
        topics_list = "\n".join(f"<li>{topic}</li>" for topic in module.get("topics", []))
        
        quiz_note = ""
        if module.get('quiz_due'):
            quiz_note = f"<li><strong>📝 Complete Quiz by {module['quiz_due']}</strong></li>"
        
        assignment_note = ""
        if module.get('assignment_due'):
            assignment_note = f"<li><strong>📎 {module.get('assignment_name', 'Assignment')} due {module['assignment_due']}</strong></li>"
        
        html = f"""
<h2>Week {module['week']}: {module['title']}</h2>
<h3><em>{module['subtitle']}</em></h3>

<p><strong>Unit:</strong> {module.get('unit', 'N/A')}</p>
<p><strong>Dates:</strong> {module['dates']['start']} to {module['dates']['end']}</p>

<hr>

<h3>📋 Topics This Week</h3>
<ul>
{topics_list}
</ul>

<hr>

<h3>✅ To-Do This Week</h3>
<ul>
    <li>Watch/read assigned materials</li>
    <li>Participate in War Room discussion</li>
    {quiz_note}
    {assignment_note}
</ul>
"""
        return self.create_page(f"Week {module['week']}: {module['title']} - Overview", html)
    
    def build_all(self):
        """Build the complete course structure with smart merge"""
        print("=" * 60)
        print(f"COURSEFLOW SMART MERGE: {self.data['course_info']['code']}")
        print(f"Mode: {'DRY RUN (preview only)' if self.dry_run else 'LIVE (creating in Canvas)'}")
        print("=" * 60)
        print()
        
        # Fetch existing content first
        self.fetch_existing()
        
        # Track stats
        created = 0
        skipped = 0
        
        # 1. Create course overview page
        print("--- PAGES ---")
        self.build_course_overview_page()
        
        # 2. Create modules and their overview pages
        print("\n--- MODULES ---")
        position = max([m.get("position", 0) for m in self.existing_modules.values()] or [0]) + 1
        
        for module in self.data["modules"]:
            if module.get("week") == "break":
                module_name = f"🌴 {module['title']} ({module['dates']['start']} - {module['dates']['end']})"
            else:
                module_name = f"Week {module['week']}: {module['title']}"
            
            result = self.create_module(module_name, position)
            
            # Create overview page for non-break modules
            if module.get("week") != "break":
                self.build_module_overview_page(module)
            
            position += 1
        
        # 3. Create assignments and quizzes
        print("\n--- ASSIGNMENTS & QUIZZES ---")
        for assignment in self.data["assignments"]:
            if assignment["type"] == "quiz":
                self.create_quiz(
                    assignment["name"],
                    assignment["points"],
                    assignment["due_date"],
                    assignment["description"]
                )
            else:
                self.create_assignment(
                    assignment["name"],
                    assignment["points"],
                    assignment["due_date"],
                    assignment["description"],
                    submission_types=assignment.get("submission_types")
                )
        
        # Count results
        for entry in self.log:
            if "✅ CREATE" in entry:
                created += 1
            elif "⏭️  SKIP" in entry:
                skipped += 1
        
        print()
        print("=" * 60)
        print(f"SMART MERGE COMPLETE")
        print(f"  ✅ Created: {created}")
        print(f"  ⏭️  Skipped: {skipped} (already existed)")
        print(f"  📊 Total actions: {len(self.log)}")
        print("=" * 60)
        
        return {
            "created": created,
            "skipped": skipped,
            "log": self.log
        }


def preview_build(course_id):
    """Preview what would be created (dry run)"""
    builder = SmartCourseBuilder(course_id, COURSE_DATA, dry_run=True)
    return builder.build_all()


def execute_build(course_id):
    """Actually create the course structure in Canvas"""
    builder = SmartCourseBuilder(course_id, COURSE_DATA, dry_run=False)
    return builder.build_all()


if __name__ == "__main__":
    import sys
    
    # Load environment from .env file
    env_path = os.path.join(os.path.dirname(__file__), "..", ".env")
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                if "=" in line and not line.startswith("#"):
                    key, value = line.strip().split("=", 1)
                    os.environ[key] = value
    
    # MCM 307 Media Ethics course ID
    COURSE_ID = 6358
    
    if len(sys.argv) > 1 and sys.argv[1] == "--execute":
        print("⚠️  EXECUTING LIVE BUILD - This will create content in Canvas!")
        print("   (Only NEW items will be created - existing items will be skipped)")
        print()
        confirm = input("Type 'yes' to confirm: ")
        if confirm.lower() == "yes":
            execute_build(COURSE_ID)
        else:
            print("Aborted.")
    else:
        print("Running in preview mode (dry run)...")
        print("To execute for real, run: python canvas_builder.py --execute")
        print()
        preview_build(COURSE_ID)
