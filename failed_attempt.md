# Online Image Editor Prototype (Failed Attempt)

## Project Idea
The initial goal was to develop a web-based image editor, similar to Photoshop or Lightroom, but accessible directly from a browser—eliminating the need for software installation. This idea was inspired by my passion for photography and my frequent use of Lightroom.

## Approach & Challenges
1. Connecting to the Lightroom API
Since I was more familiar with Lightroom, I started by integrating its API.
Adobe Creative Cloud provides APIs, but they require a secure HTTPS domain.
To bypass this, I used ngrok to generate a temporary public domain.
Successfully obtained the Lightroom API and started building the app using Streamlit.
2. The API Limitation Surprise
After a few hours of work, I realized that Lightroom’s API only supports asset management, not photo editing.
This meant the API couldn't be used to modify images like the software itself.
Lesson learned: 🚨 Always read API documentation before starting development!
3. Exploring Photoshop Express API
I then looked into Photoshop Express, hoping it would provide the required editing functionalities.
After multiple trials, I discovered that Adobe does not allow direct API calls from external applications.
This was another major roadblock, making my initial project unfeasible.

## Conclusion: Why I Abandoned This Idea
Despite my efforts, the API restrictions made it impossible to achieve the desired functionality.
While frustrating, this experience taught me valuable lessons in:

*Feasibility assessment before coding*
*The importance of API documentation*
*Quick prototyping & failing fast*
