from django.shortcuts import render

# 사용자 요청이 들어올 시 index.html 렌더
def index(request) :
    return render(request, 'index.html')

# word count가 동작하는 핵심 부분
def result(request) :
    sentence = str(request.POST.get("sentence"))
    sentence_to_list = sentence.split()
    
    dic = {}
    
    for word in sentence_to_list:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
            
    # [(key1, value2), (key2, value2)] 형태로 저장
    word_count = list(dic.items())
    
    # 요청이 들어올 시 result.html, word_count 렌더
    return render(request, 'result.html', {'word_count':word_count})

