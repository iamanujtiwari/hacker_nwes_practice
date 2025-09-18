# 📌 Hacker News Data Filter

### 📝 Introduction
This is a small Python project that works with a dataset (`hacker_news.csv`) containing Hacker News article details.  
The project allows users to filter and find specific information like:
- Articles with the word **"Python"** in the title.  
- Articles where the URL contains **"Amazon"**.  

---

### ⚙️ Features
- ✅ Filter by keyword → Search for "Python" in article titles.  
- ✅ Filter by domain → Search for "Amazon" in article URLs.  
- ✅ Count results → Displays total number of matches.  
- ✅ User input menu → Simple CLI-based menu for user choice.  

---

### 🗂️ File Structure
project-folder/
│── hacker_news.csv # Dataset file
│── filter_hn.py # Python script for filtering
│── README.md # Project overview file



### 🖥️ How It Works
1. The program asks the user to choose an option:  
   - `1` → Find Amazon in URL  
   - `2` → Find Python in Title  

2. According to the choice, it scans the CSV file using **csv.DictReader**.  
3. Matching results are displayed one by one with numbering.  
4. Finally, the total count is shown.

---

### 📊 Example Output
Python releases new version
<img width="924" height="483" alt="image" src="https://github.com/user-attachments/assets/d64428e7-a1ac-4064-a5fa-026598b08bb5" />


Best Python frameworks for beginners
Total Python titles: 2

### 📸 Screenshots

**Project Folder Structure:**  
<img width="962" height="162" alt="image" src="https://github.com/user-attachments/assets/f4b62b4c-cc47-4e11-9070-4f6490c32bf6" />



**Program Running Example:**  
<img width="944" height="198" alt="image" src="https://github.com/user-attachments/assets/a096776e-e7ee-40ff-82ff-83989bc58f12" />
<img width="924" height="483" alt="image" src="https://github.com/user-attachments/assets/6ab4fed0-0e0c-40f5-818d-4292976f17b6" />


 

**Sample CSV File:**  
<img width="1306" height="606" alt="image" src="https://github.com/user-attachments/assets/aee9744e-8243-4af1-81e0-02d097811366" />


### 👨‍💻 Author
Created by **Anuj Tiwari**
