## **Introduction**

Odessa is a chatbot application for the healthcare industry that utilizes a conversational approach 
to assist the user of the app in learning more about certain symptoms they are going through and conditions 
that they may be aware of as a result of the chatbot. That being said, Odessa aims to help users self-diagnose 
themselves. However, keep in mind that I, Odessa, and not an alternative to seeing an actual doctor. Please seek the 
correct and appropriate medical professionals so that you can receive proper diagnosis and treatment.



## **What Is the Motivation Behind the Project?"**
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
1. M
2. M
3. M
4. M
5. M
6. M
7. M
8. M
9. M
10. M
11. m
12. m
13. m
14. m
15. m
16. m
17. m
18. m
19. m
20. m
21. m
22. m
23. m
24. m
25. m
26. m
27. m
28. m
29. m
30. m