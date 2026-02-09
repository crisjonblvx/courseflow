"""
CourseFlow Canvas Builder
Creates course structure in Canvas from parsed syllabus data
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

def api_get(endpoint):
    """GET request to Canvas API"""
    url = f"{CANVAS_BASE_URL}/api/v1{endpoint}"
    response = requests.get(url, headers=HEADERS)
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


class CourseBuilder:
    """Builds Canvas course structure from syllabus data"""
    
    def __init__(self, course_id, course_data, dry_run=True):
        self.course_id = course_id
        self.data = course_data
        self.dry_run = dry_run
        self.created_modules = {}
        self.created_assignments = {}
        self.log = []
    
    def _log(self, action, item, details=""):
        """Log an action"""
        entry = f"{'[DRY RUN] ' if self.dry_run else ''}✓ {action}: {item}"
        if details:
            entry += f" ({details})"
        self.log.append(entry)
        print(entry)
    
    def create_module(self, name, position, unlock_at=None):
        """Create a module in Canvas"""
        module_data = {
            "module": {
                "name": name,
                "position": position,
                "unlock_at": unlock_at
            }
        }
        
        if self.dry_run:
            self._log("CREATE MODULE", name, f"position {position}")
            return {"id": f"dry_run_module_{position}", "name": name}
        
        result = api_post(f"/courses/{self.course_id}/modules", module_data)
        self._log("CREATE MODULE", name, f"id={result['id']}")
        return result
    
    def create_assignment(self, name, points, due_at, description, submission_types=None, assignment_group_id=None):
        """Create an assignment in Canvas"""
        assignment_data = {
            "assignment": {
                "name": name,
                "points_possible": points,
                "due_at": due_at,
                "description": description,
                "submission_types": submission_types or ["online_upload"],
                "published": False  # Don't publish yet
            }
        }
        
        if assignment_group_id:
            assignment_data["assignment"]["assignment_group_id"] = assignment_group_id
        
        if self.dry_run:
            self._log("CREATE ASSIGNMENT", name, f"{points} pts, due {due_at[:10] if due_at else 'N/A'}")
            return {"id": f"dry_run_assignment_{name}", "name": name}
        
        result = api_post(f"/courses/{self.course_id}/assignments", assignment_data)
        self._log("CREATE ASSIGNMENT", name, f"id={result['id']}")
        return result
    
    def create_quiz(self, name, points, due_at, description):
        """Create a quiz in Canvas"""
        quiz_data = {
            "quiz": {
                "title": name,
                "quiz_type": "assignment",
                "points_possible": points,
                "due_at": due_at,
                "description": description,
                "time_limit": 30,  # 30 minutes
                "allowed_attempts": 2,
                "published": False
            }
        }
        
        if self.dry_run:
            self._log("CREATE QUIZ", name, f"{points} pts, due {due_at[:10] if due_at else 'N/A'}")
            return {"id": f"dry_run_quiz_{name}", "name": name}
        
        result = api_post(f"/courses/{self.course_id}/quizzes", quiz_data)
        self._log("CREATE QUIZ", name, f"id={result['id']}")
        return result
    
    def create_page(self, title, body):
        """Create a page in Canvas"""
        page_data = {
            "wiki_page": {
                "title": title,
                "body": body,
                "published": False
            }
        }
        
        if self.dry_run:
            self._log("CREATE PAGE", title)
            return {"url": title.lower().replace(" ", "-"), "title": title}
        
        result = api_post(f"/courses/{self.course_id}/pages", page_data)
        self._log("CREATE PAGE", title, f"url={result['url']}")
        return result
    
    def add_item_to_module(self, module_id, item_type, content_id, title=None, indent=0):
        """Add an item to a module"""
        item_data = {
            "module_item": {
                "type": item_type,
                "content_id": content_id,
                "indent": indent
            }
        }
        if title:
            item_data["module_item"]["title"] = title
        
        if self.dry_run:
            self._log("ADD TO MODULE", f"{item_type}: {title or content_id}", f"module {module_id}")
            return {"id": f"dry_run_item_{content_id}"}
        
        result = api_post(f"/courses/{self.course_id}/modules/{module_id}/items", item_data)
        return result
    
    def build_course_overview_page(self):
        """Create the course overview page"""
        info = self.data["course_info"]
        grading = self.data["grading"]
        
        grading_table = "\n".join([
            f"| {name} | {details['weight']}% | {details['description']} |"
            for name, details in grading.items()
        ])
        
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
<table>
    <thead>
        <tr><th>Component</th><th>Weight</th><th>Description</th></tr>
    </thead>
    <tbody>
        {"".join(f"<tr><td>{name}</td><td>{details['weight']}%</td><td>{details['description']}</td></tr>" for name, details in grading.items())}
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
    {"<li><strong>Complete Quiz by " + module.get('quiz_due', '') + "</strong></li>" if module.get('quiz_due') else ""}
    {"<li><strong>" + module.get('assignment_name', '') + " due " + module.get('assignment_due', '') + "</strong></li>" if module.get('assignment_due') else ""}
</ul>
"""
        return self.create_page(f"Week {module['week']}: {module['title']} - Overview", html)
    
    def build_all(self):
        """Build the complete course structure"""
        print("=" * 60)
        print(f"COURSEFLOW: Building {self.data['course_info']['code']}")
        print(f"Mode: {'DRY RUN (preview only)' if self.dry_run else 'LIVE (creating in Canvas)'}")
        print("=" * 60)
        print()
        
        # 1. Create course overview page
        print("--- COURSE OVERVIEW ---")
        self.build_course_overview_page()
        print()
        
        # 2. Create modules and their content
        print("--- MODULES ---")
        position = 1
        
        for module in self.data["modules"]:
            if module.get("week") == "break":
                # Create a simple "Spring Break" module
                self.create_module(f"🌴 {module['title']} ({module['dates']['start']} - {module['dates']['end']})", position)
                position += 1
                continue
            
            # Create the module
            module_name = f"Week {module['week']}: {module['title']}"
            created_module = self.create_module(module_name, position, unlock_at=module['dates']['start'] + "T00:00:00Z")
            self.created_modules[module['week']] = created_module
            
            # Create module overview page
            self.build_module_overview_page(module)
            
            position += 1
        
        print()
        
        # 3. Create assignments
        print("--- ASSIGNMENTS ---")
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
        
        print()
        print("=" * 60)
        print(f"BUILD COMPLETE: {len(self.log)} actions")
        print("=" * 60)
        
        return self.log


def preview_build(course_id):
    """Preview what would be created (dry run)"""
    builder = CourseBuilder(course_id, COURSE_DATA, dry_run=True)
    return builder.build_all()


def execute_build(course_id):
    """Actually create the course structure in Canvas"""
    builder = CourseBuilder(course_id, COURSE_DATA, dry_run=False)
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
