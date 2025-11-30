# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    profile = {
        "name": "Văn",
        "title": "Product Designer & Front-end Enthusiast",
        "location": "Nghệ An, Việt Nam",
        "bio": "Mình thiết kế trải nghiệm người dùng tối giản, tập trung vào tính hữu dụng và cảm xúc. Ở đây là nơi mình chia sẻ dự án và suy nghĩ.",
        "avatar": "avatar.jpg",
        "links": [
            {"label": "Email", "url": "mailto:you@example.com"},
            {"label": "GitHub", "url": "https://github.com/yourusername"},
            {"label": "LinkedIn", "url": "https://www.linkedin.com/in/yourusername"},
            {"label": "Dribbble", "url": "https://dribbble.com/yourusername"},
            {"label": "Render App", "url": "https://yourapp.onrender.com"}
        ],
        "skills": ["UX/UI", "Wireframing", "Prototyping", "Design Systems", "HTML/CSS", "Tailwind", "Figma"],
        "projects": [
            {
                "name": "Portfolio 2025",
                "desc": "Hệ thống portfolio modular + dark mode + tốc độ load nhanh.",
                "tags": ["Design System", "Accessibility", "Performance"],
                "link": "https://github.com/yourusername/portfolio-2025"
            },
            {
                "name": "Landing Page A/B",
                "desc": "Thử nghiệm biến thể hero và CTA để tối ưu chuyển đổi.",
                "tags": ["Experiment", "Analytics"],
                "link": "https://github.com/yourusername/landing-ab"
            },
            {
                "name": "UI Components",
                "desc": "Bộ component UI tái sử dụng, chuẩn spacing và typography.",
                "tags": ["Components", "Figma", "CSS"],
                "link": "https://github.com/yourusername/ui-components"
            }
        ]
    }
    return render_template("index.html", profile=profile)
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # Render sẽ cấp PORT qua biến môi trường
    app.run(host="0.0.0.0", port=port, debug=True)
