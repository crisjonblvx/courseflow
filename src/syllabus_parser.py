"""
CourseFlow Syllabus Parser
Extracts course structure from parsed syllabus text
"""

# MCM 307 Media Ethics - Parsed Structure
# Based on syllabus extracted 2025-06-03

COURSE_DATA = {
    "course_info": {
        "code": "MCM 307",
        "title": "Media Ethics",
        "credits": 3,
        "term": "Spring 2026",
        "start_date": "2026-01-12",
        "end_date": "2026-05-02",
        "schedule": "Tuesday & Thursday 1:00-2:25 PM",
        "location": "Ellison Building Room 216",
        "instructor": "Professor Christopher 'CJ' Nurse",
        "email": "cjnurse@vuu.edu",
        "phone": "904.469.0263",
        "office_hours": [
            "Mon/Wed: 10:00 AM – 2:00 PM (Room 214 Ellison)",
            "Tue/Thu: 11:00 AM – 1:00 PM",
            "By Appointment: Via Canvas or Microsoft Teams"
        ]
    },
    
    "grading": {
        "Ethics Check Quizzes": {"weight": 30, "description": "10 short multiple-choice quizzes on weekly topics"},
        "The Reaction Video": {"weight": 20, "description": "2-minute video analyzing a media scandal (Midterm)"},
        "War Room Debates": {"weight": 30, "description": "In-class participation in debates"},
        "The Code Graphic": {"weight": 20, "description": "Visual one-sheet of personal Top 10 Rules (Final)"}
    },
    
    "modules": [
        {
            "week": 1,
            "title": "Can vs. Should",
            "subtitle": "Just because it's legal doesn't mean it's right",
            "unit": "The Basics (Right vs. Wrong)",
            "dates": {"start": "2026-01-12", "end": "2026-01-18"},
            "quiz_due": "2026-01-18",
            "topics": [
                "Legal vs. ethical distinctions",
                "Real-world examples of 'legal but wrong'",
                "Introduction to ethical frameworks"
            ]
        },
        {
            "week": 2,
            "title": "The Clout Trap",
            "subtitle": "Lying for views",
            "unit": "The Basics (Right vs. Wrong)",
            "dates": {"start": "2026-01-19", "end": "2026-01-25"},
            "quiz_due": "2026-01-25",
            "topics": [
                "Clickbait culture",
                "Fake pranks and staged content",
                "The cost of credibility"
            ]
        },
        {
            "week": 3,
            "title": "Privacy",
            "subtitle": "Is it okay to film people in public?",
            "unit": "The Basics (Right vs. Wrong)",
            "dates": {"start": "2026-01-26", "end": "2026-02-01"},
            "quiz_due": "2026-02-01",
            "topics": [
                "TikTok gym pranks controversy",
                "Consent and public spaces",
                "When content becomes harassment"
            ]
        },
        {
            "week": 4,
            "title": "The Paparazzi",
            "subtitle": "Case Study",
            "unit": "The Basics (Right vs. Wrong)",
            "dates": {"start": "2026-02-02", "end": "2026-02-08"},
            "quiz_due": "2026-02-08",
            "topics": [
                "History of paparazzi culture",
                "Princess Diana case study",
                "Modern celebrity privacy"
            ]
        },
        {
            "week": 5,
            "title": "Ads and Sponsorships",
            "subtitle": "The FTC Rules",
            "unit": "The Influencer World",
            "dates": {"start": "2026-02-09", "end": "2026-02-15"},
            "quiz_due": "2026-02-15",
            "topics": [
                "FTC disclosure requirements",
                "#ad vs. #sponsored",
                "Consequences of non-disclosure"
            ]
        },
        {
            "week": 6,
            "title": "Payola",
            "subtitle": "Taking money under the table",
            "unit": "The Influencer World",
            "dates": {"start": "2026-02-16", "end": "2026-02-22"},
            "quiz_due": "2026-02-22",
            "topics": [
                "History of payola in radio",
                "Modern pay-for-play schemes",
                "Crypto and NFT promotions"
            ]
        },
        {
            "week": 7,
            "title": "Cancel Culture",
            "subtitle": "When does the mob go too far?",
            "unit": "The Influencer World",
            "dates": {"start": "2026-02-23", "end": "2026-03-01"},
            "quiz_due": "2026-03-01",
            "topics": [
                "Accountability vs. destruction",
                "Case studies of cancellations",
                "The right to redemption"
            ]
        },
        {
            "week": 8,
            "title": "Midterm Week",
            "subtitle": "The Reaction Video Due",
            "unit": "The Influencer World",
            "dates": {"start": "2026-03-02", "end": "2026-03-08"},
            "assignment_due": "2026-03-08",
            "assignment_name": "The Reaction Video",
            "topics": [
                "Midterm presentations",
                "Peer review of reaction videos",
                "Discussion of findings"
            ]
        },
        {
            "week": "break",
            "title": "Spring Break",
            "subtitle": "No Class",
            "dates": {"start": "2026-03-09", "end": "2026-03-15"}
        },
        {
            "week": 9,
            "title": "Deepfakes",
            "subtitle": "Is that video real?",
            "unit": "The Future (AI & Tech)",
            "dates": {"start": "2026-03-16", "end": "2026-03-22"},
            "quiz_due": "2026-03-22",
            "topics": [
                "How deepfakes work",
                "Political and personal misuse",
                "Detection and verification"
            ]
        },
        {
            "week": 10,
            "title": "AI Art",
            "subtitle": "Is it stealing?",
            "unit": "The Future (AI & Tech)",
            "dates": {"start": "2026-03-23", "end": "2026-03-29"},
            "quiz_due": "2026-03-29",
            "topics": [
                "How AI art generators work",
                "Artist rights and training data",
                "The future of creative work"
            ]
        },
        {
            "week": 11,
            "title": "The Algorithm",
            "subtitle": "Why does your feed show you violence?",
            "unit": "The Future (AI & Tech)",
            "dates": {"start": "2026-03-30", "end": "2026-04-05"},
            "quiz_due": "2026-04-05",
            "topics": [
                "How recommendation algorithms work",
                "Filter bubbles and radicalization",
                "Platform responsibility"
            ]
        },
        {
            "week": 12,
            "title": "Fake News",
            "subtitle": "How to spot a lie",
            "unit": "The Future (AI & Tech)",
            "dates": {"start": "2026-04-06", "end": "2026-04-12"},
            "quiz_due": "2026-04-12",
            "topics": [
                "Misinformation vs. disinformation",
                "Fact-checking techniques",
                "Media literacy skills"
            ]
        },
        {
            "week": 13,
            "title": "Diversity",
            "subtitle": "Representation in movies/TV",
            "unit": "The Wrap Up",
            "dates": {"start": "2026-04-13", "end": "2026-04-19"},
            "quiz_due": "2026-04-17",  # All work due April 17
            "topics": [
                "Representation matters",
                "Tokenism vs. authentic inclusion",
                "Behind-the-camera diversity"
            ]
        },
        {
            "week": 14,
            "title": "The HBCU Standard",
            "subtitle": "Credibility",
            "unit": "The Wrap Up",
            "dates": {"start": "2026-04-20", "end": "2026-04-26"},
            "topics": [
                "What HBCUs represent",
                "Building professional credibility",
                "Your reputation is your brand"
            ]
        },
        {
            "week": 15,
            "title": "Final Presentations",
            "subtitle": "The Code Graphic",
            "unit": "The Wrap Up",
            "dates": {"start": "2026-04-27", "end": "2026-05-02"},
            "assignment_due": "2026-04-17",  # Per syllabus: all work due April 17
            "assignment_name": "The Code Graphic",
            "topics": [
                "Final presentations",
                "Peer feedback",
                "Course reflection"
            ]
        }
    ],
    
    "assignments": [
        {
            "name": "Ethics Check Quiz 1: Can vs. Should",
            "type": "quiz",
            "points": 30,
            "due_date": "2026-01-18T23:59:00",
            "description": "10 multiple-choice questions on Week 1 material about legal vs. ethical distinctions."
        },
        {
            "name": "Ethics Check Quiz 2: The Clout Trap",
            "type": "quiz",
            "points": 30,
            "due_date": "2026-01-25T23:59:00",
            "description": "10 multiple-choice questions on Week 2 material about lying for views and clickbait culture."
        },
        {
            "name": "Ethics Check Quiz 3: Privacy",
            "type": "quiz",
            "points": 30,
            "due_date": "2026-02-01T23:59:00",
            "description": "10 multiple-choice questions on Week 3 material about privacy and filming in public."
        },
        {
            "name": "Ethics Check Quiz 4: The Paparazzi",
            "type": "quiz",
            "points": 30,
            "due_date": "2026-02-08T23:59:00",
            "description": "10 multiple-choice questions on Week 4 paparazzi case study."
        },
        {
            "name": "Ethics Check Quiz 5: Ads & Sponsorships",
            "type": "quiz",
            "points": 30,
            "due_date": "2026-02-15T23:59:00",
            "description": "10 multiple-choice questions on Week 5 material about FTC rules and disclosures."
        },
        {
            "name": "Ethics Check Quiz 6: Payola",
            "type": "quiz",
            "points": 30,
            "due_date": "2026-02-22T23:59:00",
            "description": "10 multiple-choice questions on Week 6 material about pay-for-play schemes."
        },
        {
            "name": "Ethics Check Quiz 7: Cancel Culture",
            "type": "quiz",
            "points": 30,
            "due_date": "2026-03-01T23:59:00",
            "description": "10 multiple-choice questions on Week 7 material about accountability vs. mob justice."
        },
        {
            "name": "The Reaction Video (Midterm)",
            "type": "assignment",
            "points": 200,
            "due_date": "2026-03-08T23:59:00",
            "submission_types": ["online_upload", "media_recording"],
            "description": """## The Reaction Video (Midterm Assignment)

**Worth:** 20% of your final grade

### The Task
Choose a recent "Apology Video" from a celebrity or influencer and record a **2-minute video** of yourself breaking it down.

### What to Analyze
- Was it sincere?
- Did they fake cry?
- Did they take accountability?
- What worked? What didn't?

### Requirements
- Video must be 2-3 minutes long
- You must appear on camera
- Cite the original video you're analyzing
- Submit via Canvas (upload or media recording)

### Grading Criteria
- Analysis depth (40%)
- Communication clarity (30%)
- Professional presentation (20%)
- Proper citation (10%)

This assignment assesses your analysis skills without requiring a 5-page paper."""
        },
        {
            "name": "Ethics Check Quiz 8: Deepfakes",
            "type": "quiz",
            "points": 30,
            "due_date": "2026-03-22T23:59:00",
            "description": "10 multiple-choice questions on Week 9 material about deepfakes and verification."
        },
        {
            "name": "Ethics Check Quiz 9: AI Art",
            "type": "quiz",
            "points": 30,
            "due_date": "2026-03-29T23:59:00",
            "description": "10 multiple-choice questions on Week 10 material about AI-generated art and ethics."
        },
        {
            "name": "Ethics Check Quiz 10: The Algorithm & Fake News",
            "type": "quiz",
            "points": 30,
            "due_date": "2026-04-12T23:59:00",
            "description": "10 multiple-choice questions covering Weeks 11-12 on algorithms and misinformation."
        },
        {
            "name": "The Code Graphic (Final Project)",
            "type": "assignment",
            "points": 200,
            "due_date": "2026-04-17T23:59:00",
            "submission_types": ["online_upload"],
            "description": """## The Code Graphic (Final Project)

**Worth:** 20% of your final grade

### The Task
Create a visual **One-Sheet** (using Canva or similar) that lists your personal **"Top 10 Rules"** for your career as a media professional.

### Examples of Rules
- "Rule #1: I will never promote a crypto scam."
- "Rule #2: I will always disclose ads."
- "Rule #3: I will verify before I share."

### Requirements
- Must be a single page/slide
- Visually designed (use Canva, Photoshop, etc.)
- Include 10 specific, personal rules
- Rules should reflect what you learned this semester

### Grading Criteria
- Rule quality and specificity (40%)
- Visual design and professionalism (30%)
- Connection to course material (20%)
- Creativity (10%)

This is a practical, visual manifesto you can keep and reference throughout your career."""
        },
        {
            "name": "War Room Participation",
            "type": "assignment",
            "points": 300,
            "due_date": "2026-04-17T23:59:00",
            "submission_types": ["none"],
            "description": """## War Room Participation

**Worth:** 30% of your final grade

### What is The War Room?
Every week, we put a controversial headline on the screen. You must pick a side and argue it in class.

### How It Works
- A topic is presented (e.g., "Is it okay to use AI art?")
- You choose a position
- You verbally defend your position
- You engage with opposing viewpoints

### Grading
- Based on consistent participation throughout the semester
- Quality of arguments matters
- Respect for opposing views matters
- You don't have to "win" — you have to engage

### Goal
Building verbal communication skills and confidence. This is practice for the real world, where you'll need to defend your choices."""
        }
    ],
    
    "attendance_policy": {
        "name": "The 5 for 5 Policy",
        "allowed_absences": 5,
        "consequence": "More than 5 unexcused absences = automatic F",
        "rationale": "This class relies on discussion. If you aren't here, you aren't learning."
    }
}

if __name__ == "__main__":
    import json
    print(json.dumps(COURSE_DATA, indent=2))
