"""""
國泰補習班中，有五位學生期中考的成績分別為[53,64,75,19,92],
但是老師在輸入成績的時候看反了，
把五位學生的成績改成了[35,46,57,91,29],
請用一個函數來將學生成績修正
"""

def correct_scores (wrong_scores): #定義正確分數的操作
    correct_score_list=[] #建立空白表格
    for wrong_score in wrong_scores:  #for 迴圈逐一把錯誤分數修正
        correct_scores = int(str(wrong_score)[::-1]) #[::-1]有顛倒作用，先改為字串才能顛倒，再轉回數字
        correct_score_list.append(correct_scores) #添加到空白表格
    return correct_score_list #返回值

wrong_scores = [35,46,57,91,29]
correct_scores = correct_scores (wrong_scores) #啟用def
print("修正後成績列表",correct_scores)


"""""
國泰銀行要慶祝六十周年，
需要買字母貼紙來布置活動空間，
文字為"Hello welcome to Cathay 60th year anniversary"，
請寫一個程式計算每個字母(大小寫視為同個字母)出現次數
"""

def count_letters(word): #定義以下
    count_letters = {} #建立字典
    word=word.lower() #改為小寫
    for letter in word: #for 迴圈，計算word裡letter出現次數，經在count_letters有就+1沒有就為1
        if letter in count_letters:
            count_letters[letter] += 1
        else:
            count_letters[letter] = 1
    return count_letters

#word=input("請輸入文字:") #做成可輸入的狀態
word="Hello welcome to Cathay 60th year anniversary"
result = count_letters(word) #結果=def
for letter , count in result.items(): #逐一寫下並顯示
    print("%s %s" % (letter, count)) #寫下並指定為字串取用letter和count


"""""
QA部門今天舉辦團康活動，
有n個人圍成一圈，
順序排號。
從第一個人開始報數（從1到3報數），
凡報到3的人退出圈子。
請利用一段程式計算出，
最後留下的那位同事，
是所有同事裡面的第幾順位?
"""

def find_last_person(n): #定義
    people= list(range(1,n+1)) #人數範圍為1到N
    index= 0 #起時位置
    while len(people)>1: #當人數>1
        index = (index+2)%len(people) # index=總人數除於3
        del people[index] #去除這些在列表第三的人
    return people[0] #回傳回表內

n=int(input("請輸入團康人數:")) #輸入N值為團康人數
last_person=find_last_person(n) #呼叫def運算
print(last_person) #輸出結果