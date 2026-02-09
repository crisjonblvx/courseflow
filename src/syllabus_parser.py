"""
CourseFlow Syllabus Parser
Extracts course structure from parsed syllabus text

MCM 307 Media Ethics - ADJUSTED DATES
- Quiz 3 starts Feb 15
- Spring Break: Mar 9-15
- All work due: April 17
"""

COURSE_DATA = {
    "course_info": {
        "code": "MCM 307",
        "title": "Media Ethics",
        "credits": 3,
        "term": "Spring 2026",
        "start_date": "2026-01-12",
        "end_date": "2026-04-17",
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
        # Weeks 1-2 already completed (Quiz 1 & 2 graded)
        {
            "week": 3,
            "title": "Privacy",
            "subtitle": "Is it okay to film people in public?",
            "unit": "The Basics (Right vs. Wrong)",
            "dates": {"start": "2026-02-09", "end": "2026-02-15"},
            "quiz_due": "2026-02-15",
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
            "dates": {"start": "2026-02-16", "end": "2026-02-22"},
            "quiz_due": "2026-02-22",
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
            "dates": {"start": "2026-02-23", "end": "2026-03-01"},
            "quiz_due": "2026-03-01",
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
            "dates": {"start": "2026-03-02", "end": "2026-03-08"},
            "quiz_due": "2026-03-08",
            "topics": [
                "History of payola in radio",
                "Modern pay-for-play schemes",
                "Crypto and NFT promotions"
            ]
        },
        {
            "week": "break",
            "title": "Spring Break",
            "subtitle": "No Class",
            "dates": {"start": "2026-03-09", "end": "2026-03-15"}
        },
        {
            "week": 7,
            "title": "Cancel Culture",
            "subtitle": "When does the mob go too far?",
            "unit": "The Influencer World",
            "dates": {"start": "2026-03-16", "end": "2026-03-22"},
            "quiz_due": "2026-03-22",
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
            "dates": {"start": "2026-03-23", "end": "2026-03-29"},
            "assignment_due": "2026-03-29",
            "assignment_name": "The Reaction Video",
            "topics": [
                "Midterm presentations",
                "Peer review of reaction videos",
                "Discussion of findings"
            ]
        },
        {
            "week": 9,
            "title": "Deepfakes",
            "subtitle": "Is that video real?",
            "unit": "The Future (AI & Tech)",
            "dates": {"start": "2026-03-30", "end": "2026-04-05"},
            "quiz_due": "2026-04-05",
            "topics": [
                "How deepfakes work",
                "Political and personal misuse",
                "Detection and verification"
            ]
        },
        {
            "week": 10,
            "title": "AI Art & The Algorithm",
            "subtitle": "Is it stealing? Why does your feed show you violence?",
            "unit": "The Future (AI & Tech)",
            "dates": {"start": "2026-04-06", "end": "2026-04-12"},
            "quiz_due": "2026-04-12",
            "topics": [
                "How AI art generators work",
                "Artist rights and training data",
                "How recommendation algorithms work",
                "Filter bubbles and radicalization",
                "Platform responsibility"
            ]
        },
        {
            "week": 11,
            "title": "Fake News & Wrap Up",
            "subtitle": "How to spot a lie + Final Prep",
            "unit": "The Wrap Up",
            "dates": {"start": "2026-04-13", "end": "2026-04-17"},
            "assignment_due": "2026-04-17",
            "assignment_name": "The Code Graphic",
            "topics": [
                "Misinformation vs. disinformation",
                "Fact-checking techniques",
                "Media literacy skills",
                "The HBCU Standard - Credibility",
                "Final presentations: The Code Graphic"
            ]
        }
    ],
    
    "assignments": [
        # NOTE: Quiz 1 and Quiz 2 already exist in Canvas (graded)
        # Starting from Quiz 3 with adjusted dates
        {
            "name": "Ethics Check Quiz 3: Privacy",
            "type": "quiz",
            "points": 30,
            "due_date": "2026-02-15T23:59:00",
            "description": "10 multiple-choice questions on Week 3 material about privacy and filming in public."
        },
        {
            "name": "Ethics Check Quiz 4: The Paparazzi",
            "type": "quiz",
            "points": 30,
            "due_date": "2026-02-22T23:59:00",
            "description": "10 multiple-choice questions on Week 4 paparazzi case study."
        },
        {
            "name": "Ethics Check Quiz 5: Ads & Sponsorships",
            "type": "quiz",
            "points": 30,
            "due_date": "2026-03-01T23:59:00",
            "description": "10 multiple-choice questions on Week 5 material about FTC rules and disclosures."
        },
        {
            "name": "Ethics Check Quiz 6: Payola",
            "type": "quiz",
            "points": 30,
            "due_date": "2026-03-08T23:59:00",
            "description": "10 multiple-choice questions on Week 6 material about pay-for-play schemes."
        },
        # Spring Break: Mar 9-15 (no quiz)
        {
            "name": "Ethics Check Quiz 7: Cancel Culture",
            "type": "quiz",
            "points": 30,
            "due_date": "2026-03-22T23:59:00",
            "description": "10 multiple-choice questions on Week 7 material about accountability vs. mob justice."
        },
        {
            "name": "The Reaction Video (Midterm)",
            "type": "assignment",
            "points": 200,
            "due_date": "2026-03-29T23:59:00",
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
            "due_date": "2026-04-05T23:59:00",
            "description": "10 multiple-choice questions on Week 9 material about deepfakes and verification."
        },
        {
            "name": "Ethics Check Quiz 9: AI Art & The Algorithm",
            "type": "quiz",
            "points": 30,
            "due_date": "2026-04-12T23:59:00",
            "description": "10 multiple-choice questions covering AI-generated art, algorithms, and platform responsibility."
        },
        {
            "name": "Ethics Check Quiz 10: Fake News & Media Literacy",
            "type": "quiz",
            "points": 30,
            "due_date": "2026-04-17T23:59:00",
            "description": "10 multiple-choice questions on misinformation, fact-checking, and the HBCU Standard."
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
