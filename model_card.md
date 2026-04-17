# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

TuneMatch 1.0

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

This recommender system suggests songs based on genre, mood, and energy preferences. It generates ranked lists of songs that match a user's taste profile. It assumes users have fairly simple and consistent preferences that can be represented with a few numeric and categorical features. The system is intended for classroom learning and experimentation, not real-world deployment.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

The recommender system works by comparing each song in the dataset to a user's preferences using a simple scoring system. It looks at three main features, genre, mood, and energy.
Each song gets points based on how well it matches the user. A matching genre adds the most points, a matching mood adds additional points, and energy is scored based on how close the song’s energy value is to the user’s target energy level. These values are added together to create a final score for each song.
The system then ranks all songs from highest to lowest score and returns the top recommendations. Compared to the starter version, this idea adds weighted scoring and explanations so users can understand why each song was recommended.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

The system uses a dataset of 16 songs stored in a CSV file. Each song includes features such as genre, mood, energy, tempo (BPM), valence, danceability, and acousticness.
The dataset includes a mix of genres like pop, lofi, rock, jazz, indie pop, and synthwave. It also includes different moods such as happy, chill, intense, relaxed, moody, and focused.
No songs were removed, but additional songs were added to increase variety. However, the dataset is still small and does not fully represent all types of music, so some user tastes may not be well covered.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

The system works well when user preferences clearly match patterns in the dataset, such as high-energy pop or calm lofi music. It is able to correctly prioritize songs that match multiple features at the same time, especially when genre and mood align.
The scoring system is simple and transparent, which makes it easy to understand why a song was recommended. In many cases, the top results match human intuition, especially for users with consistent and clear preferences.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

The recommender system has a limitation where it can prioritize certain features like genre and energy depending on the weights used in scoring. Because the dataset is small and contains limited diversity across genres, the system may repeatedly recommend similar types of songs, especially pop tracks. This can create a filter-bubble effect where users are not exposed to a wide variety of music. Additionally, users with mixed preferences may not be well represented because the scoring logic treats preferences independently rather than in combination. As a result, the system reflects biases in both the data distribution and the scoring design.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

I tested the recommender using three user profiles, High-Energy Pop, Chill Lofi, and Deep Intense Rock. Each profile gave different rankings, with songs matching genre and energy being consistently prioritized. 
The High-Energy Pop profile returned upbeat pop songs at the top, while the Chill Lofi profile gave recommendations toward slower and more acoustic tracks. The Rock profile gave high-energy and intense songs but sometimes still included pop tracks due to strong energy similarity scores.
What surprised me was how often energy had a strong influence on rankings, sometimes even outweighing genre or mood matches. This showed that small weight changes in the scoring system can significantly affect results and overall recommendations.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

Future improvements could include adding a much larger and more diverse dataset to improve recommendation quality and reduce repetition. The model could also be improved by using machine learning techniques instead of fixed scoring rules to better capture complex user preferences.
Another improvement would be adding a diversity feature so the system does not recommend very similar songs repeatedly. It could also include more user features such as tempo preference ranges or listening history.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

This project helped me understand how recommender systems turn simple user preferences into ranked outputs using scoring rules. I learned that even small changes in weights can significantly change the recommendations.
One surprising part was how realistic the results can feel even with a simple algorithm. Using AI tools helped me design and debug faster, but I still had to carefully check that the logic made sense. If I continued this project, I would expand the dataset and experiment with more advanced recommendation methods.