# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

VibeFinder Lite

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

This recommender suggests songs from a small catalog based on the user’s stated genre, mood, and energy preferences. It is designed for classroom learning and experimentation, not a production music service. It assumes the user can describe their taste with a few simple preferences.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

The model looks at each song’s genre, mood, and energy. It compares those to the user’s favorite genre and preferred energy level. Songs that match genre get a larger bonus, and songs close in energy get a smaller boost. This creates a ranked score list. Mood is noted in the profile, but the current version gives it little or no active scoring power, so genre and energy matter most.

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

The catalog includes 18 songs from `data/songs.csv`. The songs cover genres such as pop, rock, electronic, folk, country, reggae, and metal, with moods like chill, intense, happy, and relaxed. I added new songs for more genre variety, but the dataset is small and misses many real-world styles and detailed listening signals like user history or skips.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

The system works well for users with clear preferences such as high-energy pop or chill lofi. It captures genre and energy similarity reliably, and top recommendations often reflect the expected mood when energy is matched. For example, a pop user with high energy gets energetic pop songs near the top of the ranking.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

The model does not use acousticness or tempo for recommendations, so it misses some important listening preferences. Some genres like metal and country are underrepresented compared to pop and rock. The scoring can overfit to genre because genre matching is weighted strongly. This may favor users with clear genre tastes and hurt users who want a mix of styles.

One weakness I discovered is that the current scoring logic over-prioritizes genre. With a +2.0 bonus for matching genre and no active mood score, the recommender often prefers the same genre even when the user wants a different mood or acoustic style. This can create a filter bubble where users who like cross-genre or mood-driven tastes do not see good options. It also means the model may ignore songs that are a better emotional fit because they are in a different genre.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

I tested profiles such as High-Energy Pop, Chill Lofi, Deep Intense Rock, and edge cases like a pop user with a relaxed mood preference and an electronic user who prefers peaceful, acoustic-style music. I checked whether the top recommendations reflected the stated genre, mood, and energy target, and I verified the explanation strings to make sure the score components matched the ranking logic.  

What surprised me most was that genre matching still dominated the output once mood scoring was disabled, so the system sometimes ranked a less emotionally appropriate pop song above a mood-matching track. I also saw that strong energy similarity could push songs into the top results even when they missed the genre or mood, showing that the weights need better balance. 

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

I would add mood scoring back in and tune the weight between genre and energy. I would also use acousticness and tempo to better reflect listening style. In the future, I would add a diversity boost so top results do not all come from the same genre.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

I learned that simple recommender logic is easy to explain but can still be biased by how the score is weighted. It was interesting to see how genre matching can override mood, even when the user asks for a different feeling. This makes me think music recommendation apps need many signals to find songs that feel right, not just one strong preference.