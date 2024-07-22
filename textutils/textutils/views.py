from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def about(request):
    return HttpResponse('''<main style="padding: 20px;">
        <section style="background-color: white; padding: 20px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
            <h2 style="color: #333;">Who Am I?</h2>
            <p style="color: #666; line-height: 1.6;">
                Hello! I'm a passionate web developer with a knack for creating intuitive and dynamic user experiences. 
                My journey in web development began a few years ago, and since then, I've been dedicated to mastering 
                both front-end and back-end technologies.
            </p>
        </section>

        <section style="background-color: white; padding: 20px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); margin-top: 20px;">
            <h2 style="color: #333;">My Background</h2>
            <p style="color: #666; line-height: 1.6;">
                I have a background in computer science and a deep interest in how technology can solve real-world problems. 
                Throughout my career, I have worked on various projects, from small business websites to large-scale applications. 
                My expertise lies in JavaScript, React, Node.js, and other modern web development tools.
            </p>
        </section>

        <section style="background-color: white; padding: 20px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); margin-top: 20px;">
            <h2 style="color: #333;">My Interests</h2>
            <p style="color: #666; line-height: 1.6;">
                When I'm not coding, I enjoy exploring new technologies, reading about advancements in AI, 
                and contributing to open-source projects. I also love hiking, photography, and traveling to 
                experience different cultures and cuisines.
            </p>
        </section>
    </main>

    <footer style="background-color: #333; color: white; text-align: center; padding: 10px 0; position: absolute; width: 100%; bottom: 0;">
        <p style="margin: 0;">&copy; 2024 About Me. All rights reserved.</p>
    </footer>''');
def info(response):
    return HttpResponse('''<h1><a href="https://github.com/">Info about page</a></h1>  <section style="background-color: white; padding: 20px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
            <h2 style="color: #333;">About Me</h2>
            <p style="color: #666; line-height: 1.6;">
                Hello! I am a web developer with a passion for creating beautiful and functional websites. 
                I have experience in HTML, CSS, JavaScript, and various front-end and back-end frameworks. 
                I love to learn and explore new technologies and continuously improve my skills.
            </p>
        </section>

        <section style="background-color: white; padding: 20px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); margin-top: 20px;">
            <h2 style="color: #333;">My Skills</h2>
            <ul style="color: #666; line-height: 1.6; padding-left: 20px;">
                <li>HTML & CSS</li>
                <li>JavaScript</li>
                <li>React.js</li>
                <li>Node.js</li>
                <li>Express.js</li>
                <li>MongoDB</li>
            </ul>
        </section>

        <section style="background-color: white; padding: 20px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); margin-top: 20px;">
            <h2 style="color: #333;">Contact Me</h2>
            <p style="color: #666; line-height: 1.6;">
                Feel free to reach out to me via email at <a href="mailto:someone@example.com" style="color: #4CAF50;">someone@example.com</a>.
            </p>
        </section>''');
def removepunc(request):
    text=request.GET.get('text','default')
    return HttpResponse("remove punctuation");
def capfirst(request):
    return HttpResponse("Capitalize");