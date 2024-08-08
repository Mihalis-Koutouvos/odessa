## **Introduction**

Odessa is a chatbot application for the healthcare industry that utilizes a conversational approach 
to assist the user of the app in learning more about certain symptoms they are going through and conditions 
that they may be aware of as a result of the chatbot. That being said, Odessa aims to help users self-diagnose 
themselves. However, keep in mind that I, Odessa, and not an alternative to seeing an actual doctor. Please seek the 
correct and appropriate medical professionals so that you can receive proper diagnosis and treatment.



## **What Is the Motivation Behind the Project?**
After my first year at Northeastern University, I had gained so many insights into the plentiful list of fields computer 
science has influences in. However, I wanted to dive deeper into a few of these specializations, especially within 
healthcare. 

For some context, I originally did not want to go into computer science; my intentions were to go to medical school and 
become some sort of surgeon. Due to the long financial journey this would have caused me, I decided to step away from 
the idea of going into medical school, which extremely bummed me out. Nevertheless, after picking up programming around 
my first and second years of high school, I developed a greater love for computers. I had one of the original Mac 
laptops, a gift from my father, and that computer worked like a charm for many years. I was able to play games like 
Roblox, gain experience using tools like the Google Search, and watch videos on YouTube about virtually everything. Even
though medical school did not work out, I had computers ready to take me into their pixelated realm. 

Back to reality, I decided to build a chatbot for the healthcare industry using Python. This project allowed me to not 
only code and learn more about tools and processes such as PyTorch, machine/deep learning, and natural language 
processing, but it also allowed me to research illnesses and injuries. I love learning, so I thoroughly reseached as much 
information as I could in an efficient manner to go about this project. At the end of the day, this mutli-field project
permitted me to comprehend how crucial patience is when it comes to programming at this level and going forward and how 
almost any field can utilize the help of computers and artificial intelligence to improve the lives of humans around the 
world. 



## **What Is the Step-by-Step Process behind the Project?**
In order to create Odessa, I did some thorough research into chatbots and how to implement them effectively. For this 
style of chatbot, I figured out that a bag-of-words approach would be best. 

Firstly, the AI would tokenize the text provided by a user's input. In this case, tokenization means that each word and 
any symbols will be separated as if they are their own sentences; think of this as splitting a string into several 
parts. For example, if I have the sentence, "I have a headache.", then a tokenized version would look like so: ["I", 
"have", "a", "headache", "."].

Secondly, Odessa will take each word and stem it so that the root version of the word appears. For instance, prepares 
would become prepar.

Thirdly, Odessa will compare all the possible words with the given string from the user. The comparison is done against
all the words within the json file, with each word only appearing once within the comparison list. For instance, if a 
word in the given list is available in the list with all the words, then a 1. is inputted into the array; if not, then
a 0. is used. Whatever Odessa determines to be the closest response match within the json file will be its output. 

From here, Odessa sends its response to the user in less than a second. Both the user and Odessa's responses can be 
seen within the centered, main section of the GUI.


## **Programming Tools and Other Technical Features**

To begin, Odessa was coded in Python. However, to actually train the data that I used, Pytorch came in handy, alongside 
libraries including NumPy, NLTK, json, and random; I also employed the Tkinter library to design the GUI behind Odessa. 
For the heavy features, I used PyCharm CE as my IDE and Miniconda as a separate environment. 


All the information that I am providing you regarding ailments and physical injuries is provided by the Centers For 
Disease Control and Prevention and other credible sources such as publications by Yale Medicine. Here are all of the 
sources that I ended up using: 
1. Cold Prevention: https://www.yalemedicine.org/conditions/colds
2. Cold Definition, Symptoms: https://www.cdc.gov/common-cold/about/index.html
3. Flu Definition, Prevention: https://www.cdc.gov/flu/about/index.html#:~:text=Influenza%20(flu)%20is%20a%20contagious,risk%20of%20serious%20flu%20complications.
4. Flu Symptoms: https://www.cdc.gov/flu/symptoms/index.html#:~:text=Influenza%20(also%20known%20as%20%E2%80%9Cflu,symptoms%2C%20complications%2C%20and%20diagnosis.
5. COVID-19 Symptoms, Prevention: https://www.hopkinsmedicine.org/health/conditions-and-diseases/coronavirus/diagnosed-with-covid-19-what-to-expect#:~:text=You%20may%20have%20fever%2C%20cough,but%20do%20have%20COVID%2D19
6. COVID-19 Definition: https://www.who.int/health-topics/coronavirus#tab=tab_1
7. COVID-19 vs Flu: https://www.cdc.gov/flu/symptoms/flu-vs-covid19.htm
8. Gastroenteritis Definition, Symptoms, Prevention: https://www.yalemedicine.org/conditions/gastroenteritis
9. Viral Gastroenteritis: https://www.mayoclinic.org/diseases-conditions/viral-gastroenteritis/symptoms-causes/syc-20378847
10. Sinus Infection Definition, Symptoms, Prevention: https://my.clevelandclinic.org/health/diseases/17701-sinusitis, https://www.pennmedicine.org/for-patients-and-visitors/patient-information/conditions-treated-a-to-z/sinus-infections-sinusitis#:~:text=Definition,virus%2C%20bacteria%2C%20or%20fungus
11. Pneumonia Definition, Symptoms, Prevention: https://www.hopkinsmedicine.org/health/conditions-and-diseases/pneumonia, https://my.clevelandclinic.org/health/diseases/4471-pneumonia
12. Headache Definition, Symptoms, Prevention: https://www.hopkinsmedicine.org/health/conditions-and-diseases/headache, https://my.clevelandclinic.org/health/diseases/9639-headaches 
13. Concussion Definition, Symptoms, Prevention: https://my.clevelandclinic.org/health/diseases/15038-concussion, https://www.uofmhealth.org/conditions-treatments/pediatric-brain-neurological/brain-neurological-conditions/concussion
14. Bone Fracture Definition, Symptoms, Prevention: https://my.clevelandclinic.org/health/diseases/15241-bone-fractures, https://www.hopkinsmedicine.org/health/conditions-and-diseases/fractures, https://northazortho.com/ask-the-expert/everything-you-need-to-know-about-fractures-and-fracture-healing/#:~:text=How%20Long%20Does%20a%20Fracture,take%2020%20weeks%20or%20more.
15. Muscle Strain Definition, Symptoms, Prevention: https://www.health.harvard.edu/a_to_z/muscle-strain-a-to-z
16. Sprain Definition: https://www.urmc.rochester.edu/conditions-and-treatments/sprains
17. Sprain Definition, Symptoms, Prevention: https://my.clevelandclinic.org/health/diseases/sprains