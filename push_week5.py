"""
Push Week 5 content to Canvas:
1. Create/Update Study Pack assignment
2. Add questions to existing quiz
"""

import requests
import json
from week5_content import WEEK5_STUDY_PACK, WEEK5_QUIZ_QUESTIONS, WEEK5_QUIZ_TITLE

CANVAS_BASE_URL = "https://vuu.instructure.com"
CANVAS_TOKEN = "12227~4vU2zfZVJc9JcemerL3kt9cf4GnWL3wJThurxmD7H2Faz8eknaf2DDvreFyMLa2K"
COURSE_ID = 6358

HEADERS = {
    "Authorization": f"Bearer {CANVAS_TOKEN}",
    "Content-Type": "application/json"
}

def api_get(endpoint, params=None):
    url = f'{CANVAS_BASE_URL}/api/v1{endpoint}'
    response = requests.get(url, headers=HEADERS, params=params or {})
    response.raise_for_status()
    return response.json()

def api_post(endpoint, data):
    url = f'{CANVAS_BASE_URL}/api/v1{endpoint}'
    response = requests.post(url, headers=HEADERS, json=data)
    if not response.ok:
        print(f"Error: {response.status_code}")
        print(response.text)
    response.raise_for_status()
    return response.json()

def api_put(endpoint, data):
    url = f'{CANVAS_BASE_URL}/api/v1{endpoint}'
    response = requests.put(url, headers=HEADERS, json=data)
    response.raise_for_status()
    return response.json()


def find_quiz_by_title(title):
    """Find a quiz by its title"""
    quizzes = api_get(f'/courses/{COURSE_ID}/quizzes', {'per_page': 100})
    for q in quizzes:
        if title.lower() in q['title'].lower():
            return q
    return None


def find_assignment_by_name(name):
    """Find an assignment by name"""
    assignments = api_get(f'/courses/{COURSE_ID}/assignments', {'per_page': 100})
    for a in assignments:
        if name.lower() in a['name'].lower():
            return a
    return None


def create_or_update_study_pack():
    """Create or update the Week 5 Study Pack assignment"""
    print("=" * 60)
    print("📚 STUDY PACK: Week 5 - Ads & Sponsorships")
    print("=" * 60)
    
    assignment_name = "Week 5 Study Pack: Ads & Sponsorships"
    existing = find_assignment_by_name("Week 5 Study Pack")
    
    assignment_data = {
        "assignment": {
            "name": assignment_name,
            "description": WEEK5_STUDY_PACK,
            "submission_types": ["none"],  # Read-only resource
            "published": False,
            "due_at": "2026-03-01T04:59:00Z"
        }
    }
    
    if existing:
        print(f"✏️  Updating existing assignment (ID: {existing['id']})")
        result = api_put(f'/courses/{COURSE_ID}/assignments/{existing["id"]}', assignment_data)
        print(f"✅ Updated: {result['name']}")
    else:
        print("➕ Creating new assignment...")
        result = api_post(f'/courses/{COURSE_ID}/assignments', assignment_data)
        print(f"✅ Created: {result['name']} (ID: {result['id']})")
    
    return result


def add_quiz_questions():
    """Add questions to the Week 5 quiz"""
    print("\n" + "=" * 60)
    print("🧪 QUIZ: Ethics Check Quiz 5 - Ads & Sponsorships")
    print("=" * 60)
    
    # Find the quiz
    quiz = find_quiz_by_title("Ethics Check Quiz 5")
    if not quiz:
        print("❌ Quiz not found! Looking for 'Ethics Check Quiz 5'")
        print("Available quizzes:")
        quizzes = api_get(f'/courses/{COURSE_ID}/quizzes', {'per_page': 100})
        for q in quizzes:
            print(f"  - {q['title']}")
        return None
    
    print(f"Found quiz: {quiz['title']} (ID: {quiz['id']})")
    print(f"Current question count: {quiz.get('question_count', 0)}")
    
    # Check if questions already exist
    existing_questions = api_get(f'/courses/{COURSE_ID}/quizzes/{quiz["id"]}/questions', {'per_page': 100})
    if existing_questions:
        print(f"⚠️  Quiz already has {len(existing_questions)} questions. Skipping to avoid duplicates.")
        return quiz
    
    # Add each question
    print(f"\nAdding {len(WEEK5_QUIZ_QUESTIONS)} questions...")
    
    for i, q in enumerate(WEEK5_QUIZ_QUESTIONS, 1):
        question_data = {
            "question": {
                "question_name": q["question_name"],
                "question_text": q["question_text"],
                "question_type": q["question_type"],
                "points_possible": q["points_possible"],
                "answers": q["answers"]
            }
        }
        
        result = api_post(f'/courses/{COURSE_ID}/quizzes/{quiz["id"]}/questions', question_data)
        print(f"  ✅ Added Q{i}: {result.get('question_name', 'Question')}")
    
    # Update quiz settings
    quiz_update = {
        "quiz": {
            "points_possible": 100,
            "time_limit": 30,
            "allowed_attempts": 2,
            "shuffle_answers": True
        }
    }
    api_put(f'/courses/{COURSE_ID}/quizzes/{quiz["id"]}', quiz_update)
    print(f"\n✅ Quiz configured: 100 points, 30 min, 2 attempts, shuffled answers")
    
    return quiz


def main():
    print("\n🚀 PUSHING WEEK 5 CONTENT TO CANVAS")
    print("=" * 60)
    print(f"Course: MCM 307 (ID: {COURSE_ID})")
    print(f"Target: VUU Canvas ({CANVAS_BASE_URL})")
    print("=" * 60)
    
    # Push study pack
    study_pack = create_or_update_study_pack()
    
    # Push quiz questions  
    quiz = add_quiz_questions()
    
    print("\n" + "=" * 60)
    print("✅ COMPLETE!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Review the Study Pack in Canvas")
    print("2. Review Quiz questions")
    print("3. Publish when ready")
    print("\nLinks:")
    print(f"  Study Pack: {CANVAS_BASE_URL}/courses/{COURSE_ID}/assignments/{study_pack['id']}")
    if quiz:
        print(f"  Quiz: {CANVAS_BASE_URL}/courses/{COURSE_ID}/quizzes/{quiz['id']}")


if __name__ == "__main__":
    main()
