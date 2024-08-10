# **Introduction:**
Odessa is a chatbot application for the healthcare industry that utilizes a conversational approach 
to assist the user of the app in learning more about diseases and physical injuries, certain symptoms they are going 
through, and conditions that they may be aware of as a result of the chatbot. That being said, Odessa aims to help users
educate themselves on common diseases and physical injuries, in addition to helping the user self-diagnose themselves. 

## **Disclaimer:**
Keep in mind that Odessa is not an alternative to seeing an actual doctor. Please seek the 
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



## **How is User Data Being Handled?**
Odessa currently only collects a user's name. This name will be used when Odessa replies back to the user. It will be 
in this format: "{Name}: ...". In the near future, when I implement memory into Odessa, chat history 
between the user and Odessa will be stored during each session. However, besides the user's name, Odessa cannot access
anything else from the user. 

The user also does not have to worry about privacy concerns. 


## **How Do I Use Odessa?**
Upon loading up the Odessa application, the user will see the chat and the entire interface of Odessa load up. There is 
a field at the bottom where the user can enter some input to start the conversation with Odessa. Keep in mind that the 
user has to type some text and then press enter or click "Send" on the screen. From here, Odessa will respond to the 
user, and the conversation with the AI will begin. The user can continue to ask or add text into the input field from 
here. 



## **Testing Guide:**
When it comes to testing, I included a testing file in my project that tested a majority of the functions and methods 
that appeared in the code. I am currently in the process of understanding how to test one of the final methods, which 
involves mocking so that I can test random selections within the json file. I also included preliminary tests 
throughout the project so that I could see if some functions were working correctly right after their creation. 

Back to the testing file, I made various variables containing common and edge cases. From here, I created similar 
function and method calls as the original ones but added the word "test" in front. From here, I used to the assert 
keyword to determine if a test is correct or false. 

After going through rigorous testing, I was able to determine that some of the tests, as I have mentioned, are difficult
to implement. For instance, the get_message function is easy to test with questions that only contain one response. 
However, I have to use mocking in order to test cases where a question or discussion lead to several possible answers. 
The execution of these tests proved to be extensive and complex for random-response generation.

Despite the rough testing caused by the get_message function, I grew a lot more experience in working with mocking 
techniques to test the random selection of responses for chatbots and other programs utilizing similar processes.



## **Odessa's Limitations and Room for Improvement:**
Odessa has several limitations. Firstly, there are not too many diseases and physical injuries to choose from (twelve 
conditions, at the moment). As a result, a user may not be able to accurately predict an illness or physical injury they 
may have. Secondly, sometimes Odessa has a hard time figuring out what a user may be asking it, so "I do not understand. 
Could you please clarify?" appears a bit. Thirdly, Odessa is a great tool to use for learning about certain diseases and 
physical injuries, but getting to this point via a conversation is hard because the discussion of symptoms is a little 
complicated; Odessa can list symptoms for certain problems, but it cannot evaluate a user's symptoms and throw out a 
conclusion, especially without further testing that a physical doctor could get done. 

I believe there are a plethora of ways to improve this application. Firstly, I would like to integrate a memory feature
using LangChain so that the chatbot can understand, not instantly drop whatever a user has just told it, and employ that 
information to reach a conclusion. This would result in better discussions in understanding diseases and physical 
injuries a user may have. LangChain would especially help with the transition from a discussion of symptoms to the 
discussion of what a user has in detail, along with, say, treatment or prevention options.

I would also be open to adding more diseases and physical conditions, but I think a more practical thing to do would be 
to turn Odessa into an LLM so that I can integrate web surfing techniques more smoothly and use that to do less work to 
find conditions and elaborate on symptoms and prevention options. A transition from a basic chatbot to an LLM would 
surely aid in preventing Odessa from not being to understand a question such as, "What is a concussion?"



## **Programming Tools and Other Technical Features:**
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